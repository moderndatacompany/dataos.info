# Secret: Fisrt Steps

## Create a Secret

Secrets are deployed using manifest files through the [Command Line Interface (CLI)](/interfaces/cli/). During this deployment, Poros, the Resource Manager, orchestrates the forwarding of Secret Resource YAMLs to Heimdall, the Governance Engine within DataOS.
To create a Secret Resource in DataOS, follow these steps. This guide assumes you have the necessary permissions and access to the DataOS [CLI](/interfaces/cli/).

### **Create a manifest file**

Begin by creating a manifest file that will hold the configuration details for your Secret.The structure of the Secret manifest file is provided in the image given below:

![Secret manifest structure](/resources/secret/Slide1.jpg)
The manifest file of a Secret Resource can be broken down into two separate sections - Resource meta section and Secret-specific section.



#### **Resource meta section**

The Resource meta section of the manifest configuration file encompasses attributes that maintain uniformity across all resource types. The provided manifest snippet illustrates the key-value pairs that must be declared in this section:

```yaml
name: ${{resource-name}} 
version: v1 
type: ${{resource-type}}
tags: 
  - ${{tag1}} 
  - ${{tag2}} 
description: ${{description of the secret}} 
owner: ${{owner_username}} 
```
For more information about the various attributes in Resource meta section, refer to the Attributes of [Resource meta section](/resources/).


#### **Secret-specific section**

The Secret-specific Section of the manifest configuration file includes key-value pairs specific to the type of Secret being created. The following manifest snippet illustrates the key values to be declared in this section:

=== "Syntax"
    ```yaml
    secret:
    type: ${{secret-subtype}} # Mandatory
    acl: ${{access-control-level}} # Mandatory
    data:                   # Mandatory
        ${{key1}}: ${{value1}} 
        ${{key2}}: ${{value2}}
    files: # Manifest file path (optional)
      ${{xyz: /home/secret.yaml}}
    ```
=== "Example Usage"
    ```yaml
    secret:
    type: key-value-properties # Mandatory
    acl: r # Mandatory
    data:                   # Mandatory
        username: iamgroot
        password: qwerrty
    files: # Manifest file path (optional)
      json_keyfile:  "/home/secret.json"
    ```


#### **Secret manifest Fields**
The table below provides a summary of the various attributes of the Secret-specific section:

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`secret`](/resources/secret/configurations#secret) | object | none | none | mandatory |
| [`type`](resources/secret/configurations#type) | string | none | cloud-kernel, cloud-kernel-image-pull, key-value, key-value-properties, certificates | mandatory |
| [`acl`](/resources/secret/configurations#acl) | string | none | r, rw | mandatory |
| [`data`](/resources/secret/configurations#data) | mapping | none | none | mandatory |
| [`files`](/resources/secret/configurations#file) | string | none | file-path | optional |


For more information about the various attributes in Secret specific section, refer to the Attributes of [Secret specific section](/resources/secret/configurations/).

### **Apply the manifest**

To apply the Secret manifest, utilize the DataOS [CLI](/interfaces/cli/) by explicitly specifying the path to the manifest file and the designated workspace. The apply command is provided below:

=== "Command"
    ```shell
    dataos-ctl apply -f ${path-to-secret-yaml} -w ${name-of-the-workspace}
    ```
=== "Example Usage"
    ```shell
    dataos-ctl apply -f mysecrets.yaml -w sandbox
    ```

Alternative to the above apply command.

=== "Command"
    ```shell
    dataos-ctl resource apply -f ${path/secret.yaml} -w ${name of the workspace}
    ```
=== "Example Usage"
    ```shell
    dataos-ctl resource apply -f mysecrets.yaml -w sandbox
    ```

<aside class="callout">

🗣 If a workspace is not explicitly specified during the application process, the system will default to the "public" workspace. 
</aside>

## Manage a Secret

### **Validate the Secret**

To validate the proper creation of the Secret Resource within the DataOS environment, employ the `get` command. Execute the following command to ascertain the existence and correctness of the Secret Resource:

=== "Command"

    ```shell
    dataos-ctl get -t secret -w ${workspace}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl get -t secret -w sandbox

    Expected Output:
    🔍 get...                                     
    🔍 get...complete                             

        NAME     | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |    OWNER     
    -------------|---------|-----------------|-----------|--------|---------|--------------
      mysecret   |   v1    |    secret       |  sandbox  | active |         | iamgroot 

    ```
**Alternative command:**

=== "Command"

    ```shell
    dataos-ctl resource get -t secret -w ${workspace}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl resource get -t secret -w sandbox

    Expected Output:
    🔍 get...                                     
    🔍 get...complete                             

        NAME     | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |    OWNER     
    -------------|---------|-----------------|-----------|--------|---------|--------------
      mysecret   |   v1    |    secret       |  sandbox  | active |         | iamgroot 
    ```

### **Delete the Secret**

To remove the Secret Resource from the DataOS environment, utilize the `delete` command within the [CLI](/interfaces/cli/). Execute the following command to initiate the deletion process:

<aside class="callout">
🗣 Before you can delete a Secret, you need to make sure there are no other resources still utilizing it. For example, if a Workflow has a dependency on a Secret, trying to delete that Secret will cause an error. So, you'll need to remove the Workflow first, and then you can delete the Secret. This rule applies to both <a href="https://dataos.info/resources/instance_secret/">Instance secret</a> and Secrets.
</aside>


**delete command structure for -t (type) and -n (name)**

=== "Command"

    ```shell
    dataos-ctl delete -t {{resource-type}} -n {{resource-name}} -w ${workspace}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl delete -t secret -n mysecret -w sandbox
    ```
**Altenative command:**
=== "Command"

    ```shell
    dataos-ctl resource delete -t {{resource-type}} -n {{resource-name}} -w ${workspace}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl resource delete -t secret -n mysecret -w sandbox
    ```

**delete command structure for -i (identifier)**

=== "Command"

    ```shell
    dataos-ctl delete -i {{resource-name:version:resource-type}}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl delete -i mysecret:v1:secret
    ```

