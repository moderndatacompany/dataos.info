# azure_queue_storage

!!! warning "BETA"

      This component is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

Sends messages to an Azure Storage Queue. This processor was introduced in version 1.0.0. 


## YAML Configuration

### **Common Config**
```yaml
# Common config fields, showing default values

output:
  label: ""
  azure_queue_storage:
    storage_account: ""
    storage_access_key: ""
    storage_connection_string: ""
    storage_sas_token: ""
    queue_name: "" # No default (required)
    max_in_flight: 64
    batching:
      count: 0
      byte_size: 0
      period: ""
      jitter: 0
      check: ""
```



### **Full Config**

```yaml

# All config fields, showing default values
output:
  label: ""
  azure_queue_storage:
    storage_account: ""
    storage_access_key: ""
    storage_connection_string: ""
    storage_sas_token: ""
    queue_name: "" # No default (required)
    ttl: ""
    max_in_flight: 64
    batching:
      count: 0
      byte_size: 0
      period: ""
      jitter: 0
      check: ""
      processors: [] # No default (optional)


```


Only one authentication method is required, `storage_connection_string` or `storage_account` and `storage_access_key`. If both are set then the `storage_connection_string` is given priority.

In order to set the `queue_name` user can use function interpolations described [here](/resources/stacks/bento/configurations/interpolation/), which are calculated per message of a batch.

## Performance

This output benefits from sending multiple messages in flight in parallel for improved performance. You can tune the max number of in flight messages (or message batches) with the field `max_in_flight`.

This output benefits from sending messages as a batch for improved performance. Batches can be formed at both the input and output level. You can find out more in [this doc](/resources/stacks/bento/configurations/message_batching/).

## Fields

---


### **`storage_account`**

The storage account to access. This field is ignored if storage_connection_string is set.

Type: `string`

Default: `""`

---


### **`storage_access_key`**

The storage account access key. This field is ignored if storage_connection_string is set.

Type: `string`

Default: `""`

---


### **`storage_connection_string`**

A storage account connection string. This field is required if storage_account and `storage_access_key` / `storage_sas_token` are not set.

Type: `string`

Default: `""`

---


### **`storage_sas_token`**

The storage account SAS token. This field is ignored if `storage_connection_string` or `storage_access_key` are set.

Type: `string`

Default: `""`


---


### **`queue_name`**

The name of the target Queue Storage queue. This field supports interpolation functions.

Type: `string`

---


### **`ttl`**

The TTL of each individual message as a duration string. Defaults to 0, meaning no retention period is set This field supports interpolation functions.

Type: `string`
Default: `""`

```yaml
# Examples

ttl: 60s

ttl: 5m

ttl: 36h
```


---


### **`max_in_flight`**

The maximum number of parallel message batches to have in flight at any given time.

Type: `int`

Default: `64`

---


### **`batching`**

Allows you to configure a batching policy.

Type: `object`

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

batching:
  count: 10
  jitter: 0.1
  period: 10s
```

---


### **`batching.count`**

A number of messages at which the batch should be flushed. If 0 disables count based batching.

Type: `int`

Default: `0`

---


### **`batching.byte_size`**

An amount of bytes at which the batch should be flushed. If 0 disables size based batching.

Type: `int`

Default: `0`

---


### **`batching.period`**

A period in which an incomplete batch should be flushed regardless of its size.

Type: `string`

Default: `""`

```yaml
# Examples

period: 1s

period: 1m

period: 500ms
```

---


### **`batching.jitter`**

A non-negative factor that adds random delay to batch flush intervals, where delay is determined uniformly at random between 0 and jitter * period. For example, with period: 100ms and jitter: 0.1, each flush will be delayed by a random duration between 0-10ms.

Type: `float`

Default: `0`


```yaml
# Examples

jitter: 0.01

jitter: 0.1

jitter: 1
```


---


### **`batching.check`**

A Bloblang query that should return a boolean value indicating whether a message should end a batch.

Type: `string`
Default: `""`

```yaml
# Examples

check: this.type == "end_of_transaction"
```

---


### **`batching.processors`**

A list of processors to apply to a batch as it is flushed. This allows you to aggregate and archive the batch however you see fit. Please note that all resulting messages are flushed as a single batch, therefore splitting the batch into smaller batches using these processors is a no-op.

Type: `array`

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