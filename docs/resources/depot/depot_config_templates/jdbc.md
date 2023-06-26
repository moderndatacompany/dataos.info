# JDBC

DataOS provides the capability to establish a connection to a database using the JDBC driver in order to read data from tables using a Depot. The Depot facilitates access to all schemas visible to the specified user within the configured database.

## Requirements

To establish a JDBC connection, the following information is required:

- Database name: The name of the database you want to connect to.
- Subprotocol name: The subprotocol associated with the database (e.g., MySQL, PostgreSQL).
- Hostname/URL of the server, port, and parameters: The server's hostname or URL, along with the - port and any additional parameters needed for the connection.
- Username: The username to authenticate the JDBC connection.
- Password: The password associated with the provided username.

## Template

To create a Depot of type ‘JDBC‘, utilize the following template:

```yaml
version: v1
name: {{depot-name}}
type: depot
tags:
  - {{tag1}}
owner: {{owner-name}}
layer: user
depot:
  type: JDBC                                      
  description: {{description}}
  external: {{true}}
  connectionSecret:                              
    - acl: rw
      type: key-value-properties
      data:
        username: {{jdbc-username}}
        password: {{jdbc-password}}
    - acl: r
      type: key-value-properties
      data:
        username: {{jdbc-username}}
        password: {{jdbc-password}}
  spec:                                           
    subprotocol: {{subprotocol}}
    host: {{host}}
    port: {{port}}
    database: {{database-name}}
    params:
      {{"key1": "value1"}}
      {{"key2": "value2"}}
```