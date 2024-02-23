# Scanner for Data Profiling

Flare workflows are run for data profiling on the entire dataset or sample /filtered data and uses basic statistics to know about the validity of the data. This analysis is stored in Icebase.
> To learn more about data profiling Flare workflows, click [here](/resources/stacks/flare/#data-profiling-job).
>

A continuous running service reads about these statistics (metadata extraction related to data profiling) and stores it in Metis DB. This data helps you find your data's completeness, uniqueness, and correctness for the given dataset.

## Scanner Worker YAML 

The given Worker YAML will scan the data profile-related information whenever data profiling job is run on any dataset.

### **YAML Configuration**

```yaml
name: dataset-profiling-indexer
version: v1beta
type: worker
tags:
  - Scanner
description: >-
  The purpose of this worker is to reactively scan workflows and ingest
  profiling data whenever a lifecycle event is triggered.
owner: metis
workspace: system
worker:
  title: Dataset Profiling Indexer
  tags:
    - Scanner
  replicas: 1
  autoScaling:
    enabled: true
    minReplicas: 1
    maxReplicas: 2
    targetMemoryUtilizationPercentage: 120
    targetCPUUtilizationPercentage: 120
  stack: scanner:2.0
  stackSpec:
    type: worker
    worker: data_profile_indexer
  logLevel: INFO
  compute: runnable-default
  runAsUser: metis
  resources:
    requests:
      cpu: 500m
      memory: 1024Mi
    limits: {}
  runAsApiKey: '****************************************************************************'
```

## Metadata on Metis UI

On a successful run, you are able to view the captured data profiling information about the dataset on Metis UI.