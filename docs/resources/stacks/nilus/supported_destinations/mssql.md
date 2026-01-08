# MS SQL Server

Microsoft SQL Server (MS SQL Server) is a robust relational database system developed by Microsoft. The Nilus connector supports MS SQL Server as a destination, enabling both Change Data Capture (CDC) and Batch data movement—whether streaming in real time or bulk ingestion on a schedule.

Nilus connects to MS SQL Server using standard drivers (via ODBC) and supports upsert (`merge`), append, and replace strategies, as well as efficient staging for bulk loads.

## Prerequisites

The following configurations must be set up before using the MS SQL Server:

* **Network Reachability:** Nilus must connect over TCP/IP to the SQL Server host.
* **Database & Schema:** The target database and schema should be pre-created.
* **Sink User Permissions:** Nilus sink user should have, at minimum:
    * `CONNECT` on the database
    * `USAGE` on target schema
    * `CREATE` & `INSERT` for table creation and data loading
    * `UPDATE` & `DELETE` if using incremental `merge`
    * `DROP` or `TRUNCATE` for full replace operations

!!! info
    - In production environments, while full ownership simplifies setup, it's recommended to use least-privilege access limited to the destination schema.
    - Contact the DataOS Administrator or Operator to obtain configured Depot UDL and other required parameters.



## Sink Configuration

=== "Syntax"
    ```yaml
    sink:
      address: dataos://sqlserver_depot
      options:
        dest-table: retail.orders
        incremental-strategy: merge
        primary-key: order_id
    ```
=== "Example"
    ```yaml
    name: nb-lh-aws-test-01
    version: v1
    type: workflow
    tags:
        - workflow
        - nilus-batch
    description: Nilus Batch Workflow Sample for AWS Lakehouse to MSSQL
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
                address: dataos://sqlserver_depot
                options:
                  dest-table: retail.orders
                  incremental-strategy: merge
                  primary-key: order_id
    ```

## Sink Attributes Details

Nilus supports the following PostgreSQL sink configuration options:

| Option                 | Required           | Description                                                | Callouts                     |
| ---------------------- | ------------------ | ---------------------------------------------------------- | ---------------------------- |
| `dest-table`           | Yes                | Destination table name in `schema.table` format            |                              |
| `incremental-strategy` | Yes                | Strategy for writes (`append`, `replace`, `merge`)         | Merge requires `primary-key` |
| `primary-key`          | Required for merge | Column(s) used to deduplicate                              |                              |
| `aws_region`           | Optional           | Only for AWS-backed setups if required by your environment |                              |

* A `primary-key` is needed for `merge` when using `mode`/`incremental-strategy`.
* Ensure `DROP` or `TRUNCATE` privileges are available for `replace` mode.
* The `COPY` privilege is necessary for staging loaders.
* For S3/Lakehouse workflows, include the `aws_region`.
