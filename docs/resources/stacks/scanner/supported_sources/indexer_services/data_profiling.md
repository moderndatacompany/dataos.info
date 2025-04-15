# Scanner for Data profiling 

Scanner for Data profiling is continuous running service that reads about the statistics (metadata extraction related to data profiling) and stores it in Metis DB. This data helps user understand data's completeness, uniqueness, and correctness for the given dataset. Below is a sample Scanner manifest file:

```yaml
name: dataset-profiling-indexer
version: v1beta
type: worker
tags:  
  - Scanner
description: 
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

```

The above sample manifest file is deployed using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Scanner YAML}}
```


**Updating the Scanner Workflow**:

If the Depot or Scanner configurations are updated, the Scanner must be redeployed after deleting the previous instance. Use the following command to delete the existing Scanner:

```bash 
  dataos-ctl delete -f ${{path-to-Scanner-YAML}}]
```

**OR**

```bash
  dataos-ctl delete -t workflow -n ${{name of Scanner}} -w ${{name of workspace}}
```


!!! info "**Best Practice**"

    As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.
    User can view this captured metadata, data profiling information about the dataset on Metis UI.

The objective of this worker is to proactively scan data profiling information, which includes descriptive statistics for datasets stored in Icebase. It operates in response to a triggered data profiling job, publishing the metadata to the Metis DB.