---
title: Lens
search:
  boost: 4
---

# :resources-lens: Lens


Lens [Resource](/resources/) in DataOS is a logical modelling layer designed for accessing tabular data in data warehouses or lakehouses. It operates on top of physical tables, allowing the extension of these tables into logical tables by adding logical columns (measures) and relationships. It  empowers analytical engineers, the key architects of business intelligence, with a model-first approach.  To understand about the different elements of lens click [here](/resources/lens/concepts/). 


!!!tip "Lens within the Data Product Lifecycle"

    Lens operates within the consumption layer of the Data Product Life Cycle within DataOS, By leveraging Lens, Data Products can be created to inform decision-making, ensuring that data is logically organized and aligned with business objectives from the outset. To consume it, Lens exposes APIs such as JDBC, HTTP, and GraphQL.



<div style="text-align: center;">
    <img src="/resources/lens/lens_diagram.jpg" alt="Untitled(5)" style="max-width: 80%; height: auto; border: 1px solid #000;">
   <figcaption>Lens Ecosystem<figcaption>
</div>



**Why Lens?**

The data modeling layer serves as an interface that overlays the underlying data, consistently presenting business users with familiar and well-defined terms like "product," "customer," or "revenue." This abstraction enables users to access and consume data in a way that aligns with their understanding, facilitating self-service analytics and reducing dependence on data engineers for ad-hoc data requests. 

As a resource within the DataOS ecosystem, Lens enhances Data Product consumption by delivering improvements in how Data Products are accessed and utilized. It streamlines the developer experience in consumption patterns, focusing specifically on refining the use and interaction with data products.

## Key features of Lens 

Lens  is engineered to handle complex and large-scale data models with ease. Key features include:

- **Code modularity:** Lens supports modular code structures, simplifying the maintenance of extensive models, particularly when dealing with entities, dimensions, and measures. This modularity enables efficient development and management, allowing teams to navigate large codebases with reduced complexity.

- **Structured YAML templates:** Lens provides standardized, easy-to-customize YAML templates. These templates streamline the creation of Lens YAML files, ensuring consistency across models and reducing manual effort. They offer an efficient way to define tables, views, dimensions, measures, joins, and segments, allowing you to quickly set up and modify your data models with minimal hassle.

- **Local Development environment for model inspection and validation:** Lens features a [local development environment](/resources/lens/optimizing_lens_testing_in_local_development/) that supports real-time inspection and validation of models. This minimizes delays caused by SQL syntax errors, and the inclusion of a web app for model inspection allows issues to be identified and resolved before deployment.

- **Segments:** [Segments](/resources/lens/working_with_segments/) are predefined filters that enable the definition of complex filtering logic in SQL. They allow you to create specific subsets of data, such as users from a particular city, which can be reused across different queries and reports. This feature helps streamline the data exploration process by simplifying the creation of reusable filters.

- **API Support:** Lens enhances interoperability by simplifying application development with support for [Postgres API](/resources/lens/exploration_of_deployed_lens_using_sql_apis/), [REST API](/resources/lens/exploration_of_deployed_lens_using_rest_apis/), and [GraphQL](/resources/lens/exploration_of_deployed_lens_using_graphql/). Additionally, learn how to [work with payloads](/resources/lens/working_with_payload/) for querying and interacting with the system in the API Documentation.

- **Governance and Access Control:** Lens ensures data governance through[ user group management and data policies](/resources/lens/working_with_user_groups_and_data_policies/), enabling precise control over who can access and interact with data models. 

- **BI integration:** Lens improves interoperability through robust integration with Superset, Tableau and PowerBI. This ensures that data models can be easily utilized across various BI platforms, enhancing the overall analytics experience. For more details on BI integration, visit the [BI Integration Guide](/resources/lens/bi_integration/).


- **Performance optimization through Flash:** Designed to work with DataOS Lakehouse and Iceberg-format depots, [Flash](/resources/stacks/flash/) improves query performance by leveraging in-memory execution. This optimization ensures that data teams can efficiently handle large-scale queries with enhanced speed and performance.

## How to build Lens?

The process begins with creating a new Lens project and generating a data model. Once the model is prepared, it will be tested within the development environment to ensure it is error-free before deployment. 

#### **Lens model folder set-up**

The initial step involves setting up the folder structure for your Lens project. [This section](/resources/lens/lens_model_folder_setup/) will guide you through organizing your project files, including the model configuration files and necessary resources, in a structured and maintainable way.

#### **Develop Lens locally**

Before deploying your Lens models into the DataOS environment, you can build and test your models on your local system. [This guide](/resources/lens/optimizing_lens_testing_in_local_development/) includes the steps to develop and test Lens models locally, ensuring they function as intended.

#### **Develop Lens within DataOS**

[This section](/resources/lens/lens_deployment/) involves the step-by-step guide on building and deploying Lens models within the DataOS environment. You will learn how to use Lens to generate and deploy data models, making sure they integrate seamlessly with the broader DataOS ecosystem.

## Configurations

Lens can be configured to connect to different sources using data source attributes and configurable attributes in the `docker-compose.yml` or `lens.yml` manifest files. Here is a comprehensive guide to APIs and configuring supported properties.

- [Configuration Fields of the Deployment Manifest File (YAML) for Lens Resource](/resources/lens/lens_manifest_attributes/)
    Understand the various configuration fields available in the deployment manifest file for Lens resources.

- [Configuration Fields of the Docker Compose File](/resources/lens/docker_compose_manifest_attributes/)
    Review the configuration fields and settings in the Docker Compose file for orchestrating multi-container applications.


<aside class="callout">
If working with Lens 1.0 interface, click [here](/interfaces/lens/).
</aside>

<!-- - [Supported Data Sources](/resources/lens/data_sources/)
    Explore the list of data sources that are supported by our system. -->

<!-- - [BI Integration](/resources/lens/bi_integration/)
    Learn how to connect and integrate visualization tools with our system for effective data representation. -->

<!-- - [Working with Payload](/resources/lens/working_with_payload/)
    Learn how to work with payloads for querying and interacting with the system. -->

<!-- - [Working with User Groups and Data Policies](/resources/lens/working_with_user_groups_and_data_policies/)    
    Learn how to configure user groups and enforce data policies for secure and organized access to data resources. -->

<!-- - [Supported Parameters for Table & Views](/resources/lens/supported_parameters_for_tables_and_views/)
    Discover the parameters you can use for configuring tables and views in the system.
 -->

<!-- - [Supported Data Quality Checks](/resources/lens/supported_data_quality_checks/)
    Find information on the data quality checks supported by our system to ensure data accuracy and integrity. -->



## Exploration of deployed Lens

After creating a Lens data model, the next step is to explore it—this means interacting with the model by running queries. The following section explains the key concepts for querying Lens through various methods, though all queries follow the same general format. Multiple ways are available to explore or interact with the Lens model or its underlying data, allowing you to ask meaningful questions of the data and retrieve valuable insights. Exploration can be performed using the following methods:

- [Exploration of deployed Lens using SQL APIs](/resources/lens/exploration_of_deployed_lens_using_sql_apis/)

- [Exploration of deployed Lens using Python](/resources/lens/exploration_of_deployed_lens_using_python/)

- [Exploration of deployed Lens using Rest APIs](/resources/lens/exploration_of_deployed_lens_using_rest_apis/)

- [Exploration of deployed Lens using GraphQL](/resources/lens/exploration_of_deployed_lens_using_graphql/)


## Data modelling

[Data modeling](/resources/lens/overview/) is the process of defining and structuring raw data into organized and meaningful business definitions. It involves creating logical schemas, relationships, and aggregations to represent how data is stored, processed, and accessed. Effective data modeling ensures optimal performance for queries and allows users to extract valuable insights without modifying the underlying data structure. Below are resources to guide you through essential aspects of data modeling to optimize performance and accuracy.

  - [Data modelling concepts:](/resources/lens/concepts/)
    Understand the core principles and methodologies essential for designing effective data models.

  - [Best practices:](/resources/lens/best_practices/)
    Explore recommended guidelines and techniques to create efficient and scalable data models.

  - [Do's and don'ts:](/resources/lens/dos_and_donts/)
    A concise list of actions to follow and pitfalls to avoid when designing your data model.

  - [Error reference:](/resources/lens/errors/)
    A quick reference for understanding and resolving common errors in data modeling.
    
  <!-- - [Working with Segments](/resources/lens/working_with_segments/) 
    Learn how to create and manage data segments to improve query performance and user experience. -->

  <!-- - [Supported Parameters for Tables and Views](/resources/lens/supported_parameters_for_tables_and_views/)
    Understand the role of logical tables and views in data models. -->


## Optimizing Lens model

The Lens semantic layer provides several optimization techniques that can significantly enhance the performance of data queries. The following page explores best practices and strategies for fine-tuning your Lens model to maximize efficiency. 

[Optimizing Lens model: Best practices for the Semantic Layer](/resources/lens/fine_tuning_a_lens_model/)



