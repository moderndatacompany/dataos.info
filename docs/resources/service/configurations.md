# Attributes of Service Resource Manifest

This document provide a comprehensive overview of the configuration attributes available for the Service Resource.

## Structure of Service Resource manifest

The manifest below demonstrates the structure of the Service Resource:

```yaml
# ==========================
# RESOURCE META SECTION
# Common attributes for all DataOS Resources
# ==========================

name: ${{service_resource_name}}  # (Required) Name of the Service Resource (e.g., my-first-service). Must conform to regex [a-z0-9]([-a-z0-9]*[a-z0-9]). Total length of the string should be less than or equal to 48 characters.
version: v1  # (Required) Manifest version of the Service Resource. Must be `v1`.
type: service  # (Required) Resource type. Must be `service` for a Service Resource.
tags:  # (Optional) Tags for categorization. Must be a list of strings.
  - ${{tag_example_1}}  # Example: dataos:service
  - ${{tag_example_2}}  # Example: dataos:workspace:curriculum
description: ${{resource_description}}  # (Optional) Description of the Service Resource (e.g., Customer data syndication service).
owner: ${{resource_owner}}  # (Optional) Owner of the Service Resource. Defaults to the user applying the manifest.
layer: ${{resource_layer}}  # (Optional) DataOS layer. Defaults to `user`. Possible values: `user` or `system`.

# ==========================
# SERVICE-SPECIFIC SECTION
# Attributes specific to the Service resource type
# ==========================

service:  
  title: ${{service_title}}  # (Optional) Title of the service (e.g., Flash Service).
  tags:  # (Optional) List of service-specific tags.
    - ${{service_tag1}}  
    - ${{service_tag2}}  
  servicePort: ${{service_port_number}}  # (Optional) Service port declaration for a single port. Must be an integer.
  servicePorts:  # (Optional) List of multiple port declarations.
    - name: ${{service_port1_name}}  # (Required) Port name. Must be a string.
      servicePort: ${{service_port_1_number}}  # (Required) Port number. Must be an integer.
    - name: ${{service_port_2_name}}  
      servicePort: ${{service_port_2_number}}  
  ingress:  # (Optional) Ingress configuration.
    enabled: ${{enable_ingress}}  # (Required) Boolean to enable or disable ingress.
    path: ${{service_path}}  # (Required) String representing the service path (e.g., `/randomapi`).
    stripPath: ${{strip_path_flag}}  # (Optional) Boolean to enable or disable path stripping.
    noAuthentication: ${{no_auth_flag}}  # (Optional) Boolean to enable or disable authentication.
    appDetailSpec: ${{app_details}}  # (Optional) String for custom application details.
    apiDetailSpec: ${{api_details}}  # (Optional) String for custom API details.
  replicas: ${{service_replicas}}  # (Optional) Number of service replicas. Must be an integer greater than or equal to 1. Defaults to 0.
  autoScaling:  # (Optional) Autoscaling configuration.
    enabled: ${{autoscaling_enabled}}  # (Required) Boolean to enable or disable autoscaling.
    minReplicas: ${{min_replicas}}  # (Required) Minimum number of replicas. Must be an integer.
    maxReplicas: ${{max_replicas}}  # (Required) Maximum number of replicas. Must be an integer.
    targetMemoryUtilizationPercentage: ${{memory_utilization}}  # (Optional) Target memory utilization percentage. Must be an integer.
    targetCPUUtilizationPercentage: ${{cpu_utilization}}  # (Optional) Target CPU utilization percentage. Must be an integer.
  stack: ${{stack_to_be_orchestrated}}  # (Required) Stack to be orchestrated (e.g., `bento:1.0`, `flash`, `lakesearch`). Must be a string.
  logLevel: ${{log_level}}  # (Optional) Logging level. Must be a string.

  configs:  # (Optional) Key-value mapping for configuration settings.
    ${{config_key1}}: ${{config_value1}}  
    ${{config_key2}}: ${{config_value2}}  

  envs:  # (Optional) Key-value mapping for environment variables.
    ${{env_key1}}: ${{env_value1}}  
    ${{env_key2}}: ${{env_value2}}  

  secrets:  
    - ${{secret_name}}  # (Optional) List of secret names. Must be a list of strings.

  dataosSecrets:  # (Optional) List of DataOS secret configurations.
    - name: ${{secret_name}}  # (Required) Secret name. Must be a string.
      workspace: ${{secret_workspace}}  # (Required) Workspace where the secret is stored.
      key: ${{secret_key}}  # (Optional) Single secret key.
      keys:  # (Optional) Array of multiple secret keys.
        - ${{secret_key1}}  
        - ${{secret_key2}}  
      allKeys: ${{all_keys_flag}}  # (Optional) Boolean to include all keys.
      consumptionType: ${{consumption_type}}  # (Optional) Type of consumption.

  dataosVolumes:  # (Optional) List of DataOS volume configurations.
    - name: ${{volume_name}}  # (Required) Volume name.
      directory: ${{volume_directory}}  # (Required) Directory path.
      readOnly: ${{read_only_flag}}  # (Optional) Boolean flag for read-only access.
      subPath: ${{volume_subpath}}  # (Optional) Sub-directory path.

  tempVolume: ${{temp_volume_name}}  # (Optional) Temporary volume. Must be a string.

  persistentVolume:  # (Optional) Persistent volume configuration.
    name: ${{persistent_volume_name}}  # (Required) Volume name.
    directory: ${{persistent_volume_directory}}  # (Required) Directory path.
    readOnly: ${{persistent_volume_read_only}}  # (Optional) Boolean flag for read-only access.
    subPath: ${{persistent_volume_subpath}}  # (Optional) Sub-directory path.

  compute: ${{compute_resource_name}}  # (Required) Compute resource (e.g., `runnable-default`). Must be a string.

  resources:  # (Optional) Resource requests and limits.
    requests:
      cpu: ${{cpu_request}}  # (Optional) CPU request (e.g., `1000m`). Must be a string.
      memory: ${{memory_request}}  # (Optional) Memory request (e.g., `100Mi`). Must be a string.
    limits:
      cpu: ${{cpu_limit}}  
      memory: ${{memory_limit}}  

  dryRun: ${{dry_run_flag}}  # (Optional) Boolean to enable or disable dry-run mode.

  runAsApiKey: ${{api_key}}  # (Optional) API key for running the service.
  runAsUser: ${{run_as_user}}  # (Optional) User to run the service as.

  topology:  # (Optional) List of topology configurations.
    - name: ${{topology_name}}  # (Required) Topology name.
      type: ${{topology_type}}  # (Required) Topology type.
      doc: ${{topology_doc}}  # (Optional) Documentation reference.
      properties:  # (Optional) Key-value mapping for topology properties.
        ${{property_key}}: ${{property_value}}  
      dependencies:  # (Optional) List of topology dependencies.
        - ${{dependency1}}  
        - ${{dependency2}}  

# ==========================
# STACK-SPECIFIC SECTION
# Attributes specific to the chosen Stack
# ==========================

  stackSpec:  # (Optional) Additional stack-specific attributes.
    ${{stack_specific_attributes}}  
```

## Configuration Attributes

This document describes all configurable attributes within the Service Resource manifest. Each attribute includes a description, data type, requirement status, default values, possible values, and example usage.

### **`service`**

**Description:** Defines the configuration for the Service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | mandatory      | none                 | none |

**Example Usage:**<br>
```yaml
service:
  title: My Service
  tags:
    - tag1
    - tag2
  servicePort: 4000
  # ... (other service configuration attributes)
```

---

### **`title`**

**Description:** Specifies the title of the Service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | optional       | none                  | any string |

**Example Usage:**<br>
```yaml
service:
  title: Flash Service
```

---


### **`tags`**

**Description:** Defines tags associated with the Service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| list of strings | optional   | none                 | valid [tag](/resources/policy/configurations/#tags) |

**Example Usage:**<br>
```yaml
service:
  tags:
    - tag1
    - tag2
```

---

### **`servicePort`**

**Description:** Specifies the port on which the service is exposed. This creates a new Service Resource targeting the specified TCP port. Ensure that no other service is using the same port, else it would get replaced. 

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | none                   | valid port number |

**Example Usage:**<br>
```yaml
service:
  servicePort: 8080
```

### **`servicePorts`**

**Description:** Specifies multiple ports on which the service can listen.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping       | optional       | none                   | valid port mappings |

**Example Usage:**

```yaml
service:
  servicePorts:
    - name: http
      servicePort: 8080
    - name: metrics
      servicePort: 9090
```

---

### **`ingress`**

**Description:** Configures the ingress for the service, which exposes HTTP and HTTPS routes from outside DataOS to services within DataOS.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | optional       | none                  | none |

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

### **`enabled`**

**Description:** Determines whether ingress is enabled for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean       | optional       | false                | true or false |

**Example Usage:**<br>
```yaml
service:
  ingress:
    enabled: true
```

---

### **`path`**

**Description:** Specifies the path for the ingress configuration. If a service with the same path already exists, it will be replaced.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | optional       | none              | any valid path |

**Example Usage:**<br>
```yaml
service:
  ingress:
    path: /my-service
```

---

### **`stripPath`**

**Description:** Determines whether to remove the path prefix from incoming requests.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean       | optional       | false                | true or false |

**Example Usage:**<br>
```yaml
service:
  ingress:
    stripPath: true
```

---

### **`noAuthentication`**

**Description:** Determines whether authentication is disabled for the ingress configuration.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean       | optional       | true               | true or false |

**Example Usage:**<br>
```yaml
service:
  ingress:
    noAuthentication: true
```

---

### **`replicas`**

**Description:** Specifies the number of replicas for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | 1                   | any positive integer |

**Example Usage:**<br>
```yaml
service:
  replicas: 3
```

---

### **`autoScaling`**

**Description:** Configures auto-scaling for the service to adjust workload dynamically.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | optional       | none                 | none |

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

### **`enabled`**

**Description:** indicates whether autoscaling is enabled for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean       | optional       | true                | true or false |

**Example Usage:**<br>
```yaml
service:
  autoScaling:
    enabled: true
```

---

### **`minReplicas`**

**Description:** the minimum number of replicas for autoscaling.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | 1                   | any positive integer |

**Example Usage:**<br>
```yaml
service:
  autoScaling:
    minReplicas: 2
```

---

### **`maxReplicas`**

**Description:** the maximum number of replicas for autoscaling.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | none                  | any positive integer |

**Example Usage:**<br>
```yaml
service:
  autoScaling:
    maxReplicas: 3
```

---

### **`targetMemoryUtilizationPercentage`**

**Description:** the target memory utilization percentage for autoscaling is the average memory usage of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' CPU utilization is higher than the target you defined, then your replicas will be adjusted.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer       | optional       | none                  | any integer between 0 and 100 |

**Example Usage:**<br>
```yaml
service:
  autoScaling:
    targetMemoryUtilizationPercentage: 70
```

---

### **`targetCPUUtilizationPercentage`**

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

**Description:** the name and version of the [Stack](/resources/stacks/) Resource which the Service orchestrates.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | mandatory      | none                  | bento/<br>alpha/beacon+rest

<b>Additional Details:</b> <br>
- <i>bento:</i> for Stream Analytics/Event Stream Processing <br>
- <i>beacon:</i> for Web and other applications gain access to PostgreSQL database within DataOS<br>
- <i>alpha:</i> for connecting to Web-Server based application images developed on top of DataOS
 <br>

**Example Usage:**<br>
```yaml
service:
  stack: bento
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
| list of strings | optional   | none                   | none |

**Example Usage:**<br>
```yaml
service:
  secrets:
    - mysecret
```

---

### **`dataosSecrets`**

**Description:** list of [DataOS Secrets](/resources/secret/) associated with the Service. Each DataOS Secret is an mapping containing various attributes.

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

**Description:** the name of the [Compute](/resources/compute/) Resource for the Service. 

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

**Description:** The `resources` attribute defines **CPU and memory allocations** for a Service, specifying both requests and limits. This ensures that the Service gets the necessary computing resources while preventing excessive consumption that could affect performance of the system. This attribute is useful when:  

- **Controlling resource allocation** – Ensuring a service gets the required CPU and memory.  
- **Preventing resource overuse** – Setting upper limits to avoid service crashes or disruptions.  
- **Optimizing performance** – Balancing workload execution across Compute node pools.  

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
|--------------|--------------|------------------|------------------|
| mapping     | Optional     | None             | None            |

**Sub-Attributes:**  

- **Requests (`requests.cpu`, `requests.memory`)** - Guarantees a minimum level of CPU/memory allocation for the service. If a node cannot provide the requested resources, the pod will not be scheduled.  

- **Limits (`limits.cpu`, `limits.memory`)** - Specifies the **maximum** amount of CPU/memory a service can consume. If exceeded, the service may be throttled (CPU) or evicted (memory).  

| **Key**   | **Description**                                    | **Data Type** | **Requirement** | **Example Values** |
|-----------|------------------------------------------------|-------------|--------------|-----------------|
| `requests.cpu` | Minimum CPU required for the service       | string      | Optional     | `"500m"`, `"1"` |
| `requests.memory` | Minimum memory required for the service | string      | Optional     | `"256Mi"`, `"1Gi"` |
| `limits.cpu` | Maximum CPU allocated to the service       | string      | Optional     | `"1000m"`, `"2"` |
| `limits.memory` | Maximum memory allocated to the service | string      | Optional     | `"512Mi"`, `"2Gi"` |

**Example usage**  

```yaml
service:
  resources:
    requests:
      cpu: "500m"
      memory: "256Mi"
    limits:
      cpu: "1000m"
      memory: "512Mi"
```  

**Best practices for using `resources`**  

- **Right-Size Your Resources** – Avoid setting high limits unless required to prevent unnecessary resource consumption.  
- **Monitor Usage** – Use monitoring tools (e.g., **DataOS Operations app**, **Grafana**) to track resource utilization and adjust requests/limits accordingly.  
- **Consider Autoscaling** – If workloads vary, enable **autoscaling** instead of over-provisioning resources.  

---

### **`dryRun`**  

**Description:**  The `dryRun` attribute determines whether a Service deployment is executed in **dry-run mode**. When enabled (`true`), the service configuration is validated, and the deployment process is simulated **without actually submitting it** to the DataOS. This allows users to verify configurations before making actual changes. This attribute is useful when:  

- Testing service configurations before applying them in a production environment.  
- Verifying YAML manifest syntax and resource constraints. 
- Ensuring that changes do not unintentionally override existing deployments.  

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
|--------------|--------------|------------------|------------------|
| boolean     | Optional     | `true`           | `true` or `false` |

**Example Usage**  

```yaml
service:
  dryRun: true
```  

---

### **`runAsApiKey`**  

**Description:** The `runAsApiKey` attribute allows a Service to assume the identity of another user by using their API key. This enables programmatic access to DataOS services under a specific user's authorization, ensuring that actions performed by the Service are executed with the appropriate permissions. This attribute is useful when:  

- Automating service deployments on behalf of a specific application user.
- Running workloads that require user-specific permissions for authentication and authorization.  

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
|--------------|--------------|------------------|------------------|
| string      | Mandatory    | None             | Any valid API key |

**Additional Details:** The apikey can be obtained by executing the following command from the CLI:

```shell
dataos-ctl user apikey get
```

In case no apikey is available, the below command can be run to create a new apikey

```shell
dataos-ctl user apikey create -n ${{name of the apikey}} -d ${{duration for the apikey to live}}
```

**Example Usage**  

```yaml
service:
  runAsApiKey: abcdefghijklmnopqrstuvwxyz
```

---

### **`runAsUser`**  

**Description:**  When configured, the `runAsUser` attribute allows  a Service to run with the permissions of the specified **UserID** of the use-case assignee, enabling access control and execution privileges. This attribute is particularly useful when:  

- Running services that require user/role-specific permissions.  
- Enforcing security policies where certain actions should be restricted to a designated user.  
- Managing workloads that need to impersonate a user for auditing or operational control.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
|--------------|--------------|------------------|------------------|
| string      | Mandatory    | User ID of the user applying the manifest | Any valid User ID of the use-case assignee |

**Example Usage**  

```yaml
service:
  runAsUser: iamgroot
```  