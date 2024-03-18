# Instance Secret Attributes

## Intance-Secret manifest

=== "Syntax"
    ```yaml
    # Instance-secret specific section
    instance-secret:
      type: key-value-properties # Type of Instance-secret (mandatory)
      acl: ${{r|rw}} # Access control list (mandatory)
      data: # Data section mapping (mandatory)
        ${{username: iamgroot}}
        ${{password: abcd1234}}
      files: # Manifest file path (optional)
        ${{xyz: /home/instance-secret.yaml}}
    ```
=== "Example Usage"
    ```yaml
    instance-secret: 
      type: key-value-properties 
      acl: r 
      data: 
        username: iamgroot
        password: ********
    ```
Description: The Instance-Secret specific section comprises properties of Instance Secret Resources.

Data Type: Object

Requirement: Mandatory


## **Instance-Secrets:type**


=== "Syntax"
    ```yaml
    type: {{Instance-Secret-type}}
    ```
=== "Example Usage"
    ```yaml
    instance-secret:
      type: key-value-properties
    ```

Description: Specifies the type of Instance Secret within DataOS.

Default Value: None

Possible Value: key-value, key-value-properties, certificate

Data Type: String

Requirement: Mandatory


## **Types of Instance Secret**

=== "key-value"
    - **Purpose:** The 'key-value' Instance secret type is a versatile solution for storing key-value pairs of sensitive information. Its simplicity and flexibility make it suitable for a wide range of secrets, including usernames, passwords, and API keys.
    - **Use Case:** Commonly employed for the secure storage of various sensitive information due to its adaptable and straightforward structure.

    === "Syntax"
        ```yaml
        name: ${{testing}}
        version: v1
        type: instance-secret
        instance-secret:
          type: key-value
          acl: r
          data:
            ${{key1:value1}}
            ${{key2:value2}}
        ```

    === "Example Usage"
        ```yaml
        name: my-secret-name-rw
        version: v1beta1
        type: instance-secret
        instance-secret:
          type: key-value
          acl: rw    # can be r|rw
          data:
            accesskeyid: *****************
            secretkey: ******************
        ```

=== "key-value-properties"
    - **Purpose:** The 'key-value-properties' Instancce Secret type shares similarities with the 'key-value' type but emphasizes properties. It allows for the storage of additional metadata or properties alongside key-value pairs, providing a more structured approach.
    - **Use Case:** This type is ideal for scenarios where associating additional metadata or properties with each key-value pair is necessary.
    === "Syntax"
        ```yaml
        name: ${{testing}}
        version: v1
        type: instance-secret
        instance-secret:
          type: key-value-properties
          acl: r
          data:
            ${{key1:value1}}
            ${{key2:value2}}
          key_json: ${{json-file-name}} # instance secrets in a file
        ```

    === "Sample"
        ```yaml
        version: v1beta1
        name: s3-pos-rw
        type: instance-secret
        instance-secret:
          type: key-value-properties
          acl: rw    # can be r|rw
          data:
            accesskeyid: *****************
            secretkey: ******************
            awsaccesskeyid: ****************
            awssecretaccesskey: **************
        ```

=== "certificate"
    - **Purpose:** The 'certificates' Instance Secret type is designed to manage certificates. It facilitates the secure storage of sensitive information about SSL/TLS certificates, ensuring secure communication within a system.
    - **Use Case:** Well-suited for securely managing certificates utilized in secure communication protocols.
    === "Syntax"
        ```yaml
        name: ${{instance-secret-name}}
        version: v1
        type: instance-secret
        instance-secret:
          type: certificate
          acl: rw
          files:
            truststoreLocation: ${{file-path}}
            keystoreLocation: ${{file-path}}
        ```

    === "Sample"
        ```yaml
        name: my-certificate-secret
        version: v1
        type: instance-secret
        instance-secret:
          type: certificate
          acl: rw
          files:
            truststoreLocation: /path/to/truststore/file
            keystoreLocation: /path/to/keystore/file
        ```

The main difference between "key-value" and "key-value-properties" Instance Secret types lies in how the system handles the data:

- **key-value**: The system passes each key-value pair separately, without any alterations, maintaining them as individual fields.

- **key-value-properties**: In contrast, the system passes all the secrets as one single field, treating them collectively, but it also allows for associating additional metadata or properties with each key-value pair. Additionally, this type supports referencing a file containing the secret value, providing flexibility in managing larger sets of data.

## **Instance-secret:acl**

=== "Syntax"
    ```yaml
    acl: r|rw
    ```

=== "Example Usage"
    ```yaml
    instance-secret: 
      type: key-value-properties 
      acl: r
    ```

Description: Access control list, defining the level of permissions for Instance Secret.

Default Value: None

Possible Values: r (Read), rw (Read-Write)

Data Type: String

Requirement: Mandatory


## **instance-secret:data** 

The syntax of data attributes within the instance-secret type can vary depending on its specific type. 

=== "Syntax"
    ```yaml
    data: # Data section mapping (mandatory)
      ${{username: iamgroot}}
      ${{password: abcd1234}}
    ```

=== "Example Usage"
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

These key-value pair can be different as per the different types of resources, get to know more about this in [Instance-Secret templates section](../instance_secret.md).
   