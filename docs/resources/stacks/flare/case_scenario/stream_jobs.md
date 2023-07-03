# Stream Job


## Case Scenario

This case scenario describes the ingestion of stream data from Kafka Depot and saving it to file systems, databases, Iceberg, etc. To know more about a Stream Job click [here](../flare_job_types.md#stream-job)

To check out the various properties for the streaming section, click [here.](../flare_stack_yaml_configurations/streaming.md) 

## Implementation Flow

1. You need to define `checkpointlocation` to store the intermediate batches. The batched files are uploaded into a staging storage zone in DataOS, processed, and pushed into the main storage zone, batch by batch.
2. Save the YAML given below and adjusted the depot locations.
3. Apply the `config.yaml` from the CLI.
4. Once applied the data would start getting written to icebase, but it won’t showcase on the Metis.
5. As its stream data its metadata needs to be updated at regular intervals, so we would have to schedule the data tool job.
6. Define the cron within the data tool job and apply the `datatool.yaml` from CLI.

## Outcomes

The following Flare job saves data from Kafka to Iceberg tables.

## Code files

### **config.yaml**

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
                  kafka.sasl.jaas.config: org.apache.kafka.common.security.plain.PlainLoginModule required username="admin" password="0b9c4dd98ca9cc944160";
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

### **datatool.yaml**

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