# Kafka


DataOS allows you to create a Depot of type 'KAFKA' to read live topic data. This Depot enables you to access and consume real-time streaming data from Kafka.

## Requirements

To connect to Kafka, you need:

To establish a connection to Kafka, you need to provide the following information:

- KAFKA broker list: The list of brokers in the Kafka cluster. The broker list enables the Depot to fetch all the available topics in the Kafka cluster.

## Template

To create a Depot of type 'KAFKA', utilize the following template:

```yaml
version: v1
name: {{depot-name}}
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
```

<style>
    blockquote {
        background-color: #F6F3F8;
    }
</style>

<blockquote style="color: black;">

*Note*: The support for creating 'KAFKA' Depot using secrets in configuration is coming soon.
</blockquote>
