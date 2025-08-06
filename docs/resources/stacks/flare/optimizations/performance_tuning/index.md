# Performance Tuning

When applied correctly, performance tuning enables efficient utilization of available resources and contributes to reduced system execution time. Due to the numerous variables involved—such as cluster size, concurrent workloads, input data volume, and computation type—identifying the optimal Spark configuration often requires iterative refinement.

## Tweaking Spark Properties

The `sparkConf` property in the job YAML file defines Spark configuration parameters for a given Flare job. This property includes environment settings, default values, and other configuration directives represented as YAML key-value pairs, as shown below:

```yaml
sparkConf:
  - <Configuration>: <value>
  - <Configuration>: <value>
```

For example, to configure a job with five executors and use the Kryo serializer, the following entries must be included:

```yaml
sparkConf:
  - spark.executor.instances: 5
  - spark.serializer: org.apache.spark.serializer.KryoSerializer
```

These properties may either be specified directly within the manifest file or sourced from an external configuration file referenced during job submission. Active configuration details for a running job can be viewed under the **Environment** tab in the Spark Web UI.

!!! info "Configuring Spark Properties"

      Tuning Spark properties ensures optimal resource utilization, especially given Spark's in-memory execution model. **Resource bottlenecks** can be mitigated through deliberate adjustments to configuration parameters based on specific system requirements.

## SQL Query Optimization

SQL query tuning is an iterative process aimed at improving execution metrics such as processing time and disk I/O. Within Flare workflows, optimized queries significantly reduce response time and improve throughput. Further details are available in [SQL Query Optimization](/resources/stacks/flare/optimizations/performance_tuning/sql_query_optimization/).

## Job Tuning Configurations

In addition to resource allocation, several configuration properties—including serialization format, parallelism level, and disk spill behavior—can substantially impact job performance depending on workload characteristics. For more information, refer to [Tuning Configurations](/resources/stacks/flare/optimizations/performance_tuning/tuning_configurations/).


