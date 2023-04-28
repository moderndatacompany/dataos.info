# Read Stream Data as Batch

## Overview
This use case describes the scenario when you want to write an evolving stream data coming from Kafka to Iceberg table. 

As Iceberg does not support writing streaming data, so this is achieved by providing a buffering point from stream data coming from Kafka and moving data from this buffering point to the Iceberg table.


## Solution approach

Iceberg doesn’t support “continuous processing”, as it doesn’t provide the interface to “commit” the output.

Iceberg supports append and complete output modes:

- append: appends the rows of every micro-batch to the table
- complete: replaces the table contents every micro-batch

We need to buffer our writes as a micro batch. The batched files are uploaded into a staging storage zone in DataOS, processed, and committed into the main storage zone, batch by batch.

## Implementation details

Iceberg has snapshotId and timestamp, corresponding, Kafka has offset and
timestamp:

- offset: It is used for incremental read, such as the state of a checkpoint in a computing system.

- timestamp: It is explicitly specified by the user to specify the scope of consumption. 

You need to define checkpointlocation to store the intermediate batches.

## Outcomes


## Code files

```yaml
dag:
    - name: cloudevents-data
      title: stream data to dataset
      description: This job ingests stream data to Iceberg table
      spec:
        stack: flare:1.0
        flare:
          job:
            explain: true
            streaming:
              batchMode: true                      # to create batches
              triggerMode: Once #Once for cont
              checkpointLocation: dataos://icebase:raw01/checkpoints/cloudevents/ce01?acl=rw       
              #triggerDuration: "20 seconds"
            inputs:
             - name: input_cloudevents
               dataset: dataos://kafka:default/cloudevents?acl=r
               schemaRegistryUrl: http://schema-registry.caretaker:8081
               isStream: false
               options:
                  startingOffsets: earliest
            logLevel: INFO
            outputs:
             - name: output01
               depot: dataos://icebase:sys01?acl=rw
               # checkpointLocation: dataos://icebase:raw01/checkpoints/cloudevents/cedev01
            steps:
              - sequence:
                  - name: cloudevents
                    sql: SELECT *, time as _timestamp FROM input_cloudevents
                    functions:
                      - name: set_type
                        columns:
                          _timestamp: timestamp
                          time: timestamp
                sink:
                  - sequenceName: cloudevents
                    datasetName: cloudevents
                    outputName: output01
                    outputType: Iceberg
                    title: cloudevents data
                    description: cloudevents data
                    outputOptions:
                      saveMode: overwrite
                      # extraOptions:
                        # fanout-enabled: "true"
                      # triggerDuration: "20 seconds"
                      iceberg:
                        properties:
                          write.metadata.previous-versions-max: "10"
                          history.expire.max-snapshot-age-ms: "7200000"
                          overwrite-mode: dynamic
                        partitionSpec:
                          - type: identity
                            column: source
                          - type: hour
                            column: _timestamp
                            name: hour
                    tags:
                      - Cloudevents
```