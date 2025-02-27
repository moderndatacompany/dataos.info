# kafka

The kafka output type writes a batch of messages to Kafka brokers and waits for acknowledgment before propagating it back to the input.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
output:
  label: ""
  kafka:
    addresses: []
    topic: ""
    target_version: 2.0.0
    key: ""
    partitioner: fnv1a_hash
    compression: none
    static_headers: {}
    metadata:
      exclude_prefixes: []
    max_in_flight: 64
    batching:
      count: 0
      byte_size: 0
      period: ""
      check: ""
```

The config field `ack_replicas` determines whether we wait for acknowledgment from all replicas or just a single broker.

Both the `key` and `topic` fields can be dynamically set using function interpolations described here.

Metadata will be added to each message sent as headers (version 0.11+) but can be restricted using the field [`metadata`](#metadata).

### Strict Ordering and Retries

When strict ordering is required for messages written to topic partitions, it is important to ensure that both the field `max_in_flight` is set to `1` and that the field `retry_as_batch` is set to `true`.

You must also ensure that failed batches are never rerouted back to the same output. This can be done by setting the field `max_retries` to `0` and `backoff.max_elapsed_time` to empty, which will apply back pressure indefinitely until the batch is sent successfully.

However, this also means that manual intervention will eventually be required in cases where the batch cannot be sent due to configuration problems such as an incorrect `max_msg_bytes` estimate. A less strict but automated alternative would be to route failed batches to a dead letter queue using a `fallback` broker, but this would allow subsequent batches to be delivered in the meantime whilst those failed batches are dealt with.

### Troubleshooting

If you're seeing issues writing to or reading from Kafka with this component, then it's worth trying out the newer `kafka_franz` output.

- I'm seeing logs that report `Failed to connect to kafka: kafka: client has run out of available brokers to talk to (Is your cluster reachable?)`, but the brokers are definitely reachable.

Unfortunately, this error message will appear for a wide range of connection problems even when the broker endpoint can be reached. Double-check your authentication configuration and also ensure that you have enabled TLS if applicable.

## Performance

This output benefits from sending multiple messages in flight in parallel for improved performance. You can tune the max number of in-flight messages (or message batches) with the field `max_in_flight`.

This output benefits from sending messages as a batch for improved performance. Batches can be formed at both the input and output levels. You can find out more in this doc.

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

An optional root certificate authority to use. This is a string representing a certificate chain from the parent trusted root certificate, to possible intermediate signing certificates, to the host certificate.

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

A list of client certificates to use. For each certificate, either the fields `cert` and `key` or  `cert_file` and `key_file` should be specified, but not both.

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

SECRET

This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`Default: `""`

### `tls.client_certs[].cert_file`

The path of a certificate to use.

Type: `string`Default: `""`

### `tls.client_certs[].key_file`

The path of a certificate key to use.

Type: `string`Default: `""`

### `tls.client_certs[].password`

A plain text password for when the private key is password encrypted in PKCS#1 or PKCS#8 format. The obsolete `pbeWithMD5AndDES-CBC` algorithm is not supported for the PKCS#8 format. Warning: Since it does not authenticate the ciphertext, it is vulnerable to padding oracle attacks that can let an attacker recover the plaintext.

SECRET

This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`Default: `""`

```
# Examples

password: foo

password: ${KEY_PASSWORD}

```

### `sasl`

Enables SASL authentication.

Type: `object`

### `sasl.mechanism`

The SASL authentication mechanism, if left empty SASL authentication is not used. Warning: SCRAM based methods within Benthos have not received a security audit.

Type: `string`Default: `"none"`

| Option | Summary |
| --- | --- |
| none | Default, no SASL authentication. |
| PLAIN | Plain text authentication. NOTE: When using plain text auth it is extremely likely that you'll also need to refer `tlsenabled`. |
| OAUTHBEARER | OAuth Bearer based authentication. |
| SCRAM-SHA-256 | Authentication using the SCRAM-SHA-256 mechanism. |
| SCRAM-SHA-512 | Authentication using the SCRAM-SHA-512 mechanism. |

### `sasl.user`

A PLAIN username. It is recommended that you use environment variables to populate this field.

Type: `string`Default: `""`

```
# Examples

user: ${USER}

```

### `sasl.password`

A PLAIN password. It is recommended that you use environment variables to populate this field.

SECRET

This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`Default: `""`

```
# Examples

password: ${PASSWORD}

```

### `sasl.access_token`

A static OAUTHBEARER access token

Type: `string`Default: `""`

### `sasl.token_cache`

Instead of using a static `access_token` allows you to query a cache resource to fetch OAUTHBEARER tokens from

Type: `string`Default: `""`

### `sasl.token_key`

Required when using a `token_cache`, the key to query the cache with for tokens.

Type: `string`Default: `""`

### `topic`

The topic to publish messages to. This field supports interpolation functions.

Type: `string`Default: `""`

### `client_id`

An identifier for the client connection.

Type: `string`Default: `"bento"`

### `target_version`

The version of the Kafka protocol to use. This limits the capabilities used by the client and should ideally match the version of your brokers.

Type: `string`Default: `"2.0.0"`

### `rack_id`

A rack identifier for this client.

Type: `string`Default: `""`

### `key`

The key to publish messages with. This field supports interpolation functions.

Type: `string`Default: `""`

### `partitioner`

The partitioning algorithm to use.

Type: `string`Default: `"fnv1a_hash"`Options: `fnv1a_hash`, `murmur2_hash`, `random`, `round_robin`, `manual`.

### `partition`

The manually-specified partition to publish messages to, relevant only when the field `partitioner` is set to `manual`. Must be able to parse as a 32-bit integer. This field supports interpolation functions.

Type: `string`Default: `""`

### `compression`

The compression algorithm to use.

Type: `string`Default: `"none"`Options: `none`, `snappy`, `lz4`, `gzip`, `zstd`.

### `static_headers`

An optional map of static headers that should be added to messages in addition to metadata.

Type: `object`Default: `{}`

```
# Examples

static_headers:
  first-static-header: value-1
  second-static-header: value-2

```

### `metadata`

Specify criteria for which metadata values are sent with messages as headers.

Type: `object`

### `metadata.exclude_prefixes`

Provide a list of explicit metadata key prefixes to be excluded when adding metadata to sent messages.

Type: `array`Default: `[]`

### `inject_tracing_map`

EXPERIMENTAL: A Bloblang mapping used to inject an object containing tracing propagation information into outbound messages. The specification of the injected fields will match the format used by the service wide tracer.

Type: `string`Default: `""`Requires version 3.45.0 or newer

```
# Examples

inject_tracing_map: meta = meta().merge(this)

inject_tracing_map: root.meta.span = this

```

### `max_in_flight`

The maximum number of parallel message batches to have in flight at any given time.

Type: `int`

Default: `64`

---

### `ack_replicas`

Ensure that messages have been copied across all replicas before acknowledging receipt.

Type: `bool`

Default: `false`

---

### `max_msg_bytes`

The maximum size in bytes of messages sent to the target topic.

Type: `int`

Default: `1000000`

---

### `timeout`

The maximum period of time to wait for message sends before abandoning the request and retrying.

Type: `string`

Default: `"5s"`

---

### `retry_as_batch`

When enabled forces an entire batch of messages to be retried if any individual message fails on a send, otherwise only the individual messages that failed are retried. Disabling this helps to reduce message duplicates during intermittent errors but also makes it impossible to guarantee strict ordering of messages.

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

```
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

```
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

---

### `max_retries`

The maximum number of retries before giving up on the request. If set to zero, there is no discrete limit.

Type: `int`

Default: `0`

---

### `backoff`

Control time intervals between retry attempts.

Type: `object`

---

### `backoff.initial_interval`

The initial period to wait between retry attempts.

Type: `string`

Default: `"3s"`

---

### `backoff.max_interval`

The maximum period to wait between retry attempts.

Type: `string`

Default: `"10s"`

---

### `backoff.max_elapsed_time`

The maximum period to wait before retry attempts are abandoned. If zero, then no limit is used.

Type: `string`

Default: `"30s"`