# Elasticsearch


DataOS allows you to connect to Elasticsearch data using Depot. The Depot enables the access to all documents visible to the specified user for text queries and analytics.

## Requirements

To connect to Elasticsearch, you need:

- Username
- Password
- Nodes, Hostname/URL of the server and ports

## Template

To create a Depot of type ‘ELASTICSEARCH‘, use the following template:

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
  type: ELASTICSEARCH              **# Depot type**
  description: <description>
  external: true
  connectionSecret:                **# Data source specific configurations**
    - acl: rw
      values:
        username: <username>
        password: <password>
    - acl: r
      values:
        username: <username>
        password: <password>
  spec:                            **# Data source specific configurations**
    nodes: ["localhost:9092", "localhost:9093"]
```