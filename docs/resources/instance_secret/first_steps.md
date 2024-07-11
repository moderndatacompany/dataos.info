# Intance Secret: First Steps

## Create an Instance Secret

To create an Instance Secret Resource in DataOS, ensure you have access to the [DataOS Command Line Interface (CLI)](/interfaces/cli/) and the required permissions. Then, follow the provided steps to complete the creation process efficiently and securely.

### **Get Appropriate Access Permission Use Case**

In DataOS, different actions require specific use cases that grant the necessary permissions to execute a task. You can grant these use cases directly to a user or group them under a tag, which is then assigned to the user. The following table outlines various actions related to Worker Resources and the corresponding use cases required:

| **Action** | **Required Use Cases** |
|------------|------------------------|
| Create a Worker   | [Read Workspace]()         |
| Applying a Worker     | [Read Workspace]()         |
| Get Workers in a Workspace       | [Read Workspaces]()<br>[Read Resources in User Specified Workspace]() OR<br>[Read Resources in User Workspaces]() (for public and sandbox workspaces) |
| Delete Worker   | [Update]()                 |
| Get Worker Logs   | [Update]()                 |

To assign use cases, you can either contact the DataOS Operator or create a Grant Request by creating a Grant Resource. The request will be validated by the DataOS Operator.

### **Create a manifest file**

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



### **Apply the manifest**

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
    dataos-ctl resource apply -f depot_secret.yaml
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

### **Manage an Instance-Secret**

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
  

#### **Deleting an Instance Secret**

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

To remove the Instance Secret Resource from the DataOS environment, utilize the `delete` command. Execute the following commands to initiate the deletion process:

**Method 1:** Specify the Workspace, Resource-type, and Instance Secret name in the [`delete`](/interfaces/cli/command_reference/#delete) command.


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
    dataos-ctl resource delete -t instance-secret -n sampleinstsecret
    ```
    Alternative command
    ```shell
    dataos-ctl delete -t instance-secret -n sampleinstsecret
    ```
Output

```shell
dataos-ctl delete -t instance-secret -n sampleinstsecret
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstsecret:instance-secret...deleted
INFO[0000] 🗑 delete...complete
```

**Method 2:** Copy the Instance Secret name, version, and Resource-type from the output of the [`get`](/interfaces/cli/command_reference/#get) command seperated by '|' enclosed within quotes and use it as a string in the delete command.

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
    dataos-ctl resource delete -i sampleinstsecret:v1:instance-secret
    ```
Output

```shell
dataos-ctl delete -t instance-secret -n sampleinstsecret
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstsecret:instance-secret...deleted
INFO[0000] 🗑 delete...complete
```
**Method 3:** Specify the path of the YAML file and use the [`delete`](/interfaces/cli/command_reference/#delete) command.

=== "Command"

    ```shell
    dataos-ctl delete -f ${manifest-file-path}
    ```

=== "Example"

    ```shell
    dataos-ctl delete -f /home/desktop/connect-city/instance_secret.yaml
    ```

Output

```shell
dataos-ctl delete -t instance-secret -n sampleinstsecret
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstsecret:instance-secret...deleted
INFO[0000] 🗑 delete...complete
```