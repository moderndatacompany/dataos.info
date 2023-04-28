# Use Cases for various scenarios

This articles explains all the scenarios with the proper use cases to understand the desired functionality and intented behaviour while writing Flare jobs. It also includes yaml for the respective use cases.

> *Note: You need to run data tool for all the use cases related to iceberg to access the ingested data in the Workbench. Ensure to update the latest data tool image and dataset path in the data tool yaml.*



## Scenario #1- Too many files with few records problem.

### Overview
This use case involves combining a large number of files with very few records.
### Solution approach
Files are combined and compressed.
### Implementation Details
### Outcomes
if there are  many files in some partition or non partitioned data,  it will merge all small files into a large one 
### Impediments/fallbacks
### Code files


## Scenario #2- Ensure dataset to be available for query while a job is writing data to it.
### Overview
### Solution approach
### Implementation Details
### Outcomes
Tested this- While a job is running and metadata location is set, we can run the query with the previous metadata location set before the job run. If we update the snapshot id during a job run, it picks data from that snapshot
### Impediments/fallbacks
### Code files

. 


## Scenario #3- Try out with partition keys with different data types

### Overview
Partitioning is a way to make queries faster by grouping similar rows together when writing.
This use case checks how partitioning works for Flare while writing data to iceberg and non iceberg type data storage in order to improve query processing performance.

### Solution approach

Iceberg can partition timestamps by year, month, day, and hour granularity. It can also use a categorical column of data type- string, integer, long, *double(to be checked)*, like vendor id in this example, to store rows together and speed up queries. 

Iceberg produces partition values by taking a column value and optionally transforming it. Iceberg converts timestamp values into a date, and extracts year, month, day, hour, etc.

While in non-iceberg data sink, provide the columns explicitly for the year, month, hour as transformation is not automatic.

### Implementation details

The five partitioning modes were tested ( identity, year, month, day & hour). 

- Partition using type identity
Two cases were checked, one for integer values and another for string values. 
- Partition using type timestamp column
All four (year, month, day, hour) partitioning cases around timestamp column  are working.

Example 1: Partitioning is done on identity by taking the vendor_id column. You don't need to give name property if  partition field type is identity type.

```yaml
partitionSpec:
    - type: identity  # options tested: identity, year, month, day, hour
      column: vendor_id # columns used - identity (vendor_id, one string column) & for rest date_col
```

Example 2: Partitioning is done on the year.

```yaml
partitionSpec:
    - type: year  # options tested: identity, year, month, day, hour
      column: date_col # columns used - identity (vendor_id, one string column) & for rest date_col
      name: year
```

Example 3: Nested partitioning is done on (identity, year). Here, the vendor_id used for identity should come at the first level.

```yaml
partitionSpec:
    - type: identity  
      column: vendor_id # columns used - identity (vendor_id, one string column) & for rest date_col
      
    - type: year        # options tested: identity, year, month, day, hour
      column: date_col  
      name: year
```

> *Note: When specifying the partition criterion, the 'partitionSpec' property should be defined as a child property under 'iceberg' in the sink section. Otherwise partioning will not be performed as desired.*

### Outcome

The files are stored in the folders based on the partition criterion defined, and you can view them in workbench or storage locations.

### Impediments/fallouts

### Code files
```yaml
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
        driver:
          coreLimit: 2400m
          cores: 2
          memory: 3072m
        executor:
          coreLimit: 2400m
          cores: 2
          instances: 1
          memory: 4096m
        job:
          explain: true
          inputs:
           - name: ny_taxi
             dataset: dataos://thirdparty01:none/ny-taxi-data
             format: json
             isStream: false

          logLevel: INFO
          outputs:
            - name: output01
              depot: dataos://icebase:raw01
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
                    - type: identity  # options tested: string, integer, long
                      column: vendor_id # columns used - identity (vendor_id, one string column) 

                    - type: year  # options tested: identity, year, month, day, hour
                      column: date_col # columns used - identity (vendor_id, one string column) & for rest date_col
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


        sparkConf:
        - spark.serializer: org.apache.spark.serializer.KryoSerializer
        - spark.sql.shuffle.partitions: "800"
        - spark.executor.extraJavaOptions: -XX:+PrintFlagsFinal -XX:+PrintReferenceGC
            -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintAdaptiveSizePolicy
            -XX:+UnlockDiagnosticVMOptions -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/hoodie-heapdump.hprof
        - spark.driver.extraJavaOptions: -XX:+PrintTenuringDistribution -XX:+PrintGCDetails
            -XX:+PrintGCDateStamps -XX:+PrintGCApplicationStoppedTime -XX:+PrintGCApplicationConcurrentTime
            -XX:+PrintGCTimeStamps -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/hoodie-heapdump.hprof
        - spark.memory.storageFraction: "0.1"
        - spark.memory.fraction: "0.1"
        - spark.kryoserializer.buffer.max: 256m
        - spark.shuffle.memoryFraction: "0.0"
```

## Scenario #4- Data Replay

### Overview
This use case describes the data replay scenario where you need to re-write a data segment for various reasons, such as incomplete or corrupted data. You can configure your data ingestion jobs to write the proper partitions to avoid expensive complete data re-write.

### Solution approach
This use case configures jobs for replacing one partition of data. The behavior was to overwrite partitions dynamically.

### Implementation details

1. Data replay scenario is tested by first ingesting the  NY-taxi data at vendor level partitioning and then one vendor data was replaced using the following properties:
- saveMode: overwrite 
- overwrite-mode: dynamic 

The test validation is done with timestamp column by comparing the values written at the time of first write and the second time when the data is written only for the one vendor data.

2. Data replay is  tested by writing data with partitioning and one partition of data was replaced by another job. 

### Outcomes
The files are stored in the folders  based on the partition criterion defined and can be viewed in workbench or  storage locaions. The accuracy of the output was tested by running queries accessing data from the modified partition and confirmed with the timestamp values.

### Impediments/fallbacks

### Code files

```yaml
### this job is for only changing one partition of dataset

---
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
        driver:
          coreLimit: 2400m
          cores: 2
          memory: 3072m
        executor:
          coreLimit: 2400m
          cores: 2
          instances: 1
          memory: 4096m
        job:
          explain: true
          inputs:
           - name: ny_taxi
             dataset: dataos://thirdparty01:none/ny-taxi-data
             format: json
             isStream: false

          logLevel: INFO
          outputs:
            - name: output01
              depot: dataos://icebase:raw01
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
                      overwrite-mode: dynamic
                      #overwrite-mode: dynamic # this was used only when one partition data is need to replace with saveMode as Overwrite that job was seperate if need will send that as well
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
                  ts_ny_taxi FROM ny_taxi where vendor_id = 1   ## data written for only one vendor


        sparkConf:
        - spark.serializer: org.apache.spark.serializer.KryoSerializer
        - spark.sql.shuffle.partitions: "800"
        - spark.executor.extraJavaOptions: -XX:+PrintFlagsFinal -XX:+PrintReferenceGC
            -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintAdaptiveSizePolicy
            -XX:+UnlockDiagnosticVMOptions -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/hoodie-heapdump.hprof
        - spark.driver.extraJavaOptions: -XX:+PrintTenuringDistribution -XX:+PrintGCDetails
            -XX:+PrintGCDateStamps -XX:+PrintGCApplicationStoppedTime -XX:+PrintGCApplicationConcurrentTime
            -XX:+PrintGCTimeStamps -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/hoodie-heapdump.hprof
        - spark.memory.storageFraction: "0.1"
        - spark.memory.fraction: "0.1"
        - spark.kryoserializer.buffer.max: 256m
        - spark.shuffle.memoryFraction: "0.0"
```


## Scenario #5- Test concurrent writes and parallel processing

### Overview
This use case tests the scenario where multiple jobs are concurrently writing at the same location.
### Solution approach

This scenario works only for iceberg as it allows parallel writes. A workflow with two jobs are defined to write at the same data location.

### Implementation Details
 
This use case was tested on NY-Taxi data. Two jobs (in one dag) were created for each vendor (data was filtered on vendor level). The workflow is to be submitted for both the modes:
- first, with the **append save mode** and then
When written in append mode, the data should be written from both jobs. 

- **overwrite save mode**

When Flare's overwrite mode is dynamic, partitions that have rows produced by the jobs will be replaced on every new write operation. Only the last finished job's data should be seen in this case.

### Outcomes
Queries were run to validate the expected behavior. Also, it was possible to query data while data was being written.

### Impediments/fallbacks


### Code files

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
      # persistentVolume:
      #   name: persistent-v
      #   directory: connectCity
      flare:
        driver:
          coreLimit: 1200m
          cores: 1
          memory: 1024m
        executor:
          coreLimit: 1200m
          cores: 1
          instances: 1
          memory: 1024m
        job:
          explain: true
          inputs:
           - name: ny_taxi
             dataset: dataos://thirdparty01:none/ny-taxi-data
             format: json
             isStream: false

          logLevel: INFO
          outputs:
            - name: output01
              depot: dataos://icebase:raw01
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
        sparkConf:
        - spark.serializer: org.apache.spark.serializer.KryoSerializer
        - spark.sql.shuffle.partitions: "800"
        - spark.executor.extraJavaOptions: -XX:+PrintFlagsFinal -XX:+PrintReferenceGC
            -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintAdaptiveSizePolicy
            -XX:+UnlockDiagnosticVMOptions -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/hoodie-heapdump.hprof
        - spark.driver.extraJavaOptions: -XX:+PrintTenuringDistribution -XX:+PrintGCDetails
            -XX:+PrintGCDateStamps -XX:+PrintGCApplicationStoppedTime -XX:+PrintGCApplicationConcurrentTime
            -XX:+PrintGCTimeStamps -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/hoodie-heapdump.hprof
        - spark.memory.storageFraction: "0.1"
        - spark.memory.fraction: "0.1"
        - spark.kryoserializer.buffer.max: 256m
        - spark.shuffle.memoryFraction: "0.0"

  - name: nytaxi-vendor-two
    title: NY-taxi data ingester-parallel
    description: The job ingests NY-Taxi data from dropzone into raw zone
    spec:
      tags:
      - Connect
      - NY-Taxi
      stack: flare:1.0
      # persistentVolume:
      #   name: persistent-v
      #   directory: connectCity
      flare:
        driver:
          coreLimit: 1200m
          cores: 1
          memory: 1024m
        executor:
          coreLimit: 1200m
          cores: 1
          instances: 1
          memory: 1024m
        job:
          explain: true
          inputs:
           - name: ny_taxi
             dataset: dataos://thirdparty01:none/ny-taxi-data
             format: json
             isStream: false

          logLevel: INFO
          outputs:
            - name: output02
              depot: dataos://icebase:raw01
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

        sparkConf:
        - spark.serializer: org.apache.spark.serializer.KryoSerializer
        - spark.sql.shuffle.partitions: "800"
        - spark.executor.extraJavaOptions: -XX:+PrintFlagsFinal -XX:+PrintReferenceGC
            -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintAdaptiveSizePolicy
            -XX:+UnlockDiagnosticVMOptions -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/hoodie-heapdump.hprof
        - spark.driver.extraJavaOptions: -XX:+PrintTenuringDistribution -XX:+PrintGCDetails
            -XX:+PrintGCDateStamps -XX:+PrintGCApplicationStoppedTime -XX:+PrintGCApplicationConcurrentTime
            -XX:+PrintGCTimeStamps -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/hoodie-heapdump.hprof
        - spark.memory.storageFraction: "0.1"
        - spark.memory.fraction: "0.1"
        - spark.kryoserializer.buffer.max: 256m
        - spark.shuffle.memoryFraction: "0.0"
```

## Scenario #6- Finalize strategy to supply credentials to Flare for GCP.
- Overview
- Solution approach
We will ask for access to the service account, which is configured during the install process,  As a par limitation on the GCP cloud we can set only one credential in the flare job,  So we need to ask for permissions on that account only. We need to document this strategy and mentation all required permission.

- BigQuery Data Viewer

- BigQuery Job User

- BigQuery Metadata Viewer

- BigQuery Read Session User

- Storage Admin

- Storage Object Viewer

### Implementation details
### Outcomes
### Impediments/fallbacks
### Code files

