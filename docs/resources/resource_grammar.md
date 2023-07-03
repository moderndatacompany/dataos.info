# Resource Grammar

Following attributes are declared for every instance of a Resource that is deployed in a DataOS context. Some of these attributes/fields need to mandatorily declared, while others are optional.

### **name**

```yaml
name: 
```

**Description:** declare a name for the Resource  
**Data type:** string  
**Requirement:** mandatory  
**Default value:** none  
**Possible values:** <br>
- alpha numeric values with the RegEx `[a-z0-9]([-a-z0-9]*[a-z0-9])`; a hyphen/dash is allowed as a special character  
- total length of the string should be less than or equal to 48 characters  
- names of cluster & depot have a different RegEx `[a-z]([a-z0-9]*)`; a hyphen/dash is **not** allowed as a special character <br>

**Example usage:** myfirstworkflow01  
**Additional information:** two resources in the same workspace cannot have the same name   

### **version**

```yaml
version: 
```

**Description:** the version of the Resource  
**Data type:** string  
**Requirement:** mandatory  
**Default value:** none  
**Possible value:** v1, v1beta, v2       
**Example usage:** v1  
**Additional information:**  

### **type**

```yaml
type: 
```

**Description:** provide the value for the Resource-type  
**Data type:** string    
**Requirement:** mandatory    
**Default value:** none    
**Possible value:** cluster, compute, depot, policy, secret, service, stack or workflow     
**Example usage:** depot    
**Additional information:**     

### **tags**

```yaml
tags:
  -
  -
```

**Description:** assign tags to the Resource-instance    
**Data type:** an array of strings  
**Requirement:** optional  
**Default value:** none
**Possible value:** any; special characters are allowed   
**Example usage:**  
```
tags: 
  - tag-example
  - dataos:resource:type
  - fordiscoverability
```
**Additional information:**
### **description**

```yaml
description: 
```

**Description:** assign tags to Resource  
**Data type:** string  
**Requirement:** optional  
**Default value:** none  
**Possible value:** any  
**Example usage:** "This is a sample description of a Resource"  
**Additional information:** The description can be within quotes or without.  
> YAML supports *scalars* such as strings, numbers, booleans, and null. A scalar value can be unquoted, within single quotes (') or double quotes ("). When the scalar contains a special character, the value must be declared within quotes.   

### **owner**

```yaml
owner: 
```

**Description:** identification of the user  
**Data type:** string  
**Requirement:** optional  
**Default value:** id of the user applying the Resource  
**Possible value:**   
**Example usage:** iamgroot  
**Additional information:** 
> when no id is provided, or an incorrect id is provided, the system automatically corrects it to the id of the user who applied the Resource on DataOS CLI   

### **layer**

```yaml
layer: 
```

**Description:** declare the name of the layer in which Resource is going to be deployed
**Data type:** string  
**Requirement:** optional  
**Default value:** user  
**Possible value:** user or system  
**Example usage:**  
**Additional information:** 
> From a user's perspective, the operating system can be envisaged as working at two levels - user layer & system layer. This is only a logical separation to understand the workings of the system.  

### **{{RESOURCE-TYPE}}**

```yaml
cluster: 
or
workflow:
# all resource-types are created in the same manner
```
**Description:** replace the key {{RESOURCE-TYPE}} with the type of the Resource being deployed  
**Data type:** string  
**Requirement:** mandatory    
**Default value:** none  
**Possible value:** cluster, compute, depot, policy, secret, service, stack or workflow   
**Example usage:** depot  
**Additional information:** In this case, the placeholder is meant for the key itself, and not the value. 
> By declaring the type of the Resource, say `workflow:`, followed by a space, we are basically creating a *mapping* in YAML.

The table below summarizes how the values for `version`, `type` & `layer` are declared for different types of Resources.

| Resource | Version | Type | layer | {{RESOURCE-TYPE}} |
| --- | --- | --- | --- | --- |
| Cluster | v1 | cluster | not required | cluster |
| Compute | v1beta | compute | system | compute |
| Depot | v1 | depot | user | depot |
| Policy | v1 | policy | user | policy |
| Secret | v1 | secret | not required | secret |
| Service | v1 | service | not required | service |
| Stack | NA | NA | NA | stack |
| Workflow | v1 | workflow | not required | workflow |