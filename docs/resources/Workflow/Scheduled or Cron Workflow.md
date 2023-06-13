# Scheduled or Cron Workflow

# Case Scenario

Let’s take a case scenario, where we read data from Kafka depot and write it to the Icebase. Since this would be a continuous read/write we will have to update the metadata on the Metis continuously. So we will have schedule the toolbox workflow in the datatool.yaml at an interval of 5 minutes.

# Implementation Flow

1. Save the below code snippets into separate YAML files.
2. Get the username and password for the `kafka.sasl.jaas.config` property.
3. To schedule the toolbox workflow at an interval of 5 minutes, you would be required to provide the cron expression. In case you don’t know how to define the cron expression, navigate to the below [link](https://en.wikipedia.org/wiki/Cron)
4. First Apply the `kafka-to-icebase.yaml` from the CLI.
5. Then apply the `datatool.yaml` command from the CLI.

# Outcome

When you apply the `datatool.yaml` workflow at a frequency of 5 minutes. The metadata of ingested data gets updated in Metis after every 5 minutes.

# Code Snippets

### kafka-to-icebase.yaml

```yaml
version: v1beta1
name: kafka-to-icebase-02
type: workflow
description: From kafka to icebase
title: From kafka to icebase
workflow:
  dag:
    - name: k-to-ice-02
      description: From kafka to icebase
      title: From kafka to icebase
      spec:
        stack: flare:3.0
        flare:
          job:
            explain: true

            streaming:
              checkpointLocation: dataos://icebase:checkpoints/kafka-to-icebase/random-users/fygsfhb?acl=rw
              triggerMode: ProcessingTime
              triggerDuration: 10 seconds
              forEachBatchMode: false # Only one view can be wwritten

            inputs:
              - name: random_user
                dataset: dataos://kafka1:default/kafka_test01
                isStream: true
                options:
                  startingOffsets: latest
                  kafka.sasl.jaas.config: org.apache.kafka.common.security.plain.PlainLoginModule required username="<user>" password="<password>";
                  kafka.sasl.mechanism: PLAIN
                  kafka.security.protocol: SASL_PLAINTEXT

            logLevel: INFO

            outputs:
              - name: extracted_columns
                dataset: dataos://icebase:kafka/random_users_icebase01?acl=rw
                outputType: Iceberg
                title: Random Users Enriched Data Kafka
                options:
                  saveMode: append
                  extraOptions:
                    fanout-enabled: "true"
                    triggerDuration: "20 seconds"

            steps:
              - sequence:
                - name: extracted_values
                  sql: select cast(value as string) data from random_user
                  functions:
                    - name: parse_as_json
                      column: data
                      asColumn: data_parsed
                      sparkSchema: "{\"type\":\"struct\",\"fields\":[{\"name\":\"age\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"city\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"country\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"email\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"first_name\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"gender\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"last_name\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"phone\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"postcode\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"state\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"title\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}}]}"

                - name: extracted_columns
                  sql: select data_parsed.* from extracted_values
                  functions:
                    - name: drop
                      columns:
                        - __metadata
```

### datatool.yaml

```yaml
version: v1
name: dataos-tool-random-user
type: workflow
workflow:
  schedule:
    cron: '*/5 * * * *'
  dag:
    - name: dataos-tool-kafkastream
      spec:
        stack: toolbox
        compute: runnable-default
        toolbox:
          dataset: dataos://icebase:kafka/random_users_icebase01?acl=rw
          action:
            name: set_version
            value: latest
```

Table of Contents