# Redis

DataOS allows you to connect to Redis using Depot. The Depot then enables querying of live data stored in Redis and provides access to all of Redis' data structures - String, Hash, List, Set, and Sorted Set. You can also read Data Frames.

## Requirements

To connect to Redis, you need:

- Hostname
- Port
- DB name
- Table
- Password

## Template

To create a Depot of type ‘REDIS‘, use the following template:

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
  type: REDIS                                    # Depot type
  description: <description>
  external: true
  connectionSecret:                              # Data source specific configurations
    - acl: rw
      values:
        password: <password>
    - acl: r
      values:
        password: <password>
  spec:                                          # Data source specific configurations
      host: "localhost"
      port: 5432
      db: 10
      table: "user"        
```