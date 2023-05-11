# Microsoft SQL Server

DataOS allows you to connect to the Microsoft SQL Server database to read data from tables using Depots. The Depot enables access to all tables visible to the specified schema in the configured database. You can create as many Depots as you need to access additional SQL servers/databases.

## Requirements

To connect to SQL Server database, you need:

- Host url and parameters
- Database schema where your table belongs
- Port
- Username
- Password

## Template

To create a Depot of type ‘SQLSERVER‘, use the following template:

Use this template, if self-signed certificate is enabled.

```yaml
version: v1
name: "mssql01"
type: depot
tags:
  - dropzone
  - mssql
layer: user
depot:
  type: JDBC
  description: "MSSQL Sample data"
  spec:
    subprotocol: sqlserver
    host: 
    port: 
    database:
    params: #required in this scenario
      encrypt: false
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username:
        password: 
```

If self-signed certificates are not being used by your organisation, for connection to these storage systems, then you do not need to write additional parameters within the spec section.

```yaml
version: v1
name: "mssql01"
type: depot
tags:
  - dropzone
  - mssql
layer: user
depot:
  type: JDBC
  description: "MSSQL Sample data"
  spec:
    subprotocol: "sqlserver"
    host: ""
    port: "<provide.port>"
    database: "<provide.database>"
    params: '{"key":"value","key2":"value2"}'
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: 
        password: 
```