# couchbase

Tags: Couchbase

<aside>
🗣 **EXPERIMENTAL**

This component is experimental and, therefore, subject to change or removal outside of major version releases.

</aside>

Use a Couchbase instance as a cache.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
label: ""
couchbase:
  url: ""
  username: ""
  password: ""
  bucket: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
label: ""
couchbase:
  url: ""
  username: ""
  password: ""
  bucket: ""
  collection: _default
  transcoder: legacy
  timeout: 15s
  default_ttl: ""
```

## Fields

### **`url`**

Couchbase connection string.

**Type:** `string`

```yaml
# Examples

url: couchbase://localhost:11210
```


**Type:** `string`

---

### **`bucket`**

Couchbase bucket.

**Type:** `string`

---

### **`collection`**

Bucket collection.

**Type:** `string`

**Default:** `"_default"`

---

### **`transcoder`**

Couchbase transcoder to use.

**Type:** `string`

**Default:** `"legacy"`

| Option | Summary |
| --- | --- |
| **json** | JSONTranscoder implements the default transcoding behavior and applies JSON transcoding to all values. This will apply the following behavior to the value: binary ([]byte) -> error. default -> JSON value, JSON Flags. |
| **legacy** | LegacyTranscoder implements the behaviour for a backward-compatible transcoder. This transcoder implements behaviour matching that of gocb v1.This will apply the following behavior to the value: binary ([]byte) -> binary bytes, Binary expectedFlags. string -> string bytes, String expectedFlags. default -> JSON value, JSON expectedFlags. |
| **raw** | RawBinaryTranscoder implements passthrough behavior of raw binary data. This transcoder does not apply any serialization. This will apply the following behavior to the value: binary ([]byte) -> binary bytes, binary expectedFlags. default -> error. |
| **rawjson** | RawJSONTranscoder implements passthrough behavior of JSON data. This transcoder does not apply any serialization. It will forward data across the network without incurring unnecessary parsing costs. This will apply the following behavior to the value: binary ([]byte) -> JSON bytes, JSON expectedFlags. string -> JSON bytes, JSON expectedFlags. default -> error. |
| **rawstring** | RawStringTranscoder implements passthrough behavior of raw string data. This transcoder does not apply any serialization. This will apply the following behavior to the value: string -> string bytes, string expectedFlags. default -> error. |

---

### **`timeout`**

Operation timeout.

**Type:** `string`

**Default:** `"15s"`

---

### **`default_ttl`**

An optional default TTL to set for items, calculated from the moment the item is cached.

**Type:** `string`