# Resource Grammar

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
<center><i>Resource Section YAML configuration attributes/fields</i></center>

## Configuration Attributes/Fields

### **`name`**

**Description:** declare a name for the Resource<br> 
**Data type:** string<br>
**Requirement:** mandatory<br>
**Default value:** none<br>
**Possible value:**   
  - alpha numeric values with the RegEx `[a-z0-9]([-a-z0-9]*[a-z0-9])`; a hyphen/dash is allowed as a special character  
  - total length of the string should be less than or equal to 48 characters  
  - names of cluster & depot have a different RegEx `[a-z]([a-z0-9]*)`; a hyphen/dash is **not** allowed as a special character<br>
**Additional information:** two resources in the same workspace cannot have the same name.<br>
**Example usage:**
```yaml
name: resourcename
```

---

### **`version`**

**Description:** the version of the Resource <br> 
**Data type:** string <br>
**Requirement:** mandatory <br>
**Default value:** none <br>
**Possible value:** v1, v1beta, v2<br>
**Example usage:**
```yaml
version: v1
```

---
### **`type`**

**Description:** provide the value for the Resource-type <br> 
**Data type:** string <br>
**Requirement:** mandatory <br>
**Default value:** none <br>
**Possible value:** cluster, compute, depot, policy, secret, service, stack or workflow <br>
**Example usage:**
```yaml
type: depot
```
---
### **`tags`**

**Description:** assign tags to the Resource-instance <br>
**Data type:** a list of strings <br>
**Requirement:** optional <br>
**Default value:** none <br>
**Possible value:** any string; special characters are allowed <br>
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
**Data type:** string<br>
**Requirement:** optional<br>
**Default value:** none<br>
**Possible value:** any<br>
**Additional information:** the description can be within quotes or without.<br>
> YAML supports *scalars* such as strings, numbers, booleans, and null. A scalar value can be unquoted, within single quotes (') or double quotes ("). When the scalar contains a special character, the value must be declared within quotes.

**Example usage:**
```yaml
description: "This is a sample description of a Resource"  
```

---

### **`owner`**

**Description:** identification of the user <br>
**Data type:** string <br>
**Requirement:** optional <br>
**Default value:** id of the user applying the Resource<br>
**Possible value:** any valid dataos user id<br>
**Additional information:** when no id is provided, or an incorrect id is provided, the system automatically corrects it to the id of the user who applied the Resource on DataOS CLI<br>
**Example usage:**
```yaml
owner: iamgroot
```

---

### **`layer`**

**Description:** declare the name of the layer in which Resource is going to be deployed <br>
**Data type:** string <br>
**Requirement:** optional <br>
**Default value:** user <br>
**Possible value:** user/system <br>
**Additional information:** 
From a user's perspective, the operating system can be envisaged as working at two levels - user layer & system layer. This is only a logical separation to understand the workings of the system. <br>
**Example usage:** 
```yaml
layer: user
```
---

### **`<resource-type>`**

**Description:** specifies attributes specific to a \<resource-type\> <br>
**Data type:** object <br>
**Requirement:** mandatory <br>
**Default value:** none <br>
**Possible value:** 
- *key* - cluster, compute, depot, policy, secret, service, stack or workflow
- *value* - attributes specific for a particular \<resource-type\> <br>

> By declaring the type of the Resource, say `workflow:`, followed by a space, we are basically creating a *mapping* in YAML. 

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

| Resource | version | type | layer | \<resource-type\> |
| --- | --- | --- | --- | --- |
| Cluster | v1 | cluster | not required | cluster |
| Compute | v1beta | compute | system | compute |
| Depot | v1 | depot | user | depot |
| Policy | v1 | policy | user/system | policy |
| Secret | v1 | secret | not required | secret |
| Service | v1 | service | not required | service |
| Stack | NA | NA | NA | stack |
| Workflow | v1 | workflow | not required | workflow |