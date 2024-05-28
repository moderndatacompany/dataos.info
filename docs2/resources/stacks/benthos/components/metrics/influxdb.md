# influxdb

> 🗣 BETA
This component is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

Send metrics to InfluxDB 1.x using the `/write` endpoint.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
metrics:
  influxdb:
    url: ""
    db: ""
  mapping: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
metrics:
  influxdb:
    url: ""
    db: ""
    tls:
      enabled: false
      skip_cert_verify: false
      enable_renegotiation: false
      root_cas: ""
      root_cas_file: ""
      client_certs: []
    username: ""
    password: ""
    include:
      runtime: ""
      debug_gc: ""
    interval: 1m
    ping_interval: 20s
    precision: s
    timeout: 5s
    tags: {}
    retention_policy: ""
    write_consistency: ""
  mapping: ""
```

Refer to this [link](https://docs.influxdata.com/influxdb/v1.8/tools/api/#write-http-endpoint) for further details on the write API.

## Fields

### `url`

A URL of the format `[https|http|udp]://host:port` to the InfluxDB host.

Type: `string`

Default: `""`

---

### `db`

The name of the database to use.

Type: `string`

Default: `""`

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

### `username`

A username (when applicable).

Type: `string`

Default: `""`

---

### `password`

A password (when applicable).

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`

Default: `""`

---

### `include`

Optional additional metrics to collect, enabling these metrics may have some performance implications as it acquires a global semaphore and does `stoptheworld()`.

Type: `object`

---

### `include.runtime`

A duration string indicating how often to poll and collect runtime metrics. Leave empty to disable this metric

Type: `string`

Default: `""`

```yaml
# Examples

runtime: 1m
```

---

### `include.debug_gc`

A duration string indicating how often to poll and collect GC metrics. Leave empty to disable this metric.

Type: `string`

Default: `""`

```yaml
# Examples

debug_gc: 1m
```

---

### `interval`

A duration string indicating how often metrics should be flushed.

Type: `string`

Default: `"1m"`

---

### `ping_interval`

A duration string indicating how often to ping the host.

Type: `string`

Default: `"20s"`

---

### `precision`

[ns|us|ms|s] timestamp precision passed to write api.

Type: `string`

Default: `"s"`

---

### `timeout`

How long to wait for response for both ping and writing metrics.

Type: `string`

Default: `"5s"`

---

### `tags`

Global tags added to each metric.

Type: `object`

Default: `{}`

```yaml
# Examples

tags:
  hostname: localhost
  zone: danger
```

---

### `retention_policy`

Sets the retention policy for each write.

Type: `string`

Default: `""`

---

### `write_consistency`

[any|one|quorum|all] sets write consistency when available.

Type: `string`

Default: `""`