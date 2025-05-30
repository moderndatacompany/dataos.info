# Scanner for Quality Checks 


## Scanner for Data quality

Scanner for Data quality is a Worker(continuous running service), designed to reactively scan datasets and ingest quality checks and metrics data along with their pass/fail status whenever a Flare data quality scan is initiated. The acquired metadata related to data quality is then published to the Metis DB, contributing to a comprehensive understanding of data quality. The sample manifest file to extract the metadata of the quality checks are as follows:

```yaml
name: dataset-quality-checks-indexer
version: v1beta
type: worker
tags: 
  - Scanner
description: 
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

```

User can view the list of SLOs created for the dataset to monitor the data quality and trend charts for each run. The trend charts also show whether the checks are passed or failed.


## Scanner for SODA quality checks

DataOS now also extends support to other quality check platforms, such as SQL-powered SODA. It enables user to use the Soda Checks Language (SodaCL) to turn user-defined inputs into aggregated SQL queries. With Soda, user get a far more expressive language to test the quality of your datasets. It allows for complex user-defined checks with granular control over fail and warn states.

The primary objective of Scanner for SODA quality checks (a Worker which is a continuous running service) is to reactively scan datasets, for collecting quality checks and metrics data along with their pass/fail status whenever a SODA quality scan is triggered. The collected data is saved to the Metis DB, facilitating thorough analysis and monitoring. The sample manifest file to extract the metadata of the quality checks are as follows:

```yaml
name: soda-quality-checks-indexer
version: v1beta
type: worker
tags:
  - Scanner
description: 
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
```

On Metis UI, you can view the list of SLOs created for the dataset to monitor the data quality and trend charts for each run. The trend charts also show whether the checks are passed or failed. The above sample manifest files can be deployed using the following command:

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

## Data Quality vs Soda Quality

Data quality and Soda quality are related but distinct concepts in the context of data validation and quality checks.

* **Data Quality**: Refers to the overall quality of a dataset, including its accuracy, completeness, consistency, and reliability. DataOS allows user to define personalize assertions with a combination of tests to check the rules for data quality.

* **Soda Quality**: Specifically refers to the quality checks performed using the Soda Checks Language (SodaCL) and the SODA quality check platform. SodaCL enables to turn user-defined inputs into aggregated SQL queries, allowing for complex user-defined checks with granular control over fail and warn states.

In other words, data quality is a broader concept that encompasses various aspects of data quality, while Soda quality is a specific implementation of data quality checks using the Soda platform.