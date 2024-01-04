# Data Toolbox

Data Toolbox Stack or simply Toolbox Stack provides vital functionality in case of metadata updation in [Icebase](../depot.md#icebase) depots. When data is ingested into Icebase using [Flare](./flare.md) Stack, the metadata of ingested datasets needs to be registered with [Metis](../../interfaces/metis.md) before it can be queried using [Workbench](../../interfaces/workbench.md). The Data Toolbox allows `set_version` action on the data stored in the DataOS internal storage Icebase, which uses the Iceberg format. The [Metis](../../interfaces/metis.md) keeps track of the Iceberg table by storing a reference to the latest metadata file. Using the Data Toolbox `set_version` action, you can update the metadata version to the latest or any specific version.

## Syntax of Data Toolbox YAML Configuration

![Data Toolbox YAML Configuration Syntax](./data_toolbox/data_toolbox_syntax.png)

## Performing Data Toolbox Actions

You can write Data Toolbox action as a separate workflow or part of a dag in a workflow. 

<aside class="callout">
🗣️ For batch workloads, you can use both ways of performing the Toolbox action but for streaming workloads, you need to create separate workflows for Flare and Toolbox.

</aside>

## Toolbox Action as a separate Workflow

To perform a data toolbox action, follow the below steps:

### **Create a YAML file for Workflow**

If you have already ingested data, you can create a separate workflow for toolbox action, as shown in the following YAML. To know more about workflows, click [here](../workflow.md). 

### **Define a Job that executes upon Toolbox Stack**

Within the DAG, define a job that executes upon the Toolbox Stack. To know more about the various properties for a job executed upon toolbox stack, click [here](../workflow.md#configuring-the-dag-section). 

**Sample Toolbox Workflow**

```yaml
version: v1 
name: dataos-toolbox-workflow 
type: workflow 
workflow: 
  dag: 
    - name: dataos-toolbox-city-01 
      spec: 
      stack: toolbox 
      compute: runnable-default 
      toolbox: 
        dataset: dataos://icebase:sample/city?acl=rw 
        action: 
          name: set_version 
          value: latest 
```
The table below elucidates the various attributes within the Toolbox-specific Section.

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`toolbox`](./data_toolbox/data_toolbox_grammar.md#toolbox) | object | none | none | mandatory |
| [`dataset`](./data_toolbox/data_toolbox_grammar.md#dataset) | string | none | any valid iceberg dataset udl address | mandatory |
| [`action`](./data_toolbox/data_toolbox_grammar.md#action) | object | none | none | mandatory |
| [`name`](./data_toolbox/data_toolbox_grammar.md#name) | string | none | set_version | mandatory |
| [`value`](./data_toolbox/data_toolbox_grammar.md#value) | string | none | latest or any other specific metadata version | mandatory |


To know more about Toolbox-specfic Section YAML Configuration fields, click [here.](./data_toolbox/data_toolbox_grammar.md)

### **Apply the Workflow using CLI**

Use the apply command to apply the workflow using CLI

```bash
dataos-ctl apply -f <path/file-name> -w <workspace> # By default the workspace is public so you may not include the -w flag
```

## Toolbox Action in a Job within the Flare Workflow

Instead of creating a separate workflow for Toolbox, you can create a single workflow. With a DAG with two jobs, one job runs on Flare Stack while the second one runs on the Toolbox Stack, which depends on the first job for the start of execution.

<details>
<summary>Sample Toolbox Stack Action in a Job within a Workflow</summary>

```yaml
version: v1 # Version
name: wf-sample-002 # Workflow Name
type: workflow # Name of the Resource
tags: # Tags
- Con
- CONNECT
description: The job ingests data using Flare and registers the metadata using Toolbox Stack # Description of the Workflow
workflow: # Workflow Section
  title: Connect City # Title
  dag: # Directed Acyclic Graph

		# Job 1 executed upon Flare Stack: This job ingests city data
  - name: wf-sample-job-001
    title: City Data Ingester
    description: The job ingests city data 
    spec:
      tags:
      - Connect
      - City
      stack: flare:3.0
      compute: runnable-default
      flare:
        job:
          explain: true
          logLevel: INFO

          inputs:
           - name: city_connect
             dataset: dataos://thirdparty01:none/city
             format: csv
             schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc

          outputs:
            - name: cities
              dataset: dataos://icebase:retail/city01?acl=rw
              format: Iceberg
              description: City data ingested from external csv
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
          steps:
          - sequence:
              - name: cities
                doc: Pick all columns from cities and add version as yyyyMMddHHmm formatted
                  timestamp.
                sql: |
                    SELECT
                      *,
                      date_format (now(), 'yyyyMMddHHmm') AS version,
                      now() AS ts_city
                    FROM
                      city_connect

	# Job 2 executes upon Toolbox Stack: This job registers latest version of metadata to Metis
  - name: data-tool-job-001
    spec:
      stack: toolbox
      compute: runnable-default
      toolbox:
        dataset: dataos://icebase:retail/city01
        action:
          name: set_version
          value: latest
    dependencies: wf-sample-job-001
```
</details>

Once you define the workflow, you can apply it using [CLI](../../interfaces/cli.md).

