# Performance Tuning

If used properly, tuning can ensure the proper use of all resources in an effective manner and improvement in the performance time of the system. Because of the many variables associated with tuning a job - cluster dimensions, cluster traffic, input data size, and type of computation finding the optimal Spark configuration is difficult to do without some trial and error.

# Tweaking Spark Properties

The `sparkConf` property within the YAML defines how Spark should be configured for a given Flare Job. The `sparkConf` property contains all the configurations, defaults, and environment information that govern the behavior of Spark. These settings are represented as YAML key/value pairs, the syntax for which is given below:

```yaml
sparkConf:
            - <Configuration>: <value>
							<Configuration>: <value>
```

For example, to submit a job with five executors and serializer as Kryo, you need to specify the values of `spark.executor.instances` and `spark.serializer`. This can be done as follows:

```yaml
sparkConf:
            - spark.executor.instances: 5
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
```

You can either specify the values of the `sparkconf` directly in the form of key-value pairs or define them in an external file and pass its path as an argument

The configurations for a running Flare Job can be found in the environment tab of the Spark Web UI.

## Configuring Spark Properties

Flare Job Tuning guarantees that Spark has optimal performance. Spark has in-memory computation nature and resources often get bottlenecked. Effective changes can be made to each property and setting, to ensure the correct usage of resources based on the system-specific setup. 

## SQL Query Optimization

SQL Query optimization or tuning is an iterative process of enhancing the performance of a query in terms of execution time, the number of disk accesses, and many more cost-measuring criteria.

When it comes to Flare workflows, optimizing the queries can have a drastic impact on overall execution time in terms of reducing response time with improved throughput. To know more, refer to
[SQL Query Optimization](Performance%20Tuning/SQL%20Query%20Optimization.md).

# Job Tuning Configurations

Apart from configuring the allocated resources, other properties like serializing formats, level of parallelism, disk spillage etc. can affect a job significantly in certain scenarios. To know more, refer to
[Tuning Configurations](Performance%20Tuning/Tuning%20Configurations.md).