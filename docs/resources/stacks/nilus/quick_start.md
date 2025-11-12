---
description: Welcome to the Nilus Quick Start Guide!
---

# Quick Start

This page will help you onboard rapidly and begin moving data with Nilus using either Batch Ingestion or Change Data Capture (CDC). Whether you're syncing large historical datasets or streaming real-time updates, Nilus makes data movement into DataOS Lakehouse and other destinations simple, secure, and scalable.

## Change Data Capture (CDC)

CDC identifies and streams row-level changes (inserts, updates, and deletes) from a source database to a target system, keeping the target system up to date without requiring full reloads.

!!! info
    This Quick Start example displays MongoDB as the source system and DataOS Lakehouse as the destination system. To explore more source and destination options, visit:

    * [Supported CDC Source](/resources/stacks/nilus/cdc_sources/)
    * [Supported Destination](/resources/stacks/nilus/supported_destinations/)

### **Prerequisites**

The following are mandatory requirements that need to be completed to make CDC work:

**MongoDB Replica Set**

* MongoDB **must run as a replica set**, even for single-node deployments.
* Nilus CDC for MongoDB relies on the `oplog.rs` collection, which is only available in replica sets.

**Enable `oplog` Access**

* Nilus uses MongoDB's `oplog.rs` to capture changes.
*   Nilus requires a user with `read` access to business data and internal system databases to access the `oplog`.
    If the user is not created, create a user in MongoDB using the following:

    ```javascript
    db.createUser({
      user: "debezium",
      pwd: "dbz",
      roles: [
        { role: "read", db: "your_app_db" },      // Read target database
        { role: "read", db: "local" },            // Read oplog
        { role: "read", db: "config" },           // Read cluster configuration
        { role: "readAnyDatabase", db: "admin" }, // Optional: discovery
        { role: "clusterMonitor", db: "admin" }   // Recommended: monitoring
      ]
    })
    ```

!!! info
    Grant only the roles required for your environment to follow the principle of least privilege.


**Pre-created MongoDB Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
|    NAME      | VERSION | TYPE  | STATUS | OWNER    |
| ------------ | ------- | ----- | ------ | -------- |
| mongodbdepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create:

??? note "MongoDB Depot Manifest"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    tags:
      - ${{tag1}}
      - ${{tag2}}
    layer: user
    depot:
      type: mongodb                                 
      description: ${{description}}
      compute: ${{runnable-default}}
      mongodb:                                          
        subprotocol: ${{\"mongodb+srv\"}}
        nodes: ${{[\"clusterabc.ezlggfy.mongodb.net\"]}}
      external: ${{true}}
      secrets:
        - name: ${{instance-secret-name}}-r
          allkeys: ${{true}}

        - name: ${{instance-secret-name}}-rw
          allkeys: ${{true}}
    ```

    !!! info
        Update variables such as `name`, `owner`, `compute`, `layer`, etc., and contact the DataOS Administrator or Operator to obtain the appropriate secret name.

### **CDC Manifest Configuration**

The following manifest defines a Nilus CDC service that captures changes from a MongoDB source and persists them into the DataOS Lakehouse (S3 Iceberg).

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

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


The above sample manifest file is deployed using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Service YAML}}
```

The MongoDB host used in the CDC service YAML must exactly match the host defined during replica set initiation.

### **CDC Attribute Details**

This section outlines the necessary attributes of Nilus CDC Service.

??? info "Attribute Details"

    **Metadata Fields**

    | Field Name | Description |
    |-----------|-------------|
    | `name` | Unique service identifier |
    | `version` | Configuration version |
    | `type` | Must be `service` |
    | `tags` | Classification tags |
    | `description` | Describes the service |
    | `workspace` | Namespace for the service |

    **Service Specification Fields**

    | Field Name           | Description                              |
    | -------------------- | ---------------------------------------- |
    | `servicePort`        | Internal port exposed by the service     |
    | `replicas`           | Number of instances to run               |
    | `logLevel`           | Logging verbosity level                  |
    | `compute`            | Compute type for workload placement   |
    | `resources.requests` | Guaranteed compute resources             |
    | `resources.limits`   | Max compute resources allowed            |
    | `stack`              | Specifies the stack to use with version. |

    **Source Configuration Fields**

    | Field Name                         | Description                                                                                                                                                                                                                                                                                                                                                       | Required |
    | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
    | `address`                          | The address to the source<br>1. Can be connected using a Depot<br>2. Can be connected directly using connection string, but it will need a secret                                                                                                                                                                                                          | Yes      |
    | `engine`                           | Must be `debezium` to enable CDC processing                                                                                                                                                                                                                                                                                                                       | Yes      |
    | `collection.include.list`          | List of database collections to monitor (namespace: collection) (example MongoDB)                                                                                                                                                                                                                                                                                 | Yes      |
    | `table.include.list`               | List of database tables to monitor (sandbox.customers) (example SQL Server)                                                                                                                                                                                                                                                                                       | Yes      |
    | `topic.prefix`                     | Prefix for CDC topics; appended to the final dataset name in the sink                                                                                                                                                                                                                                                                                             | Yes      |
    | `max-table-nesting`                | Degree of JSON nesting to unnest (MongoDB specific).<br>• Accepts string representation of digits: `"0"`, `"1"`, etc.<br>• Default is 0 if no value is set<br>• `"0"` means **no unnesting** (nested fields will be left as-is).<br>• Higher values control recursive flattening for nested documents. | Optional |
    | `transforms.unwrap.array.encoding` | Controls encoding for array elements                                                                                                                                                                                                                                                                                                                              | Optional |

    **Sink Configuration Fields**

    | Field Name             | Description                                                                 | Required |
    | ---------------------- | --------------------------------------------------------------------------- | -------- |
    | `address`              | Target address (DataOS Lakehouse as example)                                | Yes      |
    | `dest-table`           | Schema to write change records. Table name will fetched from `topic.prefix` | Yes      |
    | `incremental-strategy` | Defines write mode; append is preferred for CDC                             | Yes      |

## Batch Ingestion

Batch ingestion transfers data from sources to the destination system on a scheduled basis (hourly, daily, or weekly).

!!! info
    This Quick Start example displays MongoDB as the source system and DataOS Lakehouse as the destination system. To explore more source and destination options, visit:

    * [Supported Batch Source](/resources/stacks/nilus/batch_sources/)
    * [Supported Destination](/resources/stacks/nilus/supported_destinations/)

### **Prerequisites**

The following are the requirements for enabling Batch Data Movement in MongoDB:

**Database User Permissions**

The connection user must have at least **read** privileges on the source collection:

```jsx
{
  "role": "read",
  "db": "<database_name>",
  "collection": "<collection_name>"
}
```

**Pre-created MongoDB Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
|    NAME      | VERSION | TYPE  | STATUS | OWNER    |
| ------------ | ------- | ----- | ------ | -------- |
| mongodbdepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create:

??? note "MongoDB Depot Manifest"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    tags:
      - ${{tag1}}
      - ${{tag2}}
    layer: user
    depot:
      type: mongodb                                 
      description: ${{description}}
      compute: ${{runnable-default}}
      mongodb:                                          
        subprotocol: ${{\"mongodb+srv\"}}
        nodes: ${{[\"clusterabc.ezlggfy.mongodb.net\"]}}
      external: ${{true}}
      secrets:
        - name: ${{instance-secret-name}}-r
          allkeys: ${{true}}

        - name: ${{instance-secret-name}}-rw
          allkeys: ${{true}}
    ```

    !!! info
        Update variables such as `name`, `owner`, `compute`, `layer`, etc., and contact the DataOS Administrator or Operator to obtain the appropriate secret name.

### **Batch Manifest Configuration**

The following manifest defines a Nilus Batch Workflow that transfers data from a MongoDB source into the DataOS Lakehouse (S3 Iceberg).

```yaml
name: nb-mdb-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for MongoDB to S3 Lakehouse
workspace: research
workflow:
  dag:
    - name: nb-job-01
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
            address: dataos://mongodbdepot
            options:
              source-table: "retail.customer"
          sink:
            address: dataos://testinglh
            options:
              dest-table: mdb_retail.batch_customer_1
              incremental-strategy: replace

```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.

The above sample manifest file is deployed using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Service YAML}}
```

### **Batch Attribute Details**

This section outlines the necessary attributes of Nilus Batch Workflow.

??? info "Attribute Details"

    **Metadata Fields**

    | Field Name | Description                                     |
    | ---------- | ----------------------------------------------- |
    | `name`     | Unique name of the batch workflow               |
    | `version`  | Batch workflow version identifier               |
    | `type`     | Must be `workflow`                              |
    | `tags`     | Categorization tags for search and organization |

    **Workflow Specification Fields**

    | Field Name      | Description                                                                                                                                                                                          |
    | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `schedule`      | Defines the frequency and schedule for workflow runs. This parameter is optional. If not specified, the workflow is triggered only once at run time.                                                 |
    | `dag`           | dag (Directed Acyclic Graph) specifies the sequence of processing steps in the workflow.                                                                                                             |
    | `stack`         | Identifies the Nilus stack to be used. Available versions can be viewed in the Operations App.                                                                                                       |
    | `compute`       | Defines the Compute type to be used. Available profiles can be viewed in the Operations App.                                                                                                      |
    | `resources`     | Specifies the resources allocated to complete the batch workflow. This parameter is optional.                                                                                                        |
    | `loglevel`      | Defines the level of logging to be applied for the workflow.                                                                                                                                         |
    | `dataosSecrets` | Points to the secret resource that stores credentials required to connect to a source. This is applicable for non-depotable sources. If the source supports a depot, this parameter is not required. |

    **Source Specification Fields**

    | Field Name        | Description                                                                                                                                    | Required |
    | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
    | `address`         | The address to the source. 1. Can be connected using a Depot 2. Can be connected directly using a connection string, but it requires a secret. | Yes      |
    | `source-table`    | Name of the source table/entity from which the data is extracted. (Salesforce object name in the above example.)                               | Yes      |
    | `primary-key`     | Primary key of the source table.                                                                                                               | No       |
    | `incremental-key` | Key used for incremental data ingestion.                                                                                                       | No       |
    | `interval-start`  | Start of the interval for data ingestion.                                                                                                      | No       |
    | `interval-end`    | End of the interval for data ingestion.                                                                                                        | No       |
    | `columns`         | List of columns to be included (as string).                                                                                                    | No       |

    **Sink Configuration Fields**

    | Field Name             | Description                                                                                | Required |
    | ---------------------- | ------------------------------------------------------------------------------------------ | -------- |
    | `address`              | Target address (DataOS Lakehouse as example)                                               | Yes      |
    | `dest-table`           | Schema to write change records. Destination table is defined in `schema.table_name` format | Yes      |
    | `incremental-strategy` | Data ingestion strategy (append or replace)                                                | Yes      |