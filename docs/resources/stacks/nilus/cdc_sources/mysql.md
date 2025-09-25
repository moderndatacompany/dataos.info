# MySQL

The Nilus connector for MySQL supports Change Data Capture (CDC), which captures row-level changes from MySQL's binary log (binlog) and streams them to the [Supported Destinations](/resources/stacks/nilus/supported_destinations/), such as the Lakehouse. Nilus CDC in MySQL continuously reads the binlog to capture `INSERT`, `UPDATE`, and `DELETE` operations.

## Prerequisites 

Before enabling CDC, ensure the following configurations:

### **MySQL Server Configuration**

- **Enable binlog** in **row‑based format**:

      ```sql
      server-id = <unique-id>
      log_bin = mysql-bin
      binlog_format = ROW
      binlog_row_image = FULL
      ```

- **Recommended**: Enable GTID (Global Transaction Identifier) for consistency and easier replication—especially in HA (High Availability) environments.

- Binlog retention (`expire_logs_days`) should be set such that logs aren’t purged before Nilus processes them.

### **Supported Topologies**

Nilus works with various MySQL architectures:

* Standalone
* Primary–Replica (reads from one binlog-streaming instance)
* High-Availability clusters using GTID (including multi-primary Network Database Clusters)
* Hosted platforms (e.g., RDS/Aurora), though note that global read locks may not be allowed. In such cases, Nilus uses table-level locks for consistent snapshots.

### **Configure MySQL for CDC**

!!! info
    Contact the Database Administrator (DBA) to either set up Change Data Capture (CDC) or to provide the correct values for parameters such as  `server-id`, `log_bin`, `port`, `snapshot` etc.


To configure Change Data Capture (CDC) in MySQL, follow these steps:&#x20;

1.  **Edit `my.cnf` (or pass as Docker args):** 
      


      ```ini
      [mysqld]
      server-id               = 184054
      log_bin                 = mysql-bin
      binlog_format           = ROW
      binlog_row_image        = FULL
      gtid_mode               = ON
      enforce_gtid_consistency= ON
      ```

      Restart MySQL after these changes.

2.  **Create CDC User**


    Connect as root:

    ```sql
    CREATE USER 'cdcuser'@'%' IDENTIFIED BY 'cdcpass';

    GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, LOCK TABLES ON *.* TO 'cdcuser'@'%';
    GRANT ALL PRIVILEGES ON sampledb.* TO 'cdcuser'@'%';

    -- (For MySQL 8+ auth issues)
    ALTER USER 'cdcuser'@'%' IDENTIFIED WITH mysql_native_password BY 'cdcpass';
    FLUSH PRIVILEGES;
    ```


3. **Important Notes**

      1. Ensure tables have a primary key for CDC functionality.
      2. Use fully qualified names in `table.include.list` (e.g., `database.table`).
      3. Restart the Nilus service after making changes to include lists.
      4. Ensure the table name case sensitivity exactly matches.

### **User Permissions**

Nilus requires a user with these grants:

```sql
GRANT SELECT, RELOAD, SHOW DATABASES,
REPLICATION SLAVE, REPLICATION CLIENT
ON *.* TO 'nilus'@'%';
```

If global read locks are prohibited (e.g., RDS/Aurora), also grant:

```sql
GRANT LOCK TABLES ON *.* TO 'nilus'@'%';
```

Apply `FLUSH PRIVILEGES;` afterward. 

**Tip:** If Nilus stores snapshot history in a MySQL schema, also grant `CREATE`, `INSERT`, `UPDATE`, and `DELETE` on that schema.

### **Pre-created PostgreSQL Depot** 

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
|   NAME     | VERSION | TYPE  | STATUS | OWNER    |
| ---------- | ------- | ----- | ------ | -------- |
| mysqldepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create the MySQL Depot:

??? note "MySQL Depot Manifest"

    ```yaml
    name: ${{mysqldepot}}
    version: v2alpha
    type: depot
    description: ${{"MYSQL Sample Database"}}
    tags:
      - ${{dropzone}}
      - ${{mysql}}
    layer: user
    depot:
      type: MYSQL
      external: ${{true}}
      secrets:
        - name: ${{mysql-instance-secret-name}}-r
          allkeys: true
        - name: ${{mysql-instance-secret-name}}-rw
          allkeys: true 
            - ${{mysql-instance-secret-name}}-rw
      mysql:
        subprotocol: "mysql"
        host: ${{host}}
        port: ${{port}}
        params: # Required
          tls: ${{skip-verify}}
    ```

    !!! info
        Update variables such as `name`, `owner`, and `layer`, and contact the DataOS Administrator or Operator to obtain the appropriate secret name.




## Sample Service Config

The following manifest configuration template can be used to apply the CDC for MySQL:

```yaml
name: ${{service-name}}                                    # Service identifier
version: v1                                                # Version of the service
type: service                                              # Defines the resource type
tags:                                                      # Classification tags
    - ${{tag}}                                              
    - ${{tag}}                                              
description: Nilus CDC Service for MySQL                   # Description of the service
workspace: public                                          # Workspace where the service is deployed

service:                                                   # Service specification block
  servicePort: 9010                                        # Service port
  replicas: 1                                              # Number of replicas
  logLevel: INFO                                           # Logging level
  compute: ${{query-default}}                              # Compute profile
  stack: nilus:1.0                                         # Nilus stack version
  stackSpec:                                               # Stack specification
    source:                                                # Source configuration block
      address: dataos://mysqldepot                         # Source depot address/UDL
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
         dest-table: destination_schema                    # Destination table name in sink
        incremental-strategy: append                       # Append mode for CDC write strategy
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Service YAML}}
```

## **Source Options**

| Option                                   | Default   | Description                                   | Required |
| ---------------------------------------- | --------- | --------------------------------------------- | -------- |
| `engine`                                 | —         | Must be `debezium` for CDC.                   | Yes      |
| `database.include.list` / `exclude.list` | —         | Databases to include/exclude.                 | Optional |
| `table.include.list` / `exclude.list`    | —         | Tables to include/exclude (`schema.table`).   | Optional |
| `snapshot.mode`                          | `initial` | `initial`, `when_needed`, `schema_only`, etc. | Optional |
| `include.schema.changes`                 | `true`    | Whether to emit DDL change events.            | Optional |
| `heartbeat.interval.ms`                  | `60000`   | Interval for heartbeat events.                | Optional |
| `topic.prefix`                           | —         | Prefix for change event stream topics.        | Yes      |
| `max.batch.size`                         | `2048`    | Max events per batch.                         | Optional |
| `poll.interval.ms`                       | `1000`    | Frequency for polling binlog.                 | Optional |

## Sink Options

| Field                  | Description                         | Default  |
| ---------------------- | ----------------------------------- | -------- |
| `dest-table`           | Target sink table.                  | —        |
| `incremental-strategy` | Write mode (`append` for CDC).      | `append` |
| `aws_region`           | AWS region for S3-backed Lakehouse. | —        |

## Core Concepts

1. **Supported MySQL Topologies**
      1. Standalone MySQL with binlog enabled works seamlessly.
      2. Primary/Replica replication: Nilus may follow the primary or any replica that has binlog enabled; it tracks its position per server.
      3. High-availability (HA) clusters using GTIDs are supported — failover works if the new replica is fully caught up.
      4. Cloud-hosted instances (e.g., Amazon RDS, Aurora) supported—snapshotting uses table-level locks due to the lack of global lock capability.

2. **Snapshot + Binlog Streaming**
      1. Upon startup, Nilus performs a **consistent snapshot** of selected tables using repeatable-read semantics. It then reads the binlog starting from that snapshot point.
      2. Snapshot flow:
            1. Acquire transactional locks
            2. Read table schemas and data
            3. Capture the current binlog position
            4. Release locks and begin streaming

3. **Schema Evolution Handling**
      1. The connector captures DDL statements (like `CREATE`, `ALTER`, `DROP`) from the binlog and updates its in-memory schema representation.
      2. DDL history is recorded in a database history topic to rebuild the schema on restart.
      3. Optionally, Nilus can also emit DDLs as consumer-facing schema change events to a dedicated topic (`include.schema.changes=true`).

4. **Offsets & Recovery**
      1. Supports both GTID-based tracking and traditional binlog filename + position.
      2. On restart, Nilus replays the DDL history to reconstruct the right schema state before resuming.

5. **Binlog Retention & Snapshot Safety**

      1. MySQL often purges binlogs after a retention period. Nilus’s snapshot + offset model ensures continuity, but care must be taken to prevent data loss.
      2. Use retention settings like `expire_logs_days` or `binlog_expire_logs_seconds` to ensure binlogs persist until Nilus reads them.

### **Best Practices**

- Always configure:

    ```ini
    binlog_format = ROW
    binlog_row_image = FULL
    ```

- Ensure **binlog retention** is sufficient to cover connector lag/downtime.

- Use read replicas and `when_needed` snapshot mode for minimal impact on production.

- If DDL tools (like `gh-ost`) are used, configure Nilus to include or ignore helper tables.

- Configure schema change topic with epoch = 1 partition to preserve global ordering.
