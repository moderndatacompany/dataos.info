# Attributes of Resource Section

Following attributes are declared for every instance of a Resource that is deployed in a DataOS context. Some of these attributes/fields need to mandatorily declared, while others are optional.

## Resource Section Configuration Syntax

```yaml
name: {{myfirstresource}}
version: v1
type: {{resource-type}}
tags:
  - {{example-resource}}
  - {{dataos:workspace:curriculum}}
description: {{common attributes applicable to all dataos resources}}
owner: {{iamgroot}}
layer: {{user}}
<resource-type>:
```
<center><i>Resource section YAML configuration attributes</i></center>

## Configuration Attributes/Fields

### **`name`**

**Description:** declare a name for the Resource<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              |   <ul><li>alpha numeric values with the RegEx <br>`[a-z0-9]([-a-z0-9]*[a-z0-9])`; a hyphen/dash is allowed as a special character</li>  <li>total length of the string should be less than or equal to 48 characters</li>  <li>names of cluster & depot have a different RegEx <br>`[a-z]([a-z0-9]*)`; a hyphen/dash is **not** allowed as a special character</li>      |

**Additional information:** two resources in the same workspace cannot have the same name.<br>
**Example usage:**
```yaml
name: resourcename
```

---

### **`version`**

**Description:** the version of the Resource <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | v1, v1beta, v1alpha, v2alpha              |

**Example usage:**
```yaml
version: v1
```

---
### **`type`**

**Description:** provide the value for the Resource-type <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | cluster, compute, depot, policy,<br> secret, service, stack or workflow              |

**Example usage:**
```yaml
type: depot
```
---
### **`tags`**

**Description:** assign tags to the Resource-instance <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| mapping          | mandatory       | none              | any string; special characters are allowed  |

**Example usage:**
```yaml
tags: 
  - tag-example
  - dataos:resource:type
  - fordiscoverability
```
---

### **`description`**

**Description:** assign description to Resource<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | optional       | none              | any string  |

**Additional information:** the description can be within quotes or without.<br>
> YAML supports *scalars* such as strings, numbers, booleans, and null. A scalar value can be unquoted, within single quotes (') or double quotes ("). When the scalar contains a special character, the value must be declared within quotes.

**Example usage:**
```yaml
description: "This is a sample description of a Resource"  
```

---

### **`owner`**

**Description:** identification of the user <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | optional       | id of the user applying the Resource              | any valid dataos user id  |

**Additional information:** when no id is provided, or an incorrect id is provided, the system automatically corrects it to the id of the user who applied the Resource on DataOS CLI<br>
**Example usage:**
```yaml
owner: iamgroot
```

---

### **`layer`**

**Description:** declare the name of the layer in which Resource is going to be deployed <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | optional       | user             | user/system  |

**Additional information:** 
From a user's perspective, the operating system can be envisaged as working at two levels - user layer & system layer. This is only a logical separation to understand the workings of the system. <br>
**Example usage:** 
```yaml
layer: user
```
---

### **`<resource-type>`**

**Description:** specifies attributes specific to a \<resource-type\> <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| mapping          | mandatory       | none             | <ul><li><i>key</i> - cluster, compute, depot, policy, secret, service, stack or workflow</li><li><i>value</i> - attributes specific for a particular \<resource-type\></li></ul>  |

> By declaring the type of the Resource, say `workflow:`, followed by a space, we are basically creating a *mapping* in YAML.
> To know about the key-value pairs within each *mapping*, go through the pages of respective DataOS Resources. 

**Example usage:**
```yaml
cluster:
  {cluster-specific-attributes}
or
workflow:
  {workflow-specific-attributes}
# all resource-types are created in the same manner
```

The table below summarizes how the values for `version`, `type` & `layer` are declared for different types of Resources.

<center>

| Resource | version | type | layer | <resource-type\> |
| --- | --- | --- | --- | --- |
| Cluster | v1 | cluster | not required | cluster |
| Compute | v1beta | compute | system | compute |
| Depot | v1 | depot | user | depot |
| Policy | v1 | policy | user/system | policy |
| Secret | v1 | secret | not required | secret |
| Service | v1 | service | not required | service |
| Stack | NA | NA | NA | stack |
| Workflow | v1 | workflow | not required | workflow |

</center>
