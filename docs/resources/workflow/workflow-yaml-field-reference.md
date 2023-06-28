# Workflow YAML Field Reference

## Syntax

```yaml
workflow: #(Mandatory)
  schedule: #(Optional**)
    cron: ${'*/10 * * * *'} #(Optional**)
    concurrencyPolicy: ${Allow} #(Optional)
    startOn: ${2022-01-01T23:30:30Z} #(Optional)
    endOn: ${2022-01-01T23:40:45Z} #(Optional)
    completeOn: ${2022-01-01T23:30:45Z} #(Optional)
  dag: #(Mandatory)
    - name: ${job1-name} #(Mandatory)
      spec: #(Mandatory)
        stack: ${stack1:version} #(Mandatory)
        compute: ${compute-name} #(Mandatory)
        stack1: #(Mandatory)
          {stack1-specific-properties}
    - name: ${job2-name} #(Mandatory)
      spec: #(Mandatory)
        stack: ${stack2:version} #(Mandatory)
        compute: ${compute-name} #(Mandatory)
        stack2: #(Mandatory)
          {stack2-specific-properties}
      dependencies: #(Optional)
       - ${job1-name}
```

## Configuration Fields

### `workflow`
<b>Description:</b> Workflow Section <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
workflow: # Workflow Section
  schedule: # Schedule Section
    cron: '*/10 * * * *' # Cron Expression
  dag: # Directed Acyclic Graph (DAG)
    {} # Collection of Jobs
```

### `schedule`
<b>Description:</b> Schedule Section <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional (Mandatory for Scheduled Workflows) <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
schedule: # Schedule Section
  cron: '*/10 * * * *' # Cron Expression
  concurrencyPolicy: Forbid # Concurrency Policy
```

### `cron`
<b>Description:</b> The cron field encompasses the cron expression, a string that comprises six or seven sub-expressions providing specific details of the schedule. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional (Mandatory for Scheduled Workflows) <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any valid cron expression <br>
<b>Additional Details:</b> The cron expression consists of value separated by white spaces  <br>
<b>Example Usage:</b>
```yaml
cron: '*/10 * * * *' # Cron Expression
```

### `concurrencyPolicy`
<b>Description:</b> The concurrencyPolicy field determines how concurrent executions of a workflow, created by a cron workflow, are handled<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> Allow <br>
<b>Possible Value:</b> Allow/Forbid/Replace <br>
<b>Additional Details:</b> <br>
- <i> concurrencyPolicy: Forbid -</i> When the concurrencyPolicy is set to "Forbid", the cron workflow strictly prohibits concurrent runs. In this scenario, if it is time for a new workflow run and the previous workflow run is still in progress, the cron workflow will skip the new workflow run altogether.  <br>
- <i> concurrencyPolicy: Allow -</i> On the other hand, setting the concurrencyPolicy to "Allow" enables the cron workflow to accommodate concurrent executions. If it is time for a new workflow run and the previous workflow run has not completed yet, the cron workflow will proceed with the new workflow run concurrently.  <br>
- <i> concurrencyPolicy: Replace -</i> When the concurrencyPolicy is set to "Replace", the cron workflow handles concurrent executions by replacing the currently running workflow run with a new workflow run if it is time for the next job workflow and the previous one is still in progress.  <br>

<b>Example Usage:</b>
```yaml
concurrencyPolicy: Replace # Concurrency Policy
```

### `startOn`
<b>Description:</b> Specifies start time of a schedule in ISO 8601 format.<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any time provided in ISO 8601 format <br>
<b>Example Usage:</b>
```yaml
startOn: 2022-01-01T23:30:45Z # Start time of Scheduled Workflow Run
```

### `endOn`
<b>Description:</b> endOn terminates the scheduled workflow run at the specified time, even if the last workflow run isn’t complete <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any time provided in ISO 8601 format <br>
<b>Example Usage:</b>
```yaml
endOn: 2022-01-01T23:30:45Z # End time of Scheduled Workflow Run
```

### `completeOn`
<b>Description:</b> completeOn signifies successful completion. completeOn will let the last workflow run if it was triggered before the specified time <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any time provided in ISO 8601 format <br>
<b>Example Usage:</b>
```yaml
completeOn: 2022-01-01T23:30:45Z # Completion time of Scheduled Workflow Run
```

### `title`
<b>Description:</b> Title of Workflow <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string <br>
<b>Example Usage:</b>
```yaml
title: Quality Assessment Workflow # Title of the Workflow
```

### `dag`
<b>Description:</b> DAG is a Directed Acyclic Graph, a conceptual representation of a sequence of jobs (or activities). These jobs in a DAG are executed in the order of dependencies between them <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Additional Details:</b> There should be atleast one job within a DAG<br>
<b>Example Usage:</b>
```yaml
  dag: #(Mandatory) 
    - name: profiling-job # Name of the Job
      spec: # Specs of the Job
        stack: flare:4.0 # Stack
        compute: runnable-default # Compute
        flare: # Flare Stack Section
          {} # Flare Stack specific configurations
```

### `name`
<b>Description:</b> Name of the Job <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string confirming the regex `[a-z0-9]([-a-z0-9]*[a-z0-9])` and length less than or equal to 48<br>
<b>Example Usage:</b>
```yaml
name: flare-ingestion-job # Name of the Job
```

### `title`
<b>Description:</b> Title of Job <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string <br>
<b>Example Usage:</b>
```yaml
title: Profiling Job # Title of the Job
```

### `description`
<b>Description:</b> Text describing the Job <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string <br>
<b>Example Usage:</b>
```yaml
description: The job ingests customer data # Job Description
```

### `spec`
<b>Description:</b> Specs of the Job <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
spec: # Specs of the Job
  stack: flare:4.0 # Stack
  compute: runnable-default # Compute
  flare: # Flare Stack Section
    {} # Flare Stack specific configurations
```

### `runAsUser`
<b>Description:</b> When the "runAsUser" field is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> UserID of the Use Case Assignee <br>
<b>Example Usage:</b>
```yaml
runAsUser: iamgroot # Run as User Iamgroot
```

### `compute`
<b>Description:</b> A Compute resource provides processing power for the job.  <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> runnable-default or any other custom compute created by the user<br>
```yaml
compute: runnable-default # Compute Resource
```

### `stack`
<b>Description:</b> A Stack is a Resource that serves as a secondary extension point, enhancing the capabilities of a Workflow Resource by introducing additional programming paradigms.  <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> flare/toolbox/scanner/alpha. <br>
<b>Additional Details:</b> It is also possible to specify specific versions of the stack. For example, you can use the notation "flare:4.0" to indicate a specific version. If no version is explicitly specified, the system will automatically select the latest version as the default option <br>
<b>Example Usage:</b>
```yaml
stack: alpha # Stack Resource
```

### `retry`
<b>Description:</b> Retrying failed jobs  <br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
retry: # Retry Section
  count: 2 # Retry after counts
  strategy: "OnFailure" # Strategy
```

### `count`
<b>Description:</b> Count post which retry occurs  <br>
<b>Data Type:</b> Integer <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any positive integer <br>
<b>Example Usage:</b>
```yaml
count: 2 # Retry after counts
```

### `strategy`
<b>Description:</b> Strategies to choose which job failures to retry  <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Always/OnFailure/OnError/OnTransientError <br>
<b>Additional Details:</b> <br>
  - <i> Always -</i> Retry all failed steps.  <br>
  - <i> OnFailure -</i> Retry steps whose main container is marked as failed in Kubernetes (this is the default).  <br>
  - <i> OnError -</i> Retry steps that encounter errors or whose init or wait containers fail.  <br>
  - <i> OnTransientError -</i> Retry steps that encounter errors defined as transient or errors matching the `TRANSIENT_ERROR_PATTERN` environment variable.   <br>
<b>Example Usage:</b>
```yaml
strategy: "OnTransientError" # Retry Strategy
```
