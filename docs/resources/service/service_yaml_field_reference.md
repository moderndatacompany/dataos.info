# Service YAML Configuration Field Reference
The Service YAML Field Reference provides a comprehensive overview of the configuration fields available for the Service resource.

## Syntax
The syntax below demonstrates the structure of the Service YAML configuration:

```yaml
service:
  title: ${alpha-stack-python-file}
  servicePort: ${8080}
  metricPort: ${8093}
  ingress:
    enabled: ${true}
    path: ${/file_python}
    stripPath: ${true}
    noAuthentication: ${true}
  replicas: ${1}
  autoScaling:
    enabled: ${true}
    minReplicas: ${1}
    maxReplicas: ${2}
    targetMemoryUtilizationPercentage: ${120}
    targetCPUUtilizationPercentage: ${120}
  stack: ${alpha}
  logLevel: ${INFO}
  envs:
    ${CONTAINER_NAME: 'itsrandom'}
  compute: ${runnable-default}
  resources:
    requests:
      cpu: ${100m}
      memory: ${100Mi}
    limits:
      cpu: ${400m}
      memory: ${400Mi}
  runAsApiKey: ${abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz}
  runAsUser: ${iamgroot}
  dryRun: ${true}
```
<center><i>Service YAML Configuration</i></center>

## Configuration Fields

### **`service`**
<b>Description:</b> Service Section <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
service:
  title: alpha-stack-python-file
  servicePort: 8080 
  metricPort: 8093
  ingress:
    {}
```

### **`title`**
<b>Description:</b> Title of the Service <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string <br>
<b>Example Usage:</b>
```yaml
title: Workflow Indexer
```

### **`servicePort`**
<b>Description:</b> This specification creates a new Service object, which targets the TCP port number whose number is given. Ensure that any other service is not using this port else it would replace it. <br>
<b>Data Type:</b> Integer <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any valid port number <br>
<b>Additional Details:</b> Ensure that any other service is not using this port else it would replace it<br>
<b>Example Usage:</b>
```yaml
servicePort: 1234
```

### **`metricPort`**
<b>Description:</b> This specification creates a new Service object, which targets the metric port number whose number is given. <br>
<b>Data Type:</b> Integer <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any valid port number <br>
<b>Additional Details:</b> Ensure that any other service is not using this port else it would replace it<br>

<b>Example Usage:</b>
```yaml
metricPort: 1234
```

### **`ingress`**
<b>Description:</b> Ingress exposes HTTP and HTTPS routes from outside DataOS to services within DataOS. Configure the incoming port for the service to allow access to DataOS resources from external links.<br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory for external paths <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
ingress: 
    enabled: true
    noAuthentication: true
    path: /sample-service 
    stripPath: true
```

### **`enabled`**
<b>Description:</b> Enables the Ingress Port <br>
<b>Data Type:</b> Boolean <br>
<b>Requirement:</b> Mandatory for external paths <br>
<b>Default Value:</b> false <br>
<b>Possible Value:</b> true/false <br>
<b>Example Usage:</b>
```yaml
enabled: true
```

### **`path`**
<b>Description:</b> Provide a path that will be part of the public URL to access the service outside DataOS. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory for external paths <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any valid path <br>
<b>Additional Details:</b>If a service by the same path already exists, it would get replaced<br>
<b>Example Usage:</b>
```yaml
path: /spam-detection
```

### **`stripPath`**
<b>Description:</b> Enable the stripPath to strip the specified path and forward the request to the upstream service <br>
<b>Data Type:</b> Boolean <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> false <br>
<b>Possible Value:</b> true/false <br>
<b>Example Usage:</b>
```yaml
stripPath: true
```

### **`noAuthentication`**
<b>Description:</b> Set noAuthentication to false if authentication is needed. <br>
<b>Data Type:</b> Boolean <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> false <br>
<b>Possible Value:</b> true/false <br>
<b>Example Usage:</b>
```yaml
noAuthentication: false
```

### **`replicas`**
<b>Description:</b> The number of replicated services <br>
<b>Data Type:</b> Integer <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> 1 <br>
<b>Possible Value:</b> Any positive integer<br>
<b>Example Usage:</b>
```yaml
replicas: 2
```

### **`autoScaling`**
<b>Description:</b> Manage autoscaling to match changing application workload levels <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
autoscaling: 
    enabled: true
    minReplicas: 2
    maxReplicas: 4
    targetMemoryUtilizationPercentage: 80
    targetCPUUtilizationPercentage: 80
```

### **`enabled`**
<b>Description:</b> Enables autoscaling <br>
<b>Data Type:</b> Boolean <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> false <br>
<b>Possible Value:</b> true/false <br>
<b>Example Usage:</b>
```yaml
enabled: true
```

### **`minReplicas`**
<b>Description:</b> Minimum number of replicas  <br>
<b>Data Type:</b> Integer <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any positive integer <br>
<b>Example Usage:</b>
```yaml
minReplicas: 2
```

### **`maxReplicas`**
<b>Description:</b> Maximum number of replicas. It must be a value greater than minReplicas. <br>
<b>Data Type:</b> Integer <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any value greater than or equal to minReplicas <br>
<b>Example Usage:</b>
```yaml
maxReplicas: 4
```

### **`targetMemoryUtilizationPercentage`**
<b>Description:</b> Average memory usage of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' CPU utilization is higher than the target you defined, then your replicas will be adjusted. <br>
<b>Data Type:</b> Number <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any number <br>
<b>Example Usage:</b>
```yaml
targetMemoryUtilizationPercentage: 80
```

### **`targetCPUUtilizationPercentage`**
<b>Description:</b> Average CPU usage of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' memory utilization is higher than the target you defined, then your replicas will be adjusted. <br>
<b>Data Type:</b> Number <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any number <br>
<b>Example Usage:</b>
```yaml
targetCPUUtilizationPercentage: 70
```

### **`stack`**
<b>Description:</b> A Stack is a Resource that serves as a secondary extension point, enhancing the capabilities of a Service Resource by introducing additional programming paradigms. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> benthos/beacon/alpha <br>
<b>Additional Details:</b> <br>
- <i>benthos:</i> for Stream Analytics/Event Stream Processing <br>
- <i>beacon:</i> for Web and other applications gain access to PostgreSQL database within DataOS<br>
- <i>alpha:</i> for connecting to Web-Server based application images developed on top of DataOS
 <br>
<b>Example Usage:</b>
```yaml
stack: alpha
```

### **`logLevel`**
<b>Description:</b> Classifies enteries in logs in terms of urgency which helps to filter logs during search and helps control the amount of information in logs <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> INFO <br>
<b>Possible Value:</b> INFO/WARN/DEBUG/ERROR <br>
<b>Additional Details:</b>
- <i>INFO:</i> Designates informational messages that highlight the progress of the service
- <i>WARN:</i> Designates potentially harmful situations
- <i>DEBUG:</i> Designates fine-grained informational events that are most useful while debugging
- <i>ERROR:</i> Desingates error events that might still allow the workflow to continue running
<b>Example Usage:</b>
```yaml
logLevel: WARN
```

### **`envs`**
<b>Description:</b> Environment Variables <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any key-value pair of environment variables <br>
<b>Example Usage:</b>
```yaml
  envs:
    CONTAINER_NAME: 'itsrandom'
```

### **`compute`**
<b>Description:</b> A Compute resource provides processing power for the job.  <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> runnable-default or any other custom compute created by the user<br>
```yaml
compute: runnable-default # Compute Resource
```

### **`resources`**
<b>Description:</b> Resource Configuration <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
resources:
    requests:
        cpu: 100m
        memory: 100Mi
    limits:
        cpu: 400m
        memory: 400Mi
```

### **`requests`**
<b>Description:</b> Requested Resource Configuration <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
requests:
    cpu: 100m
    memory: 100Mi
```

### **`limits`**
<b>Description:</b> Resource limit Configuration <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
limits:
    cpu: 1000m
    memory: 1000Mi
```

### **`cpu`**
<b>Description:</b> CPU Configuration <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> requests: 100m, limits: 400m <br>
<b>Possible Value:</b> Number CPU units in milliCPU(m) or CPU Core <br>
<b>Example Usage:</b>
```yaml
cpu: 1000m
```

### **`memory`**
<b>Description:</b> Memory Configuration <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> requests: 100Mi, limits: 400Mi <br>
<b>Possible Value:</b> Memory in Mebibytes(Mi) or Gibibytes(Gi) <br>
<b>Example Usage:</b>
```yaml
memory: 1000Mi
```

### **`runAsApiKey`**
<b>Description:</b> When the "runAsApiKey" field is configured with the Api Key of a user, it grants the authority to perform operations on behalf of that user. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> Apikey of the User <br>
<b>Possible Value:</b> Any user's valid DataOS API Key <br>
<b>Example Usage:</b>
```yaml
runAsApiKey: abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
```

### **`runAsUser`**
<b>Description:</b> When the "runAsUser" field is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> User-ID of the User <br>
<b>Possible Value:</b> User-ID of the Use-Case Assignee <br>
<b>Example Usage:</b>
```yaml
runAsUser: iamgroot
```

### **`dryRun`**
<b>Description:</b> When enabled, the dryRun property deploys the service to the cluster without submitting it. <br>
<b>Data Type:</b> Boolean <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> false <br>
<b>Possible Value:</b> true/false <br>
<b>Example Usage:</b>
```yaml
dryRun: true
```
