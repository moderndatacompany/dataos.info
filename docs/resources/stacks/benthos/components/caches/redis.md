# redis

Tags: Redis

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

## Fields[](https://www.benthos.dev/docs/components/caches/redis#fields)

### `url`[](https://www.benthos.dev/docs/components/caches/redis#url)

The URL of the target Redis server. Database is optional and is supplied as the URL path.

**Type:** `string`

```yaml
# Examples

url: :6397

url: localhost:6397

url: redis://localhost:6379

url: redis://:foopassword@redisplace:6379

url: redis://localhost:6379/1

url: redis://localhost:6379/1,redis://localhost:6380/1
```


**Type:** `string`

**Default:** `""`

```yaml
# Examples

root_cas: |-
  -----BEGIN CERTIFICATE-----
  ...
  -----END CERTIFICATE-----
```


**Type:** `string`

**Default:** `""`


**Type:** `string`

**Default:** `""`

```yaml
# Examples

password: foo

password: ${KEY_PASSWORD}
```

### `**prefix**`

An optional string to prefix item keys with in order to prevent collisions with similar services.

**Type:** `string`

---

### `default_ttl`[](https://www.benthos.dev/docs/components/caches/redis#default_ttl)

An optional default TTL to set for items, calculated from the moment the item is cached.

**Type:** `string`

---

### `retries`[](https://www.benthos.dev/docs/components/caches/redis#retries)

Determine time intervals and cut-offs for retry attempts.

**Type:** `object`

---

### `retries.initial_interval`[](https://www.benthos.dev/docs/components/caches/redis#retriesinitial_interval)

The initial period to wait between retry attempts.

**Type:** `string`

**Default:** `"500ms"`

```yaml
# Examples

initial_interval: 50ms

initial_interval: 1s
```

---

### `retries.max_interval`[](https://www.benthos.dev/docs/components/caches/redis#retriesmax_interval)

The maximum period to wait between retry attempts

**Type:** `string`

**Default:** `"1s"`

```yaml
# Examples

max_interval: 5s

max_interval: 1m
```

---

### `retries.max_elapsed_time`[](https://www.benthos.dev/docs/components/caches/redis#retriesmax_elapsed_time)

The maximum overall period of time to spend on retry attempts before the request is aborted.

**Type:** `string`

**Default:** `"5s"`

```yaml
# Examples

max_elapsed_time: 1m

max_elapsed_time: 1h
```