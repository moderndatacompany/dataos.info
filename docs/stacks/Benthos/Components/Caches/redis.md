# redis

Use a Redis instance as a cache. The expiration can be set to zero or an empty string in order to set no expiration.

## YAML Configuration

### Common Config

```yaml
# Common config fields, showing default values
label: ""
redis:
  url: ""
  prefix: ""
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

### `prefix`

An optional string to prefix item keys with in order to prevent collisions with similar services.

Type: `string`

---

### `default_ttl`

An optional default TTL to set for items, calculated from the moment the item is cached.

Type: `string`

---

### `retries`

Determine time intervals and cut-offs for retry attempts.

Type: `object`

---

### `retries.initial_interval`

The initial period to wait between retry attempts.

Type: `string`

Default: `"500ms"`

```yaml
# Examples

initial_interval: 50ms

initial_interval: 1s
```

---

### `retries.max_interval`

The maximum period to wait between retry attempts

Type: `string`

Default: `"1s"`

```yaml
# Examples

max_interval: 5s

max_interval: 1m
```

---

### `retries.max_elapsed_time`

The maximum overall period of time to spend on retry attempts before the request is aborted.

Type: `string`

Default: `"5s"`

```yaml
# Examples

max_elapsed_time: 1m

max_elapsed_time: 1h
```