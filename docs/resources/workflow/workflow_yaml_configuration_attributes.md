# Attributes of Workflow YAML Configuration

## Structure of a Workflow YAML

```yaml
workflow:
  title: {{title of workflow}}
  schedule: 
    cron: {{'*/10 * * * *'}}
    concurrencyPolicy: {{Allow}}
    startOn: {{2022-01-01T23:30:30Z}}
    endOn: {{2022-01-01T23:40:45Z}}
    completeOn: {{2022-01-01T23:30:45Z}}
  dag: 
    - name: {{job1-name}}
      description: {{description}}
      title: {{title of job}}
      tags:
        - {{tag1}}
        - {{tag2}}
      spec: 
        stack: {{stack1:version}}
        compute: {{compute-name}}
        stack1: 
          {{stack1-specific-properties}}
    - name: {{job2-name}}
      spec: 
        stack: {{stack2:version}}
        compute: {{compute-name}}
        stack2: 
          {{stack2-specific-properties}}
      dependencies: 
       - {{job1-name}}
```
<center><i> Structure of Workflow YAML configuration </i></center>

## Configuration Attributes

### **`workflow`**
<b>Description:</b> workflow section <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| mapping          | mandatory       | none              | none              |

<b>Example Usage:</b>

```yaml
workflow: 
  schedule: 
    cron: '*/10 * * * *' 
  dag: 
    {} # List of Jobs
```

---

### **`schedule`**
<b>Description:</b> schedule section <br>

| **Data Type**     | **Requirement**                          | **Default Value** | **Possible Value** |
|---------------|--------------------------------------|---------------|----------------|
| mapping       | optional (mandatory for <br>Scheduled Workflows) | none          | none           |

<b>Example Usage:</b>

```yaml
schedule: 
  cron: '*/10 * * * *' 
  concurrencyPolicy: Forbid 
```

---

### **`cron`**
<b>Description:</b> the cron field encompasses the cron expression, a string that comprises six or seven sub-expressions providing specific details of the schedule. <br>

| **Data Type** | **Requirement**                          | **Default Value** | **Possible Value**          |
|-----------|--------------------------------------|---------------|-------------------------|
| string    | optional (mandatory for<br> Scheduled Workflows) | none          | any valid cron expression |

<b>Additional Details:</b> the cron expression consists of value separated by white spaces  <br>
<b>Example Usage:</b>

```yaml
cron: '*/10 * * * *' 
```

---

### **`concurrencyPolicy`**
<b>Description:</b> the concurrencyPolicy field determines how concurrent executions of a Workflow, created by a scheduled Workflow, are handled<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ----------- | ------------- | --------------- | --------------- |
|    string     |    optional     |       Allow       | Allow/Forbid/Replace |

<b>Additional Details:</b> <br>
- <i> concurrencyPolicy: Forbid -</i> When the concurrencyPolicy is set to "Forbid", the Schedule/Cron Workflow strictly prohibits concurrent runs. In this scenario, if it is time for a new workflow run and the previous workflow run is still in progress, the cron workflow will skip the new workflow run altogether.  <br>
- <i> concurrencyPolicy: Allow -</i> On the other hand, setting the concurrencyPolicy to "Allow" enables the Schedule/Cron Workflow to accommodate concurrent executions. If it is time for a new workflow run and the previous workflow run has not completed yet, the cron workflow will proceed with the new workflow run concurrently.  <br>
- <i> concurrencyPolicy: Replace -</i> When the concurrencyPolicy is set to "Replace", the Schedule/Cron Workflow handles concurrent executions by replacing the currently running workflow run with a new workflow run if it is time for the next job workflow and the previous one is still in progress.  <br>

<b>Example Usage:</b>

```yaml
concurrencyPolicy: Replace 
```

---

### **`startOn`**
<b>Description:</b> specifies start time of a schedule in ISO 8601 format.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                  |
|-----------|-------------|---------------|---------------------------------|
| string    | optional    | none          | any time provided in ISO 8601 format |

<b>Example Usage:</b>
```yaml
startOn: 2022-01-01T23:30:45Z 
```

---

### **`endOn`**
<b>Description:</b> endOn terminates the scheduled Workflow run at the specified time, even if the last workflow run isn’t complete <br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                  |
|-----------|-------------|---------------|---------------------------------|
| string    | optional    | none          | any time provided in ISO 8601 format |

<b>Example Usage:</b>
```yaml
endOn: 2022-01-01T23:30:45Z 
```

---

### **`completeOn`**
<b>Description:</b> completeOn signifies successful completion. completeOn will let the last workflow run if it was triggered before the specified time <br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**            |
| ----------- | ------------- | --------------- | --------------------------- |
|    string     |    optional     |       none        | any time provided in ISO 8601 format |

<b>Example Usage:</b>
```yaml
completeOn: 2022-01-01T23:30:45Z 
```

---

### **`title`**
<b>Description:</b> title of Workflow <br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| string    | optional    | none          | any string     |

<b>Example Usage:</b>
```yaml
title: Quality Assessment Workflow 
```

---

### **`dag`**
<b>Description:</b> DAG is a Directed Acyclic Graph, a conceptual representation of a sequence of jobs (or activities). These jobs in a DAG are executed in the order of dependencies between them <br>

| **Data Type**        | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-------------|---------------|----------------|
| mapping          | mandatory   | none          | none           |

<b>Additional Details:</b> there should be atleast one job within a DAG<br>
<b>Example Usage:</b>
```yaml
dag: 
  - name: profiling-job 
    spec: 
      stack: flare:4.0 
      compute: runnable-default 
      flare: 
        {} # Flare Stack-specific attributes
```

---

### **`name`**
<b>Description:</b> name of the Job <br>

| **Data Type**        | **Requirement** | **Default Value** | **Possible Value**                                 |
|------------------|-------------|---------------|------------------------------------------------|
| string           | mandatory   | none          | any string confirming the regex<br> `[a-z0-9]([-a-z0-9]*[a-z0-9])` and <br>length less than or equal to 48 |

<b>Example Usage:</b>
```yaml
name: flare-ingestion-job 
```
---

### **`title`**
<b>Description:</b> title of Job <br>

| **Data Type**       | **Requirement** | **Default Value** | **Possible Value** |
|-----------------|-------------|---------------|----------------|
| string          | optional    | none          | any string     |

<b>Example Usage:</b>
```yaml
title: Profiling Job 
```
---

### **`description`**
<b>Description:</b> text describing the Job <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Value** |
|-------------|-------------|---------------|----------------|
| string      | optional    | none          | any string     |

<b>Example Usage:</b>
```yaml
description: The job ingests customer data 
```

---

### **`spec`**
<b>Description:</b> specs of the Job <br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| mapping   | mandatory   | none          | none           |

<b>Example Usage:</b>
```yaml
spec: 
  stack: flare:4.0 
  compute: runnable-default 
  flare: 
    {} # Flare Stack specific configurations
```

---

### **`runAsUser`**
<b>Description:</b> when the `runAsUser` field is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user. <br>

| **Data Type**       | **Requirement** | **Default Value** | **Possible Value**            |
|-----------------|-------------|---------------|---------------------------|
| string          | optional    | none          | userID of the Use <br>Case Assignee |

<b>Example Usage:</b>
```yaml
runAsUser: iamgroot 
```
---

### **`compute`**
<b>Description:</b> a Compute Resource provides processing power for the job.  <br>

| **Data Type**       | **Requirement** | **Default Value** | **Possible Value**                           |
|-----------------|-------------|---------------|------------------------------------------|
| string          | mandatory   | none          | runnable-default or any <br> other custom compute <br>created by the user |

<b>Example Usage:</b>
```yaml
compute: runnable-default 
```

---

### **`stack`**
<b>Description:</b> a Stack is a Resource that serves as a secondary extension point, enhancing the capabilities of a Workflow Resource by introducing additional programming paradigms.  <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Value**                         |
|-------------|-------------|---------------|----------------------------------------|
| string      | mandatory   | none          | flare/toolbox/scanner/alpha            |

<b>Additional Details:</b> it is also possible to specify specific versions of the Stack. For example, you can use the notation "flare:4.0" to indicate a specific version. If no version is explicitly specified, the system will automatically select the latest version as the default option <br>
<b>Example Usage:</b>
```yaml
stack: alpha 
```

---

### **`retry`**
<b>Description:</b> retrying failed jobs  <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Value** |
|-------------|-------------|---------------|----------------|
| mapping     | optional    | none          | none           |

<b>Example Usage:</b>

```yaml
retry: 
  count: 2 
  strategy: "OnFailure" 
```

---

### **`count`**
<b>Description:</b> count post which retry occurs  <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value**            |
|--------------|-------------|---------------|---------------------------|
| integer      | optional    | none          | any positive integer      |

<b>Example Usage:</b>

```yaml
count: 2 
```

---

### **`strategy`**
<b>Description:</b> strategies to choose which job failures to retry  <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Value**                     |
|-------------|-------------|---------------|------------------------------------|
| string      | optional    | none          | Always/OnFailure/<br>OnError/OnTransientError |

<b>Additional Details:</b> <br>
  - <i> Always -</i> Retry all failed steps.  <br>
  - <i> OnFailure -</i> Retry steps whose main container is marked as failed in Kubernetes (this is the default).  <br>
  - <i> OnError -</i> Retry steps that encounter errors or whose init or wait containers fail.  <br>
  - <i> OnTransientError -</i> Retry steps that encounter errors defined as transient or errors matching the `TRANSIENT_ERROR_PATTERN` environment variable.   <br>

<b>Example Usage:</b>

```yaml
strategy: "OnTransientError" 
```

---

### **`dependency`**
<b>Description:</b> specifies the dependency between jobs/Workflows  <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Value** |
|-------------|-------------|---------------|----------------|
| string      | optional    | none          | none           |

<b>Example Usage:</b>

```yaml
dependency: job2
```