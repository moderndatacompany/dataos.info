# Recommended Cluster Configuration

DataOS offers the flexibility to create clusters on-demand based on specific use cases, allowing you to customize the cluster according to your needs. The following cluster configurations are recommended for different query loads.

## Scenario 1: Running ad hoc queries by a group of analysts

In this scenario, workloads are not intensive, and the cluster is shared among users.

**High availability**

For this use case, it is recommended to have multiple Minerva clusters to ensure high availability.

**Recommended Configuration**

A default Minerva cluster can be used with the properties specified in the toggle below.

<details>
<summary>Minerva Cluster Configuration</summary>

```yaml
name: minervab
version: v1    
type: cluster
description: the default minerva cluster b
tags:
- cluster
- minerva
cluster:                          
nodeSelector:
    "dataos.io/purpose": "query"
toleration: query
runAsApiKey: api-key
minerva:            
    replicas: 2
    resources:
    limits:
        cpu: 2000m
        memory: 4Gi
    requests:
        cpu: 2000m
        memory: 4Gi
    debug:
    logLevel: INFO
    trinoLogLevel: ERROR
```
</details>

For more information, refer to the [Multi-Cluster Setup](/resources/cluster/examples/multiple_cluster_setup).

## Scenario 2: Data scientists/analysts running intensive data exploration

In this scenario, clusters are required for specialized use cases or teams, such as data scientists running complex data exploration and machine learning algorithms.

**Recommended Configuration**

For these use cases, it is recommended to use on-demand Minerva Clusters and consider the following configurations:

1. Use a bigger cluster by increasing the maximum worker node count.
2. Add a limit clause for all subqueries.
3. Use a larger cluster instance.

Increasing the number of nodes in a single cluster improves throughput and resource utilization, enabling efficient processing of large queries.


## Scenario 3: CPU optimized instance

In scenarios where a high number of concurrent small queries with significant CPU time is required, a CPU-optimized instance is recommended.

**Recommended Configuration**

For a combination of large and medium queries, where data scanned ranges from a hundred Megabytes to a Terabyte, a memory-optimized instance is more suitable.

These parameters can be tuned based on specific requirements.

For further details, please refer to the [Performance Tuning](/resources/cluster/performance_tuning) section.