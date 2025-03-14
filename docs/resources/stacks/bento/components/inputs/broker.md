# broker

Allows you to combine multiple inputs into a single stream of data, where each input will be read in parallel.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  broker:
    inputs: []
    batching:
      count: 0
      byte_size: 0
      period: ""
      check: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  broker:
    copies: 1
    inputs: []
    batching:
      count: 0
      byte_size: 0
      period: ""
      check: ""
      processors: []
```

A broker type is configured with its own list of input configurations and a field to specify how many copies of the list of inputs should be created.

Adding more input types allows you to combine streams from multiple sources into one. For example, reading from both RabbitMQ and Kafka:

```yaml
input:
  broker:
    copies: 1
    inputs:
      - amqp_0_9:
          urls:
            - amqp://guest:guest@localhost:5672/
          consumer_tag: bento-consumer
          queue: bento-queue

        # Optional list of input specific processing steps
        processors:
          - mapping: |
              root.message = this
              root.meta.link_count = this.links.length()
              root.user.age = this.user.age.number()

      - kafka:
          addresses:
            - localhost:9092
          client_id: bento_kafka_input
          consumer_group: bento_consumer_group
          topics: [ bento_stream:0 ]
```

If the number of copies is greater than zero, the list will be copied that number of times. For example, if your inputs were of type foo and bar, with 'copies' set to '2', you would end up with two 'foo' inputs and two 'bar' inputs.

### Batching

It's possible to configure a batch policy with a broker using the `batching` fields. When doing this, the feeds from all child inputs are combined. Some inputs do not support broker-based batching and specify this in their documentation.

### Processors

It is possible to configure [processors](../../components/processors.md) at the broker level, where they will be applied to *all* child inputs, as well as on the individual child inputs. If you have processors at both the broker level *and* on child inputs, then the broker processors will be applied *after* the child nodes processors.

## Fields

### `copies`

Whatever is specified within `inputs` will be created this many times.

Type: `int`

Default: `1`

---

### `inputs`

A list of inputs to create.

Type: `array`

Default: `[]`

---

### `batching`

Allows you to configure a batching policy.

Type: `object`

```yaml
# Examples

batching:
  byte_size: 5000
  count: 0
  period: 1s

batching:
  count: 10
  period: 1s

batching:
  check: this.contains("END BATCH")
  count: 0
  period: 1m
```

---

### `batching.count`

A number of messages at which the batch should be flushed. If `0` disables count-based batching.

Type: `int`

Default: `0`

---

### `batching.byte_size`

An amount of bytes at which the batch should be flushed. If `0` disables size-based batching.

Type: `int`

Default: `0`

---

### `batching.period`

A period in which an incomplete batch should be flushed regardless of its size.

Type: `string`

Default: `""`

```yaml
# Examples

period: 1s

period: 1m

period: 500ms
```

---

### `batching.check`

A Bloblang query that should return a boolean value indicating whether a message should end a batch.

Type: `string`

Default: `""`

```yaml
# Examples

check: this.type == "end_of_transaction"
```

### `batching.processors`

A list of [processors](../../components/processors.md) to apply to a batch as it is flushed. This allows you to aggregate and archive the batch however you see fit. Please note that all resulting messages are flushed as a single batch, therefore splitting the batch into smaller batches using these processors is a no-op.

Type: `array`

```yaml
# Examples

processors:
  - archive:
      format: concatenate

processors:
  - archive:
      format: lines

processors:
  - archive:
      format: json_array
```