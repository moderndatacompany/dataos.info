# Presto

DataOS allows you to connect to the Presto query engine for fast analytic queries against data of any size using Depot. The Depot enables access to all catalogs visible to the specified user in the configured query engine.

## Requirements

To connect to Presto, you need:

- Hostname and port
- Username
- Password
- Catalog name

## Template

To create a Depot of type ‘PRESTO‘, use the following template:

```yaml
version: v1
name: <depot-name>
type: depot
tags:
  - <tag1>
  - <tag2>
owner: <owner-name>
layer: user
depot:
  type: PRESTO                                    # Depot type
  description: <description>
  external: true
  connectionSecret:                               # Data source specific configurations
    - acl: rw
      values:
        username: <username>
        password: <password>
    - acl: r
      values:
        username: <username>
        password: <password>
  spec:                                           # Data source specific configurations
      host: "localhost"
      port: "5432"
      catalog: "postgres"
```