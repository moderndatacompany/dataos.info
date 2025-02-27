# memcached

Tags: Memcached

Connects to a cluster of memcached services, a prefix can be specified to allow multiple cache types to share a memcached cluster under different namespaces.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
label: ""
memcached:
  addresses: []
  prefix: ""
  default_ttl: 300s
```

### Advanced Config

```yaml
# All config fields, showing default values
label: ""
memcached:
  addresses: []
  prefix: ""
  default_ttl: 300s
  retries:
    initial_interval: 1s
    max_interval: 5s
    max_elapsed_time: 30s
```

## Fields

### **`addresses`**

A list of addresses of memcached servers to use.

**Type:** `array`

---

### **`prefix`**

An optional string to prefix item keys with in order to prevent collisions with similar services.

**Type:** `string`

---

### **`default_ttl`**

A default TTL to set for items, calculated from the moment the item is cached.

**Type:** `string`

**Default:** `"300s"`

---

### **`retries`**

Determine time intervals and cut-offs for retry attempts.

**Type:** `object`

---

### **`retries.initial_interval`**

The initial period to wait between retry attempts.

**Type:** `string`

**Default:** `"1s"`

```yaml
# Examples

initial_interval: 50ms

initial_interval: 1s
```

---

### **`retries.max_interval`**

The maximum period to wait between retry attempts

**Type:** `string`

**Default:** `"5s"`

```yaml
# Examples

max_interval: 5s

max_interval: 1m
```

---

### **`retries.max_elapsed_time`**

The maximum overall period of time to spend on retry attempts before the request is aborted.

**Type:** `string`

**Default:** `"30s"`

```yaml
# Examples

max_elapsed_time: 1m

max_elapsed_time: 1h
```