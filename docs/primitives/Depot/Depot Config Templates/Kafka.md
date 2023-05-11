# Kafka

DataOS allows you to create a Depot of type 'KAFKA' to read live topic data. The created Depot enables you to read live streaming data.

## Requirements

To connect to Kafka, you need:

- KAFKA broker list

Once you provide the broker list, the Depot enables fetching all the topics in the KAFKA cluster.

## Template

To create a Depot of type 'KAFKA', use the following template:

```yaml
version: v1
name: <depot-name>
type: depot
tags:
  - <tag1>
owner: <owner-name>
layer: user
depot:
  type: KAFKA                     # Depot type
  description: <description>
  external: true
  spec:                           # Data source specific configurations
    brokers:
      - <broker1>
      - <broker2>
```

> 📌 Note: The support for creating 'KAFKA' Depot using secrets in configuration is coming soon.
>