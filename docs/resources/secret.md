# Secret

In DataOS, a Secret resource serves as an entity for securely storing sensitive data such as usernames, passwords, certificates, tokens, or keys. The inclusion of such information directly in application code or configuration poses an exposure risk, which can be mitigated by using Secrets. Secrets facilitate the separation of sensitive data from resource definitions, thereby reducing accidental exposure during the creation, viewing, or editing of these resources and still allowing accessibility to the user as and when required.

Each Secret in DataOS is associated with a specific Workspace, thereby limiting its accessibility and application to that particular Workspace.

DataOS allows these Secrets to be referenced by other resources such as Depots, Stacks, Services, and more. When a Secret resource YAML is deployed via CLI, Poros, the resource manager, forwards it to Heimdall, the Governance Engine within DataOS. Heimdall provides vault support for Secrets and enables you to control access to secrets using fine-grained permissions whenever the users or applications want to retrieve credentials.

## Syntax of a Secret Resource

The YAML given below provides a definition of the Secret Resource.

```yaml
# Resource Section
version: v1 # Manifest Version
name: my-secret # Name of the Secret Resource
type: secret # Resource type here is Secret
description: Secret for the Developer Account # Description of the Secret

# Secret-specific Section
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
| version | string | None | v1 | Mandatory |
| name | string | None | Must conform to the regex [a-z0-9]([-a-z0-9]*[a-z0-9]), and length must be less than 47 characters. | Mandatory |
| type | string | None | secret | Mandatory |
| description | string | None | Any string | Optional |
| tags | list of strings | None | - developer | Optional |
| secret | object | None | None | Mandatory |
| type | string | None | cloud-kernel, cloud-kernel-image-pull,
key-value, key-value-properties,
certificates | Mandatory |
| data | object | None | None | Mandatory |

To dive deep into these configuration fields, click on the link below.

[Secret Resource YAML Configuration Field Reference](./secret/secret_resource_yaml_configuration_field_reference.md)

## Types of Secrets in DataOS

When creating a Secret resource, you can specify its type using the `type` field within the `secrets` section. The Secret type is used to facilitate programmatic handling of the Secret data.

DataOS provides several built-in types for some common usage scenarios. These types vary in terms of the validations performed and the constraints DataOS imposes on them.

| Secret Type | Usage |
| --- | --- |
| cloud-kernel | This type stores arbitrary user-defined data in the form of key-value pair as a Kubernetes Secret with the same name as the Secret resource in the same Workspace. |
| cloud-kernel-image-pull | This type retains credentials needed for pulling images from a private Docker container registry. |
| certificates | This is a secret type used to securely store certificates, which are often necessary for secured communication in the system.  |
| key-value-properties | This type conserves arbitrary user-defined data as a Secret by transforming multiple key-value pairs into a singular key-value pair, which is then encoded in base64 format. |
| key-value | This type stores arbitrary user-defined data as key-value pairs within a Secret, with each pair being encoded separately in base64 format. |

For a more detailed analysis of each type and to explore the syntax, please follow the link below.

[Types of Secret Resources ](./secret/types_of_secret_resources.md)

## Governance of Secrets

Various use cases are tied to the Secret Resource as outlined in the following table:

| Use Case | Subjects |
| --- | --- |
| Create or Update Secrets | • roles:id:operator
• users:id:dataos-maintenance-manager |
| Read Secrets | • roles:id:operator
• users:id:depot-service
• users:id:metis
• users:id:dataos-resource-manager
• users:id:dataos-maintenance-manager |
| Read Stack Secrets | • roles:id:operator
• roles:id:system-dev
• roles:id:data-dev |
| Read Specific Secrets (Icebase Read, Dropzone01 Read, and Container Registry User Pass) | • roles:id:system-dev
• roles:id:data-dev |

## Creating Secrets

Unleash the power of secrecy by crafting your very own "Secret" resource using the sacred language of YAML. Once your secret recipe is complete, bring it to life by applying it from CLI using the `apply` command. To learn more about creating secrets, click on the link below. 

[Creating Secrets](./secret/creating_secrets.md)

## Referencing Secrets

To access the mystical data stored within your secrets, simply reference them in your code. DataOS provides separate mechanisms like `secrets` and `dataosSecrets` for creating and referring secrets. These identifiers allow for secure referencing of secrets across resources, further reinforcing system security and operational integrity. To know more, click on the link below.

[Referencing Secrets ](./secret/referencing_secrets.md)