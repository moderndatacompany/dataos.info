# HTTP

When Bento runs, it kicks off an HTTP server that provides a few generally useful endpoints and is also where configured components such as the `http_server` input and output can register their own endpoints if they don't require their own host/port.

The configuration for this server lives under the `http` namespace, with the following default values:

## YAML Configurations

### Common Config

```yaml
# Common config fields showing default values

http:
  address: 0.0.0.0:4195
  enabled: true
  root_path: /bento
  debug_endpoints: false
```

### Advanced Config

```yaml
# All config fields showing default values

http:
  address: 0.0.0.0:4195
  enabled: true
  root_path: /bento
  debug_endpoints: false
  cert_file: ""
  key_file: ""
  cors:
    enabled: false
    allowed_origins: []
  basic_auth:
    enabled: false
    username: ""
    password_hash: ""
    algorithm: "sha256"
    salt: ""
```

The field `enabled` can be set to `false` in order to disable the server.

The field `root_path` specifies a general prefix for all endpoints, this can help isolate the service endpoints when using a reverse proxy with other shared services. All endpoints will still be registered at the root as well as behind the prefix, e.g. with a `root_path` set to `/foo` the endpoint `/version` will be accessible from both `/version` and `/foo/version`.

## Enabling HTTPS

By default, Bento will serve traffic over HTTP. In order to enforce TLS and serve traffic exclusively over HTTPS, you must provide a `cert_file` and `key_file` path in your config, which points to a file containing a certificate and a matching private key for the server, respectively.

If the certificate is signed by a certificate authority, the `cert_file` should be the concatenation of the server's certificate, any intermediates, and the CA's certificate.

## Enabling Basic Authentication

By default, Bento does not do any sort of authentication for the service-wide HTTP server. However, it's possible to configure basic authentication with the `basic_auth` field. Passwords configured must be hashed according to the specified algorithm and base64 encoded, for some hashing algorithms, you can do this using Bento itself:

```bash
echo mynewpassword | bento blobl 'root = content().hash("sha256").encode("base64")'
```

## Endpoints

The following endpoints will be generally available when the HTTP server is enabled:

- `/version` provides version info.
- `/ping` can be used as a liveness probe as it always returns a 200.
- `/ready` can be used as a readiness probe as it serves a 200 only when both the input and output are connected. Otherwise, a 503 is returned.
- `/metrics`, `/stats` both provide metrics when the metrics type is either `json_api` or `prometheus`.
- `/endpoints` provide a JSON object containing a list of available endpoints, including those registered by configured components.

## CORS

In order to serve Cross-Origin Resource Sharing headers, which instruct browsers to allow CORS requests, set the subfield `cors.enabled` to `true`.

### allowed_origins

A list of allowed origins to connect from. The literal value `*` can be specified as a wildcard. Note `cors.enabled` must be set to `true` for this list to take effect.

## Debug Endpoints

The field `debug_endpoints` when set to `true` prompts Bento to register a few extra endpoints that can be useful for debugging performance or behavioral problems:

- `/debug/config/json` returns the loaded config as JSON.
- `/debug/config/yaml` returns the loaded config as YAML.
- `/debug/pprof/block` responds with a pprof-formatted block profile.
- `/debug/pprof/heap` responds with a pprof-formatted heap profile.
- `/debug/pprof/mutex` responds with a pprof-formatted mutex profile.
- `/debug/pprof/profile` responds with a pprof-formatted cpu profile.
- `/debug/pprof/goroutine` responds with a pprof-formatted goroutine profile.
- `/debug/pprof/symbol` looks up the program counters listed in the request, responding with a table mapping program counters to function names.
- `/debug/pprof/trace` responds with the execution trace in binary form. Tracing lasts for duration specified in seconds GET parameter, or for 1 second if not specified.
- `/debug/stack` returns a snapshot of the current service stack trace.

## Fields

The schema of the `http` section is as follows:

### `enabled`

Whether to enable to HTTP server.

**Type:** `bool`

**Default:** `true`



### `address`

The address to bind to.

**Type:** `string`

**Default:** `"0.0.0.0:4195"`



### `root_path`

Specifies a general prefix for all endpoints, this can help isolate the service endpoints when using a reverse proxy with other shared services. All endpoints will still be registered at the root as well as behind the prefix, e.g. with a root_path set to `/foo` the endpoint `/version` will be accessible from both `/version` and `/foo/version`.

**Type:** `string`

**Default:** `"/bento"`



### `debug_endpoints`

Whether to register a few extra endpoints that can be useful for debugging performance or behavioral problems.

**Type:** `bool`

**Default:** `false`



### `cert_file`

An optional certificate file for enabling TLS.

**Type:** `string`

**Default:** `""`



### `key_file`

An optional key file for enabling TLS.

**Type:** `string`

**Default:** `""`



### `cors`

Adds Cross-Origin Resource Sharing headers.

**Type:** `object`



### `cors.enabled`

Whether to allow CORS requests.

**Type:** `bool`

**Default:** `false`



### `cors.allowed_origins`

An explicit list of origins that are allowed for CORS requests.

**Type:** list of `string`

**Default:** `[]`



### `basic_auth`

Allows you to enforce and customize basic authentication for requests to the HTTP server.

**Type:** `object`



### `basic_auth.enabled`

Enable basic authentication

**Type:** `bool`

**Default:** `false`



### `basic_auth.realm`

Custom realm name

**Type:** `string`

**Default:** `"restricted"`



### `basic_auth.username`

Username required to authenticate.

**Type:** `string`

**Default:** `""`



### `basic_auth.password_hash`

Hashed password required to authenticate. (base64 encoded)

**Type:** `string`

**Default:** `""`



### `basic_auth.algorithm`

Encryption algorithm used to generate `password_hash`.

**Type:** `string`

**Default:** `"sha256"`

```yaml
# Examples

algorithm: md5

algorithm: sha256

algorithm: bcrypt

algorithm: scrypt
```



### `basic_auth.salt`

Salt for scrypt algorithm. (base64 encoded)

**Type:** `string`

**Default:** `""`