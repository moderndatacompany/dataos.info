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

The section labeled as `inputs` consist of settings that enable the retrieval of data from diverse sources such as cloud buckets provided by popular cloud services providers like AWS, GCP, and Azure, APIs, and social media sites, including Twitter and Discord. These sources may be classified into categories such as Services, Networks, etc.

To access specific YAML configurations for each input source, users can refer to the accompanying database that lists the categories for each source. By clicking on the corresponding ‘OPEN’ button within the name section of the input source, a new popup window will appear displaying the relevant YAML configurations and description of each field.

[amqp_0_9](./amqp_0_9.md)

[amqp_1](./amqp_1.md)

[aws_kinesis](./aws_kinesis.md)

[aws_s3](./aws_s3.md)

[aws_sqs](./aws_sqs.md)

[azure_blob_storage](./azure_blob_storage.md)

[azure_queue_storage](./azure_queue_storage.md)

[azure_table_storage](./azure_table_storage.md)

[batched](./batched.md)

[beanstalkd](./beanstalkd.md)

[broker](./broker.md)

[cassandra](./cassandra.md)

[csv](./csv.md)

[discord](./discord.md)

[dynamic](./dynamic.md)

[file](./file.md)

[gcp_bigquery_select](./gcp_bigquery_select.md)

[gcp_cloud_storage](./gcp_cloud_storage.md)

[gcp_pubsub](./gcp_pubsub.md)

[generate](./generate.md)

[hdfs](./hdfs.md)

[http_client](./http_client.md)

[http_server](./http_server.md)

[inproc](./inproc.md)

[kafka](./kafka.md)

[kafka_franz](./kafka_franz.md)

[mongodb](./mongodb.md)

[nanomsg](./nanomsg.md)

[parquet](./parquet.md)

[pulsar](./pulsar.md)

[sftp](./sftp.md)

[socket](./socket.md)

[socket_server](./socket_server.md)

[stdin](./stdin.md)

[twitter_search](./twitter_search.md)

[mqtt](./mqtt.md)