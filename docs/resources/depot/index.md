---
search:
 exclude: true
---

# Depot

Depot in DataOS is a [Resource](../resources.md) used to connect different data sources to DataOS by abstracting the complexities associated with the underlying source system (including protocols, credentials, and connection schemas). It enables users to establish connections and retrieve data from various data sources, such as file systems (e.g., AWS S3, Google GCS, Azure Blob Storage), data lake systems, database systems (e.g., Redshift, SnowflakeDB, Bigquery, Postgres), and event systems (e.g., Kafka, Pulsar) without moving the data. To understand the key characteristics of Depot, refer to the following link: [Core Concepts](/resources/depot/core_concepts/).

!!!tip "Depot in the Data Product Lifecycle"

    In the Data Product Lifecycle, Depots play a crucial role in the **Desgin and Build Phase**, facilitating the seamless connection and integration of various data sources into the Data Product. Depots are particularly useful when your connection involves:

    - **Stable Integration Points**: Establishing a reliable connection to data sources that do not change frequently, ensuring data is consistently available. For example, a Depot connecting to a company's ERP system to continuously import transactional data into the data product. 
    - **Authentication and Security**: Managing secure connections to data sources by handling authentication, encryption, and other security measures. For example, a Depot can manage API keys or OAuth tokens to securely connect to external data services without exposing sensitive credentials.

    Depots ensure that the data product has a stable and consistent feed of data from various sources, enabling effective and efficient data processing in the subsequent **transformation phase**.

<center>
![Worker overview](/resources/worker/worker.png)
<i>Worker Resource in DataOS</i>
</center>

## First Steps

Depot Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/depot/first_steps/).

## Configuration

Depots can be configured to connect various data sources. The specific configurations may vary depending on the organization. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Depot manifest](/resources/depot/configuration/).

## Recipes

Below are some recipes to help you configure and utilize Depot effectively:

- [How to utilize Depots?](/resources/depot/how_to_guide/utilize_depot/)
- [Templates of Depot for different source systems](/resources/depot/how_to_guide/templates/)