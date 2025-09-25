---
description: >-
  This document outlines best practices for configuring and operating Nilus within the DataOS platform.
---

# Best Practices

Following the given recommendations helps ensure stable behavior, avoids runtime warnings, and supports efficient execution of data pipelines.



## 1. Identifier Normalization

**Purpose:** Avoid unexpected transformations due to automatic normalization of identifiers.

* Use **underscores (`_`)** instead of **hyphens (-)** in all custom identifiers, such as:
    * `dataset_name`
    * `destination_table`
    * `topic_prefix`
* Hyphens are automatically converted to underscores during runtime, which can affect:
    * Database schema names
    * Folder paths
* This transformation **does not** alter the original configuration in the pipeline manifest.

**Example Warning:**

```bash
[WARNING]|_normalize_identifier:243|Due to normalization dataset name got changed from 'A-test-01' to 'a_test_01'...
```

**Recommendation:**

Avoid using hyphens in identifiers to prevent normalization and potential naming mismatches.



## 2. Replication Slot Management (PostgreSQL CDC Service)

**Purpose:** Prevent conflicts and ensure consistent replication behavior in Change Data Capture Service.

* Each **CDC Service** must be assigned a **unique replication slot**.
* Reusing a replication slot across services may result in:
    * Replication state conflicts
    * Duplicate or inconsistent data
    * Service errors

**Example Error:**

```bash
ERROR: replication slot "abc_test_01" is active for PID 1092637
```

**Recommendation:**

Define a dedicated replication slot per CDC Service to maintain accurate state tracking and avoid replication overlap.



## 3. Defining Incremental and Primary Keys in Batch Workflow

**Purpose:** Enable accurate delta processing and maintain data integrity in Nilus batch workflows.

* Explicitly declare both `primary-key` and `incremental-key` under `source.options`.
* These keys determine:
    * How data changes are identified between runs
    * Uniqueness and deduplication logic

**Example Manifest:**

```yaml
name: nilus-batch-pg-test
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Service Sample
workspace: public
workflow:
  schedule:
    cron: '*/4 * * * *'
    concurrencyPolicy: Allow

  dag:
    - name: batch-job-01
      spec:
        stack: nilus:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
        logLevel: INFO
        stackSpec:
          source:
            address: dataos://ncdcpostgres
            options:
              source-table: ecom.product
              primary-key: "id"
              incremental-key: "id"

          sink:
            address: dataos://testinglh
            options:
              dest-table: B_007_batch.ecom_product_test
              incremental-strategy: append
              aws_region: us-west-2
```

**Recommendation:**

Always specify both `primary-key` and `incremental-key`. Omitting these keys can result in faulty delta detection and incorrect replication.



## 4. Specifying Heartbeat Settings in PostgreSQL CDC Service

**Purpose:** Maintain real-time change data capture (CDC) synchronization and regularly check the health of replication streams.

* Always define both `heartbeat.interval.ms` and `topic.heartbeat.prefix` under `source.options`.
* These properties help maintain reliable CDC operations by:
    * Detecting connectivity issues between source and sink
    * Emitting regular heartbeat messages even during periods of low change volume

**Example Manifest:**

```yaml
name: ${{service-name}}                                    # Service identifier
version: v1                                                # Version of the service
type: service                                              # Defines the resource type
tags:                                                      # Classification tags
    - ${{tag}}                                              
    - ${{tag}}                                              
description: Nilus CDC Service for Postgres description    # Description of the service
workspace: public                                          # Workspace where the service is deployed

service:                                                   # Service specification block
  servicePort: 9010                                        # Service port
  replicas: 1                                              # Number of replicas
  logLevel: INFO                                           # Logging level
  compute: ${{query-default}}                              # Compute profile
  persistentVolume:                                        # Persistent volume configuration
    name: ${{ncdc-vo1-01}}                                 # Volume name (multiple options commented)
    directory: ${{nilus_01}}                               # Target directory within the volume
  stack: nilus:3.0                                         # Nilus stack version
  stackSpec:                                               # Stack specification
    source:                                                # Source configuration block
      address: dataos://postgresdepot                      # Source depot address/UDL
      options:                                             # Source-specific options
        engine: debezium                                   # Required for CDC; not used for batch ingestion
        table.include.list: "public.customers"             # Tables to include from source
        topic.prefix: "cdc_changelog"                      # Required topic prefix, can be customized 
        slot.name: "test3"                                 # Required replication slot name, must be unique  
        heartbeat.interval.ms: 60000                       # Required heartbeat interval (ms)
        topic.heartbeat.prefix: "nilus_heartbeat"          # Required heartbeat topic prefix
    sink:                                                  # Sink configuration block
      address: dataos://testinghouse                       # Sink DataOS Lakehouse address
      options:                                             # Sink-specific options
        dest-table: pgdb_lenovo_test_004                   # Destination table name in sink
        incremental-strategy: append                       # Append mode for CDC write strategy
        aws_region: us-west-2                              # AWS region for S3-backed DataOS Lakehouse
```

**Recommendation:**

Always include `heartbeat.interval.ms` and `topic.heartbeat.prefix` in CDC for PostgreSQL. Their absence can lead to undetected pipeline failures or broken replication streams.