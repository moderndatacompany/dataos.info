# Toolbox

Toolbox Stack or Data Toolbox Stack provides vital functionality in case of metadata updation in Icebase depots. When data is ingested into Icebase using Flare workflow, the metadata of ingested datasets needs to be registered with Metis before it can be queried using Workbench. The Data Toolbox allows `set_version` action on the data stored in the DataOS internal storage Icebase, which uses the Iceberg format. The Metis keeps track of the Iceberg table by storing a reference to the latest metadata file. Using the Data Toolbox `set_version` action, you can update the metadata version to the latest or any specific version.

## Performing Data Toolbox Actions

You can write Data Toolbox action as a separate workflow or part of a dag in a workflow. 

> 🗣️ For batch workloads, you can use both ways of performing the Toolbox action but for streaming workloads, you need to create separate workflows for Flare and Toolbox.


## Toolbox Action as a separate Workflow

To perform a data toolbox action, follow the below steps:

### Step 1: Create a YAML file for Workflow

If you have already ingested data, you can create a separate workflow for toolbox action, as shown in the following YAML. To know more, refer to [Workflow](../Primitives/Workflow/Workflow.md). 

### Step 2: Define a Job that executes upon Toolbox Stack

Within the DAG, define a job that executes upon the Toolbox Stack. To know more about the various properties for a job executed upon toolbox stack, refer to [Toolbox](./Toolbox.md). 

Sample Toolbox Workflow

```yaml
version: v1 # Version
name: dataos-toolbox-workflow # Workflow Name
type: workflow # Resource Type (Here its workflow)
workflow: # Workflow Section
  dag: # Directed Acyclic Graph (DAG)
	- name: dataos-toolbox-city-01 # Job Name
	      spec: # Specifications
	        stack: toolbox # Here stack is Toolbox
		      compute: runnable-default # Compute
	        toolbox: # Toolbox Specific Section
	          dataset: dataos://icebase:sample/city?acl=rw # UDL Address
	          action: # Toolbox Action 
	            name: set_version # Action Name
	            value: latest # Sets version to latest (if you wanna choose a specific version refer it here)
```

### Step 3: Apply the Workflow using CLI

Use the apply command to apply the workflow using CLI

```bash
dataos-ctl apply -f <path/file-name> -w <workspace> # By default the workspace is public so you may not include the -w flag
```

## Toolbox Action in a Job within the Flare Workflow

Instead of creating a separate workflow for Toolbox, you can create a single workflow. With a DAG with two jobs, one job runs on Flare Stack while the second one runs on the Toolbox Stack, which depends on the first job for the start of execution.

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

Once you define the workflow, you can apply it using [CLI](../CLI/CLI.md).

## Building Blocks of Toolbox Job

Here, you need to specify the configuration settings required to perform a data processing job such as driver, executor, inputs, outputs, steps, etc. You can define multiple jobs that will be executed in sequential order.

The below table summarizes the various attributes within the dag structure:

||||||||
| --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the job | `name: dataos-toolbox-city-01` | NA | NA | Rules for name: 37 alphanumeric characters and a special character '-' allowed. `[a-z0-9]([-a-z0-9]*[a-z0-9])`. The maximum permissible length for the name is 47, as showcased on CLI. Still, it's advised to keep the name length less than 30 characters because Kubernetes appends a Unique ID in the name which is usually 17 characters. Hence reduce the `name` length to 30, or your workflow will fail. | Mandatory |
| `title` | Title of the job | `title: Toolbox Job` | NA | NA | There is no limit on the length of the title. | Optional |
| `description` | This is the text describing the job. | `description: The job sets the metadata version to the latest using Toolbox stack` | NA | NA | There is no limit on the length of the description. | Optional |
| `spec` | Specs of job | `spec:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `{}` | NA | NA | NA | Mandatory |
| `tags` | Tags for the job | `tags:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `- Toolbox` <br>&nbsp;&nbsp;&nbsp;&nbsp; `- City` | NA | NA | The tags are case-sensitive, so `Connect` and `CONNECT` will be different tags. There is no limit on the length of the `tag`.  | Optional |
| `stack` | The Toolbox stack to run the workflow is defined here.  | `stack: toolbox` | NA | `toolbox` | NA | Mandatory |
| `toolbox` | Stack specific section | `toolbox:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `{}` | NA | NA | NA | Mandatory |
| `dataset` | Dataset addressThe dataset UDL address is defined here.  | `dataset: dataos://icebase:sample/city?acl=rw` | NA | NA | The dataset UDL should be defined in the form of `dataos://[depot]:[collection]/[dataset]` | Mandatory |
| `action` | The Toolbox action section | `action:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `{}` | NA | NA | NA | Mandatory |
| `name` | Name of the Toolbox Action | `name: set_version` | NA | `set_version` | The `set_verison` action sets the metadata version to any specific version you want it to. | Mandatory |
| `value` | The version of the metadata which you want to set to. | `value: latest` | NA | `latest/v2` or any specific version of the metadata. | You can use the `dataos-ctl list-metadata` to check the available metadata version for iceberg datasets. | Mandatory |