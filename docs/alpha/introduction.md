# Introduction

DataOS provides various stacks to accomplish different kinds of functionality. You can use **Flare**, a Spark-backed data-processing engine, to create complex workflows to carry out the data processing tasks. For querying, you have SQL query engine, **Minerva**,  **Surge** for Complex Event Processing, and **Benthos**; for mundane stream workloads. 
 
DataOS gives you a convenient way to use Alpha stack to add ad-hoc functionalities on top of DataOS. You can develop your application and create an image of it. This image can be exposed to the DataOS using the Alpha stack. 

All the functionality and logic are written within your application, and then this logic is executed within DataOS using Alpha stack.

You can add ingress and autoscaling capabilities to your application. You can also make it part of a workflow.

## Deploy application 

The following steps describe how to deploy an application as a service using DataOS Alpha stack.

1. Package your application into a Docker image.

2. [Create a service using Alpha stack](#create-a-service)

3. [Define policy for your application](#define-a-policy)

### Create a Service
Provide the following configuration properties:

- **replicas**: Create multiple replicated services.
- **autoscaling**: Manage autoscaling to match changing application workload levels
```yaml
  autoScaling:
    enabled: true
    minReplicas: 2
    maxReplicas: 4
    targetMemoryUtilizationPercentage: 80
    targetCPUUtilizationPercentage: 80
```
- **ingress**: Configure the incoming port for the service to allow access to DataOS resources from external links.
  Provide the following properties.
     - enable ingress port
     - provide path that will be part of public url to access the service from outside dataOS
     - enable the stripPath to strip the specified path and then forward the request to the upstream service.
     - Set noAuthentication to false if authentication is needed.
```yaml
  ingress:
    enabled: true
    noAuthentication: true
    path: <path>                  
    stripPath: true
```

- **image**: Latest application docker image 
```yaml
  stack: alpha
    alpha:
      image: <docker-image>
```
- **arguments**: to pass arguments to the application

Here is the complete example YAML for a Swagger UI that enable users try out the API calls directly in the browser.

```yaml
version: v1beta1
name: swaggerui
type: service

service:
  title: Swagger UI
  replicas: 1
  servicePort: 8080
  
  ingress:                                # configure ingress
    enabled: true
    noAuthentication: true
    path: /swagger-ui                     # 
    stripPath: true

  envs:
    LOG_LEVEL: info
  
  stack: alpha
  alpha:
    image: swaggerapi/swagger-ui           # docker image
```

### Define a Policy 
Allow users to perform specific set of operations using the application.
```yaml
name: "swagger-ui"
version: v1beta1
type: policy
layer: system
description: "Allow user to access swagger-ui static files"
policy:
  access:
    subjects:
      tags:
        - - "dataos:u:user"                 
    predicates:             
      - "GET"
      - "POST"
      - "OPTIONS"
    objects:
      paths:
        - "/swagger-ui"
    allow: true
```

The following example shows how to define the arguments that are passed for the multiple commands to be executed by the data tool.
```yaml
version: v1beta1
name: dataos-tool-add-prop
type: workflow
workflow:
  dag:
   - name: dataos-tool-add-prop
  spec:
  envs:
    LOG_LEVEL: debug
  stack: alpha
  alpha:
    image: <docker-image>
    arguments:
      - dataset
      - add-properties
         - --address
         - dataos://icebase:retail/city_pulsar_01
         - --property
         - write.metadata.previous-versions-max:3
```
