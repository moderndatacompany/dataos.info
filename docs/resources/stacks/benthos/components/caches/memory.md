# memory

Tags: Memory

Stores key/value pairs in a map held in memory. This cache is, therefore, reset every time the service restarts. Each item in the cache has a TTL set from the moment it was last edited, after which it will be removed during the next compaction.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
label: ""
memory:
  default_ttl: 5m
  compaction_interval: 60s
  init_values: {}
```

### Advanced Config

```yaml
# All config fields, showing default values
label: ""
memory:
  default_ttl: 5m
  compaction_interval: 60s
  init_values: {}
  shards: 1
```

The compaction interval determines how often the cache is cleared of expired items, and this process is only triggered on writes to the cache. Access to the cache is blocked during this process.

Item expiry can be disabled entirely by setting the `compaction_interval` to an empty string.

The field `init_values` can be used to prepopulate the memory cache with any number of key/value pairs that are exempt from TTLs:

```yaml
cache_resources:
  - label: foocache
    memory:
      default_ttl: 60s
      init_values:
        foo: bar
```

These values can be overridden during execution, at which point the configured TTL is respected as usual.

## Fields[](https://www.benthos.dev/docs/components/caches/memory#fields)

### `default_ttl`[](https://www.benthos.dev/docs/components/caches/memory#default_ttl)

The default TTL of each item. After this period, an item will be eligible for removal during the next compaction.

**Type:** `string`

**Default:** `"5m"`

---

### `compaction_interval`[](https://www.benthos.dev/docs/components/caches/memory#compaction_interval)

The period of time to wait before each compaction, at which point expired items are removed. This field can be set to an empty string in order to disable compactions/expiry entirely.

**Type:** `string`

**Default:** `"60s"`

---

### `init_values`[](https://www.benthos.dev/docs/components/caches/memory#init_values)

A table of key/value pairs that should be present in the cache on initialization. This can be used to create static lookup tables.

**Type:** `object`

**Default:** `{}`

```yaml
# Examples

init_values:
  Nickelback: "1995"
  Spice Girls: "1994"
  The Human League: "1977"
```

---

### `shards`[](https://www.benthos.dev/docs/components/caches/memory#shards)

A number of logical shards to spread keys across, increasing the shards can have a performance benefit when processing a large number of keys.

**Type:** `int`

**Default:** `1`