# Scanner for Data Quality Checks

Flare workflows are run for data quality checks on the entire dataset or sample /filtered data. DataOS now also extends support to other quality check platforms, such as SQL-powered SODA. It enables you to use the Soda Checks Language (SodaCL) to turn user-defined inputs into aggregated SQL queries. With Soda, you get a far more expressive language to test the quality of your datasets.

It allows for complex user-defined checks with granular control over fail and warn states.

## Worker YAML for Scanning Soda Quality Checks 

Soda Quality Scanner Worker is a continuous running service to read about these quality checks for your data along with their pass/fail status whenever a SODA quality job is run. It extracts metadata related to data quality and stores it in Metis DB. 

### **YAML Configuration** 

```yaml
name: soda-quality-checks-indexer
version: v1beta
type: worker
tags:
  - Scanner
description: >-
  The purpose of this worker is to reactively scan datasets and ingest quality
  checks and metrics data whenever a soda scan is triggered.
owner: metis
workspace: system
worker:
  title: Soda Quality Checks Indexer
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
    worker: soda_indexer
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

You can view the list of SLOs created for the dataset to monitor the data quality and trend charts for each run. The trend charts also show whether the checks are passed or failed.