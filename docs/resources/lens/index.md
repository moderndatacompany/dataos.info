---
title: Lens
search:
  boost: 4
---

# :resources-lens: Lens

Lens is a data product consumption layer designed for accessing tabular data in data warehouses or lakehouses. It operates on top of physical tables, allowing the extension of these tables into Logical Tables by adding logical columns (measures) and relationships. Lens exposes APIs such as JDBC, HTTP, and GraphQL for accessing modified data.

It is intended strictly for direct data consumption and should not be used as a layer for building additional microservices.

It  empowers analytical engineers, the key architects of business intelligence, with a model-first approach. By leveraging Lens , data products can be created to inform decision-making, ensuring that data is logically organized and aligned with business objectives from the outset. To understand about the Model-first approach click [here](/resources/lens/core_concepts/).

As a core resource within the DataOS ecosystem, Lens  enhances the entire data product lifecycle, delivering substantial improvements in developer experience, consumption patterns, and overall data management.

> The data modeling layer serves as an interface that overlays the underlying data, consistently presenting business users with familiar and well-defined terms like "product," "customer," or "revenue." This abstraction enables users to access and consume data in a way that aligns with their understanding, facilitating self-service analytics and reducing dependence on data engineers for ad-hoc data requests. 

<div style="text-align: center;">
    <img src="/resources/lens/lens_diagram.jpg" alt="Untitled(5)" style="max-width: 80%; height: auto; border: 1px solid #000;">
   <figcaption>Lens Ecosystem<figcaption>
</div>

                                                    
## Key features of Lens 

Lens  is engineered to handle complex and large-scale data models with ease. Key features include:

- **Code Modularity**

  Lens supports modular code structures, simplifying the maintenance of extensive models, particularly when dealing with entities, dimensions, and measures. This modularity enables efficient development and management, allowing teams to navigate large codebases with reduced complexity.

- **YAML Template Generation**

  Lens offers a tailored YAML template generator through its VS Code plugin, streamlining the creation of Lens YAML files. This feature reduces manual effort, ensuring consistency across models and speeding up the setup process.

- **Advanced Linter Capabilities**

  With enhanced linter functionalities, Lens provides more accurate and relevant error detection during deployment. Developers can quickly identify and resolve issues, reducing time spent on troubleshooting non-essential errors.

- **Real-time Verification and Validation**

  Lens features a local development environment that supports real-time inspection and validation of models. This minimizes delays caused by SQL syntax errors, and the inclusion of a web app for model inspection allows issues to be identified and resolved before deployment.

- **Customizable Views**

  Lens enables users to create customizable views, allowing for multiple data slices tailored to specific business needs. These views can be easily edited, queried, and integrated with BI tools, offering greater flexibility in data analysis and reporting.

- **Interoperability**

Lens is designed for seamless integration with external applications and tools, enhancing interoperability across various systems:

  - **API Support:** Lens simplifies application development with support for Postgres API, REST API, and GraphQL, enabling smoother interactions with external systems.

  - **First-Class BI Integration:** Lens offers robust integration with Superset, and ongoing efforts aim to extend connectivity to Tableau and PowerBI. This integration ensures that data models can be easily utilized across various BI platforms, improving the overall analytics experience.

**Performance Optimization**

Lens is optimized to deliver high performance, especially when dealing with large datasets:

  - **Flash:** Designed to work with DataOS Lakehouse and Iceberg-format depots, Flash improves query performance by leveraging DuckDB for in-memory execution. This optimization ensures that data teams can efficiently handle large-scale queries with enhanced speed and performance.

## Lens Set-up

**Pre-requisites**

Before setting up Lens, ensure you have the following dependencies installed on your system:

1. Docker  (Docker to run Lens in an isolated environment on our local system)
2. Docker-compose  (Lens leverages Docker Compose for configuring multi-container Docker applications)
3. Postman App/Postman VSCode Extension (For querying and testing lens)
4. VS Code (Code editor to build Lens Model YAMLs)
5. VS Code Plugin (This is optional. It will aid in creating Lens views and tables)

To install the above prerequisites, refer to the detailed doc [here](/resources/lens/installing_prerequisites/).


If you are familiar with how to set up and run a Lens Project and you have an existing Lens Model that you want to run, directly [jump to this step](/resources/lens/#getting-started-with-lens)


## Getting Started with Lens

Once you've completed the prerequisite setup, proceed to the next step.

We’ll start by creating a new Lens project and generating a data model. Once the model is ready, we’ll test it in our development environment itself to ensure it is error-free before using it.

This guide will walk you through the following tasks:

[Lens set-up](/resources/lens/lens_setup/).

## Configurations

Lens is configured via [environment variables](/resources/lens/data_sources/) and configurating attributes in a configuration file of `docker-compose.yml` or `lens.yml`. Usually, both would be used to configure Lens deployment.Here is a comprehensive guide to APIs and configuring supported properties.

- [Supported Data Sources](/resources/lens/data_sources/)
    Explore the list of data sources that are supported by our system.

- [BI Integration](/resources/lens/bi_integration/)
    Learn how to connect and integrate visualization tools with our system for effective data representation.

- [Configuration Fields of the Deployment Manifest File (YAML) for Lens Resource](/resources/lens/lens_manifest_attributes/)
    Understand the various configuration fields available in the deployment manifest file for Lens resources.

- [Configuration Fields of the Docker Compose File](/resources/lens/docker_compose_manifest_attributes/)
    Review the configuration fields and settings in the Docker Compose file for orchestrating multi-container applications.

- [Working with Payload](/resources/lens/working_with_payload/)
    Learn how to work with payloads for querying and interacting with the system.

- [Supported Data Quality Checks](/resources/lens/supported_data_quality_checks/)
    Find information on the data quality checks supported by our system to ensure data accuracy and integrity.

- [Supported Parameters for Table & Views](/resources/lens/supported_parameters_for_tables_and_views/)
    Discover the parameters you can use for configuring tables and views in the system.


## Consumption of Deployed Lens

After creating a Lens data model, you would like to ask questions to it, i.e., run queries against this data model. The following pages describes the common concepts of querying Lens through different ways. Although, All queries share the same query format.

We have various ways to consume or interact with our newly created Lens or data model.

The consumption can be done using following ways:

- [Consumption of Lens using Iris Dashboard](/resources/lens/consumption_using_iris_dashboard/)

- [Consumption of Lens using SQL APIs](/resources/lens/consumption_using_sql_apis/)

- [Consumption of Lens using REST APIs](/resources/lens/consumption_using_rest_apis/)

- [Consumption of Lens using Python](/resources/lens/consumption_using_python/)








