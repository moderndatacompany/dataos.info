# Inputs

An input is a source of data piped through an array of optional processors:

```yaml
input:
  label: my_redis_input

  redis_streams:
    url: tcp://localhost:6379
    streams:
      - benthos_stream
    body_key: body
    consumer_group: benthos_group

  # Optional list of processing steps
  processors:
   - mapping: |
       root.document = this.without("links")
       root.link_count = this.links.length()
```

Some inputs have a logical end, for example, a `csv` input ends once the last row is consumed, when this happens, the input gracefully terminates and Benthos will shut itself down once all messages have been processed fully.

It's also possible to specify a logical end for an input that otherwise doesn't have one with the `read_until` input, which checks a condition against each consumed message in order to determine whether it should be the last.

## Brokering[](https://www.benthos.dev/docs/components/inputs/about#brokering)

Only one input is configured at the root of a Benthos config. However, the root input can be a broker which combines multiple inputs and merges the streams:

```yaml
input:
  broker:
    inputs:
      - kafka:
          addresses: [ TODO ]
          topics: [ foo, bar ]
          consumer_group: foogroup

      - redis_streams:
          url: tcp://localhost:6379
          streams:
            - benthos_stream
          body_key: body
          consumer_group: benthos_group
```

## Labels[](https://www.benthos.dev/docs/components/inputs/about#labels)

Inputs have an optional field `label` that can uniquely identify them in observability data such as metrics and logs. This can be useful when running configs with multiple inputs, otherwise their metrics labels will be generated based on their composition. For more information check out the metrics documentation.

### Sequential Reads[](https://www.benthos.dev/docs/components/inputs/about#sequential-reads)

Sometimes it's useful to consume a sequence of inputs, where an input is only consumed once its predecessor is drained fully, you can achieve this with the `sequence` input.

## Generating Messages[](https://www.benthos.dev/docs/components/inputs/about#generating-messages)

It's possible to generate data with Benthos using the `generate` input, which is also a convenient way to trigger scheduled pipelines.

# Various Input Sources and Their Categories

The section labeled as **`inputs`** consist of settings that enable the retrieval of data from diverse sources such as cloud buckets provided by popular cloud services providers like AWS, GCP, and Azure, APIs, and social media sites, including Twitter and Discord. These sources may be classified into categories such as Services, Networks, etc.

To access specific YAML configurations for each input source, users can refer to the accompanying database that lists the categories for each source. By clicking on the corresponding ‘OPEN’ button within the name section of the input source, a new popup window will appear displaying the relevant YAML configurations and description of each field.


<center>

|Name|Category|
|---|---|
|[amqp_0_9](./inputs/amqp_0_9.md)|AMQP, Services|
|[amqp_1](./inputs/amqp_1.md)|AMQP, Services|
|[aws_kinesis](./inputs/aws_kinesis.md)|AWS, Services|
|[aws_s3](./inputs/aws_s3.md)|AWS, Services|
|[aws_sqs](./inputs/aws_sqs.md)|AWS, Services|
|[azure_blob_storage](./inputs/azure_blob_storage.md)|Azure, Services|
|[azure_queue_storage](./inputs/azure_queue_storage.md)|Azure, Services|
|[azure_table_storage](./inputs/azure_table_storage.md)|Azure, Services|
|[batched](./inputs/batched.md)|Utility|
|[beanstalkd](./inputs/beanstalkd.md)|Services|
|[broker](./inputs/broker.md)|Utility|
|[cassandra](./inputs/cassandra.md)|Services|
|[csv](./inputs/csv.md)|Local|
|[discord](./inputs/discord.md)|Services, Social|
|[dynamic](./inputs/dynamic.md)|Utility|
|[file](./inputs/file.md)|Local|
|[gcp_bigquery_select](./inputs/gcp_bigquery_select.md)|GCP, Services|
|[gcp_cloud_storage](./inputs/gcp_cloud_storage.md)|GCP, Services|
|[gcp_pubsub](./inputs/gcp_pubsub.md)|GCP, Services|
|[generate](./inputs/generate.md)|Utility|
|[hdfs](./inputs/hdfs.md)|Services|
|[http_client](./inputs/http_client.md)|Network|
|[http_server](./inputs/http_server.md)|Network|
|[inproc](./inputs/inproc.md)|Utility|
|[kafka](./inputs/kafka.md)|Services|
|[kafka_franz](./inputs/kafka_franz.md)|Services|
|[mongodb](./inputs/mongodb.md)|Services|
|[nanomsg](./inputs/nanomsg.md)|Network|
|[parquet](./inputs/parquet.md)|Local|
|[pulsar](./inputs/pulsar.md)|Services|
|[sftp](./inputs/sftp.md)|Network|
|[socket](./inputs/socket.md)|Network|
|[socket_server](./inputs/socket_server.md)|Network|
|[stdin](./inputs/stdin.md)|Local|
|[twitter_search](./inputs/twitter_search.md)|Services, Social|
|[mqtt](./inputs/mqtt.md)|Services|

</center>