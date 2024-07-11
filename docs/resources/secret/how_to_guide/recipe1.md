# How to refer Secrets in other DataOS Resources?

To refer the stored secret data in DataOS, you can reference them in your code using the `secrets` and `dataosSecrets` identifier. These identifiers ensure secure referencing of Secrets across different resources, enhancing system security and operational integrity.

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

    In addition to serving as a conduit for real-time and streaming data exchanges, the [Service Resource](/resourcesservice) within DataOS incorporates Secrets for secure access to confidential information. This ensures data privacy, and regulatory compliance, and facilitates timely insights and responses to dynamic information.


    === "Secret"
        ```yaml title="secret.yaml"
        --8<-- "examples/resources/secret/service/secret_service.yaml"
        ```

    === "Service"
        ```yaml title="service.yaml"
        --8<-- "examples/resources/secret/service/service.yaml"
        ```

=== "In Workflow"

    The [Workflow](/resourcesworkflow) in DataOS serves as a Resource for orchestrating data processing tasks with dependencies. It enables the creation of complex data workflows by defining a hierarchy based on a dependency mechanism some requiring access to sensitive information such as API keys, authentication tokens, or database credentials. Instead of embedding these secrets directly in the workflow configuration, it is advisable to leverage references to the Secret Resource.

    === "Secret"
        ```yaml title="secret.yaml"
        --8<-- "examples/resources/secret/workflow/secret_workflow.yaml"
        ```

    === "Workflow"
        ```yaml title="workflow.yaml"
        --8<-- "examples/resources/secret/workflow/workflow.yaml"
        ```    

=== "In Worker"

    A [Worker Resource](/resourcesworker) in DataOS is a long-running process responsible for performing specific tasks or computations indefinitely. Workers are capable of securely accessing confidential information, such as API keys, through the referencing of secrets, thereby ensuring the safeguarding of sensitive data.

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


