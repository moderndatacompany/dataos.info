# Data Product

!!!info "Overview"

    This documentation is intended to provide structured information essential for understanding the Data Product's purpose, functionality, and operational aspects. This documentation is crucial for both technical teams and stakeholders to ensure clarity, consistency, and effective management throughout the lifecycle of the Data Product.

## Introduction

A Data Product is a self-contained unit within DataOS designed for handling and sharing analytical data, developed and managed by the dedicated teams. It includes meta data, data transformation code, input and output definitions, discovery and observability, APIs, documentation, service level objectives (SLOs), governance, transformation and platform dependencies such as compute and storage resources. Data Product is reusable, composable, portable and cloud-agnostic.​

> A data product is an integrated and self-contained combination of data, metadata, semantics and templates. It includes access and logic-certified implementation for tackling specific data and analytics (D&A) scenarios and reuse. A data product must be consumption-ready (trusted by consumers), up to date (by engineering teams) and approved for use (governed). Data products enable various D&A use cases, such as data
sharing, data monetization, analytics and application integration. 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **-** Gartner<sup>&reg;</sup><span class="circle"></span>


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **How to develop a Data Product?**

    ---

    Learn how to develop and manage a Data Product within DataOS.

    [:octicons-arrow-right-24: Data Product development lifecycle](/products/data_product/#data-product-development-lifecycle)


-   :material-list-box-outline:{ .lg .middle } **How to configure the manifest file of a Data Product?**

    ---

    Discover how to configure the manifest file of a Lakehouse by adjusting its attributes.

    [:octicons-arrow-right-24: Data Product configuration](/products/data_product/#configurations)

-   :material-list-box-outline:{ .lg .middle } **Learn more about the Data Product**

    ---

    Discover how to configure the manifest file of a Lakehouse by adjusting its attributes.

    [:octicons-arrow-right-24: Data Product core concepts](/products/data_product/core_concepts/)

-   :material-content-duplicate:{ .lg .middle }  **Data Product Examples**

    ---

    Explore examples showcasing how an actual Data Product is developed.
    
    [:octicons-arrow-right-24: Data Product Examples](/products/data_product/#examples)

</div>



## Data Product Development Lifecycle

The development of the Data Product lifecycle consists of four key phases:
### **Design**

The Design phase of Data Product Lifecycle is pivotal in aligning business objectives with actionable solutions. It begins with a comprehensive understanding of business goals and use cases, forming the basis for developing a robust solution architecture. To know more in detail, please refer to [How to Design a Data Product](/products/data_product/how_to_guides/design/).

### **Develop**

The Build phase involves coding, configurations, and integrations to build data pipelines, application logic, and interfaces according to the solution architecture. Rigorous testing ensures functionality, performance, and reliability, with ongoing stakeholder collaboration to validate that the built product aligns with business objectives and technical specifications. To know more in detail, please refer to [How to Build a Data Product](/products/data_product/how_to_guides/build/).

### **Deploy**
The Deploy phase of Data Product lifecycle emphasis on making Data Products available for Data Product personas. To know more, please refer to [How to Deploy a Data Product](/products/data_product/how_to_guides/deploy/).

### **Iterate**
The Iterate phase in the Data Product Lifecycle focuses on continuous improvement and refinement based on feedback, usage patterns, and evolving business needs. It involves analyzing user interactions, performance metrics, and gathering stakeholder feedback to identify areas for enhancement or adjustment. To know more in detail, please refer to [How to Iterate the Data Product](/products/data_product/how_to_guides/manage_and_iterate/).


<img src="/products/data_product/Untitled.jpg" alt="Description" width="1500">

## Structure of Data Product Manifest

A Data Product manifest outlines essential metadata and configuration details about a Data Product. This structure can be modified based on specific requirements and additional metadata needed for the Data Product.

=== "Syntax"
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

Below are some recipes to help you configure Data Product effectively:

- [How to Create Data Product template using Cookiecutter?](/products/data_product/recipes/cookiecutter/)
- [How to Deploy Data Product using CI/CD pipeline?](/products/data_product/recipes/ci_cd/)

## Examples

Below are some templates to help you to design the Data Product:

- [Customer 360 Data Product](/products/data_product/templates/customer/)

- [Sales 360 Data Product](/products/data_product/templates/sales_360/)

- [FS Accelerator Data Product](/products/data_product/templates/accelerator/)
