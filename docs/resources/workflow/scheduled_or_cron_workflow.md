# Scheduled or Cron Workflow

The following code snippet illustrates a Workflow involving a Flare Stream Job that reads data from the <code>thirdparty01</code> depot in a streaming format and subsequently written to the <code>eventhub</code> depot. During this process, all intermediate streams of data batches are stored at the location specified in the <code>checkpointLocation</code> attribute.

**Code Snippet**

```yaml
name: write-eventhub-b-02
version: v1
type: workflow
tags:
  - eventhub
  - write
description: this jobs reads data from thirdparty and writes to eventhub
workflow:
  dag:
    - name: eventhub-write-b-02
      title: write data to eventhub
      description: write data to eventhub
      spec:
        tags:
          - Connect
        stack: flare:4.0
        compute: runnable-default
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

In the context of output depots, the automatic surfacing of metadata in the Metis is applicable to all depots except those supporting Iceberg file formats with Hadoop Catalog type. For such depots, manual updating of the metadata version is required using the Toolbox Stack. If there is a need to obtain the metadata at the end of transformation, when the entire data has been completely written to the output depot, you can execute the Toolbox Stack once at the conclusion of the transformation process. Alternatively, if metadata is required at a specific cadence, scheduling the job upon the Toolbox Stack can fulfill this requirement. 

The code snippet below illustrates a sample schedule workflow for updating the metadata pointer using the Toolbox Stack in output depots with Iceberg file format with Hadoop Catalog type.

```yaml
name: dataos-tool-random-user
version: v1
type: workflow
workflow:
  schedule:
    cron: '*/5 * * * *'
  dag:
    - name: dataos-tool-job
      spec:
        stack: toolbox
        compute: runnable-default
        toolbox:
          dataset: dataos://icebase:kafka/random_users_icebase01?acl=rw
          action:
            name: set_version
            value: latest
```

Once the metadata is updated, it becomes discoverable and accessible through the Metis UI.
