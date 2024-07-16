# Data Product

!!!info "Overview"

    This documentation is intended to provide structured information essential for understanding the Data Product's purpose, functionality, and operational aspects. This documentation is crucial for both technical teams and stakeholders to ensure clarity, consistency, and effective management throughout the lifecycle of the Data Product.

## Introduction

A Data Product is a self-contained unit within DataOS designed for handling and sharing analytical data, developed and managed by the dedicated teams. It includes meta data, data transformation code, input and output definitions, discovery and observability, APIs, documentation, service level objectives (SLOs), governance, transformation and platform dependencies such as compute and storage resources. Data Product is reusable, composable, portable and cloud-agnostic.​


DataOS provides a platform to develop, manage, process, and operationalize Data Products across the organization. It serves as a foundational layer that enables the effective handling of Data Products throughout its life-cycle, from ingestion and storage to analysis and delivery. By offering a cohesive environment for managing Data Products, DataOS supports better decision-making and operational efficiency.


> A Data Product is an integrated and self-contained combination of data, metadata, semantics and templates. It includes access and logic-certified implementation for tackling specific data and analytics (D&A) scenarios and reuse. A data product must be consumption-ready (trusted by consumers), up to date (by engineering teams) and approved for use (governed). Data products enable various D&A use cases, such as data
sharing, data monetization, analytics and application integration. 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **-** Gartner<sup>&reg;</sup><span class="circle"></span>

<img src="/products/data_product/diagram.jpg" alt="Description" width="1500">

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **How to develop a Data Product?**

    ---

    Learn how to develop and manage a Data Product within DataOS.

    [:octicons-arrow-right-24: Data Product Development Lifecycle](/products/data_product/#data-product-development-life-cycle)


-   :material-list-box-outline:{ .lg .middle } **How to configure the manifest file of a Data Product?**

    ---

    Discover how to configure the manifest file of a Data Product and its components.

    [:octicons-arrow-right-24: Data Product Configuration](/products/data_product/#configurations)

-   :material-list-box-outline:{ .lg .middle } **Learn more about the Data Products**

    ---

    Learn about key facets, characterisitcs, persona, and types of the Data Product.

    [:octicons-arrow-right-24: Data Product Core Concepts](/products/data_product/core_concepts/)

-   :material-content-duplicate:{ .lg .middle }  **Data Product Examples**

    ---

    Explore examples showcasing how an actual Data Product is developed.
    
    [:octicons-arrow-right-24: Data Product Examples](/products/data_product/#examples)

</div>

## Data Product Architecture
The architecture of a Data Product within DataOS typically involves several key components that handle various aspects of data processing and management. This section outlines the primary ports of a Data Product and introduces the additional Experience Ports offered by DataOS.

<center>
![Data Product](/products/data_product/ach.jpg)
<i>Data Product Architecture</i>
</center>


### **Input Ports**

Input Ports are responsible for receiving data that will form the core of the Data Product. They specify the format and protocol required to ingest data from operational source systems or other data products. These ports can be one or many, depending on the number of data sources. They specify the data format (e.g., CSV, JSON, Parquet) and protocol (e.g., HTTP, FTP, JDBC) required for data ingestion.

### **Output Ports**

Output Ports define how the data is exposed and consumed by external systems or users. They outline the format and consumption protocol for making data available to stakeholders. They specify how data can be queried or accessed (e.g., REST API, SQL query) and may support various formats depending on consumption needs (e.g., JSON, XML).

### **Control Ports**

Control Ports are used for monitoring, logging, and managing the Data Product. They also provide metadata and descriptive information about the Data Product. These ports facilitate performance tracking and operational metrics through monitoring and logging. They offer access to metadata such as ownership, organizational unit, licensing, and versioning. Additionally, they provide integration with a data marketplace, offering public and self-description information.

### **Experience Ports**

Experience Ports are provided by DataOS to support additional consumption paradigms beyond the standard input, output, and control functionalities. They enable specialized access methods such as BI tools, AI integrations, and data applications. Examples include exposing the Data Product via a REST API using Talos, creating and managing a semantic model with DataOS’s Lens for improved data understanding, and implementing a chat interface using Lens-LLM systems for natural language interactions with the data.

In the following sections, we have outlined the comprehensive thought process involved in developing a Data Product, from defining use cases to the deployment. 

## Define Usecases

The development of a Data Product initialized by defining the use cases, a single data product can cater to multiple use cases and all the way around. Let's take an example, suppose our usecase is to analyze the Website Traffic Source. This analysis provides actionable insights, enabling data-driven decision-making to optimize marketing strategies and improve business outcomes. The intended audience includes data analysts, marketing teams, business stakeholders, and technical teams responsible for data product development. The requirements for this use case include access to data source, an ETL (Extract, Transform, Load) process to clean and transform raw data, a data model to structure the transformed data, and visualization tools to present the analysis results. Additionally, secure data handling and storage must be ensured throughout the process.

## Explore and Discover Data Products
Once use cases have been defined, the next step is to explore the existing data products available in the [Data Product Hub](/interfaces/data_product_hub/). If the available Data Products sufficiently address the use cases, there is no need to develop a new data product. However, if the existing data products do not meet the requirements of the use cases, we can proceed to the Data Product Development Life Cycle to create a new data product.

## Data Product Development Life cycle

The Data Product Development Life cycle consists of four key phases: Design, Develop, Deploy, and Iterate. It starts with Design, where business goals are translated into a solution architecture. The Develop phase involves building and testing the data product based on this design. Deploy focuses on releasing the product to users and ensuring it operates effectively in a production environment. Finally, Iterate emphasizes continuous improvement through feedback and performance analysis to adapt to evolving needs and enhance the product over time. To know about Data Product Development Life cycle in detail, please [refer to this](/products/data_product/how_to_guides/).



## Structure of Data Product Manifest

A Data Product manifest outlines essential metadata and configuration details about a Data Product. This structure can be modified based on specific requirements and additional metadata needed for the Data Product.

=== "Manifest Structure"
    <img src="/products/data_product/schema.jpg" alt="Description" width="700">

=== "Code"

    ```yaml
    # Product meta section
    name: {{dp-test}} # Product name (mandatory)
    version: {{v1alpha}} # Manifest version (mandatory)
    type: {{data}} # Product-type (mandatory)
    tags: # Tags (Optional)
      - {{data-product}}
      - {{dataos:type:product}}
      - {{dataos:product:data}}
    description: {{the customer 360 view of the world}} # Descripton of the product (Optional)
    Purpose: {{This data product is intended to provide insights into the customer for strategic decisions on cross-selling additional products.}} # purpose (Optional)
    collaborators: # collaborators User ID (Optional)
      - {{thor}}
      - {{blackwidow}}
      - {{loki}}
    owner: {{iamgroot}} # Owner (Optional)
    refs: # Reference (Optional)
      - title: {{Bundle Info}} # Reference title (Mandatory if adding reference)
        href: {{https://dataos.info/resources/bundle/}} # Reference link (Mandatory if adding reference)
    entity: {{product}} # Entity (Mandatory)
    # Data Product-specific section (Mandatory)
    v1alpha: # Data Product version
      data:
        resources: # Resource specific section(Mandatory)
          - name: {{bundle-dp}} # Resource name (Mandatory)
            type: {{bundle}} # Resource type (Mandatory)
            version: {{v1beta}} # Resource version (Mandatory)
            refType: {{dataos}} # Resource reference type (Mandatory)
            workspace: {{public}} # Workspace (Requirement depends on the resource type)
            description: {{this bundle resource is for a data product}} # Resource description (Optional)
            purpose: {{deployment of data product resources}} # Purpose of the required resource (Optional)   
        
        inputs: # Input specific section (Mandatory)
          - description: Sales 360
            purpose: source
            refType: dataos
            ref: dataos://bigquery:PUBLIC/MYTABLE
        
        outputs: # Output specific section (Mandatory)
          - description: Customer
            purpose: consumption
            refType: dataos_address
            ref: dataos://icebase:sandbox/sales?acl=rw     
    ```


## Configurations 

Data Product can be configured to make the efficient business decisions based on reliable data. This section provides the detailed breakdown of each attribute, please refer to the documentation: [Attributes of Data Product manifest.](/products/data_product/configuration/)

## Recipes

 This section provides step-by-step guides to assist you in effectively configuring the Data Product to solve common challenges. Below are some recipes to help you configure Data Product effectively:

- [How to Create Data Product template using Cookiecutter?](/products/data_product/recipes/cookiecutter/)
- [How to Deploy Data Product using CI/CD pipeline?](/products/data_product/recipes/ci_cd/)

## Examples

This section provides practical, real-world scenarios demonstrating how to effectively develop a Data Product. Below are some examples to help you to understand the Data Product:

- [Financial Services Accelerator Data Product](/products/data_product/templates/accelerator/)

- [Sales 360 Data Product](/products/data_product/templates/sales_360/)

