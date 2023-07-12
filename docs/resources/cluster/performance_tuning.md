# Performance Tuning

The Minerva query engine is specifically designed to handle large data sets distributed across diverse data sources. However, executing complex queries with big data on Minerva may require some optimization to improve performance. This section outlines several key considerations that can help you accelerate your queries on Minerva.

## Cluster Sizing

To ensure optimal performance, it is crucial to appropriately size your Minerva cluster nodes. A Minerva cluster consists of a single driver (coordinator) node and multiple worker nodes. The coordinator node analyzes and plans query execution, distributing the query plan among the worker nodes for processing within the cluster. The driver node executes parallel operations on the worker nodes, leveraging connectors specific to your data sources (e.g., Snowflake, Postgres, Oracle) to read and transform data.

While the driver and worker nodes can have different instance types, Minerva's default configuration maintains consistent configurations for all worker nodes. It's important to note that Minerva clusters are static and do not automatically resize based on workloads.

Minerva utilizes parallel processing and pipelined execution across cluster nodes, making efficient use of available resources such as memory, CPU, and network allocation. The multithreaded execution model ensures maximum utilization of CPU cores. Additionally, it's essential to manage user and query concurrency requirements, considering potential fluctuations during peak and off-hours.

Query execution time is influenced by three primary dimensions: CPU time, memory requirements, and network bandwidth usage. These factors apply to both single-query and concurrent workloads. Increasing the number of CPUs can result in shorter query durations, while memory is critical for performing operations like joins, group by, and order by in your queries. These dimensions collectively contribute to the overall cost of executing queries in Minerva.

When sizing your cluster, consider the following factors:

- Data Volume: The total amount of data you need to process
- Data Growth: Anticipated data growth over time

## Small Clusters vs. Big Clusters

When initially setting up your cluster, it's advisable to start with a larger cluster size than what is strictly necessary. This allows you to ensure stability and validate that all components are functioning correctly. Running workloads on a small cluster can easily exceed resource limits (CPU, memory, network), resulting in query failures or prolonged waiting times. A single big query on a small cluster can lead to queuing and unreliable response times for query results.

If required, you can provide specific examples to determine the appropriate cluster size for different use cases.

## Machine Default Settings

Ensure that the default machine settings are sufficiently large to support the expected cluster configurations for your desired workloads. Consider the following aspects:

### **Managing Memory**
Account for memory required by the operating system for processes such as the kernel, disk, and network buffers.
### **JVM**
Configure your virtual machine options. You can use the provided diagnostic options to troubleshoot garbage collection (GC) issues.

Java heap configuration is also essential. Allocate memory for OS processes, JVM processes (e.g., garbage collection, thread management), and query processing. Here's a recommended memory allocation breakdown:

- Approximately 20% for OS overhead
- 80% allocated to the Java heap, with around 70% dedicated to query memory

For example, on a 128 GB machine, allocate 100 GB to JVM Heap and reserve 70 GB for Minerva Query Memory.

Using larger machines with fewer instances is generally preferable, as it reduces memory overhead per machine and minimizes coordination efforts. It is recommended to disable OS spilling, as JVM is not designed for spilling. Instead, scale up the cluster size for larger queries. Spilling can cause queuing issues due to slow disk access. Furthermore, disabling the "runaway" process detector is advisable since Minerva efficiently utilizes all available resources.

## Workload Tuning

To optimize your workload in Minerva, it's crucial to understand the characteristics and requirements of your overall workload. Different use cases may require different instance types and configurations. Consider the following aspects to minimize errors caused by timeouts and resource limitations:

- Identify the types of queries you run: Determine if they are memory-intensive or compute-intensive.
- Define the expected latency for your queries.
- Specify the desired consistency level.
- Evaluate the concurrency of your workload, as higher concurrency requires more core memory.
- Assess the average amount of data involved in typical queries.
- Determine peak load requirements in terms of CPU and memory.

### **Recommendations**

In high-concurrency or heavy-workload environments, it is recommended to oversize your Minerva cluster to achieve optimal performance. Additionally, closely monitor performance under different query loads and fine-tune the configuration as necessary. Refer to the provided examples for further guidance.

## Storage Formats

While optimizing query execution by addressing infrastructure aspects is important, it's equally essential to enhance storage performance. Storage performance is influenced by two key factors: latency and throughput. Latency refers to the time taken to retrieve data for end-users, while throughput represents the amount of data read by a query over time.

Improving storage performance in Minerva involves considerations related to file formats, sizes, compression, and organization. These optimizations can significantly enhance query performance.


### **Recommendations**

- **Use columnar formats that efficiently store data**

Minerva processes data in vectorized columns, holding only the relevant data for processing and compressing each column individually. Icebase stores data in the Parquet format, which is optimized for fast data retrieval.

- **Optimize file size**

File size has a significant impact on query processing. Small files result in numerous small IO requests, which can affect performance due to high latency, throttling, or IO capacity limitations. Handling each file separately increases scheduling time and costs. To mitigate these issues, use file sizes of at least 100MB to overcome potential IO-related challenges. DataOS enables merging and compacting data/metadata files within Icebase data storage.

- **Apply data compression**

Compressing your data can significantly enhance performance. Icebase stores data in the Apache Parquet format, which offers built-in data compression.

- **Partition your data**

Partitioning involves dividing your table into segments based on specific column values (e.g., date, vendor ID, product ID). This strategy keeps related data together and reduces the amount of data scanned for queries involving predicates on partitioned columns, thereby improving performance.


- **Sort your data**

Sorting your data can also improve performance by narrowing down the range of partitions that need to be read by Minerva. If you filter based on a sorted column, Minerva can efficiently skip irrelevant chunks of data.

## Configuration Properties

To achieve optimal performance for your specific workload, you may need to adjust Minerva's configuration properties. DataOS allows you to customize these properties and tune their behavior as needed. The Minerva cluster YAML configuration defines these properties for coordinator and worker nodes under the `Env` section.

```yaml
cluster:
  compute: query-default 
  runAsUser:  
  minerva: 
    selector:
      users:
        - "**"
      sources:
        - "**"
    replicas: 2 
    resources: 
      limits: 
        cpu: 2000m 
        memory: 4Gi 
      requests: 
        cpu: 2000m 
        memory: 4Gi 
    debug: 
      logLevel: INFO 
      trinoLogLevel: ERROR
    coordinatorEnvs:               # for coordinator
      CONF__config__query.max-memory: "2GB"
    workerEnvs:                   # for worker
      CONF__config__query.max-memory: "2GB"
```

### **Category: Memory Management Properties**

#### **`query.max-memory-per-node`**

<b>Description:</b> This property determines the maximum amount of user memory that a query can utilize on a worker. User memory is allocated during execution for components directly related to or controlled by the query, such as hash tables and sorting. If the user memory allocation of a query on any worker exceeds this limit, the query is terminated.<br>
<b>Type:</b> Data size<br>
<b>Key:</b>CONF__config__query.
max-memory-per-node<br>
<b>Default Value:</b> (JVM max memory * 0.3)<br>

---

#### **`query.max-memory`**
<b>Description:</b> This property defines the maximum amount of user memory that a query can use across the entire cluster. User memory is allocated during execution for components directly related to or controlled by the query, such as hash tables and sorting. If the user memory allocation of a query across all workers exceeds this limit, the query is terminated. <br>
<b>Type:</b> Data size <br>
<b>Key:</b> CONF__config__query.max-memory <br>
<b>Default Value:</b> 20GB <br>

---

#### `query.max-memory-per-task`
<b>Description:</b> This property specifies the maximum amount of memory that a task can use on a node in the cluster. Note that support for this property is experimental. <br>
<b>Type:</b> Data size <br>
<b>Key:</b> CONF__config__query.max-memory-per-task <br>
<b>Session Property:</b>query_max_total_memory_per_task<br>
<b>Default Value:</b> None (unrestricted) <br>

---

#### `memory.heap-headroom-per-node`

**Description:** This property reserves a portion of the JVM heap as headroom or buffer for memory allocations that are not tracked by Trino.<br>
**Type:** Data size<br>
**Key:** CONF__config__memory.heap-headroom-per-node<br>
**Default Value:** (JVM max memory * 0.3)

---

### **Category: Query Management Properties**

#### `query.execution-policy`

**Description:** This property configures the algorithm used to schedule the stages of a query.<br>
**Type:** String<br>
**Key:** CONF__config__query.execution-policy<br>
**Session Property:** execution_policy<br>
**Default Value:** Phased<br>
**Possible Value:** Phased, All-at-once, Legacy-phased<br>
**Additional Information:** The available execution policies are as follows:
- **Phased:** Stages are scheduled sequentially to avoid dependencies and maximize resource utilization, resulting in the lowest query wall time.
- **All-at-once:** All stages of a query are scheduled simultaneously, leading to higher initial resource utilization but potentially longer queue times and higher query wait times due to inter-stage dependencies.
- **Legacy-phased:** Similar to phased execution, but aims to minimize the number of running stages, potentially increasing query wall time.

---

#### `query.max-execution-time`

**Description:** This property sets the maximum allowed execution time for a query on the cluster. It includes only the active execution time and excludes analysis, query planning, and queue wait times.<br>
**Type:** Duration<br>
**Key:** CONF__config__query.max-execution-time<br>
**Session Property:** query_max_execution_time<br>
**Default Value:** 100 days<br>

---

#### `query.max-planning-time`

**Description:** This property defines the maximum allowed planning time for a query. If the planning time exceeds this limit, the coordinator attempts to stop the query. Note that certain planning operations may not be immediately cancellable.<br>
**Type:** Duration<br>
**Key:** CONF__config__query.max-planning-time<br>
**Default Value:** 10 minutes<br>
**Session Property:** query_max_planning_time

---

#### `query.max-run-time`

**Description:** This property specifies the maximum allowed total runtime for a query on the cluster. It includes analysis, planning, and queue wait times, providing the overall time allowed for a query to exist since its creation.<br>
**Type:** Duration<br>
**Key:** CONF__config__query.max-run-time<br>
**Default Value:** 100 days<br>
**Session Property:** query_max_run_time

---

#### `query.max-stage-count`


**Description:** This property determines the maximum number of stages that can be generated per query. If a query exceeds this limit, it will be terminated with an error indicating that it has too many stages.<br>
**Key:** CONF__config__query.max-stage-count<br>
**Type:** Integer<br>
**Default Value:** 100<br>
**Min Value:** 1<br>
**Warning:** Setting a high value for this property can cause instability in the cluster, leading to unrelated queries being terminated with a REMOTE_TASK_ERROR due to exceeding the maximum requests queued per destination.

---

#### `query.max-history`

**Description:** This property sets the maximum number of queries to retain in the query history for statistical and informational purposes. Once this limit is reached, older queries are removed based on their age.<br>
**Key:** CONF__config__query.max-history<br>
**Type:** Integer<br>
**Default Value:** 100

---

#### `query.min-expire-age`

**Description:** This property specifies the minimum age of a query in the history before it is expired. Once expired, a query is removed from the query history buffer and is no longer accessible in the Web UI.<br>
**Type:** Duration<br>
**Key:** CONF__config__query.min-expire-age<br>
**Default Value:** 15 minutes

---

### **Category: Spilling Properties**

#### **`spill-enabled`**

**Description:** This property enables spilling memory to disk in order to avoid exceeding memory limits for the query. Spilling works by offloading memory to disk, allowing queries with large memory footprints to proceed, albeit with slower execution times. Spilling is supported for aggregations, joins (inner and outer), sorting, and window functions. Please note that this property does not reduce the memory usage required for other join types. The `spill_enabled` session property can override this configuration.<br>
**Type:** Boolean<br>
**Key:** CONF__config__spill-enabled<br>
**Default Value:** FALSE

---

#### **`spiller-spill-path`**

**Description:** This property specifies the directory where spilled content is written. It can be a comma-separated list to spill simultaneously to multiple directories, leveraging multiple drives installed in the system. It is not recommended to spill to system drives. Importantly, avoid spilling to the drive where JVM logs are written to prevent disk overutilization, which may cause queries to fail.<br>
**Type:** String<br>
**Key:** CONF__config__spiller-spill-path<br>
**Default Value:** No default value. Must be set when spilling is enabled

---

#### **`spiller-max-used-space-threshold`**

**Description:** If the disk space usage ratio of a given spill path exceeds this threshold, the spill path is deemed ineligible for spilling.<br>
**Type:** Double<br>
**Key:** CONF__config__spiller-max-used-space-threshold<br>
**Default Value:** 0.9

---

#### **`spiller-threads`**

**Description:** This property determines the number of spiller threads. Increase this value if the default number of threads cannot fully utilize the underlying spilling device, such as when using RAID.<br>
**Type:** Integer<br>
**Key:** CONF__config__spiller-threads<br>
**Default Value:** 4

---

#### **`max-spill-per-node`**

**Description:** This property sets the maximum spill space to be used by all queries on a single node.<br>
**Type:** Data Size<br>
**Key:** CONF__config__max-spill-per-node<br>
**Default Value:** 100GB

---


#### **`query-max-spill-per-node`**

**Description:** This property defines the maximum spill space to be used by a single query on a single node.<br>
**Type:** Data Size<br>
**Key:** CONF__config__query-max-spill-per-node<br>
**Default Value:** 100GB


#### **`aggregation-operator-unspill-memory-limit`**

**Description:** This property defines the memory limit for unspilling a single instance of an aggregation operator.<br>
**Type:** Data Size<br>
**Key:** CONF__config__aggregation-operator-unspill-memory-limit<br>
**Default Value:** 4MB

---

#### **`spill-compression-enabled`**

**Description:** Enables data compression for pages that are spilled to disk.<br>
**Type:** Boolean<br>
**Key:** CONF__config__spill-compression-enabled<br>
**Default Value:** FALSE

---

#### **`spill-encryption-enabled`**

**Description:** Enables the use of a randomly generated secret key (per spill file) to encrypt and decrypt data that is spilled to disk.<br>
**Type:** Boolean<br>
**Key:** CONF__config__spill-encryption-enabled<br>
**Default Value:** FALSE

### **Category: Exchange Properties**

#### **`exchange.client-threads`**

**Description:** This property determines the number of threads used by exchange clients to fetch data from other Trino nodes. Increasing the value can improve performance for large clusters or clusters with high concurrency. However, setting excessively high values may result in performance degradation due to context switches and increased memory usage.<br>
**Type:** Integer<br>
**Key:** CONF__config__exchange.client-threads<br>
**Default Value:** 25<br>
**Min Value:** 1

---

#### **`exchange.concurrent-request-multiplier`**

**Description:** This property determines the multiplier for the number of concurrent requests relative to the available buffer memory. The maximum number of requests is calculated based on the average buffer usage per request multiplied by this multiplier. The heuristic takes into account the available buffer space and aims to optimize concurrency and network utilization. Adjusting this value can increase concurrency and improve network utilization.<br>
**Type:** Integer<br>
**Key:** CONF__config__exchange.concurrent-request-multiplier<br>
**Default Value:** 3<br>
**Min Value:** 1

---

#### **`exchange.data-integrity-verification`**

**Description:** This property configures the behavior in case of data integrity issues. By default, when data integrity issues are detected during the built-in verification, queries are aborted (ABORT). Setting the property to NONE disables the verification, while setting it to RETRY repeats the data exchange when integrity issues are detected.<br>
**Type:** String<br>
**Key:** CONF__config__exchange.data-integrity-verification<br>
**Default Value:** ABORT<br>
**Allowed Values:** NONE, ABORT, RETRY

---

#### **`exchange.max-buffer-size`**

**Description:** This property defines the size of the buffer in the exchange client that holds data fetched from other nodes before it is processed. A larger buffer size can increase network throughput for larger clusters, thereby reducing query processing time. However, it also reduces the available memory for other purposes.<br>
**Type:** Data Size<br>
**Key:** CONF__config__exchange.max-buffer-size<br>
**Default Value:** 32MB

---

#### **`exchange.max-response-size`**

**Description:** This property sets the maximum size of a response returned from an exchange request. The response is stored in the exchange client buffer, which is shared across all concurrent requests for the exchange. Increasing this value can improve network throughput, especially when there is high latency. Decreasing the value can improve query performance for large clusters by reducing skew, as the exchange client buffer can hold responses for more tasks.<br>
**Type:** Data Size<br>
**Key:** CONF__config__exchange.max-response-size<br>
**Default Value:** 16MB<br>
**Min Value:** 1MB

---

#### **`sink.max-buffer-size`**

**Description:** This property determines the output buffer size for task data waiting to be pulled by upstream tasks. If the task output is hash partitioned, the buffer is shared among all partitioned consumers. Increasing this value can improve network throughput for data transferred between stages, particularly in cases of high network latency or when there are many nodes in the cluster.<br>
**Type:** Data Size<br>
**Key:** CONF__config__sink.max-buffer-size<br>
**Default Value:** 32MB

---

#### **`sink.max-broadcast-buffer-size`**

**Description:** This property specifies the broadcast output buffer size for task data waiting to be pulled by upstream tasks. The broadcast buffer is used to store and transfer build-side data for replicated joins. If the buffer size is too small, it can hinder the scaling of join probe side tasks when new nodes are added to the cluster.<br>
**Type:** Data Size<br>
**Key:** CONF__config__sink.max-broadcast-buffer-size<br>
**Default Value:** 200MB

---

### **Category: Task Properties**

#### **`task.concurrency`**

**Description:** This property defines the default local concurrency for parallel operators such as joins and aggregations. The value should be adjusted based on the query concurrency and worker resource utilization. Lower values are suitable for clusters that run many queries concurrently to avoid slowdowns due to context switching and overhead. Higher values are better for clusters that handle a smaller number of queries at a time. The `task_concurrency` session property allows specifying this value on a per-query basis.<br>
**Type:** Integer<br>
**Key:** CONF__config__task.concurrency<br>
**Default Value:** 16<br>
**Restrictions:** Must be a power of two.

---

#### **`task.http-response-threads`**

**Description:** This property sets the maximum number of threads that can handle HTTP responses. Threads are created on-demand and cleaned up when idle. Increasing this value can be beneficial for clusters with a high number of concurrent queries or a large number of workers.<br>
**Type:** Integer<br>
**Key:** CONF__config__task.http-response-threads<br>
**Default Value:** 100<br>
**Min Value:** 1

---

#### **`task.http-timeout-threads`**

**Description:** This property determines the number of threads used to handle timeouts when generating HTTP responses. If all threads are frequently in use, it may be necessary to increase this value. The thread utilization can be monitored through the `trino.server:name=AsyncHttpExecutionMBean:TimeoutExecutor` JMX object. If the `ActiveCount` is consistently the same as `PoolSize`, it indicates the need for more threads.<br>
**Type:** Integer<br>
**Key:** CONF__config__task.http-timeout-threads<br>
**Default Value:** 3<br>
**Min Value:** 1

---

#### **`task.info-update-interval`**

**Description:** This property controls the staleness of task information used in scheduling. Larger values reduce coordinator CPU load but may result in suboptimal split scheduling.<br>
**Type:** Duration<br>
**Key:** CONF__config__task.info-update-interval<br>
**Default Value:** 3s<br>
**Min Value:** 1ms<br>
**Max Value:** 10s

---

#### **`task.max-drivers-per-task`**

**Description:** This property limits the maximum number of drivers that can run concurrently within a task. Setting this value reduces the likelihood of a task using too many drivers and can improve concurrent query performance. However, setting it too low may result in underutilized resources.<br>
**Type:** Integer<br>
**Key:** CONF__config__task.max-drivers-per-task<br>
**Default Value:** 2147483647<br>
**Min Value:** 1

---

#### **`task.max-partial-aggregation-memory`**

**Description:** This property specifies the maximum size of partial aggregation results for distributed aggregations. Increasing this value can reduce network transfer and lower CPU utilization by allowing more groups to be kept locally before being flushed. However, it also increases memory usage.<br>
**Type:** Data Size<br>
**Key:** CONF__config__task.max-partial-aggregation-memory<br>
**Default Value:** 16MB

---

#### **`task.max-worker-threads`**

**Description:** This property determines the number of threads used by workers to process splits. Increasing this number can improve throughput if worker CPU utilization is low and all threads are in use. However, it also increases heap space usage. Setting the value too high may lead to a drop in performance due to context switching. The number of active threads can be monitored using the `RunningSplits` property of the `trino.execution.executor:name=TaskExecutor.RunningSplits` JMX object.<br>
**Type:** Integer<br>
**Key:** CONF__config__task.max-worker-threads<br>
**Default Value:** (Node CPUs * 2)

---

#### **`task.min-drivers`**

**Description:** This property represents the target number of running leaf splits on a worker. It acts as a minimum value because each leaf task is guaranteed to have at least 3 running splits. Non-leaf tasks are also ensured to run to prevent deadlocks. Adjusting this value can impact responsiveness for new tasks and resource utilization.<br>
**Type:** Integer<br>
**Key:** CONF__config__task.min-drivers<br>
**Default Value:** (task.max-worker-threads * 2)

---

#### **`task.min-drivers-per-task`**

**Description:** This property sets the minimum number of drivers guaranteed to run concurrently for a single task, assuming the task has remaining splits to process.<br>
**Type:** Integer<br>
**Key:** CONF__config__task.min-drivers-per-task<br>
**Default Value:** 3<br>
**Min Value:** 1

---

#### **`task.writer-count`**

**Description:** This property determines the number of concurrent writer threads per worker per query. Increasing this value can enhance write speed, particularly when a query is not I/O bound and can take advantage of additional CPU for parallel writes. However, some connectors may experience CPU bottlenecks during writing due to compression or other factors. Setting this value too high may overload the cluster with excessive resource utilization. The `task_writer_count` session property allows specifying this value on a per-query basis.<br>
**Type:** Integer<br>
**Key:** CONF__config__task.writer-count<br>
**Default Value:** 1<br>
**Restrictions:** Must be a power of two.


When defining environment variables explicitly, ensure that you set `overrideDefaultEnvs` to `false` to avoid accepting default configurations.

For more details, refer to the table of configuration properties.

## Connectors for Query Optimization

Minerva supports pushdown optimization, which involves pushing transformation logic to the source database. This optimization allows Minerva to delegate specific query operations or parts of operations to the connected data source, improving overall query performance.

Pushdown optimization includes the following types:

### **Predicate Pushdown**
Optimizes row-based filtering by passing the inferred filter (typically from a `WHERE` clause) to the underlying data source for processing.

### **Projection Pushdown**
Optimizes column-based filtering by limiting access to the columns specified in the `SELECT` clause and other parts of the query. Only the necessary columns are read and returned by the data source.

### **Aggregate Pushdown**
Improves performance for queries involving groupings and aggregations by delegating these operations to the underlying data source's index service.

### **Join Pushdown**
Allows Minerva to delegate table JOIN operations to the underlying data source, reducing the amount of data processed by Minerva for subsequent query processing.

### **Limit Pushdown**
Reduces the number of returned records by applying a `LIMIT` clause to the query. For unsorted records, the processing of these queries can be pushed down to the underlying data source, potentially improving performance. Similarly, if the query includes an `ORDER BY` clause, the data source can perform the sorting, returning the top rows to Minerva for further processing.

Implementing pushdown optimization results in various benefits, including improved query performance, reduced network traffic between Minerva and the data source, and cost savings. However, it's important to note that the availability of pushdown support depends on the specific connector and the underlying source system.


