# Flare Stack YAML Configurations


A Flare Workflow is a series of activities that are necessary to complete a data processing task. It lets you run your data processing logic. At a more granular level, each Flare Workflow YAML file is composed of fundamental components that include the following essential parts.

## Structure of Flare Workflow

### **Workflow Resource**

In the context of DataOS, a Workflow is a fundamental Resource. Specifically, a Flare Workflow comprises of a job that calls upon the Flare stack to execute various processing tasks. The syntax for a Workflow is outlined below for your reference.

```yaml
version: v1 
name: wf-cust-demo-01 
type: workflow 
tags: 
  - Connect
  - Customer
description: Sample Job  
workflow:
	dag:
		{} 
```

To know more about the details of various properties within a Workflow, click [here](../../workflow.md) 

### **Job**

In the realm of task orchestration, a Job can be understood as a series of discrete steps necessary for the completion of an action. These steps can include diverse activities, such as loading initial data, modifying and writing data to a destination. While a Job is a generalized term, a Flare Job specifically involves utilizing the Flare Stack to complete processing tasks. By leveraging a directed acyclic graph (DAG), users can specify and execute numerous Jobs, each with its distinctive set of tasks in a specific order. It is possible to define multiple jobs that will be executed consecutively. The syntax for creating a Flare Job is presented below:

```yaml
dag: 
  - name: {{city-02}}
    title: {{City Dimension Ingester}}
    description: {{The job ingests city data from dropzone into raw zone}}
    tags:
      - {{Connect}}
      - {{City}}
    spec: 
      runAsUser: {{iamgroot}} 
      stack: {{flare:4.0}}
      compute: {{runnable-default}}
# Flare Stack-specific Section
      flare:
        {}
```

### **Flare Stack-specific Section**
```yaml
flare:
  driver:
    coreLimit: {{1000m}} 
    cores: {{1}}
    memory: {{1024m}}
  executor: 
    coreLimit: {{1000m}}
    cores: {{1}}
    instances: {{1}}
    memory: {{1024m}}
  job:
    explain: {{true}}
    logLevel: {{INFO}}
    streaming: # Streaming Section
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

The below table summarizes the various attributes within a Flare Job:

<center>

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`flare`](./configurations/flare_stack_specific_grammar.md#flare) | object | none | none | mandatory |
| [driver](./configurations/flare_stack_specific_grammar.md#driver) | object | none | none | optional |
| [`executor`](./configurations/flare_stack_specific_grammar.md#executor) | object | none | none | optional |
| [`job`](./configurations/flare_stack_specific_grammar.md#job) | object | none | none | mandatory |
| [`explain`](./configurations/flare_stack_specific_grammar.md#explain) | boolean | false | true/false | optional |
| [`logLevel`](./configurations/flare_stack_specific_grammar.md#loglevel) | string | INFO | INFO / WARN /<br>DEBUG/ ERROR | optional |
| [`streaming`](./configurations/streaming.md) | object | none | none | optional |
| [`inputs`](./configurations/inputs.md) | object | none | none | mandatory |
| [`steps`](./configurations/steps.md) | object | none | none | optional |
| [`outputs`](./configurations/outputs.md) | object | none | none | mandatory |
| [`assertions`](./configurations/assertions.md) | object | none | none | optional |
| [`actions`](./configurations/actions.md) | object | none | none | optional |

</center>

Refer to the link here for more information regarding the Flare Stack-specific Section attributes, click [here.](./configurations/flare_stack_specific_grammar.md)


A Flare Job can be further split into 5 sections:

#### **Inputs**

The `inputs` section encompasses crucial configuration settings necessary for extracting data from diverse sources, such as name, format, dataset address, etc. To facilitate reading data from multiple sources, an array of data source definitions are required. To obtain more detailed information, kindly refer to the link below.

[Inputs](./configurations/inputs.md)

#### **Outputs**

The `outputs` section provides comprehensive information regarding the storage location and naming convention for the output dataset. To access additional details, please refer to the link provided below.

[Outputs](./configurations/outputs.md)

#### **Steps**

The `steps` section outlines the prescribed sequence of tasks for data enrichment and processing, including but not limited to the addition of calculated columns, aggregations, and filtering via SQL. These are defined in `sequence` under `steps`. For further information, please consult the linked page.

[Steps](./configurations/steps.md)

#### **Streaming**

The `streaming` section encompasses properties that pertain to the execution of stream jobs. For further details, please refer to the page provided below.

[Streaming](./configurations/streaming.md)

#### **Assertions**

In the context of data quality, assertions refer to validation rules that are tailored to a particular business domain and serve to determine the fitness-for-purpose of datasets. The application of assertions enables the execution of additional validation checks on top of existing datasets, thereby enhancing their overall quality. Assertions are defined within the dedicated `assertions` section. To gain further insights, please refer to the following page.

[Assertions](./configurations/assertions.md)

To perform validation checks on datasets that are to be written, click [here.](./case_scenario/data_quality_jobs.md#pre-sink-assertions)

#### **Actions**

The DataOS platform provides comprehensive support for executing maintenance actions within the Icebase depot. These are specified within the `actions` section. For further information, please refer to the following page.

[Actions](./configurations/actions.md)