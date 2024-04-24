# Scheduled or Cron Workflow

The following code snippet illustrates a [Workflow](../workflow.md) involving a [Flare Stream Job](../stacks/flare.md#stream-job) that reads data from the <code>thirdparty01</code> [depot](../depot.md) in [streaming mode](../stacks/flare/case_scenario.md#stream-jobs) and subsequently writes to the [<code>eventhub</code>](../stacks/flare/configuration_templates/eventhub.md) [depot](../depot.md). During this process, all intermediate streams of data batches are stored at the location specified in the [<code>checkpointLocation</code>](../stacks/flare/configurations.md#checkpointlocation) attribute.

<details><summary>Click here to view the code snippet</summary>

```yaml
# Resource Section
name: write-eventhub-b-02
version: v1
type: workflow
tags:
  - eventhub
  - write
description: this jobs reads data from thirdparty and writes to eventhub

# Workflow-specific Section
workflow:
  dag:

# Job-specific Section
    - name: eventhub-write-b-02
      title: write data to eventhub
      description: write data to eventhub
      spec:
        tags:
          - Connect
        stack: flare:4.0
        compute: runnable-default

# Flare Stack-specific Section
        flare:
          job:
            explain: true
            streaming:
              checkpointLocation: /tmp/checkpoints/devd01
              forEachBatchMode: "true"
            inputs:
              - name: input
                dataset: dataos://thirdparty01:none/city
                format: csv
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc

            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://eventhub:default/eventhub01?acl=rw
                format: Eventhub

            steps:
              - sequence:
                - name: finalDf
                  sql: SELECT * FROM input
```
</details>

In the context of output depots, the automatic surfacing of metadata in the [Metis](../../interfaces/metis.md) is applicable to all depots except those supporting [Iceberg file formats with Hadoop Catalog type](../depot.md#limit-data-sources-file-format). For such depots, manual updating of the metadata version is required using the [Data Toolbox Stack](../stacks/data_toolbox.md) or by running the [set-metadata](../depot/icebase.md#set-metadata) command from the CLI. If there is a need to obtain the metadata at the end of transformation, when the entire data has been completely written to the output depot, you can execute a Workflow with a single job utilizing the [Data Toolbox](../stacks/data_toolbox.md) Stack once at the conclusion of the transformation process. Alternatively, if metadata is required at a specific cadence, [scheduling the Workflow](../workflow.md#scheduled-workflows) containing the job upon the [Data Toolbox Stack](../stacks/data_toolbox.md) can fulfill this requirement. 

The code snippet below illustrates a sample schedule Workflow for updating the metadata pointer using the [Toolbox](../stacks/data_toolbox.md) Stack in output depots with [Iceberg file format with Hadoop Catalog type.](../depot.md#limit-data-sources-file-format)

<details><summary>Click here to view the code snippet</summary>

```yaml
# Resource Section
name: dataos-tool-random-user
version: v1
type: workflow

# Workflow-specific Section
workflow:
  schedule:
    cron: '*/5 * * * *'
  dag:

# Job-specific Section
    - name: dataos-tool-job
      spec:
        stack: toolbox
        compute: runnable-default

# Toolbox Stack-specific Section
        toolbox:
          dataset: dataos://icebase:kafka/random_users_icebase01?acl=rw
          action:
            name: set_version
            value: latest
```
</details>

Once the metadata is updated, it becomes discoverable and accessible through the [Metis UI](../../interfaces/metis.md#metis-ui).
