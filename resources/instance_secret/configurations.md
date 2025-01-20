# Attributes of Instance Secret

## Structure of Instance Secret manifest

```yaml
# Resource meta section
name: depotsecret-r # Resource name (mandatory)
version: v1 # Manifest version (mandatory)
type: instance-secret # Resource-type (mandatory)
tags: # Tags (optional)
- just for practice
description: instance secret configuration # Description of Resource (optional)
layer: user
# Instance Secret-specific section
instance-secret: # Instance Secret mapping (mandatory)
    type: key-value-properties # Type of Instance-secret (mandatory)
    acl: r # Access control list (mandatory)
    data: # Data section mapping (mandatory)
    username: iamgroot
    password: yourpassword
```

<center><i>Structure of Instance Secret manifest</i></center>

## Configuration

### **Resource meta section**

The Instance Secret manifest comprise of a Resource meta section that outlines essential metadata attributes applicable to all Resource-types. Note that within this section some attributes are optional, while others are mandatory.
For more information about the various attributes in Resource meta section, refer to the [Attributes of Resource meta section](/resources/manifest_attributes/).

### **Instance Secret Specific Section**

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

#### **`type`**

**Description:** the type of Instance Secret<br>

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | cloud-kernel, key-value, key-value-properties, certificates |

**Example Usage:** 

```yaml
instance-secret:
  type: key-value # Type of Secret
```

Lets see each type of Instance Secrets one by one:

Instance secrets can be categorized into four types based on the nature of the credentials they store. When creating an instance secret resource, you can specify its type using the type field within the instance-secret section. The type of instance secret facilitates the programmatic handling of the secret data.

DataOS provides several built-in types for some common usage scenarios. These types vary in terms of the validations performed and the constraints DataOS imposes on them.

| Instance Secret Type | Description |
| --- | --- |
| `cloud-kernel` | This type stores arbitrary user-defined data in the form of key-value pair as a Kubernetes Secret with the same name as the Instance Secret Resource. |
| `key-value` | This type stores arbitrary user-defined data as key-value pairs within an Instance Secret, with each pair being encoded separately in base64 format. |
| `key-value-properties` | This type conserves arbitrary user-defined data as an Instance Secret by transforming multiple key-value pairs into a singular key-value pair, which is then encoded in base64 format. |
| `certificates` | This is an instance secret type used to securely store certificates, which are often necessary for secured communication in the system.  |


For a more detailed analysis of each type and to explore the syntax, please navigate the below tabs.

=== "cloud-kernel"

    The cloud-kernel instance secret type means that a Kubernetes secret will be created with the same name as the Instance Secret Resource.

    **Syntax**

    ```yaml title="instance_secret_type_cloud_kernel.yaml"
    --8<-- "examples/resources/instance_secret/types_of_instance_secret/cloud_kernel.yaml"
    ```

=== "key-value"


    This Instance Secret type is for storing simple pairs of keys and values. They are stored in Heimdall vault.

    **Syntax**

    ```yaml title="instance_secret_type_key_value.yaml"
    --8<-- "examples/resources/instance_secret/types_of_instance_secret/key_value.yaml"
    ```

    When you store an Instance Secret as a key-value type, the system passes the instance secret in the format they are stated, without any alterations.

=== "key-value-properties"

    This type is similar to key-value, but the difference lies in the way the system passes the data. In the key-value-properties type, the system passes all the key-value pairs as one single field, while in the case of the key-value type, they are passed as separate fields.

    **Syntax**

    ```yaml title="instance_secret_type_key_value_properties.yaml"
    --8<-- "examples/resources/instance_secret/types_of_instance_secret/key_value_properties.yaml"
    ```

=== "certificates"

    This type is used to store TLS certificates and keys. The most common usage scenario is Ingress resource termination, but this type is also sometimes used with other resources.

    **Syntax**

    ```yaml  title="instance_secret_type_certificates.yaml"
    --8<-- "examples/resources/instance_secret/types_of_instance_secret/certificates.yaml"
    ```


---

#### **`acl`**

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

#### **`data`**

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

#### **`files`**

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