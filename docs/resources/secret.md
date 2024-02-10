# Secret

In DataOS, a Secret [Resource](../resources.md) serves as an entity for securely storing sensitive data such as usernames, passwords, certificates, tokens, or keys. The inclusion of such information directly in application code or configuration poses an exposure risk, which can be mitigated by using Secrets. Secrets facilitate the separation of sensitive data from Resource definitions, thereby reducing accidental exposure during the creation, viewing, or editing of these Resources and still allowing accessibility to the user as and when required.

Each Secret in DataOS is associated with a specific Workspace, thereby limiting its accessibility and application to that particular Workspace.

DataOS allows these Secrets to be referenced by other resources such as [Depots](./depot.md), [Stacks](./stacks.md), [Services](./service.md), and more. When a Secret Resource YAML is deployed via CLI, Poros, the Resource manager, forwards it to Heimdall, the Governance Engine within DataOS. Heimdall provides vault support for Secrets and enables you to control access to secrets using fine-grained permissions whenever the users or applications want to retrieve credentials.

## Syntax of a Secret YAML

The YAML given below provides a definition of the Secret Resource.

```yaml
secret:
  type: key-value # Type of Secret
  acl: rw    # Access Control List (ACL) can be r|rw
  data: # Data Section
    username: developer # Key-Value Pair
    password: iamgroot # Key-Value Pair
```

## Secret YAML Configuration Fields

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`secret`](./secret/secret_specific_section_grammar.md#secret) | object | none | none | mandatory |
| [`type`](./secret/secret_specific_section_grammar.md#type) | string | none | cloud-kernel, cloud-kernel-image-pull, key-value, key-value-properties, certificates | mandatory |
| [`data`](./secret/secret_specific_section_grammar.md#data) | object | none | none | mandatory |

To dive deep into these configuration fields, refer to [Secret-specific Section Grammar.](./secret/secret_specific_section_grammar.md)

## Types of Secrets in DataOS

When creating a Secret Resource, you can specify its type using the `type` field within the `secrets` section. The Secret type is used to facilitate programmatic handling of the Secret data.

DataOS provides several built-in types for some common usage scenarios. These types vary in terms of the validations performed and the constraints DataOS imposes on them.

| Secret Type | Usage |
| --- | --- |
| [`cloud-kernel`](./secret/types_of_secret_resources.md#cloud-kernel) | This type stores arbitrary user-defined data in the form of key-value pair as a Kubernetes Secret with the same name as the Secret Resource in the same Workspace. |
| [`cloud-kernel-image-pull`](./secret/types_of_secret_resources.md#cloud-kernel-image-pull) | This type retains credentials needed for pulling images from a private Docker container registry. |
| [`certificates`](./secret/types_of_secret_resources.md#certificate) | This is a secret type used to securely store certificates, which are often necessary for secured communication in the system.  |
| [`key-value-properties`](./secret/types_of_secret_resources.md#key-value-properties) | This type conserves arbitrary user-defined data as a Secret by transforming multiple key-value pairs into a singular key-value pair, which is then encoded in base64 format. |
| [`key-value`](./secret/types_of_secret_resources.md#key-value) | This type stores arbitrary user-defined data as key-value pairs within a Secret, with each pair being encoded separately in base64 format. |

For a more detailed analysis of each type and to explore the syntax, please follow the link below.

[Types of Secret Resources ](./secret/types_of_secret_resources.md)

## Creating Secrets

To create a Secret Resource in DataOS, you can define the secret in a YAML file and then create the Resource-instance using the `apply` command in the CLI.

### **Create a YAML File for the Secret Resource**

The YAML configuration file for a Secret can be divided into two sections: Resource Section, and Secret-specific Section. Each section serves a distinct purpose and contains specific attributes and fields.

#### **Configure Resource Section**

The Resource Section of the YAML configuration file consists of attributes that are common across all Resource-types. The following YAML snippet demonstrates the key-value properties that need to be declared in this section:

```yaml
name: ${{mysecret}}
version: v1 
type: depot 
tags: 
  - ${{dataos:type:resource}}
description: ${{This is a sample secret YAML configuration}} 
owner: ${{iamgroot}}
```
For more information about the attributes of Resource Section, refer to the link [Attributes of Resource section.](../resources/resource_attributes.md)

#### **Configure Secret-specific Section**

The Secret-specific Section of the YAML configuration file includes key-value properties specific to the type of Secret being created. The following YAML snippet illustrates the key-values to be declared in this section:

```yaml
secret: 
  type: key-value 
  acl: r 
  data: 
    username: iamgroot 
    password: asgard@thor
```

### **Apply the Secret YAML**

Apply the Secret YAML via the CLI, by specifying the YAML’s path and the workspace. The `apply` command is given below.

```shell
dataos-ctl apply -f ${{path/secret.yaml}} -w ${{name of the workspace}}
```

**Expected Output**

```shell
dataos-ctl apply -f Desktop/mysecret.yaml -w public
# Expected Output
INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying(public) testing:v1:secret... 
INFO[0007] 🔧 applying(public) testing:v1:secret...created 
INFO[0007] 🛠 apply...complete
```

### **Validate the Resource**

Use the get command to validate whether, the Secret Resource has been properly created within the DataOS environment.

```shell
dataos-ctl get -t secret -w ${{workspace}}
```

**Sample**

```shell
dataos-ctl get -t secret -w public
# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

       NAME       | VERSION |  TYPE  | WORKSPACE | STATUS | RUNTIME |    OWNER     
------------------|---------|--------|-----------|--------|---------|--------------
     testing      |   v1    | secret | public    | active |         |   iamgroot
```

## Governance of Secrets

Various use cases are tied to the Secret Resource as outlined in the following table:

| Use Case | Subjects |
| --- | --- |
| Create or Update Secrets | • roles\:id\:operator<br>• users\:id\:dataos-maintenance-manager |
| Read Secrets | • roles\:id\:operator<br>• users\:id\:depot-service<br>• users\:id\:metis<br>• users\:id\:dataos-resource-manager<br>• users\:id\:dataos-maintenance-manager |
| Read Stack Secrets | • roles\:id\:operator<br>• roles\:id\:system-dev<br>• roles\:id\:data-dev |
| Read Specific Secrets (Icebase Read, Dropzone01 Read, and Container Registry User Pass) | • roles\:id\:system-dev<br>• roles\:id\:data-dev |

## Referencing Secrets

To access the stored secret data in DataOS, you can reference them in your code using the `secrets` and `dataosSecrets` mechanisms. These identifiers ensure secure referencing of Secrets across different resources, enhancing system security and operational integrity.

The `secrets` identifier is used for creating a Secret in DataOS. However, it's important to note that you cannot use the same identifier to refer to pre-existing secrets in other Resources. For referencing secrets across various DataOS Resources, the `dataosSecrets` identifier is used.

To reference a Secret Resource using the `dataosSecrets` field, use the following YAML syntax:

```yaml
dataosSecrets:
  - ${{name-of-the-secret}}
```

Here's a sample YAML configuration that demonstrates how to reference a Secret Resource using the `dataosSecrets` field:

<details>
<summary>YAML Configuration for `dataosSecrets` field</summary>

```yaml
version: v1
name: hello
type: service
service:
  compute: runnable-default
  title: Hello UI
  replicas: 1
  servicePort: 80
  dataosSecrets:
    - testing             # secret name
  stack: alpha
  envs:
    LOG_LEVEL: info
  alpha:
    image: cheesy/saucy:latest
```

The `dataosSecrets` identifier is used to reference secrets within other resources in DataOS.

</details>

#### **Referencing a Secret in a Depot**

In DataOS, you can reference a Secret within a Depot, enhancing the security and manageability of sensitive data such as credentials. For detailed steps and code samples on referencing a Secret in a Depot, please refer to the documentation page: [Referencing Secrets in Depots](./secret/referencing_secrets/referencing_secrets_in_depots.md).

### **Referencing a Secret in a Service**

Referencing a Secret in a Service Resource ensures secure access to sensitive data by the necessary services. For instructions and code snippets on referencing a Secret in a Service, please visit the page: [Referencing Secrets in a Service](./secret/referencing_secrets/referencing_secrets_in_a_service.md).

### **Referencing Secrets in Workflows**

DataOS allows the incorporation of Secrets into Workflows. To learn more about referencing Secrets in Workflows, refer to the page: [Referencing Secrets in Workflows](./secret/referencing_secrets/referencing_secrets_in_workflows.md).

### **Referencing Secrets to Pull Images from Private Container Registry**

When deploying applications in a containerized environment, you may need to pull images from a private container registry. DataOS enables secure authentication to private registries by referencing Secrets. The Secret Resource stores registry credentials securely, preventing sensitive data exposure in application configurations. For detailed instructions, please refer to the page: [Referencing Secrets to Pull Images from Private Container Registry](./secret/referencing_secrets/referencing_secrets_to_pull_images_from_private_container_registry.md).