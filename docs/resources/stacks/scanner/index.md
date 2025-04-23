---
title: Scanner Stack
search:
  boost: 2
---

# Scanner Stack

⁠The Scanner Stack in DataOS is a metadata extraction framework that ingests metadata from external source systems connected via Depot (RDBMS, cloud-based warehouses, etc.), and other DataOS components and Services.

The Scanner enables the extraction of both high-level metadata such as dataset or table names, ownership details, and tags and detailed information, including table schemas, column names, and descriptions (if available in the data). Additionally, it facilitates the retrieval of metadata related to data quality, profiling, query usage, and user information associated with data assets. The Scanner Stack  also integrates with dashboard and messaging services to collect relevant metadata. For dashboards, it retrieves information about dashboards, their elements, and associated data sources.

Within the DataOS ecosystem, the Scanner Stack collects metadata from Data Products and DataOS Resources, which provides comprehensive insights into inputs, outputs, service-level objectives (SLOs), data access permissions, and Infrastructure Resources used in the creation of Data Products. It also gathers metadata from various DataOS Resources, including [Workflows](/resources/workflow/), [Services](/resources/service/), [Clusters](/resources/cluster/), and [Depots](/resources/depot/), encompassing both historical runtime data and operational metrics.

⁠Designed for **Data Product Developers** (Data Engineers, Analytics Engineers), it enables flexible metadata scanning from target sources. Extracted metadata is stored in the **Metis Database** and can be explored using the **Metis UI**.

!!! tip  "**Scanner Stack in Data Product Lifecycle**"
    The Scanner Stack’s support for ontology and semantics. The stored metadata in MetisDB is used by various DataOS components for discoverability, governance and observability. External apps running on top of DataOS can also fetch this metadata via Metis server APIs help enhance discoverability of data that plays a crucial role in the Data Product Lifecycle, particularly in the Design and Build phases:

    - **Design**: Enables metadata ingestion from external source systems, helping identify and understand data products and assets, enhancing overall discoverability.
    - **Build**: The Scanner Stack supports ontology and semantics, ensuring that stored metadata in MetisDB enhances discoverability, governance, and observability across DataOS. External applications running on DataOS can access this metadata via Metis Server APIs. Heterogeneous datasets and data products can be easily explored in the Data Product Hub and Metis UI to streamline development.
    
## Capabilities of the Scanner Stack

* **Metadata Extraction from Data Assets:** Essential metadata is captured from datasets and tables stored in external source systems, including names, owners, tags, schemas, column details, and descriptions. Additionally, metadata such as data quality metrics, profiling insights, query usage, and user interactions is captured from internal sources, including data products, user information, and quality checks.

* **Integration with Dashboards and Messaging Services:** Extracts metadata from dashboards, including dashboard elements and associated data sources, along with relevant metadata from messaging services.

* **Comprehensive Data Product and DataOS Resource Metadata:** Retrieves metadata from DataOS Products and Resources, providing insights into inputs, outputs, Service Level Objectives (SLOs), Data Access Permissions, Infrastructure Resources, Workflows, Services, Clusters, Depots, and historical runtime and Operational data.


## Creating Scanner Workflow

A guide that explains the steps to create a Scanner Workflow to connect to the metadata source and extract the metadata of various entities. Visit [Quick Guide for Scanner](/resources/stacks/scanner/quickstart/) for more info.

## Supported Sources 

The Scanner Stack in DataOS supports three types of metadata extraction Workflows:

- **Data Sources:** Custom Scanner Workflows used to extract metadata from various external data sources(Snowflake, PostgreSQL, MySQL etc.) for discoverability and governance. Explore more about Data Source Scanners [here](/resources/stacks/scanner/supported_sources/data_sources/).  

- **System Sources:** Predefined, scheduled Workflows that scan internal system metadata at regular intervals. Explore more about system Scanner [here](/resources/stacks/scanner/supported_sources/system_metadata_sources/). 

- **Indexer Services:** Always-on service that detects changes in DataOS entities and triggers targeted metadata extraction for those specific changes. Explore more about Indexer Services Scanner [here](/resources/stacks/scanner/supported_sources/indexer_services/).

## Configuring the Scanner

For configuration of the Scanner Workflow and details on attributes in the Scanner manifest file, refer to the [Configuration Page](/resources/stacks/scanner/configurations/).

## Governing a Scanner

Access control for the Scanner Workflow is managed through Bifrost. Administrators may assign roles or define use cases to regulate permissions, including read, create, update, or delete, within specific workspaces. For additional information, refer to [Governance in Scanner](/resources/stacks/scanner/governance/).

## Cataloging

For guidance on metadata exploration and management for the Scanner Stack within the Metis UI, refer to the [Cataloging Page](/resources/stacks/scanner/cataloging/).

## Observability

Monitoring of the Scanner is supported through Monitor and Pager Resources. Step-by-step instructions are available [here](/resources/stacks/scanner/observability).

## Best Practices

A comprehensive guide on best practices for configuring and optimizing the Scanner Stack is available [here](/resources/stacks/scanner/best_practices).

## Recipes

To explore various Scanner execution scenarios and adapt its functionality to specific use cases, consult the [Recipes Page](/resources/stacks/scanner/recipes/).


## FAQ

- **What types of metadata can be extracted?**

    The Scanner Stack can extract general information about datasets/tables, such as names, owners, and tags, as well as detailed metadata like table schemas, column names, and descriptions.

- **What is the purpose of the Scanner job?**

    The Scanner job reads related metadata and pushes it to the metadata store through the Metis REST API server.

- **Dose Scanner Stack support Data Warehouses?**

    Yes, Scanner does support Data Warehouses such as Snowflake, Redshift, BigQuery and AzureSQL.

- **Can I scan description of the data from the data sources?**

    Yes, the Scanner can extract table and schema descriptions only if they preexist in the data source.

