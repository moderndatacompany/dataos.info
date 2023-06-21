# Oracle


DataOS allows you to connect to Oracle database to access data from the tables using Depots. The  Depot enables access to all schemas visible to the specified service in the configured database. Connect to on-premise Oracle Database to perform various actions such as create, update, get, and delete on rows in a table. You can create as many Depots as you need to access additional Oracle servers/databases.

## Requirements

To connect to Oracle, you need:

- URL of your Oracle account
- User name, typically your login user
- Password
- Database name
- Database schema where your table belongs

## Template

To create a Depot of type ‘ORACLE‘, use the following template:

```yaml
version: v1
name: <think of a nice name>
type: depot
tags:
  - dropzone
  - oracle
layer: user
depot:
  type: ORACLE                                     **# Depot type**
  description: "Oracle Sample data"
  spec:                                            **# Data source specific configurations**
    host: 
    port: 
    service: 
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: <get a hold of it>
        password: <you have to earn it>
```
