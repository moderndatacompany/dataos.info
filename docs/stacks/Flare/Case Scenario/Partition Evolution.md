# **Partition Evolution**

This article describes a use case of partition evolution for Iceberg and shows how seamless it is to query the data stored with multiple partition layouts.

You can update the Iceberg table partitioning in an existing table because queries do not refer to partition values directly.

Iceberg makes partitioning simple by implementing hidden partitioning. You need not supply a separate partition filter at query time. The details of partitioning and querying are handled by Iceberg automatically. That is why even when you change the partition spec, your queries do not break.

For example, a simple query like this is capable of fetching data from multiple partition spec:

```yaml
Select * from NY-Taxi where date_col > 2010-10-23 AND date_col < 2013-01-01
```

You do not need to understand the physical table layout to get accurate query results. Iceberg keeps track of the relationships between a column value and its partition.

# **Solution approach**

When you evolve a partition spec, the old data written with an earlier partition key remains unchanged, and its metadata remains unaffected. New data is written using the new partition key in a new layout. Metadata for each of the partition versions is kept separately. When you query, each partition layout’s respective metadata is used to identify the files it needs to access; this is called split-planning.

# **Implementation details**

The NY Taxi data is ingested and is partitioned by year. When the new data is appended, the table is updated so that the data is partitioned by day. Both partitioning layouts can co-exist in the same table.

Iceberg uses hidden partitioning, so you don’t need to write queries for a specific partition layout. Instead, you can write queries that select the data you need, and Iceberg automatically scans files containing matching data referring to partition layouts.

Partition evolution is a metadata operation and does not rewrite files.

The following steps demonstrate the partition evolution use case.

## **Ingest data with initial partition**

Run the following Flare job that ingests data into DataOS with the partition on year.

```yaml
---
version: v1beta1
name: workflow-ny-taxi
type: workflow
tags:
- Connect
- NY-Taxi
description: The job ingests NY-Taxi data and write with partitioning on year
workflow:
  title: Connect NY Taxi
  dag:
  - name: nytaxi-ingest-partition-update
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
             dataset: dataos://thirdparty01:none/ny-taxi-data/010100.json?acl=r
             format: json
             isStream: false
          logLevel: INFO
          outputs:
            - name: output01
              depot: dataos://icebase:raw01?acl=rw
          steps:
          - sink:
             - sequenceName: ny_taxi_ts
               datasetName: ny_taxi_partition_01
               outputName:  output01
               outputType: Iceberg
               outputOptions:
                 saveMode: overwrite
                 iceberg:
                   properties:
                     write.format.default: parquet
                     write.metadata.compression-codec: gzip
                   partitionSpec:
                     - type: year
                       column: pickup_datetime
                       name: year
               tags:
                  - NY-Taxi
                  - Connect
               title: NY-Taxi Data
            sequence:
              - name: ny_taxi_ts
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as ts_ny_taxi FROM ny_taxi
                functions:
                  - name: set_type
                    columns:
                      pickup_datetime: timestamp
                      dropoff_datetime: timestamp
```

## **Update metadata with data tool**

Run the following datatool job to update the metadata in DataOS.

```yaml
version: v1beta1
name: dataos-tool-ny-taxi-connect
type: workflow
workflow:
  dag:
  - name: dataos-tool-partition
    spec:
      stack: toolbox
      toolbox:
        dataset: dataos://icebase:raw01/ny_taxi_partition_01
        action:
          name: set_version
          value: latest
```

## **Update partition for new data**

Run the following datatool job to update the partition spec for the new data to be ingested.

```yaml
version: v1beta1
name: dataos-tool-update-partition
type: workflow
workflow:
  dag:
  - name: dataos-tool-partition-update
    spec:
      stack: alpha
      envs:
        LOG_LEVEL: debug
      alpha:
        image: rubiklabs/dataos-tool:0.2.3
        arguments:
          - dataset
          - update-partition
          - --address
          - dataos://icebase:raw01/ny_taxi_partition_01
          - --spec
          - day:pickup_datetime
```

## **Append data with new partition spec**

Run the following Flare job that appends data into DataOS with the updated partition on ‘day’.

```yaml
---
version: v1beta1
name: workflow-ny-taxi-updatepartition
type: workflow
tags:
- Connect
- NY-Taxi
description: The job ingests NY-Taxi data and write with updated partitioning on Day
workflow:
  title: Connect NY Taxi
  dag:
  - name: nytaxi-ingest-partition-update
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
             dataset: dataos://thirdparty01:none/ny-taxi-data/010100.json?acl=r
             format: json
             isStream: false
          logLevel: INFO
          outputs:
            - name: output01
              depot: dataos://icebase:raw01?acl=rw
          steps:
          - sink:
             - sequenceName: ny_taxi_ts
               datasetName: ny_taxi_01
               outputName:  output01
               outputType: Iceberg
               outputOptions:
                 saveMode: append
                 iceberg:
                   properties:
                     write.format.default: parquet
                     write.metadata.compression-codec: gzip
                   partitionSpec:
                     - type: day
                       column: pickup_datetime
                       name: day
               tags:
                  - NY-Taxi
                  - Connect
               title: NY-Taxi Data
            sequence:
              - name: ny_taxi_ts
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as ts_ny_taxi FROM ny_taxi
                functions:
                  - name: set_type
                    columns:
                      pickup_datetime: timestamp
                      dropoff_datetime: timestamp
```