# Configuration Properties

## Category: Memory Management Properties

### **`query.max-memory-per-node`**

<b>Description:</b> This property determines the maximum amount of user memory that a query can utilize on a worker. User memory is allocated during execution for components directly related to or controlled by the query, such as hash tables and sorting. If the user memory allocation of a query on any worker exceeds this limit, the query is terminated.<br>
<b>Type:</b> Data size<br>
<b>Key:</b>CONF__config__query.
max-memory-per-node<br>
<b>Requirement:</b> Optional<br>
<b>Default Value:</b> (JVM max memory * 0.3)<br>

### **`query.max-memory`**
<b>Description:</b> This property defines the maximum amount of user memory that a query can use across the entire cluster. User memory is allocated during execution for components directly related to or controlled by the query, such as hash tables and sorting. If the user memory allocation of a query across all workers exceeds this limit, the query is terminated. <br>
<b>Type:</b> Data size <br>
<b>Key:</b> CONF__config__query.max-memory <br>
<b>Default Value:</b> 20GB <br>

### `query.max-memory-per-task`
<b>Description:</b> This property specifies the maximum amount of memory that a task can use on a node in the cluster. Note that support for this property is experimental. <br>
<b>Type:</b> Data size <br>
<b>Key:</b> CONF__config__query.max-memory-per-task <br>
<b>Session Property:</b>query_max_total_memory_per_task<br>
<b>Default Value:</b> None (unrestricted) <br>


## memory.heap-headroom-per-node

- **Type:** Data size
- **DataOS Key:** CONF__config__memory.heap-headroom-per-node
- **Default Value:** (JVM max memory * 0.3)
- **Description:** This property reserves a portion of the JVM heap as headroom or buffer for memory allocations that are not tracked by Trino.

# Category: Query Management Properties

## query.execution-policy

- **Type:** String
- **DataOS Key:** CONF__config__query.execution-policy
- **Default Value:** Phased
- **Session Property:** execution_policy
- **Description:** This property configures the algorithm used to schedule the stages of a query. The available execution policies are as follows:

  - **Phased:** Stages are scheduled sequentially to avoid dependencies and maximize resource utilization, resulting in the lowest query wall time.
  - **All-at-once:** All stages of a query are scheduled simultaneously, leading to higher initial resource utilization but potentially longer queue times and higher query wait times due to inter-stage dependencies.
  - **Legacy-phased:** Similar to phased execution, but aims to minimize the number of running stages, potentially increasing query wall time.

## query.max-execution-time

- **Type:** Duration
- **DataOS Key:** CONF__config__query.max-execution-time
- **Default Value:** 100 days
- **Session Property:** query_max_execution_time
- **Description:** This property sets the maximum allowed execution time for a query on the cluster. It includes only the active execution time and excludes analysis, query planning, and queue wait times.

## query.max-planning-time

- **Type:** Duration
- **DataOS Key:** CONF__config__query.max-planning-time
- **Default Value:** 10 minutes
- **Session Property:** query_max_planning_time
- **Description:** This property defines the maximum allowed planning time for a query. If the planning time exceeds this limit, the coordinator attempts to stop the query. Note that certain planning operations may not be immediately cancellable.

## query.max-run-time

- **Type:** Duration
- **DataOS Key:** CONF__config__query.max-run-time
- **Default Value:** 100 days
- **Session Property:** query_max_run_time
- **Description:** This property specifies the maximum allowed total runtime for a query on the cluster. It includes analysis, planning, and queue wait times, providing the overall time allowed for a query to exist since its creation.

## query.max-stage-count

- **Type:** Integer
- **DataOS Key:** CONF__config__query.max-stage-count
- **Default Value:** 100
- **Min Value:** 1
- **Warning:** Setting a high value for this property can cause instability in the cluster, leading to unrelated queries being terminated with a REMOTE_TASK_ERROR due to exceeding the maximum requests queued per destination.
- **Description:** This property determines the maximum number of stages that can be generated per query. If a query exceeds this limit, it will be terminated with an error indicating that it has too many stages.

## query.max-history

- **Type:** Integer
- **DataOS Key:** CONF__config__query.max-history
- **Default Value:** 100
- **Description:** This property sets the maximum number of queries to retain in the query history for statistical and informational purposes. Once this limit is reached, older queries are removed based on their age.

## query.min-expire-age

- **Type:** Duration
- **DataOS Key:** CONF__config__query.min-expire-age
- **Default Value:** 15 minutes
- **Description:** This property specifies the minimum age of a query in the history before it is expired. Once expired, a query is removed from the query history buffer and is no longer accessible in the Web UI.

# Category: Spilling Properties

## spill-enabled

- **Type:** Boolean
- **DataOS Key:** CONF__config__spill-enabled
- **Default Value:** False
- **Description:** This property enables spilling of memory to disk to prevent exceeding memory limits for a query. Spilling works by offloading memory to disk, allowing queries with large memory footprints to continue at the cost of slower execution times. Spilling is supported for aggregations, joins (inner and outer), sorting, and window functions. The `spill_enabled` session property can override this configuration property.

## spiller-spill-path

- **Type:** String
- **DataOS Key:** CONF__config__spiller-spill-path
- **Default Value:** No default value (must be set when spilling is enabled)
- **Description:** This property specifies the directory where spilled content is written. Multiple directories can be specified as a comma-separated list to spill simultaneously to multiple locations, leveraging multiple drives in the system. It is important to avoid spilling to system drives or the drive used for JVM logs, as excessive disk utilization can cause JVM pauses and query failures.

## spiller-max-used-space-threshold

- **Type:** Double
- **DataOS Key:** CONF__config__spiller-max-used-space-threshold
- **Default Value:** 0.9
- **Description:** This property determines the maximum threshold for disk space usage in a spill path. If the disk space usage ratio of a spill path exceeds this threshold, the path is not eligible for spilling.

## spiller-threads

- **Type:** Integer
- **DataOS Key:** CONF__config__spiller-threads
- **Default Value:** 4
- **Description:** This property sets the number of spiller threads. Increasing this value may be necessary if the default number of threads cannot fully




# Category: Memory management properties

## query.max-memory-per-node

- **Type:** data size
- **DataOS Key:** CONF__config__query.max-memory-per-node
- **Default Value:** (JVM max memory * 0.3)
- **Description:** This property defines the max amount of user memory a query can use on a worker. User memory is allocated during execution for things that are directly attributable to or controllable by a user query. For example, memory used by the hash tables built during execution, memory used during sorting, etc. The query is killed when the user memory allocation of a query on any worker hits this limit.

## query.max-memory

- **Type:** data size
- **DataOS Key:** CONF__config__query.max-memory
- **Default Value:** 20GB
- **Description:** This property defines the max amount of user memory a query can use across the entire cluster. User memory is allocated during execution for things that are directly attributable to or controllable by a user query. For example, memory used by the hash tables built during execution, memory used during sorting, etc. The query is killed when the user memory allocation of a query across all workers hits this limit.

## query.max-memory-per-task

- **Type:** data size
- **DataOS Key:** CONF__config__query.max-memory-per-task
- **Default Value:** none, and therefore unrestricted
- **Session Property:** query_max_total_memory_per_task
- **Description:** This is the max amount of memory a task can use on a node in the cluster. Support for using this property is experimental only.

## memory.heap-headroom-per-node

- **Type:** data size
- **DataOS Key:** CONF__config__memory.heap-headroom-per-node
- **Default Value:** (JVM max memory * 0.3)
- **Description:** This is the amount of memory set aside as headroom/buffer in the JVM heap for allocations that Trino does not track.

# Category: Query management properties

## query.execution-policy

- **Type:** string
- **DataOS Key:** CONF__config__query.execution-policy
- **Default Value:** phased
- **Session Property:** execution_policy
- **Description:** This configures the algorithm to organize the processing of all of the stages of a query. You can use the following execution policies:

**phased:** schedules stages in a sequence to avoid blockages because of inter-stage dependencies. This policy maximizes cluster resource utilization and provides the lowest query wall time.

**all-at-once:** schedules all of the stages of a query at one time. As a result, cluster resource utilization is initially high, but inter-stage dependencies typically prevent complete processing and cause longer queue times, increasing the query wait time overall.

**legacy-phased:** has similar functionality to phased but can increase the query wall time as it attempts to minimize the number of running stages.

## query.max-execution-time

- **Type:** duration
- **DataOS Key:** CONF__config__query.max-execution-time
- **Default Value:** 100d
- **Session Property:** query_max_execution_time
- **Description:** The maximum allowed time for a query to be actively executing on the cluster before it is terminated. Compared to the run time below, execution time does not include analysis, query planning, or wait times in a queue

## query.max-planning-time

- **Type:** duration
- **DataOS Key:** CONF__config__query.max-planning-time
- **Default Value:** 10m
- **Session Property:** query_max_planning_time
- **Description:** This property sets the maximum allowed time for a query to be actively planning the execution. After this period, the coordinator will try to stop the query. Note that some operations in the planning phase are not easily cancellable and may not terminate immediately.

## query.max-run-time

- **Type:** duration
- **DataOS Key:** CONF__config__query.max-run-time
- **Default Value:** 100d
- **Session Property:** query_max_run_time
- **Description:** This property defines **t**he maximum allowed time for a query to be processed on the cluster before it is terminated. The time includes time for analysis and planning and time spent in a queue waiting, so essentially this is the time allowed for a query to exist since creation.

## query.max-stage-count

- **Type:** integer
- **DataOS Key:** CONF__config__query.max-stage-count
- **Default Value:** 100
- **Min Value:** 1
- **Warning:** Setting this to a high value can cause queries with large number of stages to introduce instability in the cluster causing unrelated queries to get killed with REMOTE_TASK_ERROR and the message Max requests queued per destination exceeded for HttpDestination ...
- **Description:** The maximum number of stages allowed to be generated per query. If a query generates more stages than this value, it will get killed with error QUERY_HAS_TOO_MANY_STAGES.

## query.max-history

- **Type: integer**
- DataOS Key: CONF__config__query.max-history
- Default Value: 100
- Description: The maximum number of queries to keep in the query history to provide statistics and other information. If this amount is reached, queries are removed based on age.

## query.min-expire-age

- **Type:** duration
- **DataOS Key:** CONF__config__query.min-expire-age
- **Default Value:** 15m
- **Description:** The minimal age of a query in the history before it is expired. An expired query is removed from the query history buffer and is no longer available in the Web UI.

# Category: Spilling properties

## spill-enabled

- **Type:** boolean
- **DataOS Key:** CONF__config__spill-enabled
- **Default Value:** FALSE
- **Description:** This is to enable spilling memory to disk to avoid exceeding memory limits for the query. Spilling works by offloading memory to disk. This process can allow a query with a large memory footprint to pass at the cost of slower execution times. Spilling is supported for aggregations, joins (inner and outer), sorting, and window functions. This property does not reduce the memory usage required for other join types. The spill_enabled session property can override this config property.

## spiller-spill-path

- **Type:** string
- **DataOS Key:** CONF__config__spiller-spill-path
- **Default Value:** No default value. Must be set when spilling is enabled
- **Description:** This is the directory where spilled content is written. It can be a comma-separated list to spill simultaneously to multiple directories, which helps to utilize multiple drives installed in the system. It is not recommended to spill to system drives. Most importantly, do not spill to the drive on which the JVM logs are written, as disk overutilization might cause JVM to pause for lengthy periods, causing queries to fail.

## spiller-max-used-space-threshold

- **Type:** double
- **DataOS Key:** CONF__config__Property
- **Default Value:** 0.9
- **Description:** If a given spill path's disk space usage ratio is above this threshold, this spill path is not eligible for spilling.

## spiller-threads

- **Type:** integer
- **DataOS Key:** CONF__config__spiller-threads
- **Default Value:** 4
- **Description:** This property defines the number of spiller threads. Increase this value if the default cannot saturate the underlying spilling device (for example, when using RAID).

## max-spill-per-nod

- **Type:** data size
- **DataOS Key:** CONF__config__max-spill-per-nod
- **Default Value:** 100GB
- **Description:** Max spill space to be used by all queries on a single node.

## query-max-spill-per-node

- **Type:** data size
- **DataOS Key:** CONF__config__query-max-spill-per-node
- **Default Value:** 100GB
- **Description:** This is max spill space to be used by a single query on a single node.

## aggregation-operator-unspill-memory-limit

- **Type:** data size
- **DataOS Key:** CONF__config__aggregation-operator-unspill-memory-limit
- **Default Value:** 4MB
- **Description:** This defines the **l**imit for memory used for unspilling a single aggregation operator instance.

## spill-compression-enabled

- **Type:** boolean
- **DataOS Key:** CONF__config__spill-compression-enabled
- **Default Value:** FALSE
- **Description:** Enables data compression for pages spilled to disk.

## spill-encryption-enabled

- **Type:** boolean
- **DataOS Key:** CONF__config__spill-encryption-enabled
- **Default Value:** FALSE
- **Description:** Enables using a randomly generated secret key (per spill file) to encrypt and decrypt data spilled to disk.

# Category: Exchange properties

## exchange.client-threads

- **Type:** integer
- **DataOS Key:** CONF__config__exchange.client-threads
- **Default Value:** 25
- **Min Value:** 1
- **Description:** This defines the number of threads used by exchange clients to fetch data from other Trino nodes. A higher value can improve performance for large clusters or clusters with very high concurrency, but excessively high values may cause a drop in performance due to context switches and additional memory usage.

## exchange.concurrent-request-multiplier

- **Type:** integer
- **DataOS Key:** CONF__config__exchange.concurrent-request-multiplier
- **Default Value:** 3
- **Min Value:** 1
- **Description:** Multiplier determining the number of concurrent requests relative to the available buffer memory. The maximum number of requests is determined using a heuristic of the number of clients that can fit into available buffer space, based on average buffer usage per request times this multiplier. For example, with an exchange.max-buffer-size of 32 MB and 20 MB already used and average size per request being 2MB, the maximum number of clients is multiplier * ((32MB - 20MB) / 2MB) = multiplier * 6. Tuning this value adjusts the heuristic, which may increase concurrency and improve network utilization.

## exchange.data-integrity-verification

- **Type:** string
- **DataOS Key:** CONF__config__exchange.data-integrity-verification
- **Default Value:** ABORT
- **Allowed values**: NONE, ABORT, RETRY
- **Description:**  This configures the resulting behavior of data integrity issues. By default, ABORT causes queries to be aborted when data integrity issues are detected as part of the built-in verification. Setting the property to NONE disables the verification. RETRY causes the data exchange to be repeated when integrity issues are detected.

## exchange.max-buffer-size

- **Type:** data size
- **DataOS Key:** CONF__config__exchange.max-buffer-size
- **Default Value:** 32MB
- **Description:** This defines the size of buffer in the exchange client that holds data fetched from other nodes before it is processed. A larger buffer can increase network throughput for larger clusters, and thus decrease query processing time, but reduces the amount of memory available for other usages.

## exchange.max-response-size

- **Type:** data size
- **DataOS Key:** CONF__config__exchange.max-response-size
- **Default Value:** 16MB
- **Min Value:** 1MB
- **Description:** This is the maximum size of a response returned from an exchange request. The response is placed in the exchange client buffer, which is shared across all concurrent requests for the exchange. Increasing the value may improve network throughput, if there is high latency. Decreasing the value may improve query performance for large clusters as it reduces skew, due to the exchange client buffer holding responses for more tasks, rather than hold more data from fewer tasks.

## sink.max-buffer-size

- **Type:** data size
- **DataOS Key:** CONF__config__sink.max-buffer-size
- **Default Value:** 32MB
- **Description:** This is the output buffer size for task data that is waiting to be pulled by upstream tasks. If the task output is hash partitioned, then the buffer is shared across all of the partitioned consumers. Increasing this value may improve network throughput for data transferred between stages, if the network has high latency, or if there are many nodes in the cluster.

## sink.max-broadcast-buffer-size

- **Type:** data size
- **DataOS Key:** CONF__config__sink.max-broadcast-buffer-size
- **Default Value:** 200MB
- **Description: This defines the b**roadcast output buffer size for task data that is waiting to be pulled by upstream tasks. The broadcast buffer is used to store and transfer build-side data for replicated joins. If the buffer is too small, it prevents scaling of join probe side tasks, when new nodes are added to the cluster.

# Category: Task properties

## task.concurrency

- **Type:** integer
- **DataOS Key:** CONF__config__task.concurrency
- **Default Value:** 16
- **Restrictions:** Must be a power of two.
- **Description:** This defines the default local concurrency for parallel operators, such as joins and aggregations. This value should be adjusted up or down based on the query concurrency and worker resource utilization. Lower values are better for clusters that run many queries concurrently because the cluster is already utilized by all the running queries, so adding more concurrency results in slowdowns due to context switching and other overhead. Higher values are better for clusters that only run one or a few queries at a time. This can also be specified on a per-query basis using the task_concurrency session property.

## task.http-response-threads

- **Type:** integer
- **DataOS Key:** CONF__config__task.http-response-threads
- **Default Value:** 100
- **Min Value:** 1
- **Description:** This property defines the maximum number of threads that may be created to handle HTTP responses. Threads are created on-demand and are cleaned up when idle, thus there is no overhead to a large value if the number of requests to be handled is small. More threads may be helpful on clusters with a high number of concurrent queries, or on clusters with hundreds or thousands of workers.

## task.http-timeout-threads

- **Type:** integer
- **DataOS Key:** CONF__config__task.http-timeout-threads
- **Default Value:** 3
- **Min Value:** 1
- **Description:** This property defines the number of threads used to handle timeouts when generating HTTP responses. This value should be increased if all the threads are frequently in use. This can be monitored via the trino.server:name=AsyncHttpExecutionMBean:TimeoutExecutor JMX object. If ActiveCount is always the same as PoolSize, increase the number of threads.

## task.info-update-interval

- **Type:** duration
- **DataOS Key:** CONF__config__task.info-update-interval
- **Default Value:** 3s
- **Min Value:** 1ms
- **Max Value:** 10s
- **Description:** This property controls the staleness of task information, which is used in scheduling. Larger values can reduce coordinator CPU load, but may result in suboptimal split scheduling.

## task.max-drivers-per-task

- **Type:** integer
- **DataOS Key:** CONF__config__task.max-drivers-per-task
- **Default Value:** 2147483647
- **Min Value:** 1
- **Description:** This property controls the maximum number of drivers a task runs concurrently. Setting this value reduces the likelihood that a task uses too many drivers and can improve concurrent query performance. This can lead to resource waste if it runs too few concurrent queries.

## task.max-partial-aggregation-memory

- **Type:** data size
- **DataOS Key:** CONF__config__task.max-partial-aggregation-memory
- **Default Value:** 16MB
- **Description:** Maximum size of partial aggregation results for distributed aggregations. Increasing this value can result in less network transfer and lower CPU utilization, by allowing more groups to be kept locally before being flushed, at the cost of additional memory usage.

## task.max-worker-threads

- **Type:** integer
- **DataOS Key:** CONF__config__task.max-worker-threads
- **Default Value:** (Node CPUs * 2)
- **Description:** This sets the number of threads used by workers to process splits. Increasing this number can improve throughput if worker CPU utilization is low and all the threads are in use, but it causes increased heap space usage. Setting the value too high may cause a drop in performance due to context switching. The number of active threads is available via the RunningSplits property of the trino.execution.executor:name=TaskExecutor.RunningSplits JMX object.

## task.min-drivers

- **Type:** integer
- **DataOS Key:** CONF__config__task.min-drivers
- **Default Value:** (task.max-worker-threads * 2)
- **Description:** This defines the target number of running leaf splits on a worker. This is a minimum value because each leaf task is guaranteed at least 3 running splits. Non-leaf tasks are also guaranteed to run in order to prevent deadlocks. A lower value may improve responsiveness for new tasks but can result in underutilized resources. A higher value can increase resource utilization but uses additional memory.

## task.min-drivers-per-task

- **Type:** integer
- **DataOS Key:** CONF__config__task.min-drivers-per-task
- **Default Value:** 3
- **Min Value:** 1
- **Description:** This is the minimum number of drivers guaranteed to run concurrently for a single task given the task has remaining splits to process.

## task.writer-count

- **Type:** integer
- **DataOS Key:** CONF__config__task.writer-count
- **Default Value:** 1
- **Restrictions**: Must be a power of two.
- **Description:** This describes the number of concurrent writer threads per worker per query. Increasing this value may increase write speed, especially when a query is not I/O bound and can take advantage of additional CPU for parallel writes. Some connectors can be bottlenecked on the CPU when writing due to compression or other factors. Setting this too high may cause the cluster to become overloaded due to excessive resource utilization. This can also be specified on a per-query basis using the task_writer_count session property.