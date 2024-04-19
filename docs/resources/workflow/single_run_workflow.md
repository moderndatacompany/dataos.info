# Single-Run Workflow

A [Single-run Workflow](../workflow.md#single-run-workflow) represent a single-time execution of a sequence of jobs. It does not include a [`schedule`](./yaml_configuration_attributes.md#schedule) section.

<center>

![Illustration of a Single-run Workflow](./sample_workflow.svg)

</center>

<center>

*Illustration of a Single-run Workflow*

</center>

**Code Snippet**

The following code snippet illustrates a [Workflow](../workflow.md) with two jobs. The first one executes upon [Flare](../stacks/flare.md) Stack that reads data from the `thirdparty01` [depot](../depot.md) in [batch mode](../stacks/flare/case_scenario.md#batch-jobs) and subsequently writes to the [`icebase`](../depot/icebase.md) [depot](../depot.md). Once the first job, completes it execution the second job starts execution, which updates the metadata version using the [Toolbox](../stacks/data_toolbox.md) Stack.

<details><summary>Click here to view the Code Snippet</summary>

```yaml
# Resource Section
version: v1 
name: wf-tmdc-01 
type: workflow 
tags:
  - Connect
  - City
description: The job ingests city data from dropzone into raw zone

# Workflow-specific Section
workflow:
  title: Connect City
  dag: 

# Job 1 Specific Section
    - name: wf-job1 # Job 1 name
      title: City Dimension Ingester
      description: The job ingests city data from dropzone into raw zone
      spec:
        tags:
          - Connect
          - City
        stack: flare:4.0 # The job gets executed upon the Flare Stack, so its a Flare Job
        compute: runnable-default

        # Flare Stack-specific Section
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

# Job 2 Specific Section
    - name: datatool-1 # Job 2 name
      spec:
        stack: toolbox # The Job gets executed upon Toolbox Stack, so its a Toolbox Job 
        compute: runnable-default
        # Toolbox Stack-specific Section
        toolbox:
        dataset: dataos://icebase:retail/city01
        action:
          name: set_version
          value: latest
    # Job 2 Dependent on Job 1 for the start of execution
      dependencies: wf-job1
```

</details>