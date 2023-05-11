# Partitioning

Partitioning is a way to make queries faster by grouping similar rows together when writing.

This use case checks how partitioning works for Flare while writing data to Iceberg and non-Iceberg type data storage (Parquet, Kafka) to improve query processing performance.

This use case describes data partitioning with partition keys of different data types for Iceberg and Parquet formats.

Iceberg can partition timestamps by year, month, day, and hour granularity. It can also use a categorical column of data type- string, integer, long, *double (to be checked)*, to store rows together and speed up queries, e.g., like vendor ID in this example. 

Iceberg produces partition values by taking a column value and optionally transforming it. Iceberg converts timestamp values into a date, and extracts year, month, day, hour, etc.

While in non-Iceberg data sink, partitions are explicit and appear as a separate column in the table that must be supplied in every table write operation. For example, you need to provide the columns explicitly for the year, month, hour as a transformation from the timestamp column is not automatic.

You need to provide a categorical column as a partition criterion for non-Iceberg formats such as Parquet.

## Implementation details

The following examples demonstrate the use of various partitioning modes.

### Iceberg

- Partition using type identity
    - Integer values
    - String values
- Partition using type timestamp
    - Year
    - Month
    - Day
    - Hour

Example 1: Partitioning is done on identity by taking the vendor_id column. You don't need to provide the property name if the partition field type is identity type.

```yaml
partitionSpec:
    - type: identity    # options tested: identity, year, month, day, hour
      column: vendor_id # columns used - identity (vendor_id, one string column) & for rest date_col
```

Example 2: Partitioning is done on the year.

```yaml
partitionSpec:
    - type: year       # options tested: identity, year, month, day, hour
      column: date_col # columns used - identity (vendor_id, one string column) & for rest date_col of type timestamp
      name: year
```

Example 3: Nested partitioning is done on (identity, year). Here, the vendor_id used for identity should come at the first level.

```yaml
partitionSpec:
    - type: identity  
      column: vendor_id   # columns used - identity (vendor_id, one string column) & for rest date_col

    - type: year          # options tested: identity, year, month, day, hour
      column: date_col  
      name: year
```

### Parquet

- Partition using type identity

Example 1: Partitioning is done on identity by taking the vendor_id column.

```yaml
- sink:
 - sequenceName: ny_taxi_ts
    datasetName: ny_taxi_parquet_06
    outputName: output01
    outputType: Parquet
    outputOptions:
    saveMode: overwrite
    partitionBy:
      - vendor_id
```

## Outcomes

The files will be stored in the folders based on the partition criterion defined, and you can view them in workbench or storage locations.

## Code files

> 📌 Note: When specifying the partition criterion for Iceberg, the 'partitionSpec' property should be defined as a child property under 'iceberg' in the sink section. Otherwise partitioning will not be performed as desired.
> 

```yaml
version: v1beta1
name: workflow-ny-taxi-partitioned-vendor
type: workflow
tags:
- Connect
- NY-Taxi
description: The job ingests NY-Taxi data small files and write with partitioning on vendor_id
workflow:
  title: Connect NY Taxi
  dag:
  - name: nytaxi
    title: NY-taxi data ingester
    description: The job ingests NY-Taxi data from dropzone into raw zone
    spec:
      tags:
      - Connect
      - NY-Taxi
      stack: flare:1.0
      flare:
        job:
          explain: true
          inputs:
           - name: ny_taxi
             dataset: dataos://thirdparty01:none/ny-taxi-data?acl=r
             format: json
             isStream: false

          logLevel: INFO
          outputs:
            - name: output01
              depot: dataos://icebase:raw01?acl=rw
          steps:
          - sink:
             - sequenceName: ny_taxi_ts
               datasetName: ny_taxi_07
               outputName:  output01
               outputType: Iceberg
               outputOptions:
                 saveMode: overwrite
                 iceberg:
                  properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: identity      # options tested: string, integer, long
                      column: vendor_id   # columns used - identity (vendor_id, one string column) 

                    - type: year          # options tested: identity, year, month, day, hour
                      column: date_col    # columns used - identity (vendor_id, one string column) & for rest date_col
                      name: year

               tags:
                  - Connect
                  - NY-Taxi
               title: NY-Taxi Data Partitioned Vendor

            sequence:
              - name: ny_taxi_changed_dateformat
                sql: select *, to_timestamp(pickup_datetime/1000) as date_col from ny_taxi

              - name: ny_taxi_ts
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                  ts_ny_taxi FROM ny_taxi_changed_dateformat
```