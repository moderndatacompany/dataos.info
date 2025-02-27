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

## Fields

### **`url`**

The URL of the target MongoDB server.

**Type:** `string`

```
# Examples

url: mongodb://localhost:27017
```


**Type:** `string`

**Default:** `""`

---

### **`database`**

The name of the target MongoDB database.

**Type:** `string`

---

### **`collection`**

The name of the target collection.

**Type:** `string`

---

### **`key_field`**

The field in the document that is used as the key.

**Type:** `string`

---

### **`value_field`**

The field in the document that is used as the value.

**Type:** `string`