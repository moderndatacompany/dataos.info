# Data Replay


This use case describes the data replay scenario where you need to re-write a data segment for various reasons, such as incomplete or corrupted data. You can configure your data ingestion jobs to fix corrupted records without rewriting all the partitions. This hugely helps to avoid expensive complete data re-write.

## Solution approach

This use case configures jobs for replacing one partition of data. The behavior was to overwrite partitions dynamically.

## Implementation details

1. Data replay scenario is tested by first ingesting the NY-taxi data at vendor level partitioning and then one vendor data was replaced using the following properties:
2. saveMode: overwrite
3. overwrite-mode: dynamic

The test validation is done with timestamp column by comparing the values written at the time of first write and the second time when the data is written only for one vendor data.

1. Data replay is tested by writing data with partitioning and one partition of data was replaced by another job.

## Outcomes

The files are stored in the folders based on the partition criterion defined and can be viewed in workbench or storage locations. The accuracy of the output was tested by running queries accessing data from the modified partition and confirmed with the timestamp values.

## Code files

```yaml
# this job is for only changing one partition of dataset**
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
               datasetName: ny_taxi_05
               outputName:  output01
               outputType: Iceberg
               outputOptions:
                 saveMode: overwrite
                 iceberg:
                  properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                      overwrite-mode: dynamic **# this was used only when one partition data is need to replace with saveMode as Overwrite** 
                  partitionSpec:
                    - type: identity
                      column: vendor_id
               tags:
                  - Connect
                  - NY-Taxi
               title: NY-Taxi Data Partitioned Vendor

            sequence:
              - name: ny_taxi_ts
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                  ts_ny_taxi FROM ny_taxi where vendor_id = 1   **## data written for only one vendor**
```