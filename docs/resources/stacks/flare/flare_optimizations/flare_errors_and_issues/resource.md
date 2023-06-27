# Resource Allocation Errors


## Error: Insufficient Resource

```verilog
check your cluster UI to ensure that workers are registered and have sufficient resources
```

**What went wrong?**

The allocated memory with Driver and Executor is less

**Solution**

Increase the memory to rectify the error

## Error: OOM (Out of Memory) Killed Error

**What went wrong?**

- Inefficient queries
- High concurrency
- Incorrect configuration

**Solution**

[https://komodor.com/learn/how-to-fix-oomkilled-exit-code-137/](https://komodor.com/learn/how-to-fix-oomkilled-exit-code-137/)

**Resource Material**

[https://towardsdatascience.com/6-recommendations-for-optimizing-a-spark-job-5899ec269b4b](https://towardsdatascience.com/6-recommendations-for-optimizing-a-spark-job-5899ec269b4b)

[https://blog.clairvoyantsoft.com/apache-spark-out-of-memory-issue-b63c7987fff](https://blog.clairvoyantsoft.com/apache-spark-out-of-memory-issue-b63c7987fff)

## Memory Usage of Reduce Tasks

Sometimes, you will get an OutOfMemoryError (Link) not because your RDDs don’t fit in memory, but because the working set of one of your tasks like one of Spark’s shuffle operations (`sortByKey`
, `groupByKey`, `reduceByKey`, `join`, etc) build a hash table within each task to perform the grouping, which can often be large. 

The simplest fix here is to increase the level of parallelism so that each task’s input set is smaller.

## Error: Driver maxresultsize error

**What went wrong?**

It is caused by actions like RDD's `collect()` that send a big chunk of data to the driver.

**Solutions**

- Set SparkConf: conf.set("spark.driver.maxResultSize", "3g")
- Increase spark.driver.maxResultSize or set it to 0 for unlimited
- If broadcast joins are the culprit, you can reduce `spark.sql.autoBroadcastJoinThreshold` to limit the size of broadcast join data
- Reduce the number of partitions.

## Error: Missing output location for shuffle partitions

**Solution**

The solution was to either add swap or configure the worker/executor to use less memory in addition to using MEMORY_AND_DISK storage level for several persists.

## Error: **Executor Lost Failure**

**Solution**

The solution, if you're using yarn, was to set `-conf spark.yarn.executor.memoryOverhead=600`, alternatively if your cluster uses Mesos you can try `-conf spark.mesos.executor.memoryOverhead=600` instead

Table of Contents