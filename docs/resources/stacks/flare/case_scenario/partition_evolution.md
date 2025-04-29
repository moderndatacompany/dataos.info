# Partition Evolution


The following document explains about a feature in Iceberg called partition evolution and explains how it allows you to change the way your data is organized (partitioned) without causing issues when you run queries on that data.


You can update the Iceberg table partitioning in an existing table because queries do not refer to partition values directly.

Iceberg makes partitioning simple by implementing hidden partitioning. You need not supply a separate partition filter at query time. The details of partitioning and querying are handled by Iceberg automatically. That is why even when you change the partition spec, your queries do not break.

For example, a simple query like this is capable of fetching data from multiple partition spec:

```yaml
Select * from NY-Taxi where date_col > 2010-10-23 AND date_col < 2013-01-01
```

You do not need to understand the physical table layout to get accurate query results. Iceberg keeps track of the relationships between a column value and its partition.

## Solution approach

When you evolve a partition spec, the old data written with an earlier partition key remains unchanged, and its metadata remains unaffected. New data is written using the new partition key in a new layout. Metadata for each of the partition versions is kept separately. When you query, each partition layout’s respective metadata is used to identify the files it needs to access; this is called split-planning.

## Implementation details

The NY Taxi data is ingested and is partitioned by year. When the new data is appended, the table is updated so that the data is partitioned by day. Both partitioning layouts can co-exist in the same table.

Iceberg uses hidden partitioning, so you don’t need to write queries for a specific partition layout. Instead, you can write queries that select the data you need, and Iceberg automatically scans files containing matching data referring to partition layouts.

Partition evolution is a metadata operation and does not rewrite files.

The following steps demonstrate the partition evolution use case.

### **Ingest data with initial partition**

Run the following Flare job that ingests data into DataOS with the partition on year.

```yaml
version: v1
name: wf-storage-event-context
type: workflow
tags:
  - NY-Taxi
  - Connect
  - Tier.Gold
description: The job ingests NY-Taxi data and writes it with partitioning on year, using an updated workflow spec.
workflow:
  title: NY Taxi Data Ingestion
  dag:
    - name: storage-event-context
      description: The job ingests NY-Taxi data from dropzone into Icebase with enhanced metadata configuration.
      title: NY Taxi Ingestion
      spec:
        tags:
          - NY-Taxi
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 2500m
            cores: 2
            memory: 3048m
          executor:
            coreLimit: 3500m
            cores: 2
            instances: 2
            memory: 4000m
          job:
            explain: true
            inputs:
              - name: ny_taxi_dataset
                dataset: dataos://lakehouse:none/ny-taxi-data/customer?acl=r
                format: Iceberg
            logLevel: INFO
            outputs:
              - name: final
                dataset: dataos://lakehouse:sample/customer_partition_evolution?acl=rw
                format: Iceberg
                description: Partitioned NY-Taxi dataset output
                tags:
                  - NY-Taxi
                options:
                  saveMode: overwrite
                  sort:
                    mode: partition
                    columns:
                      - name: pickup_datetime
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: year
                        column: pickup_datetime
                        name: year
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                title: NY-Taxi Dataset Partitioned Output
            steps:
              - sequence:
                  - name: final
                    sql: |
                      SELECT
                        *,
                        date_format(now(), 'yyyyMMddHHmm') as version,
                        now() as ts_ny_taxi
                      FROM
                        ny_taxi_dataset
                    functions:
                      - name: set_type
                        columns:
                          pickup_datetime: timestamp
                          dropoff_datetime: timestamp
```

### **Append data with new partition spec**

Run the following Flare job that appends data into DataOS with the updated partition on ‘day’.

```yaml
version: v1
name: wf-ny-taxi-updatepartition
type: workflow
tags:
  - NY-Taxi
  - Connect
  - Tier.Gold
description: The job ingests NY-Taxi data and writes it with updated partitioning on day, using an updated workflow spec.
workflow:
  title: NY Taxi Data Ingestion
  dag:
    - name: storage-event-context
      description: The job ingests NY-Taxi data from dropzone into Icebase with enhanced metadata configuration.
      title: NY Taxi Ingestion
      spec:
        tags:
          - NY-Taxi
          - Connect
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 2500m
            cores: 2
            memory: 3048m
          executor:
            coreLimit: 3500m
            cores: 2
            instances: 2
            memory: 4000m
          job:
            explain: true
            inputs:
              - name: ny_taxi
                dataset: dataos://thirdparty01:none/ny-taxi-data/010100.json?acl=r
                format: JSON
                options:
                  multiLine: true
            logLevel: INFO
            outputs:
              - name: final
                dataset: dataos://lakehouse:raw01/ny-taxi-partitioned?acl=rw
                format: Iceberg
                description: NY-Taxi data written with daily partitioning.
                tags:
                  - NY-Taxi
                  - Connect
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: pickup_datetime
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: day
                        column: pickup_datetime
                        name: day
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                title: NY-Taxi Partitioned Dataset
            steps:
              - sequence:
                  - name: final
                    sql: |
                      SELECT
                        *,
                        date_format(now(), 'yyyyMMddHHmm') as version,
                        now() as ts_ny_taxi
                      FROM
                        ny_taxi
                    functions:
                      - name: set_type
                        columns:
                          pickup_datetime: timestamp
                          dropoff_datetime: timestamp

```
