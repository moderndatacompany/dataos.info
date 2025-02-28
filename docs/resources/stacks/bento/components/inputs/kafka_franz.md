# kafka_franz

> 🗣 BETA
This component is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

An alternative Kafka input using the [Franz Kafka client library](https://github.com/twmb/franz-go).

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  kafka_franz:
    seed_brokers: []
    topics: []
    regexp_topics: false
    consumer_group: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  kafka_franz:
    seed_brokers: []
    topics: []
    regexp_topics: false
    consumer_group: ""
    checkpoint_limit: 1024
    commit_period: 5s
    start_from_oldest: true
    tls:
      enabled: false
      skip_cert_verify: false
      enable_renegotiation: false
      root_cas: ""
      root_cas_file: ""
      client_certs: []
    sasl: []
    multi_header: false
```

Consumes one or more topics by balancing the partitions across any other connected clients with the same consumer group.

### Metadata

This input adds the following metadata fields to each message:

```
- kafka_key
- kafka_topic
- kafka_partition
- kafka_offset
- kafka_timestamp_unix
- All record headers
```

## Fields

### `seed_brokers`

A list of broker addresses to connect to in order to establish connections. If an item of the list contains commas, it will be expanded into multiple addresses.

Type: `array`

```yaml
# Examples

seed_brokers:
  - localhost:9092

seed_brokers:
  - foo:9092
  - bar:9092

seed_brokers:
  - foo:9092,bar:9092
```

---

### `topics`

A list of topics to consume from, partitions are automatically shared across consumers sharing the consumer group.

Type: `array`

---

### `regexp_topics`

Whether listed topics should be interpretted as regular expression patterns for matching multiple topics.

Type: `bool`

Default: `false`

---

### `consumer_group`

A consumer group to consume as. Partitions are automatically distributed across consumers sharing a consumer group, and partition offsets are automatically committed and resumed under this name.

Type: `string`

---

### `checkpoint_limit`

Determines how many messages of the same partition can be processed in parallel before applying back pressure. When a message of a given offset is delivered to the output, the offset is only allowed to be committed when all messages of prior offsets have also been delivered, this ensures at-least-once delivery guarantees. However, this mechanism also increases the likelihood of duplicates in the event of crashes or server faults, reducing the checkpoint limit will mitigate this.

Type: `int`

Default: `1024`

---

### `commit_period`

The period of time between each commit of the current partition offsets. Offsets are always committed during the shutdown.

Type: `string`

Default: `"5s"`

---

### `start_from_oldest`

If an offset is not found for a topic partition, determines whether to consume from the oldest available offset; otherwise, messages are consumed from the latest offset.

Type: `bool`

Default: `true`

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

### `tls.root_cas_file`

An optional path of a root certificate authority file to use. This is a file, often with a .pem extension, containing a certificate chain from the parent trusted root certificate, to possible intermediate signing certificates, to the host certificate.

Type: `string`

Default: `""`

```yaml
# Examples

root_cas_file: ./root_cas.pem
```

### `tls.client_certs`

A list of client certificates to use. For each certificate, either the fields `cert` and `key`, or `cert_file` and `key_file` should be specified, but not both.

Type: `array`

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

Specify one or more methods of SASL authentication. SASL is tried in order; if the broker supports the first mechanism, all connections will use that mechanism. If the first mechanism fails, the client will pick the first supported mechanism. If the broker does not support any client mechanisms, connections will fail.

Type: `array`

```yaml
# Examples

sasl:
  - mechanism: SCRAM-SHA-512
    password: bar
    username: foo
```

---

### `sasl

The SASL mechanism to use.

Type: `string`

| Option | Summary |
| --- | --- |
| AWS_MSK_IAM | AWS IAM based authentication as specified by the 'aws-msk-iam-auth' java library. |
| OAUTHBEARER | OAuth Bearer based authentication. |
| PLAIN | Plain text authentication. |
| SCRAM-SHA-256 | SCRAM based authentication as specified in RFC5802. |
| SCRAM-SHA-512 | SCRAM based authentication as specified in RFC5802. |
| none | Disable sasl authentication |

---

### `sasl[].username`

A username to provide for PLAIN or SCRAM-* authentication.

Type: `string`

Default: `""`

---

### `sasl[].password`

A password to provide for PLAIN or SCRAM-* authentication.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`

Default: `""`

---

### `sasl[].token`

The token to use for a single session's OAUTHBEARER authentication.

Type: `string`

Default: `""`

---

### `sasl[].extensions`

Key/value pairs to add to OAUTHBEARER authentication requests.

Type: `object`

---

### `sasl[].aws`

Contains AWS-specific fields for when the `mechanism` is set to `AWS_MSK_IAM`.

Type: `object`

---

### `sasl[].aws.region`

The AWS region to target.

Type: `string`

Default: `""`

---

### `sasl[].aws.endpoint`

Allows you to specify a custom endpoint for the AWS API.

Type: `string`

Default: `""`

---

### `sasl[].aws.credentials`

Optional manual configuration of AWS credentials to use. More information can be found in this document.

Type: `object`

---

### `sasl[].aws.credentials.profile`

A profile from `~/.aws/credentials` to use.

Type: `string`

Default: `""`

---

### `sasl[].aws.credentials.id`

The ID of credentials to use.

Type: `string`

Default: `""`

---

### `sasl[].aws.credentials.secret`

The secret for the credentials being used.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`

Default: `""`

---

### `sasl[].aws.credentials.token`

The token for the credentials being used, required when using short-term credentials.

Type: `string`

Default: `""`

---

### `sasl[].aws.credentials.from_ec2_role`

Use the credentials of a host EC2 machine configured to assume [an IAM role associated with the instance](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).

Type: `bool`

Default: `false`

---

### `sasl[].aws.credentials.role`

A role ARN to assume.

Type: `string`

Default: `""`

---

### `sasl[].aws.credentials.role_external_id`

An external ID to provide when assuming a role.

Type: `string`

Default: `""`

---

### `multi_header`

Decode headers into lists to allow handling of multiple values with the same key

Type: `bool`

Default: `false`