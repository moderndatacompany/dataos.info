# Talos

Talos is a [Stack](/resources/stacks/) within DataOS that aims to help data developers deliver [RESTful APIs](https://www.redhat.com/en/topics/api/what-is-a-rest-api) from various data sources like databases, data warehouses, and data lakes. It simplifies how you write database queries and works well with standard methods for creating APIs, allowing developers to quickly build APIs for AI agents, applications, and other data-driven solutions.

*It turns your SQL into APIs in no time!*

!!!tip "Talos within the Data Product Life-cycle"
    Talos operates within the consumption layer of the Data Product Life Cycle within DataOS, facilitating access and usability for consumers, whether they are external systems, applications, or end-users. The Talos API endpoints are crucial in this process, offering a standardized and flexible interface for accessing and consuming Data Products via API. Talos is particularly valuable when Data Products need to be accessed or consumed outside the DataOS environment via API.


<div style="text-align: center;">
  <img src="/resources/stacks/talos/flowchart.jpg" style="border:1px solid black; width: 60%; height: auto;">
</div>


## Why Talos?

Given the vast amount of analytical data in databases, data warehouses, and data lakes, sharing data with stakeholders for operational business use cases is challenging. Traditional custom API development is time-consuming, error-prone, and complex, with significant integration, security, scalability, and documentation issues.

Talos simplifies this process by providing a standardized framework for creating APIs, reducing development time and integration complexity. It leverages OpenAPI for standardization, ensures scalability and ease of maintenance, and enhances data accessibility for AI agents. This streamlines API creation promotes interoperability, and improves data interaction and decision-making capabilities.

## Features of Talos

To fully utilize the capabilities of Talos, it is essential to familiarize yourself with the available features and functionalities. Here's a brief overview of the key features:

- **Rapid API Development:** Talos transforms your SQL queries into APIs swiftly, allowing developers to focus on higher-level application logic rather than manual API coding. Talos utilizes [SQL templates](/resources/stacks/talos/set_up/) to streamline API creation, reducing development time and complexity.

- **Enhanced Performance:** Talos employs in-memory database as a caching layer to enhance query speed and minimize API response times, ensuring a more efficient interaction with data sources.

- **Scalability and Maintenance:** A structured, template-driven approach makes it easier to scale and maintain APIs, adapting to changes in data schemas or business logic with minimal manual intervention.

- **Standardization and Integration:** Leverages OpenAPI for standardized API interaction, promoting interoperability and ease of integration with various systems and tools.

- **Accessibility and Usability:** Facilitates secure and scalable data sharing, making data more accessible to AI agents and other applications such as Appsmith.

- **Advanced Error Handling and Data Privacy:** Includes strategies for handling errors, such as invalid parameters or missing data, to ensure robust API performance. Implements practices for safeguarding personal and sensitive data, adhering to privacy regulations and standards.

- **Local Execution and Docker Integration:** Simplified [local setup](/resources/stacks/talos/local_set_up/) with make start and Docker Compose integration for easier development and testing of Talos.


## How does Talos work?

### **Build**

Talos allows you to insert variables into your templated SQL. It accepts input from your API and generates SQL statements on the fly.

### **Accelerate**

Talos uses DuckDB as a caching layer, boosting query speed and reducing API response time. This means faster, smoother data APIs for you and less strain on your data sources.

### **Share**

Talos offers many data-sharing options, seamlessly integrating your data into familiar applications within your workflow and building AI agents.

## How to set up Talos?

Talos provides the necessary tools and capabilities to streamline API development and deployment within DataOS, ensuring that your processes are efficient and scalable. In the following sections, you'll find detailed instructions on how to set up Talos within DataOS and locally, tailored to fit your specific needs.

### **Setting up Talos within DataOS**

Setting up Talos within DataOS involves configuring it to align with the existing API management practices. This setup ensures that Talos operates seamlessly within your DataOS environment. For step-by-step instructions, [please refer to this guide](/resources/stacks/talos/set_up/).

### **Setting up Talos locally**

For the users, who prefer or need to run Talos on their local machines, this setup provides flexibility and control over your development environment. Setting up Talos locally is perfect for users who are in the early stages of API development. This method ensures that you can build and test your APIs in a familiar environment before deploying them to a broader audience. To set up Talos locally, [please refer to this](/resources/stacks/talos/local_set_up/).

## Configurations
To configure Talos effectively, it's essential to understand each attribute of the manifest files. This section provides detailed descriptions of the key configuration files used in Talos, helping you set up and customize Talos efficiently. For detailed information on each file, please refer to [this section](/resources/stacks/talos/configuration/).


## Recipes

This section provides step-by-step guides to assist you in effectively configuring the Talos to solve common challenges. Below are some recipes to help you configure Talos effectively:

- [How to set up Talos for Lens?](/resources/stacks/talos/recipes/recipe1/)
- [How to set up Talos for Flash?](/resources/stacks/talos/recipes/recipe2/)
- [How to set up Talos for Redshift?](/resources/stacks/talos/recipes/recipe3/)
- [How to set up Talos for Snowflake?](/resources/stacks/talos/recipes/recipe4/)
- [How to set up Talos for Postgres?](/resources/stacks/talos/recipes/recipe5/)
- [How to apply data masking while exposing data through an API?](/resources/stacks/talos/recipes/recipe6/)
- [How to use external API as a data source?](/resources/stacks/talos/recipes/recipe7/)

## Example

This section provides practical, real-world scenarios demonstrating how to develop a Data Product effectively. Below are some examples to help you to understand the Data Product:

- [Covid-19](/resources/stacks/talos/example/)

You can refer to the recipes section for more examples.

## Best Practices

When developing data APIs with Talos, following best practices is crucial for securing sensitive information and ensuring efficient operation. These practices encompass both API design and SQL usage.

- [API Best Practices](/resources/stacks/talos/best_practices/api/)
- [SQL Best Practices](/resources/stacks/talos/best_practices/sql/)