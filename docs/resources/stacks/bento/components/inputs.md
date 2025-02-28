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

## Brokering

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

## Labels

Inputs have an optional field `label` that can uniquely identify them in observability data such as metrics and logs. This can be useful when running configs with multiple inputs, otherwise their metrics labels will be generated based on their composition. For more information check out the metrics documentation.

### Sequential Reads

Sometimes it's useful to consume a sequence of inputs, where an input is only consumed once its predecessor is drained fully, you can achieve this with the `sequence` input.

## Generating Messages

It's possible to generate data with Benthos using the `generate` input, which is also a convenient way to trigger scheduled pipelines.

# Various Input Sources and Their Categories

The section labeled as **`inputs`** consist of settings that enable the retrieval of data from diverse sources such as cloud buckets provided by popular cloud services providers like AWS, GCP, and Azure, APIs, and social media sites, including Twitter and Discord. These sources may be classified into categories such as Services, Networks, etc.

To access specific YAML configurations for each input source, users can refer to the accompanying database that lists the categories for each source. By clicking on the corresponding ‘OPEN’ button within the name section of the input source, a new popup window will appear displaying the relevant YAML configurations and description of each field.


<center>

|Name|Category|
|---|---|
|[amqp_0_9](/resources/stacks/bento/components/inputs/amqp_0_9/)|AMQP, Services|
|[amqp_1](/resources/stacks/bento/components/inputs/amqp_1/)|AMQP, Services|
|[aws_kinesis](/resources/stacks/bento/components/inputs/aws_kinesis/)|AWS, Services|
|[aws_s3](/resources/stacks/bento/components/inputs/aws_s3/)|AWS, Services|
|[aws_sqs](/resources/stacks/bento/components/inputs/aws_sqs/)|AWS, Services|
|[azure_blob_storage](/resources/stacks/bento/components/inputs/azure_blob_storage/)|Azure, Services|
|[azure_queue_storage](/resources/stacks/bento/components/inputs/azure_queue_storage/)|Azure, Services|
|[azure_table_storage](/resources/stacks/bento/components/inputs/azure_table_storage/)|Azure, Services|
|[batched](/resources/stacks/bento/components/inputs/batched/)|Utility|
|[beanstalkd](/resources/stacks/bento/components/inputs/beanstalkd/)|Services|
|[broker](/resources/stacks/bento/components/inputs/broker/)|Utility|
|[cassandra](/resources/stacks/bento/components/inputs/cassandra/)|Services|
|[csv](/resources/stacks/bentoomponents/inputs/csv/)|Local|
|[discord](/resources/stacks/bento/components/inputs/discord/)|Services, Social|
|[dynamic](/resources/stacks/bento/components/inputs/dynamic/)|Utility|
|[file](/resources/stacks/bento/components/inputs/file/)|Local|
|[gcp_bigquery_select](/resources/stacks/bento/components/inputs/gcp_bigquery_select/)|GCP, Services|
|[gcp_cloud_storage](/resources/stacks/bento/components/inputs/gcp_cloud_storage/)|GCP, Services|
|[gcp_pubsub](/resources/stacks/bento/components/inputs/gcp_pubsub/)|GCP, Services|
|[generate](/resources/stacks/bento/components/inputs/generate/)|Utility|
|[hdfs](/resources/stacks/bento/components/inputs/hdfs/)|Services|
|[http_client](/resources/stacks/bento/components/inputs/http_client/)|Network|
|[http_server](/resources/stacks/bento/components/inputs/http_server/)|Network|
|[inproc](/resources/stacks/bento/components/inputs/inproc/)|Utility|
|[kafka](/resources/stacks/bento/components/inputs/kafka/)|Services|
|[kafka_franz](/resources/stacks/bento/components/inputs/kafka_franz/)|Services|
|[mongodb](/resources/stacks/bento/components/inputs/mongodb/)|Services|
|[nanomsg](/resources/stacks/bento/components/inputs/nanomsg/)|Network|
|[parquet](/resources/stacks/bento/components/inputs/parquet/)|Local|
|[pulsar](/resources/stacks/bento/components/inputs/pulsar/)|Services|
|[sftp](/resources/stacks/bento/components/inputs/sftp/)|Network|
|[socket](/resources/stacks/bento/components/inputs/socket/)|Network|
|[socket_server](/resources/stacks/bento/components/inputs/socket_server/)|Network|
|[stdin](/resources/stacks/bento/components/inputs/stdin/)|Local|
|[twitter_search](/resources/stacks/bento/components/inputs/twitter_search/)|Services, Social|
|[mqtt](/resources/stacks/bento/components/inputs/mqtt/)|Services|

</center>