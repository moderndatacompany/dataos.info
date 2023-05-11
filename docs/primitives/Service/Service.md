# Service

A Service is a long-running process that is receiving and/or serving an API. Service is a primitive/Resource in the DataOS ecosystem for scenarios that need a continuous flow of real-time data such as handling event processing, streaming IoT, network devices log processing, real-time stock trades, user interface (UI), etc. DataOS Service makes it easy to gather, process, and scrutinize streaming data so you can get timely insights and react quickly to the latest information. 

A Service has a port and a socket to receive and get data. It will listen on a port on a specific URL, either you can post data to it or get data from it. The opening/closing and presence/absence of port and socket depend on what use case one wants to solve.

To scale robustly, a service has the notion of replicas. A replica enables you to maintain a stable set of replica Kubernetes Pods running a Service at any given time. It guarantees the availability of a specified number of identical Pods, thus enabling the service to scale up while handling heavy workloads without failure.

Just as a workflow, a Service is provisioned as a runnable, but it doesn’t have Directed Acyclic Graphs (DAGs). A single Service can utilize one stack at a time, unlike a Workflow which can have multiple jobs running on separate stacks.

## Syntax of a service

In DataOS, you configure a service in a YAML file consisting of several [properties](./Service.md). The syntax for the YAML is given below:

```yaml
version: v1 #(Mandatory)
name: sv-tmdc #(Mandatory)
type: service #(Mandatory)
tags: #(Optional)
  - event
  - service
description: This is a template for defining a service #(Optional)
service: #(Mandatory)
  title: "Title of a service" #(Optional)
  replicas: 1 #(Optional - By default its 1) 
  autoScaling: #(Optional)
    enabled: true 
    minReplicas: 2 
    maxReplicas: 4 
    targetMemoryUtilizationPercentage: 80 
    targetCPUUtilizationPercentage: 80 
  ingress: #(Mandatory)
    enabled: true 
    stripPath: false 
    path: /hit-collector 
    noAuthentication: true 
  stack: <stack-name> #(Mandatory) Stack Name could be Benthos, Alpha, Beacon
  logLevel: info #(Optional)
  dryRun: true #(Optional)
  servicePort: 8099 #(Optional)
  stack-name: #(Mandatory) 
    {} #(Stack specific properties)
```
    
      To understand how a Service works, let’s take a case scenario where a user wants to bring the data from a web app using Google Tag Manager to draw up insights in real-time. This would involve sending all the captured data by Google Tag Manager to an API, applying some transformations, and writing it to, let’s say, a streaming source, Kafka. This would require a Service that would keep listening to the Google Tag Manager API and sync all the data to Kafka in real time.
      
  <br>

  Diagrammatic Representation of Sample Service
       
<center>

![Picture](./Blank_diagram.svg)

</center>

  Sample Service YAML 
      
  ```yaml
      version: v1 # Version
      name: hit-collector-service # Service Name
      type: service # Type here is Service
      tags: # Tags
        - collector
        - hit
        - gtm
        - event
        - service
      description: Receives Hit data and Sinks to DataOS stream # Description
      
      service: # Service Section
        title: "Hit Collector Service" # Title of the Service
        replicas: 1 # Replicas
      
        autoScaling: # Autoscaler
          enabled: true
          minReplicas: 2
          maxReplicas: 4
          targetMemoryUtilizationPercentage: 80
          targetCPUUtilizationPercentage: 80
      
        ingress: # Ingress
          enabled: true
          stripPath: false
          path: /hit-collector
          noAuthentication: true
      
        stack: benthos # Stack Name
        logLevel: INFO
        dryRun: true
        servicePort: 8099 # Service Port
      
      # Benthos Stack-Specific Properties
        benthos:
      
      # Input (From Google Tag Manager API)
          input:
            http_server:
              address: 0.0.0.0:8099
              path: /hit-collector
              allowed_verbs:
                - POST
              timeout: 5s
            processors:
            - log:
                level: INFO
                message: hit collector - received hit...
      
      # Pipeline (Processing)
          pipeline:
            processors:
            - log:
                level: DEBUG
                message: processing message...
            - log:
                level: DEBUG
                message: ${! meta() }
            - bloblang: meta status_code = 200
            - for_each:
              - conditional:
                  condition:
                    type: processor_failed
                  processors:
                  - log:
                      level: ERROR
                      message: 'Schema validation failed due to: ${!error()}'
                  - bloblang: meta status_code = 400
                  - log:
                      level: DEBUG
                      message: ${! meta() }
                  - bloblang: |
                      root.payload = this.string().encode("base64").string()
                      root.received_at = timestamp("2006-01-02T15:04:05.000Z")
                      root.metadata = meta()
                      root.id = uuid_v4()
            - log:
                level: DEBUG
                message: processing message...complete
            threads: 1
      
      # Output (Into Kafka Depot)
          output:
            broker:
              outputs:
              - broker:
                  outputs:
                  - type: dataos_depot
                    plugin:
                      address: dataos://kafkapulsar:default/gtm_hits_dead_letter01
                      metadata:
                        type: STREAM
                        description: The GTM Hit Error Data Stream
                        format: json
                        schema: '{"type":"record","name":"default","namespace":"default","fields":[]}'
                        tags:
                        - hit
                        - gtm
                        - stream
                        - error-stream
                        - dead-letter
                        title: GTM Hit Error Stream
                  - type: sync_response
                  pattern: fan_out
                processors:
                - bloblang: root = if !errored() { deleted() }
              - broker:
                  outputs:
                  - type: dataos_depot
                    plugin:
                      address: dataos://kafkapulsar:default/gtm_hits01
                      metadata:
                        type: STREAM
                        description: The GTM Hit Data Stream
                        format: json
                        schema: '{"type":"record","name":"default","namespace":"default","fields":[]}'
                        tags:
                        - hit
                        - gtm
                        - event
                        - stream
                        title: GTM Hit Stream
                  - type: sync_response
                  pattern: fan_out
                processors:
                - bloblang: root = if errored() { deleted() }
              pattern: fan_out
```

## Building Blocks of a Service

The below table summarizes various properties within a Service YAML

| Property | Description | Example | Default Value | Possible Value | Rules | Field (Optional / Mandatory) |
| --- | --- | --- | --- | --- | --- | --- |
| `version` | Manifest Version. It allows iteration on the schema.  | `version: v1` | NA | `v1` | Configure all the properties according to the manifest version. Currently, it’s `v1`.  | Mandatory |
| `name` | Defines the name of the service. | `name: sv-pulsar-01` | NA | Any valid name that conforms to the rule. | Rules for name: 37 alphanumeric characters and a special character '-' allowed. `[a-z0-9]([-a-z0-9]*[a-z0-9])`. The maximum permissible length for the name is 47, as showcased on CLI. Still, it's advised to keep the name length less than 30 characters because Kubernetes appends a Unique ID in the name which is usually 17 characters. Hence reduce the name length to 30, or your service will fail. | Mandatory |
| `type` | The type of primitive/Resource. | `type: service` | NA | The type here is `service`. (For other primitive/Resources it could be `workflow`, `depot`, etc.) | The name of the primitive/Resource should be only in lowercase characters. Else it will throw an error. | Mandatory |
| `tags` | Tags are arrays of strings. These are attributes, and keywords qualifying the service. They are used in access control and quick search. | `tags:` <br>&nbsp;&nbsp;&nbsp;&nbsp;`- Pulsar` <br>&nbsp;&nbsp;&nbsp;&nbsp;`- IoT` | NA | NA | The tags are case-sensitive, so `Connect` and `CONNECT` will be different tags. There is no limit on the length of the tag. In order to assign an output dataset in the Bronze/Silver/Gold categories within Metis UI we can use the tag-like `tier.Bronze/tier.Silver/tier.Gold.` | Optional |
| `description` | Text describing the service. | `description: Service for an external API to Fastbase`  | NA | NA | There is no limit on the length of the description.  | Optional |
| `owner` | The `user-id` of the owner of the service. | `owner: iamgroot` | `user:id` of the resource owner (Can be seen by running the `dataos-ctl user get` command after logging in) in the Tags Section. | NA | The `owner` should be in all lowercase letters `[a-z]`, and another unique character - allowed. You cannot use a different user’s `user:id`, if you do you will encounter a Forbidden Error. Users with operator-level permissions or `roles:id:operator` can use another owner name, but the login token remains the same, thus making every owner of a service unique. | Optional |
| `service` | Corresponding section for service. | `service: {}` | NA | NA | For service, the key should be `service`. | Mandatory |
| `replicas` | The number of replicated services. | `replicas: 1` | 1 | Any integer greater than or equal to 1 | The replicas number should be an integer greater than or equal to 1. | Optional |
| `ingress` | Ingress exposes HTTP and HTTPS routes from outside DataOS to services within DataOS. Configure the incoming port for the service to allow access to DataOS resources from external links. | `ingress:` <br>&nbsp;&nbsp;&nbsp;&nbsp;`enabled: true` <br>&nbsp;&nbsp;&nbsp;&nbsp;`noAuthentication: true` <br>&nbsp;&nbsp;&nbsp;&nbsp;`path: /sample-service` <br>&nbsp;&nbsp;&nbsp;&nbsp;`stripPath: true` | Default Values for sub-properties: <br><br>`enabled: false` <br>`noAuthentication: false` <br>`&path: NA` <br>`stripPath: false` | Possible Values for sub-properties: <br><br>`enabled: true/false` <br>`noAuthentication: true/false` <br>`path: valid path` <br>`stripPath: true/false` | `enabled`: Enables the ingress port <br>`noAuthentication`: Set noAuthentication to false if authentication is needed. <br>`path`: Provide a  path that will be part of the public URL to access the service outside DataOS. If a service by the same path already exists, it would get replaced. <br>`stripPath`: Enable the stripPath to strip the specified path and forward the request to the upstream service. | Mandatory |
| `autoscaling` | Manage autoscaling to match changing application workload levels. | `autoscaling`: <br>&nbsp;&nbsp;&nbsp;&nbsp;`enabled: true` <br>&nbsp;&nbsp;&nbsp;&nbsp;`minReplicas: 2` <br>&nbsp;&nbsp;&nbsp;&nbsp;`maxReplicas: 4` <br>&nbsp;&nbsp;&nbsp;&nbsp;`targetMemoryUtilizationPercentage: 80` <br>&nbsp;&nbsp;&nbsp;&nbsp;`targetCPUUtilizationPercentage: 80` | Default Values for sub-properties: <br><br>`enabled: false` <br>`minReplicas: NA` <br>`maxReplicas: NA` <br>`targetMemoryUtilizationPercentage:NA` <br>`targetCPUUtilizationPercentage:NA` | Default Values for sub-properties: <br><br>`enabled: false/true` <br>`minReplicas: <Integer>`  <br>`maxReplicas: <Integer>` <br>`targetMemoryUtilizationPercentage: <between 1 to 100>` <br>`targetCPUUtilizationPercentage: <between 1 to 100>` | `enabled`: Enables autoscaling <br>`minReplicas`: Minimum number of pods that can be scaled down. <br>`maxReplicas`: Maximum pods that can be scaled up. It must be a value greater than minReplicas. <br>`targetMemoryUtilizationPercentage`: Average memory usage of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' CPU utilization is higher than the target you defined, then your replicas will be adjusted. <br>`targetCPUUtilizationPercentage`: Average CPU usage of all pods in a deployment across the last minute divided by the requested CPU of this deployment. If the mean of the pods' memory utilization is higher than the target you defined, then your replicas will be adjusted. | Optional |
| `logLevel` | Environment Variables. | `logLevel: INFO` | `INFO` | `INFO`, `WARN`, `ERROR`, `DEBUG` | NA | Optional |
| `stack` | Stacks are utilized to perform different kinds of functionality. Currently supported stacks in Service are Alpha, Beacon, and  Benthos. | `stack: benthos` | NA | `benthos`, `beacon`, `alpha`| `benthos`: for Stream Analytics/Event Stream Processing. <br>`beacon`: allows web and other applications access to PostgreSQL databases within DataOS. <br>`alpha`: helps you connect with web-server-based application images developed on top of DataOS. | Mandatory |
| `dryRun` | When enabled, the dryRun property deploys the service to the cluster without submitting it. | `dryRun: true` | `false` | `true`/`false` | NA | Optional |
| `servicePort` | This specification creates a new Service object, which targets the TCP port number whose number is given. Ensure that any other service is not using this port else it would replace it. | `servicePort: 1234` | NA | NA | Should be a valid servicePort. | Mandatory |

## Running a Service

Run the `apply` command on DataOS CLI to create the service resource in DataOS environment.

```bash
dataos-ctl apply -f <filename.yaml> -w <name of the workspace>
```

To learn more about `apply` command, refer to the [CLI](../../CLI/CLI.md) section.