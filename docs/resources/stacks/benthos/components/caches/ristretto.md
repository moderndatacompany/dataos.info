# ristretto

Tags: Ristretto

Stores key/value pairs in a map held in the memory-bound [Ristretto cache](https://github.com/dgraph-io/ristretto).

## YAML Configuration

### Common Config

```yaml
# Common config fields, showing default values
label: ""
ristretto:
  default_ttl: ""
```

This cache is more efficient and appropriate for high-volume use cases than the standard memory cache. However, the add command is non-atomic, and therefore this cache is not suitable for deduplication.

## Fields[](https://www.benthos.dev/docs/components/caches/ristretto#fields)

### `default_ttl`[](https://www.benthos.dev/docs/components/caches/ristretto#default_ttl)

A default TTL to set for items, calculated from the moment the item is cached. Set to an empty string or zero duration to disable TTLs.

**Type:** `string`

**Default:** `""`

```yaml
# Examples

default_ttl: 5m

default_ttl: 60s
```

---

### `get_retries`[](https://www.benthos.dev/docs/components/caches/ristretto#get_retries)

Determines how and whether get attempts should be retried if the key is not found. Ristretto is a concurrent cache that does not immediately reflect writes, and so it can sometimes be useful to enable retries at the cost of speed in cases where the key is expected to exist.

**Type:** `object`

---

### `get_retries.enabled`[](https://www.benthos.dev/docs/components/caches/ristretto#get_retriesenabled)

Whether retries should be enabled.

**Type:** `bool`

**Default:** `false`

---

### `get_retries.initial_interval`[](https://www.benthos.dev/docs/components/caches/ristretto#get_retriesinitial_interval)

The initial period to wait between retry attempts.

**Type:** `string`

**Default:** `"1s"`

```yaml
# Examples

initial_interval: 50ms

initial_interval: 1s
```

---

### `get_retries.max_interval`[](https://www.benthos.dev/docs/components/caches/ristretto#get_retriesmax_interval)

The maximum period to wait between retry attempts

**Type:** `string`

**Default:** `"5s"`

```yaml
# Examples

max_interval: 5s

max_interval: 1m
```

---

### `get_retries.max_elapsed_time`[](https://www.benthos.dev/docs/components/caches/ristretto#get_retriesmax_elapsed_time)

The maximum overall period of time to spend on retry attempts before the request is aborted.

**Type:** `string`

**Default:** `"30s"`

```yaml
# Examples

max_elapsed_time: 1m

max_elapsed_time: 1h
```