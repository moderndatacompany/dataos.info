# Toolbox Stack Grammar

```yaml
stackSpec: 
  dataset: dataos://icebase:sample/city?acl=rw 
  action: 
    name: set_version 
    value: latest 
```

## Configuration Attributes

### **`stackSpec`**

**Description:** specifies the toolbox-stack specific section<br>
**Data Type:** object<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** none<br>
**Example Usage:**<br>
```yaml
stackSpec:
  {}
```

---

### **`dataset`**

**Description:** dataset udl address<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** any iceberg dataset udl<br>
**Additional Information:** adding acl=rw after the dataset name is part of best practice in case the source system has separate keys for read and read write<br>
**Example Usage:**<br>
```yaml
dataset: dataos://icebase:sample/city?acl=rw
```

---

### **`action`**

**Description:** toolbox action specific section<br>
**Data Type:** string<br>
**Requirement:** optional<br>
**Default Value:** user-id of the user<br>
**Possible Value:** user-id of the use-case assignee<br>
**Example Usage:**<br>
```yaml
action:
  {}
```

---

### **`name`**

**Description:** specifies the toolbox action. The `set_verison` action sets the metadata version to any specific version you want it to.<br>
**Data Type:** object<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** set_version<br>
**Example Usage:**<br>
```yaml
name: set_version
```

---

### **`value`**

**Description:** the version of the metadata which you want to set to.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** latest, v2.json, v1.json<br>
**Additional Information:** you can use the `dataos-ctl list-metadata` to check the available metadata version for iceberg datasets.<br>
**Example Usage:**<br>
```yaml
value: latest
```