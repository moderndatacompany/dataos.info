# MongoDB

The Nilus connector for MongoDB supports Change Data Capture (CDC), enabling near real-time replication of data changes from MongoDB to [Supported Destinations](/resources/stacks/nilus/supported_destinations/), such as the Lakehouse. CDC captures change events from MongoDB’s `oplog.rs` and streams them continuously.

!!! info
    Batch data movement is not supported for MongoDB.


## Prerequisites 

Before enabling CDC, ensure the following configurations depending on your hosting environment:

### **MongoDB Replica Set**

* MongoDB must run as a replica set, even for single-node deployments.
* Nilus CDC for MongoDB relies on the `oplog.rs` collection, which is only available in replica sets.

!!! info
      Contact the Database Administrator (DBA) to set up and enable Change Data Capture (CDC) in MongoDB.

### **Enable `oplog` Access**

* Nilus uses MongoDB’s `oplog.rs` to capture changes.
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


### **Pre-created MongoDB Depot**

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

If the Depot is not created use the following manifest configuration template to create the MongoDB Depot:

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
        subprotocol: ${{"mongodb+srv"}}
        nodes: ${{["clusterabc.ezlggfy.mongodb.net"]}}
      external: ${{true}}
      secrets:
        - name: ${{instance-secret-name}}-r
          allkeys: ${{true}}

        - name: ${{instance-secret-name}}-rw
          allkeys: ${{true}}
    ```

    !!! info
        Update variables such as `name`, `owner`, `compute`, `layer`, etc., and contact the DataOS Administrator or Operator to obtain the appropriate secret name.



## Sample Service Config

Following manifest configuration template can be use to apply the CDC for MongoDB:

```yaml
name: ${{service-name}}                                    # Service identifier
version: v1                                                # Version of the service
type: service                                              # Defines the resource type
tags:                                                      # Classification tags
    - ${{tag}}                                              
    - ${{tag}}                                              
description: Nilus CDC Service for MongoDB description    # Description of the service
workspace: public                                          # Workspace where the service is deployed

service:                                                   # Service specification block
  servicePort: 9010                                        # Service port
  replicas: 1                                              # Number of replicas
  logLevel: INFO                                           # Logging level
  compute: ${{query-default}}                              # Compute profile
  persistentVolume:                                        # Persistent volume configuration
    name: ${{ncdc-vo1-01}}                                 # Volume name (multiple options commented)
    directory: ${{nilus_01}}                               # Target directory within the volume
  stack: ${{nilus:3.0}}                                    # Nilus stack version
  stackSpec:                                               # Stack specification
    source:                                                # Source configuration block
      address: dataos://mongodbdepot                       # Source depot address/UDL
      options:                                             # Source-specific options
        engine: debezium                                   # Required CDC engine; used for streaming changes
        collection.include.list: "retail.products"         # MongoDB collections to include
        topic.prefix: "cdc_changelog"                      # Required topic prefix for CDC stream
        max-table-nesting: "0"                             # Optional; prevents unnesting of nested documents
        transforms.unwrap.array.encoding: array            # Optional; preserves arrays in sink as-is
    sink:                                                  # Sink configuration for CDC output
      address: dataos://testinglh                          # Sink depot address
      options:                                             # Sink-specific options
        dest-table: mdb_test_001                           # Destination table name in the sink depot
        incremental-strategy: append                       # Append-only strategy for streaming writes


```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Service YAML}}
```

!!! info
    The MongoDB host used in the CDC service YAML must match exactly the host defined during replica set initialization.


## Source Options

Nilus supports the following source options for MongoDB CDC:

| Option                             | Default      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `database.include.list`            | _No Default_ | An optional comma-separated list of regular expressions or literals that match fully-qualified namespaces for MongoDB collections to be monitored. By default, the connector monitors all collections except those in the `local` and `admin` databases. When `collection.include.list` is set, the connector monitors only the collections that the property specifies. Other collections are excluded from monitoring. Collection identifiers are of the form _databaseName_._collectionName_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `collection.include.list`          | _No Default_ | An optional comma-separated list of regular expressions or literals that match fully-qualified namespaces for MongoDB collections to be excluded from monitoring. When `collection.exclude.list` is set, the connector monitors every collection except the ones that the property specifies. Collection identifiers are of the form _databaseName_._collectionName_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `snapshot.mode`                    | `initial`    | <p>Specifies the behavior for snapshots when the connector starts.<br>Options:</p><p><code>always:</code> The connector performs a snapshot every time that it starts. The snapshot includes the structure and data of the captured tables. Specify this value to populate topics with a complete representation of the data from the captured tables every time that the connector starts. After the snapshot completes, the connector begins to stream event records for subsequent database changes.</p><p></p><p><code>initial:</code> The connector performs a snapshot only when no offsets have been recorded for the logical server name.</p><p></p><p><code>no_data:</code> The connector performs an initial snapshot and then stops, without processing any subsequent changes.</p><p></p><p><code>initial_only:</code> The connector never performs snapshots.</p><p></p><p><code>when_needed:</code> After the connector starts, it performs a snapshot only if it detects one of the following circumstances:</p><ul><li>It cannot detect any topic offsets.</li><li>A previously recorded offset specifies a log position that is not available on the server.</li></ul> |
| `field.exclude.list`               | _No Default_ | An optional comma-separated list of the fully-qualified names of fields that should be excluded from change event message values. Fully-qualified names for fields are of the form databaseName.collectionName.fieldName.nestedFieldName, where databaseName and collectionName may contain the wildcard (*) which matches any characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `topic.prefix`                     | _No Default_ | <p>Topic prefix that provides a namespace for the particular MongoDB instance or cluster in which Nilus is capturing changes.</p><p>The prefix should be unique across all other connectors. Only alphanumeric characters, hyphens, dots and underscores must be used in the database server logical name.</p><p>This is mandatory. This prefix is also appended to the sink table.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `transforms.unwrap.array.encoding` | _No Default_ | It controls how array values are encoded when unwrapped by a Kafka Connect transform. Common options include "`none`" (default), "`array`", "`json`", or "`string`", which define how array elements are serialized into Kafka messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `max-table-nesting`                | _No Default_ | Specifies the maximum allowed depth for nested tables or objects (commonly in JSON or relational mapping). It helps prevent excessively deep or complex structures that can impact performance or compatibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Sink Options

Nilus supports the following sink options for MongoDB CDC:

| Field                  | Description                                    | Default  |
| ---------------------- | ---------------------------------------------- | -------- |
| `dest-table`           | Target table in the sink.                      | —        |
| `incremental-strategy` | Write mode (`append` recommended for CDC).     | `append` |


## Core Concepts

Nilus captures row-level changes from MongoDB using the replica set `oplog`. Below are the essential concepts for understanding how Nilus integrates with MongoDB.

- **Replica Set**

    - MongoDB must run as a replica set, even in single-node deployments.
    - Nilus connects to the primary replica and tails the `oplog` (`local.oplog.rs`).
    - Standalone MongoDB servers are not supported for CDC.

- **The MongoDB Oplog**

    - The **oplog** (`oplog.rs`) is a capped collection in the `local` database.
    - It records every `insert`, `update`, and `delete` applied to the primary.
    - Nilus reads this log to generate CDC events.
    - `oplog` entries roll off in FIFO (first-in-first-out) order once the allocated size is exhausted.
  
- **Schema-Less Nature of MongoDB**

    - MongoDB is schema-less, but Nilus dynamically infers schemas.
    - The sink table is created from the first document observed.
    - Schema evolution is tracked using a Schema Registry with Avro.

- **`oplog` Retention & Disk Pressure**
    
    Nilus maintains a cursor in the `oplog`. If it lags:

    - Older `oplog` entries may expire.
    - Expiration causes event loss and forces a new snapshot.

    **Disk pressure:**

    - `oplog` grows continuously with write load.
    - High disk usage can cause:
        - Write slowdowns
        - Replication failures
        - Node crashes

    **Recovery:**

    - If `oplog` retention is exceeded, Nilus enters a pending state.
    - Restarting the connector is not enough — a redeploy with a new snapshot is required.
    
- **Error 286 (ChangeStreamHistoryLost)**

    _Error 286_ means Nilus attempted to resume from an `oplog` entry that no longer exists:\


    ```bash
    Command failed with error 286 (ChangeStreamHistoryLost):
    Resume of change stream was not possible, as the resume point may no longer be in the oplog
    ```

    
    **Why It Happens**

    - Connector lag exceeds oplog window.
    - `oplog` was resized/shrunk.
    - Filesystem pressure caused truncation.
    - High write spikes shortened the retention window.

    **Recovery**

    - Redeploy the CDC service with a new PVC directory.
    - OR delete offsets so Nilus re-snapshots.
    - OR change connector name to force a fresh snapshot (from Nilus `v0.0.13+`).

    **Prevention**

    -  Size the `oplog` for the worst-case lag:

        ```
        RequiredSize(MB) ≈ PeakWrites/sec × MaxLag(sec) × avgEntrySize × safetyFactor
        ```

    - Monitor with `rs.printReplicationInfo()`.

    - Avoid long pauses beyond the `oplog` retention window.
    
    - Use `replSetResizeOplog` (MongoDB 4.4+) or `minRetentionHours` (MongoDB 6.0+) for stronger guarantees.

    !!! info
          Restarting the service alone does not fix _Error 286_. Manual intervention is required.


    - **`oplog` Polling**

    Nilus continuously tails the `oplog`:

        - Use a cursor to track the last processed entry.
        - Parses each entry and emits structured CDC events.
        - Keeps streaming aligned with replication order.
        
    - **MongoDB System Databases & Access**
    
        Nilus requires specific database access:
        
        - **`local`**
        
            - Source of oplog (`local.oplog.rs`).
            - Requires **`read`** permissions.
        - **`admin`**

            - Used for server metadata, discovery, and auth.
            - Requires **`read`** on commands like `replSetGetStatus`, `buildInfo`, `listDatabases`.
        
        - **`config`:** Needed only in **sharded clusters**.

    - **Target Databases (Application Data)**
    
        - Collections you want to capture.
        - Requires **`read`** permissions.
        - If snapshotting is enabled, Nilus reads **all documents** during startup.

    - **Recommended Source Options(Sample Configuration):**

    ```yaml
    source:
      address: dataos://mongodept
      options:
        engine: debezium
        collection.include.list: "shop.products"
        topic.prefix: "cdc_changelog"
        snapshot.mode: "when_needed"
        max.batch.size: 250
        max.queue.size: 2000
        max.queue.size.in.bytes: "134217728"
        heartbeat.interval.ms: 6000
        offset.flush.interval.ms: 15000

    sink:
      address: dataos://testawslh
      options:
        dest-table: mongodb_test
        incremental-strategy: append

    ```

    **Option Reference:**

    | Property                   | Purpose                                  | Suggested Value                                 |
    | -------------------------- | ---------------------------------------- | ----------------------------------------------- |
    | `snapshot.mode`            | Controls behavior if offsets are missing | `when_needed` (default), `initial`, or `always` |
    | `offset.flush.interval.ms` | Frequency of committing offsets          | 15000 ms                                        |
    | `heartbeat.interval.ms`    | Emit heartbeat events when idle          | 5000–10000 ms                                   |
    | `max.batch.size`           | Max records in a batch                   | 250                                             |
    | `max.queue.size`           | Max records in memory                    | 2000                                            |
    | `max.queue.size.in.bytes`  | Max memory buffer size                   | 128 MB (adjustable)                             |

- **Operational Playbook**

    | Phase              | Checklist                                                                   |
    | ------------------ | --------------------------------------------------------------------------- |
    | Daily              | Monitor oplog window & connector lag. Alert if lag > 80 % of window.        |
    | Before Maintenance | Estimate pause time. If > oplog window, temporarily resize oplog.           |
    | After Outage       | If Error 286 occurs, redeploy with fresh snapshot or clean offsets.         |
    | After Recovery     | Validate sizing assumptions, adjust oplog size or Nilus throughput configs. |

### **Useful Commands for `oplog`**

```javascript
// oplog history window
rs.printReplicationInfo();

// Latest oplog record
use local;
db.oplog.rs.find().sort({$natural:-1}).limit(1).pretty();

// Resize oplog (primary only)
use admin;
db.adminCommand({replSetResizeOplog:1, size: <MB>, minRetentionHours: <hours>});
```

