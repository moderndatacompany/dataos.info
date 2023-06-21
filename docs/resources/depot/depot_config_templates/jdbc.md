# JDBC


DataOS allows you to connect to a database with JDBC driver to read data from tables using Depot. The Depot enables access to all schemas visible to the specified user in the configured database.

## Requirements

To connect to JDBC, you need:

- Database name
- Subprotocol name
- Hostname/URL of the server, port and parameters
- Username
- Password

## Template

To create a Depot of type ‘JDBC‘, use the following template:

```yaml
version: v1
name: <depot-name>
type: depot
tags:
  - <tag1>
owner: <owner-name>
layer: user
depot:
  type: JDBC                                      **# Depot type**
  description: <description>
  external: true
  connectionSecret:                               **# Data source specific configurations**
    - acl: rw
      type: key-value-properties
      data:
        username: <jdbc-username>
        password: <jdbc-password>
    - acl: r
      type: key-value-properties
      data:
        username: <jdbc-username>
        password: <jdbc-password>
  spec:                                           **# Data source specific configurations**
    subprotocol: <mysql|postgresql>
    host: <host>
    port: <port>
    database: <database-name>
    params:
      "key1": "value1"
      "key2": "value2"
```