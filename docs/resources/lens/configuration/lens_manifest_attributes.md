# Structure of Lens manifest

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
	secrets: # Referred Instance-secret configuration (**mandatory for private repository)
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
		syncFlags: # what are these?
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
		resources:
			requests:
				cpu: 4Gi
				memory: 1000m
			limits:
				cpu: 16Gi
				memory: 2000m
	router:
		logLevel: INFO
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
		resources:
			requests:
				cpu: 4Gi
				memory: 1000m
			limits:
				cpu: 16Gi
				memory: 2000m		
	iris:
		logLevel: INFO
		resources:
			requests:
				cpu: 4Gi
				memory: 1000m
			limits:
				cpu: 16Gi
				memory: 2000m
```

# Resource meta section configuration

### **`name`**

**Description:** Declare a name for the Lens Resource

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | mandatory | none | • alphanumeric values with the RegEx`[a-z0-9]([-a-z0-9]*[a-z0-9])`; a hyphen/dash is allowed as a special character
• total length of the string should be less than or equal to 48 characters
• names of cluster & depot have a different RegEx`[a-z]([a-z0-9]*)`; a hyphen/dash is not allowed as a special character |

**Additional information:** Two Resources in the same workspace cannot have the same name.

**Example usage:**

```yaml
name: sales360lens
```

---

### **`version`**

**Description:** The version of the Lens manifest Resource

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | mandatory | none | v1alpha |

**Example usage:**

```yaml
version: v1alpha
```

---

### **`type`**

**Description:** Provide the value for the resource type. Here its lens.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | mandatory | none | lens |

**Example usage:**

```yaml
type: lens
```

---

### **`tags`**

**Description:** Assign tags to the Lens Resource-instance

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | mandatory | none | any string; special characters are allowed |

**Example usage:**

```yaml
tags:
	- lens
	- sales360
	- resource
```

---

### **`description`**

**Description:** Assign description to Lens Resource

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | optional | none | any string |

**Additional information:** the description can be within quotes or without.

> YAML supports scalars such as strings, numbers, booleans, and null. A scalar value can be unquoted, within single quotes (') or double quotes ("). When the scalar contains a special character, the value must be declared within quotes.
> 

**Example usage:**

```yaml
description: "This is a sample description of a Lens Resource"
```

---

### **`owner`**

**Description:** Identification of the user

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | optional | id of the user applying the Resource | any valid dataos user id |

**Additional information:** when no ID is provided, or an incorrect ID is provided, the system automatically corrects it to the ID of the user who applied the Resource on DataOS CLI

**Example usage:**

```yaml
owner: iamgroot
```

---

### **`layer`**

**Description:** Declare the name of the layer for which the Lens Resource is going to be deployed

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | optional | user | user/system |

**Additional information:** From a user's perspective, the operating system can be envisaged as working at two levels - user layer & system layer. This is only a logical separation to understand the workings of the system.

**Example usage:**

```yaml
layer: user
```
---

# Lens-specific section configuration

### `lens`

**Description:** The `lens` attribute defines a mapping of Lens Resource-specific attributes.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid Lens-specific attributes |

**Example Usage:**

```yaml
lens:
	compute: runnable-default 
	runAsApiKey: abcdefghijklmnopqrstuvwxyz
	runAsUser: iamgroot
	# additional Lens-specific attributes
```

---

### **`compute`**

**Description:** Defines the [Compute Resource](https://dataos.info/resources/compute/) to be used by the Lens. The value should match a pre-defined Compute Resource within DataOS that suits the workload requirements of the Lens model.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | mandatory | none | runnable-default or any other valid runnable-type Compute Resource name |

**Example Usage:**

```yaml
lens:
	compute: runnable-default
```

---

### **`runAsApiKey`**

<aside class="callout">
🗣 Before applying the manifest file of Resource comprising the apikey of the use-case assignee using the `runAsApiKey` attribute, make sure that you have the appropriate use-case assigned by the same person.

</aside>

**Description:** The `runAsApiKey` attribute allows a user to assume the identity of another user by providing the latter's API key.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | optional | apikey of the owner applying the Resource | apikey of the use-case assignee |

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

**Example Usage:**

```yaml
lens:
  runAsApiKey: abcdefghijklmnopqrstuvwxyz
```

---

### **`runAsUser`**

<aside class="callout">
🗣 Before applying the manifest file of Resource comprising the user-id of the use-case assignee using the `runAsUser` attribute, make sure that you have the appropriate use-case assigned by the same person.

</aside>

**Description:** When the `runAsUser` attribute is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | optional | user-id of the owner applying the Resource | user-id of the use-case assignee |

**Example Usage:**

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

**Attributes of `secrets`**

- **`name`**: The name of the secret to be referred to. It should match the name of a pre-existing Instance Secret within DataOS. This is a mandatory attribute specified as a string.
- **`key`**: String that identifies a specific key of the Secret. This is an optional attribute.
- **`keys`**: List of key identifiers within the secret. This is optional.
- **`allKeys`**: Boolean indicating whether all keys should be used. By default, it is false. This is also optional.
- **`consumptionType`**: How the secret is consumed. By default its value is `envVars`, signifying secret are consumed as environment variables.

**Example Usage:** If the codebase for your Lens is stored in a private code repository, you can create a Secret for the same and refer to it within the manifest file of Lens in the following way:

```yaml
name: bitbucket-r
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
	  - name: bitbucket-r
	    allkeys: true
```

---

### `source`

**Description:** Specifies the source configuration from which the Lens will be mapped.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid source configuration |

**Attributes of `source`:**

- `type`: The source type defines the type of data source to which your Lens will be mapped. This is a mandatory attribute, declared as a string. Possible types are `themis`, `trino`, etc.
- `name`: The identifier for the source to which Lens will be mapped. This is a mandatory attribute, declared as a string.
- catalog: ()

**Example Usage:**

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

- **`url`**: URL of the repository containing the Lens model. This is a mandatory attribute
- **`lensBaseDir`**: The path to the specific directory within the repository where the model files are stored. This is also mandatory.
- **`secretId`**: Identifier for a secret. It's usually of the form `${secret_name}_${acl}.` All hyphens within the secret name are also replaced by _.
- **`syncFlags`**: Additional flags that control the synchronization behavior. Used to declare the specific branch in the repository using the `--ref=${branch_name}` flag.

**Example Usage:**

```yaml
lens:
	repo: 
		url: https://www.bitbucket.org/abcd/lens2
		lensBaseDir: lens2/sales/model 
		secretId: bitbucket_r_r
		syncFlags: 
			- --ref=lens2
```

---

### **`api`**

**Description:** Defines configurations for API instances of Lens, which handles incoming requests and executes business logic.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | optional | none | valid API instance configurations |

**Attributes for `api`**

- **`logLevel`**: The log level for the API instance classifies entries in logs in terms of urgency, which helps to filter logs during searches and helps control the amount of information in logs. By default, it's INFO. Possible values include INFO, WARN, DEBUG, and ERROR. Each of the possible values is used in a specific scenario as provided below:
    - `INFO`*:* Designates informational messages that highlight the progress of the workload
    - `WARN`*:* Designates potentially harmful situations
    - `DEBUG`*:* Designates fine-grained informational events that are most useful while debugging
    - `ERROR`*:* Designates error events that might still allow the workflow to continue running

- **`replicas`**: Number of API instances to deploy. By default, it's 1, and it could be any positive integer.

- **`autoScaling`**: Auto-scaling configuration. Manage autoscaling to match changing workload levels. It comprises several attributes:

    - **`enabled`**: Indicates whether autoscaling is enabled in the form of a boolean. By default, it is false.
    - **`minReplicas`**: The minimum number of replicas for autoscaling. By default, it's 1, and could be any positive integer
    - **`maxReplicas`**: The maximum number of replicas for autoscaling. It could be any positive integer greater than `minReplicas`.
    - **`targetMemoryUtilizationPercentage`**: The target memory utilization percentage for autoscaling is the average memory usage of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' CPU utilization is higher than the target you defined, then your replicas will be adjusted. Its value could be any integer between 0 to 100.
    - **`targetCPUUtilizationPercentage`**:  The target CPU utilization percentage for autoscaling is the average CPU usage of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' memory utilization is higher than the target you defined, then your replicas will be adjusted. Its value could be any integer between 0 to 100.

- **`metricEndpoint`**: Specifies the metric collection endpoint configuration. It further contains two attributes, `port`, and `path`.

    - **`port`**: Port number for the metric endpoint.
    - **`path`**: Path at which metrics are available.

- **`resources`**: CPU and memory resource requests and limits. By default, the CPU and memory requests are 100m and 100Mi, while limits are 400m and 400Mi, respectively. The CPU units are declared in milliCPU(m) or CPU core, while memory is declared in Mebibytes (Mi) or Gibibytes (Gi).

- **`envs`**: Environment variables for API instance.
    - `LENS2_SCHEDULED_REFRESH_TIMEZONES:` "UTC,America/Vancouver,America/Toronto"

**Example Usage:**

```yaml
lens:
  api:  
    replicas: 2 
    logLevel: info
    envs:
	    LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
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

**Description:** Defines configurations for Workers of Lens.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | optional | none | valid worker configurations |

**Attributes for `worker`**

- **`logLevel`**: The log level for the Worker classifies entries in logs in terms of urgency, which helps to filter logs during searches and helps control the amount of information in logs. By default, it's INFO. Possible values include INFO, WARN, DEBUG, and ERROR. Each of the possible values is used in a specific scenario as provided below:
    - `INFO`*:* Designates informational messages that highlight the progress of the workload
    - `WARN`*:* Designates potentially harmful situations
    - `DEBUG`*:* Designates fine-grained informational events that are most useful while debugging
    - `ERROR`*:* Designates error events that might still allow the workflow to continue running

- **`replicas`**: Number of Worker to deploy. By default, it's 1, and it could be any positive integer.

- **`resources`**: CPU and memory resource requests and limits. By default, the CPU and memory requests are 100m and 100Mi, while limits are 400m and 400Mi, respectively. The CPU units are declared in milliCPU(m) or CPU core, while memory is declared in Mebibytes (Mi) or Gibibytes (Gi).

- **`envs`**: Environment variables for Worker.

**Example Usage:**

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

**Attributes for `router`**

- **`logLevel`**: The log level for the Router classifies entries in logs in terms of urgency, which helps to filter logs during searches and helps control the amount of information in logs. By default, it's INFO. Possible values include INFO, WARN, DEBUG, and ERROR. Each of the possible values is used in a specific scenario as provided below:

    - `INFO`*:* Designates informational messages that highlight the progress of the workload
    - `WARN`*:* Designates potentially harmful situations
    - `DEBUG`*:* Designates fine-grained informational events that are most useful while debugging
    - `ERROR`*:* Designates error events that might still allow the workflow to continue running

- **`replicas`**: Number of Router to deploy. By default, it's 1, and it could be any positive integer.

- **`resources`**: CPU and memory resource requests and limits. By default, the CPU and memory requests are 100m and 100Mi, while limits are 400m and 400Mi, respectively. The CPU units are declared in milliCPU(m) or CPU core, while memory is declared in Mebibytes (Mi) or Gibibytes (Gi).

- **`envs`**: Environment variables for Router.

**Example Usage:**

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

### `iris`

**Description:** Manages interaction with Iris dashboards.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid iris configuration |

**Attributes for `iris`**

- **`logLevel`**: The log level for Iris classifies entries in logs in terms of urgency, which helps to filter logs during searches and helps control the amount of information in logs. By default, it's INFO. Possible values include INFO, WARN, DEBUG, and ERROR. Each of the possible values is used in a specific scenario as provided below:

    - `INFO`*:* Designates informational messages that highlight the progress of the workload
    - `WARN`*:* Designates potentially harmful situations
    - `DEBUG`*:* Designates fine-grained informational events that are most useful while debugging
    - `ERROR`*:* Designates error events that might still allow the workflow to continue running

- **`replicas`**: Number of Iris replicas to deploy. By default, it's 1, and it could be any positive integer.

- **`resources`**: CPU and memory resource requests and limits. By default, the CPU and memory requests are 100m and 100Mi, while limits are 400m and 400Mi, respectively. The CPU units are declared in milliCPU(m) or CPU core, while memory is declared in Mebibytes (Mi) or Gibibytes (Gi).

- **`envs`**: Environment variables for Iris.

**Example Usage:**

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