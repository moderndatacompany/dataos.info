# Building Blocks of Flare Workflow


A Flare Workflow is a series of activities that are necessary to complete a data processing task. It lets you run your data processing logic. At a more granular level, each Flare Workflow YAML file is composed of fundamental components that include the following essential parts.

## Structure of Flare Workflow

### **Flare Workflow**

In the context of DataOS, a Workflow is a fundamental Primitive/Resource. Specifically, a Flare Workflow comprises of a job that calls upon the Flare stack to execute various processing tasks. The syntax for a Workflow is outlined below for your reference.

```yaml
version: v1 # Version
name: wf-cust-demo-01 # Name of the Workflow
type: workflow # Resource Type (Here its Workflow)
tags: # Tags
  - Connect
  - Customer
description: Sample Job # Description 
workflow: # Workflow Specific Section
	dag:
		{} #sequence of jobs come within DAG
```

To know more about the details of various properties within a workflow, click [here](../../workflow.md) 

### **Flare Job**

In the realm of task orchestration, a Job can be understood as a series of discrete steps necessary for the completion of an action. These steps can include diverse activities, such as loading initial data, modifying and writing data to a destination. While a Job is a generalized term, a Flare Job specifically involves utilizing the Flare Stack to complete processing tasks. By leveraging a directed acyclic graph (DAG), users can specify and execute numerous Jobs, each with its distinctive set of tasks in a specific order. It is possible to define multiple jobs that will be executed consecutively. The syntax for creating a Flare Job is presented below:

```yaml
dag: # Directed Acyclic Graph (DAG): A collection of Jobs
  - name: city-02 # Name of the Job (there can be more than 1 Job within a DAG that can run on different stacks)
    title: City Dimension Ingester # Title of the Job
    description: The job ingests city data from dropzone into raw zone # Description
		tags: # Tags
			- Connect
			- City
    spec: # Specs
      runAsUser: iamgroot # Run As User
      stack: flare:4.0 # Here stack is Flare so its a Flare Job
      compute: runnable-default # Compute
      flare: # Flare Section
        driver: # Driver Section
          coreLimit: 1000m **# m here is millicore**
          cores: 1
          memory: 1024m
        executor: # Executor Section
          coreLimit: 1000m
          cores: 1
          instances: 1
          memory: 1024m
        job: # Job
          explain: true # Explain
          logLevel: INFO # Log Level
					streaming:  # Streaming Section
								{}
          inputs: #Inputs Section
								{}
          outputs: #Outputs Section
								{}
					steps: # Steps Section
								{}
					assertions: # Assertions Section
								{}
					actions: # Actions Section
								{}
```

The `{}` symbol functions as a variable placeholder that accommodates diverse supplementary properties that are listed at the conclusion of the corresponding section.

The below table summarizes the various attributes within a Flare Job:

| --- | --- | --- | --- | --- | --- | --- |
| name | Name of the job. | name: customer | NA | NA | Rules for name: 37 alphanumeric characters and a special character '-' allowed. [a-z0-9]([-a-z0-9]*[a-z0-9]. The maximum permissible length for the name is 47 (Note: It is advised to keep the name length less than 30 characters because the orchestration engine behind the scenes adds a Unique ID which is usually 17 characters. Hence reduce the name length to 30. | Mandatory |
| title | Title of the job. | title: Sample Ingester | NA | NA | NA | Optional |
| description | This is the text describing the job. | description: The job ingests customer data and joins it with city data | NA | NA | NA | Optional |
| spec | Specs of job. | spec:
    {} | NA | NA | NA | Mandatory |
| tags | Tags for the job. | tags:
   - Connect
   - Customer | NA | NA | NA | Optional |
| runAsUser | Run as User. | runAsUser: iamgroot | NA | User ID of the use case assignee | Make sure that the user id is valid. | Optional |
| stack | The Flare stack version to run the workflow is defined here.  | stack: flare:4.0 | flare:4.0 | flare:4.0, flare:3.0 | Please check the available Flare stack version. | Optional |
| flare | Flare Stack specific section. | flare: 
     {} | NA | NA | NA | Mandatory |
| driver | The driver is the controller node of the operation and controls the operations of the workflow. | driver:
  coreLimit: 1000m
  cores: 1
  memory: 1024m | driver:
  coreLimit: 1000m
  cores: 1
  memory: 1024m | NA | If not defined, default values will be considered. Here the unit in coreLimit value is millicore(m). | Optional |
| executor | The executor is the worker node that performs the operations defined in the workflow and sends the result back to the driver. It must interface with the cluster manager in order to actually get physical resources and launch executors. | executor:
  coreLimit: 2000m
  cores: 2
  instances: 2
  memory: 1024m | executor:
  coreLimit: 1000m
  cores: 1
  instances: 1
  memory: 1024m | NA | If not defined, default values will be considered. Here the unit in coreLimit value is millicore(m). | Optional |
| job | Jobs can be defined as the steps to complete any action such as loading initial data, updating data, or writing data to sink. | job:
    {} | NA | NA | NA | Mandatory |
| explain | Use this flag to print the spark logical/physical plans in the logs.  | explain: true | false | true/false | For both physical and logical plans set to true
For just physical set to false. | Optional |
| logLevel | A log level is a piece of information from a given log message that distinguishes log events from each other. It helps in finding runtime issues with your Flare workflow and in troubleshooting. | logLevel: INFO | INFO | INFO / WARN / DEBUG/ ERROR | INFO - Designates informational messages that highlight the progress of the workflow
WARN - Designates potentially harmful situations
DEBUG - Designates fine-grained informational events that are most useful while debugging
ERROR - Desingates error events that might still allow the workflow to continue running | Optional |
| streaming | The streaming section contains properties related to executing the stream jobs. | streaming:
    {} | NA | NA | NA | Optional |
| inputs | Contains dataset details for reading data from supported data sources. | inputs:
     {} | NA | NA | NA | Mandatory |
| steps | One or more sequences to execute the steps defined for performing any transformation or applying any flare function or command. | steps:
     {} | NA | NA | NA | Mandatory |
| outputs | Contains dataset details for writing data to supported data sources. | outputs:
     {] | NA | NA | NA | Mandatory |
| assertions | Assertions allow you to perform validation checks on top of pre-written datasets. They are defined under the assertions section.  | assertions:
     {] | NA | NA | NA | Optional |
| actions | Icebase-specific actions are defined in the actions section. | actions:
     {] | NA | NA | NA | Optional |

A Flare Job can be further split into 5 sections:

#### **Inputs**

The `inputs` section encompasses crucial configuration settings necessary for extracting data from diverse sources, such as name, format, dataset address, etc. To facilitate reading data from multiple sources, an array of data source definitions are required. To obtain more detailed information, kindly refer to the link below.

[Inputs](./building_blocks_of_flare_workflow/inputs.md)

#### **Outputs**

The `outputs` section provides comprehensive information regarding the storage location and naming convention for the output dataset. To access additional details, please refer to the link provided below.

[Outputs](./building_blocks_of_flare_workflow/outputs.md)

#### **Steps**

The `steps` section outlines the prescribed sequence of tasks for data enrichment and processing, including but not limited to the addition of calculated columns, aggregations, and filtering via SQL. These are defined in `sequence` under `steps`. For further information, please consult the linked page.

[Steps](./building_blocks_of_flare_workflow/steps.md)

#### **Streaming**

The `streaming` section encompasses properties that pertain to the execution of stream jobs. For further details, please refer to the page provided below.

[Streaming](./building_blocks_of_flare_workflow/streaming.md)

#### **Assertions**

In the context of data quality, assertions refer to validation rules that are tailored to a particular business domain and serve to determine the fitness-for-purpose of datasets. The application of assertions enables the execution of additional validation checks on top of existing datasets, thereby enhancing their overall quality. Assertions are defined within the dedicated `assertions` section. To gain further insights, please refer to the following page.

[Assertions](./building_blocks_of_flare_workflow/assertions.md)

To perform validation checks on datasets that are to be written, click here

#### **Actions**

The DataOS platform provides comprehensive support for executing maintenance actions within the Icebase depot. These are specified within the `actions` section. For further information, please refer to the following page.

[Actions](./building_blocks_of_flare_workflow/actions.md)