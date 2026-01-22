# Nilus Configurations

## CDC Service Config

For Change Data Capture, Nilus is orchestrated via the **Service** resource. The example below demonstrates a service configured to monitor a MongoDB collection and capture change events in the DataOS Lakehouse.

---

### **Example CDC Manifest Configuration**

```yaml
name: ${{service-name}}                                    # Service identifier
version: v1                                                # Version of the service
type: service                                              # Defines the resource type
tags:                                                      # Classification tags
  - ${{tag}}
  - ${{tag}}
description: Nilus CDC Service for MongoDB description     # Description of the service
workspace: public                                          # Workspace where the service is deployed

service:                                                   # Service specification block
  servicePort: 9010                                        # Service port
  replicas: 1                                              # Number of replicas
  logLevel: INFO                                           # Logging level
  compute: ${{query-default}}                              # Compute type
  resources:                                               # Resource requests (optional but recommended)
    requests:
      cpu: 100m                                            # Requested CPU
      memory: 128Mi                                        # Requested memory
  stack: nilus:3.0                                         # Nilus stack version
  stackSpec:                                               # Stack specification
    source:                                                # Source configuration block
      address: ${{source_depot_address/UDL}}               # Source depot address/UDL
      options:                                             # Source-specific options
        engine: debezium                                   # Required CDC engine; used for streaming changes
        collection.include.list: "retail.products"         # MongoDB collections to include
        topic.prefix: "cdc_changelog"                      # Required topic prefix for CDC stream
        max-table-nesting: "0"                             # Optional; prevents unnesting of nested documents
        transforms.unwrap.array.encoding: array            # Optional; preserves arrays in sink as-is
    sink:                                                  # Sink configuration for CDC output
      address: ${{sink_depot_address/UDL}}                 # Sink depot address
      options:                                             # Sink-specific options
        dest-table: mdb_test_001                           # Destination table name in the sink depot
        incremental-strategy: append                       # Append-only strategy for streaming writes
```

---

## CDC Configuration Attributes

### **1. Metadata**

| Field         | Description               |
| ------------- | ------------------------- |
| `name`        | Unique service identifier |
| `version`     | Configuration version     |
| `type`        | Must be `service`         |
| `tags`        | Classification tags       |
| `description` | Describes the service     |
| `workspace`   | Namespace for the service |

---

### **2. Service Specification**

| Field                | Description                                                                         |
| -------------------- | ----------------------------------------------------------------------------------- |
| `servicePort`        | Internal port exposed by the service                                                |
| `replicas`           | Number of instances to run                                                          |
| `logLevel`           | Logging verbosity level                                                             |
| `compute`            | Compute profile for workload placement                                              |
| `resources.requests` | Guaranteed compute resources                                                        |
| `resources.limits`   | Max compute resources allowed                                                       |
| `stack`              | Specifies the stack to use. Check all available Nilus stacks in the Operations App. |

---

### **3. Stack Specification**

#### 3.1 Source

The `source` section defines how to connect to the source system (MongoDB in this example).

```yaml
source:
  address: dataos://testingmongocdc
  options:
    engine: debezium
    collection.include.list: "sample.unnest"
    topic.prefix: "cdc_changelog"
    max-table-nesting: "0"
    transforms.unwrap.array.encoding: array
```

**Address**

* Can be:

  * A **Depot path** (as shown above)
  * A **connection string** (for direct connections)

!!! info 
    When sourcing from a Depot, no dataosSecrets are required.

**Options**

| Option                             | Description                                                                                                                                                                         | Required      |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `engine`                           | Must be `debezium` to enable CDC processing                                                                                                                                         | Yes           |
| `collection.include.list`          | List of MongoDB collections to monitor (namespace: collection)                                                                                                                      | Yes           |
| `topic.prefix`                     | Prefix for CDC topics; appended to the final dataset name in the sink                                                                                                               | Yes           |
| `max-table-nesting`                | Degree of JSON nesting to unnest (MongoDB specific).<br>• Accepts string digits: `"0"`, `"1"`, etc.<br>• `"0"` means no unnesting.<br>• Higher values control recursive flattening. | Optional      |
| `transforms.unwrap.array.encoding` | Controls encoding for array elements                                                                                                                                                | Optional      |
| Other source-specific options      | Vary depending on the source database. Refer to Nilus documentation or your DataOS contact.                                                                                         | As applicable |

---

#### 3.2 Sink

The `sink` section defines where the captured change data will be written.

```yaml
sink:
  address: dataos://testinglh
  options:
    dest-table: mdb_test
    incremental-strategy: append
    aws_region: us-west-2
```

**Options**

| Field                                   | Description                                               |
| --------------------------------------- | --------------------------------------------------------- |
| `address`                               | Target Lakehouse address                                  |
| `dest-table`                            | Schema and table to write change records                  |
| `incremental-strategy`                  | Defines write mode; `append` for CDC is common            |
| Additional options (e.g., `aws_region`) | Sink-specific configurations (depends on Lakehouse setup) |

---

## Batch Workflow Config

For batch data movement, Nilus is orchestrated using the **Workflow** resource. The example below demonstrates a workflow configured to ingest data from Salesforce and load it into the DataOS Lakehouse.

---

### **Example Batch Manifest Configuration**

```yaml
name: salesforce-account-wf-test                     # Workflow identifier
version: v1                                          # Workflow version
type: workflow                                       # Defines the resource type
tags:                                                # Classification tags
  - salesforce_account
  - nilus_batch
  - client_lakehouse

workflow:                                            # Workflow specification block
  # schedule:                                        # Optional: Workflow schedule
  #   cron: '55 08 * * *'                            # Run every day at 08:55 UTC
  #   endOn: 2025-12-31T23:59:45Z                    # Optional end time for the schedule
  #   concurrencyPolicy: Forbid                     # Prevent concurrent runs

  dag:                                               # Directed Acyclic Graph definition
    - name: sf-ac                                    # DAG node name
      spec:                                          # Node specification
        stack: nilus:1.0                             # Nilus stack version
        compute: runnable-default                    # Compute profile for execution
        resources:                                   # Resource requests (optional but recommended)
          requests:
            cpu: 100m                                # Requested CPU
            memory: 128Mi                            # Requested memory
        logLevel: INFO                               # Logging verbosity level

        dataosSecrets:                               # Secrets for source connectivity
          - name: salesforce-sandbox                 # DataOS secret name
            allKeys: true                            # Mount all secret keys
            consumptionType: envVars                 # Inject secrets as environment variables

        stackSpec:                                   # Stack specification
          source:                                    # Source configuration
            address: "salesforce://?username={SALESFORCE_USERNAME}&password={SALESFORCE_PASSWORD}&token={SALESFORCE_TOKEN}&domain={SALESFORCE_DOMAIN}"
                                                      # Salesforce connection string
            options:                                 # Source-specific options
              source-table: "account"                # Salesforce object/table to ingest

          sink:                                      # Sink configuration
            address: dataos://client                 # Target Lakehouse address
            options:                                 # Sink-specific options
              dest-table: dev.accounts_test           # Destination schema and table
              incremental-strategy: append            # Append new data
```

---

## Batch Configuration Attributes

### **1. Metadata**

| Field     | Description                                     |
| --------- | ----------------------------------------------- |
| `name`    | Unique name of the workflow                     |
| `version` | Workflow version identifier                     |
| `type`    | Must be `workflow`                              |
| `tags`    | Categorization tags for search and organization |

---

### **2. Workflow Definition**

#### 2.1 Schedule (Optional)

Defines when and how often the workflow runs.

```yaml
schedule:
  cron: '55 08 * * *'
  endOn: 2025-12-31T23:59:45Z
  concurrencyPolicy: Forbid
```

!!! info
    If not defined, the workflow must be triggered manually.

---

#### 2.2 DAG (Directed Acyclic Graph)

Defines the processing steps in the workflow.

```yaml
dag:
  - name: sf-ac
    spec:
      ...
```

---

#### 2.3 Stack

Specifies the stack to use. Check all available Nilus stacks in the Operations App.

```yaml
stack: nilus:1.0
```

---

#### 2.4 Compute

Defines which compute profile to use. Check all available computes in the Operations App.

```yaml
compute: runnable-default
```

---

#### 2.5 Resources

Specifies resource requests (optional, but recommended):

```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
```

---

#### 2.6 logLevel

Controls the logging level (optional):

```yaml
logLevel: <INFO/DEBUG/ERROR>
```

---

#### 2.7 dataosSecrets (Needed only when not working with Depot)
    
Defines secret references required for source connectivity (if applicable)

```yaml
dataosSecrets:
  - name: salesforce-sandbox
    allKeys: true
    consumptionType: envVars
```

!!! info
    If using a Depot as the source, this section is not required.

---

### **3. Stack Specification**

#### 3.1 Source

Defines the source connection for ingestion.

```yaml
source:
  address: "salesforce://?username={SALESFORCE_USERNAME}&password={SALESFORCE_PASSWORD}&token={SALESFORCE_TOKEN}&domain={SALESFORCE_DOMAIN}"
  options:
    source-table: "account"
```

**Options**

| Field Name             | Type         | is_required? | Description                                                            |
| ---------------------- | ------------ | ------------ | ---------------------------------------------------------------------- |
| `source-table`         | string       | YES          | Source table/entity. Use schema.table or prefix with `query:` for SQL. |
| `primary-key`          | string       | NO           | Primary key for deduplication. Comma-separated for multiple keys.      |
| `incremental-key`      | string       | NO           | Column used for incremental loads.                                     |
| `interval-start`       | string       | NO           | Start of time range (ISO).                                             |
| `interval-end`         | string       | NO           | End of time range (ISO).                                               |
| `type-hints`           | object       | NO           | Destination type overrides.                                            |
| `page-size`            | int          | NO           | Rows per page fetched. Default: 50000.                                 |
| `extract-parallelism`  | int          | NO           | Parallel extract workers. Default: 5.                                  |
| `sql-reflection-level` | enum         | NO           | none, fast, full (default).                                            |
| `sql-limit`            | int          | NO           | Max rows to read.                                                      |
| `sql-exclude-columns`  | list[string] | NO           | Columns to exclude.                                                    |
| `yield-limit`          | int          | NO           | Max pages yielded.                                                     |
| `mask`                 | object       | NO           | Column masking rules.                                                  |
| `max-table-nesting`    | int          | NO           | Max nesting depth. Default: 0.                                         |

!!! info
    Default behavior for NULL columns:

    - SQL/schema-known sources preserve null columns.
    - Semi-structured sources materialize columns only when values appear, unless overridden via `type-hints`.
    

---

#### 3.2 Sink

Defines the target where data will be written.

```yaml
sink:
  address: dataos://demolakehouse
  options:
    dest-table: retai.accounts_test
    incremental-strategy: append
```

**Options**

| Field Name             | Type   | is_required? | Description                       |
| ---------------------- | ------ | ------------ | --------------------------------- |
| `dest-table`           | string | YES          | Destination table (schema.table). |
| `incremental-strategy` | enum   | YES          | append, replace, merge.           |
| `aws_region`           | string | NO           | Override AWS region.              |
| `partition-by`         | string | NO           | Partition column.                 |
| `cluster-by`           | string | NO           | Cluster/sort column.              |
| `full-refresh`         | bool   | NO           | Reload all data.                  |
| `staging_bucket`       | string | NO           | Temporary bucket.                 |
| `loader-file-size`     | int    | NO           | Target rows per output file.      |
