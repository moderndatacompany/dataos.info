# Secret Resource YAML Configuration Field Reference

## Syntax

```yaml
version: v1 # Manifest Version
name: <secret-name> # Name of the Secret Resource
type: secret # Resource type here is Secret
secret: # Secret Section
  type: <secret-type> # Type of Secret
  acl: <r|rw>   # Access Control List (ACL) can be r|rw
  data: # Data Section
    key1: value1 # Key Value Pair 1
    key2: value2 # Key Value Pair 2
    ...
```

## Configuration Fields

### **`version`**

**Description:** Manifest-Version

**Data Type:** String

**Requirement:** Mandatory

**Default Value:** None

**Possible Value:** v1

**Example Usage:**

```yaml
version: v1 # Manifest Version
```

---

### **`name`**

**Description:** Name of the Secret resource. 

**Data Type:** String

**Requirement:** Mandatory

**Default Value:** None

**Possible Value:** Any string confirming the regex `[a-z0-9]([-a-z0-9]*[a-z0-9])` and maximum permissible length of the name is 47. 

**Acceptable values:**

1. myname
2. my-name
3. myname123
4. my-123-name
5. abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrs (less than 47 characters)

**Non-acceptable values:**

1. MyName (contains uppercase letter)
2. my_name (contains underscore)
3. 123myname (starts with a number)
4. myname- (ends with a hyphen)
5. abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrst (exceeds 47 characters)

**Additional Notes**: Provide a unique name for the secret resource.

**Example Usage:**

```yaml
name: my-secret # Name of the Secret Resource
```

---

### **`type`**

**Description:** Resource type is declared here. In the current case, it is a secret.

**Data Type:** String

**Default Value:** None

**Possible Value:** secret (For Secret Resource, the value should be secret, though its value could be any of the available resources in DataOS)

**Requirement:** Mandatory

**Additional Notes:** Resource type should be declared in all lowercase letters.

**Example Usage:**

```yaml
type: secret # Type of Resource (Here its Secret)
```

---

### **`tags`**

**Description:** Tags are a list of strings. These are attributes and keywords.

**Data Type:** List of Strings

**Requirement:** Optional

**Default Value:** None

**Possible Value:** List of Strings

**Additional Notes:** The tags are case-sensitive, so `Connect`, and `CONNECT` will be different tags. There is no limit on the length of the `tag`. In order to assign an output dataset in the Bronze/Silver/Gold categories within Metis UI, we can use the tag-like `tier.Bronze`/ `tier.Silver`/ `tier.Gold`.

**Example Usage:**

```yaml
tags: # Tags
	- developer
	- customer
```

---

### **`description`**

**Description:** Text describing the secret.

**Data Type:** String

**Requirement:** Optional

**Default Value:** None

**Possible Value:** Any string

**Additional Notes:** There is no limit on the length of the string

**Example Usage:** 

```yaml
description: Text describing the Secret # Description 
```

---

### **`secret`**

**Description:** The Secret Section comprises the properties of Secret Resources.

**Data Type:** Object

**Requirement:** Mandatory

**Additional Notes:** There is no limit on the length of the string

**Example Usage:** 

```yaml
secret: # Secret Section
  type: key-value # Type of Secret
  acl: rw # Access Control List
  data: # Data Section
    key1: value1 # Key Value Pairs
    key2: value2
```

---

### **`type`**

**Description:** The type of Secret within DataOS

**Data Type:** String

**Requirement:** Mandatory

**Default Value:** None

**Possible Value:** cloud-kernel, cloud-kernel-image-pull, key-value, key-value-properties, certificates

**Example Usage:** 

```yaml
type: key-value # Type of Secret
```

---

### **`acl`**

**Description:** Access Control List

**Data Type:** String

**Requirement:** Mandatory

**Default Value:** None

**Possible Value:** r, rw

**Additional Notes:** The r value stands for Read while rw stands for Read-Write

**Example Usage:** 

```yaml
acl: rw # Access Control List
```

---

### **`data`**

The data section comprises the confidential data that needs to be stored. They are defined in the form of key-value pairs, which vary from secret type to type.

**Data Type:** Object

**Requirement:** Mandatory

**Additional Details:** The keys of `data` section must consist of alphanumeric characters, `-`, `_`, or `.`. 

**Example Usage:** 

```yaml
data: # Data Section
  key1: value1 # Key Value Pairs
  key2: value2
```