---
title: Data Product Hub
search:
  boost: 4
tags:
  - Data Product Hub
  - DPH
  - Data Product Catalog
hide:
  - tags
---

# :interfaces-dataproducthub: Data Product Hub

The Data Product Hub is a Graphical User Interface within DataOS where actionable [Data Products](/products/data_product/), Metrics and Perspectives can be discovered by data analysts, business analysts, data scientists, and data app developers. These Data Products are curated to provide business value and serve as a foundation for executing various use cases. Key use cases include **Analytics**, **AI/ML**, **GenAI/LLM on structured enterprise data**, and **data sharing**.

In addition, access to [Data APIs](/resources/stacks/talos/), built on top of the Data Product layer is offered by the Data Product Hub, enhancing the ability to integrate and utilize data seamlessly. The platform bridges the gap between IT-managed data infrastructure and business teams, enabling consistent data access despite changes in the underlying data systems. By providing curated, trusted data in multiple formats, time-to-value for new use cases is significantly accelerated by the Data Product Hub, helping organizations reduce data total cost of ownership (TCO) and achieve more efficient and streamlined workflows. To understand the key concepts of Data Product Hub, refer to the following link: [Core Concepts](/interfaces/data_product_hub/core_concepts/).

## Key features

The key features of the Data Product Hub are covered in this section.

### **Self-service data consumption**

The Data Product Hub is used by business users to discover, explore, and leverage Data Products that are designed for their needs. 

<center>
  <img src="/interfaces/data_product_hub/image%20(25).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Self-service Data Consumption</i></figcaption>
</center>


### **Trust and governance**

A foundation for trust and governance is provided, ensuring data is reliable, secure, and compliant with organizational policies.

<center>
  <img src="/interfaces/data_product_hub/image%20(26).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Trust and Governance</i></figcaption>
</center>



### **Embedded context**

Each Data Product is provided with lineage, quality metrics, usage patterns, governance details, semantic definitions, and documentation.

<center>
  <img src="/interfaces/data_product_hub/image%20(27).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Embedded Context</i></figcaption>
</center>

### **Seamless integrations**

A central layer for generating APIs, connecting to BI/analytics tools, and AI and ML tools is provided by the Data Product Hub, ensuring seamless integration and smooth access to metrics and insights.

<center>
  <img src="/interfaces/data_product_hub/image%20(28).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Seamless Integrations</i></figcaption>
</center>

## Data Product discovery

The right Data Products can be discovered to make timely business decisions. In this section, the Data Product Hub interface is explained in detail to discover potential Data Products for a specific use case. To get started with the Data Product Hub, click on Data Product Hub 2.0, and you will be redirected to the Data Product Hub home page.
For more information, check out the [Data Product discovery](/interfaces/data_product_hub/discovery/).

<center>
  <img src="/interfaces/data_product_hub/dph2.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product Hub on DataOS Home Page</i></figcaption>
</center>




## Data Product exploration

The Explore button on the Data Product Hub interface allows deeper exploration into the details of a Data Product. Data can be presented in visual forms such as tables and charts, details on the data model are provided, and queries can be executed using GraphQL, enabling analysis of the data before consumption via APIs or BI tools. For more information, check out the [Data Product Exploration](/interfaces/data_product_hub/exploration/).

<aside class="callout">

🗣 If no model is exposed by the Data Product, the Explore feature will not be available.

</aside>




## Data Product activation

Multiple ways to access and interact with Data Products are offered by Data Product Hub, whether using BI tools, AI/ML notebooks, or API endpoints for application development.

### **BI sync**

The BI Sync feature in the Data Product Hub allows for seamless integration with popular business intelligence tools, enabling automatic synchronization of Data Products with preferred platforms.

<div class="grid cards" markdown>

-   :interfaces-tableau:{ .lg .middle } **Tableau Cloud**

    ---

    Visualizations can be created and shared with the help of Tableau Cloud. For more details, refer to the link below.

    [:octicons-arrow-right-24: Tableau Cloud Integration](/interfaces/data_product_hub/activation/bi_sync/tableau_cloud/)


-   :interfaces-powerbi:{ .lg .middle } **Power BI**

    ---

    Power BI, a data visualization tool, is supported by the BI Sync feature. This integration ensures that Data Products are made available within Power BI, facilitating interactive data exploration and reporting.

    [:octicons-arrow-right-24: PowerBI Integration](/interfaces/data_product_hub/activation/bi_sync/powerbi/)



-   :interfaces-tableau:{ .lg .middle } **Tableau Desktop**

    ---

    Tableau Desktop is a visual analytics tool that is used for in-depth data exploration. For more information, visit the link below:

    [:octicons-arrow-right-24: Tableau Desktop Integration](/interfaces/data_product_hub/activation/bi_sync/tableau_desk/)


-   :interfaces-excel:{ .lg .middle } **Microsoft Excel**

    ---

    Data products can be imported into Excel through integration with Power BI. For more information, visit the link below:


    [:octicons-arrow-right-24: Microsoft Excel Integration](/interfaces/data_product_hub/activation/bi_sync/excel/)
     

-   :interfaces-superset:{ .lg .middle } **Apache Superset**

    ---

    For users of Apache Superset, an open-source data exploration and visualization platform, automatic synchronization of Data Product through BI Sync is provided. The connection can be set up through the link below.


    [:octicons-arrow-right-24: Apache Superset](/interfaces/data_product_hub/activation/bi_sync/superset/)


</div>


### **AI/ML**

The Data Products curated in the DPH can be consumed in data science notebooks such as Jupyter Notebook to power AI/ML use cases.

<div class="grid cards" markdown>

-   :interfaces-notebook:{ .lg .middle } **Jupyter Notebook**

    ---

    For more details, refer to the link below:

    [:octicons-arrow-right-24: Jupyter Notebook Integration](/interfaces/data_product_hub/activation/jupyter/)


</div>


### **App development**

Data applications can be developed on top of the Data Product through PostgreSQL or GraphQL API endpoints.

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **App Development**

    ---

    Develop data applications using PostgreSQL and GraphQL API endpoint. Refer to the link for more details:

    [:octicons-arrow-right-24: Postgres and GraphQL integration](/interfaces/data_product_hub/activation/app_development/)

</div>



### **Data APIs**

The Data Product can be consumed for various use cases via REST APIs. 

<div class="grid cards" markdown>

-   :material-format-list-bulleted-type:{ .lg .middle } **Data APIs**

    ---

    For more details, refer to the link below:

    [:octicons-arrow-right-24: Data APIs](/interfaces/data_product_hub/activation/data_api/)


</div>


## Best practices

Essential strategies to ensure efficient and optimal usage of the Data Product Hub are outlined in this section. Key recommendations are emphasized for users to effectively manage and utilize Data Products. For more information, check out the [best practices](/interfaces/data_product_hub/bestpractices/).


## Examples

This section involves detailed, step-by-step guides for solving specific business use cases using the Data Product Hub. Each section focuses on a particular aspect of DPH, such as discovering relevant Data Products, exploring them in-depth, and integrating the data into external tools like BI platforms and Jupyter Notebooks. These examples demonstrate how data analysts and business users can collaborate to solve real-world challenges efficiently. For more information, check out the [examples](/interfaces/data_product_hub/recipe/).



## Recipes


The various recipes on Data Product Hub are explained in this section with examples.

1. [Discovering a Data Product](/interfaces/data_product_hub/recipe/#discovering-a-data-product): This recipe introduces the process of discovering relevant Data Products within the Data Product Hub using a real-life use case. It guides users on how to filter by specific domains, such as Corporate Finance, to find the most relevant Data Products for the use case.

3. [Activating a Data Product via BI sync](/interfaces/data_product_hub/recipe/#activating-the-data-product-via-bi-sync): The steps to activate a Data Product through BI Sync for seamless integration with Tableau Cloud are outlined in this recipe. It guides users on connecting the Data Product to Tableau, activating it, and setting up a real-time dashboard to visualize key financial and operational metrics.

4. [Consuming Data Products on Tableau Cloud](/interfaces/data_product_hub/recipe/#consuming-the-data-product-on-tableau-cloud): After a Data Product is activated, users are shown in this recipe how to consume it on Tableau Cloud. Steps are provided for creating a workbook, connecting to the data source, and building visualizations to display financial and performance indicators.

5. [Exploring the Data Product](/interfaces/data_product_hub/recipe/#exploring-the-data-product): In this recipe, the Data Product can be explored in detail using the Explore feature of the Data Product Hub.

6. [Activating a Data Product via Jupyter Notebook](/interfaces/data_product_hub/recipe/#activating-the-data-product-via-jupyter-notebook): This recipe explains the activation of a Data Product for Jupyter Notebook. It provides guidance on downloading and running a Jupyter Notebook with Data Product APIs, enabling the building of advanced models and conducting machine learning tasks.