# **Kafka Depots**

To execute Flare Jobs on top of object storage depots, you first need to create a depot. If you have already created a depot, then continue reading else proceed to below link.

To run a Flare Job all you need is the UDL address of the input or output dataset for the reading and writing scenarios respectively. Apart from this you also need the file `format` of the data and some additional properties

# **Read Config**

| Scenario | Syntax | Additional Properties |
| --- | --- | --- |
| Inputs (while readingfrom a depot) | `inputs:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `- name: <input-dataset-name>` <br>&nbsp;&nbsp;&nbsp;&nbsp; `dataset: <udl-address>` <br>&nbsp;&nbsp;&nbsp;&nbsp; `format: KafkaAvro` <br>&nbsp;&nbsp;&nbsp;&nbsp; `isStream: <boolean>` | startingOffsets: <br> `options:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `startingOffsets: earliest` <br>&nbsp;&nbsp;&nbsp;&nbsp; `kafka.sasl.jaas.config: org.apache.kafka.common.security.plain.PlainLoginModule` <br>&nbsp;&nbsp;&nbsp;&nbsp; `required username="admin" password="0b9c4dd98ca9cc944160";` <br>&nbsp;&nbsp;&nbsp;&nbsp; `kafka.sasl.mechanism: PLAIN  kafka.security.protocol: SASL_PLAINTEXT` |

For reading the data, we need to configure the `name`, `dataset`, and `format` properties in the `inputs` section of the YAML. Along with this there are some additional properties which are to be mentioned in the `options` section. For instance, if your dataset name is `sample_data`, UDL address is `dataos://kafka1:default/random_users_ktok03` and the file format is `KafkaAvro`. Then the inputs section will be as follows-

```yaml
inputs:
	- name: sample_data
		dataset: dataos://kafka1:default/random_users_ktok03
		format: KafkaAvro
		isStream: false
		options:
			startingOffsets: earliest
			kafka.sasl.jaas.config: org.apache.kafka.common.security.plain.PlainLoginModule required username="admin" password="0b9c4dd98ca9cc944160";
			kafka.sasl.mechanism: PLAIN
			kafka.security.protocol: SASL_PLAINTEXT
```

**Sample Read configuration YAML**

Let’s take a case scenario where the dataset is stored in Kafka Depot and you have to read it from the source, perform some transformation steps and write it to the Icebase which is a managed depot within the DataOS. The read config YAML will be as follows

```yaml
version: v1
name: read-kafka-01
type: workflow
tags:
  - read-kafka
description: this jobs reads data from kafka
workflow:
  dag:
    - name: sample-read-kafka-01
      title: read kafka sample data
      description: This job ingest cloudevent data
      spec:
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
              #triggerDuration: "20 seconds"
            inputs:
              - name: sample_data
                dataset: dataos://kafka1:default/random_users_ktok03
                format: KafkaAvro
                isStream: false
                options:
                  startingOffsets: earliest
                  kafka.sasl.jaas.config: org.apache.kafka.common.security.plain.PlainLoginModule required username="admin" password="0b9c4dd98ca9cc944160";
                  kafka.sasl.mechanism: PLAIN
                  kafka.security.protocol: SASL_PLAINTEXT
            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://icebase:sample_datasets/sample_dataset_kafkaavro?acl=rw
                format: Iceberg
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.metadata.previous-versions-max: "10"
                      history.expire.max-snapshot-age-ms: "7200000"
            steps:
              - sequence:
                - name: finalDf
                  sql: SELECT * FROM sample_data

    - name: dataos-tool-read-sample-dataset
      spec:
        stack: toolbox
      compute: runnable-default
        toolbox:
          dataset: dataos://icebase:sample_datasets/sample_dataset?acl=rw
          action:
            name: set_version
            value: latest
```

# **Write Config**

| Scenario | Syntax |
| --- | --- |
| Outputs (while writingto a depot) | `outputs:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `- name: <name-of-output>` <br>&nbsp;&nbsp;&nbsp;&nbsp; `dataset: dataos://[depot]:[collection]/[dataset]?acl=rw` <br> `checkpointLocation: <location-of-checkpoint>` |

For writing the data to a depot on an object store, we need to configure the `name`,  `dataset` and `format` properties in the `outputs` section of the YAML. For instance, if your dataset is to be stored at the UDL address is `dataos://kafka:default?acl=rw` by the name `output01` and the file format is KafkaJson. Then the inputs section will be as follows

```yaml
outputs:
	- name: output01
		depot: dataos://kafka:default?acl=rw
		checkpointLocation: dataos://icebase:sys01/checkpoints/ny_taxi/output01/nyt01?acl=rw
```

**Sample Write configuration YAML**

Let’s take a case scenario where the output dataset is to be stored a Kafka Depot and you have to read data from the Icebase depot within the DataOS The write config YAML will be as follows

```yaml
version: v1
name: write-kafka-2
type: workflow
tags:
  - NY-Taxi
description: The job ingests NY-Taxi data small files and conbined them to one file
workflow:
  dag:
    - name: kafka-json-write
      title: write in kafka from json
      description: write to kafka json file format
      spec:
        tags:
          - Connect
        stack: flare:3.0
        compute: runnable-default
        envs:
          ENABLE_TOPIC_CREATION: "true"
        flare:
          driver:
            coreLimit: 1200m
            cores: 1
            memory: 1024m
          executor:
            coreLimit: 1200m
            cores: 1
            instances: 1
            memory: 1024m
          job:
            explain: true
            inputs:
              - name: sample_data
                dataset: dataos://thirdparty01:sampledata/avro
                format: avro
                isStream: false
            logLevel: INFO
            outputs:
              - name: output01
                depot: dataos://kafka:default?acl=rw
                checkpointLocation: dataos://icebase:sys01/checkpoints/ny_taxi/output01/nyt01?acl=rw
								format: KafkaJson
            steps:
              - sequence: 
								- name: sample_data
									sql: SELECT * FROM avro
```