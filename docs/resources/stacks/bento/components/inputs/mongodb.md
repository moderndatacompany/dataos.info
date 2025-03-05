# mongodb

> 🗣 EXPERIMENTAL
This component is experimental and, therefore, subject to change or removal outside of major version releases.

Executes a find query and creates a message for each row received.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  mongodb:
    url: ""
    database: ""
    collection: ""
    username: ""
    password: ""
    query: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  mongodb:
    url: ""
    database: ""
    collection: ""
    username: ""
    password: ""
    operation: find
    json_marshal_mode: canonical
    query: ""
```

Once the rows from the query are exhausted, this input shuts down, allowing the pipeline to gracefully terminate (or the next input in a sequence to execute).

## Fields

### `url`

The URL of the target MongoDB DB.

Type: `string`

```yaml
# Examples

url: mongodb://localhost:27017
```

---

### `database`

The name of the target MongoDB database.

Type: `string`

---

### `collection`

The collection to select from.

Type: `string`

---

### `username`

The username to connect to the database.

Type: `string`

Default: `""`

---

### `password`

The password to connect to the database.

Type: `string`

Default: `""`

---

### `operation`

The mongodb operation to perform.

Type: `string`

Default: `"find"`

Options: `find`, `aggregate`.

---

### `json_marshal_mode`

The json_marshal_mode setting is optional and controls the format of the output message.

Type: `string`

Default: `"canonical"`

| Option | Summary |
| --- | --- |
| Canonical | A string format that emphasizes type preservation at the expense of readability and interoperability. That is, conversion from canonical to BSON will generally preserve type information except in certain specific cases. |
| Relaxed | A string format that emphasizes readability and interoperability at the expense of type preservation.That is, conversion from relaxed format to BSON can lose type information. |

---

### `query`

Bloblang expression describing MongoDB query.

Type: `string`

```yaml
# Examples

query: |2
        root.from = {"$lte": timestamp_unix()}
        root.to = {"$gte": timestamp_unix()}
```