# **Kafka**

# **Read Config**

**Input Section Configuration for Reading from Kafka Data Source**

```yaml

inputs: # Read from Kafka
  - name: city_connect
    inputType: kafka
    kafka:
      brokers: <ip>:<port> #e.g. locahost:6500
      topic: my-kafka-topic02
      schemaRegistryUrl: <protocol>://<ip>:<port> # e.g. http://localhost:6500
      isBatch: true
```

**Sample YAML for Reading from Kafka Data Source**

```yaml
version: v1
name: standalone-read-kafka
type: workflow
tags:
  - standalone
  - readJob
  - kafka
description: The job ingests city data from kafka to iceberg
workflow:
  title: Connect City
  dag:
    - name: city-kafka-read-01
      title: Sample Transaction Data Ingester
      description: The job ingests city data from kafka to iceberg
      spec:
        tags:
          - standalone
          - readJob
          - kafka
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from Kafka
              - name: city_connect
                inputType: kafka
                kafka:
                  brokers: <ip>:<port> #e.g. locahost:6500
                  topic: my-kafka-topic02
                  schemaRegistryUrl: <protocol>://<ip>:<port> # e.g. http://localhost:6500
                  isBatch: true

            outputs: # Write to Local System
              - name: finalDf
                outputType: file
                file:
                  format: iceberg
                  warehousePath: /data/examples/dataout/localKafka_01/
                  schemaName: default
                  tableName: trans_oms_data3
                  options:
                    saveMode: append

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect
```

# **Write Config**

**Output Section Configuration for Writing to Kafka Data Source**

```yaml
outputs:
  - name: city_connect
    outputType: kafka
    kafka:
      brokers: <ip>:<port> # e.g. localhost:6500
      topic: my-kafka-topic02
      schemaRegistryUrl: <protocol>://<ip>:<port> #e.g. http://localhost:6500
      options:
        format: avro
```

**Sample YAML for Writing to Kafka Data Source**

```yaml
version: v1
name: standalone-write-kafka
type: workflow
tags:
  - standalone
  - writeJob
  - kafka
description: The job ingests city data from file to kafka
workflow:
  title: Connect City
  dag:
    - name: standalone-kafka-write
      title: Sample Transaction Data Ingester
      description: The job ingests city data from file to kafka
      spec:
        tags:
          - standalone
          - writeJob
          - kafka
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from Local System
              - name: transactions_data
                inputType: file
                file:
                  path: /data/examples/default/transactions
                  format: json
                  isStream: false

            outputs: # Write to Kafka
              - name: city_connect
                outputType: kafka
                kafka:
                  brokers: <ip>:<port>
                  topic: my-kafka-topic02
                  schemaRegistryUrl: <protocol>://<ip>:<port>
                  options:
                    format: avro

            steps:
              - sequence:
                  - name: city_connect
                    sql: SELECT * FROM transactions_data
```