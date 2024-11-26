---
title: Scanner Stack
search:
  boost: 2
---

# Scanner Stack

The Scanner stack in DataOS is a Python-based framework designed for developers to extract metadata from external source systems (such as RDBMS, Data Warehouses, Messaging services, Dashboards, etc.) and the components/services within the DataOS environment to extract information about Data products and DataOS Resources. 

With the DataOS Scanner stack, you can extract both general information about datasets/tables, such as their names, owners, and tags, as well as more detailed metadata like table schemas, column names, and descriptions.  Additionally, this stack can help you retrieve metadata related to data quality and profiling, query usage, and user information associated with your data assets.

It can also connect with Dashboard and Messaging services to get the related metadata. For example, in the case of dashboards, it extracts information about the dashboard, dashboard Elements, and associated data sources.

Using the Scanner stackwithin DataOS, metadata can be extracted from DataOS Products and DataOS Resources. The extracted metadata offers detailed insights into the input, output & SLOs (Service Level Objectives) for every data product, along with all the data access permissions, infrastructure resources used for creating it and more. Users can track the entire life cycle of data product creation. The Scanner stack collects comprehensive metadata across DataOS Resources such as Workflows, Services, Clusters, Depots, etc.including their historical runtime and operations data.


## How Does Scanner Stack Work?

In DataOS, metadata extraction is treated as a job, which is accomplished using a DataOS resource called Workflow. This stack provides the ability to write workflows that extract metadata from various sources and store it in a metadata store. The Scanner workflow typically includes a source, transformations, and a sink.

Similar to an ETL (Extract, Transform, Load) job, the Scanner workflow connects to the metadata source, extracts the metadata, and applies transformations to convert it into a standardized format. The transformed metadata is then pushed to a REST API server, which is backed by a centralized metadata store or database such as MySQL or Postgres. This process can be performed in either a batch or scheduled manner, depending on the requirements.

<aside class="callout">
🗣 The default metadata store in DataOS is MetisDB which is a Postgres database.

</aside>

The stored metadata is used by various DataOS components for discoverability, governance, and observability. External apps running on top of DataOS can also fetch this metadata via Metis server APIs.

<aside class="callout">
🗣 In DataOS, all the metadata entities are defined and consumed in JSON format.

</aside>

<div style="text-align: center;">
  <img src="/resources/stacks/scanner/scanner_framework.png" alt="Metadata extraction using the Scanner stack" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption><i>DataOS Scanner stack for metadata extraction</i></figcaption>
</div>

Apart from the external applications, the Scanner stack can also extract metadata from various applications & services of DataOS. The scanner job reads related metadata and pushes it to the metadata store through the Metis REST API server. You can then explore this information through the Metis UI.

The Scanner job connects with the following DataOS components and stores the extracted metadata to Metis DB:

- **Collation Service**: To scan and publish metadata related to data pipelines, including workflow information, execution history, and execution states. It also collects metadata for historical data such as pods and logs, as well as data processing stacks like Flare and Benthos, capturing job information and source-destination relationships.
- **Gateway Service**: To retrieve information from data profiles (descriptive statistics for datasets) and data quality tables (quality checks for your data along with their pass/fail status). It also scans data related to query usage, enabling insights into heavy datasets, popular datasets, and associations between datasets.
- **Heimdall**: To scan and retrieve information about users in the DataOS environment, including their descriptions and profile images. This user information is accessible through the Metis UI.
- **Pulsar** **Service**: To keep listening to the messages being published on it by various other services and stacks within the system.

<aside class="callout">
🗣 DataOS Scanner is a flexible and extensible framework; you can easily integrate it with new sources.

</aside>

## Creating and Scheduling Scanner Workflows

Within DataOS, different workflows can be deployed and scheduled, which will connect to the data sources to extract metadata. 

- **Depot Scan Workflow**: With this type of Scanner workflow, depots are used to get connected to the metadata source to extract Entities’ metadata. It enables you to scan all the datasets referred by a depot. You need to provide the depot name or address, which will connect to the data source. 

- **Non-Depot Scan Workflow**: With this type of scanner workflow, you must provide the connection details and credentials for the underlying metadata source in the YAML file. These connection details depend on the underlying source and may include details such as host URL, project ID, email, etc.

<aside class="callout">
🗣 The non-Depot scan can help extract metadata from sources where depot creation is not supported or when you do not have an already created depot.

</aside>


You can write Scanner workflows in the form of a sequential YAML for a pull-based metadata extraction system built into DataOS for a wide variety of sources in your data stack. These workflows can be scheduled to run automatically at a specified frequency.

![Scanner YAML](/resources/stacks/scanner/scanner_yaml.png)
<figcaption align = "center">Scanner YAML Components</figcaption>

Learn about the source connection and configuration options to create depot scan/non-depot scan workflow DAGs to scan entity metadata.

[Creating Scanner Workflows](/resources/stacks/scanner/creating_scanner_workflows)

## Attributes of Scanner Workflow
docs/resources/stacks/scanner/field_ref.md
The below table summarizes various properties within a Scanner workflow YAML.

| Attribute                           | Data Type  | Default Value | Possible Value                                   | Requirement |
| ----------------------------------- | ---------- | ------------- | ----------------------------------------------- | ----------- |
| [`spec`](/resources/stacks/scanner/field_ref/#spec)         | mapping    |               |                                                 | Mandatory    |
| [`stack`](/resources/stacks/scanner/field_ref/#stack)       | string     |               | `scanner`                                       | Mandatory    |
| [`compute`](/resources/stacks/scanner/field_ref/#compute)   | string     | `runnable-default` | `mycompute`                                 | Mandatory |
| [`runAsUser`](/resources/stacks/scanner/field_ref/#runasuser)| string    |               | `metis`                                         | Mandatory    |
| [`depot`](/resources/stacks/scanner/field_ref/#depot)       | string     |               | `dataos://icebase`                              | Mandatory    | in case of Depot scan only.
| [`type`](/resources/stacks/scanner/field_ref/#type)         | string     | Source-specific | `bigquery`                                      | Mandatory    | In case of non-Depot scan
| [`source`](/resources/stacks/scanner/field_ref/#source)     | string     |               | `bigquery_metasource`                           | Mandatory    | In case of non-Depot scan
| [`sourceConnection`](/resources/stacks/scanner/field_ref/#sourceconnection) | mapping | |               | Mandatory    |
| [`type`](/resources/stacks/scanner/field_ref/#type_1)       | string     | Source-specific | `BigQuery`                                      | Mandatory    | In case of non-Depot scan
| [`username`](/resources/stacks/scanner/field_ref/#username) | string     | Source-specific | `projectID` `email` `hostport`                  | Mandatory    | In case of non-Depot scan
| [`sourceConfig`](/resources/stacks/scanner/field_ref/#sourceconfig) | mapping | |               | Mandatory    |
| [`type`](/resources/stacks/scanner/field_ref/#type_2)       | string     |               | `DatabaseMetadata`  `MessagingMetadata`        | Mandatory    | In case of non-Depot scan
| [`databaseFilterPattern`](/resources/stacks/scanner/field_ref/#databasefilterpattern) | mapping | | | Mandatory    |
| [`includes/exclude`](/resources/stacks/scanner/field_ref/#includes-or-excludes)| string | | `^SNOWFLAKE.*`                               | optional    | Applicable only in case of Database/Warehouse data source |
| [`schemaFilterPattern`](/resources/stacks/scanner/field_ref/#schemafilterpattern) | mapping | | | Mandatory    |
| [`includes/excludes`](/resources/stacks/scanner/field_ref/#includes-or-excludes_1) | string | | `^public$`                              | optional    | Applicable only in case of Database/Warehouse data source |
| [`tableFilterPattern`](/resources/stacks/scanner/field_ref/#tablefilterpattern) | mapping | | | mandatory   |                                                       |
| [`includes/excludes`](/resources/stacks/scanner/field_ref/#includes-or-excludes_2) | string | | `^public$`                              | optional    | Applicable only in case of Database/Warehouse data source |
| [`topicFilterPattern`](/resources/stacks/scanner/field_ref/#topicfilterpattern) | mapping | | | Mandatory    |
| [`includes/excludes`](/resources/stacks/scanner/field_ref/#includes-or-excludes_3)| string | | `foo` `bar`                               | optional    | Applicable only in case of Messaging data source     |
| [`includeViews`](/resources/stacks/scanner/field_ref/#includeviews) | boolean | `false`       | `true` `false`                              | optional    | Applicable only in case of Database/Warehouse data source |
| [`markDeletedTables`](/resources/stacks/scanner/field_ref/#markdeletedtables) | boolean | `false` | `true` `false`                            | optional    | Applicable only in case of Database/Warehouse data source |
| [`markDeletedTablesFromFilterOnly`](/resources/stacks/scanner/field_ref/#markdeletedtablesfromfilteronly) | boolean | `false`  | `true` `false` | optional | Applicable only in case of Database/Warehouse data source |
| [`enableDebugLog`](/resources/stacks/scanner/field_ref/#enabledebuglog) | boolean | `false` | `true` `false`                               | optional    | All                                                   |
| [`ingestSampleData`](/resources/stacks/scanner/field_ref/#ingestsampledata) |  boolean | `false` | `true` `false`                             | optional    | Applicable only in case of Messaging data source       |
| [`markDeletedTopics`](/resources/stacks/scanner/field_ref/#markdeletedtopics)| boolean | `false` | `true` `false`                            | optional    | Applicable only in case of Messaging data source       |

To learn more about these fields, their possible values, example usage, refer to [Attributes of Scanner YAML](/resources/stacks/scanner/field_ref/).

## Supported Data Sources

Here you can find templates for the depot/non-depot Scanner workflows for the supported data sources.
<center>

| Type             | Data Source      | Scanner|
|------------------|------------------|------|
| Database         | Maria DB         |[Link](/resources/stacks/scanner/databases_and_warehouses/mariadb/)    |
| Database         | MSSQL            |[Link](/resources/stacks/scanner/databases_and_warehouses/mssql/)    |
| Database         | MYSQL            |[Link](/resources/stacks/scanner/databases_and_warehouses/mysql/)   |
| Database         | Oracle           |[Link](/resources/stacks/scanner/databases_and_warehouses/oracle/)      |
| Database         | PostgreSQL       |[Link](/resources/stacks/scanner/databases_and_warehouses/postgresql/)      |
| Data Warehouse   | BigQuery         |[Link](/resources/stacks/scanner/databases_and_warehouses/bigquery/)      |
| Data Warehouse   | AzureSQL         |[Link](/resources/stacks/scanner/databases_and_warehouses/azuresql/)      |
| Data Warehouse   | Redshift         |[Link](/resources/stacks/scanner/databases_and_warehouses/redshift/)      |
| Data Warehouse   | Snowflake        |[Link](/resources/stacks/scanner/databases_and_warehouses/snowflake/)      |
| Lakehouse        | Icebase          |[Link](/resources/stacks/scanner/databases_and_warehouses/icebase/)     |
| Messaging Service| Kafka            |[Link](/resources/stacks/scanner/messaging_services/kafka/)     |
| Messaging Service| Fastbase/Pulsar  |[Link](/resources/stacks/scanner/messaging_services/fastbase/)    |
<!-- | Dashboard Service| Atlas            |[Link](/resources/stacks/scanner/dashboards/atlas_scan/)      | -->
| Dashboard Service| Redash           |[Link](/resources/stacks/scanner/dashboards/redash_scan/)      |
| Dashboard Service| Superset         |[Link](/resources/stacks/scanner/dashboards/superset_scan/)      |

</center>

<!-- 
[Databases and Warehouses](scanner/databases_and_warehouses)

[Messaging Services](scanner/messaging_services)

[Dashboard Services](scanner/dashboards) -->

<aside class="callout">
🗣 You can perform both depot scans and non-depot scans on all the data sources where you have established depots. The distinction lies in the fact that non-depot scans require you to furnish connection information and credentials within the Scanner YAML file. Whereas, for depot scans, you only need to provide the depot name or address.
</aside>

## System Scanner Workflows

The following workflows are running as system workflows to periodically scan the related metadata and save it to Metis DB to reflect the updated metadata state. They are scheduled to run at a set interval.

### **Data Products**
Data product Scanner workflows is for collecting metadata related to Data products such as inputs, outputs, SLOs, policies, lineage and associated DataOS Resources.

This Scanner workflow reads the metadata and stores it in Metis DB. This metadata helps you understand data product's life cycle along with the data access permissions, infrastructure resources used for creating it.

<details><summary> Scanner for Data Product</summary>

```yaml
version: v1
name: scanner2-data-product
type: workflow
tags:
  - scanner
  - data-quality
description: The job scans schema tables and register data
workflow:
  # schedule:
  #   cron: '*/20 * * * *'
  #   concurrencyPolicy: Forbid
  dag:
    - name: scanner2-data-product-job
      description: The job scans schema from data-product and register data to metis
      spec:
        tags:
          - scanner2
        stack: scanner:2.0
        compute: runnable-default
        stackSpec:
          type: data-product
          sourceConfig:
            config:
              type: DataProduct
              markDeletedDataProducts: true
              # dataProductFilterPattern:
              #   includes:
              #     - customer-360-all$
```

</details>

<aside class="callout">

🗣 On a successful run, you can view the Data Product information on Metis UI.
</aside>

### **System Metadata Sync**

This scanner periodically scans the icebase and Fastbase and stores metadata related to tables and topics in Metis DB. It collects information from Icebase and Fastbase for the newly added data assets.<br>

<details><summary>Scanner for System Metadata</summary>

```yaml
name: system-metadata-sync
version: v1
type: workflow
tags:
  - icebase
  - fastbase
  - profile
  - scanner
description: Icebase, fastbase metadata scanner workflow
owner: metis
workspace: system
workflow:
  title: Icebase and Fastbase Depot Scanner
  schedule:
    cron: '*/30 * * * *'
    timezone: UTC
    concurrencyPolicy: Forbid
  dag:
    - name: icebase-scanner
      description: The job scans and publishes all datasets from icebase to metis.
      spec:
        stack: scanner:2.0
        logLevel: INFO
        compute: runnable-default
        resources:
          requests:
            cpu: 250m
            memory: 512Mi
          limits: {}
        runAsApiKey: >-
          ****************************************************************************
        runAsUser: metis
        stackSpec:
          depot: icebase
          sourceConfig:
            config:
              markDeletedTables: true
    - name: fastbase-scanner
      description: The job scans and publishes all datasets from fastbase to metis.
      spec:
        stack: scanner:2.0
        logLevel: INFO
        compute: runnable-default
        resources:
          requests:
            cpu: 250m
            memory: 512Mi
          limits:
            cpu: 1100m
            memory: 2048Mi
        runAsApiKey: >-
          ****************************************************************************
        runAsUser: metis
        stackSpec:
          depot: fastbase
stamp: '-bkcu'
generation: 33
uid: a105c747-410c-4edc-9953-bda462e94efd
status: {}
```

</details>

<aside class="callout">
🗣 On a successful run, you can view the scanned metadata on Metis UI under the "Assets" for tables and topics.</aside>

### **Users’ Information**

Heimdall, in DataOS, is the security engine managing user access. It ensures only authorized users can access DataOS resources. This Scanner workflow connects with Heimdall to To scan and retrieve information about users in the DataOS environment, including their descriptions and profile images and stores it in Metis DB. 

This Scanner workflow will scan the information about the users in DataOS. This is a scheduled workflow that connects with Heimdall on a given cadence to fetch information about users.

<details><summary>Scanner for User's Information</summary>

```yaml
name: heimdall-users-sync
version: v1
type: workflow
tags:
  - users
  - scanner
description: Heimdall users sync workflow
owner: metis
workspace: system
workflow:
  title: Heimdall Users Sync
  schedule:
    cron: '*/10 * * * *'
    timezone: UTC
    concurrencyPolicy: Forbid
  dag:
    - name: users-sync
      description: The job scans and publishes all users heimdall to metis.
      spec:
        stack: scanner:2.0
        stackSpec:
          type: users
        logLevel: INFO
        compute: runnable-default
        runAsUser: metis
        resources:
          requests:
            cpu: 250m
            memory: 512Mi
          limits:
            cpu: 1100m
            memory: 2048Mi
        runAsApiKey: >-
          ****************************************************************************
```
</details>

<aside class="callout">

🗣 On a successful run, you can view the users information on Metis UI.
</aside>

## Metadata Update
Indexer service, a continuous running service within the DataOS environment keeps track of newly created or updated entities such as **Data products**, **Data Assets**(datasets/topics/dashboards, etc.) and **DataOS Resources**(Workflows, Services, Workers, Monitors, Depots etc.). With this information about the changed entity, it creates a reconciliation Scanner YAML with filters to include only the affected entity. This Scanner workflow will extract the metadata about the entity and update the target metastore.

The following continuous running services are designed for triggering the specific type of metadata scan. 

### **Data Profiling**

Flare workflows are run for data profiling on the entire dataset or sample /filtered data and uses basic statistics to know about the validity of the data. This analysis is stored in Icebase.
> To learn more about data profiling Flare workflows, click [here](/resources/stacks/flare/#data-profiling-job).
>

A continuous running service reads about these statistics (metadata extraction related to data profiling) and stores it in Metis DB. This data helps you find your data's completeness, uniqueness, and correctness for the given dataset. 

The objective of this worker is to proactively scan data profiling information, which includes descriptive statistics for datasets stored in Icebase. It operates in response to a triggered data profiling job, publishing the metadata to the Metis DB.

<details><summary>Indexer Service for Data Profiling</summary>

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

</details>

<aside class="callout">
🗣
You can view this captured metadata, data profiling information about the dataset on Metis UI.</aside>

### **Data Quality**

Service Level objectives(SLOs) are business-specific validation rules applied to test and evaluate the quality of specific datasets if they are appropriate for the intended purpose. DataOS allows you to define your own assertions with a combination of tests to check the rules.

This worker is a continuous running service, designed to reactively scan datasets and ingest quality checks and metrics data along with their pass/fail status whenever a Flare data quality scan is initiated. The acquired metadata related to data quality is then published to the Metis DB, contributing to a comprehensive understanding of data quality. 

<details><summary>Indexer Service for Data Quality</summary>

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
</details>

<aside class="callout">
🗣 You can view the list of SLOs created for the dataset to monitor the data quality and trend charts for each run. The trend charts also show whether the checks are passed or failed.
</aside>

### **SODA Quality Checks**

DataOS now also extends support to other quality check platforms, such as SQL-powered SODA. It enables you to use the Soda Checks Language (SodaCL) to turn user-defined inputs into aggregated SQL queries. With Soda, you get a far more expressive language to test the quality of your datasets. It allows for complex user-defined checks with granular control over fail and warn states.

The primary objective of this continuous running service (worker) is to reactively scan datasets, for collecting quality checks and metrics data along with their pass/fail status whenever a SODA quality scan is triggered. The collected data is saved to the Metis DB, facilitating thorough analysis and monitoring.

<details><summary>Indexer Service for SODA Quality Checks</summary>

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

</details>

<aside class="callout">
🗣 On Metis UI, you can view the list of SLOs created for the dataset to monitor the data quality and trend charts for each run. The trend charts also show whether the checks are passed or failed.
</aside>

### **DataOS Resources**

DataOS Resources Metadata Scanner Worker is a continuous running service to read the metadata across Workflows, Services, Clusters, Depots, etc., including their historical runtime and operations data, and saves it to the Metis DB a whenever a DataOS Resource is created, deleted within DataOS. 

This worker operates reactively to scan specific DataOS Resource information from Poros whenever a lifecycle event is triggered. It captures relevant details and publishes them to the Metis DB, ensuring an up-to-date repository of DataOS Resources metadata. 

<details><summary>Indexer Service for DataOS Resources </summary>


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
</details>

<aside class="callout"> 🗣 You can view the collected metadata about DataOS Resources on Metis UI.</aside>

### **Query Usage**

DataOS Gateway service backed by Gateway DB  keeps query usage data, and dataset usage analytics and harvests required insights such as (heavy datasets, popular datasets, datasets most associated together, etc.). The Scanner Worker is a continuous running service to extract query-related data and saves it to MetaStore.  It scans information about queries, users, dates, and completion times. This query history/dataset usage data helps to rank the most used tables.

The following Scanner Worker is for metadata extraction related to query usage data. It reactively reads the queries data published to pulsar topic and ingest it into metis. It scans information about queries, users, dates, and completion times. 

<details><summary>Indexer Sertvice for Query Usage </summary>

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

</details>

<aside class="callout"> 🗣 You can view the query usage data for your dataset on Metis UI.
</aside>


## Common Errors

[Common Scanner Errors](/resources/stacks/scanner/common_scanner_errors/)