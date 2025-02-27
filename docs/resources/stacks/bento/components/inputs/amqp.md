# amqp_0_9

Category: AMQP, Services

Connects to an AMQP (0.91) queue. AMQP is a messaging protocol used by various message brokers, including RabbitMQ.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  amqp_0_9:
    urls: []
    queue: ""
    consumer_tag: ""
    prefetch_count: 10
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  amqp_0_9:
    urls: []
    queue: ""
    queue_declare:
      enabled: false
      durable: true
      auto_delete: false
    bindings_declare: []
    consumer_tag: ""
    auto_ack: false
    nack_reject_patterns: []
    prefetch_count: 10
    prefetch_size: 0
    tls:
      enabled: false
      skip_cert_verify: false
      enable_renegotiation: false
      root_cas: ""
      root_cas_file: ""
      client_certs: []
```

TLS is automatic when connecting to an `amqps` URL, but custom settings can be enabled in the `tls` section.

### **Metadata**

This input adds the following metadata fields to each message:

```
- amqp_content_type
- amqp_content_encoding
- amqp_delivery_mode
- amqp_priority
- amqp_correlation_id
- amqp_reply_to
- amqp_expiration
- amqp_message_id
- amqp_timestamp
- amqp_type
- amqp_user_id
- amqp_app_id
- amqp_consumer_tag
- amqp_delivery_tag
- amqp_redelivered
- amqp_exchange
- amqp_routing_key
- All existing message headers, including nested headers prefixed with the key of their respective parent.
```

You can access these metadata fields using [function interpolation](../../configurations/interpolation.md).

## Fields

### `urls`

A list of URLs to connect to. The first URL to successfully establish a connection will be used until the connection is closed. If an item of the list contains commas, it will be expanded into multiple URLs.

**Type:** `array`

**Default:** `[]`

```yaml
# Examples

urls:
  - amqp://guest:guest@127.0.0.1:5672/

urls:
  - amqp://127.0.0.1:5672/,amqp://127.0.0.2:5672/

urls:
  - amqp://127.0.0.1:5672/
  - amqp://127.0.0.2:5672/
```


**Type:** `string`

**Default:** `""`

```yaml
# Examples

root_cas: |-
  -----BEGIN CERTIFICATE-----
  ...
  -----END CERTIFICATE----
```


**Type:** `string`

**Default:** `""`


**Type:** `string`

**Default:** `""`

```yaml
# Examples

password: foo

password: ${KEY_PASSWORD}
```