# redis

> 🗣 EXPERIMENTAL
This component is experimental and, therefore, subject to change or removal outside of major version releases.

A rate limit implementation using Redis. It works by using a simple token bucket algorithm to limit the number of requests to a given count within a given time period. The rate limit is shared across all instances of Bento that use the same Redis instance, which must all have a consistent count and interval.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
label: ""
redis:
  url: ""
  count: 1000
  interval: 1s
  key: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
label: ""
redis:
  url: ""
  kind: simple
  master: ""
  tls:
    enabled: false
    skip_cert_verify: false
    enable_renegotiation: false
    root_cas: ""
    root_cas_file: ""
    client_certs: []
  count: 1000
  interval: 1s
  key: ""
```

## Fields

### `url`

The URL of the target Redis server. Database is optional and is supplied as the URL path.

Type: `string`

```yaml
# Examples

url: :6397

url: localhost:6397

url: redis://localhost:6379

url: redis://:foopassword@redisplace:6379

url: redis://localhost:6379/1

url: redis://localhost:6379/1,redis://localhost:6380/1
```

---

### `kind`

Specifies a simple, cluster-aware, or failover-aware redis client.

Type: `string`

Default: `"simple"`

Options: `simple`, `cluster`, `failover`.

---

### `master`

Name of the redis master when `kind` is `failover`

Type: `string`

Default: `""`

```yaml
# Examples

master: mymaster
```

---

### `tls`

Custom TLS settings can be used to override system defaults.

Troubleshooting

Some cloud-hosted instances of Redis (such as Azure Cache) might need some hand-holding in order to establish stable connections. Unfortunately, it is often the case that TLS issues will manifest as generic error messages such as "i/o timeout". If you're using TLS and are seeing connectivity problems consider setting `enable_renegotiation` to `true` and ensuring that the server supports at least TLS version 1.2.

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

### `count`

The maximum number of messages to allow for a given period of time.

Type: `int`

Default: `1000`

---

### `interval`

The time window to limit requests by.

Type: `string`

Default: `"1s"`

---

### `key`

The key to use for the rate limit.

Type: `string`