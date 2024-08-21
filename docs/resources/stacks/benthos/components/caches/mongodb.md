# mongodb

Tags: MongoDB

<aside>
🗣 <b>EXPERIMENTAL</b> This component is experimental and, therefore, subject to change or removal outside of major version releases.

</aside>

Use a MongoDB instance as a cache.

```yaml
# Config fields, showing default values
label: ""
mongodb:
  url: ""
  username: ""
  password: ""
  database: ""
  collection: ""
  key_field: ""
  value_field: ""
```

## Fields[](https://www.benthos.dev/docs/components/caches/mongodb#fields)

### `url`[](https://www.benthos.dev/docs/components/caches/mongodb#url)

The URL of the target MongoDB server.

**Type:** `string`

```
# Examples

url: mongodb://localhost:27017
```


**Type:** `string`

**Default:** `""`

---

### `database`[](https://www.benthos.dev/docs/components/caches/mongodb#database)

The name of the target MongoDB database.

**Type:** `string`

---

### `collection`[](https://www.benthos.dev/docs/components/caches/mongodb#collection)

The name of the target collection.

**Type:** `string`

---

### `key_field`[](https://www.benthos.dev/docs/components/caches/mongodb#key_field)

The field in the document that is used as the key.

**Type:** `string`

---

### `value_field`[](https://www.benthos.dev/docs/components/caches/mongodb#value_field)

The field in the document that is used as the value.

**Type:** `string`