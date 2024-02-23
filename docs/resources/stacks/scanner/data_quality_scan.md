# Scanner for Data Quality Checks

Service Level objectives(SLOs) are business-specific validation rules applied to test and evaluate the quality of specific datasets if they are appropriate for the intended purpose. DataOS allows you to define your own assertions with a combination of tests to check the rules. Flare workflows are run for data quality checks on the entire dataset or sample /filtered data. This analysis is stored in Icebase.

> To learn more about data quality (assertions) Flare workflows, click [here](/resources/stacks/flare/#types-of-flare-jobs).
>

## Worker YAML 

Data quality Scanner Worker is a continuous running service to read about these quality checks for your data along with their pass/fail status(metadata extraction related to data quality) and stores it in Metis DB. 

### **YAML Configuration** 

```yaml
name: dataset-quality-checks-indexer
version: v1beta
type: worker
tags:
  - Scanner
description: >-
  The purpose of this worker is to reactively scan workflows and ingest
  quality checks and metrics data whenever a lifecycle event is triggered.
owner: metis
workspace: system
worker:
  title: Dataset Quality Checks Indexer
  tags:
    - Scanner
  replicas: 1
  autoScaling:
    enabled: true
    minReplicas: 1
    maxReplicas: 2
    targetMemoryUtilizationPercentage: 120
    targetCPUUtilizationPercentage: 120
  logLevel: INFO
  runAsUser: metis
  compute: runnable-default
  stack: scanner:2.0
  stackSpec:
    type: worker
    worker: data_quality_indexer
  resources:
    requests:
      cpu: 500m
      memory: 1024Mi
    limits: {}
  runAsApiKey: '****************************************************************************'
```

## Metadata on Metis UI

You can view the list of SLOs created for the dataset to monitor the data quality and trend charts for each run. The trend charts also show whether the checks are passed or failed.