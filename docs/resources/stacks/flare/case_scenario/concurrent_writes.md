# Concurrent writes


This case scenario tests the situation where multiple jobs are being concurrently written at the same location.

!!! info

    This scenario works only for Iceberg as it supports multiple concurrent writes. 

## Implementation details

This case scenario is tested on NY-Taxi data. A workflow is created with two jobs (in one dag) to perform write operations for different vendors (data was filtered on vendor level). The workflow is to be submitted for both modes: 

**append and save mode**

For append mode, the data should be written from both jobs.

**overwrite and save mode**

When Flare's overwrite mode is dynamic, partitions that have rows produced by the jobs will be replaced on every new write operation. Only the last finished job's data should be seen in this case.

## Outcomes

Queries were run to fetch data to validate the expected behavior. Also, it was possible to query data while data was being written.

### **Job to test concurrent writes**

```yaml
# This contains two jobs and save mode as append
version: v1beta1
name: workflow-ny-taxi-parallel-write
type: workflow
tags:
- Connect
- NY-Taxi
description: The job ingests NY-Taxi data small files and combined them to one file
workflow:
  title: Connect NY Taxi
  dag:
    - name: nytaxi-vendor-one
      title: NY-taxi data ingester-parallel 
      description: The job ingests NY-Taxi data from dropzone into raw zone
      spec:
        tags:
        - Connect
        - NY-Taxi
        stack: flare:6.0
        stackSpec:
          job:
            explain: true
            inputs:
              - name: ny_taxi
                dataset: dataos://thirdparty01:none/ny-taxi-data?acl=r
                format: json
                isStream: false

            logLevel: INFO

            outputs:
              - name: ny_taxi_ts
                dataset: dataos://lakehouse:raw01/ny_taxi_ts?acl=rw
                type: iceberg
                options:
                  saveMode: append
                  iceberg:
                    properties:
                        write.format.default: parquet
                        write.metadata.compression-codec: gzip
                        # overwrite-mode: dynamic # this was used only when one partition data is need to be replaced with saveMode as Overwrite that job was seperate if need will send that as well
                    partitionSpec:
                      - type: month # identity partitioning was used at vendor_id level
                        column: date_col # col name = vendor_id
                        name: month
                    tags:
                        - Connect
                        - NY-Taxi
                    title: NY-Taxi Data Partitioned

            steps:
              - sequence:
                  - name: ny_taxi_changed_dateformat
                    sql: select *, to_timestamp(pickup_datetime/1000) as date_col from ny_taxi where vendor_id = 1

                  - name: ny_taxi_ts
                    sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                      ts_ny_taxi FROM ny_taxi_changed_dateformat


    - name: nytaxi-vendor-two
      title: NY-taxi data ingester-parallel
      description: The job ingests NY-Taxi data from dropzone into raw zone
      spec:
        tags:
        - Connect
        - NY-Taxi
        stack: flare:6.0
        stackSpec:
          job:
            explain: true
            inputs:
              - name: ny_taxi
                dataset: dataos://thirdparty01:none/ny-taxi-data?acl=r
                format: json
                isStream: false

            logLevel: INFO

            outputs:
              - name: output02
                dataset: dataos://lakehouse:raw01/ny_taxi_ts?acl=rw
                options:
                  saveMode: append
                  iceberg:
                    properties:
                        write.format.default: parquet
                        write.metadata.compression-codec: gzip
                    partitionSpec:
                      - type: month
                        column: date_col
                        name: month
                tags:
                    - Connect
                    - NY-Taxi
                title: NY-Taxi Data Partitioned
            
            steps:
              - sequence: ny_taxi_ts
                  - name: ny_taxi_changed_dateformat
                    sql: select *, to_timestamp(pickup_datetime/1000) as date_col from ny_taxi where vendor_id = 2

                  - name: ny_taxi_ts
                    sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                        ts_ny_taxi FROM ny_taxi_changed_dateformat
```
