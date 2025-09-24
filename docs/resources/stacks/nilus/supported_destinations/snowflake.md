# Snowflake

Snowflake is a cloud-native data warehouse known for its elasticity, scalability, and ability to handle structured and semi-structured data. The **Nilus connector** supports Redshift as a **destination** for both **Change Data Capture (CDC)** and **Batch** data movement, enabling real-time streaming–style upserts or scheduled bulk loads.

Nilus connects to Snowflake either via a standard connection URI or through DataOS Depot, which manages authentication, secrets, and connection parameters centrally.

## Prerequisites

The following configurations must be set up before using the Snowflake:

### **Database User Permissions**

The Snowflake user must be granted the following privileges:

```sql
-- Database access
GRANT USAGE ON DATABASE <database_name> TO <username>;
GRANT USAGE ON SCHEMA <schema_name> TO <username>;
GRANT SELECT ON ALL TABLES IN SCHEMA <schema_name> TO <username>;

-- Warehouse access
GRANT USAGE ON WAREHOUSE <warehouse_name> TO <username>;

-- Role requirements
GRANT ROLE <role_name> TO USER <username>;
```

### **Required Parameters**

| Parameter   | Description                                                                                                                                                                           |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `username`  | Snowflake account username                                                                                                                                                            |
| `password`  | Snowflake user’s password                                                                                                                                                             |
| `account`   | <p>Snowflake account identifier (e.g., <code>xy12345.snowflakecomputing.com</code>)<br>If your user has defaults for role/warehouse, you may omit them; otherwise set explicitly.</p> |
| `database`  | Target database name                                                                                                                                                                  |
| `warehouse` | Virtual warehouse to use (required)                                                                                                                                                   |
| `role`      | Role for connection (optional)                                                                                                                                                        |

## Sink Configuration

=== "Syntax with Depot"
    ```yaml
    sink:
      address: dataos://snowflake_depot
      options:
        dest-table: analytics.orders
        incremental-strategy: append
    ```
=== "Syntax without Depot"
    ```yaml
    sink:
      address: snowflake://user:password@account/database?warehouse=COMPUTE_WH
      options:
        dest-table: analytics.orders_snapshot
        incremental-strategy: replace
    ```
=== "Example"
    ```yaml
    name: nb-lh-aws-test-01
    version: v1
    type: workflow
    tags:
        - workflow
        - nilus-batch
    description: Nilus Batch Workflow Sample for AWS Lakehouse to Snowflake
    workspace: research
    workflow:
      dag:
        - name: nb-job-01
          spec:
            stack: nilus:1.0
            compute: runnable-default
            logLevel: INFO
            resources:
              requests:
                cpu: 500m
                memory: 512Mi
            stackSpec:
              source:
                address: dataos://testawslh
                options:
                  source-table: sales.orders
              sink:
                address: dataos://snowflake_depot
                options:
                  dest-table: retail.orders
                  incremental-strategy: append
    ```

## Sink Attributes Details

Nilus supports the following Redshift sink configuration options:

| Option                 | Required | Description                                    |
| ---------------------- | -------- | ---------------------------------------------- |
| `dest-table`           | Yes      | Destination table name in dataset.table format |
| `incremental-strategy` | Yes      | Strategy for writes (`append`, `replace`)      |
