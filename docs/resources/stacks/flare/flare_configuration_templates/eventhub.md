# Eventhub Depots

To execute Flare Jobs on top of EventHub depots, you first need to create a depot. If you have already created a depot, then continue reading else proceed to the below link

To run a Flare Job all you need is the UDL address of the input or output dataset for the reading and writing scenarios respectively. Apart from this you also need the file `format` of the data and some additional properties

## Read Config

For reading the data, we need to configure the `name`, `dataset`, and `format` properties in the `inputs` section of the YAML. Along with this there are some additional properties which are to be mentioned in the `options` section. Then the inputs section will be as follows-

```yaml
inputs:
	- name: input
		dataset: dataos://eventhub01:default/eventhub01
		options:
			eventhubs.consumergroup: "tmdc"
			eventhubs.startingposition: "{\"offset\":\"-1\",\"seqNo\":-1,\"enqueuedTime\":null,\"isInclusive\":true}"
		isStream: true
```

**Sample Read configuration YAML (for Batch)**

Let’s take a case scenario where the dataset is stored in Kafka Depot and you have to read it from the source, perform some transformation steps and write it to the Icebase which is a managed depot within the DataOS. The read config YAML will be as follows

```yaml
version: v1
name: read-eventhub-03
type: workflow
tags:
  - eventhub
  - read
description: this jobs reads data from eventhub and writes to icebase
workflow:
  dag:
    - name: eventhub-read-b-03
      title: read data from eventhub
      description: read data from eventhub
      spec:
        tags:
          - Connect
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: input
                dataset: dataos://eventhub01:default/eventhub01
                options:
                  "eventhubs.endingposition": "{\"offset\":\"@latest\",\"seqNo\":-1,\"enqueuedTime\":null,\"isInclusive\":false}"
                  "eventhubs.startingposition": "{\"offset\":\"-1\",\"seqNo\":-1,\"enqueuedTime\":null,\"isInclusive\":true}"
                  "eventhubs.consumergroup": "dataos"
                isStream: false
            logLevel: INFO
            outputs:
              - name: input
                dataset: dataos://icebase:sample/read_event_hub?acl=rw
                format: Iceberg
                options:
                  saveMode: append
	  - name: dataos-tool-eventhub
	    spec:
	      stack: toolbox
	      compute: runnable-default
	      toolbox:
	        dataset: dataos://icebase:sample/read_event_hub?acl=rw
	        action:
	          name: set_version
	          value: latest
```

**Sample Read configuration YAML (for Stream)**

Let’s take a case scenario where the dataset is stored in Kafka Depot and you have to read it from the source, perform some transformation steps and write it to the Icebase which is a managed depot within the DataOS. The read config YAML will be as follows

```yaml
version: v1
name: read-eventhub-stream-01
type: workflow
tags:
  - eventhub
  - read
description: this jobs reads data from eventhub and writes to icebase
workflow:
  dag:
    - name: eventhub-read-stream-01
      title: read data from eventhub
      description: read data from eventhub
      spec:
        tags:
          - Connect
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            streaming:
#                forEachBatchMode
              checkpointLocation: /tmp/checkpoints/devd01
              forEachBatchMode: false
            inputs:
              - name: input
                dataset: dataos://eventhub01:default/eventhub01
                options:
                  eventhubs.consumergroup: "tmdc"
                  eventhubs.startingposition: "{\"offset\":\"-1\",\"seqNo\":-1,\"enqueuedTime\":null,\"isInclusive\":true}"
                isStream: true
            logLevel: INFO
            outputs:
              - name: input
                dataset: dataos://icebase:sample/city_eventhub_stream_01?acl=rw
                format: Iceberg
                options:
                  saveMode: append
	  - name: dataos-tool-eventhub
	    spec:
	      stack: toolbox
	      compute: runnable-default
	      toolbox:
	        dataset: dataos://icebase:sample/city_eventhub_stream_01?acl=rw
	        action:
	          name: set_version
	          value: latest
```

# Write Config

For writing the data to a depot on an object store, we need to configure the `name`,  `dataset` and `format` properties in the `outputs` section of the YAML. For instance, if your dataset is to be stored at the UDL address is `dataos://kafka:default?acl=rw` by the name `output01` and the file format is KafkaJson. Then the inputs section will be as follows

```yaml
outputs:
	- name: finalDf
		dataset: dataos://eventhub01:default/eventhub01?acl=rw
		format: EventHub
```

**Sample Write configuration YAML**

Let’s take a case scenario where the output dataset is to be stored a Kafka Depot and you have to read data from the Icebase depot within the DataOS The write config YAML will be as follows

```yaml
version: v1
name: write-eventhub-b-03
type: workflow
tags:
  - eventhub
  - write
description: this jobs reads data from thirdparty and writes to eventhub
workflow:
  dag:
    - name: eventhub-write-b-03
      title: write data to eventhub
      description: write data to eventhub
      spec:
        tags:
          - Connect
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            streaming:
              checkpointLocation: /tmp/checkpoints/devd01
              forEachBatchMode: "true"
            inputs:
              - name: input
                dataset: dataos://thirdparty01:none/city
                format: csv
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc

            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://eventhub01:default/eventhub01?acl=rw
                format: EventHub

            steps:
              - sequence:
                - name: finalDf
                  sql: SELECT * FROM input
```