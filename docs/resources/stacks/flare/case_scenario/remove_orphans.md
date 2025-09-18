# Remove Orphans

The [`remove_orphans` action](/resources/stacks/flare/configurations/#remove_orphans) cleans up orphans files older than a specified time period. This action may take a long time to finish if you have lots of files in data and metadata directories. It is recommended to execute this periodically, but you may not need to execute this often. 

!!! note 

    - It is dangerous to remove orphan files with a retention interval **shorter** than the time expected for any write to complete; in-progress files might be treated as orphans and deleted, potentially corrupting the table.
    
    - The **default retention interval is 3 days** (if not explicitly set).

**Get the list of snapshots by using the following command**

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

| Attribute              | Type       | Description                                                                                          |
| ---------------------- | ---------- | ---------------------------------------------------------------------------------------------------- |
| `olderThanMillis`      | string/int | Remove orphan files created **before** this Unix epoch (milliseconds).                               |
| `olderThanTimestamp`   | string     | Remove orphan files created **before** this timestamp (e.g., `2024-12-01 00:00:00.000`).             |
| `location`             | string     | Directory to look for files in. Defaults to the table’s location.                                    |
| `dryRun`               | boolean    | If `true`, performs a dry run without actually removing files. Defaults to `false`.                  |
| `maxConcurrentDeletes` | int        | Size of the thread pool used for delete operations. By default, no thread pool is used (sequential). |


<!-- actions:
- name: remove_orphans
  input: input
  options:
    dryRun: true
    olderThanTimestamp: '2024-01-18 09:00:00.000'
    olderThanMillis: '1705599997318'
    location: 'path-to-file'
    maxConcurrentDeletes: 2 -->


The following code snippet demonstrates removing orphan files for different attribute format. The task relies on the `remove_orphans` action, which requires the inputDf dataset as an input. This dataset is defined as `dataos://lakehouse:retail/city` and is in Iceberg format. 

```yaml
name: orphans                                    # Name of the Workflow
version: v1                                      # Version
type: workflow                                   # Type of Resource (Here its workflow)
tags:                                            # Tags
  - orphans
workflow:                                        # Workflow Section
  title: Remove orphan files                     # Title of the DAG
  dag:                                           # Directed Acyclic Graph (DAG)
    - name: orphans                              # Name of the Job
      title: Remove orphan files                 # Title of the Job
      spec:                                      # Specs
        tags:                                    # Tags
          - orphans
        stack: flare:7.0                         # Stack is Flare
        compute: runnable-default                # Compute
        stackSpec:                               # Flare Stack Specific Section
          job:                                   # Job Section
            explain: true                        # Explain
            logLevel: INFO                       # Loglevel
            inputs:                              # Inputs Section
              - name: inputDf                    # Input Dataset Name
                dataset: ${{dataos://lakehouse:retail/city }}               # Input UDL
                format: ${{Iceberg}}                  # Format
            actions:                             # Flare Action
              - name: remove_orphans             # Action Name
                input: inputDf                   # Input Dataset Name
                options:                         # Options
                  olderThanMillis: '1740643647492'  # Timestamp in Unix Format
                  # olderThanTimestamp: '2021-06-30 00:00:00.000'
                  # location: 'path-to-file'
                  # dryRun: false
                  # maxConcurrentDeletes: 2
```

### **`olderThanMillis`**

Expire orphan files created before a Unix epoch (milliseconds):

```yaml
name: orphans-millis
version: v1
type: workflow
tags:
  - orphans
workflow:
  title: Remove orphan files (olderThanMillis)
  dag:
    - name: orphans
      title: Remove orphan files
      spec:
        tags:
          - orphans
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            logLevel: INFO
            inputs:
              - name: inputDf
                dataset: dataos://icebase:actions/random_users_data
                format: Iceberg
            actions:
              - name: remove_orphans
                input: inputDf
                options:
                  olderThanMillis: '1646309607000'   # snapshots older than this epoch are considered orphans
```

---

### **`olderThanTimestamp`**

Use a human-readable timestamp:

```yaml
name: orphans-ts
version: v1
type: workflow
tags:
  - orphans
workflow:
  title: Remove orphan files (olderThanTimestamp)
  dag:
    - name: orphans
      title: Remove orphan files
      spec:
        tags:
          - orphans
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            logLevel: INFO
            inputs:
              - name: inputDf
                dataset: dataos://icebase:actions/random_users_data
                format: Iceberg
            actions:
              - name: remove_orphans
                input: inputDf
                options:
                  olderThanTimestamp: '2021-06-30 00:00:00.000'  # do not set olderThanMillis together with this
```

### **`dryRun`**

Preview deletions without removing files:

```yaml
name: orphans-dry-run
version: v1
type: workflow
tags:
  - orphans
workflow:
  title: Remove orphan files (dry run)
  dag:
    - name: orphans
      title: Remove orphan files
      spec:
        tags:
          - orphans
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            logLevel: INFO
            inputs:
              - name: inputDf
                dataset: dataos://icebase:actions/random_users_data
                format: Iceberg
            actions:
              - name: remove_orphans
                input: inputDf
                options:
                  olderThanTimestamp: '2021-06-30 00:00:00.000'
                  dryRun: true                          # report-only; no files are deleted
```



### **`location`**

Target a specific directory (overrides table location):

```yaml
name: orphans-location
version: v1
type: workflow
tags:
  - orphans
workflow:
  title: Remove orphan files (custom location)
  dag:
    - name: orphans
      title: Remove orphan files
      spec:
        tags:
          - orphans
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            logLevel: INFO
            inputs:
              - name: inputDf
                dataset: dataos://icebase:actions/random_users_data
                format: Iceberg
            actions:
              - name: remove_orphans
                input: inputDf
                options:
                  olderThanMillis: '1646309607000'
                  location: '${{path to file}}'  # adjust for your storage
```



### **`maxConcurrentDeletes`**

Speed up deletes using a small thread pool:

```yaml
name: orphans-concurrency
version: v1
type: workflow
tags:
  - orphans
workflow:
  title: Remove orphan files (concurrent deletes)
  dag:
    - name: orphans
      title: Remove orphan files
      spec:
        tags:
          - orphans
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            logLevel: INFO
            inputs:
              - name: inputDf
                dataset: dataos://icebase:actions/random_users_data
                format: Iceberg
            actions:
              - name: remove_orphans
                input: inputDf
                options:
                  olderThanTimestamp: '2021-06-30 00:00:00.000'
                  maxConcurrentDeletes: 2     # tune based on cluster I/O and rate limits
```

!!! tip

    - Start with **2–4** threads and observe driver/executor and storage system utilization. Increase gradually if stable.
    - Combine `dryRun: true` with `maxConcurrentDeletes` during validation to estimate run duration without risk.



## Best Practices

* **Choose exactly one cutoff**: set **either** `olderThanMillis` **or** `olderThanTimestamp`.
* **Safety first**: for active tables, use a conservative cutoff (≥ 72 hours) to avoid racing in-flight writes.
* **Pilot with `dryRun`**: verify counts/paths before enabling deletion.
* **Scope with `location`**: helpful when table directories contain auxiliary data you want to exclude/include deliberately.
* **Tune concurrency carefully**: avoid overwhelming your object store or hitting API rate limits.

