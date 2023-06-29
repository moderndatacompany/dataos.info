# gcp_pubsub

Consumes messages from a GCP Cloud Pub/Sub subscription.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  gcp_pubsub:
    project: ""
    subscription: ""
    endpoint: ""
    sync: false
    max_outstanding_messages: 1000
    max_outstanding_bytes: 1000000000
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  gcp_pubsub:
    project: ""
    subscription: ""
    endpoint: ""
    sync: false
    max_outstanding_messages: 1000
    max_outstanding_bytes: 1000000000
    create_subscription:
      enabled: false
      topic: ""
```

For information on how to set up credentials, check out [this guide](https://cloud.google.com/docs/authentication/production).

### Metadata

This input adds the following metadata fields to each message:

```
- gcp_pubsub_publish_time_unix
- All message attributes
```

You can access these metadata fields using function interpolation.

## Fields

### `project`

The project ID of the target subscription.

Type: `string`

Default: `""`

---

### `subscription`

The target subscription ID.

Type: `string`

Default: `""`

---

### `endpoint`

An optional endpoint to override the default of `pubsub.googleapis.com:443`. This can be used to connect to a region-specific pub sub endpoint. For a list of valid values, check out [this document.](https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_regional_endpoints)

Type: `string`

Default: `""`

```yaml
# Examples

endpoint: us-central1-pubsub.googleapis.com:443

endpoint: us-west3-pubsub.googleapis.com:443
```

---

### `sync`

Enable synchronous pull mode.

Type: `bool`

Default: `false`

---

### `max_outstanding_messages`

The maximum number of outstanding pending messages to be consumed at a given time.

Type: `int`

Default: `1000`

---

### `max_outstanding_bytes`

The maximum number of outstanding pending messages to be consumed measured in bytes.

Type: `int`

Default: `1000000000`

---

### `create_subscription`

Allows you to configure the input subscription and creates if it doesn't exist.

Type: `object`

---

### `create_subscription.enabled`

Whether to configure a subscription or not.

Type: `bool`

Default: `false`

---

### `create_subscription.topic`

Defines the topic that the subscription should be vinculated to.

Type: `string`

Default: `""`