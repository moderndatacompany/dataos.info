## Configuration Attributes

### **`name`**

**Description:** Declare a name for the Resource 

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              |      alpha numeric values with the RegEx  `[a-z0-9]([-a-z0-9]*[a-z0-9])`; a hyphen/dash is allowed as a special character      total length of the string should be less than or equal to 48 characters      names of cluster & depot have a different RegEx  `[a-z]([a-z0-9]*)`; a hyphen/dash is **not** allowed as a special character        |

**Additional information:** two resources in the same workspace cannot have the same name. 
**Example usage:**
```yaml
name: resourcename
```

---

### **`version`**

**Description:** The version of the Resource  

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | v1, v1beta, v1alpha, v2alpha              |

**Example usage:**
```yaml
version: v1
```

---
### **`type`**

**Description:** Provide the value for the Resource-type  

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | cluster, compute, depot, policy,  secret, service, stack or workflow              |

**Example usage:**
```yaml
type: depot
```
---
### **`tags`**

**Description:** Assign tags to the Resource-instance  

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

**Description:** Assign description to Resource 

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | optional       | none              | any string  |

**Additional information:** the description can be within quotes or without. 
> YAML supports *scalars* such as strings, numbers, booleans, and null. A scalar value can be unquoted, within single quotes (') or double quotes ("). When the scalar contains a special character, the value must be declared within quotes.

**Example usage:**
```yaml
description: "This is a sample description of a Resource"  
```

---

### **`owner`**

**Description:** Identification of the user  

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | optional       | id of the user applying the Resource              | any valid dataos user id  |

**Additional information:** when no id is provided, or an incorrect id is provided, the system automatically corrects it to the id of the user who applied the Resource on DataOS CLI 
**Example usage:**
```yaml
owner: iamgroot
```

---

### **`layer`**

**Description:** Declare the name of the layer in which Resource is going to be deployed  

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | optional       | user             | user/system  |

**Additional information:** 
From a user's perspective, the operating system can be envisaged as working at two levels - user layer & system layer. This is only a logical separation to understand the workings of the system.  
**Example usage:** 
```yaml
layer: user
```