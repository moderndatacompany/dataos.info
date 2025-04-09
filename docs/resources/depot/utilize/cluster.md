# Query the source

For better understanding of the data, a user can query the data directly on Workbench without moving the data by creating a [Cluster Resource](/resources/cluster/).

**For example:**

A user wants to query data from the `bqdepot` Depot on Workbench, so they create a Cluster named `minervabq` targeting `bqdepot.`The below manifest file defines a Minerva-based Cluster Resource, `minervabq`, for querying data within DataOS. It specifies a `query-default` compute environment and configures Minerva-specific settings, including a single replica with resource allocations of 2 CPU cores (2000m) and 4Gi memory for both limits and requests. Debug settings define `INFO` log level for general logs and `ERROR` for Trino logs, ensuring controlled verbosity. The Cluster is linked to a Depot at `dataos://depotbq`, allowing seamless access to data stored in that location for querying and processing.

```yaml
# Resource meta section
name: minervabq
version: v1
type: cluster
description: testing 
tags:
    - cluster

# Cluster-specific section
cluster:
    compute: query-default
    type: minerva

    # Minerva-specific section
    minerva:
    replicas: 1
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
    depots:
        - address: dataos://bqdepot
```
