# Scanner for DataOS Resources Metadata

This worker responds reactively to scan targeted DataOS Resource information from Poros whenever a lifecycle event is triggered. It adeptly captures pertinent details and promptly publishes them to the Metis DB, thereby maintaining an up-to-date repository of DataOS Resources metadata.

## Worker YAML to Scan for DataOS Resources Metadata

Data quality Scanner Worker is a continuous running service to read the metadata across Workflows, Services, Clusters, Depots, etc., including their historical runtime and operations data, and saves it to the Metis DB a whenever a DataOS Resource is created, deleted within DataOS. 

### **YAML Configuration** 

```yaml
name: poros-indexer
version: v1beta
type: worker
tags:
  - Scanner
description: >-
  The purpose of this worker is to reactively scan metadata for DataOS Resources whenever a
  lifecycle event is triggered.
owner: metis
workspace: system
worker:
  title: Workflow Indexer
  tags:
    - Scanner
  replicas: 2
  autoScaling:
    enabled: true
    minReplicas: 2
    maxReplicas: 3
    targetMemoryUtilizationPercentage: 120
    targetCPUUtilizationPercentage: 120
  stack: scanner:2.0
  stackSpec:
    type: worker
    worker: poros_indexer
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

You can view the collected metadata about DataOS Resources on Metis UI.