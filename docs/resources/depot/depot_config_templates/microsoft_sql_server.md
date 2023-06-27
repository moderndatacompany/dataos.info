# Microsoft SQL Server

DataOS allows you to connect to a Microsoft SQL Server database and read data from tables using Depots. A Depot provides access to all tables within the specified schema of the configured database. You can create multiple Depots to connect to different SQL servers or databases.

## Requirements

To connect to a Microsoft SQL Server database, you need the following information:

- Host URL and parameters: The URL or hostname of the SQL Server along with any additional parameters required for the connection.
- Database schema: The schema in the database where your tables are located.
- Port: The port number used for the SQL Server connection.
- Username: The username for authentication.
- Password: The password for authentication.

## Template

To create a Depot of type ‘SQLSERVER‘, utilize the following template:

**Use this template, if self-signed certificate is enabled.**

```yaml
name: {{mssql01}}
version: v1
type: depot
tags:
  - {{dropzone}}
  - {{mssql}}
layer: user
depot:
  type: JDBC
  description: {{MSSQL Sample data}}
  spec:
    subprotocol: {{sqlserver}}
    host: {{host}}
    port: {{port}}
    database: {{database}}
    params: # Required
      encrypt: {{false}}
  external: {{true}}
  hiveSync: {{false}}
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: {{username}}
        password: {{password}}
```

**If self-signed certificates are not being used** by your organization, you can omit the params section within the spec:

```yaml
name: {{mssql01}}
version: v1
type: depot
tags:
  - {{dropzone}}
  - {{mssql}}
layer: user
depot:
  type: JDBC
  description: {{MSSQL Sample data}}
  spec:
    subprotocol: sqlserver
    host: {{host}}
    port: {{port}}
    database: {{database}}
    params: {{'{"key":"value","key2":"value2"}'}}
  external: {{true}}
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: {{username}}
        password: {{password}}
```