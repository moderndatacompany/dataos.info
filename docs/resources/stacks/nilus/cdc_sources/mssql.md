# MS SQL Server

The Nilus connector for **Microsoft SQL Server** supports **Change Data Capture (CDC)**, enabling real-time replication of changes from PostgreSQL transactional databases to [Supported Destinations](/resources/stacks/nilus/supported_destinations/), such as the Lakehouse. **CDC** uses SQL Server’s built-in CDC feature to capture `INSERT`, `UPDATE`, and `DELETE` operations on source tables.

## Prerequisites 

Before enabling CDC, ensure the following configurations depending on your hosting environment:

### **Version Compatibility**

* SQL Server **2016 SP1** or later (Standard or Enterprise editions).
* Supported: **2017, 2019, 2022**.

### **User Permissions**

The connection user requires:

* **`db_owner` role in:**
    * `master` database (for database-level setup).
    * Target database(s) (for CDC configuration).
* **Additional grants:**
    * `VIEW SERVER STATE`
    * `SELECT` on the `cdc` schema
* Access to **SQL Server Agent jobs** (tables: `sysjobs`, `sysjobactivity`) if CDC jobs are used.

!!! info
    SQL Server Agent must be enabled for CDC to function.


### **CDC Setup in SQL Server**

Change data capture is not enabled on the database and tables **by default** in MS SQL Server

```sql
USE demodb;
GRANT SELECT ON SCHEMA::cdc TO PUBLIC;
```

The user needs to perform the steps below to enable it before running the CDC service.

1.  **Enable CDC at Database Level**

    ```sql
    USE demodb;
    EXEC sys.sp_cdc_enable_db;

    -- Verify
    SELECT name, is_cdc_enabled FROM sys.databases WHERE name = 'demodb';
    ```

2.  **Enable CDC on a Table**

    ```sql
    USE demodb;
    EXEC sys.sp_cdc_enable_table
      @source_schema = N'dbo',
      @source_name = N'cdc_test',
      @role_name = NULL,
      @supports_net_changes = 1;
      
    -- Verify
    SELECT * FROM cdc.change_tables;
    ```

!!! info
    Contact the Database Administrator (DBA) to set up Change Data Capture (CDC) or to provide the correct values for parameters such as database name, table name, etc.


### **Pre-created SQL Server Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
|    NAME    | VERSION | TYPE  | STATUS | OWNER    |
| ---------- | ------- | ----- | ------ | -------- |
| mssqldepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create the SQL Server Depot:

??? note "MS SQL Depot Manifest"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    description: ${{description}}
    tags:
        - ${{tag1}}
        - ${{tag2}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: JDBC                                       
      external: ${{true}}
      compute: ${{runnable-default}}
      jdbc:
        subprotocol: ${{sqlserver}}
        host: ${{host}}
        port: ${{port}}
        database: ${{database}}
      secrets:
        - name: ${{instance-secret-name}}-r
          allkeys: true
        - name: ${{instance-secret-name}}-rw
          allkeys: true
    ```

    !!! info
        Update variables such as `name`, `owner`, `compute`, `layer`,`host`, `port`, `database` etc., and contact the DataOS Administrator or Operator to obtain the appropriate secret name.




## Sample Service Config

Following manifest configuration template can be use to apply the CDC for SQL Server:

```yaml
name: mssql-cdc-service
version: v1
type: service
tags:
    - mssql
    - cdc
description: Nilus CDC Service for MSSQL Server
workspace: public
service:
  servicePort: 9010
  replicas: 1
  logLevel: INFO
  compute: runnable-default
  resources:
    requests:
      cpu: 100m
      memory: 256Mi
  stack: nilus:1.0
  stackSpec:
    source:
      address: dataos://mssqldepot
      options:
        engine: debezium
        table.include.list: "dbo.cdc_test"
        topic.prefix: "mssql"
        snapshot.mode: initial
        max.batch.size: 5000
        max.queue.size: 20000
        heartbeat.interval.ms: 60000
        poll.interval.ms: 5000
    sink:
      address: dataos://lakehousedepot
      options:
        dest-table: sqlserver_cdc_test
        incremental-strategy: append
        aws_region: us-west-2
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, dest-table, and table.include.list) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Service YAML}}
```

## Source Options

Nilus supports the following SQL Server CDC source options:

| Option                   | Default    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                   | No default | Unique name for the connector. Required by all Nilus connectors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `topic.prefix`           | No default | Topic prefix that provides a namespace for the particular SQL Server database server or cluster in which Nilus is capturing changes. The prefix should be unique across all other connectors. Only alphanumeric characters, hyphens, dots and underscores must be used in the database server logical name. This is mandatory. This prefix is also appended to the sink table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `schema.include.list`    | No default | Comma-separated list of regular expressions matching schema names to include in monitoring. All non-system tables present in the defined schemas will be monitored for CDC. Cannot be used with `schema.exclude.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `schema.exclude.list`    | No default | Comma-separated list of regular expressions matching schema names to exclude from monitoring. Cannot be used with `schema.include.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `table.include.list`     | No default | Comma-separated list of regular expressions matching fully-qualified table identifiers to include in monitoring. Each identifier is of the form `schemaName.tableName`. Cannot be used with `table.exclude.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `table.exclude.list`     | No default | Comma-separated list of regular expressions matching fully-qualified table identifiers to exclude from monitoring. Each identifier is of the form `schemaName.tableName`. Cannot be used with `table.include.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `column.include.list`    | No default | Comma-separated list of regular expressions matching fully-qualified column names to include in change event records. Fully qualified names for columns are of the form `schemaName.tableName.columnName`. Cannot be used with `column.exclude.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `column.exclude.list`    | No default | Comma-separated list of regular expressions matching fully-qualified column names to exclude from change event records. Fully qualified names for columns are of the form `schemaName.tableName.columnName`. Cannot be used with `column.include.list`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `max.batch.size`         | `2048`     | Maximum size of each batch of events processed during each iteration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `snapshot.mode`          | `initial`  | <p>Specifies the behavior for snapshots when the connector starts.<br>Options:<br><code>always</code>: The connector performs a snapshot every time that it starts. The snapshot includes the structure and data of the captured tables. Specify this value to populate topics with a complete representation of the data from the captured tables every time that the connector starts. After the snapshot completes, the connector begins to stream event records for subsequent database changes.<br><code>initial</code>: The connector performs a snapshot only when no offsets have been recorded for the logical server name.<br><code>no_data</code>: The connector performs an initial snapshot and then stops, without processing any subsequent changes.<br><code>initial_only</code>: The connector never performs snapshots. <code>when_needed</code>: After the connector starts, it performs a snapshot only if it detects one of the following circumstances:- It cannot detect any topic offsets.- A previously recorded offset specifies a log position that is not available on the server.<br><em><strong><code>recovery</code></strong></em>Set this option to restore a database schema history topic that is lost or corrupted. After a restart, the connector runs a snapshot that rebuilds the topic from the source tables. You can also set the property to periodically prune a database schema history topic that experiences unexpected growth.<br><em><strong><code>when_needed</code></strong></em>After the connector starts, it performs a snapshot only if it detects one of the following circumstances:It cannot detect any topic offsets.A previously recorded offset specifies a log position that is not available on the server.<br><strong><code>configuration_based</code></strong> Set the snapshot mode to <code>configuration_based</code> to control snapshot behavior through the set of connector properties that have the prefix 'snapshot.mode.configuration.based'.</p> |
| `decimal.handling.mode`  | `precise`  | Specifies how the connector should handle values for `DECIMAL` and `NUMERIC` columns:`precise` (the default) represents them precisely using `java.math.BigDecimal` values represented in change events in a binary form.`double` represents them using `double` values, which may result in a loss of precision but is easier to use.`string` encodes values as formatted strings, which is easy to consume but semantic information about the real type is lost.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `include.schema.changes` | true       | Boolean value that specifies whether the connector publishes changes in the database schema to a internal table with the same name as the topic prefix. The connector records each schema change with a key that contains the database name, and a value that is a JSON structure that describes the schema update. This mechanism for recording schema changes is independent of the connector’s internal recording of changes to the database schema history.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Sink Options

Nilus supports the following sink options for SQL Server CDC workflows:

| Field                  | Description                                | Default  |
| ---------------------- | ------------------------------------------ | -------- |
| `dest-table`           | Target table in the sink.                  | —        |
| `incremental-strategy` | Write mode (`append` recommended for CDC). | `append` |
| `aws_region`           | AWS region (for S3-backed Lakehouse).      | —        |

## Core Concepts

Following are the Core Concepts related to MS SQL server:

1. **SQL Server CDC Framework**
      1. SQL Server’s native **CDC feature** records `INSERT`, `UPDATE`, and `DELETE` operations on tracked tables.
      2. CDC data is written to **change tables** in the `cdc` schema (e.g., `cdc.dbo_orders_CT`).
      3. **CDC Jobs**: Two SQL Server Agent jobs are created automatically:
            1. `cdc.demodb_capture`: Captures changes from the transaction log.
            2. `cdc.demodb_cleanup`: Cleans up old CDC data.
      4. Nilus consumes these change tables to emit structured CDC events.
2. **Transaction Log & LSN**
      1. All SQL Server changes are first written to the **transaction log**.
      2. Each event has a **Log Sequence Number (LSN)**, which Nilus uses to:
            1. Resume from the last processed offset.
            2. Ensure change ordering.
            3. Detect data loss if LSN ranges roll off before being consumed.
3. **Snapshot + Stream**
      1. On first run, Nilus may perform a **snapshot (**&#x49;f configure&#x64;**)**:
            1. Captures the baseline table contents.
            2. Emits op: r events for each row.
      2. After snapshotting, Nilus switches to **streaming mode**, consuming changes from CDC tables continuously.
4.  **CDC Change Tables**
      Each CDC-enabled table has a corresponding **change table** with:
      1. Source columns.
      2. Metadata:
             1. `__$start_lsn` → transaction commit LSN.
             2. `__$seqval` → event ordering within a transaction.
             3. `__$operation` → change type (1=delete, 2=insert, 3=before update, 4=after update).
             4. `__$update_mask` → bitmask showing changed columns.
   
5. **Cleanup and Retention**

      1. SQL Server periodically runs **cleanup jobs** to purge change tables.
      2. If Nilus lags beyond the retention window, data loss occurs → requires **re-snapshot**.
      3. Recommendation: extend retention to cover expected downtime or pipeline backpressure.

6.  **Monitoring & Maintenance**

       1. Validate that **CDC jobs** (`cdc.cdc_jobs`) are running.
       2. Track:
             1. Change table growth.
             2. Cleanup job latency.
             3. Connector LSN position.
       3. Adjust `poll.interval.ms` and CDC retention to avoid missed events.

### **Schema Evolution**

SQL Server CDC does not automatically adapt to schema changes. Nilus handles schema evolution by migrating to a new capture instance when schema changes are detected.

Schema changes (ALTER TABLE) are common in operational databases. Nilus handles schema evolution in two modes:

**Online Schema Evolution**

* Supported for **non-breaking changes**:
    * Adding a new nullable column.
    * Adding default values.
* Nilus detects schema changes in the base table, updates its internal schema cache, and continues streaming with minimal disruption.
* New fields appear in CDC events from the point of change.

??? note "Step-by-step commands to perform Online Schema Evolution."

    **Step 1: Apply Schema Changes to Source Table**

    When the source table has the new column (updated schema), but the existing CDC capture instance will still use the old schema by design.

    ```sql
    ALTER TABLE demodb.dbo.cdc_test
    ADD new_col VARCHAR(100);
    ```

    **Step 2: Create New CDC Capture Instance**

    A new capture table needs to be created with the updated schema. Both old and new capture instances exist simultaneously.

    ```sql
    EXEC sys.sp_cdc_enable_table 
      @source_schema = 'dbo', 
      @source_name = 'cdc_test', 
      @role_name = NULL, 
      @supports_net_changes = 0, 
      @capture_instance = 'dbo_cdc_test_v2';
    ```

    **Step 3: Insert Data to Test New Schema**

    New data includes the `new_col` field and will be captured by the new capture instance.

    ```sql
    INSERT INTO demodb.dbo.cdc_test (
      CustomerID, FirstName, LastName, Email, new_col
    ) VALUES (
      4, N'Charlie', N'Brown', N'charlie.brown@example.com', N'TEST_DATA'
    );
    ```

    **Step 4: Monitor Schema Migration**

    Nilus detects the schema change and migrates to the new capture instance:

    ```prolog
    INFO - Multiple capture instances present for the same table: Capture instance "dbo_cdc_test_v1" and Capture instance "dbo_cdc_test_v2"
    INFO - Schema will be changed for Capture instance "dbo_cdc_test_v2"
    INFO - Migrating schema to Capture instance "dbo_cdc_test_v2"
    ```

    **Step 5: Verify Schema Migration**

    Check that the new column appears in downstream systems:

    ```sql
    - Check the CDC capture tables
    SELECT  FROM cdc.change_tables;
    - Verify new column in capture instance
    SELECT TOP 5  FROM cdc.dbo_cdc_test_v2_CT ORDER BY __$start_lsn DESC;
    ```

    **Step 6: Clean Up Old Capture Instance**

    **Important:** Only perform this step after confirming that the new capture table has successfully migrated to the new capture instance.

    ```sql
    EXEC sys.sp_cdc_disable_table 
      @source_schema = 'dbo', 
      @source_name = 'cdc_test', 
      @capture_instance = 'dbo_cdc_test_v1';
    ```



**Offline Schema Evolution**

* Required for **breaking changes**, such as:
    * Dropping a column.
    * Changing column type incompatibly (e.g., `VARCHAR` → `INT`).
    * Renaming a column.
* In these cases:
    * CDC for the table must be **disabled and re-enabled**.
    * Nilus must be **reinitialized with a new snapshot**.
* Best practice:
    * Plan downtime or maintenance windows.
    * Document schema version changes for downstream consumers.

**Key Takeaway:**

* Online evolution = seamless updates (minimal impact).
* Offline evolution = requires service re-initialization and snapshotting.

### **Best Practice**

*   Enable CDC on database and table level:

    ```sql
    EXEC sys.sp_cdc_enable_db;
    EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'orders', @role_name = NULL;
    ```

* **Online schema evolution** is safe for non-breaking changes.
* For breaking changes, plan **offline schema evolution** with snapshot reinitialization.
* Align CDC retention with max expected downtime.
* Monitor CDC jobs to avoid lag or cleanup issues.

