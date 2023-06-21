# MySQL


DataOS allows you to connect to the MySQL database to read data from tables using Depots. The Depot enables access to all tables visible to the specified schema in the configured database. You can create as many Depots as you need to access additional MYSQL servers/databases.

## Requirements

To connect to the MySQL database, you need:

- Host URL and parameters
- Port
- Username
- Password

## Template

To create a Depot of type ‘MYSQL‘, use the following template:

**Use this template, if self-signed certificate is enabled.**

```yaml
version: v1
name: "mysql01"
type: depot
tags:
  - dropzone
  - mysql
layer: user
depot:
  type: MYSQL
  description: "MYSQL Sample Database"
  spec:
    subprotocol: "mysql"
    host: 
    port: 
    params: #required in this scenario
      tls: skip-verify
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: <get from the operator>
        password: <get from the operator>
```

**If self-signed certificates are not being used** by your organisation, for connection to these storage systems, then you do not need to write additional parameters within the spec section.

```yaml
version: v1
name: "mysql01"
type: depot
tags:
  - dropzone
  - mysql
layer: user
depot:
  type: MYSQL
  description: "MYSQL Sample data"
  spec:
    host:
    port:
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: <get from the operator>
        password: <get from the operator>
```