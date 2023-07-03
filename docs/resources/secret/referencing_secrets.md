# Referencing Secrets

Secrets in DataOS are a way to manage sensitive information like passwords, tokens, or keys, which are crucial in any application setup but risky if mishandled. They are an essential part of ensuring the security and integrity of your applications and workflows. This guide aims to provide you with detailed instructions and code samples on how to reference these secrets effectively and safely within your DataOS system.

The `secrets` identifier serves as a mechanism for creating a secret in DataOS. Nevertheless, it's important to emphasize that you cannot use the same identifier to refer to the pre-created secrets in other resources. For the purpose of referencing secrets across various resources in DataOS, the `dataosSecrets` identifier is utilized. 

## Referencing Secrets using the `dataosSecrets` Identifier

```yaml
dataosSecrets:
	- <name-of-the-secret>
```

Here is a YAML sample that demonstrates how to reference a Secret resource using `dataosSecrets` field.

```yaml
version: v1
name: hello
type: service
service:
  compute: runnable-default
  title: Hello UI
  replicas: 1
  servicePort: 80
# Referencing Secret Resource in other Resources using **'dataosSecrets'** field
  dataosSecrets:
    - testing             # secret name
  stack: alpha
  envs:
    LOG_LEVEL: info
  alpha:
    image: cheesy/saucy:latest
```

We use the `dataosSecrets` identifier while referencing secrets within other resources in the system.

### **Referencing a Secret in a Depot**

In DataOS, you can easily reference a Secret within a Depot, effectively enhancing the security and manageability of sensitive data such as credentials. For detailed steps and code samples on how to reference a Secret in a Depot, please refer to the page below.

[Referencing Secrets in Depots](./referencing_secrets/referencing_secrets_in_depots.md)

### **Referencing a Secret in a Service**

Referencing a Secret in a Service resource ensures that sensitive data is safely accessed by the necessary services. The link below explains the procedure, including sample code snippets.

[Referencing Secrets in a Service](./referencing_secrets/referencing_secrets_in_a_service.md)

### **Referencing Secrets in Workflows**

This functionality allows the incorporation of secrets into your workflows. To know more, click on the link below.

[Referencing Secrets in Workflows](./referencing_secrets/referencing_secrets_in_workflows.md)

### **Referencing Secrets to Pull Images from Private Container Registry**

When deploying applications in a containerized environment, you may need to pull images from a private container registry. In DataOS, you can safely handle authentication to private registries by referencing Secrets. The Secret resource stores your registry credentials securely, ensuring that sensitive data remains confined and not exposed in application configurations. For detailed instructions, please refer to the link below.

[Referencing Secrets to Pull Images from Private Container Registry](./referencing_secrets/referencing_secrets_to_pull_images_from_private_container_registry.md)