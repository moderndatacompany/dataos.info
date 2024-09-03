# Talos

Talos is a [Stack](/resources/stacks/) within DataOS designed to streamline the creation of data APIs ( [RESTful APIs](https://www.redhat.com/en/topics/api/what-is-a-rest-api) ), facilitating seamless access to data from diverse sources such as databases, data warehouses, and data lakes. By simplifying the process of writing and managing database queries, Talos enables rapid development and integration of APIs into various applications and AI agents. 

*It turns your SQL into APIs in no time!*

!!!tip "Talos within the Data Product Life Cycle"
    Talos operates within the consumption layer of the Data Product Life Cycle within DataOS, facilitating access and usability for consumers, whether they are external systems, applications, or end-users. The Talos API endpoints are crucial in this process, offering a standardized and flexible interface for accessing and consuming Data Products via APIs. Talos is particularly valuable when Data Products need to be accessed or consumed outside the DataOS environment via API.



## Why Talos?

Given the vast amount of analytical data in databases, data warehouses, and data lakes, sharing data with stakeholders for operational business use cases is challenging. Traditional custom API development is time-consuming, error-prone, and complex, with significant integration, security, scalability, and documentation issues.

Talos simplifies this process by providing a standardized framework for creating APIs, reducing development time and integration complexity. It leverages OpenAPI for standardization, ensures scalability and ease of maintenance, and enhances data accessibility for AI agents. This streamlines API creation promotes interoperability, and improves data interaction and decision-making capabilities.

## Features of Talos

To fully utilize the capabilities of Talos, it is essential to familiarize yourself with the available features and functionalities. Here's a brief overview of the key features:

- **Rapid API Development:** Talos transforms your SQL queries into APIs swiftly, allowing developers to focus on higher-level application logic rather than manual API coding. Talos utilizes [SQL templates](/resources/stacks/talos/set_up/) to streamline API creation, reducing development time and complexity.

- **Enhanced Performance:** Talos employs in-memory database as a [caching layer](/resources/stacks/talos/recipes/caching/) to enhance query speed and minimize API response times, ensuring a more efficient interaction with data sources.

- **Scalability and Maintenance:** A structured, template-driven approach makes it easier to scale and maintain APIs, adapting to changes in data schemas or business logic with minimal manual intervention.

- **Standardization and Integration:** Leverages OpenAPI for standardized [API interaction](/resources/stacks/talos/recipes/recipe9/), promoting interoperability and ease of integration with various systems and tools.

- **Accessibility and Usability:** Facilitates secure and scalable data sharing, making data more accessible to AI agents and other applications such as Appsmith.

- **Advanced Error Handling and Data Privacy:** Includes strategies for handling errors, such as invalid parameters or missing data, to ensure robust API performance. Implements practices for safeguarding personal and sensitive data, adhering to privacy regulations and standards.

- **Local Execution and Docker Integration:** Simplified [local setup](/resources/stacks/talos/local_set_up/) with make start and Docker Compose integration for easier development and testing of Talos.


## How does Talos work?

By leveraging Hemidall for authentication, Flash for caching, and SQL templates for simple query execution, Talos ensures secure, efficient, and reliable API services. Its RESTful architecture, automated documentation generation, and observability features simplify development and integration.

<center>
  <img src="/resources/stacks/talos/chart.jpg" alt="Talos" style="width:40rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Talos Framework</i></figcaption>
</center>


### **Build**

Talos streamlines the process of creating robust and scalable Data APIs by utilizing SQL templates. Users can connect to various data sources and define their data logic through these templates, which encapsulate complex queries and transformations in a simplified manner. This phase involves writing and organizing SQL templates that serve as the backbone of the APIs, validating API parameters, handling errors, and implementing caching strategies to optimize data retrieval and processing.

### **Accelerate**

Talos focuses on optimizing the performance of the APIs. It enhances query performance through efficient SQL construction and caching, ensuring rapid response times even with large datasets. Talos supports scalability by enabling easy adjustments to handle increased data volume or request load. Integrations with tools like dbt and language models from Hugging Face further streamline query generation and development, helping to maintain high performance and efficiency.

### **Share**

Talos enhances the accessibility and usability of the Data APIs created. It provides features for generating detailed API documentation, which includes descriptions of endpoints, parameters, and response formats, ensuring that users and stakeholders can easily understand and utilize the APIs.

## How to set up Talos?

Talos provides the necessary tools and capabilities to streamline API development and deployment within DataOS, ensuring that your processes are efficient and scalable. In the following sections, you'll find detailed instructions on how to set up Talos within DataOS and locally, tailored to fit your specific needs.

### **Setting up Talos within DataOS**

Setting up Talos within DataOS involves configuring it to align with the existing API management practices. This setup ensures that Talos operates seamlessly within your DataOS environment. For step-by-step instructions, [please refer to this guide](/resources/stacks/talos/set_up/).

### **Setting up Talos locally**

For the users, who prefer or need to run Talos on their local machines, this setup provides flexibility and control over your development environment. Setting up Talos locally is perfect for users who are in the early stages of API development. This method ensures that you can build and test your APIs in a familiar environment before deploying them to a broader audience. To set up Talos locally, [please refer to this](/resources/stacks/talos/local_set_up/).

## Configurations
To configure Talos effectively, it's essential to understand each attribute of the manifest files. This section provides detailed descriptions of the key configuration files used in Talos, helping you set up and customize Talos efficiently. For detailed information on each file, please refer to [this section](/resources/stacks/talos/configurations/).


## Recipes

This section provides step-by-step guides to assist you in effectively configuring the Talos to solve common challenges. Below are some recipes to help you configure Talos effectively:

- [How to set up Talos for Lens?](/resources/stacks/talos/recipes/lens_setup/)
- [How to set up Talos for Flash?](/resources/stacks/talos/recipes/flash_setup/)
- [How to set up Talos for Redshift?](/resources/stacks/talos/recipes/redshift/)
- [How to set up Talos for Snowflake?](/resources/stacks/talos/recipes/snowflake/)
- [How to set up Talos for Postgres?](/resources/stacks/talos/recipes/postgres/)
- [How to apply data masking while exposing data through an API?](/resources/stacks/talos/recipes/data_masking/)
- [How to use external API as a data source?](/resources/stacks/talos/recipes/external_api/)
- [How to fetch data exposed by Talos from the third-party tools?](/resources/stacks/talos/external_tools/)
- [Caching Datasets](/resources/stacks/talos/recipes/caching/)
- [How to generate the comprehensive API documentation?](/resources/stacks/talos/recipes/api_documentation/)

## Example

This section provides practical, real-world scenarios demonstrating how to develop a Data Product effectively. Below are some examples to help you to understand the Data Product:

- [Covid-19](/resources/stacks/talos/example/)

You can refer to the recipes section for more examples.

## Best Practices

When developing data APIs with Talos, following best practices is crucial for securing sensitive information and ensuring efficient operation. These practices encompass both API design and SQL usage.

- [API Best Practices](/resources/stacks/talos/best_practices/api/)
- [SQL Best Practices](/resources/stacks/talos/best_practices/sql/)