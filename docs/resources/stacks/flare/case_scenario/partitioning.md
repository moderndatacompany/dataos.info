# Partitioning


Partitioning is a technique used to improve query performance by grouping similar rows together when writing data. This approach helps speed up query processing by organizing data into partitions based on specific criteria.

<!-- 
This use case checks how partitioning works for Flare while writing data to Iceberg and non-Iceberg type data storage (Parquet, Kafka) to improve query processing performance. -->

This use case demonstrates how partitioning works in Flare when writing data to Iceberg and non-Iceberg data storage formats (e.g., Parquet and Kafka) to optimize query performance.

## Iceberg partitioning

Iceberg supports partitioning based on timestamp granularity such as year, month, day, and hour, as well as categorical columns (e.g., vendor ID) with data types like string, integer, long, and potentially double (to be verified). Partitioning helps group rows together and speeds up query performance.

Iceberg produces partition values by taking a column value and optionally transforming it. For example, it converts timestamp values into dates and extracts components such as year, month, day, hour, etc.

<!-- 

Iceberg can partition timestamps by year, month, day, and hour granularity. It can also use a categorical column of data type- string, integer, long, ***double (to be checked)***, to store rows together and speed up queries, e.g., like vendor ID in this example. 

Iceberg produces partition values by taking a column value and optionally transforming it. Iceberg converts timestamp values into a date, and extracts year, month, day, hour, etc.

While in non-Iceberg data sink, partitions are explicit and appear as a separate column in the table that must be supplied in every table write operation. For example, you need to provide the columns explicitly for the year, month, hour as a transformation from the timestamp column is not automatic.

You need to provide a categorical column as a partition criterion for non-Iceberg formats such as Parquet. -->

## Non-Iceberg Partitioning (e.g., Parquet, Kafka)

In non-Iceberg data formats(such as Parquet), partitions are explicit and appear as a separate column in the table that must be supplied in every table write operation. For example, you need to provide the columns explicitly for the year, month, hour as a transformation from the timestamp column is not automatic.

For non-Iceberg formats such as Parquet, you are required to provide a categorical column as the partitioning criterion.

## Implementation details

The following examples demonstrate the use of various partitioning modes.

### **Iceberg**

- Partition using type identity
    - Integer values
    - String values
- Partition using type timestamp
    - Year
    - Month
    - Day
    - Hour

**Example 1:** Partitioning by identity is used when a categorical column (e.g., vendor_id) is used to group data. When using an identity type, there is no need to specify the property name for the partition.

```yaml
partitionSpec:
    - type: identity    **# options tested: identity, year, month, day, hour**
      column: vendor_id **# columns used - identity (vendor_id, one string column) & for rest date_col**
```

**Example 2:** In this example, partitioning is done by year using a timestamp column (date_col). Iceberg will automatically extract the year from the timestamp.

```yaml
partitionSpec:
    - type: year       **# options tested: identity, year, month, day, hour**
      column: date_col **# columns used - identity (vendor_id, one string column) & for rest date_col of type timestamp**
      name: year
```

**Example 3:** This example demonstrates nested partitioning, where data is first partitioned by social_class (identity type), followed by partitioning by year (`timestamp` type). The social_class must come first in the partition specification.

```yaml
partitionSpec:
    - type: identity  
      column: vendor_id   **# columns used - identity (vendor_id, one string column) & for rest date_col**

    - type: year          **# options tested: identity, year, month, day, hour**
      column: date_col  
      name: year
```

### **Parquet**

- Partition using type identity

**Example 1: Partitioning is done on identity by taking the vendor_id column.**

```yaml
- sequence:
  - name: ny_taxi_ts
    outputType: Parquet
    outputOptions:
    saveMode: overwrite
    partitionBy:
      - vendor_id
```


<!-- ```yaml
- sink:
 - sequenceName: ny_taxi_ts
    datasetName: ny_taxi_parquet_06
    outputName: output01
    outputType: Parquet
    outputOptions:
    saveMode: overwrite
    partitionBy:
      - vendor_id
``` -->

## Outcomes

The files will be stored in the folders based on the partition criterion defined, and you can view them in workbench or storage locations.

## Code files

> **Note**: When specifying the partition criterion for Iceberg, the 'partitionSpec' property should be defined as a child property under 'iceberg' in the sink section. Otherwise partitioning will not be performed as desired.
> 

```yaml
version: v1
name: workflow-ny-customer-partitioned-03
type: workflow
tags:
- Connect
- NY-Taxi
workspace: curriculum
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
      stack: flare:6.0
      compute: runnable-default
      stackSpec:
        job:
          explain: true
          inputs:
           - name: customer
             dataset: dataos://icebase:retail/customer?acl=r
             format: Iceberg
             isStream: false

          logLevel: INFO
          outputs:
            - name: ts_customer
              dataset: dataos://icebase:sample/partioning03?acl=rw
              format: Iceberg
              description: This is a customer dataset
              options:
                 saveMode: overwrite
                 iceberg:
                  properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: identity      # options tested: string, integer, long**
                      column: social_class   # columns used - identity (vendor_id, one string column)** 

                    - type: year      # options tested: string, integer, long**
                      column: birthdate   # columns used - identity (vendor_id, one string column)** 
                      name: yearly
              tags:
                  - Connect
                  - customer
              title: customer Data Partitioned Vendor


          steps:
            - sequence:
              - name: ts_customer
                sql: SELECT *  FROM customer;
```