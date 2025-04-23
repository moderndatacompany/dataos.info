# Output

An output is a sink where we wish to send our consumed data after applying an optional array of processors. Only one output is configured at the root of a Bento config. However, the output can be a broker which combines multiple outputs under a chosen brokering pattern or a switch that is used to multiplex against different outputs. 

Bento outputs apply back pressure to components upstream. This means if your output target starts blocking traffic Bento will gracefully stop consuming until the issue is resolved.

An output config section looks like this:

```yaml
output:
  label: my_s3_output

  aws_s3:
    bucket: TODO
    path: '${! meta("kafka_topic") }/${! json("message.id") }.json'

  # Optional list of processing steps
  processors:
    - mapping: '{"message":this,"meta":{"link_count":this.links.length()}}'
```

### `label`

Outputs have an optional field `label` that can uniquely identify them in observability data such as metrics and logs. This can be useful when running configs with multiple outputs, otherwise, their metrics labels will be generated based on their composition.

## Various Output Sources and Their YAML Configurations

<div style="text-align: center;" markdown="1">

|Name|Category|
|---|---|
|[Fastbase Depot](/resources/stacks/bento/components/output/fastbase_depot/)|Depot, Pulsar|
|[kafka Depot](/resources/stacks/bento/components/output/kafka_depot/)|Depot, Kafka|
|[Kafka](/resources/stacks/bento/components/output/kafka/)|Kafka|
|[Pulsar](/resources/stacks/bento/components/output/pulsar/)|Pulsar|


</div>