# Scheduled or Cron Workflow

This documentation outlines a case scenario where data is read from Kafka depot and written to Icebase. To ensure continuous read/write operations, the metadata on Metis needs to be updated regularly. By scheduling the Toolbox workflow at a 5-minute interval, this requirement can be met effectively.

## Code Snippets

### **kafka-to-icebase.yaml**

```yaml
# Resource Section
version: v1beta1
name: kafka-to-icebase-02
type: workflow
description: From kafka to icebase
title: From kafka to icebase
# Workflow-specific Section
workflow:
  dag:
  # Job Specific Section
    - name: k-to-ice-02
      description: From kafka to icebase
      title: From kafka to icebase
      spec:
        stack: flare:3.0
        # Flare Stack-specific Section
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

### **datatool.yaml**

```yaml
# Resource Section
version: v1
name: dataos-tool-random-user
type: workflow
# Workflow-specific Section
workflow:
  # Schedule Section
  schedule:
    cron: '*/5 * * * *'
  dag:
  # Job-specific Section
    - name: dataos-tool-kafkastream
      spec:
        stack: toolbox
        compute: runnable-default
        # Toolbox-stack specific Section
        toolbox:
          dataset: dataos://icebase:kafka/random_users_icebase01?acl=rw
          action:
            name: set_version
            value: latest
```