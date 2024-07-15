# Retrying Failed Jobs within Workflows

This documentation provides information on retrying failed Jobs within Workflows, offering various strategies to handle failures effectively.

To apply a retry strategy to a Job within a Workflow, use the following YAML configuration:

=== "Command"

    ```yaml
    retry:
      count: {{retry count}}
      strategy: {{retry strategy}} # Possible Strategies: Always/OnFailure/OnError/OnTransientError
    ```
=== "Command"

    ```yaml
    retry:
      count: 2
      strategy: OnFailure # Possible Strategies: Always/OnFailure/OnError/OnTransientError
    ```

## Retry Strategies

To counter the scenario of failed job within a Workflow, following retry strategies can be employed:

### **`OnFailure`** 

This strategy involves retrying steps whose main container is marked as failed in Kubernetes. It is the **default** strategy when no other option is specified.

### **`Always`**

With this strategy, all steps that encounter failure will be retried.

### **`OnError`**

Retry steps that encounter errors or whose init or wait containers fail.

### **`OnTransientError`**

This strategy retries steps that encounter errors defined as transient or errors matching the `TRANSIENT_ERROR_PATTERN` environment variable.

## Examples

Below are two examples demonstrating the use of retry strategies in Workflow configurations.

<details><summary>Click here to view example manifest</summary>

<b>Example 1</b>

```yaml
# Resource Section
name: demo-retry
version: v1
type: workflow
tags:
  - Flare
description: Ingest data into Raw depot

# Workflow-specific Section
workflow:
  title: Demo Ingest Pipeline
  dag:

# Job 1 specific Section
    - name: connect-customer
      file: flare/connect-customer/config_v1.yaml
      retry: # Retry configuration
        count: 2
        strategy: "OnFailure"

# Job 2 specific Section
    - name: connect-customer-dt
      file: flare/connect-customer/dataos-tool_v1.yaml
      dependencies:
        - connect-customer
```

<b>Example 2</b>

```yaml
# Resource Section
name: c360-daggy
version: v1
type: workflow
tags:
- Flare
description: Ingest data into Raw depot

# Workflow-specific Section
workflow:
  title: TWT Demo Ingest Pipeline
  dag:

# Job 1 specific Section
  - name: connect-customer
    file: flare/connect-customer/configv1.yaml
    retry: # Retry configuration
      count: 2
      strategy: "OnTransientError"

# Job 2 specific Section
  - name: connect-customer-dt
    file: flare/connect-customer/dataos-tool_v1.yaml
    dependencies:
      - connect-customer
```
</details>


