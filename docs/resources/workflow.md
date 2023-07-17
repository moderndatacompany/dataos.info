# Workflow

The Workflow in DataOS serves as a fundamental [Resource](../resources.md) for orchestrating data processing tasks with dependencies. It enables the creation of complex data workflows by defining a hierarchy based on a dependency mechanism.

## Workflows and Directed Acyclic Graphs (DAGs)

In DataOS, a Workflow represents a **Directed Acyclic Graph (DAG)**, where jobs are represented as nodes, and dependencies between jobs are represented as directed edges. The DAG structure provides a visual representation of the sequence and interdependencies of jobs within a Workflow. This facilitates efficient job execution by enabling parallel and sequential processing based on job dependencies.

Within a Workflow, a job encompasses a series of processing tasks, each executed within its dedicated Kubernetes pod. This architectural design ensures that the computational workload of one job does not hinder the performance of others, effectively avoiding bottlenecks.

Furthermore, every job within a Directed Acyclic Graph (DAG) is associated with a specific [Stack](./stacks.md). A Stack serves as an extension point within a job, offering users the ability to leverage different programming paradigms based on their specific requirements. For instance, if your objective involves data transformation, ingestion, or syndication, utilizing the [Flare](./stacks/flare.md) Stack is recommended. DataOS provides a diverse range of pre-built stacks, including [Flare](./stacks/flare.md), [Scanner](./stacks/scanner.md), [Alpha](./stacks/alpha.md), and more, enabling developers to seamlessly adopt various programming environments to suit their needs.



![Diagrammatic representation of a workflow](./workflow/workflow_overview.png)
<center><i>Diagrammatic representation of a Workflow Resource</i></center>


In the depicted example, **Job 1** is the first job to be executed as it has no dependencies. Once **Job 1** completes, both **Job 2** and **Job 3** can run concurrently or parallely. Only after the successful completion of both **Job 2** and **Job 3**, **Job 4** becomes eligible for execution. Finally, **Job 5** can be executed after **Job 4** successfully finishes. This hierarchical structure ensures optimal job execution without creating bottlenecks.

It is important to note that a Directed Acyclic Graph may have multiple root nodes, which means that a Workflow can contain both jobs and other workflows stored in different locations. This feature allows for the decomposition of complex workflows into manageable components. For more information on this scenario, refer to [Executing Multiple Workflow from a Single One.](./workflow/executing_multiple_workflow_yamls_from_single_one.md)


## Types of Workflows

Workflows in DataOS can be categorized as either [single-time run](#single-time-run-workflows) or [schedulable workflows](#schedulable-workflows).

### **Single-time run Workflows**

Single-time run workflows represent a one-time execution of a sequence of jobs. These workflows do not include scheduling capabilities and rely solely on the defined DAG structure and job dependencies.

### **Schedulable Workflows** 
Schedulable Workflows enable the automated and recurring execution of jobs based on specified intervals or predetermined times. To schedule a workflow, the `schedule` section must be added, allowing the configuration of scheduling parameters. Scheduled workflows provide a powerful mechanism for automating job execution based on a cron expression. To explore case scenarios for scheduled workflows, refer to the [Scheduled or Cron Workflow](./workflow/scheduled_or_cron_workflow.md)

## Syntax of a Workflow

The Workflow Resource is defined using a YAML configuration file. The following example illustrates the syntax for defining a single-time run workflow:

![Workflow Syntax](./workflow/workflow_yaml.png)

<center>

<i>
YAML Syntax of a Workflow Resource</i></center>

In this syntax, each job within the DAG is defined with a unique name, specifications, stack configuration, compute settings, and any Stack-specific configurations. Job dependencies are specified to ensure the correct execution order.

For a comprehensive reference of available fields and their configurations, please consult the [Workflow-specific Section Grammar](./workflow/workflow_grammar.md)

## Creating a Workflow

## Creating a Workflow

To create a Workflow resource, you need to configure the YAML file with the appropriate settings. The following sections explain the necessary configurations.

### **Workflow YAML Configuration**

#### **Configuring the Resource Section**

A Workflow is a type of resource in DataOS. Below is the YAML configuration for the Resource Section:
```yaml
name: {{my-workflow}}
version: v1 
type: workflow 
tags: 
  - {{dataos:type:resource}}
  - {{dataos:type:workspace-resource}}
  - {{dataos:resource:workflow}}
description: {{This is a sample workflow YAML configuration}}
owner: {{iamgroot}}
```
<center><i>Resource Section Configuration</i></center>

For detailed customization options and additional fields within the Resource Section, refer to the [Resource Configuration](../resources.md).

#### **Configuring the Workflow-specific Section**

The Workflow-specific Section contains configurations specific to the Workflow resource. DataOS supports two types of workflows: scheduled and single-run workflows, each with its own YAML syntax.

**Scheduled Workflow**

A Scheduled Workflow triggers a series of jobs or tasks at particular intervals or predetermined times. To create a scheduled workflow, specify the scheduling configurations in the schedule section:
```yaml
workflow: 
    schedule: 
        cron: '/10 * * * *' 
    dag: 
        {collection-of-jobs}
```
<center><i>Worfklow Section Configuration - Scheduled</i></center>

**Single-Run Workflow**

A Single-run workflow executes only once. A Workflow without a schedule section is considered a single-run workflow. The YAML syntax for a single-run workflow is as follows:
```yaml
workflow: 
    dag: 
        {collection-of-jobs}
```
<center><i>Workflow Section Configuration - Single-Run</i></center>
Choose the appropriate workflow type based on your requirements.

For additional configuration options within the Workflow-specific section, refer to the [Workflow-specific Section Grammar](./workflow/workflow_grammar.md)

#### **Configuring the DAG Section**

A Directed Acyclic Graph (DAG) represents the sequence and dependencies between various jobs within the Workflow. A DAG must contain at least one job.

**Job**

A Job denotes a single processing task. Multiple jobs within a DAG can be linked in series or parallel to achieve a specific result through `dependencies`. Here is an example YAML syntax for a job:
```yaml
  dag: 
    - name: {{job1-name}}
      spec: 
        stack: {{stack1:version}}
        compute: {{compute-name}}
        stack1: 
          {{stack1-specific-configuration}}
    - name: {{job2-name}}
      spec: 
        stack: {{stack2:version}}
        compute: {{compute-name}}
        stack2: 
          {{stack2-specific-configuration}}
      dependencies: 
       - {{job1-name}}
```
<center><i>DAG Section Configuration</i></center>

Note that actual configurations for a job may vary depending on the specific stack. The provided YAML snippet includes general configuration fields for a job.

The below table summarizes various fields/attributes within a Workflow YAML

<center>

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`workflow`](./workflow/workflow_grammar.md#workflow) | object | none | none | mandatory |
| [`schedule`](./workflow/workflow_grammar.md#schedule) | object | none | none | optional**  |
| [`cron`](./workflow/workflow_grammar.md#cron) | string | none | any valid cron expression. | optional**  |
| [`concurrencyPolicy`](./workflow/workflow_grammar.md#concurrencypolicy) | string | Allow | Allow/Forbid/Replace | optional |
| [`startOn`](./workflow/workflow_grammar.md#starton) | string | none | any time provided in ISO 8601 format. | optional |
| [`endOn`](./workflow/workflow_grammar.md#endon) | string | none | any time provided in ISO 8601 format. | optional |
| [`completeOn`](./workflow/workflow_grammar.md#completeon) | string | none | any time provided in ISO 8601 format. | optional |
| [`title`](./workflow/workflow_grammar.md#title) | string | none | any valid string | optional |
| [`name`](./workflow/workflow_grammar.md#name) | string | none | any string confirming the regex <br> [a-z0-9]\([-a-z0-9]*[a-z0-9]) and length<br>less than or equal to 48 | mandatory |
| [`title`](./workflow/workflow_grammar.md#title) | string | none | any string | optional |
| [`description`](./workflow/workflow_grammar.md#description) | string | none | any string | optional |
| [`spec`](./workflow/workflow_grammar.md#spec) | object | none | none | mandatory |
| [`runAsUser`](./workflow/workflow_grammar.md#runasuser) | string | none | userID of the Use Case <br>Assignee | optional |
| [`compute`](./workflow/workflow_grammar.md#compute) | string | none | runnable-default or any <br> other custom Compute Resource | mandatory |
| [`stack`](./workflow/workflow_grammar.md#stack) | string | none | flare/toolbox/scanner/<br>alpha | mandatory |
| [`retry`](./workflow/workflow_grammar.md#retry) | object | none | none | optional |
| [`count`](./workflow/workflow_grammar.md#count) | integer | none | any positive integer | optional |
| [`strategy`](./workflow/workflow_grammar.md#strategy) | string | none | Always/OnFailure/<br>OnError/OnTransientError | optional |
| [`dependency`](./workflow/workflow_grammar.md#dependency) | string | none | any job name within the workflow | optional |

</center>

<i>optional**:</i> Fields optional for single-run workflows, but mandatory for Scheduled workflows.

To know more about the various fields, click [here.](./workflow/workflow_grammar.md)

#### **Configuring the Stack-specific Section**

The Stack-specific Section allows you to specify the desired stack for executing your workflow. Depending on your requirements, you can choose from the following supported stacks:

- [Flare Stack](./stacks/flare.md): The Flare stack provides advanced capabilities for data processing and analysis.

- [Alpha Stack](./stacks/alpha.md): The Alpha stack offers a powerful environment for hosting web-application, and custom Docker images atop DataOS.

- [Data Toolbox Stack](./stacks/data_toolbox.md): The Data Toolbox stack provides a comprehensive set of tools and utilities for data manipulation and transformation.

- [Scanner Stack](./stacks/scanner.md): The Scanner Stack provides metadata ingestion capabilities from a source.

To configure the Stack-specific Section, refer to the appropriate stack documentation for detailed instructions on setting up and customizing the stack according to your needs. Each stack has its unique features and configurations that can enhance the functionality of your workflow.


<details>
<summary>
Click here to view a sample workflow
</summary>
The sample workflow ingests product data from the thirdparty01 depot and store it in the icebase depot. This workflow leverages the Flare stack to efficiently execute the necessary data ingestion tasks. The provided YAML code snippet outlines the configuration and specifications of this workflow.

```yaml
# Resource Section
version: v1
name: cnt-product-demo-01
type: workflow
tags:
- Connect
- Product
description: The workflow ingests product data from dropzone into raw zone

# Workflow-specific Section (Single-run)
workflow:
  title: Connect Product
  dag: # DAG of Jobs
  - name: product-01
    title: Product Dimension Ingester
    description: The job ingests product data from dropzone into raw zone
    spec:
      tags:
      - Connect
      - Product
      stack: flare:3.0
      compute: runnable-default
      envs:
        FLARE_AUDIT_MODE: LOG
# Stack-specific Section (Flare)
      flare:
        job:
          explain: true
          inputs:
           - name: product_connect
             dataset: dataos://thirdparty01:none/product
             format: csv
             schemaPath: dataos://thirdparty01:none/schemas/avsc/product.avsc
          logLevel: INFO
          outputs:
            - name: products
              dataset: dataos://icebase:retail/product?acl=rw
              format: Iceberg
              description: Customer data ingested from external csv
              options:
                saveMode: append
                sort:
                  mode: partition
                  columns:
                    - name: version
                      order: desc                            
                iceberg:
                  properties:
                    write.format.default: parquet
                    write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: identity
                      column: version
              tags:
                - Connect
                - Product
              title: Product Source Data
          steps:
          - sequence:
              - name: products
                doc: Pick all columns from products and add version as yyyyMMddHHmm formatted
                  timestamp.
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                  ts_product FROM product_connect LIMIT 10
```
</details>


### **Applying the Workflow YAML**

Once you have constructed the Workflow YAML file, it's time to apply it and create the Workflow Resource within the DataOS environment. Use the following `apply` command:

```shell
dataos-ctl apply -f {{yaml-file-path}} -w {{workspace}}
```

**Create Your Workspace (Optional)**

This optional step allows you to create a new Workspace for specific workflows. By default, you can always run your Workflows in the `public` workspace. To create a new workspace, execute the following command:

```shell
dataos-ctl workspace create -n {{name of your workspace}}
```

### **Monitoring Workflow**

#### **Get Status of the Workflow**

To retrieve information about the Workflow, use the `get` command in the CLI. This command lists the workflows created by you. To check this information for all users, add the `-a` flag to the command.

Command:

```shell
dataos-ctl -t workflow -w public get
```

Output:

```shell
INFO[0000] 🔍 get...
INFO[0001] 🔍 get...complete

        NAME        | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |   OWNER
--------------------|---------|----------|-----------|--------|---------|-------------
  cnt-product-demo-01 | v1      | workflow | public    | active | running |   tmdc
```

To view workflows created by everyone:

```shell
dataos-ctl -t workflow -w public get -a
```

Output:

```shell
INFO[0000] 🔍 get...
INFO[0001] 🔍 get...complete

                 NAME                | VERSION |   TYPE   | WORKSPACE | STATUS |  RUNTIME  |       OWNER
-------------------------------------|---------|----------|-----------|--------|-----------|--------------------
  checks-sports-data                 | v1      | workflow | public    | active | succeeded | user01
  cnt-product-demo-01                  | v1      | workflow | public    | active | running   | tmdc
  cnt-product-demo-01-01               | v1      | workflow | public    | active | succeeded | otheruser
  cnt-city-demo-01001                | v1      | workflow | public    | active | succeeded | user03
```

#### **Get Runtime Information**

To obtain the runtime status of the workflow, use the following command:

```shell
dataos-ctl get runtime -w {{workspace-name}} -t workflow -n {{name-of-workflow}}
```

Example:

```shell
dataos-ctl get runtime -w public -t workflow -n cnt-product-demo-01
```

Alternatively, you can extract the workflow information from the output of the `get` command and pass it as a string to the runtime command. Look for the relevant information (highlighted) in the `get` command output:

```shell
dataos-ctl -t workflow -w public get
# the output is shown below
        NAME        | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |   OWNER     
--------------------|---------|----------|-----------|--------|---------|-------------
  <b>cnt-product-demo-01 | v1      | workflow | public</b>    | active | running |   tmdc
```

Select from Name to workspace, for example `cnt-product-demo-01 | v1 | workflow | public`.

```shell
dataos-ctl -i " cnt-product-demo-01 | v1      | workflow | public" get runtime
```

<details>

<summary>Output</summary>

```shell
INFO[0000] 🔍 workflow...
INFO[0001] 🔍 workflow...complete

        NAME        | VERSION |   TYPE   | WORKSPACE |    TITLE     |   OWNER
--------------------|---------|----------|-----------|--------------|-------------
  cnt-product-demo-01 | v1      | workflow | public    | Connect City |   tmdc

  JOB NAME |   STACK    |        JOB TITLE        | JOB DEPENDENCIES
-----------|------------|-------------------------|-------------------
  city-001 | flare:3.0  | City Dimension Ingester |                   
  system   | dataos_cli | System Runnable Steps   |                   

  RUNTIME | PROGRESS |          STARTED          |         FINISHED
----------|----------|---------------------------|----------------------------
  failed  | 6/6      | 2022-06-24T17:11:55+05:30 | 2022-06-24T17:13:23+05:30

                NODE NAME              | JOB NAME |             POD NAME              |     TYPE     |       CONTAINERS        |   PHASE
--------------------------------------|----------|-----------------------------------|--------------|-------------------------|------------
  city-001-bubble-failure-rnnbl       | city-001 | cnt-product-demo-01-c5dq-2803083439 | pod-workflow | wait,main               | failed
  city-001-c5dq-0624114155-driver     | city-001 | city-001-c5dq-0624114155-driver   | pod-flare    | spark-kubernetes-driver | failed
  city-001-execute                    | city-001 | cnt-product-demo-01-c5dq-3254930726 | pod-workflow | main                    | failed
  city-001-failure-rnnbl              | city-001 | cnt-product-demo-01-c5dq-3875756933 | pod-workflow | wait,main               | succeeded
  city-001-start-rnnbl                | city-001 | cnt-product-demo-01-c5dq-843482008  | pod-workflow | wait,main               | succeeded
  cnt-product-demo-01-run-failure-rnnbl | system   | cnt-product-demo-01-c5dq-620000540  | pod-workflow | wait,main               | succeeded
  cnt-product-demo-01-start-rnnbl       | system   | cnt-product-demo-01-c5dq-169925113  | pod-workflow | wait,main               | succeeded
```
</details>

#### **Get Runtime Refresh**

To see updates on the workflow progress, execute the following command:

```shell
dataos-ctl -i " cnt-product-demo-01 | v1     | workflow | public" get runtime -r
```

Press `Ctrl + C` to exit.

### **Troubleshoot Errors**

#### **Check Logs for Errors**

To check the logs for errors, use the following command. Retrieve the node name from the output of the `get runtime` command for the failed node.

Command:

```shell
dataos-ctl -i "{{copy the name-to-workspace in the output table from get status command}}" --node {{failed-node-name-from-get-runtime-command}} log
```

Example:

```shell
dataos-ctl -i " cnt-product-demo-01 | v1 | workflow | public" --node city-001-c5dq-0624114155-driver log
```

You will notice an error message: "*There is an existing job with the same workspace. You should use a different job name for your job as you cannot change output datasets for any job.*"

#### **Fix the Errors**

Modify the YAML configuration by changing the name of the workflow. For example, rename it from `cnt-product-demo-01` to `cnt-city-demo-999`.

#### **Delete the Workflows**

Before rerunning the workflow, delete the previous version from the environment. There are two ways to delete the workflow as shown below.

**Method 1:** Copy the name-to-workspace from the output table of the get status command and use it as a string in the delete command.

Command

```shell
dataos-ctl -i "{{name-to-workspace in the output table from get status command}}" delete
```

Example:

```shell
dataos-ctl -i " cnt-product-demo-01 | v1 | workflow | public" delete
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0001] 🗑 deleting(public) cnt-product-demo-01:v1:workflow...
INFO[0003] 🗑 deleting(public) cnt-product-demo-01:v1:workflow...deleted
INFO[0003] 🗑 delete...complete
```

**Method 2:** Specify the path of the YAML file and use the `delete` command.

Command:

```shell
dataos-ctl delete -f {{file-path}}
```

Example:

```shell
dataos-ctl delete -f /home/desktop/flare/connect-city/config_v2beta1.yaml
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0000] 🗑 deleting(public) cnt-city-demo-010:v1:workflow...
INFO[0001] 🗑 deleting(public) cnt-city-demo-010:v1:workflow...deleted
INFO[0001] 🗑 delete...complete
```

**Method 3:** Specify the workspace, workflow type, and workflow name in the `delete` command.

Command:

```shell
dataos-ctl -w {{workspace}} -t workflow -n {{workflow-name}} delete
```

Example:

```shell
dataos-ctl -w public -t workflow -n cnt-product-demo-01 delete
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0000] 🗑 deleting(public) cnt-city-demo-010:v1:workflow...
INFO[0001] 🗑 deleting(public) cnt-city-demo-010:v1:workflow...deleted
INFO[0001] 🗑 delete...complete
```

#### **Rerun the Workflow**

Run the workflow again using the `apply` command. Check the runtime for its success. Scroll to the right to see the status, as shown in the previous steps.

Command:

```shell
dataos-ctl -i "{{copy the name-to-workspace in the output table from get status command}}" get runtime -r
```

Example:

```shell
dataos-ctl -i " cnt-city-demo-999 | v1 | workflow | public" get runtime -r
```

Output:

```shell
INFO[0000] 🔍 workflow...
INFO[0002] 🔍 workflow...complete

        NAME        | VERSION |   TYPE   | WORKSPACE |    TITLE     |   OWNER
--------------------|---------|----------|-----------|--------------|-------------
  cnt-city-demo-999 | v1 | workflow | public    | Connect City | mebinmoncy

  JOB NAME |   STACK    |        JOB TITLE        | JOB DEPENDENCIES
-----------|------------|-------------------------|-------------------
  city-999 | flare:2.0  | City Dimension Ingester |                   
  system   | dataos_cli | System Runnable Steps   |                   

    RUNTIME  | PROGRESS |          STARTED          |         FINISHED
------------|----------|---------------------------|----------------------------
  succeeded | 5/5      | 2022-06-24T17:29:37+05:30 | 2022-06-24T17:31:50+05:30

                NODE NAME              | JOB NAME |             POD NAME              |     TYPE     |       CONTAINERS        |   PHASE
--------------------------------------|----------|-----------------------------------|--------------|-------------------------|------------
  city-999-execute                    | city-999 | cnt-city-demo-999-lork-1125088085 | pod-workflow | main                    | succeeded
  city-999-lork-0624115937-driver     | city-999 | city-999-lork-0624115937-driver   | pod-flare    | spark-kubernetes-driver | completed
  city-999-start-rnnbl                | city-999 | cnt-city-demo-999-lork-1790287599 | pod-workflow | wait,main               | succeeded
  city-999-success-rnnbl              | city-999 | cnt-city-demo-999-lork-2939697963 | pod-workflow | wait,main               | succeeded
  cnt-city-demo-999-run-success-rnnbl | system   | cnt-city-demo-999-lork-2544494600 | pod-workflow | wait,main               | succeeded
  cnt-city-demo-999-start-rnnbl       | system   | cnt-city-demo-999-lork-2374735668 | pod-workflow | wait,main               | succeeded
```

Make sure to replace `{{name-to-workspace in the output table from get status command}}` and `{{file-path}}` with the actual values according to your workflow.

</details>



<aside class="best-practice">

📖 <i>Best Practice:</i><br> It is part of the best practice to add relevant <code>description</code> and <code>tags</code> for your workflow. While <code>description</code> helps to determine what the workflow will help you accomplish, <code>tags</code> can help in faster searching in Metis and Operations.
</aside>



## Case Scenarios

To deepen your understanding and expand your knowledge of Workflows, explore the following case scenarios that cover different aspects and functionalities:

- [Implementing Single Run Workflow](./workflow/single_run_workflow.md)

- [Scheduled or Cron Workflow](./workflow/scheduled_or_cron_workflow.md)

- [Executing Multiple Workflow YAMLs from a Single One](./workflow/executing_multiple_workflow_yamls_from_single_one.md)




