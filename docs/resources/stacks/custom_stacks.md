# How to create your own Stack?

## Prerequisites

### **Understanding of Docker and Kubernetes**

A foundational grasp of Docker and Kubernetes is essential for the creation of basic Stacks. The data developer is expected to proficiently containerize application code. For more advanced Stacks, involving custom Operators (like Flink Operators, Spark Operators, etc. just to name a few), expertise in *Kubernetes Operators* and *Custom Resource Definitions (CRDs)* is recommended.

### **JSON Schema Proficiency**

A data developer must possess familiarity with JSON schema. JSON schemas play a crucial role in validating applied YAML manifest specs against predefined JSON schema within the Stack definition. This involves specifying attributes, their data types, and their required status in the JSON schema.

### **Go Text Templates Proficiency**

A data developer must be familiar with how the Go text templates are defined, as these are integral while specifying YAML configuration file templates and Resource configuration templates within the Stack definition.

## Building a Stack

The below points outline the high-level steps involved in the creation of a custom Stack Resource within the DataOS instance.

1. [Define the Stack image](#definition-of-stack-image)
2. [Create a Stack YAML manifest](#creation-of-stack-manifest)
    <br>a. [Configure the Resource meta section](#configure-the-resource-meta-section)
    <br>b. [Configure the Stack-specific section](#configure-the-stack-specific-section)
3. [Apply the Stack YAML manifest](#apply-the-stack-yaml)

### **Definition of Stack Image**

The initial and primary phase in the creation of a new Stack involves the development of its code. The Stack image serves as a comprehensive representation of all the functionalities and capabilities inherent in the Stack, along with delineating its interaction dynamics with its orchestrating Resource.

<aside class="best-practice">
🗣 <b>Best Practice:</b> When crafting a customized Stack, it is advisable to assess the basic functionality of the Stack by testing its vanilla image on the <a href="/resources/stacks/alpha/">Alpha</a> Stack.

</aside>

In order for a Stack to leverage the existing DataOS guarantees, such as depot and native governance, a data developer must create a layer on its code using the DataOS Software Development Kits (SDKs). For a detailed insight into this process, refer to the reference code implementations of the [DataOS Soda-Python Stack](https://bitbucket.org/rubik_/dataos-soda-py/src/master/), [DataOS Steampipe Stack](https://bitbucket.org/rubik_/dataos-steampipe/src/master/), and the [DataOS DBT Stack](https://bitbucket.org/rubik_/dataos-dbt/src/main/).

Upon completion, containerize the code and transfer it to a container registry.

<aside class="callout">
🗣 When pushing the image to a container registry, document the details of names of <code>registry</code>, <code>repository</code>, <code>image</code>, and <code>tag</code>. These particulars are later utilized in the Stack YAML manifest for pulling the image from the container registry. For a private container registry, authentication details can be provided in the form of Secret Resource and can be referenced within the YAML manifest using the <code>imagePullSecret</code> attribute. For more information about pulling images from private container registry, refer to the link: <a href="/resources/secret/referencing_secrets/referencing_secrets_to_pull_images_from_private_container_registry/">Referencing Secrets to pull images from private container registry</a>.

</aside>

### **Creation of Stack YAML manifest**

After the successful creation and upload of the Stack image to a container registry, the subsequent step involves creating a Stack YAML manifest. 

The ensuing sections delineate the various sections of a Stack YAML.

#### **Configure the Resource meta section**

In DataOS, a Stack is categorized as a [Resource-type](../types_of_dataos_resources.md). The Resource meta section within the YAML manifest encompasses attributes universally applicable to all Resource-types. The provided YAML codeblock elucidates the requisite attributes for this section:

```yaml
name: ${{my-stack}}
version: v1alpha 
type: stack
tags: 
  - ${{dataos:type:resource}}
  - ${{dataos:resource:stack}}
description: ${{This is a sample stack yaml manifest}}
owner: ${{iamgroot}}
stack: # Stack-specific Section
  ${{Attributes of Stack-specific section}}
```

For detailed information on the attributes within the Resource meta section, please refer to [Attributes of Resource Section](../resource_attributes.md).

#### **Configure the Stack-specific section**

The Stack-specific section delineates attributes exclusive to the Stack Resource. The provided code block illustrates a sample Stack-specific section:

```yaml
stack:
# Stack meta section
  name: benthosnew
  version: "3.0"
  reconciler: "stackManager"

# DataOS Address JqFilter
	dataOsAddressJqFilters:
	  - .inputs[]
    - .outputs[]

# Secret Projection
  secretProjection:
    type: "propFile"

# Image Specification section
  image:
    registry: docker.io
    repository: rubiklabs
    image: benthos-ds
    tag: 0.8.15-dev
    auth:
      imagePullSecret: dataos-container-registry

# Command and Argument section
  command:
    - /opt/dataos/benthos-ds
  arguments:
    - run
    - -c
    - /etc/dataos/config/jobconfig.yaml

# Stack Spec Value JSON Schema
  stackSpecValueSchema:
    jsonSchema: |
      {"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"input":{"type":"object"},"metrics":{"type":"object"},"logger":{"type":"object"},"http":{"type":"object"},"pipeline":{"type":"object"},"output":{"type":"object"}},"required":["input"]}

# Orchestrator (Worker/Service/Workflow configuration)
  serviceConfig:
    configFileTemplate: |
      jobconfig.yaml: |
      {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
        logger:
         level: {{.ApplicationSpec.LogLevel}}
         add_timestamp: true
         format: json
         static_fields:
           '@service': {{.Name}}
        http:
         address: 0.0.0.0:{{.MetricPort}}
         root_path: /dataos-benthos
         debug_endpoints: false
        metrics:
         prometheus:
            push_url: "http://prometheus-pushgateway.sentinel.svc.cluster.local:9091"
            push_interval: "5s"
            push_job_name: "{{ .Name }}-{{ .Type }}{{ .Stamp }}"
```

The Stack-specific section consist of the following sections that need to be further configured for a Stack Resource-instance to come to life. 

**Stack meta section**

The Stack Meta Section delineates metadata attributes providing a distinctive identity to the Stack Resource for discoverability and version control. The following code block specifies the attributes to be declared within this section:

```yaml
name: mystack
flavor: python
version: 2.0
reconciler: StackManager
```

The attributes for the Stack meta section are summarized in the table below.

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`stack`](./custom_stacks/yaml_manifest_attributes.md#stack) | mapping | none | none | mandatory |
| [`name`](./custom_stacks/yaml_manifest_attributes.md#name) | string | none | any valid string | mandatory |
| [`flavor`](./custom_stacks/yaml_manifest_attributes.md#flavor) | string | none | any valid string | optional |
| [`version`](./custom_stacks/yaml_manifest_attributes.md#version) | string | none | valid stack version | mandatory |
| [`reconciler`](./custom_stacks/yaml_manifest_attributes.md#reconciler) | string | none | StackManager/<br>LegacyStackManager | mandatory |

For additional details, regarding the various attributes refer to the: [Attributes of Stack Manifest](./custom_stacks/yaml_manifest_attributes.md).

**DataOS Address JQ Filters specification**

The DataOS Address JQ Filters specify which attributes within the YAML manifest need interpolation with DataOS Addresses for depot definition and credential retrieval.

```yaml
dataOsAddressJqFilters:
  - .inputs[]
  - .outputs[]
```

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [dataOsAddressJqFilters](./custom_stacks/yaml_manifest_attributes.md#dataosaddressjqfilters) | list of strings | none | valid strings | optional |

**Secret Projection Type**

The secretProjection type specifies the projection of secrets, such as depot and others.

```yaml
secretProjection:
	type: ${{secret projection type}}
```

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [secretProjection](./custom_stacks/yaml_manifest_attributes.md#secretprojection) | mapping | none | none | mandatory |
| [type](./custom_stacks/yaml_manifest_attributes.md#type) | string | none | none | optional |

**Image specification**

The image specification outlines attributes pertaining to the Docker image and associated details necessary for discovering and pulling it from the designated container registry.

<aside>
🗣 You have the flexibility to provide secrets for image retrieval either in the form of <a href="/resources/secret/#referencing-secrets-to-pull-images-from-private-container-registry"><code>imagePullSecret</code></a>or as environment variables.

</aside>
```yaml
image:
	registry: docker.io
	repository: personal
	image: mystack
	tag: 0.7.2-dev
	auth: 
		imagePullSecret: mysecret
```

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`image`](./custom_stacks/yaml_manifest_attributes.md#image) | mapping | none | none | optional |
| [`registry`](./custom_stacks/yaml_manifest_attributes.md#registry) | string | none | valid container registry name | mandatory |
| [`repository`](./custom_stacks/yaml_manifest_attributes.md#repository) | string | none | valid repository name | mandatory |
| [`image`](./custom_stacks/yaml_manifest_attributes.md#image-1) | string | none | valid image name | mandatory |
| [`tag`](./custom_stacks/yaml_manifest_attributes.md#tag) | string | none | valid image tag | mandatory |
| [`auth`](./custom_stacks/yaml_manifest_attributes.md#auth) | mapping | none | none | optional |
| [`imagePullSecret`](./custom_stacks/yaml_manifest_attributes.md#imagepullsecret) | string | none | valid imagePullSecret name | mandatory |

**Command and Argument specification** 

The command and arguments for executing the Docker image are defined in this section. You can either provide the entire command within the `command` attribute or split it into separate `command` and `argument` entries.

```yaml
command: 
	- python3
argument:
	- main.py
	- --configuration
	- /etc/dataos/config/jobconfig.yaml
```

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`command`](./custom_stacks/yaml_manifest_attributes.md#command) | list of strings | none | valid command | optional |
| [`arguments`](./custom_stacks/yaml_manifest_attributes.md#arguments) | list of strings | none | valid arguments | optional |

**Environment Variable specification**

This section details the environment variables essential for the execution of the Stack.

```yaml
environmentVars:
	PULSAR_TOPIC_ADDRESS: dataos://systemstreams:soda/quality_profile_results
	RESOURCE_DIR_PATH: "/etc/dataos/resources"
```

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`environmentVars`](./custom_stacks/yaml_manifest_attributes.md#environmentvars) | mapping | none | key-value pairs of environment variables  | optional |

**Ports Specification**

The Ports section specifies the service and target ports, along with unique name assigned to the port.

```yaml
ports:
	name: 
	servicePort:
	targetPort: 
```

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`ports`](./custom_stacks/yaml_manifest_attributes.md#ports) | mapping | none | none | optional |
| [`name`](./custom_stacks/yaml_manifest_attributes.md#name-1) | string | none | valid port name | mandatory |
| [`servicePort`](./custom_stacks/yaml_manifest_attributes.md#serviceport) | integer | none | valid port number | mandatory |
| [`targetPort`](./custom_stacks/yaml_manifest_attributes.md#targetport) | integer | none | valid port number | mandatory |

**StackSpec Value Schema section**

The DataOS Resource API accepts JSON Schema format. Although slightly different from YAML, with file references inlined directly as base64 and jobs and steps also inlined, the overall structure remains consistent between YAML and JSON formats.

```yaml
stackSpecValueSchema:
  jsonSchema: |
    {"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"input":{"type":"object"},"metrics":{"type":"object"},"logger":{"type":"object"},"http":{"type":"object"},"pipeline":{"type":"object"},"output":{"type":"object"}},"required":["input"]}
```

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`stackSpecValueSchema`](./custom_stacks/yaml_manifest_attributes.md#stackspecvalueschema) | mapping | none | none | optional |
| [`jsonSchema`](./custom_stacks/yaml_manifest_attributes.md#jsonschema) | string | none | valid json schema in string format | mandatory |

**Orchestrator Configuration**

A Stack encapsulates the logic pertaining to a specific task, while orchestrators like [Workflow](../workflow.md), [Worker](../worker.md), or [Service](../service.md) define how the Stack should be utilized for a particular use case. On applying these orchestrators the Kubernetes Resources of the respective Stack gets created. The YAML structure of Stacks is created at runtime, providing users the flexibility to decide the desired Stack structure and the information to include in the Stack definition. Poros, the DataOS Orchestrator, does not have hardcoded configurations; instead, it allows users to customize the specification according to their requirements.

<aside class="callout">
🗣 A Stack definition is not created every time an application, service, or job is run. Only aspects that are common, general, or standard need to be incorporated within the Stack definition. User-manipulatable information should be separately provided within the <code>stackSpec</code> attribute within the orchestrator.
</aside>

When defining Stacks within the DataOS ecosystem, two primary approaches are either as **Containerized Resources** or **Resource Dependent** ones. Each approach serves different use cases and provides flexibility based on the complexity and customization needs of the user.

***Containerized Resources***

By specifying the Containerized Resources within the Orchestrator config, users adhere to the standard default template provided by the DataOS Orchestrator, Poros. This template, which is a basic YAML configuration for the pods, comes with a predefined structure and attributes. The generic template can be overriden by passing a custom definition in the [`containerResourceTemplate`](./custom_stacks/yaml_manifest_attributes.md#containerresourcetemplate) attribute. Users only need to provide a [`configFileTemplate`](./custom_stacks/yaml_manifest_attributes.md#configfiletemplate) that the Stack will use. This is suitable for use cases where the standard template provided by Poros is sufficient. For tasks like consuming data from an API, performing transformations, and writing data to databases, users can rely on the default template without the need for additional pod information.

***Resource Dependent***

Resource Dependent approach involves declaring custom Resources and interacting with external Operators. For instance, when using Spark Operator, the user defines a template understood by Spark Operator, and Poros interpolates values into the Stack Resource of Spark Operator. In this case users need to understand the Operator, its requirements, and what resources it expects as input. For example, Spark templates require specific inputs, and users must ensure their Stack definitions align with the expectations of the Spark Operator. Users may need to specify URLs and information for communication with different services, or APIs as environment variables. Poros may propagate this information to the Operator, allowing the application code to traverse or call these clients.

The choice between Containerized Resources and Resource Dependent depends on the use case and the level of customization required. Containerized Resources are suitable for standard tasks where the default template suffices. Resource Dependent is more appropriate when dealing with external Operators, custom Resources, and intricate configuration needs. Users can select the approach that aligns with their specific requirements and understanding of the DataOS ecosystem.

Workflow Configuration

```yaml
workflowJobConfig:
	configFileTemplate: ${{config file template}}
	conatinerResourceTemplate: ${{container resource template}}
	resourceTemplateConfig:
		resourceTemplate: ${{resource template}}
		successCondition: ${{success condition}}
		failureCondition: ${{failure condition}}
```

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`workflowJobConfig`](./custom_stacks/yaml_manifest_attributes.md#workflowjobconfig) | mapping | none | none | optional |
| [`configFileTemplate`](./custom_stacks/yaml_manifest_attributes.md#configfiletemplate) | string | none | valid config file template | optional |
| [`containerResourceTemplate`](./custom_stacks/yaml_manifest_attributes.md#containerresourcetemplate-1) | string | none | valid container resource template | optional |
| [`resourceTemplateConfig`](./custom_stacks/yaml_manifest_attributes.md#resourcetemplateconfig) | mapping | none | none | optional |
| [`resourceTemplate`](./custom_stacks/yaml_manifest_attributes.md#resourcetemplate) | string | none | valid resource template | mandatory |
| [`successCondition`](./custom_stacks/yaml_manifest_attributes.md#successcondition) | string | none | valid success condition | mandatory |
| [`failureCondition`](./custom_stacks/yaml_manifest_attributes.md#failurecondition) | string | none | valid failure condition | mandatory |

To declare a Stack that will be orchestrated using a Workflow as a Containerized Resource, click on the link: [Stack orchestrated via a Workflow declared using a config template](./custom_stacks/case_scenarios/stack_orchestrated_by_a_workflow_declared_using_a_config_template.md). To declare a Stack using a custom Resource template that will be orchestrated using a Workflow, refer to the link: [Stack orchestrated via a Workflow declared using a Resource template](./custom_stacks/case_scenarios/stack_orchestrated_by_a_workflow_declared_using_a_resource_template.md).

Worker Configuration

```yaml
workerConfig:
	configFileTemplate: ${{config file template}}
	conatinerResourceTemplate: ${{container resource template}}
	resourceTemplate: ${{resource template}}
```

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`workerConfig`](./custom_stacks/yaml_manifest_attributes.md#workerconfig) | mapping | none | none | optional |
| [`configFileTemplate`](./custom_stacks/yaml_manifest_attributes.md#configfiletemplate-1) | string | none | valid config file template | optional |
| [`containerResourceTemplate`](./custom_stacks/yaml_manifest_attributes.md#containerresourcetemplate-1) | string | none | valid container Resource template | optional |
| [`resourceTemplate`](./custom_stacks/yaml_manifest_attributes.md#resourcetemplate-1) | string | none | valid resource template | optional |

To declare a Stack that will be orchestrated using a Worker as a Containerized Resource, refer to the link: [Stack orchestrated via a Worker declared using a config template](./custom_stacks/case_scenarios/stack_orchestrated_by_a_worker_declared_using_a_config_template.md). To declare a Stack using a custom Resource template that will be orchestrated using a Worker, refer to the following link: [Stack orchestrated via a Worker declared using a config template](./custom_stacks/case_scenarios/stack_orchestrated_by_a_worker_declared_using_a_resource_template.md).

Service Configuration

```yaml
serviceConfig:
	configFileTemplate: ${{config file template}}
	conatinerResourceTemplate: ${{container resource template}}
```

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`serviceConfig`](./custom_stacks/yaml_manifest_attributes.md#serviceconfig) | mapping | none | none | optional |
| [`configFileTemplate`](./custom_stacks/yaml_manifest_attributes.md#configfiletemplate-2) | string | none | valid config file template | optional |
| [`containerResourceTemplate`](./custom_stacks/yaml_manifest_attributes.md#containerresourcetemplate-2) | string | none | valid container Resource template | optional
 |

To take a look at a case scenario, refer to the link: [Stack orchestrated by a Service declared using a config template](./custom_stacks/case_scenarios/stack_orchestrated_by_a_service_declared_using_a_config_template.md). 

<aside class="callout">
🗣 A single Stack has the flexibility to be targeted by multiple orchestrators by providing the configuration for each of them. This allows users to orchestrate the same Stack using different orchestrators based on their specific requirements. For further details and examples, refer to the following link: [Multiple Orchestrator Configuration](./custom_stacks/case_scenarios/stack_orchestrated_by_a_service_declared_using_a_config_template.md).
</aside>

### **Apply the Stack YAML manifest**

Once the Stack YAML file is prepared, the [`apply`](../../interfaces/cli/command_reference.md#apply) command can be utilized to create a Stack Resource within the DataOS environment.

```shell
dataos-ctl apply -f ${{path/file-name}}
```

Upon successful creation of a Stack Resource, [CRUD operations](../../resources.md#crud-operations-on-dataos-resources) can be performed on top of it, and it can be orchestrated by Resources such as [Workflow](../workflow.md), [Worker](../worker.md), or [Service](../service.md), by specifying the Stack attribute within their respective YAMLs.

### **Verify Stack creation**

To ensure that your Stack has been successfully created, you can verify it in two ways:

Check the name of the newly created Stack in the list of Stacks where you are named as the owner:

```shell
dataos-ctl get -t operator

# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

      NAME     | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |  OWNER        
---------------|---------|----------|-----------|--------|---------|-------------------
  adf-operator | v1alpha | operator |           | active |         | iamgroot   
```

Alternatively, retrieve the list of all Stacks created in your organization:

```shell
dataos-ctl get -t operator -a
```

You can also access the details of any created Stacks through the DataOS GUI in the [Operations App](../../interfaces/operations.md).



## Attributes of Stack YAML manifest

This section outlines the various attributes associated with a Stack Resource, providing essential details for customization and configuration. To know more, navigate to the link: [Attributes of Stack YAML manifest](./custom_stacks/yaml_manifest_attributes.md).