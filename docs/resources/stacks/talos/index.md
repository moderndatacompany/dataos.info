---
title: Talos
search:
  boost: 4
---

# Talos

Talos is a [Stack](/resources/stacks/) within DataOS that empowers you to build robust and scalable data APIs ([RESTful APIs](https://www.redhat.com/en/topics/api/what-is-a-rest-api)) using SQL templates. In Talos, you can combine logic and transformation within [SQL templates](/resources/stacks/talos/set_up/#writing-sql-templates), which helps you create APIs more efficiently.
By simplifying the process of writing and managing database queries, Talos enables rapid development and integration of APIs into various applications and AI agents. 

Talos allows you to filter data from the data warehouse, perform data validation on API parameters, and handle errors. It makes the process flexible and straightforward, ensuring the accuracy and integrity of your data while delivering powerful analytics capabilities to users.

*It turns your SQL into APIs in no time!*

!!!tip "Talos within the Data Product Life Cycle"
    Talos functions within the consumption layer of the Data Product Life Cycle in DataOS, specifically designed to handle tabular data stored in data lakehouses. It enhances access and usability for consumers, including external systems, applications, and end-users. The Talos API endpoints are vital in this framework, providing a standardized and flexible interface for querying and consuming Data Products via APIs. Talos is especially valuable when working with tabular data, as it allows users to write SQL queries across one or multiple Data Products and expose the results as REST APIs, facilitating seamless integration and data retrieval outside the DataOS environment.



## Why Talos?

Nowadays data is growing at the speed of light, currently, data professionals do not have any better ways to share data with respective stakeholders for operational business use cases.

Developers today must undertake a more manual and more complex process to streamline the creation of APIs for AI agents and apps to interact with databases and data warehouses.

### **Conventional Methods and Challenges**

**Custom API Development**

- **Time-Consuming:** Developing APIs requires extensive manual coding, which can be particularly labor-intensive for complex systems or when integrating various data sources.
- **Error-Prone:** Manual coding introduces a higher likelihood of bugs and errors, potentially impacting the API’s reliability and efficiency.

**Integration Complexity**

- **Diverse Data Sources:** Combining data from various sources with different formats and protocols demands significant expertise and effort.
- **Lack of Standardization:** The absence of a unified approach means that APIs might use different conventions, complicating consistent interaction for AI systems.

**Security and Compliance**

- **Security Risks:** Protecting APIs from security threats and ensuring compliance with regulations such as GDPR or HIPAA involves additional measures, including robust authentication, authorization, and encryption.
- **Maintenance Overhead:** Security and compliance standards can change, requiring ongoing updates and maintenance of APIs to stay compliant.

**Scalability and Performance**

- **Scalability Concerns:** Custom APIs may not always be designed with scalability in mind, which can lead to performance issues as demand or data volume increases.
- **Resource Intensive:** Achieving optimal performance and scalability often demands substantial development resources and infrastructure.

**Documentation and Usability**

- **Lack of Documentation:** Effective documentation is crucial for making APIs understandable and usable by other developers or AI systems, but it can sometimes be inadequately addressed.
- **Usability Issues:** Without thorough and clear documentation, integrating and using APIs becomes more challenging for others.

### **Discover What Talos Can Do for You**

By leveraging Heimdall for authentication and [SQL templates](/resources/stacks/talos/set_up/#writing-sql-templates) for simple query execution, Talos ensures secure, efficient, and reliable API services. Its RESTful architecture, automated documentation generation, and observability features simplify development and integration.


<center>
  <img src="/resources/stacks/talos/flowchart.jpg" alt="Talos" style="width:40rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Talos Stack</i></figcaption>
</center>


**Rapid Development and Integration**

By abstracting the complexities of directly interacting with databases and data warehouses, developers can focus on the higher-level logic of their applications. This reduces the development time and simplifies the process of integrating AI capabilities into applications.

**API Documentation and Standardization**

Utilizing [OpenAPI documents](/resources/stacks/talos/recipes/api_documentation/) for interaction provides a standardized way for AI agents to understand and interact with different APIs. This promotes interoperability among various systems and tools, making it easier to integrate with a wide array of services and data sources.

**Scalability and Maintenance**

A template-driven approach to API creation can make it easier to scale and maintain APIs over time. Changes in the underlying data schema or business logic can be propagated to the APIs more efficiently, without the need for extensive manual adjustments.

**Accessibility**

Making data more accessible to AI agents through well-defined APIs can unlock new insights and capabilities by leveraging machine learning and analytics. This can enhance decision-making processes and automate routine tasks, among other benefits.

**Validating API Parameters**

Talos allows you to [validate and sanitize](/resources/stacks/talos/recipes/validating_parameters/) API parameters in Talos. This feature ensures that the input data is validated and meets the required criteria, reducing the risk of incorrect or malicious requests.

**Data Security**

Talos utilizes [data masking](/resources/stacks/talos/recipes/data_masking/) within SQL templates to ensure sensitive information is protected. By obscuring or anonymizing confidential data, Talos allows for the secure sharing and use of datasets while maintaining data privacy. This approach helps prevent unauthorized exposure of sensitive information, ensuring that security and compliance standards are upheld.

**Data Governance**

Talos provides comprehensive [data governance](/resources/stacks/talos/recipes/data_governance/) feature by enabling precise control over data access through Heimdall authentication and user groups. User groups allow you to organize individuals based on their roles, facilitating the management of access to various API scopes and the application of data policies. By assigning specific permissions and data access rights to different user groups, Talos ensures that only authorized users can access the datasets. This approach streamlines the enforcement of security policies and compliance requirements, maintaining data integrity and confidentiality across different levels of access.

**Error Handling**

Talos provides effective [error handling](/resources/stacks/talos/recipes/error_handling/) by stopping further execution and generating an error code when a problem is encountered during SQL template processing. This method prevents the return of potentially inaccurate or incomplete results and ensures that users receive clear feedback for troubleshooting. By halting execution and reporting specific error codes, Talos helps maintain the reliability and accuracy of API responses.

**Caching Datasets**

To enhance query performance and reduce the strain on data sources, Talos includes a [dataset caching](/resources/stacks/talos/recipes/caching/) feature. This functionality stores and reuses intermediate query results, leading to faster API response times. By minimizing the need for repetitive queries, caching improves overall efficiency and ensures more responsive and effective data retrieval.

**Observability and Monitoring**

observability involves analyzing detailed metrics to understand your APIs' internal state, while [monitoring](/resources/stacks/talos/recipes/monitoring/) ensures optimal performance by providing real-time updates on API metrics through the /metrics endpoint. This real-time data helps maintain accuracy, validate data, and handle errors, facilitating rapid development and integration into applications and AI agents.

## Data Sources supported by Talos

Talos offers extensive compatibility with a range of popular data sources, ensuring flexibility and ease of integration for your data needs such as BigQuery, Snowflake, Postgres, Redshift, and Depot of type BigQuery, Snowflake, Postgres, and Redshift.


## **How to Build APIs?**

Talos provides the necessary tools and capabilities to streamline API development and deployment within DataOS, ensuring that your processes are efficient and scalable. In the following sections, you'll find detailed instructions on how to set up Talos within DataOS and locally, tailored to fit your specific needs.

### **How to Build APIs Locally?**

Before deploying your APIs into the DataOS environment you can build and test your APIs on your local system. [This guide]() includes the steps to build APIs locally using Talos. 

### **How to Build APIs within DataOS?**

[This section](/resources/stacks/talos/set_up/) involves the step-by-step guide on building and deploying APIs within DataOS using Talos. Talos is orchestrated by the [Service Resource](https://dataos.info/resources/service/) to streamline the API creation.

## Configurations
To configure Talos effectively, it's essential to understand each attribute of the manifest files. This section provides detailed descriptions of the key configuration files used in Talos, helping you set up and customize Talos efficiently. For detailed information on each file, please refer to [this section](/resources/stacks/talos/configurations/).


## Recipes

This section provides step-by-step guides to assist you in effectively configuring Talos to solve common challenges. Below are some recipes to help you configure Talos effectively:

- [How to set up Talos for Lens?](/resources/stacks/talos/recipes/lens_setup/)
- [How to set up Talos for Flash?](/resources/stacks/talos/recipes/flash_setup/)
- [How to set up Talos for Redshift?](/resources/stacks/talos/recipes/redshift/)
- [How to set up Talos for Snowflake?](/resources/stacks/talos/recipes/snowflake/)
- [How to set up Talos for Postgres?](/resources/stacks/talos/recipes/postgres/)
- [How to apply data masking while exposing data through an API?](/resources/stacks/talos/recipes/data_masking/)
- [How to use external API as a data source?](/resources/stacks/talos/recipes/external_api/)
- [How to fetch data exposed by Talos from the third-party tools?](/resources/stacks/talos/recipes/external_tools/)
- [Caching Datasets](/resources/stacks/talos/recipes/caching/)
- [How to generate the comprehensive API documentation?](/resources/stacks/talos/recipes/api_documentation/)

## **APIs in action: Exploring Talos use cases**

This section involves the practical, real-world scenarios demonstrating how to consume the data with Talos effectively. Below are some examples to help you to understand Talos effectively:

- [Covid-19](/resources/stacks/talos/example/)

You can refer to the recipes section for more examples.

## Best Practices

When developing data APIs with Talos, following best practices is crucial for securing sensitive information and ensuring efficient operation. These practices encompass both API design and SQL usage.

- [API Best Practices](/resources/stacks/talos/best_practices/api/)
- [SQL Best Practices](/resources/stacks/talos/best_practices/sql/)


