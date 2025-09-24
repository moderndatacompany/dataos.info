# Redshift

Amazon Redshift is a fully managed, petabyte-scale data warehouse service in AWS that allows fast query performance and scalability. The **Nilus connector** supports Redshift as a **destination** for both **Change Data Capture (CDC)** and **Batch** data movement, enabling real-time streaming–style upserts or scheduled bulk loads.

Nilus connects to Redshift either via a direct connection URI or through DataOS Depot, which centralizes authentication, credentials, and connection details.

## Prerequisites

The following configurations must be set up before using the Redshift:

### **Database User Permissions**

The Redshift user must be granted the following privileges:

```sql
-- Database-level access
GRANT USAGE ON DATABASE <database_name> TO <username>;

-- Schema-level access
GRANT USAGE ON SCHEMA <schema_name> TO <username>;

-- Table-level access
GRANT SELECT ON ALL TABLES IN SCHEMA <schema_name> TO <username>;

-- Additional
GRANT SELECT ON <schema_name>.<table_name> TO <username>;
```

### **Required Parameters**

| Parameter  | Description                   |
| ---------- | ----------------------------- |
| `username` | Redshift database username    |
| `password` | User’s password               |
| `host`     | Redshift cluster endpoint     |
| `port`     | Redshift port (default: 5439) |
| `database` | Target database name          |

## Sink Configuration

=== "Syntax with Depot"
    ```yaml
    sink:
      address: dataos://redshift_depot
      options:
        dest-table: retail.orders
        incremental-strategy: append
    ```
=== "Syntax without Depot"
    ```yaml
    sink:
      address: redshift://user:password@host:port/dbname?sslmode=require
      options:
        dest-table: retail.orders
        incremental-strategy: append
    ```
=== "Example"
    ```yaml
    name: nb-lh-aws-test-01
    version: v1
    type: workflow
    tags:
        - workflow
        - nilus-batch
    description: Nilus Batch Workflow Sample for AWS Lakehouse to Redshift
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
                address: redshift://user:password@host:port/dbname?sslmode=require
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



