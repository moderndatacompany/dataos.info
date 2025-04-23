# Case Scenario

## Batch Jobs

Batch jobs are utilized in situations where there is a need to recompute all changed datasets in every run, ensuring consistent end-to-end performance on each occasion.

Simple Batch Jobs follow a straightforward process that involves:

1. Reading data from a specified set of depots.
2. Applying transformations to the data.
3. Writing the transformed data to another set of depots.

<details>
<summary>Case Scenario</summary>

The code snippet below demonstrates a Workflow involving a single Flare batch job that reads the input dataset from <code>thirdparty01</code> depot, perform transformation using Flare Stack, and stores the output dataset in the <code>bqdepot</code> depot. 

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


The following code snippet illustrates a Workflow involving a Flare Stream Job that reads data from the <code>thirdparty01</code> depot in a streaming format and subsequently written to the <code>eventhub</code> depot. During this process, all intermediate streams of data batches are stored at the location specified in the <code>checkpointLocation</code> attribute.

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

[Read and write from Iceberg branch](/resources/stacks/flare/case_scenario/iceberg_branch_read_write/)

<!-- [Data Profiling Jobs](/resources/stacks/flare/case_scenario/data_profiling_jobs/)

[Data Quality Jobs (Assertions)](/resources/stacks/flare/case_scenario/data_quality_jobs/) -->

[Compression](/resources/stacks/flare/case_scenario/compression/)

[Merge Data](/resources/stacks/flare/case_scenario/merge_data/)

[Enrichment](/resources/stacks/flare/case_scenario/enrichment/)

[Merge Into Functionality](/resources/stacks/flare/case_scenario/merge_into_functionality/)

[Partitioning](/resources/stacks/flare/case_scenario/partitioning/)

[Partition Evolution](/resources/stacks/flare/case_scenario/partition_evolution/)

[Data Replay](/resources/stacks/flare/case_scenario/data_replay/)

[Concurrent Writes](/resources/stacks/flare/case_scenario/concurrent_writes/)

[Query Dataset for Job in Progress](/resources/stacks/flare/case_scenario/query_dataset_for_job_in_progress/)

[Bucketing](/resources/stacks/flare/case_scenario/bucketing/)

[Caching](/resources/stacks/flare/case_scenario/caching/)

[Job Optimization by Tuning](/resources/stacks/flare/case_scenario/job_optimization_by_tuning/)

[Column Tagging](/resources/stacks/flare/case_scenario/column_tagging/)

## Data Syndication

[Syndication](/resources/stacks/flare/case_scenario/syndication/)

## Flare Actions

> The below functionality is only supported in the DataOS managed depot, Icebase
> 

[Delete from Dataset](/resources/stacks/flare/case_scenario/delete_from_dataset/)

[Expire Snapshots](/resources/stacks/flare/case_scenario/expire_snapshots/)

[Remove Orphans](/resources/stacks/flare/case_scenario/remove_orphans/)

[Rewrite Manifest Files](/resources/stacks/flare/case_scenario/rewrite_manifest_files/)

### **Rewrite Orphans**

The `remove_orphans` [action](/resources/stacks/flare/configurations/#remove_orphans) cleans up orphans files older than a specified time period. This action may take a long time to finish if you have lots of files in data and metadata directories. It is recommended to execute this periodically, but you may not need to execute this often. 

<aside class="callout">

🗣️ <b>Note:</b> It is dangerous to remove orphan files with a retention interval shorter than the time expected for any write to complete because it might corrupt the table if in-progress files are considered orphaned and are deleted. The default interval is 3 days.

</aside>

<details><summary>Case Scenario</summary>

The following code snippet demonstrates removing orphan files older than the time specified in the `olderThan` in Unix epoch format.


The following code snippet aims to remove orphan files within Iceberg tables in DataOS Depot using the ``remove_orphans`` action.

The task relies on the remove_orphans action, which requires the inputDf dataset as an input. This dataset is defined as dataos://icebase:actions/random_users_data and is in Iceberg format. Additionally, the action provides options, such as the olderThan parameter, which specifies the timestamp (in Unix format) for identifying orphan files.


```yaml
version: v1 
name: orphans 
type: workflow 
tags: 
  - orphans
workflow: 
  title: Remove orphan files 
  dag: 
    - name: orphans 
      title: Remove orphan files 
      spec: 
        tags: 
          - orphans
        stack: flare:6.0 
        compute: runnable-default 
        stackSpec: 
          job: 
            explain: true 
            logLevel: INFO 
            inputs: 
              - name: inputDf 
                dataset: dataos://icebase:actions/random_users_data 
                format: Iceberg 
            actions: # Flare Action
              - name: remove_orphans # Action Name
                input: inputDf # Input Dataset Name
                options: # Options
                  olderThan: "1674201289720" # Timestamp in Unix Format
```
</details>



### **Rewrite Dataset**

The [`rewrite_dataset`](/resources/stacks/flare/configurations/#rewrite_dataset) action provided by DataOS allows for the parallel compaction of data files in Iceberg tables using Flare. This action efficiently reduces the size of data files to meet the specified target file size in bytes, as defined in the YAML configuration.

<details><summary>Case Scenario</summary>

The following code snippet demonstrates the compression of Iceberg data files for a given input dataset, `inputDf`, stored in a DataOS Depot. The compression process aims to reduce the file size to a specified target size in bytes, denoted by the variable `target-file-size-bytes`.

```yaml
version: v1 
name: rewrite 
type: workflow 
tags: 
  - Rewrite
workflow: 
  title: Compress iceberg data files 
  dag: 
    - name: rewrite 
      title: Compress iceberg data files 
      spec: 
        tags: 
          - Rewrite
        stack: flare:6.0 
        compute: runnable-default 
        stackSpec: 
          job: 
            explain: true 
            logLevel: INFO 
            inputs: 
              - name: inputDf 
                dataset: dataos://icebase:actions/random_users_data?acl=rw
                format: Iceberg 
            actions: # Flare Action
              - name: rewrite_dataset # Name of the action
                input: inputDf # Input Dataset Name 
                options: # Options
                  properties: # Properties
                    "target-file-size-bytes": "2048" # Target File Size in Bytes
```
</details>



