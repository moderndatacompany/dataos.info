# Talos

Talos is a [stack](/resources/stacks/) within DataOS that aims to help data developers deliver [RESTful APIs](https://www.redhat.com/en/topics/api/what-is-a-rest-api) from various data sources like databases, data warehouses, and data lakes. It simplifies how you write database queries and works well with standard methods for creating APIs, allowing developers to quickly build APIs for AI agents, applications, and other data-driven solutions.

*It turns your SQL into APIs in no time!*

![talos_new.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/6d23cea7-9cde-4bc5-b57b-5d8045dac3af/talos_new.jpg)

## Why Talos?

Given the vast amount of analytical data in databases, data warehouses, and data lakes, sharing data with stakeholders for operational business use cases is challenging. Traditional custom API development is time-consuming, error-prone, and complex, with significant integration, security, scalability, and documentation issues.

Talos simplifies this process by providing a standardized framework for creating APIs, reducing development time and integration complexity. It leverages OpenAPI for standardization, ensures scalability and ease of maintenance, and enhances data accessibility for AI agents. This streamlines API creation promotes interoperability, and improves data interaction and decision-making capabilities.

## Features of Talos

To fully utilize the capabilities of Talos, it is essential to familiarize yourself with the available features and functionalities. Here's a brief overview of the key features:

### **Building Data API**

- Talos supports various data sources such as Snowflake, Redshift, Postgre, BigQuery, [Depot](/resources/depot/) (Snowflake, Redshift, Postgre, BigQuery), Lens, and Flash.
- Leverage the power of SQL templates to encapsulate your logic and transformations. Discover how to structure and write SQL templates that serve as the foundation for your data APIs, enabling you to manipulate and transform data easily.
- Explore techniques for caching datasets in Talos to optimize query performance and reduce the load on data sources. This feature lets you store and reuse intermediate results, improving overall API response times.
- Learn how to handle errors effectively in Talos. This section guides you through error handling strategies, including throwing errors when parameters are invalid or missing data.
- Discover how to validate and sanitize API parameters in Talos. This feature ensures the input data is validated and meets the required criteria, reducing the risk of incorrect or malicious requests.
- Explore the mechanisms and practices for handling data privacy in Talos. It encompasses practices and measures implemented to safeguard personal, confidential, or regulated information from unauthorized access, misuse, or disclosure.

### **API Catalog & Documentation**

- **API Catalog:** Learn how to create an API catalog with Talos, which provides a centralized repository for all your data APIs. This catalog enables easy discovery, management, and sharing of APIs within your organization.
- **API Documentation:** Understand how to generate comprehensive API documentation (OpenAPI Specification) with Talos, including endpoints, parameters, response formats, and examples.

### **API Configuration**

Discover the extensibility of Talos through API plugins. This section explains how to leverage pre-built plugins to enhance the functionality of your Data APIs, including Response Format, Pagination, CORS, Rate Limit, and Access Log.

### **Deployment and Maintenance**

Understand the deployment and maintenance considerations for Talos in a production environment. This section covers topics such as packaging and deploying your APIs.

## How does Talos work?

### **Build**

Talos offers a development experience similar to DBT. Just insert variables into your templated SQL. Talos accepts input from your API and generates SQL statements on the fly.

### **Accelerate**

Talos uses DuckDB as a caching layer, boosting query speed and reducing API response time. This means faster, smoother data APIs for you and less strain on your data sources.

### **Share**

Talos offers many data-sharing options, seamlessly integrating your data into familiar applications within your workflow and building AI agents.

## Setting up Talos within DataOS

This section will guide you through setting up the Talos within DataOS to help you build your API efficiently. To set up Talos, [please refer to this](/resources/stacks/talos/set_up/).

## Setting up Talos locally

This section will guide you through setting up the Talos locally to help you build your API efficiently. To set up Talos, [please refer to this](/resources/stacks/talos/local_set_up/).

## Configurations

This section describes each attribute of the manifest files of Talos to help you configure Talos efficiently. Please follow the below links:

- [`config.yaml`](/resources/stacks/talos/configurations/config/)
- [`docker-compose.yaml`](/resources/stacks/talos/configurations/docker_compose/)
- [`apis`](/resources/stacks/talos/configurations/apis/)
- [`service.yaml`](/resources/stacks/talos/configurations/service/)

## Recipes

This section provides step-by-step guides to assist you in effectively configuring the Talos to solve common challenges. Below are some recipes to help you configure Talos effectively:

- [How to set up Talos for Lens?](/resources/stacks/talos/recipes/recipe1/)
- [How to set up Talos for Flash?](/resources/stacks/talos/recipes/recipe2/)
- [How to set up Talos for Redshift?](/resources/stacks/talos/recipes/recipe3/)
- [How to set up Talos for Snowflake?](/resources/stacks/talos/recipes/recipe4/)
- [How to set up Talos for Postgres?](/resources/stacks/talos/recipes/recipe5/)
- [How to apply data masking while exposing data through an API?](/resources/stacks/talos/recipes/recipe6/)
- [How to use external API as a data source?](/resources/stacks/talos/recipes/recipe7/)
- [How to fetch data exposed by Talos from the third-party tools?](/resources/stacks/talos/recipes/recipe8/)

## Example

This section provides practical, real-world scenarios demonstrating how to develop a Data Product effectively. Below are some examples to help you to understand the Data Product:

- [Covid-19](/resources/stacks/talos/example/)

## Best Practices

When utilizing Talos to develop data APIs, ensuring best practices is paramount to safeguarding sensitive information. Here are essential best practices to consider:

- [API Best Practices](/resources/stacks/talos/best_practices/api/)
- [SQL Best Practices](/resources/stacks/talos/best_practices/sql/)