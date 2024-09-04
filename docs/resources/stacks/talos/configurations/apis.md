#  Talos API configurations

While configuring Talos, the `apis` folder contains an SQL file and a manifest file, an SQL file is where you write your queries, and the manifest file contains the URL path, description, source, and allowed user groups.

```sql
SELECT * FROM myschema.mytable LIMIT 10;
```

```yaml
urlPath: /table # output path
description: product list # description
source: ${{snowflakedepot}} # source name
allow:  # allowed user groups
  - intern  
  - datadev
```

### **`urlPath`**

**Description:** API endpoint path.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid URL path format |

**Example Usage:**

```yaml
urlPath: /table
```

### **`description`**

**Description:** Brief description about the data.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any descriptive text |

**Example Usage:**

```yaml
description: product list
```

### **`source`**

**Description:** The source name from which data is sourced.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid source reference |

**Example Usage:**

```yaml
source: ${{snowflakedepot}}
```

### **`allow`**

**Description:** List of allowed user groups.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | optional | none | List of valid user groups |

**Example Usage:**

```yaml
allow:
  - intern
  - datadev
```