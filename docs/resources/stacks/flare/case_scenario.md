# Case Scenario

## Data Migration and Movement

[Batch Job](./case_scenario/batch_jobs.md)

[Stream Job](./case_scenario/stream_jobs.md)

[Incremental Job](./case_scenario/incremental_jobs.md)

## Data Transformation

[Data Profiling Jobs](./case_scenario/data_profiling_jobs.md)

[Data Quality Jobs (Assertions)](./case_scenario/data_quality_jobs.md)

[Compression](./case_scenario/compression.md)

[Merge Data](./case_scenario/merge_data.md)

[Enrichment](./case_scenario/enrichment.md)

[Merge Into Functionality](./case_scenario/merge_into_functionality.md)

[Partitioning](./case_scenario/partitioning.md)

[Partition Evolution](./case_scenario/partition_evolution.md)

[Data Replay](./case_scenario/data_replay.md)

[Concurrent Writes](./case_scenario/concurrent_writes.md)

[Query Dataset for Job in Progress](./case_scenario/query_dataset_for_job_in_progress.md)

[Bucketing](./case_scenario/bucketing.md)

[Caching](./case_scenario/caching.md)

[Job Optimization by Tuning](./case_scenario/job_optimization_by_tuning.md)

[Column Tagging](./case_scenario/column_tagging.md)

## Data Syndication

[Syndication](./case_scenario/syndication.md)

## Flare Actions

> The below functionality is only supported in the DataOS managed depot, Icebase
> 

[Delete from Dataset](./case_scenario/delete_from_dataset.md)

[Expire Snapshots](./case_scenario/expire_snapshots.md)

[Remove Orphans](./case_scenario/remove_orphans.md)

### **Rewrite Orphans**

The `remove_orphans` [action](./configurations/actions.md#remove-orphans) cleans up orphans files older than a specified time period. This action may take a long time to finish if you have lots of files in data and metadata directories. It is recommended to execute this periodically, but you may not need to execute this often. 

<aside>

🗣️ **Note:** It is dangerous to remove orphan files with a retention interval shorter than the time expected for any write to complete because it might corrupt the table if in-progress files are considered orphaned and are deleted. The default interval is 3 days.

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
        stack: flare:4.0 
        compute: runnable-default 
        flare: 
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

The [`rewrite_dataset`](./configurations/actions.md#rewrite-dataset) action provided by DataOS allows for the parallel compaction of data files in Iceberg tables using Flare. This action efficiently reduces the size of data files to meet the specified target file size in bytes, as defined in the YAML configuration.

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
        stack: flare:4.0 
        compute: runnable-default 
        flare: 
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


[Rewrite Manifest Files](./case_scenario/rewrite_manifest_files.md)