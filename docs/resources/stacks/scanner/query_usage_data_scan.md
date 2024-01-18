# Scanner for Query Usage Data

DataOS Gateway service backed by Gateway DB  keeps query usage data, and dataset usage analytics and harvests required insights such as (heavy datasets, popular datasets, datasets most associated together, etc.). The Scanner Worker is a continuous running service to extract query-related data and saves it to MetaStore.  It scans information about queries, users, dates, and completion times.

This query history/dataset usage data helps to rank the most used tables.

## Scanner Workflow YAML 

The following Scanner Worker is for metadata extraction related to query usage data. It reactively reads the queries data published to pulsar topic and ingest it into metis.

### YAML Configuration 

```yaml
name: query-usage-indexer
version: v1beta
type: worker
tags:
  - Scanner
description: >-
  This worker reactively reads the queries data published to pulsar topic and
  ingest it into metis.
owner: metis
workspace: system
worker:
  title: Query Usage Indexer
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
    worker: query_indexer
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

On a successful run, you can view the query usage data on Metis UI.