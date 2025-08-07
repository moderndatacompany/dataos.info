# Expire Snapshots

The [`expire_snapshots` action](/resources/stacks/flare/configurations/#expire_snapshots) expires amassed snapshots.  Data files are not deleted until they are no longer referenced by a snapshot that may be used for time travel or rollback. Regularly expiring snapshots deletes unused data files.


!!! info "Important considerations"

    - Expiring old snapshots removes them from metadata, so they are no longer available for time travel queries.
    - Data files are not deleted until they are no longer referenced by a snapshot that may be used for time travel or rollback.
    - Regularly expiring snapshots deletes unused data files.


To check the timestamp and list of snapshot add the following command in your terminal:

```bash
dataos-ctl dataset snapshots -a dataos://lakehouse:retail/pos_store_product_cust
```

**Expected output**

```bash
INFO[0000] 📂 get snapshots...                           
INFO[0003] 📂 get snapshots...completed                  

      SNAPSHOTID      │   TIMESTAMP   │    DATE AND TIME (GMT)     
──────────────────────┼───────────────┼────────────────────────────
  7177047349072031975 │ 1744366300306 │ 2025-04-11T10:11:40+00:00  
  580493728505961346  │ 1744366356145 │ 2025-04-11T10:12:36+00:00  
  2613385101287075565 │ 1744366357891 │ 2025-04-11T10:12:37+00:00  
```

!!! Tip

    It is advisable to use Flare 5.0 with updated image tag `7.3.21` for the expire_snapshot action, as Flare 6.0 currently supports only two methods for snapshot expiration: the `expireOlderThan` and `expireSnapshotId` attributes.

## Configuration Options for Snapshot Deletion


| **Attribute**               | **Description**                                                                                                                                                   |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`olderThanMillis`**       | Milliseconds since epoch before which snapshots will be removed. This replaces `expireOlderThan` as the primary time-based expiration setting.                  |
| **`olderThanTimestamp`**    | A human-readable timestamp before which snapshots will be removed (e.g., `2024-12-01T00:00:00Z`).  |
| **`snapshotIds`**           | Specifies the list of specific snapshots to expire.                                                                                                               |
| **`retainLast`**            | Number of ancestor snapshots to preserve regardless of `olderThanMillis`. (Defaults to 1)                                                                        |
| **`max_concurrent_deletes`**| Size of the thread pool used for delete file actions. (By default, no thread pool is used.)                                                                      |
| **`streamDeleteResults`**   | By default, all files to delete are brought to the driver at once, which may cause memory issues with large file lists. Set to `true` to use `toLocalIterator`. |


## Examples

### **`olderThanMillis`**

!!! info

    `expireOlderThan` is only available in Flare 6. Use `olderThanMillis` in place of `expireOlderThan` in Flare 5.0 (image tag: `7.3.21`). 

The `olderThanMillis` attribute specifies a cutoff timestamp in unix format. Snapshots created before this timestamp are considered expired and will be deleted, along with their associated metadata and manifest files, if no longer referenced. This helps manage storage and keep the table metadata clean by removing historical data no longer needed for rollback or time travel.

```yaml
name: wf-expire-snapshots                           # Name of the Workflow
version: v1                                         # Version
type: workflow                                      # Type of Resource (Here its workflow)
tags:                                               # Tags
  - expire
workflow:                                           # Workflow Section
  title: expire snapshots                           # Title of the DAG
  dag:                                              # Directed Acyclic Graph (DAG)
    - name: expire                                  # Name of the Job
      title: expire snapshots                       # Title of the Job
      spec:                                         # Specs
        tags:                                       # Tags
          - Expire
        stack: flare:6.0                            # Stack is Flare (so its a Flare Job)
        compute: runnable-default                   # Compute
        stackSpec:                                  # Flare Stack specific Section
          job:                                      # Job Section
            explain: true                           # Explain
            logLevel: INFO                          # Loglevel
            inputs:                                 # Inputs Section
              - name: inputDf                       # Input Dataset Name
                dataset: dataos://lakehouse:retail/pos_store_product_cust?acl=rw        # Input UDL
                format: Iceberg                     # Format
            actions:                                # Action Section
              - name: expire_snapshots              # Name of Flare Action
                input: inputDf                      # Input Dataset Name
                options:                            # Options
                  olderThanMillis: "1741987433222"  # Timestamp in Unix Format (All snapshots older than the timestamp are expired)

```

### **`olderThanMillis`** with **`retainLast`**

Remove snapshots older than specific day and time, but retain the last 5 snapshots:


```yaml
name: wf-expire-snapshots                        # Name of the Workflow
version: v1                                      # Version
type: workflow                                   # Type of Resource (Here its workflow)
tags:                                            # Tags
  - expire
workflow:                                        # Workflow Section
  title: expire snapshots                        # Title of the DAG
  dag:                                           # Directed Acyclic Graph (DAG)
    - name: expire                               # Name of the Job
      title: expire snapshots                    # Title of the Job
      spec:                                      # Specs
        tags:                                    # Tags
          - Expire
        stack: flare:6.0                         # Stack is Flare (so its a Flare Job)
        compute: runnable-default                # Compute
        stackSpec:                               # Flare Stack specific Section
          job:                                   # Job Section
            explain: true                        # Explain
            logLevel: INFO                       # Loglevel
            inputs:                              # Inputs Section
              - name: inputDf                    # Input Dataset Name
                dataset: dataos://lakehouse:retail/pos_store_product_cust?acl=rw    # Input UDL
                format: Iceberg                  # Format
            actions:                             # Action Section
              - name: expire_snapshots           # Name of Flare Action
                input: inputDf                   # Input Dataset Name
                options:                         # Options
                  olderThanMillis: "1741987433222"    # Timestamp in Unix Format (All snapshots older than the timestamp are expired)
                  retainLast: 5                       # Retain the last 5 snapshots
```

### **`snapshotIds`**

Remove snapshots with snapshot ID 12345679 (note that this snapshot ID should not be the current snapshot):

```yaml
name: wf-expire-snapshots-10                     # Name of the Workflow
version: v1                                      # Version
type: workflow                                   # Type of Resource (Here its workflow)
tags:                                            # Tags
  - expire
workflow:                                        # Workflow Section
  title: expire snapshots                        # Title of the DAG
  dag:                                           # Directed Acyclic Graph (DAG)
    - name: expire                               # Name of the Job
      title: expire snapshots                    # Title of the Job
      spec:                                      # Specs
        tags:                                    # Tags
          - Expire
        stack: flare:6.0                         # Stack is Flare (so its a Flare Job)
        compute: runnable-default                # Compute
        stackSpec:                               # Flare Stack specific Section
          job:                                   # Job Section
            explain: true                        # Explain
            logLevel: INFO                       # Loglevel
            inputs:                              # Inputs Section
              - name: inputDf                    # Input Dataset Name
                dataset: dataos://lakehouse:sandbox3/test_pyflare2?acl=rw    # Input UDL
                format: Iceberg                  # Format
            actions:                             # Action Section
              - name: expire_snapshots           # Name of Flare Action     
                input: inputDf                   # Input Dataset Name                     # mandatory
                options:                         # Options                                # mandatory
                  snapshotIds:                   # Snapshots to delete by ID
                    - "12345679"                 # Snapshot with given snapshot ID will be deleted

```


You can also provide multiple snapshot Ids:

```yaml
actions:                                         # Action Section
  - name: expire_snapshots                       # Name of Flare Action     
    input: inputDf                               # Input Dataset Name    (mandatory)
    options:                                     # Options               (mandatory)
      snapshotIds:                               # Snapshots to delete by ID
        - "1234567912"                           # Snapshot with given snapshot ID will be deleted
        - "1122344342"                           # Snapshot with given snapshot ID will be deleted

```


### **olderThanTimestamp**

```yaml
name: expire-04                                  # Name of the Workflow
version: v1                                      # Version
type: workflow                                   # Type of Resource (Here its workflow)
tags:                                            # Tags
  - expire
workflow:                                        # Workflow Section
  title: expire snapshots                        # Title of the DAG
  dag:                                           # Directed Acyclic Graph (DAG)
    - name: expire                               # Name of the Job
      title: expire snapshots                    # Title of the Job
      spec:                                      # Specs
        tags:                                    # Tags
          - Expire
        stack: flare:6.0                         # Stack is Flare (so its a Flare Job)
        compute: runnable-default                # Compute
        stackSpec:                               # Flare Stack specific Section
          job:                                   # Job Section
            explain: true                        # Explain
            logLevel: INFO                       # Loglevel
            inputs:                              # Inputs Section
              - name: inputDf                    # Input Dataset Name
                dataset: dataos://lakehouse:retail/pos_store_product_cust?acl=rw    # Input UDL
                format: Iceberg                  # Format
            actions:                             # Action Section
              - name: expire_snapshots           # Name of Flare Action
                input: inputDf                   # Input Dataset Name
                options:                         # Options
                  olderThanTimestamp: '2025-04-19 00:00:00.000'    # Timestamp (All snapshots older than the timestamp are expired)
                  retainLast: 2                                       # Retain the last 2 snapshots

```


