# PostgreSQL

DataOS allows you to connect to the PostgreSQL database to read data from tables using Depot. The Depot enables access to all schemas visible to the specified user in the configured database.

## Requirements

To create a Depot to connect to the PostgreSQL database, you need:

- Database name
- Hostname/URL of the server and parameters
- Username
- Password

## Template

To create a Depot of type ‘POSTGRESQL‘, use the following template:

Use this template, if self-signed certificate is enabled.

```yaml
version: v1
name: postgresdb
type: depot
layer: user
depot:
  type: JDBC                  # Depot type
  description: To write data to postgresql database
  external: true
  connectionSecret:           # Data source specific configurations
    - acl: rw
      type: key-value-properties
      data:
        username: "<you gotta have this>"
        password: "<you gotta have this too>"
  spec:                        # Data source specific configurations
    subprotocol: "postgresql"
    host: 
    port: 
    database: postgres
    params: #required in this scenario
      sslmode: disable
```

If self-signed certificates are not being used by your organisation, for connection to these storage systems, then you do not need to write additional parameters within the spec section.

```yaml
version: v1
name: <depot-name>
type: depot
tags:
  - <tag1>
owner: <owner-name>
layer: user
depot:
  type: POSTGRESQL                                # Depot type
  description: <description>
  external: true
  connectionSecret:                               # Data source specific configurations
    - acl: rw
      type: key-value-properties
      data:
        username: <posgresql-username>
        password: <posgresql-password>
    - acl: r
      type: key-value-properties
      data:
        username: <posgresql-username>
        password: <posgresql-password>
  spec:                                           # Data source specific configurations
    host: <host>
    port: <port>
    database: <database-name>
    params: #you can remove this
      "key1": "value1"
      "key2": "value2"
```