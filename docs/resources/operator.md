---
title: Operator
search:
  boost: 2
---

# :resources-operator: Operator

Operator is a [DataOS Resource](../resources.md) that provides a standardized interface for orchestrating resources situated outside the DataOS cluster, empowering data developers with the capability to invoke actions programmatically upon these external resources directly from interfaces of DataOS.

<center>

![Operator Architecture](./operator/operator_architecture.png)

<i>High-level view of the Operator Resource within DataOS Architecture</i>

</center>

At its core, an Operator empowers the DataOS orchestrator, referred to as *Poros*, to manage these external resources using custom-built Operators. 

<aside class="callout">
🗣️ The Operator is classified as an <a href="/resources/types_of_dataos_resources/#instance-level-resources">Instance-level</a> DataOS Resource. Its creation and management fall under the purview of either the <b>DataOS Operator/Administrator</b> or the <b>Platform Engineering</b> team within an organization.

</aside>

## Key Features of Operator

**Extensibility**

The Operator augments DataOS capabilities by facilitating integration with external tools and data developer platforms such as Azure Data Factory, Databricks, Snowflake, and more. The external platform could be any platform, application, or service. It doesn't have to be Kubernetes-based, it could be anything that the Operator Pattern supports.

**Common Management Plane**

The Operator establishes a common management plane to orchestrate external resources. This not only enables CRUD operations but also provides comprehensive monitoring and logging, streamlining Root Cause Analyses (RCAs) and enhancing operational efficiency.

**Scalability and Speed**

In collaboration with the [Bundle](/resources/bundle/) Resource within the DataOS, the Operator automates processes, thus accelerating both the scale and speed of data product creation. 

**Collaboration**

The Operator alleviates collaboration hurdles arising from the diversity of technologies, each with its own frameworks, protocols, and languages. It achieves this by enabling cross-functional collaboration through a unified interface.

**Integration Burden**

The Operator enhances the developer experience and enhances productivity by offering a unified and consistent interface across all external resources. While it does not simplify the underlying architecture, it significantly streamlines interaction with the infrastructure.

## How to create an Operator?

Let’s take a scenario in which a data developer wants to trigger a pipeline run in Azure Data Factory (external platform) and synchronize the metadata from ADF back into DataOS for observability. But before proceeding ahead, make sure you have the following prerequisites.

### **Prerequisites**

#### **Azure Connection Fields**

To set up your Azure Data Factory Operator, ensure you have the following four fields readily available:

- `AZURE_SUBSCRIPTION_ID`
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`
- `AZURE_TENANT_ID`

#### **Pipeline Run-specific Fields**

For programmatic triggering, gather information regarding the various fields required for initiating a pipeline run. Refer to the official [Azure Data Factory Pipeline Run API documentation](https://learn.microsoft.com/en-us/rest/api/datafactory/pipelines/create-run?tabs=HTTP) for details.

### **Steps**

Creating your operator involves a series of logical steps, as outlined below:

1. [Implementing the Operator Interfaces](#implementing-the-operator-interfaces)<br>
    a. [Reconciler Interface](#implementing-the-operator-interfaces)<br>
    b. [OController Interface](#implementing-the-operator-interfaces)<br>
    c. [Message Handler Interface](#implementing-the-operator-interfaces)
2. [Dockerize the Code](#dockerize-the-code)
3. [Create manifest file for an Operator](#create-a-manifest-for-operator)
4. [Apply the Operator manifest](#apply-the-operator-manifest)
5. [Verify Operator creation](#verify-operator-creation)
6. [Manifest for Resource (external Resource)](#manifest-for-a-resource)
7. [Apply the Resource manifest](#apply-the-resource-manifest)
8. [Get Status of Resource](#get-status-of-pipeline-run)
9. [Check Status on Azure Data Factory UI](#check-the-status-on-azure-data-factory-ui)
10. [Metadata Synchronization in DataOS](#metadata-synchronization-in-dataos)

#### **Implementing the Operator Interfaces**

The first step in creating an Operator is implementing three key interfaces: Reconciler, OController, and Message Handler Interface using the the [DataOS SDK-Go](https://bitbucket.org/rubik_/dataos-sdk-go). 

<aside class="callout">
🗣 Implementing the Operator interfaces requires a good understanding of <b>Kubernetes</b> and associated terminology. If the Operator is present within the DataOS context, you can directly proceed to <a href="/resources/operator/#yaml-manifest-for-resource">creating the Resource manifest for the external Resource.</a>

</aside>

**Reconciler Interface**

The Reconciler Interface is responsible for reconciling resources based on state changes.

```go
type Reconciler interface {
	Id() string
	Init(OController)
	Reconcile(ReconcileRequest, context.Context) (ReconcileResult, error)
}
```

**OController Interface**

OController, the Operator Controller Interface, manages the entity status. The SDK incorporates an entity store, extendable to Redis or a database if required.

```go
type OController interface {
	GetEntity(key string, typ EntityOfInterestType) (*Entity, error)
	GetEntityStatus(key string, typ EntityOfInterestType) (*EntityStatus, error)
	UpdateEntityStatus(es *EntityStatus) error
}
```

The SDK's controller object implements the OController interface, and the reconciler implementation is integrated into this controller.

**Message Handler Interface**

The Message Handler Interface deals with communication from the DataOS Orchestrator, Poros.

```go
type MessageHandler interface {
	// HandleCommand is the way that upstream controllers can request this
	// operator to create, update and delete entities of interest.
	HandleCommand(
		me *models.MessageEnvelope,
		es state.EntityStore,
		ess state.EntityStatusStore,
		node *snowflake.Node,
	) error
	// HandleQuery is the way that upstream controllers
	// can request information about entities of interest and their status.
	HandleQuery(
		me *models.MessageEnvelope,
		es state.EntityStore,
		ess state.EntityStatusStore,
		node *snowflake.Node,
	) (*models.MessageEnvelope, error)
}
```

The message handler implementation is employed to create an instance of Messaging API, which manages the communication interface with the NATS Cluster. The state is subsequently captured within the Poros orchestrator using the query interface.

Sample Implementation for the interfaces can be found [here.](https://bitbucket.org/rubik_/todo-operator)

#### **Dockerize the Code**

After implementing the required interfaces, dockerize your code and move the image to a docker container registry.

#### **Create a Manifest for Operator**

Once you have done that proceed to create a YAML manifest for your Operator. An Operator Resource YAML manifest can be structurally broken down into following sections:

**Resource Meta section**

An Operator is classified as a [Resource-type](./types_of_dataos_resources.md) within DataOS. The YAML configuration file of an Operator Resource includes a Resource Meta section that encompasses metadata attributes shared among all Resource-types. For in-depth information about the attributes of Resource Meta section, please consult the [Attributes of Resource Meta section.](./resource_attributes.md)

**Operator-specific section**

The Operator-specific section is further divided into four distinct sections: *Computational components*, *Resource definition*, *NATS Cluster configuration*, *Enabled Workspaces*. Each of these sections should be appropriately configured when crafting an Operator YAML. 

- **Computational Components:** Computational Components encapsulate the logic for managing the interactions with resources within the external platform/application/service (*external resource*), handling the entire lifecycle of associated resources. These components are responsible for reconciling resource states and translating them back to the DataOS orchestrator, *Poros*. The [`components`](./operator/yaml_configuration_attributes.md#components) section in the Operator-specific section is a list of mappings allowing you to define multiple computational components. Each component is either a [Worker](./worker.md) or a [Service](./service.md) Resource. These components can be customized with unique Docker images, secret configuration, and environment variables to facilitate their execution.
- **Resource Definition:** The Resource definition encompasses specifications for external resources to be orchestrated through DataOS. This definition acts as a comprehensive blueprint, providing all necessary information about the resource and the schema it must adhere to. The resource definition is flexible and can be tailored to suit the specific requirements of the external resource you intend to orchestrate. Multiple resources can be defined to interact with different external platforms as needed.
- **NATS Cluster Configuration:** NATS is a lightweight pub-sub system. It is used to implement a Command Query Responsibility Segregation (CQRS)-based communication channel between the Operator Runtime, which lives in Poros, and the computational components mentioned above. It's a 2-way communication channel. The operator components have the specific knowledge regarding the management of the resources. They listen for commands and queries on the NATS Cluster. The Operator runtime communicates with the operator components using the specific commands for a Resource-type. Poros Operator takes care of manifesting the NATS Cluster.
- **Enabled Workspaces:** The [`enabledWorkspaces`](./operator/yaml_configuration_attributes.md#enabledworkspaces-1) attribute is a list of strings for selectively specifying the Operator within specific workspaces.

The following YAML manifest illustrates the attributes specified within the Operator YAML:

```yaml
# Resource meta section
name: ${{azure-data-factory}}
version: v1alpha
type: operator
layer: user
description: ${{provides management of azure data factory resources lifecycle}}
tags:
	- ${{operator}}
	- ${{adf}}
	- ${{azure-data-factory}}

# Operator-specific section
operator:

  # NATS Cluster configuration
	natsClusterConfig:
		name: ${{adf-nats}}
		compute: ${{runnable-default}}
		runAsUser: ${{minerva-cluster}} 

  # Computational Components
	components:
		- name: ${{adf-controller}}
			type: ${{worker}}
			compute: ${{runnable-default}}
			runAsUser: ${{minerva-cluster}}
			image: ${{docker.io/rubiklabs/azure-operator:0.1.5-dev}}
			imagePullSecret: ${{dataos-container-registry}}
			command: 
				- ${{/opt/tmdc-io/azure-operator}}
			arguments:
				- ${{operator}}
				- adf
				- --electionStateFile
				- /opt/tmdc-io/leader-election.log
			replicas: 2
			environmentVars: 
				LOG_LEVEL: info
				METRIC_PORT: 30001
				ELECTION_CLUSTER_NAME: azure-operators
				ELECTION_CLUSTER_SIZE: 1
				OPERATOR_MAX_WORKERS: 1
				OPERATOR_RECONCILE_WORKERS_INTERVAL: 10s
				OPERATOR_MAINTENANCE_INTERVAL: 1m
				OPERATOR_PURGE_STATE_STORE_BEFORE: 5m
				OPERATOR_STATE_STORE_TYPE: jetstream_kv
				MESSAGE_DURABILITY: true
				# NATS Cluster specific environment variables
				ENTITY_OF_INTEREST_MESSAGE_QUEUE: azure-entities-adf-52323
				ENTITY_OF_INTEREST_MESSAGE_STREAM: dataos-azure-entities
				ENTITY_OF_INTEREST_MESSAGE_COMMAND_SUBJECT: adf.pipeline.run
				ENTITY_OF_INTEREST_MESSAGE_QUERY_SUBJECT: adf.pipeline.run.query
				ENTITY_OF_INTEREST_MESSAGE_QUERY_REPLY_SUBJECT: dataos.operator.adf.reply
				# Azure Data Factory specific environment variables
				AZURE_TENANT_ID: 191b8015-c70b-4cc7-afb0-818de32c05df
				AZURE_CLIENT_ID: 769f7469-eaed-4210-8ab7-obc4549d85a1
				AZURE_CLIENT_SECRET: LGz8Q-NcuMf~GcPwjAjpJINM6n(iLFiuBsrPubAz
				AZURE_SUBSCRIPTION_ID: 79d26b17-3fbf-4c85-a88b-10a4480fac77
			ports:
				- name: metrics
					servicePort: 30001
					targetPort: 30001
	# Resource Definition
	resources: 
		- name: pipeline-run
			isRunnable: true
			specSchema:
				jsonSchema: |
						{
						"$schema": "https://json-schema.org/draft/2020-12/schema",
						"$id": "https://dataos.io/v1.0/azure-data-factory/pipeline-run",
						"title": "pipeline-run",
						"type": "object",
						"properties": {
						  "factoryName": {
						    "type": "string"
						  },
						  "pipelineName": {
						    "type": "string"
						  },
						  "resourceGroupName": {
						    "type": "string"
						  },
						  "parameters": {
						    "type": "object",
						    "additionalProperties": true
						  },
						  "referencePipelineRunID": {
						    "type": "string",
						    "nullable": true
						  },
						  "startActivityName": {
						    "type": "string",
						    "nullable": true
						  },
						  "startFromFailure": {
						    "type": "boolean",
						    "nullable": true
						  }
						},
						"required": [
						  "factoryName",
						  "pipelineName",
						  "resourceGroupName"
							],"additionalProperties": false
						}
		natsApi:
			command:
				stream: dataos-zure-entities
				subject: adf.pipeline.run
			query:
				subject: adf.pipeline.run.query
				replySubject: dataos.operator.adf.reply

	# Enabled Workspaces
	enabledWorkspaces: 
		- public
		- sandbox
```

You can also pass the Azure-specific Secrets seperately.

<details><summary>How to pass Secrets as a Resource and refer them in a separate Resource?</summary>
    
<b>Create a Secret Resource manifest</b>
    
```yaml
name: ${{adf-operator}}
version: v1
description: ${{the secrets for adf operator}}
secret: 
    type: key-value-properties
    acl: rw
    data: 
        AZURE_TENANT_ID: ${{azure tenant id}}
        AZURE_CLIENT_ID: ${{azure client id}}
        AZURE_CLIENT_SECRET: ${{azure client secret}}
        AZURE_SUBSCRIPTION_ID: ${{azure subscription id}}
```
    
<b>Apply the Secret YAML</b>
    
```shell
dataos-ctl apply -f ${{secret-yaml-file-path}} -w ${{workspace}}
```
    
<b>Reference the Secrets in the Operator YAML</b>
    
```yaml
# Resource meta section
name: ${{azure-data-factory}}
version: v1alpha
type: operator
layer: user
description: ${{provides management of azure data factory resources lifecycle}}
tags:
    - ${{operator}}
    - ${{adf}}
    - ${{azure-data-factory}}

# Operator-specific section
operator:

    # NATS Cluster configuration
    natsClusterConfig:
        name: ${{adf-nats}}
        compute: ${{runnable-default}}
        runAsUser: ${{minerva-cluster}} 

    # Computational Components
    components:
        - name: ${{adf-controller}}
            type: ${{worker}}
            compute: ${{runnable-default}}
            runAsUser: ${{minerva-cluster}}
            image: ${{docker.io/rubiklabs/azure-operator:0.1.5-dev}}
            imagePullSecret: ${{dataos-container-registry}}
            command: 
                - ${{/opt/tmdc-io/azure-operator}}
            arguments:
                - ${{operator}}
                - adf
                - --electionStateFile
                - /opt/tmdc-io/leader-election.log
            replicas: 2
            environmentVars: 
                LOG_LEVEL: info
                METRIC_PORT: 30001
                ELECTION_CLUSTER_NAME: azure-operators
                ELECTION_CLUSTER_SIZE: 1
                OPERATOR_MAX_WORKERS: 1
                OPERATOR_RECONCILE_WORKERS_INTERVAL: 10s
                OPERATOR_MAINTENANCE_INTERVAL: 1m
                OPERATOR_PURGE_STATE_STORE_BEFORE: 5m
                OPERATOR_STATE_STORE_TYPE: jetstream_kv
                MESSAGE_DURABILITY: true
# NATS specific stuff (not exposing to the user)
                ENTITY_OF_INTEREST_MESSAGE_QUEUE: azure-entities-adf-52323
                ENTITY_OF_INTEREST_MESSAGE_STREAM: dataos-azure-entities
                ENTITY_OF_INTEREST_MESSAGE_COMMAND_SUBJECT: adf.pipeline.run
                ENTITY_OF_INTEREST_MESSAGE_QUERY_SUBJECT: adf.pipeline.run.query
                ENTITY_OF_INTEREST_MESSAGE_QUERY_REPLY_SUBJECT: dataos.operator.adf.reply
# Passed as Secret Resource
            dataosSecrets:
                - name: adf-operator
                    workspace: user-system
                    allKeys: true
                    consumptionType: envVars
            ports:
                - name: metrics
                    servicePort: 30001
                    targetPort: 30001
    resources: # Resources is a list of Resources that we want to manage
        - name: pipeline-run
            isRunnable: true
            specSchema:
                jsonSchema: |
                        {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "$id": "https://dataos.io/v1.0/azure-data-factory/pipeline-run",
                        "title": "pipeline-run",
                        "type": "object",
                        "properties": {
                            "factoryName": {
                            "type": "string"
                            },
                            "pipelineName": {
                            "type": "string"
                            },
                            "resourceGroupName": {
                            "type": "string"
                            },
                            "parameters": {
                            "type": "object",
                            "additionalProperties": true
                            },
                            "referencePipelineRunID": {
                            "type": "string",
                            "nullable": true
                            },
                            "startActivityName": {
                            "type": "string",
                            "nullable": true
                            },
                            "startFromFailure": {
                            "type": "boolean",
                            "nullable": true
                            }
                        },
                        "required": [
                            "factoryName",
                            "pipelineName",
                            "resourceGroupName"
                            ],"additionalProperties": false
                        }
        natsApi:
            command:
                stream: dataos-zure-entities
                subject: adf.pipeline.run
            query:
                subject: adf.pipeline.run.query
                replySubject: dataos.operator.adf.reply
    
    enabledWorkspaces: 
        - public
        - sandbox
```
</details>

The table below summarizes the attributes of the Operator-specific section:

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`operator`](./operator/yaml_configuration_attributes.md#operator) | mapping | none | none | mandatory |
| [`components`](./operator/yaml_configuration_attributes.md#components) | list of mappings | none | none | mandatory |
| [`name`](./operator/yaml_configuration_attributes.md#name) | string | none | none  | mandatory |
| [`type`](./operator/yaml_configuration_attributes.md#type) | string | none | service/worker  | mandatory |
| [`compute`](./operator/yaml_configuration_attributes.md#compute) | string | none | runnable-default or any other custom Compute Resource name | mandatory |
| [`runAsApiKey`](./operator/yaml_configuration_attributes.md#runasapikey) | string | Apikey of user | valid DataOS Apikey | mandatory |
| [`runAsUser`](./operator/yaml_configuration_attributes.md#runasuser) | string | none | user-id of Use Case Assignee | optional |
| [`image`](./operator/yaml_configuration_attributes.md#image) | string | none | valid image name | mandatory |
| [`imagePullSecret`](./operator/yaml_configuration_attributes.md#imagepullsecret) | string | none | valid Secret Resource for pulling images from the Private Container Registry | optional |
| [`command`](./operator/yaml_configuration_attributes.md#command) | list of strings | none | valid command | optional |
| [`arguments`](./operator/yaml_configuration_attributes.md#arguments) | list of strings | none | valid arguments | optional |
| [`replicas`](./operator/yaml_configuration_attributes.md#replicas) | integer | none | any integer  | mandatory |
| [`environmentVars`](./operator/yaml_configuration_attributes.md#environmentvars) | mapping | none | list of available environment variables given here | optional |
| [`secrets`](./operator/yaml_configuration_attributes.md#secrets) | mapping | none | none | optional |
| [`name`](./operator/yaml_configuration_attributes.md#name-1) | string | none | valid Secret Resource name | mandatory |
| [`workspace`](./operator/yaml_configuration_attributes.md#workspace) | string | none | valid Workspace name | mandatory |
| [`ports`](./operator/yaml_configuration_attributes.md#ports) | list of mappings | none | none | optional |
| [`name`](./operator/yaml_configuration_attributes.md#name-2) | string | none | valid string  | mandatory |
| [`servicePort`](./operator/yaml_configuration_attributes.md#serviceport) | integer | none | valid port | mandatory |
| [`targetPort`](./operator/yaml_configuration_attributes.md#targetport) | integer | none | valid port | mandatory |
| [`resources`](./operator/yaml_configuration_attributes.md#resources) | mapping | none | none | mandatory |
| [`name`](./operator/yaml_configuration_attributes.md#name-2) | string | none | valid resources name | mandatory |
| [`nameJqFilter`](./operator/yaml_configuration_attributes.md#namejqfilter) | string | none | valid string | optional |
| [`isRunnable`](./operator/yaml_configuration_attributes.md#isrunnable) | boolean | false | true/false | mandatory |
| [`specSchema`](./operator/yaml_configuration_attributes.md#specschema) | mapping | none | none | optional |
| [`jsonSchema`](./operator/yaml_configuration_attributes.md#jsonschema) | string | none | none | mandatory |
| [`natsApi`](./operator/yaml_configuration_attributes.md#natsapi) | mapping | none | none | optional |
| [`command`](./operator/yaml_configuration_attributes.md#command-1) | mapping | none | none | mandatory |
| [`stream`](./operator/yaml_configuration_attributes.md#stream) | string | none | valid stream | mandatory |
| [`subject`](./operator/yaml_configuration_attributes.md#subject) | string | none | valid subject | mandatory |
| [`query`](./operator/yaml_configuration_attributes.md#query) | mapping | none | none | mandatory |
| [`subject`](./operator/yaml_configuration_attributes.md#subject-1) | string | none | valid subject | mandatory |
| [`replySubject`](./operator/yaml_configuration_attributes.md#replysubject-1) | string | none | valid replySubject  | mandatory |
| [`natsClusterConfig`](./operator/yaml_configuration_attributes.md#natsclusterconfig) | mapping | none | none | mandatory |
| [`name`](./operator/yaml_configuration_attributes.md#name-3) | string | none | valid name  | mandatory |
| [`compute`](./operator/yaml_configuration_attributes.md#compute-1) | string | none | runnable-default or any other custom Compute Resource name | mandatory |
| [`runAsUser`](./operator/yaml_configuration_attributes.md#runasuser-1) | string | none | user-id of Use Case Assignee | optional |
| [`runAsApiKey`](./operator/yaml_configuration_attributes.md#runasapikey-1) | string | Apikey of user | valid DataOS Apikey (if not provided it takes the user’s default apikey) | mandatory |
| [`enabledWorkspaces`](./operator/yaml_configuration_attributes.md#enabledworkspaces) | list of strings | none | valid DataOS Workspace | mandatory |

For in-depth information about the attributes of the Operator-specific section, please consult the [Attributes of Operator-specific section.](./operator/yaml_configuration_attributes.md)

#### **Apply the Operator manifest**

After creating the YAML configuration file for the Operator Resource, it's time to apply it to instantiate the Resource-instance in the DataOS environment. To apply the Operator YAML file, utilize the [`apply`](../interfaces/cli/command_reference.md#apply) command.

```shell
dataos-ctl apply -f ${{operator yaml manifest file path}}
```

#### **Verify Operator Creation**

To ensure that your Operator has been successfully created, you can verify it in two ways:

Check the name of the newly created Operator in the list of Operators where you are named as the owner:

```shell
dataos-ctl get -t operator

# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

      NAME     | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |  OWNER        
---------------|---------|----------|-----------|--------|---------|-------------------
  adf-operator | v1alpha | operator |           | active |         | iamgroot    
```

Alternatively, retrieve the list of all Operators created in your organization:

```shell
dataos-ctl get -t operator -a
```

You can also access the details of any created Operator through the DataOS GUI in the [Operations App.](../interfaces/operations.md)

<center>

![Manifestation of Operator](./operator/operator_manifestation.png)

<i>Manifestation of Operator in DataOS</i>

</center>

#### **Manifest for a Resource**

Now once we have created an Operator, we would need to create a Resource (external Resource) which is an Azure Data Factory pipeline that would be managed by this Operator. In DataOS, the process of creating external Resources involves utilizing a specific type of Resource called, aptly, "**Resource**." These Resources are categorized as second-class Resources, distinct from the first-class Resources like Workflow, Service, and Policy.

Resource as a Resource, in essence, serves as a means to interact with Operators. While Workflow, Service, and Policy Resources are first-class and can be independently managed, Resources created through the Resource are specifically designed for use with Operators. Below is the Resource YAML for the external ADF pipeline Resource:

```yaml
# Resource meta section
name: ${{pipeline-run-1}}
version: v1alpha
type: resource
tags:
	- ${{adf-pipeline}}
	- ${{adf-operator}}
description: ${{adf pipeline run}}
owner: iamgroot

# Resource-specific section
resource: 
	operator: ${{adf-operator}}
	type: ${{pipeline-run}}
	spec: 
		factoryName: ${{datafactoryoz3un3trdpaa}}
		pipelineName: ${{ArmtemplateSampleCopyPipeline}}
		resourceGroupName: ${{Engineering}}
```

When creating Resources with this approach, the Operator's JSON Schema plays a vital role in validation. The spec provided in the Resource YAML is validated against this schema, ensuring that the Resource conforms to the predefined structure.

<aside class="callout">
🗣 Operators and Resources are both separate Resources within DataOS. It's important to understand that one doesn't merely serve as an interface to the other; they have distinct purposes and functionalities.

</aside>

#### **Apply the Resource manifest**

To trigger a pipeline run, you can apply the Resource YAML using the following command:

```shell
dataos-ctl apply -f ${{resource-yaml-file-path}} -w ${{workspace}}

# Sample
dataos-ctl apply -f ../adf-operator/resource.yaml -w public
```

#### **Get Status of Pipeline Run**

```shell
dataos-ctl get -t resource -w ${{workspace}}

# Sample
dataos-ctl get -t resource -w public

# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

      NAME       | VERSION |   TYPE   | WORKSPACE | STATUS |  RUNTIME   |   OWNER        
-----------------|---------|----------|-----------|--------|------------|-------------------
  pipeline-run-1 | v1alpha | resource | public    | active | inprogress |  iamgroot  
```

#### **Check the Status on Azure Data Factory UI**

Once we apply we can go over on the Azure Data Factory UI. 

**Before Pipeline run**

<center>

![ADF Before Pipeline Run](./operator/adf_before_pipeline_run.png)

<i>Azure Data Factory UI before pipeline run</i>
</center>

**After Pipeline run**

<center>

![ADF After Pipeline Run](./operator/adf_after_pipeline_run_1.png)

<i>Azure Data Factory UI after pipeline run</i>

![ADF Pipeline Runs](./operator/adf_after_pipeline_run_2.png)

<i>Azure Data Factory UI various pipeline runs</i>

</center>

#### **Metadata Synchronization in DataOS**

While the pipeline is in progress, you have the capability to capture metadata from Azure Data Factory back into DataOS Metis. The process of metadata capture is orchestrated through the Operator Component and NATS Cluster. While coding the Operator, you have the complete complete control over determining which specific state information from the external cluster, in this case, Azure Cluster, should be retrieved and synchronized with DataOS. To get information about which information is being synchronized, utilize the following command:

```shell
dataos-ctl get -t resource -w public -n ${{external-resource-name}} -d
```

Here, `${{external-resource-name}}` should be replaced with the relevant identifier, such as the name of the specific external resource (Resource) run:

```shell
dataos-ctl get -t resource -w public -n pipeline-run-1 -d
```

#### **Delete Operator**

If you need to delete an operator, you first need to delete all the workloads or Resources that are dependent on it. Once it's done, use the `delete` command to remove the specific operator from the DataOS instance:

```shell
dataos-ctl delete -t operator -n ${{name of operator}}
```

## How does the Operator Work?

<center>

![Working of Operator](./operator/operator_working.png)
<i>Working of an Operator</i>

</center>

The diagram illustrates the workings of the DataOS Kubernetes Cluster and the process that unfolds when applying an Operator YAML via the DataOS Command Line Interface (CLI).

1. **Applying YAML Manifest**: When a user applies an Operator YAML through the CLI, the Resource API takes this information to the DataOS Orchestrator, known as Poros.
2. **Poros Orchestrator**: Poros serves as an Operator Manager, housing multiple Operators within it. One of these Operators is the Poros Operator, responsible for managing DataOS-specific Resources within the Kubernetes cluster.
3. **Custom Operator Runtime**: The Operator YAML creates a custom Operator runtime within Poros. This runtime is responsible for overseeing the operation of an external Resource.
4. **NATS Cluster Creation**: The Operator YAML also includes NATS Cluster configuration. The Operator Runtime establishes a pub-sub communication with the NATS Cluster.
5. **Operator Component**: This is the Worker or Service Resource that contains the docker image, and secret configurations for interfacing with external third-party services, platforms, or ecosystems. It could involve services like Databricks Workspace, Azure Data Factory, or others. The Operator Component interacts with these external resources via their REST APIs, enabling CRUD (Create, Read, Update, Delete) operations and other specific functionalities.
6. **NATS Cluster Communication**: The Operator Component communicates with the NATS Cluster, which acts as the communication channel between the Operator Component and the Operator Runtime.
7. **JSON Schema and Resource Definition**: The creation of the Operator YAML also involves providing a JSON schema for the external Resource. 
8. **Resource YAML Application**: Additionally, a secondary YAML is created, defining a new Resource-type called "Resource." Within this Resource, a reference to the specific Operator responsible for managing it is specified. The Resource spec is validated against the Operator's JSON schema. When the Resource YAML is applied, it informs the DataOS Orchestrator that this Resource will be managed by the custom Operator runtime created earlier.
9. **Command Query Responsibility Segregation (CQRS) Pattern:** The Operator adheres to the Command Query Responsibility Segregation (CQRS) Pattern, ensuring a clear separation of commands and queries.
    1. **Command:** When executing commands such as creating, updating, or deleting, the system forwards these actions to the NATS Cluster. The NATS Cluster then communicates with the compute component associated with the Operator, which subsequently dispatches the pertinent information to the external platform or service.
    2. **Query:** Simultaneously, the system offers a querying mechanism for retrieving information about the status and details of the service. Executing the `dataos-ctl get` command initiates a query operation, which traverses through the NATS Cluster. The query is then directed to the entity store within the computational component, which maintains the desired state information.

    <center>

![Operator control flow](./operator/operator_behind_the_scenes.png)
<i>Operator behind the scenes</i>

</center>

## Case Scenarios

- [How to orchestrate a Hightouch pipeline using a Hightouch Factory Operator?](./operator/case_scenario/hightouch_factory_operator.md)

- [How to orchestrate ADF pipeline using Azure Data Factory Operator?](#how-to-create-an-operator)