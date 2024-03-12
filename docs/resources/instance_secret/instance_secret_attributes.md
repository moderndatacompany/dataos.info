# Instance Secret Attributes
### **Name:**

```yaml
name: {{sampledepot-r|rw}} 
```

Description: A unique identifier for instance secret. The name should follow the [a-z0-9](https://www.notion.so/moderndata/%5B-a-z0-9%5D*%5Ba-z0-9%5D) regex expression. It is important to ensure the Instance Secret's name should reflect the required "-r" or "-rw" extension

Default Value: None

Possible Value: Valid names are allowed to incorporate lowercase letters (a-z), numerical digits (0-9), and hyphens (-). Furthermore, the name is required to commence and conclude with an alphanumeric character, permitting the presence of hyphens within the name, but not consecutively.

Here are some examples of valid names:

- `abc`
- `a1b2c3`
- `name-123`
- `my-name`

Here are some examples of invalid names:

- `123abc` (starts with a number)
- `abc` (starts with a hyphen)
- `name--123` (consecutive hyphens)
- `too-long-name-that-exceeds-48-characters` (exceeds 48 characters)

Example Usage:

```yaml
name: adepot-r
```


>🗣 When opting for `acl:rw`, it's imperative to establish two Instance Secrets: one configured for `acl:r` and another for `acl:rw`, and refer both Instance Secrets into the Resource YAML.

</aside>

### **Version:**

```yaml
version: {{v1}} 
```

Description: The version of Instance Secret.

Default Value: V1

Possible Value: Instance Secrets currently have only one version V1, to check out all the versions of different resources use the following CLI command     

```basic
dataos-ctl develop types versions
```


>🗣 To use the above command you need to have the operator tag.

</aside>

Data Type: String

Requirement: Mandatory

Example usage:

```yaml
version: v1
```

### **Type:**

```yaml
type: {{resource-type}}
```

Description: The type of resources within DataOS.

Default Value: None

Possible Value: instance-secret

Data Type: String

Requirement: Mandatory

Example usage:

```yaml
type: instance-secret
```

### **Tags:**

```yaml
tags: 
  - {{tag}}
  - {{tag}}
```

Description: Additional tags for categorization.

Default Value: None

Possible Value: Any possible values

Data Type: List of Strings

Requirement: Optional

Example Usage:

```yaml
Tags:
  - sensitive
  - finance
```

### **Description:**

```yaml
description: {{Description of the secret}}
```

Description: A brief description of Instance Secret.

Default Value: None

Possible Value: Any possible values

Data Type: String

Requirement: Optional

Example Usage:

```yaml
description: instance secret configuration
```

### **Owner:**

```yaml
owner: {{owner_username}}
```

Description: The owner or creator of the secret

Default Value: Your username

Possible Value: Any existing username

Data Type: String

Requirement: Optional

Example usage:

```yaml
owner: iamgroot
```

### **Layer:**

```yaml
layer: {{user}}
```

Description: The attribute "layer" within the resource manifest indicates that the resource functions within the user layer. This designation signifies that the resource primarily engages at the user level, rather than interfacing directly with the system.

Default Value: None

Possible Value: user, system

Data Type: String

Requirement: Optional

Example usage:

```yaml
layer: user
```

### **Instance-Secret:**

Description: The Instance-Secret specific section comprises properties of Instance Secret Resources.

Data Type: Object

Requirement: Mandatory

Example usage:

```yaml
instance-secret: 
type: key-value-properties 
acl: r 
data: 
username: iamgroot
password: ********
```

#### **Instance-Secrets:type:**

```yaml
type: {{Instance-Secret-type}}
```

Description: Specifies the type of Instance Secret within DataOS.

Default Value: None

Possible Value: key-value, key-value-properties, certificate

Data Type: String

Requirement: Mandatory

Example usage:

```yaml
instance-secret:
  type: key-value-properties
```

#### **Types of Instance Secret Resources:**

1. **Key-Value:**
- **Purpose:** The 'key-value' Instance Secret type is a versatile solution for storing key-value pairs of sensitive information. Its simplicity and flexibility make it suitable for many Instance secrets, including usernames, passwords, and API keys.
- **Use Case:** Commonly employed for securely storing sensitive information due to its adaptable and straightforward structure.
2. **Key-value-properties:**
- **Purpose:** The 'key-value-properties' secret type shares similarities with the 'key-value' type but emphasizes properties. It allows for the storage of additional metadata or properties alongside key-value pairs, providing a more structured approach.
- **Use Case:** This type is ideal for scenarios where associating additional metadata or properties with each key-value pair is necessary.
3. **certificates:**
- **Purpose:** The 'certificates' secret type is designed to manage certificates. It facilitates the secure storage of sensitive information about SSL/TLS certificates, ensuring secure communication within a system.
- **Use Case:** Well-suited for securely managing certificates utilized in secure communication protocols.

#### **Instance-secret:acl:**

```yaml
acl: r|rw
```

Description: Access control list, defining the level of permissions for Instance Secret.

Default Value: None

Possible Values: r (Read), rw (Read-Write)

Data Type: String

Requirement: Mandatory

Example Usage:

```yaml
instance-secret: 
type: key-value-properties 
acl: r
```

#### **instance-secret:data:** 

The syntax of data attributes within the instance-secret type can vary depending on its specific type. 

Example usage:

```yaml
data: 
username: iamgroot
password: *******
```

- username:
    Description: The username associated with the secret.
    Data Type: String
    Requirement: Mandatory
- password: 
    Description: The password or secure key associated with the secret.
    Data Type: String
    Requirement: Mandatory