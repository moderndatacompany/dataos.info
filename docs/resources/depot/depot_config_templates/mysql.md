# MySQL

DataOS allows you to connect to a MySQL database and read data from tables using Depots. A Depot provides access to all tables within the specified schema of the configured database. You can create multiple Depots to connect to different MySQL servers or databases.

## Requirements

To connect to a MySQL database, you need the following information:

- Host URL and parameters: The URL or hostname of the MySQL server along with any additional parameters required for the connection.
- Port: The port number used for the MySQL connection.
- Username: The username for authentication.
- Password: The password for authentication.

## Template

To create a Depot of type ‘MYSQL‘, utilize the following template:

**Use this template, if self-signed certificate is enabled.**

```yaml
version: v1
name: {{mysql01}}
type: depot
tags:
  - {{dropzone}}
  - {{mysql}}
layer: user
depot:
  type: MYSQL
  description: {{"MYSQL Sample Database"}}
  spec:
    subprotocol: "mysql"
    host: {{host}}
    port: {{port}}
    params: # Required
      tls: {{skip-verify}}
  external: {{true}}
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: {{username}}
        password: {{password}}
```
**If self-signed certificates are not being used** by your organization, you can omit the params section within the spec:

```yaml
version: v1
name: {{"mysql01"}}
type: depot
tags:
  - {{dropzone}}
  - {{mysql}}
layer: user
depot:
  type: MYSQL
  description: {{"MYSQL Sample data"}}
  spec:
    host: {{host}}
    port: {{port}}
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: {{username}}
        password: {{password}}
```