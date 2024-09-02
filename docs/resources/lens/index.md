---
title: Lens
search:
  boost: 4
---

# Lens

Lens  is a logical modeling layer designed to empower analytical engineers, the key architects of business intelligence, with a model-first approach. By leveraging Lens , data products can be created to inform decision-making, ensuring that data is logically organized and aligned with business objectives from the outset. To understand about the Model-first approach click [here](/resources/lens/core_concepts/).

As a core resource within the DataOS ecosystem, Lens  enhances the entire data product lifecycle, delivering substantial improvements in developer experience, consumption patterns, and overall data management.

> The data modeling layer serves as an interface that overlays the underlying data, consistently presenting business users with familiar and well-defined terms like "product," "customer," or "revenue." This abstraction enables users to access and consume data in a way that aligns with their understanding, facilitating self-service analytics and reducing dependence on data engineers for ad-hoc data requests. 

<div style="text-align: center;">
    <img src="/resources/lens/lens_diagram.jpg" alt="Untitled(5)" style="max-width: 100%; height: auto; border: 1px solid #000;">
   <figcaption>Lens Ecosystem<figcaption>
</div>

                                                    
## Key features of Lens 

Lens  is engineered to handle complex and large-scale data models with ease. Key features include:

- **Code Modularity:** The platform supports modular code structures, simplifying the maintenance of extensive models, especially when dealing with entities, dimensions, and measures. This modularity facilitates efficient development and management, enabling teams to navigate large codebases without unnecessary complexity.

- **YAML Template Generation:** Lens  offers a tailored template generator through its VS Code plugin, streamlining the creation of Lens YAML files. This enhancement reduces the manual effort involved in setting up and ensures consistency across models.

- **Advanced Linter Capabilities:** With refined linter functionalities, Lens  provides more relevant and precise error detection during deployment. This improvement helps developers address issues more effectively, reducing the time spent troubleshooting generic or irrelevant errors.

- **Real-time Verification and Validation:** A local development environment in Lens  enables real-time inspection and validation of models, minimizing the back-and-forth often associated with SQL syntax errors. The inclusion of a web app for model inspection further enhances the development process, ensuring that issues are identified and resolved before deployment.

- **Customizable Views:** Lens  introduces customizable views, allowing users to create multiple data slices tailored to their specific business needs. These views can be easily edited, queried, and seamlessly integrated with BI tools, offering greater flexibility in data analysis and reporting.

### **Interoperability**

Lens  is designed to work seamlessly with external applications and tools, making it easier to integrate with existing workflows:

- **API Support:** With the addition of Postgres API, Rest API, and GraphQL support, Lens  simplifies application development, enabling smoother interactions with external systems.

- **First-Class BI Integration:** Lens  offers robust integration with Superset, with ongoing efforts to extend this seamless connectivity to Tableau and PowerBI. This integration ensures that data models can be effectively utilized across various BI platforms, enhancing the overall analytics experience.

### **Performance**

Lens  is optimized for performance, particularly when working with large datasets:

- **Flash:**  Designed to work with DataOS Lakehouse and Iceberg-format depots. Flash enhances query performance by leveraging DuckDB for in-memory execution which further boosts performance, ensuring that data teams can handle large-scale queries with improved efficiency and speed.

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

[**Lens set-up**](/resources/lens/lens_setup/).

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

After creating a Lens data model, you would like to ask questions to it, i.e., run queries against this data model. [This page](/resources/lens/consumption_of_deployed_lens/) describes the common concepts of querying Lens through different ways.

All queries share the same query format.

# Consumping Deployed Lens

We have various ways to consume or interact with our newly created Lens or data model. All queries share the same query format.

The consumption can be done using following ways:

- [Consumption of Lens using Iris Dashboard](/resources/lens/consumption_using_iris_dashboard)

- [Consumption of Lens using SQL APIs](/resources/lens/consumption_using_sql_apis/)

- [Consumption of Lens using REST APIs](/resources/lens/consumption_using_rest_apis/)

- [Consumption of Lens using Python](/resources/lens/consumption_of_deployed_lens/consumption_using_python/)








