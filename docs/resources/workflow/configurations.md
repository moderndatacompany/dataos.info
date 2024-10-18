# Attributes of Workflow YAML Configuration

## Structure of a Workflow manifest

```yaml title="worker_manifest_reference.yml"
--8<-- "examples/resources/workflow/manifest_reference.yml"
```

<center><i> Structure of Workflow YAML configuration </i></center>

## Configuration

### **Resource meta section**

This section serves as the header of the manifest file, defining the overall characteristics of the Worker Resource you wish to create. It includes attributes common to all types of Resources in DataOS. These attributes help DataOS in identifying, categorizing, and managing the Resource within its ecosystem. To learn about the Resources of this section, refer to the following link: [Attributes of Resource meta section]().

### **Workflow-specific Section**

This section comprises attributes specific to the Workflow Resource. The attributes within the section are listed below:


##### **`workflow`**
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

##### **`title`**
<b>Description:</b> Title of Workflow <br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| string    | optional    | none          | any string     |

<b>Example Usage:</b>

```yaml
title: Quality Assessment Workflow 
```

---

##### **`schedule`**
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

##### **`cron`**
<b>Description:</b> the cron field encompasses the <a href="https://en.wikipedia.org/wiki/Cron">cron expression</a>, a string that comprises six or seven sub-expressions providing specific details of the schedule. <br>

| **Data Type** | **Requirement**                          | **Default Value** | **Possible Value**          |
|-----------|--------------------------------------|---------------|-------------------------|
| string    | optional (mandatory for <br>[Scheduled Workflows](/resources/workflow/#scheduled-workflow)) | none          | any valid cron expression |

<b>Additional Details:</b> the cron expression consists of value separated by white spaces, make sure there are no formatting issues.<br>
<b>Example Usage:</b>

```yaml
cron: '*/10 * * * *' 
```

---

##### **`concurrencyPolicy`**

<b>Description:</b> the <code>concurrencyPolicy</code> attribute determines how concurrent executions of a Workflow, created by a scheduled Workflow, are handled<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ----------- | ------------- | --------------- | --------------- |
|    string     |    optional     |       Allow       | Allow/Forbid/Replace |

<b>Additional Details:</b> <br>

- <i> <code>concurrencyPolicy: Forbid</code> -</i> When the <code>concurrencyPolicy</code> is set to <code>Forbid</code>, the Schedule/Cron Workflow strictly prohibits concurrent runs. In this scenario, if it is time for a new Workflow run and the previous Workflow run is still in progress, the cron Workflow will skip the new Workflow run altogether.  <br>
- <i> <code>concurrencyPolicy: Allow</code> -</i> On the other hand, setting the <code>concurrencyPolicy</code> to <code>Allow</code> enables the Schedule/Cron Workflow to accommodate concurrent executions. If it is time for a new Workflow run and the previous Workflow run has not completed yet, the cron Workflow will proceed with the new Workflow run concurrently.  <br>
- <i> <code>concurrencyPolicy: Replace</code> -</i> When the <code>concurrencyPolicy</code> is set to <code>Replace</code>, the Schedule/Cron Workflow handles concurrent executions by replacing the currently running Workflow run with a new Workflow run if it is time for the next job Workflow and the previous one is still in progress.  <br>

<b>Example Usage:</b>

```yaml
concurrencyPolicy: Replace 
```

---

##### **`endOn`**

<b>Description:</b> <code>endOn</code> terminates the scheduled Workflow run at the specified time, even if the last workflow run that got triggered before the threshold time isn’t complete <br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                  |
|-----------|-------------|---------------|---------------------------------|
| string    | optional    | none          | any time provided in ISO 8601 format |





**Example Usage:**

The timestamp 2022-01-01T23:30:45Z follows the ISO 8601 format:

- Date: 2022-01-01 (`YYYY-MM-DD`)
- T: Separator indicating the start of the time portion in the datetime string.
- Time: 23:30:45 (`hh:mm:ss`)
- Timezone: Z (UTC)
- Z: Indicates the time is in Coordinated Universal Time (UTC), also known as Zulu time.

It represents `January 1, 2022, at 23:30:45 UTC`.

```yaml
endOn: 2022-01-01T23:30:45Z 
```

---

##### **`timezone`**

**Description:** Time zone for scheduling the workflow.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Asia/Kolkata, America/Los_Angeles, etc |

**Example Usage:**

```yaml
timezone: Asia/Kolkata
```

---


##### **`dag`**

<b>Description:</b> DAG is a <a href="/resources/workflow/core_concepts/#workflow-and-directed-acyclic-graph-dag">Directed Acyclic Graph</a>, a conceptual representation of a sequence of jobs (or activities). These jobs in a DAG are executed in the order of dependencies between them. <br>

| **Data Type**        | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-------------|---------------|----------------|
| mapping          | mandatory   | none          | none           |

<b>Additional Details:</b> there should be atleast one job within a DAG<br>
<b>Example Usage:</b>

```yaml
dag: 
  - name: profiling-job 
    spec: 
      stack: flare:5.0 
      compute: runnable-default 
      stackSpec: 
        {} # Flare Stack-specific attributes
```

---

##### **`name`**
<b>Description:</b> name of the Job <br>

| **Data Type**        | **Requirement** | **Default Value** | **Possible Value**                                 |
|------------------|-------------|---------------|------------------------------------------------|
| string           | mandatory   | none          | any string confirming the regex<br> `[a-z0-9]([-a-z0-9]*[a-z0-9])` and <br>length less than or equal to 48 |

<b>Example Usage:</b>
```yaml
name: flare-ingestion-job 
```

---

##### **`title`**
<b>Description:</b> title of Job <br>

| **Data Type**       | **Requirement** | **Default Value** | **Possible Value** |
|-----------------|-------------|---------------|----------------|
| string          | optional    | none          | any string     |

<b>Example Usage:</b>
```yaml
title: Profiling Job 
```
---

##### **`description`**

<b>Description:</b> text describing the Job <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Value** |
|-------------|-------------|---------------|----------------|
| string      | optional    | none          | any string     |

<b>Example Usage:</b>

```yaml
description: The job ingests customer data 
```

---

##### **`tags`**

**Description:** tags associated with the Workflow.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | valid [tags](/resources/policy/configurations/#tags) |

**Example Usage:**


```yaml
tags:
  - tag1
  - tag2
``` 

---

##### **`gcWhenComplete`**

**Description:** tags associated with the Workflow.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | valid [tags](/resources/policy/configurations/#tags) |

**Example Usage:**

```yaml
  tags:
    - tag1
    - tag2
```

---

##### **`spec`**
<b>Description:</b> Specs of the Job. <br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| mapping   | mandatory   | none          | none           |

<b>Example Usage:</b>

```yaml

spec: 
  stack: flare:5.0 
  compute: runnable-default 
  stackSpec: 
    {} # Flare Stack specific configurations

```

---

##### **`stack`**

**Description:** The name and version of the [Stack](/resources/stacks/) Resource which the Workflow orchestrates.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | flare/toolBox/scanner/dataos-ctl/soda+python/steampipestack |

**Additional Details:**
To know more about each stack, go to [Stack](/resources/stacks/).

**Example Usage:**

```yaml
  stack: flare

```

---

##### **`logLevel`**

**Description:**  The log level for the Service classifies entries in logs in terms of urgency which helps to filter logs during search and helps control the amount of information in logs.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | INFO | INFO, WARN, DEBUG, ERROR |

**Additional Details:** 

- `INFO`: Designates informational messages that highlight the progress of the service.

- `WARN`: Designates potentially harmful situations.

- `DEBUG`: Designates fine-grained informational events that are most useful while debugging.

- `ERROR`: Designates error events that might still allow the workflow to continue running.

**Example Usage:**

```yaml
workflow:
	logLevel: DEBUG
```

---


##### **`configs`**

**Description:** additional optional configuration for the service.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | key-value configurations |

**Example Usage:**

```yaml
configs:
  key1: value1
  key2: value2
```

---


##### **`envs`**

**Description:** environment variables for the Workflow.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | key-value configurations |

**Example Usage:**

```yaml
envs:
  DEPOT_SERVICE_URL: http://depotservice-api.depot.svc.cluster.local:8000/ds/
  HTTP_CONNECT_TIMEOUT_MS: 60000
  HTTP_SOCKET_TIMEOUT_MS: 60000
```

**Additional Details:**

- **DEPOT_SERVICE_URL**: Specifies the base URL for the Depot Service API. This is the endpoint that the service interacts with for managing Depots.
- **HTTP_CONNECT_TIMEOUT_MS**: Defines the connection timeout for HTTP requests, in milliseconds. If a connection to a remote server cannot be established within this timeframe (60 seconds in this case), the request will timeout. This ensures that the workload does not hang indefinitely while attempting to connect.
- **HTTP_SOCKET_TIMEOUT_MS**: Sets the socket timeout for HTTP requests, in milliseconds. This controls the maximum time that the service will wait for data after a connection has been established. If data is not received from the connected server within this period (60 seconds), the request will timeout. This helps prevent long delays in response handling when waiting for data transfer.

---

##### **`secrets`**

**Description:** list of secrets associated with the Workflow.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | none |

**Example Usage:**

```yaml
secrets:
  - mysecret
```

---


##### **`dataosSecrets`**

**Description:** list of [DataOS Secrets](/resources/secret/) associated with the Workflow. Each DataOS Secret is a mapping containing various attributes.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | none |

**Example Usage:**

```yaml
workflow:
  dataosSecrets:
    - name: mysecret
      workspace: curriculum
      key: newone
      keys:
        - newone
        - oldone
      allKeys: true
      consumptionType: envVars
```

---


##### **`dataosVolumes`**

**Description:** list of DataOS Volumes associated with the Workflow. Each DataOS Volume is a mapping containing various attributes.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | none |

**Example Usage:**

```yaml
dataosVolumes:
  - name: myVolume
    directory: /file
    readOnly: true
    subPath: /random
```

---

##### **`tempVolume`**

**Description:** The temporary volume of the Workflow.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid Volume name |

**Example Usage:**

```yaml
tempVolume: abcd
```

---

##### **`persistentVolume`**

**Description:** configuration for the persistent volume associated with the Workflow.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml

  persistentVolume:
    name: myVolume
    directory: /file
    readOnly: true
    subPath: /random
```

---

##### **`compute`**

**Description:** the name of the [Compute](/resources/compute/) Resource for the Workflow.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid runnable-type Compute Resource name. |

**Example Usage:**

```yaml

  compute: MyComputeResource
```

---

##### **`resources`**

**Description:** Resource requests and limits for the Workflow. This includes CPU and memory specifications.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml

  resources:
    requests:
      cpu: 100Mi
      memory: 100Gi
    limits:
      cpu: 100Mi
      memory: 100Gi
```

---

##### **`dryRun`**

**Description:** Indicates whether the workflow is in dry run mode. When enabled, the dryRun property deploys the Workflow to the cluster without submitting it.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| boolean | optional | true | true or false. |

**Example Usage:**

```yaml

  dryRun: true
```

---

##### **`runAsUser`**

<b>Description:</b> when the <code>runAsUser</code> attribute is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user. <br>

| **Data Type**       | **Requirement** | **Default Value** | **Possible Value**            |
|-----------------|-------------|---------------|---------------------------|
| string          | optional    | none          | userID of the Use <br>Case Assignee |

<b>Example Usage:</b>
```yaml
runAsUser: iamgroot 
```

---

##### **`runAsApiKey`**

**Description:** The runAsApiKey attribute allows a user to assume another user's identity by providing the latter's API key.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid API key. |

**Additional Details:** The apikey can be obtained by executing the following command from the CLI:

`dataos-ctl user apikey get`

In case no apikey is available, the below command can be run to create a new apikey

`dataos-ctl user apikey create -n ${{name of the apikey}} -d ${{duration for the apikey to live}}`

**Example Usage:**

```yaml
runAsApiKey: abcdefghijklmnopqrstuvwxyz
```

---

##### **`topology`**

**Description:** The `topology` attribute is used to define the topology of the Workflow. It specifies the elements and dependencies within the Workflow's topology.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | list of topology element definitions |

**Example Usage:**

```yaml
topology:
  - name: random            # mandatory
    type: alpha             # mandatory
    doc: new                # Documentation for the element
    properties:
      random: lost          # Custom properties for the element
    dependencies:
      - new1
      - new2
```

---

##### **`file`**

<b>Description:</b> attribute for specifying the file path for a Workflow YAML  <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Value** |
|-------------|-------------|---------------|----------------|
| string      | optional    | none          | none           |

<b>Example Usage:</b>

```yaml
file: workflow/new/random.yaml
```

---

##### **`retry`**
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

##### **`count`**
<b>Description:</b> count post which retry occurs  <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value**            |
|--------------|-------------|---------------|---------------------------|
| integer      | optional    | none          | any positive integer      |

<b>Example Usage:</b>

```yaml
count: 2 
```

---

##### **`strategy`**
<b>Description:</b> strategies to choose which job failures to retry  <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Value**                     |
|-------------|-------------|---------------|------------------------------------|
| string      | optional    | none          | Always/OnFailure/<br>OnError/OnTransientError |

<b>Additional Details:</b> <br>
  - <i> <code>Always</code> -</i> Retry all failed steps.  <br>
  - <i> <code>OnFailure</code> -</i> Retry steps whose main container is marked as failed in Kubernetes (this is the default).  <br>
  - <i> <code>OnError</code> -</i> Retry steps that encounter errors or whose init or wait containers fail.  <br>
  - <i> <code>OnTransientError</code> -</i> Retry steps that encounter errors defined as transient or errors matching the <code>TRANSIENT_ERROR_PATTERN</code> environment variable.  <br>

<b>Example Usage:</b>

```yaml
strategy: "OnTransientError" 
```

---

##### **`dependencies`**
<b>Description:</b> specifies the dependency between jobs/Workflows  <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Value** |
|-------------|-------------|---------------|----------------|
| string      | optional    | none          | none           |

<b>Example Usage:</b>

```yaml
dependencies: job2
```

---

