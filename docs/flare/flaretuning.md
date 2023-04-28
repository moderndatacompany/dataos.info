# Flare Job Tuning 

## Overview

Flare in DataOS is built on top of Apache Spark to provide a computing platform. It is a declarative stack and defines Spark job processing configuration using YAML. Configuration setting in YAML abstracts the need for programming languages to write data processing jobs.  

You can easily modify the settings and properties of Spark, defined in YAML, to ensure that the resources are utilized properly and the jobs are executed efficiently. 

## Fine tuning of Flare jobs

Apache Spark defaults provide decent performance for large data sets but you can have significant performance gains if able to tune parameters based on resources and job. For your Flare workflows, you can modify  Spark configuration parameters such as garbage collector selection, serialization, tweaking number of workers/executors, partitioning key, partition sizes etc. 

### driver section

Determine the type and number of instances based on application needs. Define them under **driver** section in the YAML file of your Flare job.

```yaml
driver:
    coreLimit: 1200m
    cores: 1
    memory: 1024m
    executor:
    coreLimit: 1200m
    cores: 1
    instances: 1
    memory: 1024m
```

### sparkConf section

Set the Spark configuration parameters carefully for Flare job to run successfully. Define them under **sparkConf** section in the YAML file of your Flare job.

```yaml
sparkConf:
    - spark.serializer: org.apache.spark.serializer.KryoSerializer
    - spark.sql.legacy.timeParserPolicy: LEGACY
    - spark.sql.shuffle.partitions: "800"
    - spark.executor.extraJavaOptions: -XX:+PrintFlagsFinal -XX:+PrintReferenceGC
        -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintAdaptiveSizePolicy
        -XX:+UnlockDiagnosticVMOptions -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/hoodie-heapdump.hprof
    - spark.driver.extraJavaOptions: -XX:+PrintTenuringDistribution -XX:+PrintGCDetails
        -XX:+PrintGCDateStamps -XX:+PrintGCApplicationStoppedTime -XX:+PrintGCApplicationConcurrentTime
        -XX:+PrintGCTimeStamps -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/hoodie-heapdump.hprof
    - spark.memory.storageFraction: "0.1"
    - spark.memory.fraction: "0.1"
    - spark.kryoserializer.buffer.max: 256m
    - spark.shuffle.memoryFraction: "0.0"
```

## Spark configuration parameters
A brief introduction of the Spark configuration parameters is given below. To understand more about each of the parameters, see the ** <a href="https://spark.apache.org/docs/latest/configuration.html#application-properties" target="_blank">Spark documentation </a>.**

**Parameter** | **Description** | 
-------- | -------- |
spark.executor.memory | Size of memory to use for each executor that runs the task.
spark.executor.cores | Number of virtual cores.
spark.driver.memory | Size of memory to use for the driver.
spark.driver.cores | Number of virtual cores to use for the driver.
spark.executor.instances ­| Number of executors. Set this parameter unless spark.dynamicAllocation.enabled is set to true.
spark.default.parallelism | Default number of partitions in resilient distributed datasets (RDDs) returned by transformations like join, reduceByKey, and parallelize when no partition number is set by the user.
spark.network.timeout | Timeout for all network transactions.
spark.executor.heartbeatInterval | Interval between each executor’s heartbeats to the driver. This value should be significantly less than spark.network.timeout.
spark.memory.fraction | Fraction of JVM heap space used for Spark execution and storage. The lower this is, the more frequently spills and cached data eviction occur.
spark.memory.storageFraction | Expressed as a fraction of the size of the region set aside by spark.memory.fraction. The higher this is, the less working memory might be available to execution. This means that tasks might spill to disk more often.
spark.yarn.scheduler.reporterThread.maxFailures | Maximum number executor failures allowed before YARN can fail the application.
spark.rdd.compress | When set to true, this property can save substantial space at the cost of some extra CPU time by compressing the RDDs.
spark.shuffle.compress | When set to true, this property compresses the map output to save space.
spark.shuffle.spill.compress | When set to true, this property compresses the data spilled during shuffles.
spark.sql.shuffle.partitions | Sets the number of partitions for joins and aggregations.
spark.serializer | Sets the serializer to serialize or deserialize data. As a serializer, Kyro (org.apache.spark.serializer.KryoSerializer) is preferred, which is faster and more compact than the Java default serializer.
coalesce | Reduces the number of partitions to allow for less data movement.
repartition | Reduces or increases the number of partitions and performs full shuffle of data as opposed to coalesce.
partitionBy | Distributes data horizontally across partitions.
bucketBy | Decomposes data into more manageable parts (buckets) based on hashed columns.
cache/persist | Pulls datasets into a clusterwide in-memory cache. Doing this is useful when data is accessed repeatedly, such as when querying a small lookup dataset or when running an iterative algorithm.

