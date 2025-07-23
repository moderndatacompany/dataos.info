# Remove Orphans

The [`remove_orphans` action](/resources/stacks/flare/configurations/#remove_orphans) cleans up orphans files older than a specified time period. This action may take a long time to finish if you have lots of files in data and metadata directories. It is recommended to execute this periodically, but you may not need to execute this often. 

!!! note 

    It is dangerous to remove orphan files with a retention interval shorter than the time expected for any write to complete because it might corrupt the table if in-progress files are considered orphaned and are deleted. The default interval is 3 days.

**Get the list of snapshots by writing the following command**

```bash
dataos-ctl dataset snapshots -a dataos://lakehouse:retail/city
```

**Expected output**

```bash

      SNAPSHOTID      │   TIMESTAMP   │    DATE AND TIME (GMT)     
──────────────────────┼───────────────┼────────────────────────────
  7002479430618666161 │ 1740643647492 │ 2025-02-27T08:07:27+00:00  
  2926095925031493170 │ 1740737372219 │ 2025-02-28T10:09:32+00:00  
```

## Configuration

| Attribute               | Type      | Description |
|-------------------------|-----------|-------------|
| `older_than`              | timestamp | Remove orphan files created before this timestamp. Defaults to 3 days ago. |
| `location`                | string    | Directory to look for files in. Defaults to the table's location. |
| `dry_run`                 | boolean   | If true, performs a dry run without actually removing files. Defaults to false. |
| `max_concurrent_deletes`  | int       | Size of the thread pool used for delete operations. By default, no thread pool is used. |


<!-- actions:
- name: remove_orphans
  input: input
  options:
    dryRun: true
    olderThanTimestamp: '2024-01-18 09:00:00.000'
    olderThanMillis: '1705599997318'
    location: 'path-to-file'
    maxConcurrentDeletes: 2 -->


The following code snippet demonstrates removing orphan files older than the time specified in the `olderThan` in Unix epoch format.

The task relies on the `remove_orphans` action, which requires the inputDf dataset as an input. This dataset is defined as `dataos://lakehouse:retail/city` and is in Iceberg format. Additionally, the action provides options, such as the `olderThan` parameter, which specifies the timestamp (in Unix format) for identifying orphan files.

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
        stack: flare:5.0 
        compute: runnable-default 
        stackSpec: 
          job: 
            explain: true 
            logLevel: INFO 
            inputs: 
              - name: inputDf 
                dataset: dataos://lakehouse:retail/city 
                format: Iceberg 
            actions: # Flare Action
              - name: remove_orphans # Action Name
                input: inputDf # Input Dataset Name
                options: # Options
                  olderThan: "1739734172" # Timestamp in Unix Format
```
