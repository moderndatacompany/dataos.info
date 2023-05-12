# mongodb

> 🗣 EXPERIMENTAL
This component is experimental and, therefore, subject to change or removal outside of major version releases.

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

## Fields

### `url`

The URL of the target MongoDB server.

Type: `string`

```
# Examples

url: mongodb://localhost:27017
```

---

### `username`

The username to connect to the database.

Type: `string`

Default: `""`

---

### `password`

The password to connect to the database.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly; read our secrets page for more info.


Type: `string`

Default: `""`

---

### `database`

The name of the target MongoDB database.

Type: `string`

---

### `collection`

The name of the target collection.

Type: `string`

---

### `key_field`

The field in the document that is used as the key.

Type: `string`

---

### `value_field`

The field in the document that is used as the value.

Type: `string`