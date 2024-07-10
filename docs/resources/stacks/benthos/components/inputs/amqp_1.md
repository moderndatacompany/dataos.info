# amqp_1

Reads messages from an AMQP (1.0) server.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  amqp_1:
    url: ""
    source_address: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  amqp_1:
    url: ""
    source_address: ""
    azure_renew_lock: false
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
```

### Metadata

This input adds the following metadata fields to each message:

```
- amqp_content_type
- amqp_content_encoding
- amqp_creation_time
- All string-typed message annotations
```

You can access these metadata fields using [function interpolation](../../configurations/interpolation.md).

## Fields

### `url`

A URL to connect to.

Type: `string`

Default: `""`

```yaml
# Examples

url: amqp://localhost:5672/

url: amqps://guest:guest@localhost:5672/
```

---

### `source_address`

The source address to consume from.

Type: `string`

Default: `""`

```yaml
# Examples

source_address: /foo

source_address: queue:/bar

source_address: topic:/baz
```

---

### `azure_renew_lock`

Experimental: Azure service bus-specific option to renew lock if processing takes more than configured lock time.

Type: `bool`

Default: `false`

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

### `sasl`

Enables SASL authentication.

Type: `object`

---

### `sasl.mechanism`

The SASL authentication mechanism to use.

Type: `string`

Default: `"none"`

| Option | Summary |
| --- | --- |
| none | No SASL based authentication. |
| plain | Plain text SASL authentication. |

---

### `sasl.user`

A SASL plain text username. It is recommended that you use environment variables to populate this field.

Type: `string`

Default: `""`

```yaml
# Examples

user: ${USER}
```

### `sasl.password`

A SASL plain text password. It is recommended that you use environment variables to populate this field.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.

Type: `string`

Default: `""`

```yaml
# Examples

password: ${PASSWORD}
```