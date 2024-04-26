# Attributes of Instance Secret

## Structure of Instance Secret manifest

```yaml
# Instance-secret specific section
instance-secret:
  type: ${key-value-properties} # Type of Instance-secret (mandatory)
  acl: ${r|rw} # Access control list (mandatory)
  data: # Data section mapping (mandatory)
    ${username: iamgroot}
    ${password: abcd1234}
  files: # Manifest file path (optional)
    ${xyz: /home/instance-secret.yaml}
```
<center><i>Structure of Instance Secret manifest</i></center>

## Configuration

### **`instance-secret`**

**Description:** the Instance Secret section comprises the attribute of Instance Secret Resources.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid instance-secret attributes |

**Example Usage:**

```yaml
instance-secret: # Instance Secret mapping (mandatory)
  type: key-value-properties # Type of Instance-secret (mandatory)
  acl: r # Access control list (mandatory)
  data: # Data section mapping (mandatory)
    username: iamgroot
    password: yourpassword
```

---

### **`type`**

**Description:** the type of Instance Secret<br>

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | cloud-kernel, key-value, key-value-properties, certificates |

**Example Usage:** 

```yaml
instance-secret:
  type: key-value # Type of Secret
```

---

### **`acl`**

**Description:** access control list<br>

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | r, rw |

**Additional Notes:** the r value stands for Read while rw stands for Read-Write<br>

**Example Usage:** 

```yaml
instance-secret:
  acl: rw # Access Control List
```

---

### **`data`**

**Description:**the data section comprises the confidential data that needs to be stored. They are defined in the form of key-value pairs, which vary from secret type to type.<br>

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Additional Details:** The keys of `data` section must consist of alphanumeric characters, `-`, `_`, or `.`.<br>
**Example Usage:**<br>
```yaml
instance-secret:
  data: 
    key1: value1 
    key2: value2
```

---

### **`files`**

**Description:**the file section comprises the path of the file that contains the confidential data that needs to be stored. They are defined in the form of key-value pairs, which vary from secret type to type, and interpolated within the `data` field once the manifest file has been applied.<br>

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |


**Example Usage:**<br>
```yaml
instance-secret:
  files: 
    key_json: value1.json
```