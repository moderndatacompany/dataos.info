# Cluster Configuration Scenarios

DataOS supports creating clusters on-demand, allowing you to tailor your cluster according to your use cases.

You can create:

- Small clusters with limited memory and CPU for Adhoc queries
- Dedicated clusters (department-wise) for example Marketing
- Dedicated cluster (User-based ) for example data analyst/data scientist
- Ad hoc clusters
- Pool, group of clusters
- Multi-user clusters

The following section provides recommendations for Cluster configuration for different query loads.

<u>Scenario 1</u>

## Running ad hoc queries by a group of analysts

Workloads are not intensive.

- you are using the default instances.
- The cluster needs to be available all the time and shared by the users.

This requires multiple users to access data for running data analysis and ad-hoc queries. Cluster usage might fluctuate over time, and most jobs are not very resource-intensive. The users mostly require read-only access to the data and want to perform analyses or create dashboards through a simple user interface.

High availability

This cluster is always available and shared by the users belonging to a group by default. Users do not have access to start/stop the cluster, but the initial on-demand instances are immediately available to respond to user queries.

Multiple Minerva clusters are used to satisfy HA requirements.

Recommended configurations

For example, default Minerva clusters.

```yaml
- version: v1beta1
  name: minervab                    # Name of the Minerva cluster
  type: cluster
  description: the default minerva cluster b
  tags:
    - cluster
    - minerva
  cluster:                          # Minerva cluster properties 
    nodeSelector:
      "dataos.io/purpose": "query"
    toleration: query
    runAsApiKey: api-key
    minerva:                        # Tune these values for optimal performance
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

<u>Scenario 2</u>

## Data scientists/analysts running intensive data exploration

You need to provide clusters for specialized use cases or teams within your organization, for example, data scientists running complex data exploration and machine learning algorithms.

A cluster is needed for a long period of time to run these operations. Users should be able to start and stop the cluster or auto terminate. 

Admin can configure different types of clusters with different groups of users with separate access permissions for different sets of data.

Recommended configurations

For example, on-demand Minerva clusters

1. Use a bigger cluster by increasing the maximum worker node count.
2. Add a limit clause for all subqueries.
3. Use a larger cluster instance

For increasing throughput, adding more nodes to a single cluster is almost always a better option. It can utilize more worker nodes to process large queries and generally results in better resource utilization.
To learn more, refer to [Multi-Cluster Setup](Cluster%20Tuning.md).

<u>Scenarios 3</u>

### CPU optimized instance

If the use case requires a high number of concurrent small queries (data scanned less than a few hundred Megabytes), lots of CPU time is needed.

Recommended Configuration

memory-optimized instance

For a combination of large queries (data scanned greater than a Terabyte) and medium queries (data scanned between a hundred Megabytes and less than a Terabyte), a memory-optimized instance works better.

You can tune these parameters as per requirement. 
To learn more, refer to [Cluster Tuning](Cluster%20Tuning.md).