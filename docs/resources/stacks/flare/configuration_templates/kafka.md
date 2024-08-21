# Kafka Depots

To execute Flare Jobs on top of object storage depots, you first need to create a depot. If you have already created a depot, then continue reading else proceed to following link: [Kafka Depot](/resources/depot/depot_config_templates/kafka/)

To run a Flare Job all you need is the UDL address of the input or output dataset for the reading and writing scenarios respectively. Apart from this you also need the file `format` of the data and some additional properties

## Read Config

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

```yaml title="kafa_depot_read.yml"
--8<-- "examples/resources/stacks/flare/kafka_depot_read.yml"
```

## Write Config

For writing the data to a depot on an object store, we need to configure the `name`,  `dataset` and `format` properties in the `outputs` section of the YAML. For instance, if your dataset is to be stored at the UDL address is `dataos://kafka:default?acl=rw` by the name `output01` and the file format is KafkaJson. Then the inputs section will be as follows

```yaml
outputs:
  - name: output01
    depot: dataos://kafka:default?acl=rw
	checkpointLocation: dataos://icebase:sys01/checkpoints/ny_taxi/output01/nyt01?acl=rw
```

**Sample Write configuration YAML**

Let’s take a case scenario where the output dataset is to be stored a Kafka Depot and you have to read data from the Icebase depot within the DataOS The write config YAML will be as follows

```yaml title="kafa_depot_write.yml"
--8<-- "examples/resources/stacks/flare/kafka_depot_write.yml"
```