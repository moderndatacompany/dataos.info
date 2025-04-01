---
title: Lens
search:
  boost: 4
---

# :resources-lens: Lens


Lens [Resource](/resources/) in DataOS is a logical modeling layer designed for accessing tabular data in data warehouses or lakehouses. It operates on top of physical tables, allowing the extension of these tables into logical tables by adding logical columns (measures) and relationships. It  empowers analytical engineers, the key architects of business intelligence, with a model-first approach. 


!!!tip "Lens within the Data Product Lifecycle"

    Lens operates in the consumption layer of the Data Product Life Cycle within DataOS. By leveraging Lens, Data Products can be created to inform decision-making, ensuring data is well-organized and aligned with business objectives. To consume it, Lens exposes APIs such as Postgres, REST APIs, and GraphQL.



<div style="text-align: center;">
    <img src="/resources/lens/lens_diagram.jpg" alt="Untitled(5)" style="max-width: 80%; height: auto; border: 1px solid #000;">
   <figcaption>Lens Ecosystem</figcaption>
</div>


**Why Lens?**

The data modeling layer serves as an interface that overlays the underlying data, consistently presenting business users with familiar and well-defined terms like `product`, `customer`, or `revenue`. This abstraction enables users to access and consume data in a way that aligns with their understanding, facilitating self-service analytics and reducing dependence on data engineers for ad-hoc data requests. 

As a Resource within the DataOS ecosystem, Lens enhances Data Product consumption by delivering improvements in how Data Products are accessed and utilized. It streamlines the developer experience in consumption patterns, focusing specifically on refining the use and interaction with data products.

## Key features of Lens 

Lens  is engineered to handle complex and large-scale data models with ease. Key features include:

- **Code modularity:** Lens supports modular code structures, simplifying the maintenance of extensive models, particularly when dealing with entities, dimensions, and measures. This modularity enables efficient development and management, allowing teams to navigate large codebases with reduced complexity.

- **Structured YAML templates:** Lens provides standardized, easy-to-customize YAML templates. These templates streamline the creation of Lens YAML files, ensuring consistency across models and reducing manual effort. They offer an efficient way to define tables, views, dimensions, measures, joins, and segments, allowing you to quickly set up and modify your data models with minimal hassle.

- **Segments:** [Segments](/resources/lens/segments/) are predefined filters that enable the definition of complex filtering logic in SQL. They allow you to create specific subsets of data, such as users from a particular city, which can be reused across different queries and reports. This feature helps streamline the data exploration process by simplifying the creation of reusable filters.

- **API support:** Lens enhances interoperability by simplifying application development with support for [Postgres API](/resources/lens/exploration_of_lens_using_sql_apis/), [REST API](/resources/lens/exploration_of_lens_using_rest_apis/), and [GraphQL](/resources/lens/graphql_api/graphql_query_example/). Additionally, learn how to [work with payloads](/resources/lens/working_with_payload/) for querying and interacting with the system in the API Documentation.

- **Governance and access control:** Lens ensures data governance through[ user group management and data policies](/resources/lens/user_groups_and_data_policies/), enabling precise control over who can access and interact with data models. 

- **BI Integration:** Lens improves interoperability through robust integration with Superset, Tableau and PowerBI. This ensures that data models can be easily utilized across various BI platforms, enhancing the overall analytics experience. For more details on BI integration, visit the [BI Integration Guide](/resources/lens/bi_integration/).

- **Performance optimization through Flash:** Designed to work with DataOS Lakehouse and Iceberg-format depots, [Flash](/resources/stacks/flash/) improves query performance by leveraging in-memory execution. This optimization ensures that data teams can efficiently handle large-scale queries with enhanced speed and performance.

## How to build Lens?

To build a semantic model with Lens establish a connection to your data source, load relevant data, set up user access, and deploy the model with configuration settings. The following steps outline how to build the semantic model and deploy it using Lens for each type of source.

### **Single source**

- [AWS Redshift](/resources/lens/data_sources/awsredshift/)

- [Bigquery](/resources/lens/data_sources/bigquery/)

- [Postgres](/resources/lens/data_sources/postgres/)

- [Snowflake](/resources/lens/data_sources/snowflake/)

### **Multiple source**

- [Minerva](/resources/lens/data_sources/minerva/)

- [Themis](/resources/lens/data_sources/themis/)

### **Query accelaration**

- [Flash](/resources/lens/data_sources/flash/)

<!-- ### **Lens model folder set-up**

The initial step involves setting up the folder structure for your Lens project. [This section](/resources/lens/lens_model_folder_setup/) will guide you through organizing your project files, including the model configuration files and necessary resources, in a structured and maintainable way.

### **Develop Lens within DataOS**

[This section](/resources/lens/lens_deployment/) involves the step-by-step guide on building and deploying Lens models within the DataOS environment. You will learn how to use Lens to generate and deploy semantic models, making sure they integrate seamlessly with the broader DataOS ecosystem. -->

## Exploration of semantic model

After creating a semantic model, the next step is to explore it by running queries. This section covers key concepts for querying Lens through various methods, all following the same general format. Multiple methods are available to interact with the Lens model or its data, enabling to ask questions and gain insights.

### **BI Integration**

- [Power BI Desktop](/resources/lens/bi_integration/powerbi/)

- [Power BI Service](/resources/lens/bi_integration/powerbi_service/)

- [Superset](/resources/lens/bi_integration/superset/)

- [Tableau](/resources/lens/bi_integration/tableau/)

### **GraphQL APIs**

GraphQL API enables Lens to deliver data over the HTTP protocol to GraphQL enabled data applications, e.g., most commonly, front-end applications. The following resources provide detailed instructions on how to interact with the Lens GraphQL API:

- To explore the Lens using the GraphQL API click [here](/resources/lens/exploration_of_lens_using_graphql/).
- To learn about the query format for GraphQL and explore more examples click [here](/resources/lens/graphql_api/graphql_query_example/).

### **Python**

Lens supports interaction through Python, allowing one to use libraries such as requests for making API calls and handling responses programmatically. This method is ideal for more complex queries and automation tasks. For detailed instructions on setting up and using Python with Lens click [here](/resources/lens/exploration_of_lens_using_python/).

### **SQL APIs**

Lens provides a PostgreSQL-compatible interface, enabling users to interact with the semantic model over SQL. The following resources offer detailed instructions on how to set up and use the SQL APIs with Lens:

- To explore how to interact with Lens using SQL APIs, click [here](/resources/lens/sql_apis/supported_functions_and_operators/).
- To learn about the supported functions and operators within the SQL API, click [here](/resources/lens/sql_apis/supported_functions_and_operators/).

### **REST APIs**

Lens offers a REST API for querying data, retrieving metadata, and managing resources programmatically. To know step-by-step guidance on interacting with Lens through API calls, details of available endpoints, parameters, and request-response formats please refer to this [link](/resources/lens/exploration_of_lens_using_rest_apis/).


### **Python**

Lens supports interaction through Python, allowing one to use libraries such as requests for making API calls and handling responses programmatically. This method is ideal for more complex queries and automation tasks. For detailed instructions on setting up and using Python with Lens, refer to the full Python guide [here](/resources/lens/exploration_of_lens_using_python/).

## Semantic modeling

Semantic modeling is the process of organizing raw data into meaningful business definitions. It involves creating schemas, relationships, and aggregations to represent how data is stored, processed, and accessed. Navigate through the following documents to explore the concepts involved in creating a semantic model in Lens:

- [Key concepts](/resources/lens/concepts/)
- [Working with segments](/resources/lens/segments/)
- [Working with views](/resources/lens/views/)
- [Working with user groups and data policies](/resources/lens/user_groups_and_data_policies/)


## Configurations

Lens can be configured to connect to different sources using data source attributes and configurable attributes in the deployment.yml manifest files. For a comprehensive guide to configure supported properties, click [here](/resources/lens/lens_manifest_attributes/).

<!-- - [Configuration Fields of the Docker Compose File](/resources/lens/docker_compose_manifest_attributes/)
    Review the configuration fields and settings in the Docker Compose file for orchestrating multi-container applications. -->

<aside class="callout">
🗣️ If working with Lens 1.0 interface, click <a href="/interfaces/lens/">here</a>.
</aside>


## Best Practices

Click [here](/resources/lens/best_practices/) to explore recommended guidelines and techniques to create efficient and scalable semantic models, along with a concise list of do’s and don’ts.

## Troubleshooting

Click [here](/resources/lens/errors/) to understand and resolve common errors while creating semantic model and deploying Lens.


## Cataloging

Click [here](/resources/lens/cataloging/) to learn about how the metadata of a semantic model or Lens Resource is cataloged and can easily be discovered.


## Governance

Click [here](/resources/lens/governance/) to learn how data governance in DataOS is structured across four different layers.


## Observability

Click [here](/resources/lens/observability/) to learn how to observe and monitor Lens Resource and semantic model.

## Optimizing Lens semantic model

The Lens semantic layer provides several optimization techniques that can significantly enhance the performance of data queries. The following page explores best practices and strategies for fine-tuning your Lens model to maximize efficiency. 

- [Optimizing semantic model layer](/resources/lens/fine_tuning_a_lens_model/)

- [Best practices for efficient query processing in Lens](/resources/lens/best_practices_for_solution_designing/)