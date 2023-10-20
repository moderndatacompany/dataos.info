# Scanner
The Scanner stack in DataOS is a Python-based framework designed for developers to extract metadata from external source systems (such as RDBMS, Data Warehouses, Messaging services, Dashboards, etc.) and the components/services within the DataOS environment. 

With the DataOS Scanner stack, you can extract both general information about datasets/tables, such as their names, owners, and tags, as well as more detailed metadata like table schemas, column names, and descriptions.  It can also connect with Dashboard and Messaging services to get the related metadata. For example, in the case of dashboards, it extracts information about the dashboard, dashboard Elements, and associated data sources.

Additionally, the Scanner stack can help you retrieve metadata related to data quality and profiling, query usage, pipelines (workflows), and user information associated with your data assets.

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

![Metadata extraction using the Scanner stack](./scanner/scanner_framework.png)
<figcaption align = "center">DataOS Scanner stack for metadata extraction</figcaption>

Apart from the external applications, the Scanner stack can also extract metadata from various applications & services of DataOS. The scanner job reads related metadata and pushes it to the metadata store through the Metis REST API server. You can then explore this information through the Metis UI.

The Scanner job connects with the following DataOS components and stores the extracted metadata to Metis DB:

- **Collation Service**: To scan and publish metadata related to data pipelines, including workflow information, execution history, and execution states. It also collects metadata for historical data such as pods and logs, as well as data processing stacks like Flare and Benthos, capturing job information and source-destination relationships.
- **Gateway Service**: To retrieve information from data profiles (descriptive statistics for datasets) and data quality tables (quality checks for your data along with their pass/fail status). It also scans data related to query usage, enabling insights into heavy datasets, popular datasets, and associations between datasets.
- **Heimdall**: To scan and retrieve information about users in the DataOS environment, including their descriptions and profile images. This user information is accessible through the Metis UI.
- **Pulsar** **Service**: To keep listening to the messages being published on it by various other services and stacks within the system.

Indexer service, a continuous running service within the DataOS environment keeps track of newly created or updated entities(datasets/topics/workflows, etc.). With this information about the changed entity, it creates a reconciliation Scanner YAML with filters to include only the affected entity. This Scanner workflow will extract the metadata about the entity and update the target metastore.
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

![Scanner YAML](./scanner/scanner_yaml.png)
<figcaption align = "center">Scanner YAML Components</figcaption>

Learn about the source connection and configuration options to create depot scan/non-depot scan workflow DAGs to scan entity metadata.

[Creating Scanner Workflows](scanner/creating_scanner_workflows.md)

## Attributes of Scanner Workflow

The below table summarizes various properties within a Scanner workflow YAML.

| Attribute                           | Data Type  | Default Value | Possible Value                                   | Requirement |
| ----------------------------------- | ---------- | ------------- | ----------------------------------------------- | ----------- |
| [`spec`](./field_ref/#spec)         | mapping    |               |                                                 | Mandatory    |
| [`stack`](./field_ref/#stack)       | string     |               | `scanner`                                       | Mandatory    |
| [`compute`](./field_ref/#compute)   | string     | `runnable-default` | `mycompute`                                 | Mandatory |
| [`runAsUser`](./field_ref/#runasuser)| string    |               | `metis`                                         | Mandatory    |
| [`depot`](./field_ref/#depot)       | string     |               | `dataos://icebase`                              | Mandatory    | in case of Depot scan only.
| [`type`](./field_ref/#type)         | string     | Source-specific | `bigquery`                                      | Mandatory    | In case of non-Depot scan
| [`source`](./field_ref/#source)     | string     |               | `bigquery_metasource`                           | Mandatory    | In case of non-Depot scan
| [`sourceConnection`](./field_ref/#sourceconnection) | mapping | |               | Mandatory    |
| [`type`](./field_ref/#type_1)       | string     | Source-specific | `BigQuery`                                      | Mandatory    | In case of non-Depot scan
| [`username`](./field_ref/#username) | string     | Source-specific | `projectID` `email` `hostport`                  | Mandatory    | In case of non-Depot scan
| [`sourceConfig`](./field_ref/#sourceconfig) | mapping | |               | Mandatory    |
| [`type`](./field_ref/#type_2)       | string     |               | `DatabaseMetadata`  `MessagingMetadata`        | Mandatory    | In case of non-Depot scan
| [`databaseFilterPattern`](./field_ref/#databasefilterpattern) | mapping | | | Mandatory    |
| [`includes/exclude`](./field_ref/#includes-or-excludes)| string | | `^SNOWFLAKE.*`                               | optional    | Applicable only in case of Database/Warehouse data source |
| [`schemaFilterPattern`](./field_ref/#schemafilterpattern) | mapping | | | Mandatory    |
| [`includes/excludes`](./field_ref/#includes-or-excludes_1) | string | | `^public$`                              | optional    | Applicable only in case of Database/Warehouse data source |
| [`tableFilterPattern`](./field_ref/#tablefilterpattern) | mapping | | | mandatory   |                                                       |
| [`includes/excludes`](./field_ref/#includes-or-excludes_2) | string | | `^public$`                              | optional    | Applicable only in case of Database/Warehouse data source |
| [`topicFilterPattern`](./field_ref/#topicfilterpattern) | mapping | | | Mandatory    |
| [`includes/excludes`](./field_ref/#includes-or-excludes_3)| string | | `foo` `bar`                               | optional    | Applicable only in case of Messaging data source     |
| [`includeViews`](./field_ref/#includeviews) | boolean | `false`       | `true` `false`                              | optional    | Applicable only in case of Database/Warehouse data source |
| [`markDeletedTables`](./field_ref/#markdeletedtables) | boolean | `false` | `true` `false`                            | optional    | Applicable only in case of Database/Warehouse data source |
| [`markDeletedTablesFromFilterOnly`](./field_ref/#markdeletedtablesfromfilteronly) | boolean | `false`  | `true` `false` | optional | Applicable only in case of Database/Warehouse data source |
| [`enableDebugLog`](./field_ref/#enabledebuglog) | boolean | `false` | `true` `false`                               | optional    | All                                                   |
| [`ingestSampleData`](./field_ref/#ingestsampledata) |  boolean | `false` | `true` `false`                             | optional    | Applicable only in case of Messaging data source       |
| [`markDeletedTopics`](./field_ref/#markdeletedtopics)| boolean | `false` | `true` `false`                            | optional    | Applicable only in case of Messaging data source       |

To learn more about these fields, their possible values, example usage, refer to [Attributes of Scanner YAML](scanner/field_ref.md).

### **Supported Data Sources**

Here you can find templates for the depot/non-depot Scanner workflows. 

[Databases and Warehouses](scanner/databases_and_warehouses.md)

[Messaging Services](scanner/messaging_services.md)

[Dashboard Services](scanner/dashboards.md)

<aside class="callout">
🗣 You can perform both depot scans and non-depot scans on all the data sources where you have established depots. The distinction lies in the fact that non-depot scans require you to furnish connection information and credentials within the Scanner YAML file. Whereas, for depot scans, you only need to provide the depot name or address.
</aside>

## System Scanner Workflows

The following workflows are running as system workflows to periodically scan the related metadata and save it to Metis DB to reflect the updated metadata state. They are scheduled to run at a set interval.

### **Data Profiling and Quality**

DataOS can leverage Scanner workflows to write jobs that could pull information from data profiles (descriptive statistics for the datasets) and data quality tables on an incremental basis and publish it to Metis DB.

[Data Profiling Scanner](scanner/data_profile_scan.md)

[Data Quality Scanner](scanner/data_quality_scan.md)

### **Pipelines/Workflows Data**

For metadata extraction related to data about workflows and resource consumption, the following workflow is scheduled.

[Workflows Data Scanner](scanner/workflows_data_scan.md)

### **Query History**

This Scanner workflow will ingest metadata related to query history. It scans information about queries, users, dates, and completion times. It connects with the Gateway service on a given cadence to fetch information about queries.

[Query Usage Scanner](scanner/query_usage_data_scan.md)

### **Users’ Information**

This workflow will scan the information about the users in DataOS. This is a scheduled workflow that connects with Heimdall on a given cadence to fetch information about users.

## Common Errors

[Common Scanner Errors](scanner/common_scanner_errors.md)