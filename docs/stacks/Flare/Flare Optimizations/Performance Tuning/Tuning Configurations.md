# **Tuning Configurations**

# **Use Serialized data formats**

> **Beneficial Scenario:**  If your job performance is low and you are using CSV, JSON, or Text input files.
> 

Most of the Spark jobs run as a pipeline where one Spark job writes data into a File and another Spark job read the data, processes it, and writes it to another file for another Spark job to pick up. 

When you have such a use case, prefer writing an intermediate file in serialized and optimized formats like Avro, Parquet, etc, any transformations on these formats perform better than text, CSV, and JSON.  

> 🗣️ The combination of **Parquet** along with **snappy** compression gives very high performance.

# **Serialization**

> **Beneficial Scenario:** When transferring data over the network or writing to disk, you experience slower access speed.
> 

An object is serialized and deserialized during network transfer, writing to disk, etc. It plays a distinctive role in the performance of any distributed application as storing data in serialized form is slower to access, due to having to deserialize each object on the fly. 

> 🗣️ The Kryo Serializer is highly recommended if you want to cache data in serialized form, as it leads to much smaller sizes than Java serialization.


**Configuration Property**

| Property | Description | Default | Recommended |
| --- | --- | --- | --- |
| `spark.serializer` | Data Serialization Format | org.apache.spark.serializer.JavaSerializer | org.apache.spark.serializer.KryoSerializer | Often, this will be the first thing you should tune to optimize your Flare job. 

# **Memory Management and Tuning**

> **Beneficial Errors:** When you encounter Out of Space Errors during execution
> 

For computations such as shuffling, sorting, and so on, **Execution memory** is used whereas for caching purposes **storage memory** is used that also propagates internal data. Cached jobs always apply less storage space where the data is not allowed to be evicted by any execution requirement. **Configuration Properties**

<img src="Tuning%20Configurations/Untitled.png"
        alt="Diagrammatic representation of Memory allocation within Spark"
        style="display: block; margin: auto" />

<figcaption align = "center">Diagrammatic representation of Memory allocation within Spark</figcaption>
<br>

Although there are two relevant configurations, the typical user should not need to adjust them as the default values are applicable to most workloads:

| Property | Description | Default | Recommended |
| --- | --- | --- | --- |
| `spark.memory.fraction` | Amount of JVM Heap Space used for Spark Execution Memory *Unified Space (M)* / *JVM Heap Space {300 MiB}* | 0.6 | Executor memory must be kept as less as possible because it may lead to a delay in JVM Garbage collection. This fact is also applicable for small executors as multiple tasks may run on a single JVM instance. |
| `spark.memory.storageFraction` | Represents the size of storage space R where cached blocks are immune to eviction. *Storage Space (R)* / *Unified Space (M)* | 0.5 | The higher the value higher the cache blocks will be immune to eviction and the lesser the space for execution. |

# **Cost Based Optimizer**

> **Beneficial Scenario:** While working with multiple joins
> 

When working with Multiple joins, Cost Based Optimizer improves the query plan on the table and column statistics.

**Configuration Property**

This is enabled by default but if it’s disabled, you can enable it using the following property

| Property | Description | Default | Recommended |
| --- | --- | --- | --- |
| `spark.sql.cbo.enabled` | Enables Cost Based Optimizer | true | true (if its false set to true) |

> 🗣️ Prior to the Join query, run `ANALYZE TABLE` command by mentioning all columns you are joining. This command collects the statistics for tables and columns for a cost-based optimizer to find out the best query plan. 

**Syntax of `ANALYZE TABLE` Command** 

```sql
ANALYZE TABLE table_name [ PARTITION ( partition_col_name [ = partition_col_val ] [ , ... ] ) ]
    COMPUTE STATISTICS [ NOSCAN | FOR COLUMNS col [ , ... ] | FOR ALL COLUMNS ]
```

# **Enable Adaptive Query Execution**

> **Beneficial Scenario:** In cases where you suffer performance problems due to miscalculations in manual query plans due to an increased amount of data.
> 

Adaptive Query Execution is a feature that improves the query performance by re-optimizing the query plan during runtime with the statistics it collects after each stage completion. 

At runtime, the adaptive execution mode can change shuffle join to broadcast join if it finds the size of one table is less than the broadcast threshold. It can also handle skewed input data for join and change the partition number of the next stage to better fit the data scale. 

In general, adaptive execution decreases the effort involved in tuning SQL query parameters and improves the execution performance by choosing a better execution plan and parallelism at runtime.

There are three major features in AQE: coalescing post-shuffle partitions, converting sort-merge join to broadcast join, and skew join optimization.

**Configuration Properties**

| Property | Description | Default Value | Set Value |
| --- | --- | --- | --- |
| `spark.sql.adaptive.enabled` | Enables Adaptive Query Execution | false | true |

## **Converting sort-merge join to broadcast join**

> **Beneficial Scenario:** When one of your joins tables is small enough to fit in memory within the broadcast threshold.
> 

AQE converts sort-merge join to broadcast hash join when the runtime statistics of any join side is smaller than the adaptive broadcast hash join threshold. This is not as efficient as planning a broadcast hash join in the first place, but it’s better than keep doing the sort-merge join, as we can save the sorting of both the join sides, and read shuffle files locally to save network traffic (if `spark.sql.adaptive.localShuffleReader.enabled` is true)

**Configuration Property**

| Property | Description | Default Value  | Recommended Value |
| --- | --- | --- | --- |
| `spark.sql.autoBroadcastJoinThreshold` | Configures the maximum size in bytes for a table that will be broadcast to all worker nodes when performing a join. By setting this value to -1 broadcasting can be disabled. The default value is same with spark.sql.autoBroadcastJoinThreshold. Note that, this config is used only in adaptive framework. | (none) | Increase the broadcast threshold size if your table is big. |

## **Coalescing Post-Shuffle Partitions**

> **Beneficial Scenario:** When you don’t know the exact number of shuffle partitions to be done
> 

After every stage of the job, Spark dynamically determines the optimal number of partitions by looking at the metrics of the completed stage. 

This feature coalesces the post-shuffle partitions based on the map output statistics when both and `spark.sql.adaptive.coalescePartitions.enabled` configurations are true. This feature simplifies the tuning of shuffle partition numbers when running queries. You do not need to set a proper shuffle partition number to fit your dataset. Spark can pick the proper shuffle partition number at runtime once you set a large enough initial number of shuffle partitions via `spark.sql.adaptive.coalescePartitions.initialPartitionNum` configuration.

**Configuration Property**

| Property | Description | Default Value  | Recommended Value |
| --- | --- | --- | --- |
| `spark.sql.adaptive.enabled` | Enables Adaptive Query Execution | true | true |
| `spark.sql.adaptive.coalescePartitions.enabled`  | When true and  `spark.sql.adaptive.enabled` is true, Spark will coalesce contiguous shuffle partitions according to the target size (specified by `spark.sql.adaptive.advisoryPartitionSizeInBytes`), to avoid too many small tasks. | true | true |
| `spark.sql.adaptive.coalescePartitions.initialPartitionNum` | The initial number of shuffle partitions before coalescing. If not set, it equals to spark.sql.shuffle.partitions. This configuration only has an effect when `spark.sql.adaptive.enabled` and `spark.sql.adaptive.coalescePartitions.enabled` are both enabled. | (none) | This number should be relatively higher |
| `spark.sql.adaptive.advisoryPartitionSizeInBytes` | The advisory size in bytes of the shuffle partition during adaptive optimization (when `spark.sql.adaptive.enabled` is true). It takes effect when Spark coalesces small shuffle partitions or splits skewed shuffle partition. | 64 MB |  |

## ****Converting sort-merge join to shuffled hash join****

> **Beneficial Scenario: W**hen projections of the joined tables are not already sorted on the join columns
> 

AQE converts sort-merge join to shuffled hash join when all post-shuffle partitions are smaller than a threshold.

**Configuration Property**

To enable sort-merge to shuffle hash join, configure the below two properties with the set value

| Property Name | Description | Default  | Set Value |
| --- | --- | --- | --- |
| `spark.sql.adaptive.enabled`  | Enables Adaptive Query Execution | (none) | true |
| `spark.sql.adaptive.maxShuffledHashJoinLocalMapThreshold` | Configures the maximum size in bytes per partition that can be allowed to build a local hash map. If this value is not smaller than `spark.sql.adaptive.advisoryPartitionSizeInBytes` and all the partition size are not larger than this config, join selection prefer to use shuffled hash join instead of sort-merge join regardless of the value of `spark.sql.join.preferSortMergeJoin`. | 0 |  |

## **Optimizing Skew Join**

> **Beneficial Scenario:** When there is Data Skew
> 

When data in partitions is not evenly distributed, it's called Data Skew. Operations such as join perform very slowly on these partitions. By enabling Adaptive Query Execution (AQE), Spark checks the stage statistics and determines if there are any Skew joins, and optimizes it by splitting the bigger partitions into smaller (matching partition size on another table/dataframe)

**Configuration Properties**

To enable skew join optimization enable the below two properties

| Property Name | Description | Default  | Recommended |
| --- | --- | --- | --- |
| `spark.sql.adaptive.enabled`  | Enables Adaptive Query Execution | (none) | true |
| `spark.sql.adaptive.skewJoin.enabled` | When true and `spark.sql.adaptive.enabled` is true, Spark dynamically handles skew in sort-merge join by splitting (and replicating if needed) skewed partitions. | (none) | true |

# **Level of Parallelism**

> **Beneficial Scenario:** When your job performance is low due to improper cluster utilization. Though it can be used to increase performance in general too.
> 

An increase in parallelism can considerably increase performance. Every partition or task requires a single core for processing. Clusters will not be fully utilized unless you set the level of parallelism for each operation high enough.  

**Configuration Property**

You can use the below parameter to change the default value type

| Property | Description | Default | Recommended |
| --- | --- | --- | --- |
| `spark.default.parallelism` | The default value for this configuration is set to the number of all cores on all nodes in a cluster, on local, it is set to the number of cores on your system. | Integer (Number of cores in cluster, on local, it is set to the number of cores on your system) | 2-3 tasks per CPU core in cluster |

# **Garbage Collection Tuning**

> **Beneficial Scenario:** When you have a large collection of unused objects resulting in a long-running job process and decreased performance time.
> 

To make room for new objects, old objects are evicted, which requires the need to trace through all Java objects and find unused ones. The main point to remember here is that the cost of garbage collection (GC) is proportional to the number of Java objects. 

**Measuring the Impact of Garbage Collection**

The first step in Garbage Collection tuning is to collect statistics on how frequently garbage collection occurs and the amount of time spent GC. 

This can be done by adding `-verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps`
 to the Java options. 

**Configuration Property**

```yaml
sparkConf:
    - spark.executor.extraJavaOptions: 
        -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps
```

Next time your Spark job is run, you will see messages printed in the worker’s logs each time a garbage collection occur

> 🗣️ In an ideal situation we try to keep GC overheads < 10% of heap memory.


**Ways to reduce garbage collection cost**

- Use data structures with fewer objects (e.g. an array of `Int`s instead of a `LinkedList`) greatly lowers this cost.
- An even better method is to persist objects in serialized form.

# **Caching Optimizations**

## **Use Columnar Formats for Caching**

When you cache data from Dataframe/SQL, use the in-memory columnar format. When you perform Dataframe/SQL operations on columns, Spark retrieves only the required columns which result in less data retrieval and less memory usage.

**Configuration Properties**

| Property Name | Description | Default Value | Recommended Value |
| --- | --- | --- | --- |
| `spark.sql.inMemoryColumnarStorage.compressed` | When set to true Spark SQL will automatically select a compression codec for each column based on statistics of the data. | false | true |

## **Tune the batchSize while Caching**

By Tuning the batchSize property you can improve Spark Performance

**Configuration Property**

| Property | Description | Default Value | Recommended Value |
| --- | --- | --- | --- |
| `spark.sql.inMemoryColumnarStorage.batchSize` | Controls the size of batches for columnar caching.  | 10000 | Larger batch sizes can improve memory utilization and compression, but risk OOMs when caching data. |

# **Optimal Value of Shuffle Partitions**

> **Beneficial Scenario:** While performing operations that trigger data shuffle (like Aggregate and Joins)
> 

Shuffling is a mechanism Spark uses to redistribute data across different executors and even across machines. Spark Shuffle is an expensive operation since it involves Disk I/O, data serialization and deserialization, and Network I/O. 

We cannot completely avoid shuffle operations but when possible try to reduce the number of shuffle operations and remove any unused operations.

The Default Value for shuffle partitions is set to 200 because Spark doesn’t know the optimal partition size to use, post-shuffle operation. Most of the time these values cause performance issues hence, change them based on the data size. 

**Configuration Properties**

| Property | Description | Default Value | Recommended Value |
| --- | --- | --- | --- |
| `spark.sql.shuffle.partitions` | Provides value for the shuffle partition | 200 | If you have huge data then you need to have a higher number and if you have a smaller dataset have it lower number |

You need to tune this value along with others until you reach your performance baseline.

# **Parallel Listing on Input Paths**

> **Beneficial Scenario:** When job has large number of directories, especially in object stores like S3, GCS etc.
> 

To increase directory listing parallelism when job input has large number of directories, when against object store like S3. For Spark SQL with file-based data sources, you can tune the following property

**Configuration Property**

| Property | Description | Default Value | Recommended Value |
| --- | --- | --- | --- |
| `spark.sql.sources.parallelPartitionDiscovery.threshold` | Configures the threshold to enable parallel listing for job input paths. If the number of input paths is larger than this threshold, Spark will list the files by using Spark distributed job. Otherwise, it will fallback to sequential listing. This configuration is only effective when using file-based data sources such as Parquet, ORC and JSON. | 32 | Higher the value of the threshold the less frequently the distributed listing will occur |
| `spark.sql.sources.parallelPartitionDiscovery.parallelism` | Configures the maximum listing parallelism for job input paths. In case the number of input paths is larger than this value, it will be throttled down to use this value. Same as above, this configuration is only effective when using file-based data sources such as Parquet, ORC and JSON. | 10000 | Higher value more the parallelism |