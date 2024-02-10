# Secret-specific Section Grammar

## Syntax

```yaml
secret: 
  type: ${{secret-type}} 
  acl: ${{r|rw}}   
  data: 
    ${{key1: value1}} 
    ${{key2: value2}} 
    ...
```

## Configuration Fields

### **`secret`**

**Description:** the Secret Section comprises the properties of Secret Resources.
**Data Type:** object
**Requirement:** mandatory
**Additional Notes:** there is no limit on the length of the string
**Example Usage:** 

```yaml
secret: 
  type: key-value 
  acl: rw 
  data: 
    key1: value1 
    key2: value2
```

---

### **`type`**

**Description:** the type of Secret within DataOS<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** cloud-kernel, cloud-kernel-image-pull, key-value, key-value-properties, certificates<br>
**Example Usage:** 

```yaml
type: key-value # Type of Secret
```

---

### **`acl`**

**Description:** access control list<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** r, rw<br>
**Additional Notes:** the r value stands for Read while rw stands for Read-Write<br>
**Example Usage:** 

```yaml
acl: rw # Access Control List
```

---

### **`data`**

**Description:**the data section comprises the confidential data that needs to be stored. They are defined in the form of key-value pairs, which vary from secret type to type.<br>
**Data Type:** object<br>
**Requirement:** mandatory<br>
**Additional Details:** The keys of `data` section must consist of alphanumeric characters, `-`, `_`, or `.`.<br>
**Example Usage:**<br>
```yaml
data: 
  key1: value1 
  key2: value2
```