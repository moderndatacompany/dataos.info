# Reading Stream Data 

## Overview

This use case describes the scenario when you want your Flare job to ingest  stream data  from  Kafka and save it to file systems, databases, Iceberg, etc. Flare provides a declarative stack to run Spark jobs.

## Solution approach

As Spark does not support writing streaming data, so this is achieved by using Spark Streaming API.
Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput stream processing of live data streams. 

Spark Streaming provides a high-level abstraction called discretized stream or DStream, which represents a continuous stream of data. DStreams can be created either from input data streams from sources such as Kafka. Internally, a DStream is represented as a sequence of RDDs.

Internally, Spark streaming  receives live input data streams and divides the data into batches, which are then processed by the Spark engine to generate the final stream of results in batches. 

## Implementation details 

Similar to RDDs, DStreams also allow developers to persist the stream’s data in memory. 

You need to define checkpointlocation to store the intermediate batches. The batched files are uploaded into a staging storage zone in DataOS, processed, and pushed into the main storage zone, batch by batch. 

Checkpointing of RDDs incurs the cost of saving to reliable storage. This may cause an increase in the processing time of those batches where RDDs get checkpointed. Hence, the interval of checkpointing needs to be set carefully using dstream.checkpoint(checkpointInterval). Checkpointing with large intervals may  cause the lineage and task sizes to grow, which may have detrimental effects. Typically, a checkpoint interval of 5 - 10 seconds of a DStream is recommended.


## Outcomes
The following Flare job saves the data from Kafka to Iceberg tables.

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
               # checkpointLocation: dataos://icebase:raw01/checkpoints/cloudevents/cedev01?acl=rw
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