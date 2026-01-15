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
  compute: ${{query-default}}                              # Compute type
 
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

1. **Replica Set**

    - MongoDB must run as a replica set, even in single-node deployments.
    - Nilus connects to the primary replica and tails the `oplog` (`local.oplog.rs`).
    - Standalone MongoDB servers are not supported for CDC.

2. **The MongoDB Oplog**

    - The **oplog** (`oplog.rs`) is a capped collection in the `local` database.
    - It records every `insert`, `update`, and `delete` applied to the primary.
    - Nilus reads this log to generate CDC events.
    - `oplog` entries roll off in FIFO (first-in-first-out) order once the allocated size is exhausted.
  
3. **Schema-Less Nature of MongoDB**

    - MongoDB is schema-less, but Nilus dynamically infers schemas.
    - The sink table is created from the first document observed.
    - Schema evolution is tracked using a Schema Registry with Avro.

4. **`oplog` Retention & Disk Pressure**

    * Nilus maintains a cursor within the MongoDB oplog to track change events. When the connector is paused or lags behind, MongoDB retains older oplog entries to accommodate delayed consumption.
    * If the connector's lag exceeds the oplog retention threshold, expired entries may lead to data loss. In such cases, a full snapshot must be reinitiated to resume consistent processing.
    * The term **Disk Pressure** refers to the stress placed on disk resources due to the continuous growth of the `oplog.rs` file. MongoDB retains these entries until Nilus acknowledges their processing.

    **Implications of High Disk Pressure**

    1. The oplog continuously expands as new changes are recorded.
    2. Disk utilization increases on the volume where MongoDB stores its data.
    3. Excessive disk usage can lead to:
          1. Write operation slowdowns
          2. Replication failures
          3. Potential node instability or crashes

    Although rare, this condition can result in a fatal error, placing the service in a pending state. Recovery requires redeployment of the CDC service. Upon redeployment, the system performs a full snapshot followed by real-time change data capture.

    **Error 286**:
    
    ??? note "Handling MongoDB *Error 286* in CDC Pipelines"
        **TL;DR**

        - **Error 286 is always a symptom of *history loss***  -  the resume token is gone.
        - The **root cause** is an undersized or force‑truncated oplog relative to the maximum connector lag.
        - **Prevention** = correct **oplog sizing + connector throughput + monitoring**.
        - **Recovery** is straightforward (new snapshot or larger oplog) but can be time‑consuming—plan ahead.

        **Overview**
        
        *Error 286* indicates that a MongoDB change stream (which Nilus relies on for CDC) attempted to resume from a point that is **no longer present in the replica‑set oplog (**`local.oplog.rs`**)**. When this happens, Nilus logs the following exception:

        ```
        Command failed with error 286 (ChangeStreamHistoryLost):
        Resume of change stream was not possible, as the resume point may no longer be in the oplog
        ```

        Understanding why the oplog entry disappeared and how to size & monitor the oplog is therefore critical for reliable CDC.

        **The MongoDB Oplog in a Nutshell**


        - A capped collection (`local.oplog.rs`) that stores every write against the primary so secondaries (and tools such as Nilus) can replicate those changes.
        - The oplog is truncated on a **first‑in‑first‑out** basis once it reaches its allocated size.
        - **Default size** – When you initiate a replica set, MongoDB chooses the oplog size automatically: **5 % of free disk space (minimum ≈ 990 MB).**

        *Because the collection is capped, what really matters is **time window**: How many hours of history does this size translate to under your peak write load?*
        

        **Why Error 286 Happens**


        1. The connector is paused or slowed down; older entries roll off before it resumes.
        2. Manually shrinking the oplog or re-initializing the replica set discards old tokens.
        3. MongoDB may truncate more aggressively if the filesystem is full.
        4. Very high write bursts, such as a sudden surge (e.g., bulk load), shrink the effective time window.

        *When the connector restarts it looks up its resume token in the oplog; if that token has vanished, MongoDB throws error 286 and Nilus refuses to start.*


        **Recovery Options**


        - Delete and reapply the failing service with a new PV directory or PVC. (*OR* Keep the connector up and running, but **delete the offset** (from the PVC directory) so that Nilus believes it is new and snapshots again.)
            
            *OR*
            
        - Change the name of the connector service *(from `nilus:0.0.13` onwards)* using the same config. Nilus will take a snapshot (as specified by the `snapshot.mode`) and then continue to stream changes.


        **Note:** *Error 286 cannot be resolved by simply restarting the connector. **Manual intervention is required to restore the service once this error occurs.***

        **Preventing Error 286**


        1. Size the Oplog for Worst‑Case Lag
            
            *MongoDB 4.4+ also supports `replSetResizeOplog`, and 6.0 adds `minRetentionHours` for time‑based guarantees.*
            
            
            The objective is to ensure the oplog retains *at least* as much history as the connector could ever fall behind, with headroom for bursts.
            
            Formula:
            
            `RequiredSize(MB) ≈ PeakWrites/sec × MaxLag(sec) × avgEntrySize × safetyFactor`
            
            - **Peak Writes/sec** – Insert + Update + Delete ops during the busiest interval (consult `serverStatus().opcounters` or monitoring).
            - **Max Lag** – Longest plausible outage/back‑pressure window (connector maintenance + downstream outage + buffer).
            - **avgEntrySize** – In bytes; rule‑of‑thumb ≈ 1 kB if most documents are small.
            - **safetyFactor** – 1.3–2.0 depending on risk appetite.
            
            
            **Example**
        
            | Parameter | Value | Notes |
            | --- | --- | --- |
            | Peak writes/sec | **15 000** ops | Observed from Grafana at 95‑th percentile |
            | Max lag | **30 min** = 1 800 s | Upgrade window + 10 min contingency |
            | Avg entry size | **1 kB** | Typical BSON size of collection docs |
            | Safety factor | **1.5** | Gives headroom for burst writes |
            
            ```
                Raw volume = 15000 × 1800 × 1024 ≈ 27648000kB ≈ 27GB
                With safety = 27GB × 1.5 ≈ 41GB
            ```
            
            - Recommendation: Round up to 48 GB when running replSetResizeOplog or the --oplogSize init option.
            - A 48 GB oplog provides ~35 min at *double* the recorded peak, so the window remains safe even during black‑swan spikes.

        2. Monitor Key Metrics
            - Use `rs.printReplicationInfo()` to retrieve information on the oplog status, including the size of the oplog and the time range of operations.
        3. Avoid Long Pauses
            - Schedule connector downtime within the calculated oplog window.
        4. Recommended Nilus Source Options

            ??? info "Sample Configuration"
                
                ```yaml
                source:
                      address: dataos://mongodept
                      options:
                        engine: debezium #mandatory for CDC; no need for batch
                        collection.include.list: "spam.product"
                        topic.prefix: "cdc_changelog" #mandatory; can be custom
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
                        aws_region: us-west-2
                ```
                
            
            | Property | Why it helps | Suggested value |
            | --- | --- | --- |
            | `snapshot.mode` | Controls what Nilus does when offsets are missing. |  - Set to `initial` (default) or `always` if you anticipate long downtimes - `when_needed` - After the connector starts, it performs a snapshot only if either It cannot detect any topic offsets or a previously recorded offset specifies a log position that is not available on the server |
            | `offset.flush.interval.ms` | How often offsets are committed. Shorter intervals reduce duplicate events after crashes. | 15000 ms |
            | `heartbeat.interval.ms` | Emits heartbeat records to keep offsets moving even when no data changes. Helps detect lag early. | 5000–10000 ms |
            | `max.batch.size`, `max.queue.size` & `max.queue.size.in.bytes` | Tune to keep connector processing speed > peak write rate, avoiding backlog. | Start with small (eg. 250 / 2000 & 128 MB), adjust according to the data volume and change frequency |

        **Operational Playbook**


        | Phase | Checklist |
        | --- | --- |
        | **Daily** | - Monitor `oplog window` & connector lag </br>- Alert if lag > 80 % of window |
        | **Before maintenance** | - Calculate expected pause; if > window, increase oplog temporarily |
        | **After unplanned outage** | - If connector fails with 286, decide between *re‑snapshot or clean the PV directory* |
        | **After success** | - Review sizing assumptions; adjust `oplogSizeMB` or Nilus throughput limits |

        **Useful MongoDB Shell Commands**


        ```bash
        // Check how many hours of history are currently in the oplog
        rs.printReplicationInfo();

        // Show the newest record in the oplog
        use local;
        db.oplog.rs.find().sort({$natural:-1}).limit(1).pretty();

        // Resize oplog (requires primary)
        use admin;
        db.adminCommand({replSetResizeOplog:1, size: <MB>, minRetentionHours: <hours>});

        ```  

    **Warning Reference "Buffer Lock Warning"**:
    
    `BufferingChangeStreamCursor: Unable to acquire buffer lock, buffer queue is likely full`
    
    ??? note "Handling MongoDB Warning BufferingChangeStreamCursor in CDC Pipelines"
        **TL;DR**


        - This warning indicates that the MongoDB CDC pipeline temporarily stopped reading new changes because its internal buffer filled up.
        - It is **not an error by itself**, but if it continues for long periods, it can cause **CDC lag**, **resume-token failures**, or **change stream interruptions**.

        **To prevent the issue:**

        - Reduce Debezium batch size
        - Increase service memory & set memory limits (if not set already)
        - Ensure sink writes are healthy (check the *source*ts_ms)
        - Avoid long-running Iceberg commits or high write spikes

        **If it occurs:**

        - Verify whether CDC is still progressing
        - Check sink performance
        - Restart the CDC service only if offsets stop advancing
        - Take action before the MongoDB oplog window is exceeded

        **Overview**


        ```
        Unable to acquire buffer lock, buffer queue is likely full
        ```

        This warning comes from the Debezium MongoDB connector’s internal Change Stream Cursor reader. It means that Debezium’s internal in-memory buffer is full and cannot accept more events until the downstream consumer (sink writer) catches up.

        ### Key points:

        - The warning **does not mean data loss**.
        - It **can indicate backpressure** in the pipeline.
        - If backpressure persists long enough, it can eventually lead to **MongoDB change stream errors,** such as:
            - `ChangeStreamHistoryLost`
            - `InvalidResumeToken`

        This document explains why it happens, how to mitigate it proactively, and what to do if it occurs.

        **Root Cause**


        The warning appears when the **event-production rate (Mongo writes)** temporarily exceeds the **event-consumption rate (Nilus processing + Iceberg writes)**.

        Below are the typical contributing factors:

        1. **Downstream Sink Is Slow (Most Common)**
            
            Nilus writes the CDC data to a destination. If these operations slow down, for example, due to:
            
            - Large Iceberg commits
            - Compaction or manifest rewrites
            - S3 throttling or retry storms
            - High latency writes
            
            Then Debezium cannot drain its queue fast enough. *Result → buffer fills → warning appears.*
            
        2. Large Debezium Batch Size
            
            `max.batch.size: 2048` (default)
            
            - May cause Debezium to process very large chunks at once.
            - Large batches increase processing time and memory consumption, slowing down queue draining.
        3. Insufficient Memory
            
            This can lead to:
            
            - Very small heap → too many minor GCs
            - Very large heap → long GC pauses
            - GC pauses → slow consumer thread → queue full
        4. No Kubernetes Memory Limits
            
            If container memory limits are not set:
            
            - The JVM may assume it has access to full node memory.
            - It may pick an inappropriate heap size automatically.
            - During heavy load, this causes GC pressure and stalls.
        5. CPU Contention
            
            Heavy pipeline activity + large batches may saturate CPU in a 1-replica setup.
            
        6. High Write Brusts from MongoDB
            
            During traffic spikes, the change stream volume can exceed regular processing capacity.
            

        **Prevention**


        The following configuration adjustments significantly reduce the likelihood of buffer-full conditions.

        1. Reduce Debezium Batch Size
            
            Smaller batches = faster downstream commits = steady buffer drain.
            
            - Example
                
                ```
                max.batch.size: 1024
                # or
                max.batch.size: 512
                ```
                
        2. Allocate Sufficient (or more) Memory to the Service
            
            This prevents the service from operating at the edge of its memory budget.
            
        3. Define Resource Memory Limits
            
            Why this matters:
            
            - Predictable heap sizing
            - Reduced GC stalls
            - Improved Debezium throughput

        **Resolution**


        Use the following checklist to assess whether the warning is transient or serious. Steps

        1. **Verify Whether CDC is Still Progressing**
            - Check the sink dataset:
                - Are new rows appearing?
                - Is the CDC timestamp (`_ts` or equivalent) moving forward?
            - Check offset logs:
                - If offsets are updating → pipeline is healthy, warning was transient.
            - Check if heartbeats are processing:
                - Are new heartbeats committed to the heartbeat dataset?
                - Latest heartbeat was commit timestamp; how far is it since the current timestamp?
        2. **Measure CDC Lag**
            - Compare the last ingested timestamp vs the MongoDB server time
            - How to check MongoDB Server Time
                
                Replica set members rely on **synchronized clocks** for:
                
                - Oplog timestamp ordering
                - Heartbeat timeouts and election timing
                - Write concern “majority” acknowledgment
                
                **Run this in your MongoDB shell:**
                
                ```
                db.adminCommand({ hello: 1 })
                ```
                
                - Output
                    
                    ```
                    {
                      "hosts": [
                        "mongo1:27017",
                        "mongo2:27017",
                        "mongo3:27017"
                      ],
                      "setName": "rs0",
                      "setVersion": 3,
                      "ismaster": true,
                      "secondary": false,
                      "primary": "mongo1:27017",
                      "me": "mongo1:27017",
                      **"localTime": ISODate("2025-11-13T08:25:31.729Z"),**
                      ...
                    }
                    
                    ```
                    
                
                **Check the time on all Replica Set Members**
                
                ```
                #Consolidated Check
                rs.status().members.forEach(m => {
                  print(m.name);
                  printjson(db.getSiblingDB("admin").getMongo().getDB("admin").runCommand({ hello: 1 }));
                });
                
                --OR-- 
                #Individual Checks
                
                mongosh --host mongo1:27017
                db.adminCommand({ hello: 1 })
                
                mongosh --host mongo2:27017
                db.adminCommand({ hello: 1 })
                
                mongosh --host mongo3:27017
                db.adminCommand({ hello: 1 })
                
                ```
                
        3. **Check Sink Performance**
            - Query the Nilus metadata table (stored in PostgreSQL) and check for the throughput.
            - Query
                
                ```sql
                SELECT 
                    li.*, 
                    ri.dataos_resource_id,
                    ri.total_records,
                
                    -- Extract tag from dataos_resource_id
                    regexp_extract(ri.dataos_resource_id, 'workflow:v1:wf-([^-]+)-', 1) AS tag,
                
                    -- Calculate MB/sec
                    CASE 
                        WHEN ri.duration_sec > 0 THEN li.files_size_mb / li.duration_sec 
                        ELSE NULL 
                    END AS mb_per_sec,
                
                    -- Calculate records/sec
                    CASE 
                        WHEN ri.duration_sec > 0 THEN ri.total_records / li.duration_sec 
                        ELSE NULL 
                    END AS events_per_sec
                
                FROM "nilusdb"."public".load_info li
                JOIN (
                    SELECT 
                        id,  
                        run_id,  
                        load_id,  
                        started_at,  
                        finished_at,  
                        duration_sec,    
                        files_size_mb,  
                        memory_mb,  
                        cpu_percent,
                        dataos_resource_id,
                        reduce(
                            map_values(CAST(records_count AS map(varchar, integer))),
                            0,
                            (s, x) -> s + x,
                            s -> s
                        ) AS total_records 
                    FROM "nilusdb"."public".runs_info
                    WHERE run_as_user = 'dataos-manager' # define username 
                      AND dataos_resource_id LIKE 'workflow:v1:wf-%' #define your service name here
                      # AND finished_at > TIMESTAMP '2025-09-17 09:38:00.000 UTC'
                ) ri ON li.load_id = ri.load_id AND li.run_id = ri.run_id
                # WHERE ri.total_records > 1000
                ORDER BY ri.started_at DESC;
                ```
                
        4. **Assess the Stability of the Warning**
            - **If the warning lasts < 5 seconds**
                - Normal temporary backpressure.
                - No action needed.
            - **If the warning lasts ~5–30 seconds**
                - Monitor closely; CDC lag may grow.
                - Check sink and memory usage.
            - **If the warning persists > 30 seconds**
                - Risk zone for `ChangeStreamHistoryLost`
                - Take the Following Actions
                    - **Restart the service**
                        
                        This resets Debezium’s internal threads while preserving its position in the stream.
                        

        **Useful MongoDB Shell Commands**


        1. Check oplog size & window
            
            This helps determine the available oplog window (how far Debezium can fall behind).
            
            ```jsx
            use local
            db.oplog.rs.stats()
            db.oplog.rs.find().sort({ $natural: 1 }).limit(1)
            db.oplog.rs.find().sort({ $natural: -1 }).limit(1)
            ```
            
        2. Estimate Oplog Window Duration
            
            This is crucial: **If Debezium’s lag > oplog window, the change stream will fail.**
            
            ```jsx
            var first = db.oplog.rs.find().sort({$natural: 1}).limit(1)[0].ts.getTime();
            var last  = db.oplog.rs.find().sort({$natural: -1}).limit(1)[0].ts.getTime();
            print((last - first)/1000/60 + " minutes");
            ```
            
        3. Check Recent Write Rate
            
            ```jsx
            db.serverStatus().opcounters
            ```
            
        4. Check Collection-level Throughput
            
            ```jsx
            db.<collection>.stats()
            ```

5. **`oplog` Polling**

    Nilus continuously tails the `oplog`:

        - Use a cursor to track the last processed entry.
        - Parses each entry and emits structured CDC events.
        - Keeps streaming aligned with replication order.
        
6. **MongoDB System Databases & Access**
    
    Nilus requires specific database access:
    
    - **`local`**
    
        - Source of oplog (`local.oplog.rs`).
        - Requires **`read`** permissions.
  
    - **`admin`**

        - Used for server metadata, discovery, and auth.
        - Requires **`read`** on commands like `replSetGetStatus`, `buildInfo`, `listDatabases` and `isMaster`.
    
    - **`config`:** Needed only in **sharded clusters**.

    - **Target Databases (Application Data)**
    
        - Collections you want to capture.
        - Requires **`read`** permissions.
        - If snapshotting is enabled, Nilus reads **all documents** during startup.
<!-- 
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
 -->
