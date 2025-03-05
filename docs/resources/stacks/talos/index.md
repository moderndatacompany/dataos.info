---
title: Talos Stack
search:
  boost: 4
---

# Talos Stack

Talos is a <span title="Stack is a DataOS Resource that acts as an execution engine and an extension point for integrating new programming paradigms within the platform.">
  <a href="/resources/stacks/">Stack</a>
</span> within DataOS designed to facilitate the development of robust and scalable data APIs (RESTful APIs) using SQL templates.
 It enables the integration of logic and transformation within SQL templates, streamlining the creation and management of APIs. This approach enhances the efficiency of API development and integration into various applications and AI agents.

Talos provides functionality for filtering data from the data warehouse, validating API parameters, and handling errors. It ensures data accuracy and integrity while delivering advanced analytics capabilities to users.

By converting SQL into APIs efficiently, Talos accelerates the deployment of data-driven solutions.

!!!tip "Talos within the Data Product Life Cycle"
    Talos operates within the consumption layer of the Data Product Life Cycle in DataOS, specifically managing tabular data stored in data lakehouses. It optimizes data access and usability for various consumers, including external systems, applications, and end-users.

    Talos API endpoints provide a standardized and flexible interface for querying and consuming Data Products through APIs. This capability is particularly useful when working with tabular data, as it allows users to execute SQL queries across one or multiple Data Products and expose the results as REST APIs. This approach enables seamless integration and data retrieval outside the DataOS environment.



## **Why Talos?**

The rapid growth of data presents challenges for data professionals in efficiently sharing data with stakeholders for operational business use cases. Traditional methods for creating APIs require complex and manual processes which complicates the integration of databases and data warehouses with AI agents and applications.

### **Conventional Methods and Challenges**

- **Custom API Development:** Developing APIs traditionally involves extensive manual coding, which is resource-intensive, particularly for complex systems or when integrating multiple data sources. Manual development increases the risk of bugs and errors, potentially affecting API reliability and efficiency.

- **Integration Complexity:** Integrating data from diverse sources with varying formats and protocols requires significant expertise. The lack of standardized conventions leads to inconsistencies in API interactions, complicating integration with AI systems.

- **Security and Compliance:** Ensuring API security and compliance with regulations such as GDPR or HIPAA necessitates robust authentication, authorization, and encryption. As security and compliance requirements evolve, APIs must be continuously updated and maintained to remain compliant.

- **Scalability and Performance:** Custom APIs are often not designed with scalability in mind, leading to performance issues as data volumes or user demand increases. Achieving optimal scalability and performance requires considerable development resources and infrastructure.

- **Documentation and Usability:** Comprehensive documentation is essential for making APIs understandable and usable by developers and AI systems. However, inadequate documentation can hinder effective integration and usage, increasing the complexity of implementation.

### **Features of Talos**

Talos utilizes Heimdall for authentication and employs SQL templates for streamlined query execution, ensuring secure, efficient, and reliable API services. Its RESTful architecture facilitates seamless integration, while automated documentation generation and observability features enhance development efficiency and maintainability.

- **Rapid development and integration:** 
    By abstracting the complexities of directly interacting with databases and data warehouses, developers can focus on the higher-level logic of their applications. This reduces the development time and simplifies the process of integrating AI capabilities into applications.

- **API documentation and standardization:** 
    Utilizing [OpenAPI documents](/resources/stacks/talos/recipes/api_documentation/) for interaction provides a standardized way for AI agents to understand and interact with different APIs. This promotes interoperability among various systems and tools, making it easier to integrate with a wide array of services and data sources.

- **Scalability and maintenance:** 
    A template-driven approach to API creation can make it easier to scale and maintain APIs over time. Changes in the underlying data schema or business logic can be propagated to the APIs more efficiently, without the need for extensive manual adjustments.

- **Accessibility:**
    Enhancing data accessibility for AI agents through well-defined APIs enables the integration of machine learning and analytics, facilitating improved decision-making and task automation.

- **Validating API parameters:** 
    Talos provides functionality for [validating and sanitizing API parameters](/resources/stacks/talos/recipes/validating_parameters/), ensuring that input data meets required criteria. This reduces the risk of incorrect or malicious requests.

- **Data security:** 
    Talos implements [data masking](/resources/stacks/talos/recipes/data_masking/) within SQL templates to protect sensitive information. By obscuring or anonymizing confidential data, it enables secure dataset sharing while maintaining data privacy. This approach mitigates the risk of unauthorized exposure and ensures compliance with security standards.

- **Data governance:** 
    Talos provides comprehensive [data governance](/resources/stacks/talos/recipes/data_governance/) by enabling precise control over data access through Heimdall authentication and user groups. User groups facilitate role-based organization, managing access to API scopes and enforcing data policies. By assigning specific permissions and data access rights, Talos ensures that only authorized users can access datasets. This approach streamlines security policy enforcement and compliance, maintaining data integrity and confidentiality across access levels.

- **Error handling:** 
    Talos provides effective [error handling](/resources/stacks/talos/recipes/error_handling/) by stopping further execution and generating an error code when a problem is encountered during SQL template processing. This method prevents the return of potentially inaccurate or incomplete results and ensures that users receive clear feedback for troubleshooting. By halting execution and reporting specific error codes, Talos helps maintain the reliability and accuracy of API responses.

- **Caching datasets:** 
    To enhance query performance and reduce the strain on data sources, Talos includes a [dataset caching](/resources/stacks/talos/recipes/caching/) feature. This functionality stores and reuses intermediate query results, leading to faster API response times. By minimizing the need for repetitive queries, caching improves overall efficiency and ensures more responsive and effective data retrieval.

- **Observability and monitoring:** 
    Observability involves analyzing detailed metrics to understand your APIs' internal state, while monitoring ensures optimal performance by providing real-time updates on API metrics through the [“/metrics”](/resources/stacks/talos/recipes/monitoring/) endpoint. This real-time data helps maintain accuracy, validate data, and handle errors, facilitating rapid development and integration into applications and AI agents.

## Data sources supported by Talos

Talos offers extensive compatibility with a range of popular data sources, ensuring flexibility and seamless integration. The supported sources include [Lens](/resources/lens/), [Flash](/resources/stacks/flash/), along with [Depot](/resources/depot/) of MySQL, Snowflake, Postgres, Redshift and others.

<center>
  <img src="/resources/stacks/talos/flowchart.jpg" alt="Talos" style="width:40rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Talos Stack</i></figcaption>
</center>

<aside class="callout">
🗣 Talos does not directly support Icebase Depots. However, <span title="Flash is a Stack designed to manage and control query costs and performance within DataOS. It achieves this by caching datasets using an in-memory query processing layer."> <a href="/resources/stacks/flash/">Flash</a> 
</span> can be used as a data source to build APIs for data stored in Icebase.
</aside>


## **Building APIs with Talos**

Talos provides the tools and capabilities required to streamline API development and deployment within DataOS. This ensures efficient, scalable processes for building and managing APIs. The following sections outline the steps for setting up Talos both within DataOS and in a local environment.

### **Developing APIs**

[This section](/resources/stacks/talos/set_up/) provides a step-by-step guide for building and deploying APIs within DataOS using Talos. Talos is orchestrated by the <span title="A Service represents a long-running process that acts as a receiver and/or provider of APIs."><a href="/resources/service/">Service Resource</a>
</span> to automate and streamline API creation, ensuring seamless integration and management within the DataOS ecosystem. 

### **Configurations**

Effective configuration of Talos requires an understanding of the attributes within its manifest files. [This section](/resources/stacks/talos/configurations/) provides detailed descriptions of key configuration files used in Talos, enabling proper setup and customization.


## Recipes

This section provides step-by-step guides to assist you in effectively configuring Talos to solve common challenges. Below are some recipes to help you configure Talos effectively:

- [How to set up Talos for Lens?](/resources/stacks/talos/recipes/lens_setup/)
- [How to set up Talos for Flash?](/resources/stacks/talos/recipes/flash_setup/)
- [How to set up Talos for MySQL?](/resources/stacks/talos/recipes/mysql/)
- [How to set up Talos for Redshift?](/resources/stacks/talos/recipes/redshift/)
- [How to set up Talos for Snowflake?](/resources/stacks/talos/recipes/snowflake/)
- [How to set up Talos for Postgres?](/resources/stacks/talos/recipes/postgres/)
- [How to apply data masking while exposing data through an API?](/resources/stacks/talos/recipes/data_masking/)
- [How to use external API as a data source?](/resources/stacks/talos/recipes/external_api/)
- [How to fetch data exposed by Talos from the third-party tools?](/resources/stacks/talos/recipes/external_tools/)
- [How to apply Caching in Talos?](/resources/stacks/talos/recipes/caching/)
- [How to generate the comprehensive API documentation?](/resources/stacks/talos/recipes/api_documentation/)

## **APIs in action: Exploring Talos use cases**

This section involves the practical, real-world scenarios demonstrating how to consume the data with Talos effectively.

- [Covid-19](/resources/stacks/talos/example/)

You can refer to the recipes section for more examples.

## Best practices

When developing data APIs with Talos, following best practices is crucial for securing sensitive information and ensuring efficient operation. These practices encompass both API design and SQL usage.

- [API Best Practices](/resources/stacks/talos/best_practices/api/)
- [SQL Best Practices](/resources/stacks/talos/best_practices/sql/)


