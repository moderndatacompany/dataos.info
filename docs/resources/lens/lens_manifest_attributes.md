# Attribute of Lens  manifest

## Structure of Lens manifest

```yaml
# RESOURCE META SECTION
name: saleslens # Lens Resource name (mandatory)
version: v1alpha # Resource manifest version (mandatory)
type: lens # Type of Resource (mandatory)
tags: # Tags (optional)
 - sales
 - lens
 - resource
owner: iamgroot # Resource owner (optional)
layer: user # DataOS Layer (optional)

# LENS-SPECIFIC SECTION
lens:
 compute: runnable-default # Compute Resource name (mandatory)
 runAsApiKey: abcdefghijklmnopqrstuvwxyz # DataOS APIkey (optional)
 runAsUser: iamgroot # DataOS UserID (optional)
 secrets: # Referred Instance-secret configuration (mandatory for private repository)
	- name: bitbucket-r # Instance-secret name (mandatory)
		key: abcd # Key to be referred (optional)
		keys: # List of keys to be referred (optional)
			- abcd
			- efgh
		allKeys: true # Whether all keys are required or not (optional)
		consumptionType: envVars # Secret consumption type (optional)
 source: # mandatory
	type: themis # mandatory
	name: minithemis # mandatory
	catalog: icebase
 repo: # Code repository configuration (mandatory)
	url: https://www.bitbucket.org/abcd/lens2 # Code Repository URL (mandatory)
	lensBaseDir: lens2/sales/model # mandatory
  secretId: bitbucket_r_r
	syncFlags: # refer to the branch of the repo, default main,master branch
		- --ref=lens2test
 api:
	logLevel: INFO  
	replicas: 3
	autoScaling:
		enabled: true
		minReplicas: 1
		maxReplicas: 3
		targetMemoryUtilizationPercentage: 60
		targetCPUUtilizationPercentage: 60
  resources:                     #optional
    requests:
      cpu: 4Gi
      memory: 1000m
    limits:
      cpu: 16Gi
      memory: 2000m
  envs:
    LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
    LENS2_SOURCE_WORKSPACE_NAME: public
    LENS2_DB_TIMEOUT: 1500000
 router:
	logLevel: INFO
  envs:
    LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
    LENS2_SOURCE_WORKSPACE_NAME: public
    LENS2_DB_TIMEOUT: 1500000
	resources:
    requests:
      cpu: 4Gi
      memory: 1000m
    limits:
      cpu: 16Gi
      memory: 2000m		
    
 worker:
	logLevel: INFO
	replicas: 2
  envs:
    LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
    LENS2_SOURCE_WORKSPACE_NAME: public
    LENS2_DB_TIMEOUT: 1500000
	resources:
		requests:
			cpu: 4Gi
			memory: 1000m
		limits:
			cpu: 16Gi
			memory: 2000m		
 iris:
	logLevel: INFO
  envs:
    LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
    LENS2_SOURCE_WORKSPACE_NAME: public
    LENS2_DB_TIMEOUT: 1500000
	resources:
		requests:
			cpu: 4Gi
			memory: 1000m
		limits:
			cpu: 16Gi
			memory: 2000m
```

## Resource meta section

Click [here](/resources/manifest_attributes/)  to learn about the Resource meta section configuration.

## Lens-specific section

### **`lens`**

**Description:** The `lens` attribute defines a mapping of Lens Resource-specific attributes.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid Lens-specific attributes |

**Example usage:**

```yaml
lens:
 compute: runnable-default 
 runAsApiKey: abcdefghijklmnopqrstuvwxyz
 runAsUser: iamgroot
	# additional Lens-specific attributes
```

---

### **`compute`**

**Description:** Defines the [Compute Resource](/resources/compute/) to be used by the Lens. The value should match a pre-defined Compute Resource within DataOS that suits the workload requirements of the Lens model.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | mandatory | none | runnable-default or any other valid runnable-type Compute Resource name |

**Example usage:**

```yaml
lens:
 compute: runnable-default
```

---

### **`runAsApiKey`**

<aside class="callout">
🗣 The <b>runAsApiKey</b> attribute allows a user to assume the identity of another user through the provision of the latter's API key.
</aside>

**Description:** The `runAsApiKey` attribute allows a user to assume the identity of another user by providing the latter's API key.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | optional | DataOS APIKEY of the owner| apikey of the use-case assignee |

**Additional Details**: The apikey can be obtained by executing the following command from the CLI:

```bash
dataos-ctl user apikey get
```

In case no apikey is available, the below command can be run to create a new apikey:

```bash
dataos-ctl user apikey create -n ${name-of-the-apikey} -d ${duration-for-the-apikey-to-live}
```

This sample command below creates a new API key named `myapikey` that will remain valid for 30 days.

```bash
dataos-ctl user apikey create -n myapikey -d 30d
```

**Example usage:**

```yaml
lens:
 runAsApiKey: abcdefghijklmnopqrstuvwxyz
```

---

### **`runAsUser`**

<aside class="callout">
🗣 Before applying the manifest file for a resource that includes the user ID of the use-case assignee using the runAsUser attribute, ensure that the same person has assigned the appropriate use-case to you
</aside>

**Description:** When the `runAsUser` attribute is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | optional | user-id of the owner applying the Resource | user-id of the use-case assignee |

**Example usage:**

```yaml
lens:
 runAsUser: iamgroot
```

---

### **`secrets`**

**Description:** The `secret` attribute is used to reference pre-defined Instance Secrets within the Lens manifest file. Each referred secret is a list of secret configurations.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | list of secret configurations |

**Attributes for `secrets`**

### **`name`**

**Description:** A valid secret name that matches a pre-existing Instance Secret within DataOS.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                             |
| ---           | ---             | ---               | ---                                                             |
| string        | mandatory       | none              | A valid secret name                                             |

### **`key`**

**Description:** A specific key of the Secret.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                             |
| ---           | ---             | ---               | ---                                                             |
| string        | optional        | none              | A valid key for the secret                                      |

### **`keys`**

**Description:** List of key identifiers within the secret.

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value**                                             |
| ----------------- | --------------- | ----------------- | --------------------------------------------------------------- |
| list of strings   | optional        | none              | List of key identifiers within the secret                       |

### **`allKeys`**

**Description:** Whether to include all keys in the secret.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                             |
| ---           | ---             | ---               | ---                                                             |
| boolean       | optional        | false             | true, false                                                     |

### **`consumptionType`**

**Description:** Defines how the secret will be consumed (e.g., as environment variables or other methods).

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                             |
| ---           | ---             | ---               | ---                                                             |
| string        | optional        | `envVars`         | `envVars`, or other consumption methods                         |

**Example usage:** If the codebase for your Lens is stored in a private code repository, you can create a Secret for the same and refer to it within the manifest file of Lens in the following way:

```yaml title="instance_secret.yml"
name: github-r
version: v1
type: instance-secret
description: "bitbucket read secrets for lens repos"
layer: user
instance-secret:
 type: key-value
 acl: r
 data:
  GITSYNC_USERNAME: ${USERNAME}
  GITSYNC_PASSWORD: ${PASSWORD}
```

```yaml
# Referred in Lens manifest file
lens:
	secrets:
	  - name: github-r
	    allkeys: true
```

---

### **`source`**

**Description:** Specifies the source configuration from which the Lens will be mapped. The Lens support the following sources

- depot, 
- themis, 
- minerva, 
- flash.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid source configuration |

**Attributes for `source`:**

### **`type`**

**Description:** Specifies the type of the source for Lens (e.g., themis, depot, minerva, flash.).

| Data Type | Requirement | Default Value | Possible Values      |
|-----------|-------------|---------------|----------------------|
| string    | mandatory   | none          | themis, trino, etc.  |


### **`name`**

**Description:** Defines a valid identifier for the source.

| Data Type | Requirement | Default Value | Possible Values               |
|-----------|-------------|---------------|-------------------------------|
| string    | mandatory   | none          | A valid identifier for the source.For instance, for source type cluster  (e.g., Themis and Minerva), the name refers to the cluster name (e.g., miniature, system). For Depot sources, the name refers to the Depot name. (e.g., bigquerydepot, redshift). |

### **`catalog`**

**Description:** Specifies a valid identifier for the catalog within Trino/Themis.

| Data Type | Requirement | Default Value | Possible Values                            |
|-----------|-------------|---------------|--------------------------------------------|
| string    | mandatory   | none          | A valid identifier for the catalog within Trino/Themis. e.g., system, miniature, etc.|


**Example usage:**

```yaml
lens:
 source:
  type: themis
  name: minithemis
```

---

### **`repo`**

**Description:** Configures the code repository details for Lens.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid repository configuration |

**Attributes for `repo`**

### **url**

**Description:** URL of the repository containing the Lens codes and model. This is a mandatory attribute. 

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | URL of the repository (e.g., https://bitbucket.org/mywork15/talos/). |

**Example usage:**


```yaml
repo:
	url: https://github.com/abcd/lens2
```


###  **lensBaseDir**

**Description:** The path to the specific directory within the repository where the model files are stored. This is a mandatory field that tells the system where to look for model configurations within the repository.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | required | none | A valid path within the repository (e.g., lens2/sales/model). |


```yaml
repo: # Code repository configuration (mandatory)
	url: https://www.bitbucket.org/abcd/lens2 # Code Repository URL (mandatory)
	lensBaseDir: lens2/sales/model # mandatory
```


### **secretId**

**Description:** Identifier for a secret. It's usually of the form ${secret_name}_${acl}. All hyphens within the secret name are also replaced by _. It is mandatory only in case of private repository.  

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | conditional | none | A valid secret identifier in the form ${secret_name}_${acl}. |


**Example usage:**


```yaml
lens:
 repo: 
	url: https://github.com/abcd/lens2
	lensBaseDir: lens2/sales/model 
	secretId: github-r
```


### **syncFlags**

**Description:** Additional flags that control the synchronization behavior. Used to declare the specific branch in the repository using the `--ref=${branch_name}` flag. The default branch will be the main or master branch.

| Data Type | Requirement | Default Value | Possible Values |
| ----------| ----------- | ------------- | --------------- |
|  string   |   optional  |      none     | List of flags for synchronization (e.g., --ref=main). |

**Example usage:**
         
```yaml
lens:
  repo: 
    url: https://github.com/abcd/lens
    lensBaseDir: lens/sales/model 
    secretId: github-r
    syncFlags: 
        - --ref=main
```   
### **`api`**

**Description:** Defines configurations for API instances of Lens, which handles incoming requests and executes business logic.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | optional | none | valid API instance configurations |

**Attributes for `api`**

### **`logLevel`**

**Description:** the log level for the Lens api classifies enteries in logs in terms of urgency which helps to filter logs during search and helps control the amount of information in logs.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | optional       | INFO               | Valid log level from amongst<br> INFO, WARN DEBUG, ERROR

**Additional Details:**

- INFO: Designates informational messages that highlight the progress of the API Instance.<br>
- WARN: Designates potentially harmful situations.<br>
- DEBUG: Designates fine-grained informational events that are most useful while debugging.<br>
- ERROR: Desingates error events that might still allow the workflow to continue running.<br>

**Example usage:**<br>
```yaml
lens:
  api:
    logLevel: DEBUG
```


### **`replicas`**

**Description:** the number of replicas for the API instances to deploy.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | 1                   | any positive integer

**Example usage:**<br>
```yaml
api:
  replicas: 3
```


### **`autoScaling`**

**Description:** configuration for auto-scaling of the Lens api instance. Manage autoscaling to match changing application workload levels.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | optional       | none                 | none

**Example usage:**<br>
```yaml
api:
  autoScaling:
    enabled: true
    minReplicas: 3
    maxReplicas: 5
    targetMemoryUtilizationPercentage: 50
    targetCPUUtilizationPercentage: 80
```

**Attributes for `autoScaling`**

### **`enabled`**

**Description:** indicates whether autoscaling is enabled for the Lens api instance.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean       | optional       | true                | true or false.

**Example usage:**<br>
```yaml
lens:
  api:
    autoScaling:
      enabled: true
```

<!-- - **`metricEndpoint`**: Specifies the metric collection endpoint configuration. It further contains two attributes, `port`, and `path`.

    - **`port`**: Port number for the metric endpoint.
    - **`path`**: Path at which metrics are available. -->


### **`minReplicas`**

**Description:** the minimum number of replicas for autoscaling.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | 1                   | any positive integer.

**Example usage:**<br>

```yaml
lens:
  api:
    autoScaling:
      minReplicas: 2
```

---

### **`maxReplicas`**

**Description:** the maximum number of replicas for autoscaling.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | none                  | any positive integer

**Example usage:**<br>
```yaml
lens:
  api:
    autoScaling:
      maxReplicas: 3
```

---

### **`targetMemoryUtilizationPercentage`**

**Description:** the target memory utilization percentage for autoscaling is the average memory usage: of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' CPU utilization is higher than the target you defined, then your replicas will be adjusted.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | none                  | any integer between 0 and 100.

**Example usage:**<br>
```yaml
lens:
  api:
  autoScaling:
    targetMemoryUtilizationPercentage: 70
```

---

### **`targetCPUUtilizationPercentage`**

**Description:** the target CPU utilization percentage for autoscaling is the average CPU usage: of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' memory utilization is higher than the target you defined, then your replicas will be adjusted.


 **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | 80                  | any integer between 0 and 100.

**Example usage:**<br>
```yaml
lens:
  api:
  autoScaling:
    targetCPUUtilizationPercentage: 90
```

---


### **`resources`**: 


**Description:** The resources attribute provides the configuration for CPU and memory resources allocated to the Lens API Instances. It includes settings for both requests and limits of these resources.

| **Data Type** | **Requirement**| **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------| -------------------|
| mapping       | optional       | none              | none               |


**Example usage:**

```yaml
lens:
 api:  
  resources:
    requests:
      cpu: 100m
      memory: 256Mi
    limits:
      cpu: 2000m
      memory: 2048Mi
```

### **`envs`**

**Description:** List of environment variables for API instance.

 **Attributes for `env`**


#### **`LENS2_SCHEDULED_REFRESH_TIMEZONES`**

**Description:** Specifies a list of time zones in which the user wants to run queries. Multiple time zones can be specified using the TZ Database Name format, such as "UTC,America/Vancouver,America/Toronto". The default value is a single time zone, UTC.

| Data Type | Requirement | Default Value | Possible Values                       |
|-----------|-------------|---------------|---------------------------------------|
| string    | mandatory   | UTC           | "UTC", "America/Vancouver", "America/Toronto", etc. |



### **`LENS2_DB_TIMEOUT`**

**Description:** Defines the maximum amount of time (in milliseconds) that Lens will wait for a response from the database before timing out a query. This setting prevents long-running or inefficient queries from occupying resources too long.

| Data Type | Requirement | Default Value | Possible Values |
|-----------|-------------|---------------|-----------------|
| integer   | mandatory   | none          | A positive integer representing time in milliseconds |

**Example usage:**

```yaml
lens:
 api:  
  replicas: 2 
  logLevel: info
  envs:
	  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
    LENS2_DB_TIMEOUT: 300000
  resources:
    requests:
      cpu: 100m
      memory: 256Mi
    limits:
      cpu: 2000m
      memory: 2048Mi
```

---

### **`worker`**

**Description:** Defines worker instance of Lens.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | optional | none | valid worker configurations |

**Attributes for `worker`**

### **`logLevel`**

**Description:** Specifies the logging level for the Worker. This controls the verbosity of the logs generated by the Worker instance.

| Data Type | Requirement | Default Value | Possible Values                |
|-----------|-------------|---------------|--------------------------------|
| string    | optional    | INFO          | `INFO`, `WARN`, `DEBUG`, `ERROR`|


### **`replicas`**

**Description:** Defines the number of Worker replicas to run. A higher number of replicas allows for better load handling.

| Data Type | Requirement | Default Value | Possible Values       |
|-----------|-------------|---------------|-----------------------|
| integer   | optional    | 1             | Any positive integer  |


### **`resources`**

**Description:** Specifies the CPU and memory resources allocated for the Worker instance, including both requested and limited values.

| Data Type                  | Requirement | Default Value                                                              | Possible Values                                                                 |
|----------------------------|-------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| mapping (CPU/memory)       | optional    | CPU: 100m, Memory: 100Mi (request) / CPU: 400m, Memory: 400Mi (limit)      | CPU: declared in milliCPU (m) or core / Memory: Mebibytes (Mi) or Gibibytes (Gi) |


### **`envs`**

**Description:** List of environment variables to be configured for the Worker instance.

| Data Type | Requirement | Default Value | Possible Values               |
|-----------|-------------|---------------|-------------------------------|
| mapping   | optional    | none          | List of environment variables  |


| **Attribute**       | **Data Type**       | **Requirement** | **Default Value**     | **Possible Values**                                                   |
| ------------------- | ------------------- | --------------- | --------------------- | --------------------------------------------------------------------- |
| **`logLevel`**      | string              | optional        | INFO                  | `INFO`, `WARN`, `DEBUG`, `ERROR`                                       |
| **`replicas`**      | integer             | optional        | 1                     | Any positive integer                                                  |
| **`resources`**     | mapping (CPU/memory)| optional        | CPU: 100m, Memory: 100Mi (request) / CPU: 400m, Memory: 400Mi (limit) | CPU: declared in milliCPU (m) or core / Memory: Mebibytes (Mi) or Gibibytes (Gi) |
| **`envs`**          | mapping             | optional        | none                  | List of environment variables for the Worker.                         |

**Example usage:**

```yaml
lens:
 worker: 
  replicas: 1 
  logLevel: info
  envs:
    LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  resources: # optional
    requests:
    cpu: 100m
    memory: 256Mi
    limits:
    cpu: 6000m
    memory: 6048M
```

---

### **`router`**

**Description:** Manages interaction between API instance and workers.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid router configuration |


### **`logLevel`**

**Description:** Specifies the logging level for the router instance.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                                |
| -------------- | --------------- | ----------------- | ------------------------------------------------- |
| string         | optional        | INFO              | `INFO`, `WARN`, `DEBUG`, `ERROR`                  |


### **`replicas`**

**Description:** Defines the number of router instances to run.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                     |
| -------------- | --------------- | ----------------- | --------------------------------------- |
| integer        | optional        | 1                 | Any positive integer                    |


### **`resources`**

**Description:** Specifies the CPU and memory resources allocated to the router.

| **Data Type**        | **Requirement** | **Default Value**                                             | **Possible Values**                                                |
| -------------------- | --------------- | ------------------------------------------------------------- | ------------------------------------------------------------------ |
| mapping (CPU/memory) | optional        | CPU: 100m, Memory: 100Mi (request) / CPU: 400m, Memory: 400Mi (limit) | CPU: declared in milliCPU (m) or core / Memory: Mebibytes (Mi) or Gibibytes (Gi) |


### **`envs`**

**Description:** List of environment variables for the router instance.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                              |
| -------------- | --------------- | ----------------- | ------------------------------------------------ |
| mapping        | optional        | none              | List of environment variables for the router.    |

**Example usage:**

```yaml
lens:
 router: 
  logLevel: info 
  envs:
    LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  resources: # optional
    requests:
      cpu: 100m
      memory: 256Mi
    limits:
      cpu: 6000m
      memory: 6048Mi
```

---

### **`iris`**

**Description:** Manages interaction with Iris dashboards.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid iris configuration |

### **`logLevel`**

**Description:** Defines the level of logs for Iris.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | optional | INFO | `INFO`, `WARN`, `DEBUG`, `ERROR` |


### **`replicas`**

**Description:** Defines the number of replicas for the Iris instance.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| integer | optional | 1 | Any positive integer |

### **`resources`**

**Description:** Specifies the CPU and memory resource requirements for Iris.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping (CPU/memory) | optional | CPU: 100m, Memory: 100Mi (request) / CPU: 400m, Memory: 400Mi (limit) | CPU: declared in milliCPU (m) or core / Memory: Mebibytes (Mi) or Gibibytes (Gi) |

### **`envs`**

**Description:** List of environment variables for the Iris instance.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | optional | none | List of environment variables for the iris |                     |

**Example usage:**

```yaml
lens:
 iris: 
  logLevel: info 
  resources: # optional
    requests:
      cpu: 100m
      memory: 256Mi
    limits:
      cpu: 6000m
      memory: 6048Mi
```