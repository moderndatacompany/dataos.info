# Streaming Jobs

In scenarios where there is a continuous requirement to process incoming data in real-time, Flare stream jobs offer an effective solution. However, it is advisable to exercise caution when creating stream jobs, as they should be reserved for cases where strict latency requirements exist, typically demanding a processing time of less than a minute, considering that they may incur higher computing costs.

## Attribute configuration table for streaming job:


| **Feature**                        | **Description**                                                                                                                                                                          | **Used In Which Trigger Modes?**                                             | **Notes**                                                                 |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [`trigger (Trigger Mode)`](/resources/stacks/flare/case_scenario/streaming_jobs#trigger-modes)         | Specifies the trigger mechanism that defines how and when streaming data is processed. Supported modes include `ProcessingTime`, `Continuous`, `Once`, and `AvailableNow`.                            | Applies to all modes (`Once`, `AvailableNow`, `ProcessingTime`, `Continuous`) | Defines how the Stream job triggers micro-batches or continuous tasks.    |
| `trigger durations`               | Configures the time interval between micro-batches or checkpoint commits depending on trigger mode. Used to control frequency of micro-batch execution or commit interval in continuous mode.         | Used in `ProcessingTime`, `Continuous` modes only                            | Defines the frequency (e.g., 10s) between batches or commits.             |
| `batchMode` | Used in orchestration layers to simulate batch-style jobs. Implied by triggers like `Once` or `AvailableNow`.                                                         | Typically used when using `Once`, `AvailableNow` triggers                    | Forces Stream Job to behave like a batch-style job. Implied by the trigger itself. |
| [`foreachBatchMode`](/resources/stacks/flare/case_scenario/streaming_jobs#foreachbatchmodes)        | Applies custom logic to each micro-batch, enabling batch-style integration with external systems.                                        | Used with any trigger that processes micro-batches (`ProcessingTime`, `AvailableNow`, `Once`) | Provides per-micro-batch dataset access. Not used in pure `Continuous` mode. |
| `startingOffsets` (Kafka-specific)| Specifies where Streaming job starts consuming topics (like in Kafka) when no checkpoint exists. Accepts `earliest`, `latest`.                                                 | Effective during first run of the query (with any trigger mode) if no checkpoint exists | Gets ignored if `checkpointLocation` exists (uses stored offsets).       |
| `checkpointLocation`              | For output sinks that support end-to-end fault-tolerance (such as Kafka, etc.), this setting specifies the location to store all checkpoint information, including offsets, state, and metadata required to resume or recover streaming queries. This must be a directory in an HDFS-compatible fault-tolerant file system. Mandatory for exactly-once semantics or stateful operations. | Required/recommended in all trigger modes if fault-tolerance or exactly-once is desired | Acts as the single source of truth after the first execution, enabling recovery and progress tracking. |


!!! info "Important considerations"

    - It is mandatory to provide `isStream:true` in the input section when creating a streaming job.
    - Always provide `checkpointLocation` to save all the progress information.



## **ForeachBatchMode**

The `foreachBatchMode` option enables treating each micro-batch of streaming data as a standard batch dataset when set to true.

This is particularly useful for storage systems that do not support direct streaming writes (e.g., JDBC, Snowflake, Iceberg, MongoDB), as it allows leveraging existing batch data writers.

It also facilitates writing the same micro-batch to multiple destinations, supporting scenarios like data replication or multi-environment writes.

!!! note

    `foreachBatchMode` does not work with the continuous processing mode as it fundamentally relies on the micro-batch execution of a streaming query. 

## **Trigger modes**

The `triggerMode` controls the frequency and style in which streaming data is processed. By setting an appropriate trigger mode, you can decide whether the streaming query operates in micro-batch mode (processing data in discrete intervals) or in continuous mode (processing data as soon as it arrives).

This setting is crucial to balance between latency, throughput, and cost-efficiency, depending on your business needs. Here are the different kinds of triggers that are supported:

### **`Unspecified(default)`** 


If no trigger setting is explicitly specified, then by default, the query will be executed in micro-batch mode, where micro-batches will be generated as soon as the previous micro-batch has completed processing.


### **`Once`**

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
            inputs:
              - name: sample_data
                dataset: dataos://systemstreams:audit/themis_query_events_03?acl=rw
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
                  checkpointLocation: dataos://lakehouse:checkpoints/tqueryeventsync01
```

### **`AvailableNow`**

Similar to `Once` trigger, the query will process all the available data and then stop on its own. The difference is that, it will process the data in (possibly) multiple micro-batches based on the source options which will result in better query scalability.

- This trigger provides a strong guarantee of processing: regardless of how many batches were left over in previous run, it ensures all available data at the time of execution gets processed before termination. All uncommitted batches will be processed first.
- Watermark gets advanced per each batch, and no-data batch gets executed before termination if the last batch advances the watermark. This helps to maintain smaller and predictable state size and smaller latency on the output of stateful operators.

**Example**

```yaml
version: v1
name: resource-metadata-lakehouse-sink-01
type: workflow
tags:
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
                dataset: dataos://${DEPOT_NAME}:${COLLECTION_NAME}/stream_${DATASET_SUFFIX}?acl=rw
                isStream: true
                options:
                  startingOffsets: earliest
            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://${LAKEHOUSE_DEPOT_NAME}:${LAKEHOUSE_COLLECTION_NAME}/${STREAM_FOR_EACH_DATASET}?acl=rw
                format: Iceberg
                options:
                  saveMode: append
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM input
```

### **`ProcessingTime`**

Processes data at a fixed time interval (e.g., every 5 seconds). The query will be executed with micro-batches mode, where micro-batches will be kicked off at the user-specified intervals.

- If the previous micro-batch completes within the interval, then the engine will wait until the interval is over before kicking off the next micro-batch.
- If the previous micro-batch takes longer than the interval to complete (i.e. if an interval boundary is missed), then the next micro-batch will start as soon as the previous one completes (i.e., it will not wait for the next interval boundary).
- If no new data is available, then no micro-batch will be kicked off.

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
                dataset: dataos://${DEPOT_NAME}:${COLLECTION_NAME}/stream_${DATASET_SUFFIX}?acl=rw
                isStream: true
                options:
                  startingOffsets: earliest
            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://${LAKEHOUSE_DEPOT_NAME}:${LAKEHOUSE_COLLECTION_NAME}/${STREAM_FOR_EACH_DATASET}?acl=rw
                format: Iceberg
                options:
                  saveMode: append
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM input
```

### **`Continuous`**

A trigger that continuously processes streaming data, asynchronously checkpointing at a specified interval (e.g., every 1 second).

- **Latency**: Near real-time (sub-second).

- **Use-cases**: Ideal for use cases with strict low-latency requirements and immediate event processing needs, such as financial transactions or fraud detections.

!!! info 

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

## Kafka specific configurations

In Kafka, every message is structured as a key-value pair:

- The key helps determine which partition the message is routed to, ensuring ordering of messages with the same key.

- The value contains the actual data payload that is processed downstream.

Even if the producer does not explicitly provide a key (null), Kafka maintains the key-value message structure.

When consumed in Flare streaming, messages from Kafka arrive in their native key and value structure, but both are received as raw binary (byte[]) format.

This raw format is not human-readable and must be explicitly deserialized by the developer inside Flare.

The most common and straightforward approach to deserialize these fields is to use the `CAST` operation during  transformations, converting the key and value into a readable string format.

**Example transformation**

```yaml hl_lines='7-8'
steps:
  - sequence:
      - name: final
        sql: |
          SELECT 
            *,
            CAST(key AS STRING) AS key_string,
            CAST(value AS STRING) AS value_string
          FROM
            kafka
```

??? note "Click here to view the full manifest file"

    ```yaml 
    version: v1
    name: kafka-lakehouse-if-stream-flare
    type: workflow
    tags:
      - Tier.Gold
    description: This workflow is responsible for getting insight finder insights data from kafka and persist the lakehouse
    workflow:
      title: Insight finder raw insights
      dag:
        - name: kafka-lakehouse-if-stream-flare
          description: This workflow is responsible for getting insight finder insights data from kafka and persist the lakehouse
          title: Insight finder raw insights
          spec:
            tags:
              - Tier.Gold
            stack: flare
            compute: query-default
            stackSpec:
              job:
                explain: true
                streaming:
                  triggerMode: Continous
                  checkpointLocation: dataos://lakehouse:sys01/if_kafka_raw/if_kafka_raw_ip_chkpt
                  showPreviewLines: 20
                inputs:
                  - name: kafka
                    dataset: dataos://kafkadepot:none/if-raw-test?acl=rw
                    format: KAFKAJSON
                    isStream: true
                    options:
                      startingOffsets: earliest
                      # failOnDataLoss: false
                logLevel: INFO
                outputs:
                  - name: final
                    dataset: dataos://lakehouse:raw/if_raw_data?acl=rw
                    format: Iceberg
                    description: The kafka test depot
                    tags:
                      - Tier.Gold
                    options:
                      saveMode: append
                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip
                          write.metadata.previous-versions-max: "10"
                          history.expire.max-snapshot-age-ms: "7200000"
                    title: Device Audit Record Source Dataset

                steps:
                  - sequence:
                      - name: final
                        sql: |
                          SELECT 
                            *,
                            CAST(key AS STRING) AS key_string,
                            CAST(value AS STRING) AS value_string
                          FROM
                            kafka
    
    ```