# Case Scenario

## Batch Jobs

Batch jobs are utilized in situations where there is a need to recompute all changed datasets in every run, ensuring consistent end-to-end performance on each occasion.

Simple Batch Jobs follow a straightforward process that involves:

1. Reading data from a specified set of Depots.
2. Applying transformations to the data.
3. Writing the transformed data to another set of Depots.

<details>
<summary>Case Scenario</summary>

The code snippet below demonstrates a Workflow involving a single Flare batch job that reads the input dataset from <code>thirdparty01</code> Depot, perform transformation using Flare Stack, and stores the output dataset in the <code>bqdepot</code> Depot. 

**Code Snippet**

```yaml
name: bq-write-01
version: v1
type: workflow
tags:
  - bq
  - City
title: Write bq
workflow:
  dag:
    - name: city-write-bq-01
      title: City write bq
      description: This job read data from azure and writes to Sbq
      spec:
        tags:
          - Connect
          - City
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
              - name: city_connect
                dataset: dataos://thirdparty01:none/city
                format: csv
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://bqdepot:dev/city?acl=rw
                format: bigquery
                options:
                  saveMode: overwrite
                  bigquery:
                    temporaryBucket: tmdc-development-new
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect LIMIT 10
```


</details>


## Stream Jobs

In scenarios where there is a continuous requirement to process incoming data in real-time, Flare Stream Jobs offer an effective solution. However, it is advisable to exercise caution when creating Stream Jobs, as they should be reserved for cases where strict latency requirements exist, typically demanding a processing time of less than a minute, considering that they may incur higher computing costs.

<details>
<summary>Case Scenario</summary>


The following code snippet illustrates a Workflow involving a Flare Stream Job that reads data from the <code>thirdparty01</code> Depot in a streaming format and subsequently written to the <code>eventhub</code> Depot. During this process, all intermediate streams of data batches are stored at the location specified in the <code>checkpointLocation</code> attribute.

**Code Snippet**

```yaml
version: v1
name: write-eventhub-b-02
type: workflow
tags:
  - eventhub
  - write
description: this jobs reads data from thirdparty and writes to eventhub
workflow:
  dag:
    - name: eventhub-write-b-02
      title: write data to eventhub
      description: write data to eventhub
      spec:
        tags:
          - Connect
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            streaming:
              checkpointLocation: /tmp/checkpoints/devd01
              forEachBatchMode: "true"
            inputs:
              - name: input
                dataset: dataos://thirdparty01:none/city
                format: csv
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
                isStream: true  #Set to True if the data is being streamed. This is mandatory when working with streaming data.

            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://eventhub:default/eventhub01?acl=rw
                format: Eventhub

            steps:
              - sequence:
                - name: finalDf
                  sql: SELECT * FROM input
```

</details> 


## Incremental Jobs

Computes only the changed rows or files of data since the last build, reducing overall computation and latency. Incremental Jobs only compute the rows or files of data that have changed since the last build. They are suitable for processing event data and datasets with frequent changes. Incremental jobs reduce overall computation and significantly decrease end-to-end latency compared to batch jobs. Moreover, compute costs for incremental jobs can be lower than batch jobs when dealing with high-scale datasets, as the amount of actual computation is minimized. By processing only new data, incremental jobs eliminate the need to redo analysis on large datasets where most information remains unchanged. For case scenarios on Incremental Jobs, refer to [here](/resources/stacks/flare/case_scenario/incremental_jobs/).

[Incremental Job](/resources/stacks/flare/case_scenario/incremental_jobs/)

## Data Transformation

- [Read and write from Iceberg branch](/resources/stacks/flare/case_scenario/iceberg_branch_read_write/)

- [Data Replay](/resources/stacks/flare/case_scenario/data_replay/)

- [Concurrent Writes](/resources/stacks/flare/case_scenario/concurrent_writes/)

- [Query Dataset for Job in Progress](/resources/stacks/flare/case_scenario/query_dataset_for_job_in_progress/)

- [Merge Into Functionality](/resources/stacks/flare/case_scenario/merge_into_functionality/)


## Job performance and optimization

- [Job Optimization by Tuning](/resources/stacks/flare/case_scenario/job_optimization_by_tuning/)


## Metadata and data management

- [Column Tagging](/resources/stacks/flare/case_scenario/column_tagging/)

- [Data Syndication](/resources/stacks/flare/case_scenario/syndication/)


## Optimizing the performance of Iceberg tables 

Managing the datafiles and metadata files in your Lakehouse is of paramount importance as data grows over time. In Iceberg, metadata files are core to so many critical operations, such as time travel and query optimization. However, with the increase in the number of datafiles, the number of metadata files also increases. Additionally, streaming-based ingestion jobs can lead to a lot of small files being generated as data is written in smaller chunks as and when they arrive. 

Performance of such tables can be optimized by reducing the number of data files, applying effective partitioning, sorting, and managing updates efficiently. Below are  Below are the key strategies for achieving these optimizations:

### **Compaction**

When querying Iceberg tables, every file operation—opening, scanning, closing—adds to compute time and cost. As the number of files involved in a query increases as  each file needs to be opened, scanned, and closed, performance can degrade due to the overhead of handling many small files (in batch or stream job both). 

To optimize query performance and reduce overhead, two types of compaction can be applied:

- [Data File Compaction](/resources/stacks/flare/case_scenario/rewrite_dataset/): Compact small data files into larger files at regular intervals. This reduces the number of files to scan during queries.

- [Manifest Rewrite](/resources/stacks/flare/case_scenario/rewrite_manifest_files/): Rewrite manifests if their count becomes disproportionately large compared to data files. Rewriting manifests helps reduce metadata overhead, which in turn speeds up data scan.

### **Partitioning**

Optimize query performance by organizing data into folders based on key columns. Learn when and how to apply partitioning to reduce scan time and improve efficiency.

- [Partitioning](/resources/stacks/flare/case_scenario/partitioning/)

- [Partition Evolution](/resources/stacks/flare/case_scenario/partition_evolution/)

Apart from compaction and partitioning below methods are also used to make the query result faster.

## Bucketing

- [Bucketing](/resources/stacks/flare/case_scenario/bucketing/)

## Caching

- [Caching](/resources/stacks/flare/case_scenario/caching/)


## Data Lifecycle and Maintenance

It is important to have a strategy as part of your organization’s regular maintenance process to remove unnecessary metadata files or to compact smaller files into larger ones for better read performance. Flare provides actions for easy maintenance of Iceberg tables:

!!! note  
  
    The below functionality is only supported in the DataOS managed Depot, Lakehouse.
 

| **Action Name**                           | **Description**                                                                                                                                                                                                                       |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Delete from Dataset](/resources/stacks/flare/case_scenario/delete_from_dataset/) | Deletes data from a dataset in an Iceberg table. This operation typically creates a new snapshot to reflect the state after deletion.                                                         |
| [Expire Snapshots](/resources/stacks/flare/case_scenario/expire_snapshots/)       | Removes outdated snapshots from Iceberg tables. Cleans up associated manifest lists, manifests, data files, and delete files, provided they’re no longer used by any active snapshots.         |
| [Remove Orphans](/resources/stacks/flare/case_scenario/remove_orphans/)           | Deletes orphaned data files in Iceberg tables—those that are no longer referenced in metadata. Helps save space and prevents inconsistencies.                                                  ||                                  |

