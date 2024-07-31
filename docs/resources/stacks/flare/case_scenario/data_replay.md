# Data Replay

## Overview

This documentation outlines the data replay case scenario, which involves the need to rewrite a data segment for various reasons, such as incomplete or corrupted data. In this scenario, we explore the configuration of data ingestion jobs to rectify corrupted records without the necessity of rewriting all partitions. This approach significantly reduces costs associated with complete data rewrites.

## Solution Approach

The primary objective of this case scenario is to configure data ingestion jobs for the replacement of a single partition of data while maintaining the ability to overwrite partitions dynamically.

## Implementation Details

### **Data Ingestion and Replacement**
To validate the data replay scenario, we conducted the following steps:

1. **Data Ingestion**: We initiated the data replay scenario by ingesting NY-taxi data, utilizing vendor-level partitioning.

2. **Data Replacement**: Subsequently, we replaced the data of a specific vendor using the following attributes:
   - `saveMode`: overwrite
   - `overwrite-mode`: dynamic

### **Validation**

To ensure the correctness of our data replay approach, we conduct tests involving timestamp columns. Specifically, we compared the values written during the initial write operation to the values written during the second write operation, which targeted only the data for a single vendor.

### **Partitioning and Replacement**


We also evaluated data replay by writing data with partitioning in mind. During this phase, we replaced one partition of data using a separate job.

## Outcomes

The results of the data replay process are organized and stored in folders based on predefined partition criteria. These files are accessible via Workbench or designated storage locations. To verify the accuracy of the output, we performed queries accessing data from the modified partition and cross-referenced the results with timestamp values. This validation process confirmed the success of the data replay operation.

## Code files

```yaml
# this job is for only changing one partition of dataset**
name: workflow-ny-taxi-partitioned-vendor
version: v1
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
        stack: flare:5.0
        compute: runnable-default
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
              - name: output01
                depot: dataos://icebase:raw01?acl=rw
                format: iceberg
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                        write.format.default: parquet
                        write.metadata.compression-codec: gzip
                        overwrite-mode: dynamic # this was used only when one partition data is need to replace with saveMode as Overwrite 
                    partitionSpec:
                      - type: identity
                        column: vendor_id
            steps:
              - sequence:
                - name: ny_taxi_ts
                  sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as ts_ny_taxi FROM ny_taxi where vendor_id = 1   ## data written for only one vendor
```