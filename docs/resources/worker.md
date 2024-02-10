# Worker

A **Worker** Resource in DataOS is a long-running process responsible for performing specific tasks or computations indefinitely.

## Key Characteristics

- **Continuous Execution**: Workers are built to run perpetually, performing their assigned tasks without a defined end time.
- **No Ingress**: Workers do not have ingress ports like [Services](./service.md).
- **Throughput-Based**: Workers are throughput-based and do not require synchronous responses.
- **Lightweight**: Workers are lightweight compared to [Services](./service.md), as they do not require multiple open network ports. This makes them faster to deploy and more efficient.
- **Specialized Execution**: Worker is a self-contained system, an independent entity, ideal for executing specific tasks within a larger application, providing focused functionality.
- **Autoscalability**: Workers can be autoscaled to handle larger workloads, making them highly adaptable.
- **Robustness**: Workers are perfect for use cases where robustness and continuous execution are essential.

## Workflow vs. Service vs. Worker

[Workflow](./workflow.md), [Service](./service.md), and Worker are distinct [DataOS Resources](../resources.md), each with unique roles in the ecosystem. Data developers often face the dilemma of deciding when to use a Workflow, a Service, or a Worker in the DataOS environment. To aid in this decision-making process, the following table compares Workflow, Service, and Worker comprehensively, helping developers understand their distinct characteristics and optimal use cases within the DataOS ecosystem.

| Characteristic | Workflow | Service | Worker |
| --- | --- | --- | --- |
| *Overview* | Workflows orchestrate sequences of tasks, jobs, or processes, terminating upon successful completion or failure. | Services are long-running processes that continuously operate, serve, and process API requests. | Workers execute specific tasks or computations continuously without a defined end time. |
| *Execution Model* | Workflows process data in discrete chunks, following predefined DAGs (Directed Acyclic Graphs). | Services expose API endpoints and ingress ports for external data or request intake. They don’t have DAGs. | Workers perform continuous task execution independently, without synchronous inputs or ingress ports. |
| *Data Dependency* | Workflows follow predefined orders or DAGs, depending on data input sequences. | Services rely on incoming data through ingress ports for logic execution. | Workers are throughput-based and do not require synchronous inputs or ingress ports. |
| *Stack Orchestration* | Yes | Yes | Yes |
| *Scope* | Workspace-level | Workspace-level | Workspace-level |
| *Pre-defined Stacks compatibility* | Flare, Flare SDK,  Toolbox, Scanner, Alpha, Soda | Scanner, Alpha, Benthos, Beacon  | Benthos-worker, Scanner |
| *Use Cases* | 1. Batch Data Processing Pipelines: Ideal for orchestrating complex data processing pipelines.<br>2. Scheduled Jobs: Perfect for automating tasks at specific intervals, such as data backups and ETL processes.  | 1. API Endpoints: Used to create API endpoints for various purposes, such as data retrieval and interaction with external systems.<br>2. User Interfaces: Suitable for building interfaces that interact with data or services. | 1. Continuous Processing: Perfect for tasks like real-time analytics, and event-driven operations.<br>2. Independence: Ideal for creating independent systems that perform specific tasks indefinitely. |

## How to create a Worker?

Data developers can create a Worker Resource using a YAML configuration file via the [DataOS CLI.](../interfaces/cli.md)

### **Worker YAML configuration**

A Worker Resource YAML configuration consists of two distinct sections:

- [Resource meta Section](./resource_attributes.md): This section comprises attributes that are shared among all Resource-types.
- [Worker-specific Section](./worker/yaml_configuration_attributes.md): The Worker-specific section contains attributes unique to the Worker Resource.

The configuration of each of these sections is provided in detail below.

### **Configuring the Resource meta section**

In DataOS, a Worker is categorized as a [Resource-type](../resources/types_of_dataos_resources.md). The YAML configuration file for a Worker Resource includes a Resource meta section, which encompasses attributes shared among all Resource-types. 

The following YAML excerpt illustrates the attributes that are specified within this section:

```yaml
name: ${{my-worker}}
version: v1beta 
type: worker
layer: user 
tags: 
  - ${{dataos:type:resource}}
  - ${{dataos:resource:worker}}
description: ${{this worker resource is for a data product}}
owner: ${{iamgroot}}
worker: # worker-specific section
  ${{worker-specific Attributes}}
```
<center><i>Resource meta section</i></center>

For additional information about the attributes within the Resource meta section, please consult the [Attributes of Resource meta section.](./resource_attributes.md)

### **Configuring Worker-specific section**

The below YAML provides a high-level structure for the Worker-specific section:

```yaml
worker: 
	title: ${{title of worker}}
	tags:
		- ${{tag 1}}
		- ${{tag 2}}
	replicas: ${{worker replicas}}
	autoscaling: 
		enabled: ${{enable autoscaling}}
		minReplicas: ${{minimum replicas}}
		maxReplicas: ${{maximum replicas}}
		targetMemoryUtilizationPercentage: ${{60}}
		targetCPUUtilizationPercentage: ${{70}}
	stack: ${{stack name and version}} 
	logLevel: ${{log level}}
	configs: 
		${{additional configuration}}
	envs: 
		${{environment variable configuration}}
	secrets: 
		- ${{secret configuration}}
	dataosSecrets:
		${{dataos secret resource configuration}}
	dataosVolumes: 
		${{dataos volumes resource configuration}} 
	tempVolume: hola
	persistentVolume: 
		${{persistent volume configuration}}
	compute: runnable-default 
	resources:
		requests:
			cpu: ${{cpu requests}}
			memory: ${{memory requests}}
		limits:
			cpu: ${{cpu limits}}
			memory: ${{memory limits}}
	dryRun: ${{enables dryrun}}
	runAsApiKey: ${{dataos apikey}}
	runAsUser: ${{dataos user-id}}
	topology:
		${{worker topology}}
	stackSpec: 
		${{Stack-specific Attributes}}
```
<center><i>Resource meta section</i></center>

Here's a summary of the attributes within the Worker-specific section:

| Attribute | Data Type | Default Value | Possible Values | Requirement |
| --- | --- | --- | --- | --- |
| [`worker`](./worker/yaml_configuration_attributes.md#worker) | mapping | none | none | mandatory |
| [`title`](./worker/yaml_configuration_attributes.md#title) | string | none | any valid string | optional |
| [`tags`](./worker/yaml_configuration_attributes.md#tags) | list of strings | none | list of valid strings | optional |
| [`replicas`](./worker/yaml_configuration_attributes.md#replicas) | integer | 1 | any positive integer | optional |
| [`autoscaling`](./worker/yaml_configuration_attributes.md#autoscaling) | mapping | none | valid autoscaling configuration | optional |
| [`stack`](./worker/yaml_configuration_attributes.md#stack) | string | none | valid stack name | mandatory |
| [`logLevel`](./worker/yaml_configuration_attributes.md#loglevel) | string | info | INFO, DEBUG, WARN, ERROR | optional |
| [`configs`](./worker/yaml_configuration_attributes.md#configs) | mapping | none | valid custom configurations in key-value format | optional |
| [`envs`](./worker/yaml_configuration_attributes.md#envs) | mapping | none | valid environment variable definitions | optional |
| [`secrets`](./worker/yaml_configuration_attributes.md#secrets) | list of secrets | none | list of secret definitions | optional |
| [`dataosSecrets`](./worker/yaml_configuration_attributes.md#dataossecrets) | list of mappings | none | list of DataOS Secret Resource definitions | optional |
| [`dataosVolumes`](./worker/yaml_configuration_attributes.md#dataosvolumes) | list of mappings | none | list of DataOS Volume Resource definitions | optional |
| [`tempVolume`](./worker/yaml_configuration_attributes.md#tempvolume) | string | none | valid volume name | optional |
| [`persistentVolume`](./worker/yaml_configuration_attributes.md#persistentvolume) | mapping | none | valid persistent volume definition | optional |
| [`compute`](./worker/yaml_configuration_attributes.md#compute) | string | none | runnable-default or any other custom Compute Resource name | mandatory |
| [`resources`](./worker/yaml_configuration_attributes.md#resources) | mapping | none | valid CPU and memory resource requests and limits | optional |
| [`dryRun`](./worker/yaml_configuration_attributes.md#dryrun) | boolean | false | true or false | optional |
| [`runAsApiKey`](./worker/yaml_configuration_attributes.md#runasapikey) | string | none | valid DataOS API key | optional |
| [`runAsUser`](./worker/yaml_configuration_attributes.md#runasuser) | string | none | valid user identity | optional |
| [`topology`](./worker/yaml_configuration_attributes.md#topology) | list of mappings | none | list of topology element definitions | mandatory |
| [`stackSpec`](./worker/yaml_configuration_attributes.md#stackspec) | mapping | none | valid stack-specific attributes | optional |

By configuring these sections as needed, data developers can create highly customizable Worker Resources. For a detailed explanation of the attributes within the Worker-specific section, you can refer to the [Attributes of Worker-specific section.](./worker/yaml_configuration_attributes.md)

### **Apply the Worker YAML**

After creating the YAML configuration file for the Worker Resource, it's time to apply it to instantiate the Resource-instance in the DataOS environment. To apply the Worker YAML file, utilize the [`apply`](../interfaces/cli/command_reference.md#apply) command.

```shell
dataos-ctl apply -f ${{yaml config file path}} - w ${{workspace name}}
# Sample
dataos-ctl apply -f dataproducts/new-worker.yaml -w curriculum
```

<details>
<summary>Sample Worker YAML</summary>
    
```yaml
name: benthos3-worker-sample
version: v1beta
type: worker
tags:
    - worker
    - dataos:type:resource
    - dataos:resource:worker
    - dataos:layer:user
    - dataos:workspace:public
description: Random User Console
worker:
    tags:
    - worker
    replicas: 1
    stack: benthos-worker:3.0
    logLevel: DEBUG
    compute: runnable-default
    resources:
    requests:
        cpu: 100m
        memory: 128Mi
    limits:
        cpu: 1000m
        memory: 1024Mi
    stackSpec:
    input:
        http_client:
        headers:
            Content-Type: application/octet-stream
        url: https://randomuser.me/api/
        verb: GET
    output:
        stdout:
        codec: |
            delim:
            -----------GOOD------------
```
</details>

### **Verify Worker Creation**

To ensure that your Worker has been successfully created, you can verify it in two ways:

Check the name of the newly created Worker in the list of workers created by you in a particular Workspace:

```shell
dataos-ctl get -t worker - w ${{workspace name}}
# Sample
dataos-ctl get -t worker -w curriculum
```

Alternatively, retrieve the list of all Workers created in the Workspace by appending `-a` flag:

```shell
dataos-ctl get -t worker -w ${{workspace name}} -a
# Sample
dataos-ctl get -t worker -w curriculum
```

You can also access the details of any created Worker through the DataOS GUI in the Resource tab of the  [Operations App.](../interfaces/operations.md)

### **Deleting a Worker**

Use the [`delete`](../interfaces/cli/command_reference.md#delete) command to remove the specific Worker Resource-instance from the DataOS environment. There are three ways to delete a Worker as shown below.

**Method 1:** Copy the name to Workspace from the output table of the [`get`](../interfaces/cli/command_reference.md#get) command and use it as a string in the delete command.

Command

```shell
dataos-ctl delete -i "${{name to workspace in the output table from get status command}}"
```

Example:

```shell
dataos-ctl delete -i "cnt-product-demo-01 | v1beta | worker | public"
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0001] 🗑 deleting(public) cnt-product-demo-01:v1beta:worker...
INFO[0003] 🗑 deleting(public) cnt-product-demo-01:v1beta:worker...deleted
INFO[0003] 🗑 delete...complete
```

**Method 2:** Specify the path of the YAML file and use the [`delete`](../interfaces/cli/command_reference.md#delete) command.

Command:

```shell
dataos-ctl delete -f ${{file-path}}
```

Example:

```shell
dataos-ctl delete -f /home/desktop/connect-city/config_v1.yaml
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0000] 🗑 deleting(public) cnt-city-demo-010:v1beta:worker...
INFO[0001] 🗑 deleting(public) cnt-city-demo-010:v1beta:worker...deleted
INFO[0001] 🗑 delete...complete
```

**Method 3:** Specify the Workspace, Resource-type, and Worker name in the [`delete`](../interfaces/cli/command_reference.md#delete) command.

Command:

```shell
dataos-ctl delete -w ${{workspace}} -t worker -n ${{worker name}}
```

Example:

```shell
dataos-ctl delete -w public -t worker -n cnt-product-demo-01
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0000] 🗑 deleting(public) cnt-city-demo-010:v1beta:worker...
INFO[0001] 🗑 deleting(public) cnt-city-demo-010:v1beta:worker...deleted
INFO[0001] 🗑 delete...complete
```


## Attributes of Worker YAML

The Attributes of Worker YAML define the key properties and configurations that can be used to specify and customize Worker Resources within a YAML file. These attributes allow data developers to define the structure and behavior of their Worker Resources. For comprehensive information on each attribute and its usage, please refer to the link: [Attributes of Worker YAML.](./worker/yaml_configuration_attributes.md)

## Worker Templates

The Worker templates serve as blueprints, defining the structure and configurations for various Workers. To know more, refer to the link: [Worker Templates.](./worker/templates.md)

## Worker Command Reference

Here is a reference to the various commands related to managing Workers in DataOS:

- **Applying a Worker:** Use the following command to apply a Worker using a YAML configuration file:
    
    ```shell 
    dataos-ctl apply -f ${{yaml config file path}} -w ${{workspace}}
    dataos-ctl resource apply -f ${{yaml config file path}} -w ${{workspace}}
    # Sample
    dataos-ctl resource apply -f worker/worker.yaml -w curriculum
    dataos-ctl resource apply -f worker/worker.yaml -w curriculum
    ```
    
- **Get Worker Status:** To retrieve the status of a specific Worker, use the following command:
    
    ```shell
    dataos-ctl get -t worker -w ${{workspace name}}
    # Sample
    dataos-ctl get -t worker -w curriculum
    ```
    
- **Get Status of all Workers within a Workspace:** To get the status of all Workers within the current context, use this command:
    
    ```shell
    dataos-ctl get -t worker -w ${{workspace name}} -a
    # Sample
    dataos-ctl get -t worker -w curriculum -a
    ```
    
- **Generate Worker JSON Schema:** To generate the JSON schema for a Worker with a specific version (e.g., v1alpha), use the following command:
    
    ```shell
    dataos-ctl develop schema generate -t worker -v ${{version}}
    # Sample
    dataos-ctl develop schema generate -t worker -v v1alpha
    ```
    
- **Get Worker JSON Resource Schema:** To obtain the JSON resource schema for a Worker with a specific version (e.g., v1alpha), use the following command:
    
    ```shell
    dataos-ctl develop get resource -t worker -v ${{version}}
    # Sample
    dataos-ctl develop get resource -t worker -v v1alpha
    ```
    
- **Delete Workers:** To delete a specific worker you can use the below command
    
    ```shell
    dataos-ctl delete -t worker -w ${{workspace name}} -n ${{name of worker}}
    # Sample
    dataos-ctl delete -t worker -w curriculum -n benthos3-worker
    ```