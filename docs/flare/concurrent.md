# Concurrent writes 

## Overview

This use case tests the scenario where multiple jobs are concurrently writing at the same location.

### Solution approach

This scenario works only for Iceberg as it supports multiple concurrent writes. A workflow with two jobs is defined to write at the same data location.

## Implementation Details
 
This use case is tested on NY-Taxi data. A workflow is created with two jobs (in one dag) to perform write operation for different vendors (data was filtered on vendor level). The workflow is to be submitted for both the modes:
-  **append save mode** 

For append mode, the data should be written from both jobs. 

- **overwrite save mode**

When Flare's overwrite mode is dynamic, partitions that have rows produced by the jobs will be replaced on every new write operation. Only the last finished job's data should be seen in this case.

## Outcomes

Queries were run to fetch data to validate the expected behavior. Also, it was possible to query data while data was being written.

## Code files

### **Job to test concurrent writes**

```yaml
# This contains two jobs and save mode as append

---
version: v1beta1
name: workflow-ny-taxi-parallel-write
type: workflow
tags:
- Connect
- NY-Taxi
description: The job ingests NY-Taxi data small files and conbined them to one file
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
               datasetName: ny_taxi_04
               outputName:  output01
               outputType: Iceberg
               outputOptions:
                 saveMode: append
                 iceberg:
                  properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                      #overwrite-mode: dynamic # this was used only when one partition data is need to be replaced with saveMode as Overwrite that job was seperate if need will send that as well
                  partitionSpec:
                    - type: month # identity partitioning was used at vendor_id level
                      column: date_col # col name = vendor_id
                      name: month

               tags:
                  - Connect
                  - NY-Taxi
               title: NY-Taxi Data Partitioned

            sequence:
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
            - name: output02
              depot: dataos://icebase:raw01?acl=rw
          steps:
          - sink:
             - sequenceName: ny_taxi_ts
               datasetName: ny_taxi_04
               outputName:  output02
               outputType: Iceberg
               outputOptions:
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

            sequence:
              - name: ny_taxi_changed_dateformat
                sql: select *, to_timestamp(pickup_datetime/1000) as date_col from ny_taxi where vendor_id = 2

              - name: ny_taxi_ts
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                  ts_ny_taxi FROM ny_taxi_changed_dateformat
```
### **DataOS Tool Yaml**

```yaml
version: v1beta1
name: dataos-tool-ny-taxi-parallel-write
type: workflow
workflow:
  dag:
  - name: dataos-tool
    spec:
      stack: alpha
      envs:
        LOG_LEVEL: debug
      alpha:
        image: rubiklabs/dataos-tool:0.0.26
        
        arguments:
          - dataset
          - set-metadata
          - --address
          - dataos://icebase:raw01/ny_taxi_04
          - --version
          - latest
```