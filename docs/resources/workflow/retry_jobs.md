# Retrying Failed Jobs within Workflows

This documentation provides information on retrying failed Jobs within Workflows, offering various strategies to handle failures effectively.

To apply a retry strategy to a Job within a Workflow, use the following YAML configuration:

```yaml
retry:
  count: {{retry count}}
  strategy: {{retry strategy}} # Possible Strategies: Always/OnFailure/OnError/OnTransientError
```

## Retry Strategies

To counter the scenario of failed job within a Workflow, following retry strategies can be employed:

### **`OnFailure`** 

This strategy involves retrying steps whose main container is marked as failed in Kubernetes. It is the default strategy when no other option is specified.

### **`Always`**

With this strategy, all steps that encounter failure will be retried.

### **`OnError`**

Retry steps that encounter errors or whose init or wait containers fail.

### **`OnTransientError`**

This strategy retries steps that encounter errors defined as transient or errors matching the `TRANSIENT_ERROR_PATTERN` environment variable.

## Examples

Below are two examples demonstrating the use of retry strategies in Workflow configurations.

### **Example 1**

```yaml
name: demo-retry
version: v1
type: workflow
tags:
  - Flare
description: Ingest data into Raw depot
workflow:
  title: Demo Ingest Pipeline
  dag:
    - name: connect-customer
      file: flare/connect-customer/config_v1.yaml
      retry:
        count: 2
        strategy: "OnFailure"
    - name: connect-customer-dt
      file: flare/connect-customer/dataos-tool_v1.yaml
      dependencies:
        - connect-customer
```

### **Example 2**

```yaml
version: v1
name: c360-daggy
type: workflow
tags:
- Flare
description: Ingest data into Raw depot
workflow:
  title: TWT Demo Ingest Pipeline
  dag:
  - name: connect-customer
    file: flare/connect-customer/configv1.yaml
    retry:
      count: 2
      strategy: "OnTransientError"
  - name: connect-customer-dt
    file: flare/connect-customer/dataos-tool_v1.yaml
    dependencies:
      - connect-customer
  - name: connect-city
    file: flare/connect-city/config_v1.yaml
    retry:
      count: 2
      strategy: "OnTransientError"
```


