## How to create and manage an Instance Secret?

To create an Instance Secret Resource in DataOS, ensure you have access to the [DataOS Command Line Interface (CLI)](/interfaces/cli/) and the required permissions. Then, follow the provided steps to complete the creation process efficiently and securely.

### **Structure of an Instance Secret manifest file**

The structure of the Instance Secret manifest file is outlined as follows:

![Instance Secret Manifest Structure](/resources/instance_secret/instance_secret_manifest_structure.jpg)


### **Create an Instance Secret manifest file**

Begin by creating a manifest file that will hold the configuration details for your Instance Secret. A sample manifest is provided below:

???tip "Sample Instance Secret manifest"

    ```yaml title="sample_instance_secret_manifest.yaml"
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


#### **Resource meta section**

The Instance Secret manifest comprise of a Resource meta section that outlines essential metadata attributes applicable to all Resource-types. Note that within this section some attributes are optional, while others are mandatory.

```yaml
# Resource meta section
name: ${depotsecret-r} # Resource name (mandatory)
version: v1 # Manifest version (mandatory)
type: instance-secret # Resource-type (mandatory)
tags: 
  - ${new instance secret} # Tags (optional)
  - ${resource}
description: ${resource description} # Description (optional)
owner: ${iamgroot} # Owner's DataOS UserID (optional)
layer: ${user} # Layer (optional)
instance-secret: # Instance-secret specific section
```
<center><i>Resource meta section of the manifest file</i></center>

For more information about the various attributes in Resource meta section, refer to the [Attributes of Resource meta section](/resources/resource_attributes/).

#### **Instance Secret specific section**

This section focuses on Instance Secret attributes, outlining details such as Instance Secret `type`, `acl`(access control list), sensitive `data` to be stored. Additionally, it allows for the optional inclusion of file paths of sensitive information to be stored using the `files` attribute.

```yaml
instance-secret: # Instance-secret specific section
  type: ${{key-value-properties}} # Type of Instance-secret (mandatory)
  acl: ${{r|rw}} # Access control list (mandatory)
  data: # Data section mapping (either files or data is required)
    ${{username: iamgroot}}
    ${{password: abcd1234}}
  files: # Manifest file path (either files or data is required)
    ${{xyz: /home/instance-secret.yaml}}
```
<center><i>Instance-secret specific section of the manifest file</i></center>

The table below summarizes the attributes of Instance-secret specific section:

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`instance-secret`](/resources/instance_secret/manifest_attributes/#instance-secret) | mapping | none | none | mandatory |
| [`type`](/resources/instance_secret/manifest_attributes/#type) | string | none | cloud-kernel, key-value, key-value-properties, certificates | mandatory |
| [`acl`](/resources/instance_secret/manifest_attributes/#acl) | string | none | r, rw | mandatory |
| [`data`](/resources/instance_secret/manifest_attributes/#data) | mapping | none | none | mandatory |
| [`files`](/resources/instance_secret/manifest_attributes/#files) | string | none | file-path | optional |


For more information about the various attributes in Instance Secret specific section, refer to the [Attributes of Instance Secret specific section](/resources/instance_secret/configuration/).



### **Apply the Instance Secret manifest**

To create an Instance Secret Resource-instance within the DataOS, use the `apply` command. When applying the manifest file from the DataOS CLI, make sure you don't specify Workspace as Instance Secrets are [Instance-level Resource](/resources/). The `apply` command is as follows:

=== "Command"
    ```shell
    dataos-ctl resource apply -f ${path/instance_secret.yaml}
    ```
    Alternate
    ```shell
    dataos-ctl apply -f ${path/instance_secret.yaml}
    ```
=== "Example Usage"
    ```shell
    dataos-ctl apply -f depot_secret.yaml
    ```
    Alternate
    ```shell
    dataos-ctl apply -f depot_secret.yaml
    ```
    Expected output:

    ```shell
    $ dataos-ctl apply -f depot_secret.yaml
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying depotsecret-r:v1:instance-secret... 
    INFO[0004] 🔧 applying depotsecret-r:v1:instance-secret...created 
    INFO[0004] 🛠 apply...complete
    ```

### **Managing an Instance-Secret**

#### **Validate the Instance Secret**

To validate the proper creation of the Instance Secret Resource within the DataOS environment, employ the `get` command. Execute the following command to ascertain the existence of the Instance Secret Resource:

=== "Command"
    - To get the details of instance-secret created by the user who applies the instance-secret, use the following command:

        ```shell
        dataos-ctl resource get -t instance-secret
        ```
        Alternative command

        ```shell
        dataos-ctl get -t instance-secret
        ```
    - To get the details of instance-secret created by all the users within the DataOS Instance, use the above command with `-a` flag:

        ```shell
        dataos-ctl resource get -t instance-secret -a
        ```
        Alternate command

        ```shell
        dataos-ctl get -t instance-secret -a
        ```


=== "Example Usage"

    ```shell
    dataos-ctl get -t instance-secret
    ```
    Alternative command
    ```shell
    dataos-ctl resource get -t instance-secret -a
    ```
    Expected Output
    ```shell
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             

            NAME     | VERSION |      TYPE       | WORKSPACE | STATUS |  RUNTIME  |  OWNER             
    -----------------|---------|-----------------|-----------|--------|-----------|------------------------------
         depotsecret | v1      | instance-secret |           | active |           | iamgroot               
    ```


#### **Delete the Instance Secret**

<aside class="callout">
🗣️ Before you can delete an Instance Secret, you need to make sure there are no other Resources dependent on it. For example, if a Depot has a dependency on an Instance Secret, trying to delete that Instance Secret will cause an error. So, you'll need to remove the Depot first, and then you can delete the Instance Secret. This rule applies to not just Depot, but all dependent Resources, such as Workflow, Service, Worker, etc.

<details><summary>Error</summary>
The following error will be thrown if any Resource has a dependency on Instance Secret as shown below.

Example usage:

```shell
dataos-ctl delete -t instance-secret -n sampleinstsecret
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstsecret:v1:instance-secret... 
INFO[0001] 🗑 deleting sampleinstsecret:v1:instance-secret...error 
WARN[0001] 🗑 delete...error                             
ERRO[0001] Invalid Parameter - failure deleting instance resource : cannot delete resource, it is a dependency of 'depot:v2alpha:sampleinstdepot'
```
</aside>

To remove the Instance Secret Resource from the DataOS environment, utilize the `delete` command. Execute the following command to initiate the deletion process:

**Deleting using the -t (type) and -n (name) flag**

=== "Command"

    ```shell
    dataos-ctl resource delete -t ${resource-type} -n ${resource-name}
    ```
    Alternative command
    ```shell
    dataos-ctl delete -t ${resource-type} -n ${resource-name}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl resource delete -t instance-secret -n myinstance_secret
    ```
    Alternate
    ```shell
    dataos-ctl delete -t instance-secret -n myinstance_secret
    ```


**Deleting using the -i (identifier) flag**

=== "Command"

    ```shell
    dataos-ctl resource delete -i ${resource-name:version:resource-type}
    ```
    Alternative command
    ```shell
    dataos-ctl resource delete -i ${resource-name:version:resource-type}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl delete -i myinstance_secret:v1:instance-secret
    ```
    Expected output
    ```shell
    dataos-ctl delete -t instance-secret -n sampleinstsecret
    INFO[0000] 🗑 delete...                                  
    INFO[0000] 🗑 deleting sampleinstsecret:instance-secret...nothing 
    INFO[0000] 🗑 delete...complete
    ```

## Types of Instance Secrets

When creating Instance Secret Resource, you can specify its type using the `type` field within the `instance-secret` section. The Instance Secret type is used to facilitate programmatic handling of the Secret data.

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