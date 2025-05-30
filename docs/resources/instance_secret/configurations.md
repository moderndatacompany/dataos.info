# Instance Secret attributes details

This section provides detailed information about each attribute in the manifest file of an Instance Secret.


## Structure of Instance Secret manifest

=== "Read-only Instance Secret"

    ```yaml 
    # Resource meta section
    name: depotsecret-r # Resource name (mandatory)
    version: v1 # Manifest version (mandatory)
    type: instance-secret # Resource-type (mandatory)
    tags: # Tags (optional)
      - data connection
      - snowflake depot
    description: instance secret configuration for snowflake data source # Description of Resource (optional)
    owner: iamgroot
    layer: user
    # Instance Secret-specific section
    instance-secret: # Instance Secret mapping (mandatory)
        type: key-value-properties # Type of Instance-secret (mandatory)
        acl: r # Access control list (mandatory)
        data: # Data section mapping (mandatory)
          username: iamgroot
          password: yourpassword
        files: 
          key_json: value1.json
    ```

=== "Read-write Instance Secret"

    ```yaml 
    # Resource meta section
    name: depotsecret-rw # Resource name (mandatory)
    version: v1 # Manifest version (mandatory)
    type: instance-secret # Resource-type (mandatory)
    tags: # Tags (optional)
      - data connection
      - snowflake depot
    description: instance secret configuration for snowflake data source # Description of Resource (optional)
    owner: iamgroot
    layer: user
    # Instance Secret-specific section
    instance-secret: # Instance Secret mapping (mandatory)
        type: key-value-properties # Type of Instance-secret (mandatory)
        acl: rw # Access control list (mandatory)
        data: # Data section mapping (mandatory)
          username: iamgroot
          password: yourpassword
        files: 
          key_json: value1.json      
    ```


## Configuration Attributes

### **`name`**

**Description:** Declare a name for the Instance Secret.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                                                                                                                                                                                                                                                                                                   |
| ------------- | --------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| string        | mandatory       | none              | alpha numeric values with the RegEx  `[a-z0-9]([-a-z0-9]*[a-z0-9])`; a hyphen/dash is allowed as a special character      total length of the string should be less than or equal to 48 characters      names of cluster & depot have a different RegEx  `[a-z]([a-z0-9]*)`; a hyphen/dash is **not** allowed as a special character |

**Additional information:** two resources in the same workspace cannot have the same name.

**Example usage:**

```yaml
name: resourcename
```

### **`version`**

**Description:** The version of the Resource

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**           |
| ------------- | --------------- | ----------------- | ---------------------------- |
| string        | mandatory       | none              | v1, v1beta, v1alpha, v2alpha |

**Example usage:**

```bash
version: v1
```

### **`type`**

**Description:** Provide the value for the Resource type.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                                   |
| ------------- | --------------- | ----------------- | -------------------------------------------------------------------- |
| string        | mandatory       | none              | cluster, compute, depot, policy,  secret, service, stack or workflow |

**Example usage:**

```yaml
type: instance-secret
```

### **`tags`**

**Description:** Assign tags to the Resource-instance

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                         |
| ------------- | --------------- | ----------------- | ------------------------------------------ |
| mapping       | mandatory       | none              | any string; special characters are allowed |

**Example usage:**

```javascript
tags: 
  - data connection
  - snowflake depot
```

### **`description`**

**Description:** Assign description to Resource

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------- | ----------------- | ------------------ |
| string        | optional        | none              | any string         |

**Additional information:** the description can be within quotes or without.

<aside class="callout">
🗣️ YAML supports 'scalars' such as strings, numbers, booleans, and null. A scalar value can be unquoted, within single quotes (') or double quotes ("). When the scalar contains a special character, the value must be declared within quotes.
</aside>

**Example usage:**

```yaml
description: "This is a sample description of a Resource"  
```

### **`owner`**

**Description:** Identification of the user

| **Data Type** | **Requirement** | **Default Value**                    | **Possible Value**       |
| ------------- | --------------- | ------------------------------------ | ------------------------ |
| string        | optional        | id of the user applying the Resource | any valid dataos user id |

**Additional information:** when no ID**** is provided, or an incorrect ID is provided, the system automatically corrects it to the ID of the user who applied the Resource on DataOS CLI

**Example usage:**

```yaml
owner: iamgroot
```

### **`layer`**

**Description:** Declare the name of the layer in which the Resource is going to be deployed

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------- | ----------------- | ------------------ |
| string        | optional        | user              | user/system        |

**Additional information:**
From a user's perspective, the operating system can be envisaged as working at two levels - user layer & system layer. This is only a logical separation to understand the workings of the system.

**Example usage:**

```yaml
layer: user
```

### **instance-secret**

**Description:**  The Instance Secret section comprises the attribute of Instance Secret Resources.

| Data Type | Requirement | Default Value | Possible Value                   |
| --------- | ----------- | ------------- | -------------------------------- |
| mapping   | mandatory   | none          | valid instance-secret attributes |

**Example Usage:**

```yaml
instance-secret: # Instance Secret mapping (mandatory)
  type: key-value-properties # Type of Instance-secret (mandatory)
  acl: r # Access control list (mandatory)
  data: # Data section mapping (mandatory)
    username: iamgroot
    password: yourpassword
```

### **`type`**

**Description:** the type of Instance Secret

| Data Type | Requirement | Default Value | Possible Value                                |
| --------- | ----------- | ------------- | --------------------------------------------- |
| string    | mandatory   | none          | key-value, key-value-properties, certificates |

**Example Usage:**

```yaml
instance-secret:
  type: key-value # Type of Secret
```

Let's see each type of Instance Secrets one by one:

Instance secrets can be categorized into three types based on the nature of the credentials they store. When creating an Instance Secret Resource, you can specify its type using the type field within the instance-secret section. The type of instance secret facilitates the programmatic handling of the secret data.

DataOS provides several built-in types for some common usage scenarios. These types vary in terms of the validations performed and the constraints DataOS imposes on them.

| Instance Secret Type   | Description                                                                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key-value`            | This type stores arbitrary user-defined data as key-value pairs within an Instance Secret, with each pair being encoded separately in base64 format.                                   |
| `key-value-properties` | This type conserves arbitrary user-defined data as an Instance Secret by transforming multiple key-value pairs into a singular key-value pair, which is then encoded in base64 format. |
| `certificates`         | This is an instance secret type used to securely store certificates, which are often necessary for secured communication in the system.                                                |

For a more detailed analysis of each type and to explore the syntax, please navigate the below tabs.


=== "key-value"

    This Instance Secret type is for storing simple pairs of keys and values. They are stored in Heimdall vault.

    **Syntax:**

    ```yaml
    name: ${testing}
    version: v1
    type: instance-secret
    instance-secret:
      type: key-value
      acl: r
      data:
        ${key1}: ${value1}
        ${key2}: ${value2}
    ```

    When you store an Instance Secret as a key-value type, the system passes the instance secret in the format they are stated, without any alterations.

=== "key-value-properties"

    This type is similar to key-value, but the difference lies in the way the system passes the data. In the key-value-properties type, the system passes all the key-value pairs as one single field, while in the case of the key-value type, they are passed as separate fields.

    **Syntax:**

    ```yaml
    name: ${testing}
    version: v1
    type: instance-secret
    secret:
      type: key-value-properties
      acl: r
      data:
        ${key1}: ${value1}
        ${key2}: ${value2}
    ```

=== "Certificates"

    This type is used to store TLS certificates and keys. The most common usage scenario is Ingress resource termination, but this type is also sometimes used with other resources.

    **Syntax:**

    ```yaml
    name: ${secret-name}
    version: v1
    type: instance-secret
    instance-secret:
      type: certificate
      acl: rw
      files:
          truststoreLocation: ${file-path}
          keystoreLocation: ${file-path}
    ```

---

### **`acl`**

**Description:** access control list

| Data Type | Requirement | Default Value | Possible Value |
| --------- | ----------- | ------------- | -------------- |
| string    | mandatory   | none          | r, rw          |

**Additional Notes:** the r value stands for Read while rw stands for Read-Write

**Example Usage:**

```yaml
instance-secret:
  acl: rw # Access Control List
```

### **`data`**

**Description:** The data section comprises the confidential data that needs to be stored. They are defined in the form of key-value pairs, which vary from secret type to type.

| Data Type | Requirement | Default Value | Possible Value |
| --------- | ----------- | ------------- | -------------- |
| mapping   | mandatory   | none          | none           |

**Additional Details:** The keys of `data` section must consist of alphanumeric characters, `-`, `_`, or `.`.

**Example Usage:**

```yaml
instance-secret:
  data: 
    key1: value1 
    key2: value2
```

### **`files`**

**Description:** The file section comprises the path of the file that contains the confidential data that needs to be stored. They are defined in the form of key-value pairs, which vary from secret type to type, and interpolated within the `data` field once the manifest file has been applied.

| Data Type | Requirement | Default Value | Possible Value |
| --------- | ----------- | ------------- | -------------- |
| mapping   | mandatory   | none          | none           |

**Example Usage:**

```yaml
instance-secret:
  files: 
    key_json: value1.json
```