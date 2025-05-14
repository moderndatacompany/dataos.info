In scenarios where there is a continuous requirement to process incoming data in real-time, Flare Stream Jobs offer an effective solution. However, it is advisable to exercise caution when creating Stream Jobs, as they should be reserved for cases where strict latency requirements exist, typically demanding a processing time of less than a minute, considering that they may incur higher computing costs.


## Available configurations for streaming job


| **Feature**                        | **Description**                                                                                                                                                                          | **Used In Which Trigger Modes?**                                             | **Notes**                                                                 |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `trigger (Trigger Mode)`          | Specifies the trigger mechanism that defines how and when streaming data is processed. Supported modes include `ProcessingTime`, `Continuous`, `Once`, and `AvailableNow`.                            | Applies to all modes (`Once`, `AvailableNow`, `ProcessingTime`, `Continuous`) | Defines how the Stream job triggers micro-batches or continuous tasks.    |
| `trigger durations`               | Configures the time interval between micro-batches or checkpoint commits depending on trigger mode. Used to control frequency of micro-batch execution or commit interval in continuous mode.         | Used in `ProcessingTime`, `Continuous` modes only                            | Defines the frequency (e.g., 10s) between batches or commits.             |
| `batchMode` | Used in orchestration layers to simulate batch-style jobs. Implied by triggers like `Once` or `AvailableNow`.                                                         | Typically used when using `Once`, `AvailableNow` triggers                    | Forces Stream Job to behave like a batch-style job. Implied by the trigger itself. |
| `foreachBatchMode`         | Applies custom logic to each micro-batch as a standard DataFrame, enabling batch-style integration with external systems.                                        | Used with any trigger that processes micro-batches (`ProcessingTime`, `AvailableNow`, `Once`) | Provides per-micro-batch DataFrame access. Not used in pure `Continuous` mode. |
| `startingOffsets` (Kafka-specific)| Specifies where Streaming job starts consuming topics (like in Kafka) when no checkpoint exists. Accepts `earliest`, `latest`.                                                 | Effective during first run of the query (with any trigger mode) if no checkpoint exists | Gets ignored if `checkpointLocation` exists (uses stored offsets).       |
| `checkpointLocation`              | Stores offsets, state, and metadata required to resume or recover streaming queries. Mandatory for exactly-once or stateful operations.                                                                | Required/recommended in all trigger modes if fault-tolerance or exactly-once is desired | Manages offsets, metadata, and state. Becomes the single source of truth after first execution. |

!!! info "Important considerations"

    - It is mandatory to provide `isStream:true` in the input section when creating a streaming job.
    - Always provide `checkpointLocation` to save all the progress information.

### **Trigger modes**

To control how frequently the streaming query checks for new data and processes it, Flare uses Trigger modes. By configuring the trigger mode, you can optimize for latency, throughput, or batch-style processing based on your use case. Following is the list of available trigger modes:


-  [Once](/resources/stacks/flare/case_scenario/streaming_jobs#once)
-  [ProcessingTime](/resources/stacks/flare/case_scenario/streaming_jobs#availablenow)
-  [AvailableNow](/resources/stacks/flare/case_scenario/streaming_jobs#processingtime)
-  [Continuous](/resources/stacks/flare/case_scenario/streaming_jobs#continuous)
  

#### **`Once`**

The query will execute only one micro-batch to process all the available data and then stop on its own. This is useful in scenarios you want to periodically spin up a cluster, process everything that is available since the last period, and then shutdown the cluster. In some case, this may lead to significant cost savings.

- **Latency**: Not applicable ( No  streaming continuity — acts like a batch job for all unprocessed data).
- **Use-cases**:  Ideal for periodic streaming jobs (e.g., nightly ETL processes).

!!! info

    You need to run it over a cron to periodically check the events came in that duration, process them and stop. For other trigger modes, cron is not needed.

**Example**

```yaml
version: v1
name: read-kafka
type: workflow
tags:
  - read-kafka
description: this jobs reads data from kafka
workflow:
  dag:
    - name: sample-read-kafka
      title: read kafka sample data
      spec:
        stack: flare:6.0
        compute: runnable-default

        stackSpec:
          job:
            explain: true
            streaming:
             batchMode: true
             triggerMode: Once #Once for cont
             checkpointLocation: dataos://lakehouse:stream/stream_checkpoint_read_once_15?acl=rw
            inputs:
              - name: sample_data
                dataset: dataos://${LAKEHOUSE_DEPOT_NAME}:${LAKEHOUSE_COLLECTION_NAME}/${STREAM_FOR_EACH_DATASET}?acl=rw
                isStream: true
                options:
                  startingOffsets: earliest
            logLevel: INFO
            outputs:
              - name: sample_data
                dataset: dataos://lakehouse:stream/stream_read_once_04?acl=rw
                format: Iceberg
                options:
                  saveMode: append
```

#### **`AvailableNow`**

AvailableNow Similar to `Once` trigger, the query will process all the available data and then stop on its own. The difference is that, it will process the data in (possibly) multiple micro-batches based on the source options which will result in better query scalability.

- This trigger provides a strong guarantee of processing: regardless of how many batches were left over in previous run, it ensures all available data at the time of execution gets processed before termination. All uncommitted batches will be processed first.
- Watermark gets advanced per each batch, and no-data batch gets executed before termination if the last batch advances the watermark. This helps to maintain smaller and predictable state size and smaller latency on the output of stateful operators.

**Example**

```yaml
version: v1
name: resource-metadata-lakehouse-sink-01
type: workflow
tags:
  - pulsar
  - read
workflow:
  dag:
    - name: resource-metadata-lakehouse-sink
      title: Resource Metadata Lakehouse Sink
      description: sinks resource metadata into an iceberg warehouse
      spec:
        tags:
          - Connect
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            showPreviewLines: 20
            streaming:
              forEachBatchMode: true
              triggerMode: AvailableNow
              checkpointLocation: dataos://lakehouse:stream/${CHECKPOINT_DATASET}
            inputs:
              - name: input
                dataset: dataos://${PULSAR_DEPOT_NAME}:${PULSAR_COLLECTION_NAME}/stream_${PULSAR_DATASET_SUFFIX}?acl=rw
                isStream: true
                options:
                  startingOffsets: earliest
            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://${ICEBASE_DEPOT_NAME}:${ICEBASE_COLLECTION_NAME}/${STREAM_FOR_EACH_DATASET}?acl=rw
                format: Iceberg
                options:
                  saveMode: append
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM input
```

#### **`ProcessingTime`**

- **Latency**: User-defined interval (e.g., every 5 or 10 seconds).
- **Use-cases**: 
    - Scenarios where small batches of data need to be processed periodically.

    - Applications requiring a balance between resource efficiency and acceptable latency, such as dashboard refresh, metric aggregation, or periodic data transformation.

**Example**

```yaml
version: v1
name: resource-metadata-lakehouse-sink-01
type: workflow
tags:
  - pulsar
  - read
workflow:
  dag:
    - name: resource-metadata-lakehouse-sink
      title: Resource Metadata Lakehouse Sink
      description: sinks resource metadata into an iceberg warehouse
      spec:
        tags:
          - Connect
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            showPreviewLines: 20
            streaming:
              forEachBatchMode: true
              triggerMode: ProcessingTime
              triggerDuration: 600 seconds
              checkpointLocation: dataos://lakehouse:stream/${CHECKPOINT_DATASET}
            inputs:
              - name: input
                dataset: dataos://${PULSAR_DEPOT_NAME}:${PULSAR_COLLECTION_NAME}/stream_${PULSAR_DATASET_SUFFIX}?acl=rw
                isStream: true
                options:
                  startingOffsets: earliest
            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://${ICEBASE_DEPOT_NAME}:${ICEBASE_COLLECTION_NAME}/${STREAM_FOR_EACH_DATASET}?acl=rw
                format: Iceberg
                options:
                  saveMode: append
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM input
```

#### **`Continuous`**

A trigger that continuously processes streaming data, asynchronously checkpointing at a specified interval (e.g., every 1 second).

- **Latency**: Near real-time (sub-second).

- **Use-cases**: Ideal for use cases with strict low-latency requirements and immediate event processing needs, such as financial transactions or fraud detections.


!!! info "Important considerations"

    There is no need to use `forEachBatchMode: true` in Continuous trigger mode as the data is fetched in near real-time.

**Example**

```yaml
version: v1
name: read-kafka
type: workflow
tags:
  - read-kafka
description: this jobs reads data from kafka
workflow:
  dag:
    - name: sample-read-kafka
      title: read kafka sample data
      spec:
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 2000m
            cores: 1
            memory: 1000m
          executor:
            coreLimit: 2000m
            cores: 1
            instances: 1
            memory: 2000m
          job:
            explain: true
            streaming:
             batchMode: true
             triggerMode: Continuous # options:  ProcessingTime | Continuous | AvailableNow | Once
             triggerDuration: 1 seconds
             checkpointLocation: dataos://lakehouse:stream/stream_cl1?acl=rw
            inputs:
              - name: sample_data
                dataset: dataos://stkafka:default/tmdc?acl=rw
                #dataset: dataos://kakafka:default/sensor_data?acl=rw
                format: kafkajson
                isStream: true
                options:
                  startingOffsets: earliest
            logLevel: INFO
            outputs:
              - name: sample_data
                dataset: dataos://lakehouse:stream/as_stream?acl=rw
                format: Iceberg
                options:
                  saveMode: append
```