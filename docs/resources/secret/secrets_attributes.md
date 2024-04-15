#  Attributes of Secret-specific section

## Structure of Secret manifest

=== "Syntax"

    ```yaml
    secret:
      type: ${{secret_subtype}}
      acl: {{access_control_level}}
      data:
        ${{key1}}: ${{value1}}
        ${{key2}}: ${{value2}}
      file:   #Optional
        ${{xyz}}: ${{file-path}}  
    ```

=== "Example Usage"  

    ```yaml
    secret:
      type: key-value
      acl: rw
      data:
        username: iamgroot
        password: secure_password
    ```
## Secret-specific section attributes

**`secret`**

**Description**: `secret` comprising various configurations specific to the Secret.

| Default Value | Possible Values                                    | Data Type | Requirement |
|---------------|-----------------------------------------------------|-----------|-------------|
| None          | None | list of mappings   | Mandatory  |


**`type`**

**Description**: `type` specifies the type of Secret within DataOS.

| Default Value | Possible Values                                    | Data Type | Requirement |
|---------------|-----------------------------------------------------|-----------|-------------|
| None          | cloud-kernel, cloud-kernel-image-pull, key-value, key-value-properties, certificate | String    | Mandatory  |

Lets see each type of secrets one by one:

=== "cloud-kernel"
    - **Purpose**: The 'cloud-kernel' secret type is intended for the secure storage of credentials or sensitive information associated with cloud kernels. It is particularly suitable for managing authentication details, such as access keys or API tokens, required for interactions at the kernel level in cloud environments.
    - **Use Case**: This type is well-suited for the secure management of cloud-specific kernel-level credentials and configurations.

    === "Syntax"
        ```yaml
        name: testing
        version: v1
        type: secret
        description: a very special test secret
        secret:
          type: cloud-kernel
          acl: r
          data:
            ${{a: b}}
            ${{c: d}}
            ${{e: f}}
        ```

    === "Sample"
        ```yaml
        name: testing
        version: v1
        type: secret
        description: a very special test secret
        secret:
          type: cloud-kernel
          acl: r
          data:
            accesskeyid: *****************
            secretkey: ******************
        ```
        
=== "cloud-kernel-image-pull"
    - **Purpose:** The 'cloud-kernel-image-pull' secret type is designed for secrets related to the pulling of images in cloud environments. It encompasses authentication details essential for pulling container images from cloud-based repositories or registries.
    - **Use Case:** This type is optimal for securely managing secrets required during the retrieval of container images from cloud repositories.
    === "Syntax"
        ```yaml
        name: testing
        version: v1
        type: secret
        description: a very special test secret
        secret:
          type: cloud-kernel-image-pull
          acl: r
          data:
            ${{a: b}}
            ${{c: d}}
            ${{e: f}}
        ```
    === "Sample"
        ```yaml
        name: docker-image-pull
        version: v1beta1
        type: secret
        description: a very special test secret
        secret:
          type: cloud-kernel-image-pull
          acl: r
          data:
            .dockerconfigjson: |
              {
                "auths": {
                  "https://index.docker.io/v1/": {
                    "auth": "",
                    "username": "",
                    "password": ""
                  }
                }
              }
        ```

=== "key-value"
    - **Purpose:** The 'key-value' secret type is a versatile solution for storing key-value pairs of sensitive information. Its simplicity and flexibility make it suitable for a wide range of secrets, including usernames, passwords, and API keys.
    - **Use Case:** Commonly employed for the secure storage of various sensitive information due to its adaptable and straightforward structure.

    === "Syntax"
        ```yaml
        name: ${{testing}}
        version: v1
        type: secret
        secret:
          type: key-value
          acl: r
          data:
            ${{key1:value1}}
            ${{key2:value2}}
        ```

    === "Sample"
        ```yaml
        name: my-secret-name-rw
        version: v1beta1
        type: secret
        secret:
          type: key-value
          acl: rw    # can be r|rw
          data:
            accesskeyid: *****************
            secretkey: ******************
        ```

=== "key-value-properties"
    - **Purpose:** The 'key-value-properties' secret type shares similarities with the 'key-value' type but emphasizes properties. It allows for the storage of additional metadata or properties alongside key-value pairs, providing a more structured approach.
    - **Use Case:** This type is ideal for scenarios where associating additional metadata or properties with each key-value pair is necessary.
    === "Syntax"
        ```yaml
        name: ${{testing}}
        version: v1
        type: secret
        secret:
          type: key-value-properties
          acl: r
          data:
            ${{key1:value1}}
            ${{key2:value2}}
          key_json: ${{json-file-name}} # secrets in a file
        ```

    === "Sample"
        ```yaml
        version: v1beta1
        name: s3-pos-rw
        type: secret
        secret:
          type: key-value-properties
          acl: rw    # can be r|rw
          data:
            accesskeyid: *****************
            secretkey: ******************
            awsaccesskeyid: ****************
            awssecretaccesskey: **************
        ```

=== "certificate"
    - **Purpose:** The 'certificates' secret type is designed to manage certificates. It facilitates the secure storage of sensitive information about SSL/TLS certificates, ensuring secure communication within a system.
    - **Use Case:** Well-suited for securely managing certificates utilized in secure communication protocols.
    === "Syntax"
        ```yaml
        name: ${{secret-name}}
        version: v1
        type: secret
        secret:
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
        type: secret
        secret:
          type: certificate
          acl: rw
          files:
            truststoreLocation: /path/to/truststore/file
            keystoreLocation: /path/to/keystore/file
        ```

The main difference between "key-value" and "key-value-properties" secret types lies in how the system handles the data:

- **key-value**: The system passes each key-value pair separately, without any alterations, maintaining them as individual fields.

- **key-value-properties**: In contrast, the system passes all the secrets as one single field, treating them collectively, but it also allows for associating additional metadata or properties with each key-value pair. Additionally, this type supports referencing a file containing the secret value, providing flexibility in managing larger sets of data.

**`acl`**

**Description**: Access control list, defining the level of permissions for the secret.

| Default Value | Possible Values            | Data Type | Requirement |
|---------------|----------------------------|-----------|-------------|
| None          | r (Read), rw (Read-Write) | String    | Mandatory   |

Example Usage:

=== "read-only"

    ```yaml
    secret:
      type: key-value
      acl: r
      data:
        username: john_doe
        password: secure_password
    ```
=== "read-write"

    ```yaml
    secret:
      type: key-value
      acl: rw
      data:
        username: john_doe
        password: secure_password
    ```

**`data`**

**Description**: `data` comprises the various key value pairs of sensitive informations such as username and password.

Example Usage:

=== "Syntax"
    ```yaml
    secret:
      type: ${{key-value}}
      acl: rw|r
      data:
        key: ${{value}}
        key: ${{value}}
    ```

=== "Example Usage"
    ```yaml
    secret:
      type: key-value
      acl: rw
      data:
        username: john_doe
        password: secure_password
    ```
As per the Secret type, the data-specific section can contain different attributes. Below is the example usage of key-value-properties.

- username:
    Description: The username associated with the secret.
    Data Type: String
    Requirement: Mandatory
- password: 
    Description: The password or secure key associated with the secret.
    Data Type: String
    Requirement: Mandatory

These key-value pair can be different as per the different types of resources.

**`file`**

**Description**: You can directly pass the file containing your credentials.

| Default Value | Possible Values  | Data Type | Requirement |
|---------------|------------------|-----------|-------------|
| None          | Secret-file-path| String    | Optional    |


=== "Syntax"

    ```yaml
    secret:
      type: ${{key-value}}
      acl: rw|r
      data:
        key: ${{value}}
        key: ${{value}}
      file: ${{file-path}}  
    ```

=== "Example Usage"

    ```yaml
    secret:
      type: key-value-properties
      acl: rw
      data:
        username: john_doe
        password: secure_password
      file: path/file
    ```