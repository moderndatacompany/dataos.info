# Oracle

DataOS allows you to connect to an Oracle database and access data from tables using Depots. A Depot provides access to all schemas within the specified service in the configured database. You can create multiple Depots to connect to different Oracle servers or databases.

## Requirements

To connect to an Oracle database, you need the following information:

- URL of your Oracle account: The URL or hostname of the Oracle database.
- User name: Your login user name.
- Password: Your password for authentication.
- Database name: The name of the Oracle database.
- Database schema: The schema where your table belongs.

## Template

To create a Depot of type ‘ORACLE‘, you can use the following template:

```yaml
name: {{depot-name}}
version: v1
type: depot
tags:
  - {{dropzone}}
  - {{oracle}}
layer: user
depot:
  type: ORACLE                                    
  description: {{"Oracle Sample data"}}
  spec:                                            
    host: {{host}}
    port: {{port}}
    service: {{service}}
  external: {{true}}
  connectionSecret:
    - acl: {{rw}}
      type: key-value-properties
      data:
        username: {{username}}
        password: {{password}}
```
