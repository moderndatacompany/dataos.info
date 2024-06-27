# How to refer Instance Secret in other DataOS Resources?

To access the stored secret data in DataOS, you can reference them in your code using the `dataosSecrets` attribute. This identifier ensures secure referencing of Instance Secrets for various resources, enhancing system security and operational integrity.

## **Referring Instance Secret in Depot**

To refer to an instance-secret in Depots, follow these steps:

1. **Ensure Creation of Instance-Secret:** First, make sure you have created the respective instance-secrets.

2. **Use `dataosSecrets` Identifier:** In the depot manifest, use the `dataosSecrets` identifier to refer to the instance-secret.

For read-only access to a depot, create read-only secrets. For read-write access, create both read and read-write instance-secrets. This is necessary because when providing someone else access to the Depot, you can grant either read or read-write access using either CLI or Bifrost UI. For either type of access, the person will have access to the respective instance-secret.

=== "Read-only Instance Secret"

    ```yaml title="read_instance_secret.yaml"
    --8<-- "examples/resources/instance_secret/referencing_instance_secret_in_depot/sample_secret_r.yaml"
    ```

=== "Read-write Instance Secret"

    ```yaml title="read_write_instance_secret.yaml"
    --8<-- "examples/resources/instance_secret/referencing_instance_secret_in_depot/sample_secret_rw.yaml"
    ```

    Now while creating the manifest file for your Depot, ensure to include a reference to the Instance Secret using the `dataosSecrets` identifier, instead of directly specifying the secret using the `connectionSecrets` attribute:

=== "Depot"

    ```yaml title="depot.yaml"
    --8<-- "examples/resources/instance_secret/referencing_instance_secret_in_depot/sample_depot.yaml"
    ```

<aside class="callout">

🗣️ To ensure controlled access for read-write, it is essential to create two Instance Secrets: one with acl:r for read-only access and another with acl:rw for both read and write access and refer to both Instance-Secrets in a Depot as shown above. This enables precise management of permissions for different levels of access.

</aside>

## **Refering Instance Secret in Workflow**

