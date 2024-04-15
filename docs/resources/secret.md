<!-- ![Secret Icon](/resources/secret_updated/Secret%20Icon.svg){ align=left } -->

# :resources-secret: Secret

In DataOS, Secrets are [Resources](../resources.md) designed for the secure storage of sensitive information, including usernames, passwords, certificates, tokens, or keys within the confines of a specific [DataOS Workspace](../resources/types_of_dataos_resources.md). 

To mitigate the risk of exposing confidential data, Secrets in DataOS separate sensitive information from application code or configuration files. This practice minimizes the chance of accidental exposure during resource management phases like creation, viewing, or editing. By leveraging Secrets, data developers safeguard sensitive information, thus reducing security vulnerabilities in their data workflows.

Operators can exercise precise control over who can retrieve credentials from Secrets, if in your organisation any data developer need access to secrets you can assign them a 'read secret' use case using [Bifrost](../interfaces/bifrost.md).

<aside class="callout">

🗣️ Each Secret in DataOS is linked to a specific <a href="https://dataos.info/resources/types_of_dataos_resources/#workspace-level-resources">Workspace</a>, confining its accessibility and application within that Workspace. This reinforces data security measures by ensuring that Secrets are only accessible within their designated Workspace. However, it's important to note that <a href="https://dataos.info/resources/instance_secret/">Instance-secret</a> have a broader scope, spanning across the entirety of the <a href="https://dataos.info/resources/types_of_dataos_resources/#instance-level-resources">DataOS instance</a> .

</aside>


<div class="grid cards" markdown>

-   :material-format-list-bulleted-type:{ .lg .middle } **How to create and manage a Secret?**

    ---

    Learn how to create and manage a Secret in DataOS.

    [:octicons-arrow-right-24: Create Secret](/resources/secret/#how-to-create-a-secret)


-   :material-script-text-outline:{ .lg .middle } **How to configure a Secret manifest file?**

    ---

    Discover how to configure a Secret manifest file by adjusting its attributes.

    [:octicons-arrow-right-24: Configure Secret](#create-a-secret-manifest-file)



-   :material-clock-fast:{ .lg .middle } **Different types of Secrets**

    ---

    Different types of Secret securely store diverse sensitive data, addressing specific needs like docker credentials, certificates, etc.

    [:octicons-arrow-right-24: Types](../resources/secret/secrets_attributes.md#secret-specific-section-attributes)


-   :material-console:{ .lg .middle } **How to refer to Secrets in other DataOS Resources?**

    ---

    Learn how to leverage DataOS Secrets to securely refer sensitive information in other DataOS Resources.


    [:octicons-arrow-right-24: Refer Secret](/resources/secret/#how-to-refer-secrets-in-other-dataos-resources)
</div>


## How to create a Secret?

Secrets are deployed using manifest files through the [Command Line Interface (CLI)](../interfaces/cli.md). During this deployment, Poros, the Resource Manager, orchestrates the forwarding of Secret Resource YAMLs to Heimdall, the Governance Engine within DataOS.
To create a Secret Resource in DataOS, follow these steps. This guide assumes you have the necessary permissions and access to the DataOS [CLI](../interfaces/cli.md).

### **Create a Secret manifest file**

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
For more information about the various attributes in Resource meta section, refer to the Attributes of [Resource meta section](../resources/resource_attributes.md).


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
| [`secret`](./secret/secrets_attributes.md) | object | none | none | mandatory |
| [`type`](./secret/secrets_attributes.md#types-of-secret) | string | none | cloud-kernel, cloud-kernel-image-pull, key-value, key-value-properties, certificates | mandatory |
| [`acl`](./secret/secrets_attributes.md#secretacl) | string | none | r, rw | mandatory |
| [`data`](./secret/secrets_attributes.md#secret-data) | mapping | none | none | mandatory |
| [`files`](./secret/secrets_attributes.md#secret-file) | string | none | file-path | optional |


For more information about the various attributes in Secret specific section, refer to the Attributes of [Secret specific section](./secret/secrets_attributes.md).

### **Apply the Secret manifest**

To apply the Secret manifest, utilize the DataOS [CLI](../interfaces/cli.md) by explicitly specifying the path to the manifest file and the designated workspace. The apply command is provided below:

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

## How to manage a Secret?

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

To remove the Secret Resource from the DataOS environment, utilize the `delete` command within the [CLI](../interfaces/cli.md). Execute the following command to initiate the deletion process:

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


## How to refer Secrets in other DataOS Resources?

To access the stored secret data in DataOS, you can reference them in your code using the `secrets` and `dataosSecrets` identifier. These identifiers ensure secure referencing of Secrets across different resources, enhancing system security and operational integrity.

<aside class="callout">

🗣 When you use the <code>secrets</code> identifier while referencing, the encrypted secrets are visible during linting, which is a process to check for errors, but they remain visible to end-users. So, while they are encrypted, they can still be seen by people accessing the configuration. On the other hand, if you use <code>dataosSecrets</code> identifier, during linting, the secrets are completely hidden within the configuration. This provides a higher level of security and confidentiality because even during checks for errors, the secrets are not exposed.
</aside>

**Syntax**

=== "dataosSecrets"
    ```yaml
    dataosSecrets:
    - name: ${your-secret-name} # Mandatory
        workspace: ${secret-workspace} # Optional
        key: ${key of your secret} # Optional, used when only single key is required.
        keys:            # Optional, used when multiple key is required.
        - ${secret_key}
        - ${secret-key}
        allKeys: ${true-or-false} # Optional
        consumptionType: ${envVars} # Optional, possible values: envVars, propfile and file.
    ```
=== "secrets"    
    ```yaml
    secrets:
    - name: ${your-secret-name} # Mandatory
        workspace: ${secret-workspace} # Optional
        key: ${key of your secret} # Optional, used when only single key is required.
        keys:            # Optional, used when multiple key is required.
        - ${secret_key}
        - ${secret-key}
        allKeys: ${true-or-false} # Optional
        consumptionType: ${envVars} # Optional, possible values: envVars, propfile and file.
    ```
Let's see how you can refer secrets in various resources: 

=== "In Service"

    In addition to serving as a conduit for real-time and streaming data exchanges, the [Service Resource](./service.md) within DataOS incorporates Secrets for secure access to confidential information. This ensures data privacy, and regulatory compliance, and facilitates timely insights and responses to dynamic information.


    === "Secret"
        ```yaml title="secret.yaml"
        --8<-- "examples/resources/secret/service/secret_service.yaml"
        ```

    === "Service"
        ```yaml title="service.yaml"
        --8<-- "examples/resources/secret/service/service.yaml"
        ```

=== "In Workflow"

    The [Workflow](./workflow.md) in DataOS serves as a Resource for orchestrating data processing tasks with dependencies. It enables the creation of complex data workflows by defining a hierarchy based on a dependency mechanism some requiring access to sensitive information such as API keys, authentication tokens, or database credentials. Instead of embedding these secrets directly in the workflow configuration, it is advisable to leverage references to the Secret Resource.

    === "Secret"
        ```yaml title="secret.yaml"
        --8<-- "examples/resources/secret/workflow/secret_workflow.yaml"
        ```

    === "Workflow"
        ```yaml title="workflow.yaml"
        --8<-- "examples/resources/secret/workflow/workflow.yaml"
        ```    

=== "In Worker"

    A [Worker Resource](./worker.md) in DataOS is a long-running process responsible for performing specific tasks or computations indefinitely. Workers are capable of securely accessing confidential information, such as API keys, through the referencing of secrets, thereby ensuring the safeguarding of sensitive data.

    === "Secret"
        ```yaml title="secret.yaml"
        --8<-- "examples/resources/secret/worker/secret_worker.yaml"
        ```

    === "Worker"
        ```yaml title="worker.yaml"
        --8<-- "examples/resources/secret/worker/worker.yaml"
        ```

=== "In Cluster"

    A Cluster in DataOS is a Resource that encompasses a set of computational resources and configurations necessary for executing data engineering and analytics tasks. Clusters are capable of securely accessing confidential information through the referencing of secrets, thereby ensuring the safeguarding of sensitive data.
    
    === "Secret"
        ```yaml title="secret.yaml"
        --8<-- "examples/resources/secret/cluster/cluster_secret.yaml"
        ```

    === "Cluster"
        ```yaml title="cluster.yaml"
        --8<-- "examples/resources/secret/cluster/cluster.yaml"
        ```


### **Referencing Secrets to Pull Images from Private Container Registry**

Following the successful creation of a Secret Resource, it can seamlessly pull images from the container registries. This approach obviates the need to embed sensitive authentication information directly within the resource configuration.

Container registries, pivotal for storing and managing images, including essential details like registry type, access credentials, and repository information, can efficiently reference pertinent secrets. This ensures a secure and streamlined process for pulling images from a private container registry without exposing sensitive authentication data within the configuration files.

=== "secret"
    ```yaml title="secret_image.yaml"
    --8<-- "examples/resources/secret/docker_image/secret_image.yaml"
    ```

=== "pull-image"    
    ```yaml title="refer_image_secret.yaml"
    --8<-- "examples/resources/secret/docker_image/alpha.yaml"
    ```
