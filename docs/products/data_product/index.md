---
title: Data Product
search:
  boost: 4
tags:
  - Data Product
hide:
  - tags
---

# :products-dataproduct: Data Product

A Data Product is a self-contained unit within DataOS designed for handling and sharing analytical data, developed and managed by the dedicated teams. It includes meta data, data transformation code, input and output definitions, discovery and observability, APIs, documentation, service level objectives (SLOs), governance, transformation and platform dependencies such as compute and storage resources. Data Product is reusable, composable, portable and cloud-agnostic.​

DataOS provides the platform for the development, management, processing, and deployment of Data Products across an organization. It provides a streamlined approach to handling Data Products throughout their entire lifecycle, from ingestion and storage to analysis and delivery. By integrating these functionalities into a single, cohesive system, DataOS enhances decision-making and boosts operational efficiency.


> A Data Product is an integrated and self-contained combination of data, metadata, semantics and templates. It includes access and logic-certified implementation for tackling specific data and analytics (D&A) scenarios and reuse. A Data Product must be consumption-ready (trusted by consumers), up to date (by engineering teams) and approved for use (governed). Data Products enable various D&A use cases, such as data
sharing, data monetization, analytics and application integration. 

>  **-** Gartner<sup>&reg;</sup><span class="circle"></span>

<center>
![Data Product Development lifecycle](/products/data_product/diagram.jpg){: style="width:36rem;" }
<figcaption><i>Data Product Development lifecycle</i></figcaption>
</center>



<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **How to develop a Data Product?**

    ---

    Learn how to develop and manage a Data Product within DataOS.

    [:octicons-arrow-right-24: Data Product Development Lifecycle](/products/data_product/#data-product-development-life-cycle)

-   :material-list-box-outline:{ .lg .middle } **Learn more about the Data Product**

    ---

    Learn about key facets, characterisitcs, persona, and types of the Data Product.

    [:octicons-arrow-right-24: Data Product Core Concepts](/products/data_product/core_concepts/)

-   :material-content-duplicate:{ .lg .middle }  **Data Product Examples**

    ---

    Explore examples showcasing how an actual Data Product is developed.
    
    [:octicons-arrow-right-24: Data Product Examples](/products/data_product/#examples)

</div>

## Data Product Architecture
The architecture of a Data Product within DataOS involves several components designed to facilitate the data consumption and deliver business value. This section outlines the primary consumption ports of a Data Product and introduces the additional Experience Ports offered by DataOS.

<center>
![Data Product](/products/data_product/ach.jpg){: style="width:31rem;" }
<figcaption><i>Data Product Architecture</i></figcaption>
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

## Define usecases

The development of a Data Product initialized by defining the use cases, a single data product can cater to multiple use cases and all the way around. Let's take an example, suppose our usecase is to analyze the Website Traffic Source. This analysis provides actionable insights, enabling data-driven decision-making to optimize marketing strategies and improve business outcomes. The intended audience includes data analysts, marketing teams, business stakeholders, and technical teams responsible for data product development. The requirements for this use case include access to data source, an ETL (Extract, Transform, Load) process to clean and transform raw data, a data model to structure the transformed data, and visualization tools to present the analysis results. Additionally, secure data handling and storage must be ensured throughout the process.

## Explore and discover Data Products
Once use cases have been defined, the next step is to explore the existing Data Products available in the [Data Product Hub](/interfaces/data_product_hub/). If the available Data Products sufficiently address the use cases, there is no need to develop a new Data Product. However, if the existing Data Products do not meet the requirements of the use cases, we can proceed to the Data Product Development lifecycle to create a new Data Product.

## Data Product development lifecycle

The Data Product Development lifecycle consists of four key phases: Design, Develop, Deploy, and Iterate. It starts with Design, where business goals are translated into a solution architecture. The Develop phase involves building and testing the Data Product based on this design. Deploy focuses on releasing the product to users and ensuring it operates effectively in a production environment. Finally, Iterate emphasizes continuous improvement through feedback and performance analysis to adapt to evolving needs and enhance the product over time. To know about Data Product Development lifecycle in detail, please [refer to this](/products/data_product/how_to_guides/).

## Structure of Data Product manifest

A Data Product manifest outlines essential metadata and configuration details about a Data Product. This structure can be modified based on specific requirements and additional metadata needed for the Data Product.

=== "Manifest Structure"
    <center>
    ![Data Product Manifest Structure](/products/data_product/manifestfile.png){: style="width:31rem;" }
    <figcaption><i>Data Product Manifest Structure</i></figcaption>
    </center>

=== "Code"

    ```yaml
    # Product meta section
    name: ${{product-360}} # mandatory
    version: ${{v1beta}} # mandatory
    entity: ${{product}} # mandatory
    type: ${{data}} # mandatory
    tags:   # optional
      - ${{DPDomain.Sales}}
      - ${{DPDomain.Marketing}}
      - ${{DPUsecase.Customer Segmentation}}
      - ${{DPUsecase.Product Recommendation}}
      - ${{DPTier.DataCOE Approved}}
    description: ${{Leverages product affinity analysis to identify cross-sell opportunities, enabling businesses to enhance customer recommendations and drive additional sales by understanding the relationships between products purchased together}} # optional
    refs: # optional
    - title: ${{'Workspace Info'}}
      href: ${{https://dataos.info/interfaces/cli/command_reference/#workspace}}
    # Product specific section
    v1beta: # mandatory
      data: # mandatory
        meta: # optional
          title: ${{Product 360}}
          sourceCodeUrl: ${{https://bitbucket.org/mywork/talos/src/main/}}
          trackerUrl: ${{https://rubikai.atlassian.net/browse/DPRB-65}}
    
        collaborators: # optional
          - name: ${{iamgroot}}
            description: ${{developer}}
          - name: ${{iamthor}}
            description: ${{consumer}}

        resource: # mandatory
          refType: ${{dataos}}
          ref: ${{bundle:v1beta:product-360-bundle}}

        inputs: # mandatory
          - refType: ${{dataos}}
            ref: ${{dataset:icebase:customer_relationship_management:customer}}

          - refType: ${{dataos}}
            ref: ${{dataset:icebase:customer_relationship_management:purchase}}

          - refType: ${{dataos}}
            ref: ${{dataset:icebase:customer_relationship_management:product}}

        outputs: # optional
          - refType: ${{dataos}}
            ref: ${{dataset:icebase:customer_relationship_management:product_affinity_matrix}}

          - refType: ${{dataos}}
            ref: ${{dataset:icebase:customer_relationship_management:cross_sell_recommendations}}

        ports: # optional
          lens:
            - ref: ${{lens:v1alpha:cross-sell-affinity:public}}
              refType: ${{dataos}}

          talos:
            - ref: ${{service:v1:cross-sell-api:public}}
              refType: ${{dataos}}    
    ```


## Configurations 

Data Product can be configured to make the efficient business decisions based on reliable data. This section provides the detailed breakdown of each attribute, please refer to the documentation: [Attributes of Data Product manifest](/products/data_product/configurations/)

## Recipes

This section provides step-by-step guides to assist you in effectively configuring the Data Product to solve common challenges. Below are some recipes to help you configure Data Product effectively:

- [How to Deploy Data Product using CI/CD pipeline?](/products/data_product/recipes/ci_cd/)

## Examples

This section provides practical, real-world scenarios demonstrating how to effectively develop a Data Product. Below are some examples to help you to understand the Data Product:

- [Product affinity Data Product](/products/data_product/templates/product_affinity/)
