# kafka

Connects to Kafka brokers and consumes one or more topics.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  kafka:
    addresses: []
    topics: []
    target_version: 2.0.0
    consumer_group: ""
    checkpoint_limit: 1024
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  kafka:
    addresses: []
    topics: []
    target_version: 2.0.0
    tls:
      enabled: false
      skip_cert_verify: false
      enable_renegotiation: false
      root_cas: ""
      root_cas_file: ""
      client_certs: []
    sasl:
      mechanism: none
      user: ""
      password: ""
      access_token: ""
      token_cache: ""
      token_key: ""
    consumer_group: ""
    client_id: bento
    rack_id: ""
    start_from_oldest: true
    checkpoint_limit: 1024
    commit_period: 1s
    max_processing_period: 100ms
    extract_tracing_map: ""
    group:
      session_timeout: 10s
      heartbeat_interval: 3s
      rebalance_timeout: 60s
    fetch_buffer_cap: 256
    multi_header: false
    batching:
      count: 0
      byte_size: 0
      period: ""
      check: ""
      processors: []
```

Offsets are managed within Kafka under the specified consumer group, and partitions for each topic are automatically balanced across members of the consumer group.

The Kafka input allows parallel processing of messages from different topic partitions, but by default, messages of the same topic partition are processed in lockstep in order to enforce ordered processing. This protection often means that batching messages at the output level can stall, in which case it can be tuned by increasing the field `checkpoint_limit`, ideally to a value greater than the number of messages you expect to batch.

Alternatively, if you perform batching at the input level using the `batching` field, it is done per partition and therefore avoids stalling.

### Metadata

This input adds the following metadata fields to each message:

```
- kafka_key
- kafka_topic
- kafka_partition
- kafka_offset
- kafka_lag
- kafka_timestamp_unix
- All existing message headers (version 0.11+)
```

The field `kafka_lag` is the calculated difference between the high watermark offset of the partition at the time of ingestion and the current message offset.

You can access these metadata fields using function interpolation.

### Ordering

By default, messages of a topic partition can be processed in parallel up to a limit determined by the field `checkpoint_limit`. However, if strict ordered processing is required, then this value must be set to 1 in order to process shard messages in lock-step. When doing so, it is recommended that you perform batching at this component for performance, as it will not be possible to batch lock-stepped messages at the output level.

### Troubleshooting

If you're seeing issues writing to or reading from Kafka with this component, then it's worth trying out the newer `kafka_franz` input.

- I'm seeing logs that report `Failed to connect to kafka: kafka: client has run out of available brokers to talk to (Is your cluster reachable?)`, but the brokers are definitely reachable.

Unfortunately, this error message will appear for a wide range of connection problems even when the broker endpoint can be reached. Double-check your authentication configuration and also ensure that you have enabled TLS if applicable.

## Fields

### `addresses`

A list of broker addresses to connect to. If an item of the list contains commas, it will be expanded into multiple addresses.

Type: `array`

Default: `[]`

```yaml
# Examples

addresses:
  - localhost:9092

addresses:
  - localhost:9041,localhost:9042

addresses:
  - localhost:9041
  - localhost:9042
```

---

### `topics`

A list of topics to consume from. Multiple comma-separated topics can be listed in a single element. Partitions are automatically distributed across consumers of a topic. Alternatively, it's possible to specify explicit partitions to consume from with a colon after the topic name, e.g., `foo:0` would consume partition 0 of the topic foo. This syntax supports ranges, e.g., `foo:0-10` would consume partitions 0 through to 10 inclusive.

Type: `array`

Default: `[]`

```yaml
# Examples

topics:
  - foo
  - bar

topics:
  - foo,bar

topics:
  - foo:0
  - bar:1
  - bar:3

topics:
  - foo:0,bar:1,bar:3

topics:
  - foo:0-5
```

---

### `target_version`

The version of the Kafka protocol to use. This limits the capabilities used by the client and should ideally match the version of your brokers.

Type: `string`

Default: `"2.0.0"`

---

### `tls`

Custom TLS settings can be used to override system defaults.

Type: `object`

---

### `tls.enabled`

Whether custom TLS settings are enabled.

Type: `bool`

Default: `false`

---

### `tls.skip_cert_verify`

Whether to skip server-side certificate verification.

Type: `bool`

Default: `false`

---

### `tls.enable_renegotiation`

Whether to allow the remote server to repeatedly request renegotiation. Enable this option if you're seeing the error message `local error: tls: no renegotiation`.

Type: `bool`

Default: `false`

---

### `tls.root_cas`

An optional root certificate authority to use. This is a string, representing a certificate chain from the parent trusted root certificate, to possible intermediate signing certificates, to the host certificate.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`

Default: `""`

```yaml
# Examples

root_cas: |-
  -----BEGIN CERTIFICATE-----
  ...
  -----END CERTIFICATE-----
```

---

### `tls.root_cas_file`

An optional path of a root certificate authority file to use. This is a file, often with a .pem extension, containing a certificate chain from the parent trusted root certificate, to possible intermediate signing certificates, to the host certificate.

Type: `string`

Default: `""`

```yaml
# Examples

root_cas_file: ./root_cas.pem
```

---

### `tls.client_certs`

A list of client certificates to use. For each certificate, either the fields `cert` and `key` or `cert_file` and `key_file` should be specified, but not both.

Type: `array`

Default: `[]`

```yaml
# Examples

client_certs:
  - cert: foo
    key: bar

client_certs:
  - cert_file: ./example.pem
    key_file: ./example.key
```

---

### `tls.client_certs[].cert`

A plain text certificate to use.

Type: `string`

Default: `""`

---

### `tls.client_certs[].key`

A plain text certificate key to use.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`

Default: `""`

---

### `tls.client_certs[].cert_file`

The path of a certificate to use.

Type: `string`

Default: `""`

---

### `tls.client_certs[].key_file`

The path of a certificate key to use.

Type: `string`

Default: `""`

---

### `tls.client_certs[].password`

A plain text password for when the private key is password encrypted in PKCS#1 or PKCS#8 format. The obsolete `pbeWithMD5AndDES-CBC` algorithm is not supported for the PKCS#8 format. Warning: Since it does not authenticate the ciphertext, it is vulnerable to padding oracle attacks that can let an attacker recover the plaintext.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`

Default: `""`

```yaml
# Examples

password: foo

password: ${KEY_PASSWORD}
```

---

### `sasl`

Enables SASL authentication.

Type: `object`

---

### `sasl.mechanism`

The SASL authentication mechanism, if left empty SASL authentication is not used. Warning: SCRAM-based methods within Bento have not received a security audit.

Type: `string`

Default: `"none"`

| Option | Summary |
| --- | --- |
| none | Default, no SASL authentication. |
| PLAIN | Plain text authentication. NOTE: When using plain text auth it is extremely likely that you'll also need to enable TLS. |
| OAUTHBEARER | OAuth Bearer-based authentication. |
| SCRAM-SHA-256 | Authentication using the SCRAM-SHA-256 mechanism. |
| SCRAM-SHA-512 | Authentication using the SCRAM-SHA-512 mechanism. |

---


### `sasl.user`

A PLAIN username. It is recommended that you use environment variables to populate this field.

Type: `string`

Default: `""`

```yaml
# Examples

user: ${USER}
```

---

### `sasl.password`

A PLAIN password. It is recommended that you use environment variables to populate this field.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`

Default: `""`

```yaml
# Examples

password: ${PASSWORD}
```

---

### `sasl.access_token`

A static OAUTHBEARER access token

Type: `string`

Default: `""`

---

### `sasl.token_cache`

Instead of using a static `access_token` allows you to query a `cache` resource to fetch OAUTHBEARER tokens from

Type: `string`

Default: `""`

---

### `sasl.token_key`

Required when using a `token_cache`, the key to query the cache with for tokens.

Type: `string`

Default: `""`

---

### `consumer_group`

An identifier for the consumer group of the connection. This field can be explicitly made empty in order to disable stored offsets for the consumed topic partitions.

Type: `string`

Default: `""`

---

### `client_id`

An identifier for the client connection.

Type: `string`

Default: `"bento"`

---

### `rack_id`

A rack identifier for this client.

Type: `string`

Default: `""`

---

### `start_from_oldest`

If an offset is not found for a topic partition, determines whether to consume from the oldest available offset; otherwise, messages are consumed from the latest offset.

Type: `bool`

Default: `true`

---

### `checkpoint_limit`

The maximum number of messages of the same topic and partition that can be processed at a given time. Increasing this limit enables parallel processing and batching at the output level to work on individual partitions. Any given offset will not be committed unless all messages under that offset are delivered in order to preserve at least once delivery guarantees.

Type: `int`

Default: `1024`

---

### `commit_period`

The period of time between each commit of the current partition offsets. Offsets are always committed during shutdown.

Type: `string`

Default: `"1s"`

---

### `max_processing_period`

A maximum estimate for the time taken to process a message, this is used for tuning consumer group synchronization.

Type: `string`

Default: `"100ms"`

---

### `extract_tracing_map`

> 🗣 EXPERIMENTAL
A Bloblang mapping that attempts to extract an object containing tracing propagation information, which will then be used as the root tracing span for the message. The specification of the extracted fields must match the format used by the service-wide tracer.

Type: `string`

Default: `""`

```yaml
# Examples

extract_tracing_map: root = meta()

extract_tracing_map: root = this.meta.span
```

---

### `group`

Tuning parameters for consumer group synchronization.

Type: `object`

---

### `group.session_timeout`

A period after which a consumer of the group is kicked after no heartbeats.

Type: `string`

Default: `"10s"`

---

### `group.heartbeat_interval`

A period in which heartbeats should be sent out.

Type: `string`

Default: `"3s"`

---

### `group.rebalance_timeout`

A period after which rebalancing is abandoned if unresolved.

Type: `string`

Default: `"60s"`

---

### `fetch_buffer_cap`

The maximum number of unprocessed messages to fetch at a given time.

Type: `int`

Default: `256`

---

### `multi_header`

Decode headers into lists to allow the handling of multiple values with the same key

Type: `bool`

Default: `false`

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

---

### `batching.processors`

A list of processors to apply to a batch as it is flushed. This allows you to aggregate and archive the batch however you see fit. Please note that all resulting messages are flushed as a single batch, therefore splitting the batch into smaller batches using these processors is a no-op.

Type: `array`

Default: `[]`

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