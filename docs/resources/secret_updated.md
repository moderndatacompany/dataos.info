<!-- ![Secret Icon](/resources/secret_updated/Secret%20Icon.svg){ align=left } -->

# :resources-secret: Secret

In DataOS, Secrets are [Resources](../resources.md) designed for the secure storage of sensitive information, including usernames, passwords, certificates, tokens, or keys within the confines of a specific **DataOS Workspace**. The primary purpose of Secrets is to address the inherent exposure risk associated with directly embedding such confidential data within application code or configuration files.

Data developers leverage Secrets in DataOS to achieve a crucial separation of sensitive data from Resource definitions. This segregation minimizes the likelihood of accidental exposure during the various phases of Resource management, including creation, viewing, or editing. Using Secrets, data developers ensure that sensitive information remains protected, reducing security vulnerabilities in their data workflows.

Data developers can exercise precise control over who can retrieve credentials from Secrets. Heimdall's fine-grained permissions enable effective management of access, ensuring that only authorized users or applications can access sensitive information when needed.

<aside class="callout">

Each Secret within DataOS is intricately linked to a specific Workspace. This association effectively confines the accessibility and application of the Secret to the boundaries of that particular Workspace, reinforcing data security measures.
While Workspace-level confidentiality is maintained for Secrets, it's essential to recognize that instance secrets exhibit a broader scope, spanning across the entirety of the DataOS Instance.

</aside>


<div class="grid cards" markdown>

-   :material-format-list-bulleted-type:{ .lg .middle } **How to create and manage a Secret?**

    ---

    Secrets provide secure storage for sensitive information, reducing exposure risks inherent in embedding such data directly in resource configurations.

    [:octicons-arrow-right-24: Create Secret](/resources/secret_updated/#how-to-create-a-secret)


-   :material-script-text-outline:{ .lg .middle } **How to refer a Secret into other Resources?**

    ---

    A Secret manifest file includes resource meta and Secret specific sections with attributes that must be configured for creating a Secret.

    [:octicons-arrow-right-24: Refering Secrets](#how-to-refer-secrets-in-other-dataos-resources)



-   :material-clock-fast:{ .lg .middle } **Types of Secrets**

    ---

    DataOS Secret types securely store diverse sensitive data, addressing specific needs like cloud credentials, image pulling, key-value pairs, metadata, and SSL/TLS certificates.

    [:octicons-arrow-right-24: Types](../resources/secret_updated/secrets_attributes.md)


-   :material-console:{ .lg .middle } **Example Usage**

    ---

    Secret Resources streamline secure image pulling from container registries, preventing exposure of authentication data in configuration files.


    [:octicons-arrow-right-24: Example](/resources/secret_updated/#referencing-secrets-to-pull-images-from-private-container-registry)
</div>


## How to create a Secret?

Secrets are deployed using YAML files through the [Command Line Interface (CLI)](../interfaces/cli.md). During this deployment, Poros, the Resource Manager, orchestrates the forwarding of Secret Resource YAMLs to Heimdall, the Governance Engine within DataOS.
To create a Secret Resource in DataOS, follow these steps. This guide assumes you have the necessary permissions and access to the DataOS [Command Line Interface (CLI)](../interfaces/cli.md).

### **Create a Secret manifest file**

Begin by creating a manifest file that will hold the configuration details for your Secret.

![Secret YAML structure](/resources/secret_updated/Slide1.jpg)


#### **Resource meta section**

The Resource meta section of the YAML configuration file encompasses attributes that maintain uniformity across all resource types. The provided YAML snippet illustrates the key-value pairs that must be declared in this section:

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

The Secret-specific Section of the YAML configuration file includes key-value pairs specific to the type of Secret being created. The following YAML snippet illustrates the key values to be declared in this section:

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

#### **Secret YAML Configuration Fields**

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`secret`](./secret_updated/secrets_attributes.md#secret-attributes-configuration) | object | none | none | mandatory |
| [`type`](./secret_updated/secrets_attributes.md#types-of-secret) | string | none | cloud-kernel, cloud-kernel-image-pull, key-value, key-value-properties, certificates | mandatory |
| [`acl`](./secret_updated/secrets_attributes.md#secretacl) | string | none | r, rw | mandatory |
| [`data`](./secret_updated/secrets_attributes.md#secret-data) | object | none | none | mandatory |
| [`files`](./secret_updated/secrets_attributes.md#secret-file) | string | none | file-path | optional |


For more information about the various attributes in Secret specific section, refer to the Attributes of [Secret specific section](./secret_updated/secrets_attributes.md).

### **Apply the Secret configurations**

To apply the Secret YAML, utilize the DataOS [Command Line Interface (CLI)](../interfaces/cli.md) by explicitly specifying the path to the YAML file and the designated workspace. The apply command is provided below:

=== "Command"
    ```shell
    dataos-ctl apply -f ${path/secret.yaml} -w ${name of the workspace}
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

🗣 If a workspace is not explicitly specified during the application process, the system will default to the "public" workspace. This default behavior ensures seamless execution, allowing for the application of the Secret YAML within the public workspace without the need for an explicit workspace designation.

</aside>

## How to manage a Secret?

### **Validate the Secret**

To validate the proper creation of the Secret Resource within the DataOS environment, employ the `get` command. Execute the following command to ascertain the existence and correctness of the Secret Resource:

=== "Command"

    ```shell
    dataos-ctl get -t secret -w {{workspace}}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl get -t secret -w sandbox
    ```

### **Delete the Secret**

To remove the Secret Resource from the DataOS environment, utilize the `delete` command within the [Command Line Interface (CLI)](../interfaces/cli.md). Execute the following command to initiate the deletion process:

**delete command structure for -t (type) and -n (name)**

=== "Command"

    ```shell
    dataos-ctl delete -t {{resource-type}} -n {{resource-name}}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl delete -t secret -n mysecret
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

Before you can delete a Secret, you need to make sure there are no other resources still utilizing it. For example, if a Workflow has a dependency on a Secret, trying to delete that Secret will cause an error. So, you'll need to remove the Workflow first, and then you can delete the Secret. This rule applies to both [Instance Secrets](../resources/instance_secret.md) and Secrets.

## How to refer Secrets in other DataOS Resources?

To access the stored secret data in DataOS, you can reference them in your code using the secrets and dataosSecrets mechanisms. These identifiers ensure secure referencing of Secrets across different resources, enhancing system security and operational integrity.

The secrets identifier is used for creating a Secret in DataOS. However, it's important to note that you cannot use the same identifier to refer to pre-existing secrets in other Resources. For referencing secrets across various DataOS Resources, the dataosSecrets identifier is used.

**Syntax**

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


=== "In Service"

    In addition to serving as a conduit for real-time and streaming data exchanges, the [Service Resource](./service.md) within DataOS incorporates Secrets for secure access to confidential information. This ensures data privacy, and regulatory compliance, and facilitates timely insights and responses to dynamic information.


    === "Secret"
        ```yaml title="secret_service.yaml"
            --8<-- "examples/resources/secret/service/secret_service.yaml"
        ```

    === "Service"
        ```yaml title="service.yaml"
            --8<-- "examples/resources/secret/service/service.yaml"
        ```

=== "In Workflow"

    [Workflow](./workflow.md) often orchestrates various processes, involving different services and components, each requiring access to sensitive information such as API keys, authentication tokens, or database credentials. Instead of embedding these secrets directly in the workflow configuration, it is advisable to leverage references to the Secret Resources.

    === "Secret"
        ```yaml title="secret_workflow.yaml"
            --8<-- "examples/resources/secret/workflow/secret_workflow.yaml"
        ```

    === "Workflow"
        ```yaml title="workflow.yaml"
            --8<-- "examples/resources/secret/workflow/workflow.yaml"
        ```    

=== "In Worker"

    Within the framework of DataOS, a [Worker Resource](./worker.md) is defined as an enduring operation that systematically performs designated tasks or computations over a protracted duration. Workers are capable of securely accessing confidential information, such as API keys, through the referencing of secrets, thereby ensuring the safeguarding of sensitive data.

    === "Secret"
        ```yaml title="secret_worker.yaml"
            --8<-- "examples/resources/secret/worker/secret_worker.yaml"
        ```

    === "Worker"
        ```yaml title="worker.yaml"
            --8<-- "examples/resources/secret/worker/worker.yaml"
        ```

=== "In Cluster"

    A Cluster in DataOS is a Resource that encompasses a set of computational resources and configurations necessary for executing data engineering and analytics tasks. Clusters are capable of securely accessing confidential information through the referencing of secrets, thereby ensuring the safeguarding of sensitive data.
    
    === "Secret"
        ```yaml title="secret_cluster.yaml"
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


<aside class="callout">

🗣 When you use the `secrets` attribute, the encrypted secrets are visible during linting, which is a process to check for errors, but they remain visible to end-users. So, while they are encrypted, they can still be seen by people accessing the configuration.

On the other hand, if you use `dataosSecrets`, during linting, the secrets are completely hidden within the configuration. This provides a higher level of security and confidentiality because even during checks for errors, the secrets are not exposed.

This difference allows for precise control over how sensitive information is exposed within the configuration environment, ensuring that only authorized individuals can access it.

</aside>