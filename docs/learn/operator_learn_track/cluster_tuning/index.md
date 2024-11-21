# Tuning and optimizing Clusters in DataOS

By default, Clusters in DataOS use predefined settings for simplicity. To tailor performance to specific workloads, you can enhance the Cluster manifest file with advanced attributes. This allows you to fine-tune memory limits, query execution policies, and resource configurations, ensuring efficiency and scalability. This guide covers how to customize and optimize Clusters for improved performance.

## Scenario

You’ve set up a Minerva Cluster to analyze customer transaction data. As the workload grows, you notice query performance lagging. By customizing the manifest file, you increase memory allocation with properties like query.max-memory and enable phased execution policies to optimize query scheduling. After applying the changes, the Cluster processes queries faster, ensuring smooth and efficient analytics for your team.

## Sample Cluster manifest with additional properties.
    
```yaml
name: minervac
version: v1
type: cluster
tags:
    - dataos:type:resource
    - dataos:resource:cluster
    - dataos:layer:user
    - dataos:workspace:public
description: the default minerva cluster 
owner: dataos-manager
workspace: public
cluster:
    compute: query-default
    type: minerva
    minerva:
    replicas: 2
    resources:
        requests:
        cpu: 2000m
        memory: 2Gi
        limits:
        cpu: 4000m
        memory: 16Gi
    depots:
        - address: dataos://icebase:default
        properties:
            hive.config.resources: '************************************'
            iceberg.compression-codec: '****'
            iceberg.file-format: '*******'
        - address: dataos://metisdb:default
        - address: dataos://bigquery:demo_prep
        - address: dataos://postgres:default
    catalogs:
        - name: cache
        type: memory
        properties:
            memory.max-data-per-node: '*****'
    coordinatorEnvs:
        CONF__config__exchange.max-buffer-size: 200MB
        CONF__config__optimizer.optimize-metadata-queries: "true"
        CONF__config__query.client.timeout: 12m
        CONF__config__query.max-memory: 15GB
        CONF__config__query.max-stage-count: "300"
        CONF__config__task.max-partial-aggregation-memory: 300MB
        CONF__oauth2-jwk__http-client__connect-timeout: 90s
        JVM__opts: --add-opens=java.base/java.nio=ALL-UNNAMED
    workerEnvs:
        CONF__config__exchange.max-buffer-size: 200MB
        CONF__config__optimizer.optimize-metadata-queries: "true"
        CONF__config__query.client.timeout: 12m
        CONF__config__query.max-memory: 15GB
        CONF__config__query.max-stage-count: "300"
        CONF__config__task.max-partial-aggregation-memory: 300MB
        CONF__oauth2-jwk__http-client__connect-timeout: 90s
        JVM__opts: --add-opens=java.base/java.nio=ALL-UNNAMED
    debug:
        logLevel: INFO
        trinoLogLevel: ERROR
    runAsApiKey: '****************************************************************************************'
    runAsUser: minerva-cluster
    maintenance:
    restartCron: 0 */8 * * *
    timezone: ""
```
    

## Resizing the Cluster

You can resize the Cluster as per the usage by adding the below properties in the Cluster manifest file.

### **`query.max-memory-per-node`**

**Description:** This property determines the maximum amount of user memory that a query can utilize on a worker. User memory is allocated during execution for components directly related to or controlled by the query, such as hash tables and sorting. If the user memory allocation of a query on any worker exceeds this limit, the query is terminated.

**Type:** Data size

**Key:**CONF__config__query. max-memory-per-node

**Default Value:** (JVM max memory * 0.3)

---

### **`query.max-memory`**

**Description:** This property defines the maximum amount of user memory that a query can use across the entire cluster. User memory is allocated during execution for components directly related to or controlled by the query, such as hash tables and sorting. If the user memory allocation of a query across all workers exceeds this limit, the query is terminated.

**Type:** Data size

**Key:** CONF__config__query.max-memory

**Default Value:** 20GB

---

### **`query.max-memory-per-task`**

**Description:** This property specifies the maximum amount of memory that a task can use on a node in the cluster. Note that support for this property is experimental.

**Type:** Data size

**Key:** CONF__config__query.max-memory-per-task

**Session Property:**query_max_total_memory_per_task

**Default Value:** None (unrestricted)

---

### **`memory.heap-headroom-per-node`**

**Description:** This property reserves a portion of the JVM heap as headroom or buffer for memory allocations that are not tracked by Trino.

**Type:** Data size

**Key:** CONF__config__memory.heap-headroom-per-node

**Default Value:** (JVM max memory * 0.3)

## Managing the Queries

### **Query Management Properties**

### **`query.execution-policy`**

**Description:** This property configures the algorithm used to schedule the stages of a query.

**Type:** String

**Key:** CONF__config__query.execution-policy

**Session Property:** execution_policy

**Default Value:** Phased

**Possible Value:** Phased, All-at-once, Legacy-phased

**Additional Information:** The available execution policies are as follows: - **Phased:** Stages are scheduled sequentially to avoid dependencies and maximize resource utilization, resulting in the lowest query wall time. - **All-at-once:** All stages of a query are scheduled simultaneously, leading to higher initial resource utilization but potentially longer queue times and higher query wait times due to inter-stage dependencies. - **Legacy-phased:** Similar to phased execution, but aims to minimize the number of running stages, potentially increasing query wall time.

---

### **`query.max-execution-time`**

**Description:** This property sets the maximum allowed execution time for a query on the cluster. It includes only the active execution time and excludes analysis, query planning, and queue wait times.

**Type:** Duration

**Key:** CONF__config__query.max-execution-time

**Session Property:** query_max_execution_time

**Default Value:** 100 days

---

### **`query.max-planning-time`**

**Description:** This property defines the maximum allowed planning time for a query. If the planning time exceeds this limit, the coordinator attempts to stop the query. Note that certain planning operations may not be immediately cancellable.

**Type:** Duration

**Key:** CONF__config__query.max-planning-time

**Default Value:** 10 minutes

**Session Property:** query_max_planning_time

---

### **`query.max-run-time`**

**Description:** This property specifies the maximum allowed total runtime for a query on the cluster. It includes analysis, planning, and queue wait times, providing the overall time allowed for a query to exist since its creation.

**Type:** Duration

**Key:** CONF__config__query.max-run-time

**Default Value:** 100 days

**Session Property:** query_max_run_time

---

### **`query.max-stage-count`**

**Description:** This property determines the maximum number of stages that can be generated per query. If a query exceeds this limit, it will be terminated with an error indicating that it has too many stages.

**Key:** CONF__config__query.max-stage-count

**Type:** Integer

**Default Value:** 100

**Min Value:** 1

**Warning:** Setting a high value for this property can cause instability in the cluster, leading to unrelated queries being terminated with a REMOTE_TASK_ERROR due to exceeding the maximum requests queued per destination.

---

### **`query.max-history`**

**Description:** This property sets the maximum number of queries to retain in the query history for statistical and informational purposes. Once this limit is reached, older queries are removed based on their age.

**Key:** CONF__config__query.max-history

**Type:** Integer

**Default Value:** 100

---

### **`query.min-expire-age`**

**Description:** This property specifies the minimum age of a query in the history before it is expired. Once expired, a query is removed from the query history buffer and is no longer accessible in the Web UI.

**Type:** Duration

**Key:** CONF__config__query.min-expire-age

**Default Value:** 15 minutes

## Spilling Management

<aside class="callout">
🗣

spilling refers to the process where data that cannot fit into the cluster's memory is temporarily written to disk or an external storage medium, such as local disk storage, network-attached storage, or cloud storage.

</aside>

You can manage the spilling by adding the below-given properties.

### **`spill-enabled`**

**Description:** This property enables spilling memory to disk in order to avoid exceeding memory limits for the query. Spilling works by offloading memory to disk, allowing queries with large memory footprints to proceed, albeit with slower execution times. Spilling is supported for aggregations, joins (inner and outer), sorting, and window functions. Please note that this property does not reduce the memory usage required for other join types. The `spill_enabled` session property can override this configuration.

**Type:** Boolean

**Key:** CONF__config__spill-enabled

**Default Value:** FALSE

---

### **`spiller-spill-path`**

**Description:** This property specifies the directory where spilled content is written. It can be a comma-separated list to spill simultaneously to multiple directories, leveraging multiple drives installed in the system. It is not recommended to spill to system drives. Importantly, avoid spilling to the drive where JVM logs are written to prevent disk overutilization, which may cause queries to fail.

**Type:** String

**Key:** CONF__config__spiller-spill-path

**Default Value:** No default value. Must be set when spilling is enabled

---

### **`spiller-max-used-space-threshold`**

**Description:** If the disk space usage ratio of a given spill path exceeds this threshold, the spill path is deemed ineligible for spilling.

**Type:** Double

**Key:** CONF__config__spiller-max-used-space-threshold

**Default Value:** 0.9

---

### **`spiller-threads`**

**Description:** This property determines the number of spiller threads. Increase this value if the default number of threads cannot fully utilize the underlying spilling device, such as when using RAID.

**Type:** Integer

**Key:** CONF__config__spiller-threads

**Default Value:** 4

---

### **`max-spill-per-node`**

**Description:** This property sets the maximum spill space to be used by all queries on a single node.

**Type:** Data Size

**Key:** CONF__config__max-spill-per-node

**Default Value:** 100GB

---

### **`query-max-spill-per-node`**

**Description:** This property defines the maximum spill space to be used by a single query on a single node.

**Type:** Data Size

**Key:** CONF__config__query-max-spill-per-node

**Default Value:** 100GB

### **`aggregation-operator-unspill-memory-limit`**

**Description:** This property defines the memory limit for unspilling a single instance of an aggregation operator.

**Type:** Data Size

**Key:** CONF__config__aggregation-operator-unspill-memory-limit

**Default Value:** 4MB

---

### **`spill-compression-enabled`**

**Description:** Enables data compression for pages that are spilled to disk.

**Type:** Boolean

**Key:** CONF__config__spill-compression-enabled

**Default Value:** FALSE

---

### **`spill-encryption-enabled`**

**Description:** Enables the use of a randomly generated secret key (per spill file) to encrypt and decrypt data that is spilled to disk.

**Type:** Boolean

**Key:** CONF__config__spill-encryption-enabled

**Default Value:** FALSE

## Managing exchange

<aside class="callout">
🗣

**Exchange** refers to the process of transferring data between nodes in a distributed system, often during query execution. Exchanges are crucial for enabling distributed systems to coordinate and process data across multiple nodes.

</aside>

Manage the exchange by adding the below properties.

### **`exchange.client-threads`**

**Description:** This property determines the number of threads used by exchange clients to fetch data from other Trino nodes. Increasing the value can improve performance for large clusters or clusters with high concurrency. However, setting excessively high values may result in performance degradation due to context switches and increased memory usage.

**Type:** Integer

**Key:** CONF__config__exchange.client-threads

**Default Value:** 25

**Min Value:** 1

---

### **`exchange.concurrent-request-multiplier`**

**Description:** This property determines the multiplier for the number of concurrent requests relative to the available buffer memory. The maximum number of requests is calculated based on the average buffer usage per request multiplied by this multiplier. The heuristic takes into account the available buffer space and aims to optimize concurrency and network utilization. Adjusting this value can increase concurrency and improve network utilization.

**Type:** Integer

**Key:** CONF__config__exchange.concurrent-request-multiplier

**Default Value:** 3

**Min Value:** 1

---

### **`exchange.data-integrity-verification`**

**Description:** This property configures the behavior in case of data integrity issues. By default, when data integrity issues are detected during the built-in verification, queries are aborted (ABORT). Setting the property to NONE disables the verification while setting it to RETRY repeats the data exchange when integrity issues are detected.

**Type:** String

**Key:** CONF__config__exchange.data-integrity-verification

**Default Value:** ABORT

**Allowed Values:** NONE, ABORT, RETRY

---

### **`exchange.max-buffer-size`**

**Description:** This property defines the size of the buffer in the exchange client that holds data fetched from other nodes before it is processed. A larger buffer size can increase network throughput for larger clusters, thereby reducing query processing time. However, it also reduces the available memory for other purposes.

**Type:** Data Size

**Key:** CONF__config__exchange.max-buffer-size

**Default Value:** 32MB

---

### **`exchange.max-response-size`**

**Description:** This property sets the maximum size of a response returned from an exchange request. The response is stored in the exchange client buffer, which is shared across all concurrent requests for the exchange. Increasing this value can improve network throughput, especially when there is high latency. Decreasing the value can improve query performance for large clusters by reducing skew, as the exchange client buffer can hold responses for more tasks.

**Type:** Data Size

**Key:** CONF__config__exchange.max-response-size

**Default Value:** 16MB

**Min Value:** 1MB

---

### **`sink.max-buffer-size`**

**Description:** This property determines the output buffer size for task data waiting to be pulled by upstream tasks. If the task output is hash partitioned, the buffer is shared among all partitioned consumers. Increasing this value can improve network throughput for data transferred between stages, particularly in cases of high network latency or when there are many nodes in the cluster.

**Type:** Data Size

**Key:** CONF__config__sink.max-buffer-size

**Default Value:** 32MB

---

### **`sink.max-broadcast-buffer-size`**

**Description:** This property specifies the broadcast output buffer size for task data waiting to be pulled by upstream tasks. The broadcast buffer is used to store and transfer build-side data for replicated joins. If the buffer size is too small, it can hinder the scaling of join probe side tasks when new nodes are added to the cluster.

**Type:** Data Size

**Key:** CONF__config__sink.max-broadcast-buffer-size

**Default Value:** 200MB

## Managing tasks

Manage the tasks by adding the below properties in the Cluster manifest file.

### **`task.concurrency`**

**Description:** This property defines the default local concurrency for parallel operators such as joins and aggregations. The value should be adjusted based on the query concurrency and worker resource utilization. Lower values are suitable for clusters that run many queries concurrently to avoid slowdowns due to context switching and overhead. Higher values are better for clusters that handle a smaller number of queries at a time. The `task_concurrency` session property allows specifying this value on a per-query basis.

**Type:** Integer

**Key:** CONF__config__task.concurrency

**Default Value:** 16

**Restrictions:** Must be a power of two.

---

### **`task.http-response-threads`**

**Description:** This property sets the maximum number of threads that can handle HTTP responses. Threads are created on-demand and cleaned up when idle. Increasing this value can be beneficial for clusters with a high number of concurrent queries or a large number of workers.

**Type:** Integer

**Key:** CONF__config__task.http-response-threads

**Default Value:** 100

**Min Value:** 1

---

### **`task.http-timeout-threads`**

**Description:** This property determines the number of threads used to handle timeouts when generating HTTP responses. If all threads are frequently in use, it may be necessary to increase this value. The thread utilization can be monitored through the `trino.server:name=AsyncHttpExecutionMBean:TimeoutExecutor` JMX object. If the `ActiveCount` is consistently the same as `PoolSize`, it indicates the need for more threads.

**Type:** Integer

**Key:** CONF__config__task.http-timeout-threads

**Default Value:** 3

**Min Value:** 1

---

### **`task.info-update-interval`**

**Description:** This property controls the staleness of task information used in scheduling. Larger values reduce coordinator CPU load but may result in suboptimal split scheduling.

**Type:** Duration

**Key:** CONF__config__task.info-update-interval

**Default Value:** 3s

**Min Value:** 1ms

**Max Value:** 10s

---

### **`task.max-drivers-per-task`**

**Description:** This property limits the maximum number of drivers that can run concurrently within a task. Setting this value reduces the likelihood of a task using too many drivers and can improve concurrent query performance. However, setting it too low may result in underutilized resources.

**Type:** Integer

**Key:** CONF__config__task.max-drivers-per-task

**Default Value:** 2147483647

**Min Value:** 1

---

### **`task.max-partial-aggregation-memory`**

**Description:** This property specifies the maximum size of partial aggregation results for distributed aggregations. Increasing this value can reduce network transfer and lower CPU utilization by allowing more groups to be kept locally before being flushed. However, it also increases memory usage.

**Type:** Data Size

**Key:** CONF__config__task.max-partial-aggregation-memory

**Default Value:** 16MB

---

### **`task.max-worker-threads`**

**Description:** This property determines the number of threads used by workers to process splits. Increasing this number can improve throughput if worker CPU utilization is low and all threads are in use. However, it also increases heap space usage. Setting the value too high may lead to a drop in performance due to context switching. The number of active threads can be monitored using the `RunningSplits` property of the `trino.execution.executor:name=TaskExecutor.RunningSplits` JMX object.

**Type:** Integer

**Key:** CONF__config__task.max-worker-threads

**Default Value:** (Node CPUs * 2)

---

### **`task.min-drivers`[¶](https://dataos.info/resources/cluster/performance_tuning/#taskmin-drivers)**

**Description:** This property represents the target number of running leaf splits on a worker. It acts as a minimum value because each leaf task is guaranteed to have at least 3 running splits. Non-leaf tasks are also ensured to run to prevent deadlocks. Adjusting this value can impact responsiveness for new tasks and resource utilization.

**Type:** Integer

**Key:** CONF__config__task.min-drivers

**Default Value:** (task.max-worker-threads * 2)

---

### **`task.min-drivers-per-task`[¶](https://dataos.info/resources/cluster/performance_tuning/#taskmin-drivers-per-task)**

**Description:** This property sets the minimum number of drivers guaranteed to run concurrently for a single task, assuming the task has remaining splits to process.

**Type:** Integer

**Key:** CONF__config__task.min-drivers-per-task

**Default Value:** 3

**Min Value:** 1

---

### **`task.writer-count`[¶](https://dataos.info/resources/cluster/performance_tuning/#taskwriter-count)**

**Description:** This property determines the number of concurrent writer threads per worker per query. Increasing this value can enhance write speed, particularly when a query is not I/O bound, and can take advantage of additional CPU for parallel writes. However, some connectors may experience CPU bottlenecks during writing due to compression or other factors. Setting this value too high may overload the cluster with excessive resource utilization. The `task_writer_count` session property allows specifying this value on a per-query basis.

**Type:** Integer

**Key:** CONF__config__task.writer-count

**Default Value:** 1

**Restrictions:** Must be a power of two.

When defining environment variables explicitly, ensure that you set `overrideDefaultEnvs` to `false` to avoid accepting default configurations.

Please [refer to this link](https://dataos.info/resources/cluster/) for more information about Cluster.