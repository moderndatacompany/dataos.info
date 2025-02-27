# pulsar

> 🗣 EXPERIMENTAL
This component is experimental and, therefore, subject to change or removal outside of major version releases.


Reads messages from an Apache Pulsar server.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  pulsar:
    url: ""
    topics: []
    subscription_name: ""
    subscription_type: shared
    tls:
      root_cas_file: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  pulsar:
    url: ""
    topics: []
    subscription_name: ""
    subscription_type: shared
    tls:
      root_cas_file: ""
    auth:
      oauth2:
        enabled: false
        audience: ""
        issuer_url: ""
        private_key_file: ""
      token:
        enabled: false
        token: ""
```

## Metadata

This input adds the following metadata fields to each message:

```yaml
- pulsar_message_id
- pulsar_key
- pulsar_ordering_key
- pulsar_event_time_unix
- pulsar_publish_time_unix
- pulsar_topic
- pulsar_producer_name
- pulsar_redelivery_count
- All properties of the message
```

You can access these metadata fields using function interpolation.

## Fields

### `url`

A URL to connect to.

Type: `string`

```yaml
# Examples

url: pulsar://localhost:6650

url: pulsar://pulsar.us-west.example.com:6650

url: pulsar+ssl://pulsar.us-west.example.com:6651
```

---

### `topics`

A list of topics to subscribe to.

Type: `array`

---

### `subscription_name`

Specify the subscription name for this consumer.

Type: `string`

---

### `subscription_type`

Specify the subscription type for this consumer.

> NOTE: Using a key_shared subscription type will allow out-of-order delivery since nack-ing messages sets non-zero nack delivery delay - this can potentially cause consumers to stall. See Pulsar documentation and this Github issue for more details.
> 

Type: `string`

Default: `"shared"`

Options: `shared`, `key_shared`, `failover`, `exclusive`.

---

### `tls`

Specify the path to a custom CA certificate to trust broker TLS service.

Type: `object`

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

### `auth`

Optional configuration of Pulsar authentication methods.

Type: `object`

---

### `auth.oauth2`

Parameters for Pulsar OAuth2 authentication.

Type: `object`

---

### `auth.oauth2.enabled`

Whether OAuth2 is enabled.

Type: `bool`

Default: `false`

---

### `auth.oauth2.audience`

OAuth2 audience.

Type: `string`

Default: `""`

---

### `auth.oauth2.issuer_url`

OAuth2 issuer URL.

Type: `string`

Default: `""`

---

### `auth.oauth2.private_key_file`

The path to a file containing a private key.

Type: `string`

Default: `""`

---

### `auth.token`

Parameters for Pulsar Token authentication.

Type: `object`

---

### `auth.token.enabled`

Whether Token Auth is enabled.

Type: `bool`

Default: `false`

---

### `auth.token.token`

Actual base64 encoded token.

Type: `string`

Default: `""`