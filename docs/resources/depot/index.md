---
search:
  exclude: true
---

# Depot

Depot in DataOS is a [Resource](../resources.md) used to connect different data sources to DataOS by abstracting the complexities associated with the underlying source system (including protocols, credentials, and connection schemas). It enables users to establish connections and retrieve data from various data sources, such as file systems (e.g., AWS S3, Google GCS, Azure Blob Storage), data lake systems, database systems (e.g., Redshift, SnowflakeDB, Bigquery, Postgres), and event systems (e.g., Kafka, Pulsar) without moving the data. To understand the key characteristics of Depot, refer to the following link: [Core Concepts](/resources/depot/core_concepts/).

## First Steps

Depot Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/depot/first_steps/).

## Configuration

Depots can be configured to connect various data sources. The specific configurations may vary depending on the organization. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Depot manifest](/resources/depot/configuration/).

## Recipes

Below are some recipes to help you configure and utilize Depot effectively:

- [How to utilize Depots?](/resources/depot/how_to_guide/utilize_depot/)
- [Templates of Depot for different source systems](/resources/depot/how_to_guide/templates/)