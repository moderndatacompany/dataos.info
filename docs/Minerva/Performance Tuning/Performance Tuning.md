# Performance Tuning

Minerva query engine is designed to query large data sets distributed over heterogeneous data sources. It can take time to execute when you run complex queries with big data on Minerva. 

Here are some of the considerations which can help you accelerate your queries on Minerva.

## Cluster sizing

This section contains recommendations for hardware for your cluster nodes. It also provides information that helps you appropriately size the hardware components to meet the needs of your environment.

Minerva clusters have a single driver (coordinator) node and multiple worker nodes. The coordinator analyzes and plans query execution and then distributes the query plan among worker machines for processing in the cluster. A driver node runs the main function and executes various parallel operations on the worker nodes. The worker nodes read data using connectors specific to your data sources, such as Snowflake, Postgres, and Oracle to transform queries and return data.

The driver and worker nodes can have different instance types, but Minerva supports the same configurations by default for all the worker nodes.  Minerva has static clusters, so, it does not allow clusters to resize automatically based on workloads.

Minerva uses parallel processing and pipelined execution across nodes in the cluster.  Minerva is designed in such a way that it uses all available resources, Memory, CPU, and network allocated. Its multithreaded execution model keeps all the CPU cores busy. You also need to manage your user and query concurrency needs as they may change during peak and off-hours.

CPU time, memory requirements, and network bandwidth usage are the three dimensions that contribute to query execution time, both in single-query and concurrent workloads. More CPUs will result in shorter queries. Memory is needed to perform joins, group by, order by operations for your queries. These dimensions constitute the cost in Minerva.

- CPU
- Memory
- Network

Consider these factors when sizing your cluster:

- Data Volume
- Data Growth

## Small clusters vs big clusters

Decide on an initial size, based on rough estimates and available infrastructure. You can then monitor utilization and performance. 

The general strategy is to create a big cluster bigger than what you require. You need to ensure first that everything is running and stable.  In the small cluster, the workload can easily exceed cluster limits for the resources( CPU, memory, network) and will result either in query failure or long waiting. A single big query on a small cluster can cause queuing and can feel unreliable when long response time for the results.

<span style="color:maroon">Can we provide some examples here to quickly know how much cluster size is required for the particular use case?</span>

## Machine default settings

Ensure that default machine settings are sufficiently large enough to support the expected cluster configurations for the desired workloads.

- Managing Memory - You must know that some memory is required by the operating system for its processes such as kernel and disk and network buffers etc.
- JVM- You need to tune your virtual machine options.
    
    The following can be helpful for diagnosing GC issues:
    
    ```yaml
    -XX:+PrintGCApplicationConcurrentTime
    -XX:+PrintGCApplicationStoppedTime
    -XX:+PrintGCCause
    -XX:+PrintGCDateStamps
    -XX:+PrintGCTimeStamps
    -XX:+PrintGCDetails
    -XX:+PrintReferenceGC
    -XX:+PrintClassHistogramAfterFullGC
    -XX:+PrintClassHistogramBeforeFullGC
    -XX:PrintFLSStatistics=2
    -XX:+PrintAdaptiveSizePolicy
    -XX:+PrintSafepointStatistics
    -XX:PrintSafepointStatisticsCount=1
    ```
    
- Java heap configuration - Keep a provision of memory requirement for OS processes as well as JVM processes such as garbage collection, and thread management, then allocate memory to the Java heap. Which will be used for query processing.

### Recommendations

1. Keep approximately 20 % for OS overhead, and allocate 80% to the Java heap. From the allocated Java heap, approximately 70% is for query memory.

    For Example:

    128 GB machine => 100 Gb JVM Heap => 70 GB Minerva Query Memory

1. Use bigger machines. Having fewer bigger machines is better than more smaller machines as there will be less memory overhead per machine. And also there will be less coordination work.
2. Disable OS spilling (JVM is not designed for spilling). Rather scale-up cluster size for bigger queries. Spilling causes queuing as disks are slow.
3. Disable the “runaway” process detector as Minerva uses all available resources. 

# Workload Tuning

Develop an understanding of your total workload. Different use cases need different instances. You need to know the following to reduce the number of errors caused by timeouts and insufficient resources–

- What queries are run: memory intensive or compute-intensive?
- What is the expected latency?
- What is the expected consistency?
- Concurrency: The number of concurrently running queries. The higher the concurrency, the more core memory you need.
- The amount of data on which the average query will operate.
- What are the Peak loads (CPU and Memory requirements)?

## Recommendations

1. In a high-concurrency or heavy-workload environment, oversize your cluster to achieve better performance.
2. You also need to observe the performance for different query loads and fine-tune the configuration. To learn more, refer to the examples.

# Storage Formats

While addressing the infrastructure is an important step to speed up query execution, it’s not the only step. You need to make the storage more performant. For storage performance, there are two factors to consider- latency and throughput.  Latency is the time it takes to get the data to the end-user and throughput is the amount of data the query is reading over time.

File format, size, compression, and organization can significantly improve your Minerva query performance. 

> 💡 Icebase, DataOS’s lakehouse implementation, allows users to store structured, unstructured, and streaming data in scalable object storage Iceberg format.

## Recommendations

1. Use columnar formats  that store data efficiently

    Minerva processes the data as vectorized columns. This means that it only holds the amount of data it processes without carrying around the additional fields that are not relevant to the query in the process. Moreover, columnar data usually compresses better since each column can be compressed separately. Icebase stores data in Parquet format, optimized for fast data retrieval.

1. Watch your file size 

    The file size is a big deal in query processing. Small files create many small IO requests that impact performance (high latency, getting throttled, or running out of IO capacity). Each file requires separate handling, which increases the scheduling time and cost. So, use file sizes of at least 100MB to overcome potential IO issues. DataOS enables you to merge and compact data/metadata files in its Icebase data storage.

    To learn more, refer to this [*use case*](/mkdocs/Mk%20Docs/Transformation/Flare/Building%20Blocks%20of%20Flare%20Workflow/Actions.md). 

1. Compress your data

    Additionally, always consider compressing your data for better performance.  Icebase stores data in Apache Parquet format which compresses the data by default.

1. Partition  your data

    Partitioning divides your table into parts and keeps the related data together based on column values such as date, vendor id, and product id. The partitions are defined at the time of table creation, and they help reduce the amount of data scanned for queries with predicates over the partitioned column, thereby improving performance. 

    To learn, refer to this [*use case*](../../Transformation/Flare/Case%20Scenario/Partitioning.md).

1. Sort your data

    Additionally, sorting your data also helps narrow the range of partitions that need to be read by Minerva. We can efficiently skip irrelevant chunks if we sort each file, but only if we filter over the sorted column.

## Configuration Properties

When setting up a cluster for a specific workload, it may be necessary to adjust the Minerva configuration properties to ensure optimal performance. DataOS enables you to set these configuration properties to tune or alter their behavior when required.  Minerva includes many configuration options for the coordinator and worker, such as memory and CPU limits for queries for optimized execution.

The following Minerva cluster YAML shows how you define these properties for Coordinator and Worker nodes under the Env section:

```yaml
cluster:
  compute: query-default 
  runAsUser:  
  minerva: 
    selector:
      users:
        - ""
      sources:
        - ""
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

> *Note:*  While defining environment variables explicitly, make sure to set overrideDefaultEnvs to false otherwise default configurations will be accepted.
> 

To understand more, refer to the table of
[Configuration Properties](Performance%20Tuning/Configuration%20Properties.md).

## Connectors to participate in Query Optimization

When pushdown optimization is applied, transformation logic is pushed to the source database. 

Minerva can push down the processing of queries, or parts of queries for transformation logic, to the connected data source. This means that a specific filter operation such as predicate or aggregation & grouping operation is passed through to the underlying database or storage system for processing.  

Each of the following rules would be responsible for pushing down the corresponding type of operation into the table scan. 

## Predicate pushdown

Predicate pushdown optimizes row-based filtering. It uses the inferred filter, typically resulting from a condition in a `WHERE` clause to omit unnecessary rows. The processing is pushed down to the data source by the connector and then processed by the data source.

## Projection pushdown

Projection pushdown optimizes column-based filtering. It uses the columns specified in the `SELECT` clause and other parts of the query to limit access to these columns. The processing is pushed down to the data source by the connector and then the data source only reads and returns the necessary columns.

## Aggregate pushdown

Aggregate pushdown improves the performance of queries with groupings and aggregations not performed by the query engine, instead, the query intelligently requests the underlying data source’s index service to perform grouping and aggregation.

## Join pushdown

Join pushdown allows the connector to delegate the table `JOIN` operation to the underlying data source. This will allow Minerva to perform the remaining query processing on a smaller set of data.

## Limit pushdown

A `LIMIT` clause in the query reduces the number of returned records. Query performance can be improved by pushing the processing of such queries of unsorted records to the underlying data source. Similarly, if the query is containing the ‘Order By’ clause, the sorting of the result data can be performed on the data source level, and the top rows are returned to Minerva for further processing.

<u>Performance Advantage:</u>

The results of pushdown can include the following benefits:

- Improved overall query performance
- Reduced network traffic between Minerva and the data source
- Significant cost reduction

> Note: Please note that this support for pushdown is specific to each connector and the relevant underlying database or storage system. Read about [Depot](../../Integration%20&%20Ingestion/Depot.md) to get the list of data sources that provide PushBack support.
> 

To know more about the supported connectors, refer to [Minerva](../Minerva.md).