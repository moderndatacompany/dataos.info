# azure_queue_storage

Category: Azure, Services

<aside>
🗣 <b> BETA </b>

This component is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

</aside>

Dequeue objects from an Azure Storage Queue.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  azure_queue_storage:
    storage_account: ""
    storage_access_key: ""
    storage_sas_token: ""
    storage_connection_string: ""
    queue_name: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  azure_queue_storage:
    storage_account: ""
    storage_access_key: ""
    storage_sas_token: ""
    storage_connection_string: ""
    queue_name: ""
    dequeue_visibility_timeout: 30s
    max_in_flight: 10
    track_properties: false
```

Dequeue objects from an Azure Storage Queue.

This input adds the following metadata fields to each message:

```
- queue_storage_insertion_time
- queue_storage_queue_name
- queue_storage_message_lag (if 'track_properties' set to true)
- All user defined queue metadata
```

Only one authentication method is required,  `storage_connection_string`  or  `storage_account` and `storage_access_key`. If both are set, then the `storage_connection_string` is given priority.

## Fields

### `storage_account`

The storage account to dequeue messages from. This field is ignored if  `storage_connection_string` is set.

**Type:** `string`

**Default:** `""`

---

### `storage_access_key`

The storage account access key. This field is ignored if `storage_connection_string` is set.

**Type:** `string`

**Default:** `""`

---

### `storage_sas_token`

The storage account SAS token. This field is ignored if  `storage_connection_string`  or  `storage_access_key` are set.

**Type:** `string`

**Default:** `""`

---

### `storage_connection_string`

A storage account connection string. This field is required if  `storage_account`  and  `storage_access_key` / `storage_sas_token` are not set.

**Type:** `string`

**Default:** `""`

---

### `queue_name`

The name of the source storage queue. This field supports [function interpolation](../../configurations/interpolation.md).

**Type:** `string`

**Default:** `""`

```yaml
# Examples

queue_name: foo_queue

queue_name: ${! env("MESSAGE_TYPE").lowercase() }
```

---

### `dequeue_visibility_timeout`

The timeout duration until a dequeued message gets visible again, 30s by default.

**Type:** `string`

**Default:** `"30s"`

---

### `max_in_flight`

The maximum number of unprocessed messages to fetch at a given time.

**Type:** `int`

**Default:** `10`

---

### `track_properties`

If set to `true` the queue is polled on each read request for information such as the queue message lag. These properties are added to consumed messages as metadata but will also have a negative performance impact.

**Type:** `bool`

**Default:** `false`