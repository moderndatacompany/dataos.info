# mqtt

Subscribe to topics on MQTT brokers.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  mqtt:
    urls: []
    topics: []
    client_id: ""
    connect_timeout: 30s
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  mqtt:
    urls: []
    topics: []
    client_id: ""
    dynamic_client_id_suffix: ""
    qos: 1
    clean_session: true
    will:
      enabled: false
      qos: 0
      retained: false
      topic: ""
      payload: ""
    connect_timeout: 30s
    user: ""
    password: ""
    keepalive: 30
    tls:
      enabled: false
      skip_cert_verify: false
      enable_renegotiation: false
      root_cas: ""
      root_cas_file: ""
      client_certs: []
```

### Metadata

This input adds the following metadata fields to each message:

```
- mqtt_duplicate
- mqtt_qos
- mqtt_retained
- mqtt_topic
- mqtt_message_id
```

You can access these metadata fields using function interpolation.

## Fields

### `urls`

A list of URLs to connect to. If an item of the list contains commas it will be expanded into multiple URLs.

Type: `array`

Default: `[]`

---

### `topics`

A list of topics to consume from.

Type: `array`

Default: `[]`

---

### `client_id`

An identifier for the client connection.

Type: `string`

Default: `""`

---

### `dynamic_client_id_suffix`

Append a dynamically generated suffix to the specified `client_id` on each run of the pipeline. This can be useful when clustering Bento producers.

Type: `string`

Default: `""`

| Option | Summary |
| --- | --- |
| Nanoid | Append a nanoid of length 21 characters |

---

### `qos`

The level of delivery guarantee to enforce.

Type: `int`

Default: `1`

Options: `0`, `1`, `2`.

---

### `clean_session`

Set whether the connection is non-persistent.

Type: `bool`

Default: `true`

---

### `will`

Set last will message in case of Bento failure

Type: `object`

---

### `will.enabled`

Whether to enable last-will messages.

Type: `bool`

Default: `false`

---

### `will.qos`

Set QoS for the last will message.

Type: `int`

Default: `0`

Options: `0`, `1`, `2`.

---

### `will.retained`

Set retained for last will message.

Type: `bool`

Default: `false`

---

### `will.topic`

Set topic for last will message.

Type: `string`

Default: `""`

---

### `will.payload`

Set payload for last will message.

Type: `string`

Default: `""`

---

### `connect_timeout`

The maximum amount of time to wait in order to establish a connection before the attempt is abandoned.

Type: `string`

Default: `"30s"`

```yaml
# Examples

connect_timeout: 1s

connect_timeout: 500ms
```

---

### `user`

A username to assume for the connection.

Type: `string`

Default: `""`

---

### `password`

A password to provide for the connection.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`

Default: `""`

---

### `keepalive`

Max seconds of inactivity before a keepalive message is sent.

Type: `int`

Default: `30`

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

### `tls.client_certs`

A list of client certificates to use. For each certificate either the fields `cert` and `key` or `cert_file` and `key_file` should be specified, but not both.

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