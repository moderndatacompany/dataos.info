# Attributes of Service YAML Manifest

This document provide a comprehensive overview of the configuration attributes available for the Service Resource.

## Structure of Service-specifc Section

The manifest below demonstrates the structure of the Service-specific section YAML configuration:

```yaml
service:
  title: ${{title of service}}
  tags:
    - ${{tag1}}
    - ${{tag2}}
  servicePort: ${{service port number}}
  ingress: 
    enabled: ${{enables ingress}}
    path: ${{/alpha}}
    stripPath: ${{true}}
    noAuthentication: ${{false}}
    appDetailSpec: ${{}}
    apiDetailSpec: ${{}}
  replicas: ${{2}}
  autoScaling: 
    enabled: ${{true/false}}
    minReplicas: ${{3}}
    maxReplicas: ${{5}}
    targetMemoryUtilizationPercentage: ${{50}}
    targetCPUUtilizationPercentage: ${{80}}
  stack: ${{stack name and version}} # mandatory
  logLevel: ${{log level}}
  configs: 
    ${{alpha: beta}}
  envs: 
    ${{random: delta}}
  secrets: 
    - ${{mysecret}}
  dataosSecrets:
    - name: ${{mysecret}}
      workspace: ${{curriculum}}
      key: ${{newone}}
      keys:
        - ${{newone}}
        - ${{oldone}}
      allKeys: ${{true}}
      consumptionType: ${{envVars}}
  dataosVolumes: 
    - name: ${{myVolume}}
      directory: ${{/file}}
      readOnly: ${{true}}
      subPath: ${{/random}}
  tempVolume: ${{abcd}}
  persistentVolume:
    name: ${{myVolume}}
    directory: ${{/file}}
    readOnly: ${{true}}
    subPath: ${{/random}}
  compute: ${{compute resource name}} # mandatory
  resources:
    requests:
      cpu: ${{100Mi}}
      memory: ${{100Gi}}
    limits:
      cpu: ${{100Mi}}
      memory: ${{100Gi}}
  dryRun: ${{true}}
  runAsApiKey: ${{abcdefghijklmnopqrstuvwxyz}}
  runAsUser: ${{iamgroot}}
  topology:
    name: ${{abcd}} # mandatory
    type: ${{efgh}} # mandatory
    doc: ${{abcd efgh}}
    properties: 
      ${{alpha: random}}
    dependencies: 
      - ${{abc}}
```

## Configuration Attributes

## **`service`**

**Description:** configuration for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | mandatory      | none                   | none

**Example Usage:**<br>
```yaml
service:
  title: My Service
  tags:
    - tag1
    - tag2
  servicePort: 4
  # ... (other service configuration attributes)
```

---

### **`title`**

**Description:** the title of the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | optional       | none                  | any string

**Example Usage:**<br>
```yaml
service:
  title: benthos service
```

---


### **`tags`**

**Description:** tags associated with the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| list of strings | optional   | none                 | valid [tag](../policy/manifest_attributes.md#tags)

**Example Usage:**<br>
```yaml
service:
  tags:
    - tag1
    - tag2
```

---

### **`servicePort`**

**Description:** the port on which the service is exposed. this specification creates a new Service object, which targets the TCP port number whose number is given. Ensure that any other service is not using this port else it would replace it.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | none                   | valid port number

**Example Usage:**<br>
```yaml
service:
  servicePort: 8080
```

---

### **`ingress`**

**Description:** configuration for the service's ingress. Ingress exposes HTTP and HTTPS routes from outside DataOS to services within DataOS. Configure the incoming port for the service to allow access to DataOS resources from external links.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | optional       | none                  | none

**Example Usage:**<br>
```yaml
service:
  ingress: 
      enabled: true
      noAuthentication: true
      path: /sample-service 
      stripPath: true
```
---

#### **`enabled`**

**Description:** indicates whether ingress is enabled for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean       | optional       | false                | true/false

**Example Usage:**<br>
```yaml
service:
  ingress:
    enabled: true
```

---

#### **`path`**

**Description:** the path for the Service's ingress configuration. If a Service by the same path already exists, it would get replaced.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | optional       | none              | any valid path

**Example Usage:**<br>
```yaml
service:
  ingress:
    path: /my-service
```

---

#### **`stripPath`**

**Description:** indicates whether to strip the path from incoming requests in the ingress configuration.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean       | optional       | false                | true/false

**Example Usage:**<br>
```yaml
service:
  ingress:
    stripPath: true
```

---

#### **`noAuthentication`**

**Description:** indicates whether authentication is disabled for the ingress configuration.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean       | optional       | true               | true or false.

**Example Usage:**<br>
```yaml
service:
  ingress:
    noAuthentication: true
```

---

### **`replicas`**

**Description:** the number of replicas for the service

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | 1                   | any positive integer

**Example Usage:**<br>
```yaml
service:
  replicas: 3
```

---

### **`autoScaling`**

**Description:** configuration for auto-scaling of the service. Manage autoscaling to match changing application workload levels.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | optional       | none                 | none

**Example Usage:**<br>
```yaml
service:
  autoScaling:
    enabled: true
    minReplicas: 3
    maxReplicas: 5
    targetMemoryUtilizationPercentage: 50
    targetCPUUtilizationPercentage: 80
```

---

#### **`enabled`**

**Description:** indicates whether autoscaling is enabled for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean       | optional       | true                | true or false.

**Example Usage:**<br>
```yaml
service:
  autoScaling:
    enabled: true
```

---

#### **`minReplicas`**

**Description:** the minimum number of replicas for autoscaling.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | 1                   | any positive integer.

**Example Usage:**<br>
```yaml
service:
  autoScaling:
    minReplicas: 2
```

---

#### **`maxReplicas`**

**Description:** the maximum number of replicas for autoscaling.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | none                  | any positive integer

**Example Usage:**<br>
```yaml
service:
  autoScaling:
    maxReplicas: 3
```

---

#### **`targetMemoryUtilizationPercentage`**

**Description:** the target memory utilization percentage for autoscaling is the average memory usage of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' CPU utilization is higher than the target you defined, then your replicas will be adjusted.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | none                  | any integer between 0 and 100.

**Example Usage:**<br>
```yaml
service:
  autoScaling:
    targetMemoryUtilizationPercentage: 70
```

---

#### **`targetCPUUtilizationPercentage`**

**Description:** the target CPU utilization percentage for autoscaling is the average CPU usage of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' memory utilization is higher than the target you defined, then your replicas will be adjusted.
|

 **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | 80                  | any integer between 0 and 100.

**Example Usage:**<br>
```yaml
service:
  autoScaling:
    targetCPUUtilizationPercentage: 90
```

---

### **`stack`**

**Description:** the name and version of the [Stack](../stacks.md) Resource which the Service orchestrates.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | mandatory      | none                  | benthos/<br>alpha/beacon+rest

<b>Additional Details:</b> <br>
- <i>benthos:</i> for Stream Analytics/Event Stream Processing <br>
- <i>beacon:</i> for Web and other applications gain access to PostgreSQL database within DataOS<br>
- <i>alpha:</i> for connecting to Web-Server based application images developed on top of DataOS
 <br>

**Example Usage:**<br>
```yaml
service:
  stack: benthos
```

---

### **`logLevel`**

**Description:** the log level for the Service classifies enteries in logs in terms of urgency which helps to filter logs during search and helps control the amount of information in logs.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | optional       | INFO               | Valid log level from amongst<br> INFO, WARN DEBUG, ERROR

<b>Additional Details:</b>
- <i>INFO:</i> Designates informational messages that highlight the progress of the service
- <i>WARN:</i> Designates potentially harmful situations
- <i>DEBUG:</i> Designates fine-grained informational events that are most useful while debugging
- <i>ERROR:</i> Desingates error events that might still allow the workflow to continue running

**Example Usage:**<br>
```yaml
service:
  logLevel: DEBUG
```

---

### **`configs`**

**Description:** additional optional configuration for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | optional       | none                  | key-value configurations

**Example Usage:**<br>
```yaml
service:
  configs:
    key1: value1
    key2: value2
```

---

### **`envs`**

**Description:** environment variables for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | optional       | none                 | key-value configurations

**Example Usage:**<br>
```yaml
service:
  envs:
    CONTAINER_NAME: 'itsrandom'
```

---

### **`secrets`**

**Description:** list of secrets associated with the service

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| list of strings | optional   | none                   | none

**Example Usage:**<br>
```yaml
service:
  secrets:
    - mysecret
```

---

### **`dataosSecrets`**

**Description:** list of [DataOS Secrets](../secret.md) associated with the Service. Each DataOS Secret is an mapping containing various attributes.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| list of mappings | optional   | none                   | none

**Example Usage:**<br>
```yaml
service:
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

### **`dataosVolumes`**

**Description:** list of DataOS Volumes associated with the Service. Each DataOS Volume is a mapping containing various attributes.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| list of mappings | optional   | none                   | none

**Example Usage:**<br>
```yaml
service:
  dataosVolumes:
    - name: myVolume
      directory: /file
      readOnly: true
      subPath: /random
```

---

### **`tempVolume`**

**Description:** the temporary volume for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | optional       | none                   | any valid Volume name

**Example Usage:**<br>
```yaml
service:
  tempVolume: abcd
```

---

### **`persistentVolume`**

**Description:** configuration for the persistent volume associated with the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | optional       | none                | none

**Example Usage:**<br>
```yaml
service:
  persistentVolume:
    name: myVolume
    directory: /file
    readOnly: true
    subPath: /random
```

---

### **`compute`**

**Description:** the name of the [Compute](../compute.md) Resource for the Service. 

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | mandatory      | none                  | valid runnable-type Compute Resource name.

**Example Usage:**<br>
```yaml
service:
  compute: MyComputeResource
```

---

### **`resources`**

**Description:** Resource requests and limits for the Service. This includes CPU and memory specifications.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | optional       | none                 | none

**Example Usage:**<br>
```yaml
service:
  resources:
    requests:
      cpu: 100Mi
      memory: 100Gi
    limits:
      cpu: 100Mi
      memory: 100Gi
```

---

### **`dryRun`**

**Description:** indicates whether the service is in dry run mode. When enabled, the dryRun property deploys the service to the cluster without submitting it.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean       | optional       | true                | true or false.

**Example Usage:**<br>
```yaml
service:
  dryRun: true
```

---

### **`runAsApiKey`**

**Description:** the runAsApiKey attribute allows a user to assume the identity of another user through the provision of the latter's API key.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | mandatory      | none               | any valid API key.

**Additional Details:** The apikey can be obtained by executing the following command from the CLI:

```shell
dataos-ctl user apikey get
```

In case no apikey is available, the below command can be run to create a new apikey

```shell
dataos-ctl user apikey create -n ${{name of the apikey}} -d ${{duration for the apikey to live}}
```

**Example Usage:**<br>
```yaml
service:
  runAsApiKey: abcdefghijklmnopqrstuvwxyz
```

---

### **`runAsUser`**

**Description:** when the `runAsUser` attribute is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | mandatory      | user-id of the user                   | user-id of the use-case assignee

**Example Usage:**<br>
```yaml
service:
  runAsUser: iamgroot
```
