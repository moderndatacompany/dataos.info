# PostgreSQL

The Nilus connector for PostgreSQL supports Change Data Capture (CDC), enabling real-time replication of changes from PostgreSQL transactional databases to  [Supported Destinations](/resources/stacks/nilus/supported_destinations/), such as the Lakehouse.

## Prerequisites

Before enabling CDC, ensure the following configurations depending on your hosting environment:

### **PostgreSQL Configuration**

!!! info
    Contact the Database Administrator (DBA) to set up Change Data Capture (CDC) for PostgreSQL.


- **Azure-hosted PostgreSQL :** Set `wal_level` to `logical` to enable logical replication.

    ```sql
    ALTER SYSTEM SET wal_level = logical;
    ```

    **Note:** This is required for logical replication, which enables Change Data Capture.

- **Azure portal:** This setting is found under **Server Parameters**.
    <figure><img src="/resources/stacks/nilus/images/cdc-psql.png" style="width:40rem;" ><figcaption><i>Serve Parameters on Azure Cloud Console</i></figcaption></figure>

- **Amazon RDS for PostgreSQL**

    - Enable the `pglogical` extension.
    -   Set the static parameter:

        ```sql
        rds.logical_replication = 1;
        ```

    - Adjust replication parameters if needed:\
      `wal_level`, `max_wal_senders`, `max_replication_slots`, `max_connections`.

- **Important:** Reboot the DB instance for changes to take effect.

- Links for more information
    - [**Performing logical replication for Amazon RDS for PostgreSQL**](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication.html)
    - [**Set up the pglogical extension**](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.basic-setup.html)

### **User Permissions**

The connection user must have login and replication permissions. Check permissions with:

```sql
SELECT rolcanlogin AS can_login, rolreplication AS can_replicate
FROM pg_roles
WHERE rolname = 'username';
```

- Grant if required:

    ```sql
    ALTER ROLE <username> WITH LOGIN REPLICATION;
    ```

- Or create a new user:

    ```sql
    CREATE ROLE <username> WITH LOGIN REPLICATION PASSWORD '<password>';
    ```

### **Replication Slot**

Create a logical replication slot as explained. This process requires that you specify a decoding plugin.:

* `test_decoding`
* `wal2json`

!!! info
    Use a unique slot name for each Nilus instance.


### **Pre-created PostgreSQL Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
| NAME          | VERSION | TYPE  | STATUS | OWNER    |
| ------------- | ------- | ----- | ------ | -------- |
| postgresdepot | v2alpha | depot | active | usertest |
```

If the Depot is not created use the following manifest configuration template to create the PostgreSQL Depot:

??? note "PostgreSQL Depot Manifest"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    tags:
      - ${{tag1}}
      - ${{tag2}}
    layer: user
    depot:
      type: postgres
      external: true
    secrets:
      - name: ${{instance-secret-name}}-r
        allkeys: ${{true}}

      - name: ${{instance-secret-name}}-rw
        allkeys: ${{true}}
            
    ```

    !!! info
        Update variables such as `name`, `owner`, and `layer`, and contact the DataOS Administrator or Operator to obtain the appropriate secret name.




## Sample Service Config

Following manifest configuration template can be use to apply the CDC for PostgreSQL:

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
  compute: ${{query-default}}                              # Compute type

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
         dest-table: pgdb_test_004                         # Destination table name in sink
        incremental-strategy: append                       # Append mode for CDC write strategy


```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Service YAML}}
```

### **Best Practices**

1. Always include all partitions in `table.include.list`.
2. Confirm `wal_level = logical`.
3. Grant replication user sufficient privileges.
4. Monitor replication slots to avoid WAL buildup.



## Source Options

Nilus supports the following PostgreSQL CDC source options:

| Option                      | Default      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Requirement |
| --------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `heartbeat.interval.ms`     | _No default_ | Controls how frequently the connector sends heartbeat messages to a Kafka topic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Optional    |
| `topic.heartbeat.prefix`    | _No default_ | Controls the name of the topic for heartbeat messages. The naming pattern is: `topic.heartbeat.prefix.topic.prefix`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Optional    |
| `slot.name`                 | _No default_ | Name of the logical replication slot for streaming changes. Unique per Nilus instance, it tracks WAL changes as a bookmark.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Mandatory   |
| `topic.prefix`              | _No default_ | Unique topic prefix for change events. Must be alphanumeric, hyphens, dots, or underscores. Forms the namespace and is appended to sink table names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Mandatory   |
| `schema.include.list`       | _No default_ | Regular expressions of schema names to include, monitoring all non-system tables. Not usable with `schema.exclude.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Optional    |
| `schema.exclude.list`       | _No default_ | Regular expressions of schema names to exclude from monitoring. Not usable with `schema.include.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Optional    |
| `table.include.list`        | _No default_ | Regular expressions of fully qualified table names to include in CDC. Format: `schemaName.tableName`. Not usable with `table.exclude.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Optional    |
| `table.exclude.list`        | _No default_ | Regular expressions of fully qualified table names to exclude in CDC. Format: `schemaName.tableName`. Not usable with `table.include.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Optional    |
| `column.include.list`       | _No default_ | Regular expressions of fully qualified column names to include in events. Format: `schemaName.tableName.columnName`. Not usable with `column.exclude.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Optional    |
| `column.exclude.list`       | _No default_ | Regular expressions of fully qualified column names to exclude from events. Format: `schemaName.tableName.columnName`. Not usable with `column.include.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Optional    |
| `include.unknown.datatypes` | `false`      | Includes fields with unknown data types as binary payloads in change events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Optional    |
| `max.batch.size`            | `2048`       | Maximum number of events processed in a single batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Optional    |
| `snapshot.mode`             | `initial`    | Defines snapshot behavior at connector startup with options like `always`, `initial`, `no_data`, `initial_only`, or `when_needed`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Optional    |
| `time.precision.mod`        | adaptive     | <p><code>adaptive</code> captures the time and timestamp values exactly as in the database using either millisecond, microsecond, or nanosecond precision values based on the database column’s type.<br><br><code>adaptive_time_microseconds</code> captures the date, datetime and timestamp values exactly as in the database using either millisecond, microsecond, or nanosecond precision values based on the database column’s type. An exception is <code>TIME</code> type fields, which are always captured as microseconds.<br><br><code>connect</code> always represents time and timestamp values by using connectors built-in representations for <code>Time</code>, <code>Date</code>, and <code>Timestamp</code>, which use millisecond precision regardless of the database columns' precision.</p> | Optional    |
| `decimal.handling.m`        | precise      | <p><code>precise</code> represents values by using <code>java.math.BigDecimal</code> to represent values in binary form in change events.<br><br><code>double</code> represents values by using <code>double</code> values, which might result in a loss of precision but which is easier to use.<br><br><code>string</code> encodes values as formatted strings, which are easy to consume but semantic information about the real type is lost.</p>                                                                                                                                                                                                                                                                                                                                                               | Optional    |

## Sink Options

Nilus supports the following sink options for PostgreSQL CDC workflows:

| Field                  | Description                                    | Default  |
| ---------------------- | ---------------------------------------------- | -------- |
| `dest-table`           | Target table in the sink.                      | —        |
| `incremental-strategy` | Write mode (`append` recommended for CDC).     | `append` |


## Core Concepts

Nilus captures row-level changes from PostgreSQL using its logical replication infrastructure. Below are the key concepts that explain how Nilus works with PostgreSQL.

1. **Logical Replication**

      1. Nilus relies on logical replication to stream data changes from the Write-Ahead Log (WAL).
      2. It must be enabled at the PostgreSQL server level (`wal_level = logical`).
      3. Only changes to tables with a primary key and a valid replica identity are captured.
      4. Replica Identity defines how PostgreSQL identifies rows during `UPDATE` or `DELETE` operations.

2. **WAL and LSN**
      1. Write-Ahead Log (WAL): PostgreSQL’s transaction log containing all committed changes.
      2. Nilus reads the WAL via a logical decoding plugin.
      3. Each event is tagged with a Log Sequence Number (LSN), allowing Nilus to:
            1. Resume precisely after interruptions.
            2. Guarantee ordered and lossless streaming.
   
3. **Initial Snapshot**

      When a Nilus connector starts for the first time (or if snapshotting is explicitly enabled):

       1. It connects via JDBC.
       2. Reads schema metadata from system catalogs (`information_schema.tables`, `pg_catalog.pg_attribute`, etc.).
       3. Captures baseline schema (columns, types, primary keys).
       4. Emits a `read` (`op: r`) event for every row in the included tables.
       5. This provides a consistent starting point for downstream pipelines.

4. **Logical Decoding**

      After snapshotting, Nilus switches to streaming mode:

      1. Consumes logical decoding messages from WAL using a plugin such as:
               1. `pgoutput` (default, recommended for PostgreSQL ≥10).
               2. `wal2json` or `decoderbufs` (alternative formats).
      2. These messages contain row-level changes only.
      3. Nilus uses cached schema from the snapshot to interpret them.
      4. Schema changes (e.g., ALTER TABLE) are detected and the cache is updated dynamically.

5. **Replication Slot**

      1. Nilus creates a replication slot to retain WAL changes until consumed.
      2. Ensures no data loss, but requires monitoring (slots can cause WAL bloat if Nilus is paused).
      3.  Useful queries:

          ```sql
          -- List all replication slots
          SELECT * FROM pg_replication_slots;

          -- Check WAL sender status
          SELECT * FROM pg_stat_replication;

          -- Drop an inactive slot
          SELECT pg_drop_replication_slot('slot_name');

          -- Terminate a backend process
          SELECT pg_terminate_backend(pid);
          ```

6. **Change Event Structure**

      A sample event produced by Nilus:

      ```json
      {
        "before": {},
        "after": {},
        "source": {
          "version": "2.6.0.Final",
          "connector": "postgresql",
          "name": "dbserver1",
          "ts_ms": 1675348820467,
          "snapshot": "false",
          "db": "mydb",
          "sequence": "[null, \"22817752\"]",
          "schema": "public",
          "lsn": 22817752,
          "txId": 567,
          "xmin": null
        },
        "op": "c",
        "ts_ms": 1675348820467
      }
      ```



      **Key fields:**

      * `lsn`: WAL Log Sequence Number, used for resuming position.
      * `txId`: PostgreSQL transaction ID (shared across changes in one transaction).
      * `sequence`: Ordering of changes within a transaction.
      * `xmin`: Optional transaction visibility marker.

7.  **Partitioned Tables**

      Nilus supports declaratively partitioned tables, with special considerations:

      1. **Data Routing:** Inserts/updates/deletes must target the parent table. PostgreSQL routes changes to child partitions.
      2. **Primary Key:** Must be defined on the parent table and inherited by child partitions.
      3. **Table Inclusion:** Both parent and child partitions must be explicitly listed in `table.include.list`.
      4. **Publication:** Must include parent and child tables (or `FOR ALL TABLES`). Nilus can auto-create this if permissions allow.
      5. **Event Consolidation:** Uses `ByLogicalTableRouter` SMT to unify partition events into a single topic.
      6.  **Permissions:** Replication user must have:

            1. `REPLICATION` role (or `rds_replication` on AWS).
            2. `SELECT` and `USAGE` on schemas/tables.
            3. `CREATE` if Nilus should auto-create publications.

            **Example Partition Setup:**

            ```sql
            CREATE TABLE orders (
                id SERIAL PRIMARY KEY,
                customer_id INT,
                created_at DATE NOT NULL
            ) PARTITION BY RANGE (created_at);

            CREATE TABLE orders_2024_q1 PARTITION OF orders
              FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');
            ```

      **CDC Configuration:**

      ```yaml
      source:
        address: dataos://postgresdepot
        options:
          engine: debezium
          slot.name: "nilus_slot"
          plugin.name: "pgoutput"
          publication.name: "nilus_pub"
          table.include.list: "public.orders,public.orders_2024_q1"
          topic.prefix: "cdc_changelog"
          heartbeat.interval.ms: 60000
          transforms: "unwrap,Reroute"
          transforms.unwrap.type: "io.debezium.transforms.ExtractNewRecordState"
          transforms.Reroute.type: "io.debezium.transforms.ByLogicalTableRouter"
          transforms.Reroute.topic.regex: "(.*)\\.(.*)\\.orders(_.*)?"
          transforms.Reroute.topic.replacement: "cdc_changelog.public.orders"
      ```





