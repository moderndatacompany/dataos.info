# memory

Tags: In Memory

Stores consumed messages in memory and acknowledge them at the input level. During a shutdown, Benthos will make the best attempt at flushing all remaining messages before exiting cleanly.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
buffer:
  memory:
    limit: 524288000
    batch_policy:
      enabled: false
      count: 0
      byte_size: 0
      period: ""
      check: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
buffer:
  memory:
    limit: 524288000
    batch_policy:
      enabled: false
      count: 0
      byte_size: 0
      period: ""
      check: ""
      processors: []
```

This buffer is appropriate when consuming messages from inputs that do not gracefully handle back pressure and where delivery guarantees aren't critical.

This buffer has a configurable limit, where consumption will be stopped with back pressure upstream if the total size of messages in the buffer reaches this amount. Since this calculation is only an estimate, and the real size of messages in RAM is always higher, it is recommended to set the limit significantly below the amount of RAM available.

## Delivery Guarantees[](https://www.benthos.dev/docs/components/buffers/memory#delivery-guarantees)

This buffer intentionally weakens the delivery guarantees of the pipeline and, therefore, should never be used in places where data loss is unacceptable.

## Batching[](https://www.benthos.dev/docs/components/buffers/memory#batching)

It is possible to batch up messages sent from this buffer using a batch policy.

## Fields[](https://www.benthos.dev/docs/components/buffers/memory#fields)

### `limit`[](https://www.benthos.dev/docs/components/buffers/memory#limit)

The maximum buffer size (in bytes) to allow before applying backpressure upstream.

**Type:** `int`

**Default:** `524288000`

---

### `batch_policy`[](https://www.benthos.dev/docs/components/buffers/memory#batch_policy)

Optionally configure a policy to flush buffered messages in batches.

**Type:** `object`

---

### `batch_policy.enabled`[](https://www.benthos.dev/docs/components/buffers/memory#batch_policyenabled)

Whether to batch messages as they are flushed.

**Type:** `bool`

**Default:** `false`

---

### `batch_policy.count`[](https://www.benthos.dev/docs/components/buffers/memory#batch_policycount)

A number of messages at which the batch should be flushed. If `0` disables count-based batching.

**Type:** `int`

**Default:** `0`

---

### `batch_policy.byte_size`[](https://www.benthos.dev/docs/components/buffers/memory#batch_policybyte_size)

An amount of bytes at which the batch should be flushed. If `0` disables size-based batching.

**Type:** `int`

**Default:** `0`

---

### `batch_policy.period`[](https://www.benthos.dev/docs/components/buffers/memory#batch_policyperiod)

A period in which an incomplete batch should be flushed regardless of its size.

**Type:** `string`

**Default:** `""`

```yaml
# Examples

period: 1s

period: 1m

period: 500ms
```

---

### `batch_policy.check`[](https://www.benthos.dev/docs/components/buffers/memory#batch_policycheck)

A [Bloblang query](../../../benthos/bloblang.md) that should return a boolean value indicating whether a message should end a batch.

**Type:** `string`

**Default:** `""`

```yaml
# Examples

check: this.type == "end_of_transaction"
```

---

### `batch_policy.processors`[](https://www.benthos.dev/docs/components/buffers/memory#batch_policyprocessors)

A list of [processors](../../components/processors.md) to apply to a batch as it is flushed. This allows you to aggregate and archive the batch however you see fit. Please note that all resulting messages are flushed as a single batch, therefore splitting the batch into smaller batches using these processors is a no-op.

**Type:** `array`

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