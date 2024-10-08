# :interfaces-dataproducthub: Data Product Hub

Data Product Hub (DPH) is a Graphical User Interface within DataOS where data analysts, business analysts, data scientists, and data app developers can discover actionable [Data Products](/products/data_product/) and perspectives. These Data Products are meticulously curated to provide business value and serve as a robust foundation for executing various use cases. Key use cases include **Analytics**, **AI/ML**, **GenAI/LLM on structured enterprise data**, and **data sharing**.

In addition, the DPH offers access to **DataAPIs** built on top of the Data Product layer, enhancing the ability to integrate and utilize data seamlessly. This platform effectively bridges the gap between IT-managed data infrastructure and business teams, enabling consistent data access despite changes in the underlying data systems. By providing curated, trusted data in multiple formats, the DPH significantly accelerates **time-to-value** for new use cases, helping organizations reduce **data total cost of ownership (TCO)** and achieve **more efficient and streamlined workflows**.

## Key Features

This section covers the key features of the Data Product Hub.

### **Self-Service Data Consumption**

Using Data Product Hub, business users can independently discover, explore, and leverage purposefully designed Data Products tailored to their needs. 

<center>
  <img src="/interfaces/data_product_hub/image%20(25).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Self-service Data Consumption</i></figcaption>
</center>


### **Trust and Governance**

Data Product Hub provides a robust foundation for trust and governance, ensuring data is reliable, secure, and compliant with organizational policies.

<center>
  <img src="/interfaces/data_product_hub/image%20(26).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Trust and Governance</i></figcaption>
</center>



### **Embedded Context**

Data Product Hub provides lineage, quality metrics, usage patterns, governance details, semantic definitions, and documentation for each Data Product. 

<center>
  <img src="/interfaces/data_product_hub/image%20(27).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Embedded Context</i></figcaption>
</center>

### **Seamless Integrations**

The Data Product Hub acts as a central layer for generating APIs, connecting to BI/analytics tools, and,  AI and ML tools, ensuring seamless integration and smooth access to metrics and insights.

<center>
  <img src="/interfaces/data_product_hub/image%20(28).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Seamless Integrations</i></figcaption>
</center>

## **Data Product Discovery**

Discover the right Data Products to make timely business decisions. In this section, you will explore the DPH interface in detail to discover the potential Data Products for your specific use case. To get started with the DPH, click on the **Data Product Hub 2.0**, you will be redirected to the Data Product Hub home page.

> [Data Product Discovery](/interfaces/data_product_hub/discovery/)

<center>
  <img src="/interfaces/data_product_hub/dataos.png" alt="DPH" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Data Product Hub on DataOS Home Page</i></figcaption>
</center>

---


## Data Product Exploration

The **Explore** button on the Data Product Hub interface allows you to drill deeper into the details of a Data Product. It presents data in visual forms such as tables and charts, provides details on the data model, and allows you to query using GraphQL enabling you to analyze the data before consuming it via APIs or BI tools.

<aside class="callout">

🗣 If no model is exposed by the Data Product, the Explore feature will be unavailable.

</aside>

> [Data Product Exploration](/interfaces/data_product_hub/exploration/)

---

## Data Product Activation

DPH offers multiple ways to access and interact with your Data Products, whether you're using BI tools, data science notebooks, or API endpoints for application development.

### **BI Sync**

The BI Sync feature in the DPH enables seamless integration with popular business intelligence tools, allowing for automatic synchronization of data products with your preferred platforms.

<div class="grid cards" markdown>

-   :interfaces-tableau:{ .lg .middle } **Tableau Cloud**

    ---

    Tableau Cloud allows you to access and share your visualizations online. For more details, refer to the link below:

    [:octicons-arrow-right-24: Tableau Cloud Integration](/interfaces/data_product_hub/activation/bi_sync/tableau_cloud/)


-   :interfaces-powerbi:{ .lg .middle } **Power BI**

    ---

    The BI Sync feature also supports Power BI, a data visualization tool from Microsoft. This integration ensures that your data products are automatically available within Power BI, facilitating interactive data exploration and reporting.

    [:octicons-arrow-right-24: PowerBI Integration](/interfaces/data_product_hub/activation/bi_sync/powerbi/)



-   :interfaces-tableau:{ .lg .middle } **Tableau Desktop**

    ---

    Tableau Desktop is a powerful visual analytics tool that enables in-depth data exploration. For more information, visit the link below:

    [:octicons-arrow-right-24: Tableau Desktop Integration](/interfaces/data_product_hub/activation/bi_sync/tableau_desk/)


-   :interfaces-excel:{ .lg .middle } **Microsoft Excel**

    ---

    Microsoft Excel remains a popular tool for data analysis and reporting. For more information, visit the link below:


    [:octicons-arrow-right-24: Microsoft Excel Integration](/interfaces/data_product_hub/activation/bi_sync/excel/)
     

-   :interfaces-superset:{ .lg .middle } **Apache Superset**

    ---

    For users of Apache Superset, an open-source data exploration and visualization platform, the DPH provides automatic synchronization through BI Sync. Set up the connection through the link below.


    [:octicons-arrow-right-24: Apache Superset](/interfaces/data_product_hub/activation/bi_sync/superset/)


</div>


### **AI/ML**

You can consume the data products curated in the DPH into data science notebooks such as Jupyter Notebook to power your AI/ML use cases.

<div class="grid cards" markdown>

-   :interfaces-notebook:{ .lg .middle } **Jupyter Notebook**

    ---

    For more details, refer to the link below:

    [:octicons-arrow-right-24: Jupyter Notebook Integration](/interfaces/data_product_hub/activation/jupyter/)


</div>


### **App Development**

You can develop applications on top of your Data Product through PostgreSQL or GraphQL API endpoint.

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **App Development**

    ---

    Develop data applications using PostgreSQL and GraphQL API endpoint. Refer to the link for more details:

    [:octicons-arrow-right-24: Postgres and GraphQL integration](/interfaces/data_product_hub/activation/app_development/)

</div>



### **Data APIs**

You can consume the Data Product to create data applications via REST APIs.  

<div class="grid cards" markdown>

-   :material-format-list-bulleted-type:{ .lg .middle } **Data APIs**

    ---

    For more details, refer to the link below:

    [:octicons-arrow-right-24: Data APIs](/interfaces/data_product_hub/activation/data_api/)


</div>

---

## Best Practices

This section outlines essential strategies to ensure efficient and optimal usage of the DPH. It emphasizes key recommendations for users to effectively manage and utilize Data Products within the platform.

> [Best Practices](/interfaces/data_product_hub/bestpractices/)

---

## Recipes

This section is designed to provide detailed, step-by-step guides for solving specific business use cases using the Data Product Hub. Each recipe focuses on a particular aspect of DPH, such as discovering relevant Data Products, exploring them in-depth, and integrating the data into external tools like BI platforms and Jupyter Notebooks. These recipes demonstrate how data analysts and business users can collaborate to solve real-world challenges efficiently.

> [Data Product Hub Recipe](/interfaces/data_product_hub/recipe/)

The above recipe incorporates the following seperate sections:

1. [Discovering a Data Product](/interfaces/data_product_hub/recipe/#discovering-a-data-product): This recipe introduces you to the process of discovering relevant Data Products within the DPH using a real-life use case. It guides the user on how to filter by specific domains, such as **Corporate Finance**, to find the most relevant Data Products for the use case. 

3. [Activating a Data Product via BI Sync](/interfaces/data_product_hub/recipe/#activating-the-data-product-via-bi-sync): This recipe outlines the steps to activate a Data Product through **BI Sync** for seamless integration with **Tableau Cloud**. It will guide you through connecting the Data Product to Tableau, activating it, and setting up a real-time dashboard to visualize key financial and operational metrics. 

4. [Consuming Data Products on Tableau Cloud](/interfaces/data_product_hub/recipe/#consuming-the-data-product-on-tableau-cloud): After activating a Data Product, this recipe shows users how to consume it on **Tableau Cloud**. It provides steps for creating a workbook, connecting to the data source, and building visualizations to display financial and performance indicators. 

5. [Exploring the Data Product](/interfaces/data_product_hub/recipe/#exploring-the-data-product): In this recipe, you can explore the Data Product in detail using the **Explore** feature of the Data Product Hub. 

6. [Activating a Data Product via Jupyter Notebook](/interfaces/data_product_hub/recipe/#activating-the-data-product-via-jupyter-notebook): This recipe explains how to activate a Data Product for use in the **Jupyter Notebook**. It guides you through downloading and running a Jupyter Notebook with Data Product APIs, enabling you to build advanced models and conduct machine learning tasks.