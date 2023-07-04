# Service

A Service represents a long-running process that acts as a receiver and/or provider of APIs. It serves as a fundamental resource in the DataOS ecosystem, catering to various scenarios involving continuous real-time and streaming data flow. Whether it's event processing, streaming IoT data, log processing for network devices, real-time stock trade analysis, or dynamic user interfaces (UIs), the Service resource enables data developers to gather, process, and analyze real-time/streaming data flow, enabling timely insights and swift response to the latest information.

While resembling a workflow in some aspects, a Service differentiates itself by not employing Directed Acyclic Graphs (DAGs). Instead, a Service is provisioned as a runnable entity, albeit limited to utilizing a single stack at a time. This contrasts with a Workflow, which can accommodate multiple jobs running on separate stacks simultaneously.

## Core Concepts

### **Ports and Sockets**

The Service resource is equipped with a port and a socket, for data reception and transmission. By listening on a specific URL port, the Service facilitates the posting or retrieval of data. The presence or absence of these ports and sockets depends on the specific use case requirements and objectives.

### **Replicas**

To achieve robust scalability, the Service resource introduces the concept of replicas. Replicas ensure a stable set of identical Kubernetes Pods that run the Service concurrently. This mechanism guarantees availability by maintaining a specified number of Pods, enabling the Service to effortlessly handle heavy workloads without succumbing to failure.


## Syntax of a service

The Service resource is configured using a YAML file, consisting of several rooted sections. The syntax for a Service YAML is given below:

<center>

![Syntax of a Service](./service/service_yaml.png)

</center>


<center>

<i>YAML Syntax of a Service Resource</i>

</center>

## Creating a Service

To understand how a Service works, let’s take a case scenario where a user wants to bring the data from a web app using Google Tag Manager to draw up insights in real-time. This would involve sending all the captured data by Google Tag Manager to an API, applying some transformations, and writing it to, let’s say, a streaming source, Kafka. This would require a Service that would keep listening to the Google Tag Manager API and sync all the data to Kafka in real time. To know more, please refer to the following [link](./service/creating-a-service.md)

## Service YAML Configuration Field Reference

The table below presents an exhaustive list of key-value properties and their descriptions within a Service YAML file:

<center>

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| `service` | object | None | None | Mandatory |
| `title` | string | None | Any string | Optional |
| `servicePort` | integer | None | Any valid service port | Optional |
| `metricPort` | integer | None | Any valid metric port | Optional |
| `ingress` | object | None | None | Mandatory**  |
| `enabled` | boolean | false | true/false | Mandatory** |
| `path` | string | None | Any valid path | Mandatory** |
| `stripPath` | boolean | false | true/false | Mandatory** |
| `noAuthentication` | boolean | false | true/false | Optional |
| `replicas` | integer | 1 | Any positive integer | Optional  |
| `autoscaling` | object | None | None | Optional |
| `enabled` | boolean | false | true/false | Optional |
| `minReplicas` | integer | 1 | Any positive integer | Optional  |
| `maxReplicas` | integer | 1 | Any positive integer | Optional  |
| `targetMemoryUtilizationPercentage` | integer | None | Any positive integer | Optional  |
| `targetCPUUtilizationPercentage` | integer | None | Any positive integer | Optional  |
| `stack` | string | None | benthos/alpha/beacon | Mandatory |
| `logLevel` | string | INFO | INFO/WARN/DEBUG/ERROR | Optional |
| `envs` | object | None | Key-value pairs of environment variables | Optional |
| `compute` | string | None | runnable-default or any other custom Compute Resource | Mandatory |
| `resources` | object | None | None | Optional  |
| `requests` | object | None | None | Optional  |
| `limits` | object | None | None | Optional  |
| `cpu` | string | requests: 100m, limits: 400m | CPU units in milliCPU(m) or CPU Core | Optional  |
| `memory` | string | requests: 100Mi, limits: 400Mi | Memory in Mebibytes(Mi) or Gibibytes(Gi) | Optional  |
| `runAsApiKey` | string | User's API Key | Any valid DataOS API Key | Optional  |
| `runAsUser` | string | User's User-id | UserID of Use-Case Assignee | Optional  |
| `dryRun` | boolean | false | true/false | Optional |

</center>


<i>Mandatory**:</i> Fields mandatory for external paths, but optional for internal paths.

For a detailed explanation of each field, consult the [Service YAML Field Reference](./service/service_yaml_field_reference.md)