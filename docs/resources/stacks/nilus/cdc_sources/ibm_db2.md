# IBM DB2

The Nilus connector for **IBM Db2** supports **Change Data Capture (CDC)**, enabling row-level changes from Db2 tables to be streamed in near real-time into [supported destinations](/resources/stacks/nilus/supported_destinations/) such as the Lakehouse. CDC leverages Db2’s **SQL Replication** feature, which uses **ASN Capture/Apply agents** to detect and store changes in change-data tables.

!!! info
      IBM Db2 is not supported via Depot.


## Prerequisites 

The following are the requirements to enable CDC data movement in IBM DB2:

### **SQL Replication and Licensing**

* SQL Replication must be enabled on the Db2 source.
* This requires a license for **IBM InfoSphere Data Replication (IIDR)**.

### **Capture Mode**

* Tables must be explicitly placed into **capture mode**.
* Capture mode generates **change-data tables** that store row-level changes.
* Administrators manage capture mode using Db2 control commands to:
    * Start, stop, or reinitialize the ASN Capture agent.
    * Put tables into/out of capture mode.
    * Generate change-data tables.

### **CDC Setup & Enablement**

Steps for setting up and enabling Change Data Capture in IBM DB2:

- **Access the DB2 Environment**
- **Start CDC Capture Agent**

    ```bash
    nohup ~/sqllib/bin/asncap \
      capture_schema=ASNCDC \
      capture_server=SAMPLEDB \
      > ~/asncap.log 2>&1 &

    ~/sqllib/bin/asnccmd reinit \
      capture_schema=ASNCDC \
      capture_server=SAMPLEDB
    ```

    Verify status:

    ```sql
    db2 connect to SAMPLEDB
    db2 -x "VALUES ASNCDC.ASNCDCSERVICES('status','asncdc')"
    ```

- **Enable CDC for a Table**

    Create a test table:

    ```sql
    CREATE TABLE CDC_TEST (
      ID INT NOT NULL PRIMARY KEY,
      VAL VARCHAR(100)
    );

    INSERT INTO CDC_TEST (ID, VAL) VALUES
      (1, 'First'),
      (2, 'Second');
    ```

    Enable capture mode:

    ```sql
    VALUES ASNCDC.ASNCDCSERVICES('start','asncdc');
    CALL ASNCDC.ADDTABLE('DB2INST1','CDC_TEST');
    VALUES ASNCDC.ASNCDCSERVICES('reinit','asncdc');
    ```

- **Test CDC**

    ```sql
    INSERT INTO CDC_TEST (ID, VAL) VALUES (1000, 'CDC Check');
    SELECT * FROM CDC_TEST;
    ```

### **User Permissions**

The Db2 connection user requires elevated privileges to enable and manage CDC:

```sql
-- Grant execution privileges on Debezium UDFs (if used)
GRANT EXECUTE ON FUNCTION admin.start_capture TO user;
GRANT EXECUTE ON FUNCTION admin.stop_capture TO user;
GRANT EXECUTE ON FUNCTION admin.init_capture TO user;
GRANT EXECUTE ON FUNCTION admin.set_capture_table TO user;
GRANT EXECUTE ON FUNCTION admin.rm_capture_table TO user;

-- For Db2 control commands alternative:
GRANT DATAACCESS, DBADM ON DATABASE TO user;
-- Depending on environment:
GRANT CATALOGADM, SECADM ON DATABASE TO user;
```

!!! info
      Elevated roles such as `DBADM`, `DATAACCESS`, `CATALOGADM`, or `SECADM` may be required depending on how replication is managed. Contact the Database Administrator (DBA) to set up Change Data Capture (CDC).


## Sample Service Config

The following manifest configuration template can be used to apply the CDC for Db2:

```yaml
name: db2-cdc-service
version: v1
type: service
tags:
    - db2
    - cdc
description: Nilus CDC Service for IBM Db2
workspace: public

service:
  servicePort: 9010
  replicas: 1
  logLevel: INFO
  compute: runnable-default
  stack: nilus:1.0
  stackSpec:
    source:
      address: debezium+db2:username:password@host:port/database-name
      options:
        engine: debezium
        table.include.list: "SCHEMA.TABLE1,SCHEMA.TABLE2"
        topic.prefix: "db2"
        snapshot.mode: initial
        snapshot.isolation.mode: read_committed
    sink:
      address: dataos://lakehousedepot
      options:
        dest-table: db2_table_cdc
        incremental-strategy: append
```

!!! info
    * Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.
    * The Db2 source tables are in **capture mode,** and the change-data tables exist before deploying.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Service YAML}}
```

## Source Options

Nilus supports the following Db2 CDC source options:

| Option                  | Default      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Requirement |
| ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `heartbeat.interval.ms` | _No default_ | Controls how frequently the connector sends heartbeat messages to a Kafka topic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Optional    |
| `topic.prefix`          | _No default_ | Unique topic prefix for change events. Must be alphanumeric, hyphens, dots, or underscores. Forms the namespace and is appended to sink table names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Mandatory   |
| `table.include.list`    | _No default_ | Regular expressions of fully qualified table names to include in CDC. Format: `schemaName.tableName`. Not usable with `table.exclude.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Optional    |
| `table.exclude.list`    | _No default_ | Regular expressions of fully qualified table names to exclude in CDC. Format: `schemaName.tableName`. Not usable with `table.include.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Optional    |
| `column.include.list`   | _No default_ | Regular expressions of fully qualified column names to include in events. Format: `schemaName.tableName.columnName`. Not usable with `column.exclude.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Optional    |
| `column.exclude.list`   | _No default_ | Regular expressions of fully qualified column names to exclude from events. Format: `schemaName.tableName.columnName`. Not usable with `column.include.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Optional    |
| `max.batch.size`        | `2048`       | Maximum number of events processed in a single batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Optional    |
| poll.interval.ms        | 500          | Frequency (ms) at which the connector polls Db2 change-data tables.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Optional    |
| `snapshot.mode`         | `initial`    | Defines snapshot behavior at connector startup with options like `always`, `initial`, `no_data`, `initial_only`, or `when_needed`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Optional    |
| `time.precision.mod`    | adaptive     | <p><code>adaptive</code> captures the time and timestamp values exactly as in the database using either millisecond, microsecond, or nanosecond precision values based on the database column’s type.<br><br><code>adaptive_time_microseconds</code> captures the date, datetime and timestamp values exactly as in the database using either millisecond, microsecond, or nanosecond precision values based on the database column’s type. An exception is <code>TIME</code> type fields, which are always captured as microseconds.<br><br><code>connect</code> always represents time and timestamp values by using connectors built-in representations for <code>Time</code>, <code>Date</code>, and <code>Timestamp</code>, which use millisecond precision regardless of the database columns' precision.</p> | Optional    |
| `decimal.handling.m`    | precise      | <p><code>precise</code> represents values by using <code>java.math.BigDecimal</code> to represent values in binary form in change events.<br><br><code>double</code> represents values by using <code>double</code> values, which might result in a loss of precision but which is easier to use.<br><br><code>string</code> encodes values as formatted strings, which are easy to consume but semantic information about the real type is lost.</p>                                                                                                                                                                                                                                                                                                                                                               | Optional    |

## Sink Options

Nilus supports the following sink options for Db2 CDC service:

| Field                  | Description                                    | Default  |
| ---------------------- | ---------------------------------------------- | -------- |
| `dest-table`           | Target table in the sink.                      | —        |
| `incremental-strategy` | Write mode (`append` recommended for CDC).     | `append` |
| `aws_region`           | AWS region (required for S3-backed Lakehouse). | —        |

## Core Concepts

Nilus integrates with IBM Db2 using its SQL Replication / CDC framework. It captures changes written by Db2 into change-data tables (CD tables), enabling real-time pipelines.

- **Capture Agent (`asncap`)**
    - The `asncap` agent is a long-running background process.
    - Reads committed transactions from Db2 logs.
    - Writes row-level changes into CD tables for downstream consumption.

- **Capture Schema (e.g., `ASNCDC`)**
    - Stores all metadata, control procedures, and change-data tables.
    - Examples:
      - `ASNCDC.ASNCDCSERVICES` → Capture service definitions.
      - `ASNCDC.IBMSNAP_REGISTER` → Registry of source tables.
      - `ASNCDC.CDC_<DB>_<TABLE>` → Table-specific CD table.

- **Subscription & Apply Agent (`asnapply`)**
    - Db2 SQL Replication supports apply agents that replicate changes from CD tables into target tables.
    - Nilus does not use `asnapply` directly — instead, it reads from CD tables itself.
    - However, the concept is important for users familiar with traditional Db2 replication.

- **Snapshot + Stream**
    - Nilus can snapshot source tables to initialize downstream stores.
    - After snapshot, it switches to streaming, reading incremental changes continuously from CD tables.

- **Change Data Tables (CD Tables)**
    - For each registered source table, Db2 creates a corresponding CD table.
    - Structure = Source table columns + CDC metadata:
      - Operation type (`I/U/D`)
      - Commit LSN
      - Timestamp
      - Transaction identifiers
    - These tables are continuously populated by the capture agent.

- **Re-initialization**
    - CDC capture must be reinitialized after events such as:
      - Adding/removing source tables.
      - Schema modifications.
      - Capture agent restart or failure recovery.
      - CD table truncation or corruption.

- **Replica Identity in Db2**
    - Similar to PostgreSQL’s concept of replica identity.
    - Source tables must have a primary key or unique index.
    - Without this, Db2 cannot uniquely identify updated/deleted rows in the CD table.

- **Log Reading & LSNs**
    - Db2 CDC relies on transaction logs.
    - Each change is associated with a Log Sequence Number (LSN).
    - Nilus uses LSNs to:
      - Guarantee ordering.
      - Track resume position after restarts.

- **Data Latency**
    - Changes are not instantly visible in CD tables.
    - A small latency window exists between commit → capture → CD table population.
    - Polling interval (`poll.interval.ms`) controls how often Nilus queries CD tables.

- **Monitoring & Maintenance**
    - Key monitoring tasks:
      - CD table growth: prune/archive if needed.
      - Capture agent health: ensure `asncap` is running.
      - Re-initialization events: watch for schema changes.
    - Commands like:
      ```sql
      SELECT * FROM ASNCDC.IBMSNAP_REGISTER;
      ```
      help validate which tables are CDC-enabled.

- **Error Handling**
    - If CD tables are dropped, truncated, or corrupted, Nilus cannot resume from offsets.
    - In these cases, Nilus must re-snapshot the source.
    - Proper backup/restore of CDC schema helps mitigate data loss.
