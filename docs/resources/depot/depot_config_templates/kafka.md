# Kafka

DataOS allows you to create a Depot of type 'KAFKA' to read live topic data. This Depot enables you to access and consume real-time streaming data from Kafka.

## Requirements

To connect to Kafka, you need:

To establish a connection to Kafka, you need to provide the following information:

- KAFKA broker list: The list of brokers in the Kafka cluster. The broker list enables the Depot to fetch all the available topics in the Kafka cluster.
- Schema Registry URL

## Template

To create a Depot of type 'KAFKA', utilize the following template:

```yaml
name: {{depot-name}}
version: v1
type: depot
tags:
  - {{tag1}}
owner: {{owner-name}}
layer: user
depot:
  type: KAFKA                     
  description: {{description}}
  external: {{true}}
  spec:                           
    brokers:
      - {{broker1}}
      - {{broker2}}
    schemaRegistryUrl: {{http://20.9.63.231:8081/}}
```



>*Note*: The support for creating 'KAFKA' Depot using secrets in configuration is coming soon.
