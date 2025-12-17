---
title: Nilus Stack
search:
  boost: 4
---

# Nilus Stack

Nilus functions as the data movement stack within DataOS. It provides a lightweight and extensible architecture designed for production-grade data pipelines. Nilus supports both [Batch]("Batch data ingestion is the process of collecting and transferring large volumes of data at scheduled intervals from a source system into a data warehouse, data lake, or lakehouse.") data ingestion and real-time [Change Data Capture(CDC)]("Change Data Capture (CDC) is a method used to identify and propagate row-level changes—such as inserts, updates, and deletes—from a source database to a target system.") from various data sources. The framework enables declarative, reliable, and seamless [Batch](/resources/stacks/nilus/batch_sources/) and [CDC](/resources/stacks/nilus/cdc_sources/) data movement from external source systems into [supported destination](/resources/stacks/nilus/supported_destinations/) systems.

!!! tip "Nilus within the Data Product Lifecycle"

    Nilus operates at the initial stage of the Data Product lifecycle, facilitating the ingestion of raw data from external systems into the destination. Once ingested, the data becomes the foundation for downstream processing.

    - Downstream processing includes data transformation, policy-driven governance (via DataOS), and consumption by applications/analytical tools.
    - Standardizing and unifying the ingestion process accelerates the integration of new data sources and improves data product development efficiency. 
    - Nilus plays a key role in streamlining ingestion and supporting data product development.

## Key Features

The diagram below highlights the core features that empower flexible and reliable data ingestion in Nilus:

<figure>
  <img src="/resources/stacks/nilus/images/nilu-key-feature.avif" style="width:40rem;" />
  <figcaption><i>Key Features of Nilus</i></figcaption>
</figure>


## Why Nilus?

Nilus is designed as a lightweight, extensible, and API-centric ingestion framework optimized for modern data platform needs. Its design prioritizes simplicity, interoperability, and developer productivity, making it suitable for diverse ingestion scenarios across batch and real-time workloads.

- **Lightweight Runtime Architecture**

    Nilus operates without reliance on heavyweight distributed computing frameworks such as Apache Spark or Kafka. Instead, ingestion logic is implemented through minimal-dependency Python or JVM-based applications. This design choice significantly reduces operational complexity and infrastructure footprint.

- **Accelerated Source Onboarding**

    Custom data source connectors can be defined in Python and deployed rapidly. Most new connectors can be developed, tested, and onboarded within one week, enabling teams to respond quickly to changing ingestion requirements.

- **Unified Support for Batch and CDC**

    Nilus supports both scheduled batch jobs and real-time data ingestion using change data capture (CDC) patterns, including Write-Ahead Logging (WAL)-based techniques. This dual-mode support ensures compatibility with both periodic and event-driven ingestion use cases.

- **Extensibility and Maintainability**

    The framework's plugin-based architecture encourages modular development. Each connector or ingestion job operates independently, facilitating easy updates, testing, and debugging. This results in lower maintenance overhead and higher reliability.

- **Strategic Value**

    By combining a minimal operational footprint with extensible design and broad integration capabilities, Nilus reduces total cost of ownership (TCO) while unlocking advanced use cases across operational analytics, machine learning pipelines, and real-time observability.

## Setting Up Nilus 

Set up Nilus to enable seamless data movement across DataOS. Deploy the Nilus Server (backed by PostgreSQL) and the Nilus Stack to orchestrate pipelines, manage metadata, and support both batch and CDC workloads.

[**Get started with Nilus Setup →**](/resources/stacks/nilus/set_up/)


## Choosing Between CDC and Batch

Since Nilus supports both CDC and Batch ingestion modes, selecting the appropriate one depends on your specific data requirements, latency tolerances, and the capabilities of your source system. The following key considerations can help determine whether CDC or Batch ingestion best suits your use case.

| **Criterion**            | **Use CDC**                                                  | **Use Batch**                                                    |
| -------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| **Data freshness**   | Near real-time or frequent updates are required          | Periodic updates (daily/hourly) are sufficient               |
| **Data volume**      | Only a small portion of data changes                     | Large portions of data change or full reloads are acceptable |
| **Source impact**    | Minimal impact on source system is required              | Source can tolerate heavy queries during scheduled windows   |
| **Downstream needs** | Consumers need change history or event-level detail      | Consumers only need latest state snapshots                   |
| **Cost/complexity**  | Higher infrastructure cost and complexity are acceptable | Lower cost and simpler setup is preferred                    |

### **Start using Nilus**

To begin ingesting data using Nilus, refer to the appropriate quick-start guide based on the ingestion mode required.

1. [Nilus CDC Workflow](/resources/stacks/nilus/quick_start/#change-data-capture-cdc)
2. [Nilus Batch Workflow](/resources/stacks/nilus/quick_start/#batch-ingestion)


### **Data Masking in Nilus**

Data masking replaces or transforms sensitive values with non-sensitive equivalents. This technique enables Nilus users to safeguard sensitive information during data ingestion while maintaining its structural integrity and analytical utility.

[**Get started with Data Masking in Nilus →**](/resources/stacks/nilus/data_masking/)


Data masking is required when handling production-grade data in non-production, shared, or compliance-sensitive environments.

## Source and Destination

Nilus supports a variety of databases, warehouses, and lakehouses as both sources and destinations, which are as follows:

* [Supported Batch Sources](/resources/stacks/nilus/batch_sources/)
* [Supported CDC Sources](/resources/stacks/nilus/cdc_sources/)
* [Supported Destinations](/resources/stacks/nilus/supported_destinations/)

## API Data Ingestion

!!! tip "Ingest Data from Any API"
    **Need to ingest data from REST APIs, GraphQL endpoints, or custom APIs?** Nilus makes it easy!
    
    While Nilus includes built-in connectors for popular APIs like Google Analytics, Salesforce, and Stripe, you can ingest data from any API using our powerful [Custom Source](/resources/stacks/nilus/batch_sources/custom_source/) feature.
    
    **Common API Integration Use Cases:**
    
    * **REST APIs** - CRM systems, marketing platforms, payment gateways
    * **GraphQL APIs** - Modern application APIs and data services
    * **Internal APIs** - Company-specific microservices and applications
    * **Webhook endpoints** - Real-time event streaming from external systems
    * **Third-party SaaS platforms** - Any service with API access
    
    **Key Benefits:**
    
    * Write simple Python code to connect to any API endpoint
    * Automatic incremental loading with state tracking
    * Built-in retry logic and error handling
    * Flexible authentication support (API keys, OAuth, custom headers)
    * Deploy in minutes using Git repository integration
    
    [**Get started with Custom Sources →**](/resources/stacks/nilus/batch_sources/custom_source/)


## Special Characters in Credentials

Nilus supports the use of special characters in connection credentials across all major sources and destinations.

**Supported Characters:** `@ : / ? # & = + ; % \ ' { } ( ) * $ !`


!!! info
    When connection credentials include special characters, the `--disable-interpolation` flag must be used while applying `instance-secrets`, or `secrets`. This ensures the special characters are preserved accurately.

**Example:**  

```bash
dataos-ctl resource apply -f ${{/config/instance-secret.yml}} --disable-interpolation
```

The table below outlines the current compatibility of special character handling across supported sources and destinations.

| **Source**    | **Batch Source** | **CDC Source** | **Destination** | **Comments**                                                                                                                              |
| ------------- | ---------------- | -------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| MS SQL Server | ✅                | ✅              | ✅               |                                                                                                                                           |
| PostgreSQL    | ✅                | ✅              | ✅               |                                                                                                                                           |
| MongoDB       | ✅                | ✅              | ✅               |                                                                                                                                           |
| MySQL         | ✅                | ✅              | ✅               |                                                                                                                                           |
| Redshift      | ✅                | 🚫             | ✅               | The source system does not support `'`, `"`, `\`, `/`, or `@` in credentials. This is a source-side limitation and not governed by Nilus. |
| Snowflake     | ✅                | 🚫             | ✅               |                                                                                                                                           |
| Clickhouse    | ✅                | 🚫             | ❌               | Support for special characters in connection credentials for Clickhouse as a destination is not available in the current release.         |
| Azure Synapse | ✅                | 🚫             | 🚫              |                                                                                                                                           |

**Legend:**

* ✅ — Supported
* ❌ — Not supported (Planned for future releases)
* 🚫 — Not applicable
