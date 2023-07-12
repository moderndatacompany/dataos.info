# Creating a Workflow

This section covers a Workflow YAML file structure,configuration options, and applying the YAML to create a Workflow resource.

## Workflow YAML File

To create a Workflow resource, you need to configure the YAML file with the appropriate settings. The following sections explain the necessary configurations.

### **Configuring the Resource Section**

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

For detailed customization options and additional fields within the Resource Section, refer to the [Resource Configuration](../../resources.md).

### **Configuring the Workflow-specific Section**

The Workflow-specific Section contains configurations specific to the Workflow resource. DataOS supports two types of workflows: scheduled and single-run workflows, each with its own YAML syntax.

#### **Scheduled Workflow**

A Scheduled Workflow triggers a series of jobs or tasks at particular intervals or predetermined times. To create a scheduled workflow, specify the scheduling configurations in the schedule section:
```yaml
workflow: 
    schedule: 
        cron: '/10 * * * *' 
    dag: 
        {collection-of-jobs}
```
<center><i>Worfklow Section Configuration - Scheduled</i></center>

#### **Single-Run Workflow**

A Single-run workflow executes only once. A Workflow without a schedule section is considered a single-run workflow. The YAML syntax for a single-run workflow is as follows:
```yaml
workflow: 
    dag: 
        {collection-of-jobs}
```
<center><i>Workflow Section Configuration - Single-Run</i></center>
Choose the appropriate workflow type based on your requirements.

For additional configuration options within the Workflow-specific section, refer to the [Workflow Grammar](./workflow_grammar.md).

### **Configuring the DAG Section**

A Directed Acyclic Graph (DAG) represents the sequence and dependencies between various jobs within the Workflow. A DAG must contain at least one job.

#### **Job**

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

### **Configuring the Stack-specific Section**

The Stack-specific Section allows you to specify the desired stack for executing your workflow. Depending on your requirements, you can choose from the following supported stacks:

- [Flare Stack](../stacks/flare.md): The Flare stack provides advanced capabilities for data processing and analysis.

- [Alpha Stack](../stacks/alpha.md): The Alpha stack offers a powerful environment for hosting web-application, and custom Docker images atop DataOS.

- [Data Toolbox Stack](../stacks/data_toolbox.md): The Data Toolbox stack provides a comprehensive set of tools and utilities for data manipulation and transformation.

- [Scanner Stack](../stacks/scanner.md): The Scanner Stack provides metadata ingestion capabilities from a source.

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


## Applying the Workflow YAML

Once you have constructed the Workflow YAML file, it's time to apply it and create the Workflow resource within the DataOS environment. Use the following `apply` command:

```shell
dataos-ctl apply -f <yaml-file-path> -w <workspace>
```

You have successfully created a Workflow Resource. Feel free to explore various case scenarios and advanced features related to Workflow resources.

[Implementing Single Run Workflow](./single_run_workflow.md)

[Scheduled or Cron Workflow](./scheduled_or_cron_workflow.md)

[Executing Multiple Workflow YAMLs from Single One](./executing_multiple_workflow_yamls_from_single_one.md)