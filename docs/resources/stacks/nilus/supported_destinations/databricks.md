# Databricks

Nilus offers seamless integration with Databricks as a destination for both Batch and Change Data Capture (CDC) pipelines via the Databricks SQL Warehouse. Data ingested or created through this integration is stored as Delta Lake tables within the specified **Unity Catalog** (`catalog.schema`). 

Additionally, Databricks can serve as a **source** for batch data extraction, enabling comprehensive data movement workflows within Nilus.


## Prerequisites

The following setup and permissions must be ensured before configuring Databricks as a sink in Nilus.

- **Databricks SQL Warehouse Access:** The target SQL Warehouse must be **active** and accessible from Nilus.

- **Unity Catalog Configuration:** The destination **catalog** and **schema** must exist before data load.

- **Authentication:** Nilus uses a **Personal Access Token (PAT)** to authenticate with Databricks.

- **Sink Permissions:** The user associated with the token must have:
    - Access to the SQL Warehouse
    - `CREATE` and `INSERT` privileges on the target `catalog.schema`
    - Additional permissions (`UPDATE`, `DELETE`) if using the `merge` strategy.

!!! info
    Contact the DataOS Administrator or Operator to obtain configured Depot UDL and other required parameters.


## Sink Configuration

=== "Syntax"
    ```yaml
    sink:
      address: databricks://token:<access_token>@<server_hostname>?http_path=<http_path>&catalog=<catalog>&schema=<schema>
      options:
        dest-table: <table_name>
        incremental-strategy: <append|replace|merge>
    ```

=== "Example"
    ```yaml
    name: salesforce-to-dbx
    version: v1
    type: service
    workspace: public
    service:
      stack: nilus:1.0
      compute: runnable-default
      replicas: 1
      servicePort: 9010
      logLevel: INFO
      stackSpec:
        source:
          address: "salesforce://?username={SALESFORCE_USERNAME}&password={SALESFORCE_PASSWORD}&token={SALESFORCE_TOKEN}"
          options:
            source-table: "account"
        sink:
          address: databricks://token:{DATABRICKS_TOKEN}@{DATABRICKS_HOST}?http_path={DATABRICKS_HTTP_PATH}&catalog=main&schema=analytics
          options:
            dest-table: account
            incremental-strategy: append
    ```

- The connection URI follows this format:

  ```bash
  databricks://token:<access_token>@<server_hostname>?http_path=<http_path>&catalog=<catalog>&schema=<schema>
  ```

- Nilus executes all SQL DDL/DML operations through the configured **SQL Warehouse**.
- All tables are stored as **Delta** format tables managed by the **Unity Catalog**.


| **Parameter** | **Description** |   **Callouts**  |
| --- | --- |--- |
| `catalog`           | Unity Catalog where the Delta table resides                     | Must exist prior to load                                      |
| `schema`            | Schema within the catalog for table creation                    | Required for Nilus routing                                    |
| `http_path`         | SQL Warehouse endpoint path (`/sql/1.0/warehouses/<id>`)        | Must point to an active warehouse                             |
| `access_token`      | Databricks Personal Access Token for authentication             | Ensure proper scope and expiry                                |
| `server_hostname`   | Hostname of the Databricks workspace                            | e.g., `dbc-123abc-def.cloud.databricks.com`                   |


## Sink Attributes Details

Nilus supports the following Databricks sink configuration options:

| Option                 | Required | Description                                                     | Callouts                                                      |
| ---------------------- | -------- | --------------------------------------------------------------- | ------------------------------------------------------------- |
| `dest-table`           | Yes      | Destination table name within the specified `catalog.schema`    | Must not include schema prefix if already defined in sink URI |
| `incremental-strategy` | Yes      | Defines write behavior — one of `append`, `replace`, or `merge` | `merge` requires upsert logic support                         |




## Compute and Table Format

* **Compute:** The Databricks SQL Warehouse specified by `http_path` executes all queries on behalf of Nilus. Nilus operates as a client connection using standard JDBC/ODBC-compatible APIs.
* **Table Format:** All tables are created as **Delta tables** within the specified Unity Catalog schema. Nilus does not modify Databricks default Delta behavior.


## Troubleshooting

| Issue                                  | Cause                                                      | Resolution                                                                     |
| -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Invalid HTTP Path / Inactive Warehouse | The SQL Warehouse is suspended or `http_path` is incorrect | Resume or validate the correct warehouse path in Databricks                    |
| Permission Denied                      | PAT lacks required privileges on target schema             | Grant `CREATE` and `INSERT` (and `UPDATE` for merge) on the destination schema |
| Connection Failure                     | Invalid token or workspace hostname                        | Verify token validity and workspace endpoint                                   |

