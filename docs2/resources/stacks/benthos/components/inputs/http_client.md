# http_client

Connects to a server and continuously performs requests for a single message.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  http_client:
    url: ""
    verb: GET
    headers: {}
    rate_limit: ""
    timeout: 5s
    payload: ""
    stream:
      enabled: false
      reconnect: true
      codec: lines
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  http_client:
    url: ""
    verb: GET
    headers: {}
    metadata:
      include_prefixes: []
      include_patterns: []
    dump_request_log_level: ""
    oauth:
      enabled: false
      consumer_key: ""
      consumer_secret: ""
      access_token: ""
      access_token_secret: ""
    oauth2:
      enabled: false
      client_key: ""
      client_secret: ""
      token_url: ""
      scopes: []
    basic_auth:
      enabled: false
      username: ""
      password: ""
    jwt:
      enabled: false
      private_key_file: ""
      signing_method: ""
      claims: {}
      headers: {}
    tls:
      enabled: false
      skip_cert_verify: false
      enable_renegotiation: false
      root_cas: ""
      root_cas_file: ""
      client_certs: []
    extract_headers:
      include_prefixes: []
      include_patterns: []
    rate_limit: ""
    timeout: 5s
    retry_period: 1s
    max_retry_backoff: 300s
    retries: 3
    backoff_on:
      - 429
    drop_on: []
    successful_on: []
    proxy_url: ""
    payload: ""
    drop_empty_bodies: true
    stream:
      enabled: false
      reconnect: true
      codec: lines
      max_buffer: 1000000
```

The URL and header values of this type can be dynamically set using function interpolations.

### Streaming

If you enable streaming, then Benthos will consume the body of the response as a continuous stream of data, breaking messages out following a chosen codec. This allows you to consume APIs that provide long-lived streamed data feeds (such as Twitter).

### Pagination

This input supports interpolation functions in the `url` and `headers` fields where data from the previous successfully consumed message (if there was one) can be referenced. This can be used in order to support basic levels of pagination. However, in cases where pagination depends on logic, it is recommended that you use an `http` processor instead, often combined with a `generate` input in order to schedule the processor.

## Examples

### Basic Pagination

Interpolation functions within the `url` and `headers` fields can be used to reference the previously consumed message, which allows simple pagination.

```yaml
input:
  http_client:
    url: >-
      https://api.example.com/search?query=allmyfoos&start_time=${! (
        (timestamp_unix()-300).ts_format("2006-01-02T15:04:05Z","UTC").escape_url_query()
      ) }${! ("&next_token="+this.meta.next_token.not_null()) | "" }
    verb: GET
    rate_limit: foo_searches
    oauth2:
      enabled: true
      token_url: https://api.example.com/oauth2/token
      client_key: "${EXAMPLE_KEY}"
      client_secret: "${EXAMPLE_SECRET}"

rate_limit_resources:
  - label: foo_searches
    local:
      count: 1
      interval: 30s
```

## Fields

### `url`

The URL to connect to. This field supports interpolation functions.

Type: `string`

---

### `verb`

A verb to connect with

Type: `string`

Default: `"GET"`

```yaml
# Examples

verb: POST

verb: GET

verb: DELETE
```

---

### `headers`

A map of headers to add to the request. This field supports interpolation functions.

Type: `object`

Default: `{}`

```yaml
# Examples

headers:
  Content-Type: application/octet-stream
  traceparent: ${! tracing_span().traceparent }
```

---

### `metadata`

Specify optional matching rules to determine which metadata keys should be added to the HTTP request as headers.

Type: `object`

---

### `metadata.include_prefixes`

Provide a list of explicit metadata key prefixes to match against.

Type: `array`
Default: `[]`

```yaml
# Examples

include_prefixes:
  - foo_
  - bar_

include_prefixes:
  - kafka_

include_prefixes:
  - content-
```

---

### `metadata.include_patterns`

Provide a list of explicit metadata key regular expression (re2) patterns to match against.

Type: `array`

Default: `[]`

```yaml
# Examples

include_patterns:
  - .*

include_patterns:
  - _timestamp_unix$
```

---

### `dump_request_log_level`

> 🗣 EXPERIMENTAL
Optionally set a level at which the request and response payload of each request made will be logged.

Type: `string`

Default: `""`

newerOptions: `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL`.

---

### `oauth`

Allows you to specify open authentication via OAuth version 1.

Type: `object`

---

### `oauth.enabled`

Whether to use OAuth version 1 in requests.

Type: `bool`

Default: `false`

---

### `oauth.consumer_key`

A value used to identify the client to the service provider.

Type: `string`

Default: `""`

---

### `oauth.consumer_secret`

A secret used to establish ownership of the consumer key.

SECRET

This field contains sensitive information that usually shouldn't be added to a config directly.

Type: `string`

Default: `""`

---

### `oauth.access_token`

A value used to gain access to the protected resources on behalf of the user.

Type: `string`

Default: `""`

---

### `oauth.access_token_secret`

A secret provided in order to establish ownership of a given access token.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly.


Type: `string`

Default: `""`

---

### `oauth2`

Allows you to specify open authentication via OAuth version 2 using the client credentials token flow.

Type: `object`

---

### `oauth2.enabled`

Whether to use OAuth version 2 in requests.

Type: `bool`

Default: `false`

---

### `oauth2.client_key`

A value used to identify the client to the token provider.

Type: `string`

Default: `""`

---

### `oauth2.client_secret`

A secret used to establish ownership of the client key.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly.

Type: `string`

Default: `""`

---

### `oauth2.token_url`

The URL of the token provider.

Type: `string`

Default: `""`

---

### `oauth2.scopes`

A list of optional requested permissions.

Type: `array`

---

### `basic_auth`

Allows you to specify basic authentication.

Type: `object`

---

### `basic_auth.enabled`

Whether to use basic authentication in requests.

Type: `bool`

Default: `false`

---

### `basic_auth.username`

A username to authenticate as.

Type: `string`

Default: `""`

---

### `basic_auth.password`

A password to authenticate with.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly.

Type: `string`

Default: `""`

---

### `jwt`

> 🗣 BETA
Allows you to specify JWT authentication.

Type: `object`

---

### `jwt.enabled`

Whether to use JWT authentication in requests.

Type: `bool`

Default: `false`

---

### `jwt.private_key_file`

A file with the PEM encoded via PKCS1 or PKCS8 as private key.

Type: `string`

Default: `""`

---

### `jwt.signing_method`

A method used to sign the token such as RS256, RS384, RS512, or EdDSA.

Type: `string`

Default: `""`

---

### `jwt.claims`

A value used to identify the claims that issued the JWT.

Type: `object`

---

### `jwt.headers`

Add optional key/value headers to the JWT.

Type: `object`

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
This field contains sensitive information that usually shouldn't be added to a config directly.

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
This field contains sensitive information that usually shouldn't be added to a config directly.

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
This field contains sensitive information that usually shouldn't be added to a config directly

Type: `string`

Default: `""`

```yaml
# Examples

password: foo

password: ${KEY_PASSWORD}
```

---

### `extract_headers`

Specify which response headers should be added to resulting messages as metadata. Header keys are lowercased before matching, so ensure that your patterns target lowercased versions of the header keys that you expect.

Type: `object`

---

### `extract_headers.include_prefixes`

Provide a list of explicit metadata key prefixes to match against.

Type: `array`

Default: `[]`

```yaml
# Examples

include_prefixes:
  - foo_
  - bar_

include_prefixes:
  - kafka_

include_prefixes:
  - content-
```

---

### `extract_headers.include_patterns`

Provide a list of explicit metadata key regular expression (re2) patterns to match against.

Type: `array`

Default: `[]`

```yaml
# Examples

include_patterns:
  - .*

include_patterns:
  - _timestamp_unix$
```

---

### `rate_limit`

An optional rate limit to throttle requests by.

Type: `string`

---

### `timeout`

A static timeout to apply to requests.

Type: `string`

Default: `"5s"`

---

### `retry_period`

The base period to wait between failed requests.

Type: `string`

Default: `"1s"`

---

### `max_retry_backoff`

The maximum period to wait between failed requests.

Type: `string`

Default: `"300s"`

---

### `retries`

The maximum number of retry attempts to make.

Type: `int`

Default: `3`

---

### `backoff_on`

A list of status codes whereby the request should be considered to have failed and retries should be attempted, but the period between them should be increased gradually.

Type: `array`

Default: `[429]`

---

### `drop_on`

A list of status codes whereby the request should be considered to have failed, but retries should not be attempted. This is useful for preventing wasted retries for requests that will never succeed. Note that with these status codes the *request* is dropped, but *message* that caused the request will not be dropped.

Type: `array`

Default: `[]`

---

### `successful_on`

A list of status codes whereby the attempt should be considered successful, this is useful for dropping requests that return non-2XX codes indicating that the message has been dealt with, such as a 303 See Other or a 409 Conflict. All 2XX codes are considered successful unless they are present within `backoff_on` or `drop_on`, regardless of this field.

Type: `array`

Default: `[]`

---

### `proxy_url`

An optional HTTP proxy URL.

Type: `string`

Default: `""`

---

### `payload`

An optional payload to deliver for each request. This field supports interpolation functions.

Type: `string`

---

### `drop_empty_bodies`

Whether empty payloads received from the target server should be dropped.

Type: `bool`

Default: `true`

---

### `stream`

Allows you to set streaming mode, where requests are kept open and messages are processed line-by-line.

Type: `object`

---

### `stream.enabled`

Enables streaming mode.

Type: `bool`

Default: `false`

---

### `stream.reconnect`

Sets whether to re-establish the connection once it is lost.

Type: `bool`

Default: `true`

---

### `stream.codec`

The way in which the bytes of a continuous stream are converted into messages. It's possible to consume lines using a custom delimiter with the `delim:x` codec, where x is the character sequence custom delimiter. It's not necessary to add gzip in the codec when the response headers specify it, as it will be decompressed automatically.

Type: `string`

Default: `"lines"`

| Option | Summary |
| --- | --- |
| auto | EXPERIMENTAL: Attempts to derive a codec for each file based on information such as the extension. For example, a .tar.gz file would be consumed with the gzip/tar codec. Defaults to all-bytes. |
| all-bytes | Consume the entire file as a single binary message. |
| avro-ocf:marshaler=x | EXPERIMENTAL: Consume a stream of Avro OCF datum. The marshaler parameter is optional and has the options: goavro (default), json. Use goavro if OCF contains logical types. |
| chunker:x | Consume the file in chunks of a given number of bytes. |
| csv | Consume structured rows as comma-separated-values, the first row must be a header row. |
| csv:x | Consume structured rows as values separated by a custom delimiter, the first row must be a header row. The custom delimiter must be a single character, e.g., the codec "csv:\t" would consume a tab-delimited file. |
| delim:x | Consume the file in segments divided by a custom delimiter. |
| gzip | Decompress a gzip file, this codec should precede another codec, e.g., gzip/all-bytes, gzip/tar, gzip/csv, etc. |
| lines | Consume the file in segments divided by linebreaks. |
| multipart | Consumes the output of another codec and batches messages together. A batch ends when an empty message is consumed. For example, the codec lines/multipart could be used to consume multipart messages where an empty line indicates the end of each batch. |
| regex:(?m)^\d\d:\d\d:\d\d | Consume the file in segments divided by regular expression. |
| tar | Parse the file as a tar archive, and consume each file of the archive as a message. |

```yaml
# Examples

codec: lines

codec: "delim:\t"

codec: delim:foobar

codec: csv
```

---

### `stream.max_buffer`

Must be larger than the largest line of the stream.

Type: `int`

Default: `1000000`