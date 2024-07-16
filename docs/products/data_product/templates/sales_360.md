
# Sales 360 Case Study: StrideRight Shoes

## Overview

**Company Background**

StrideRight Shoes is a leading manufacturer and retailer specializing in high-quality footwear for various demographics, from children to adults. With a commitment to comfort, style, and durability, StrideRight Shoes aims to provide exceptional customer experiences both online and in-store.

**Challenges Faced**

 StrideRight Shoes experienced significant operational challenges, including quality issues, late deliveries, and sampling delays. These issues impacted sales effectiveness and customer satisfaction, highlighting the need for streamlined operations and improved customer engagement strategies.

**Vision**

To revolutionize the footwear industry by leveraging advanced data analytics enhancing operational efficiency, and delivering personalized customer experiences that drive engagement, loyalty, and sustainable growth.

**Goals and Objectives**

  -  **Increase Customer engagement and lower churn rate:** Understand customer preferences and provide personalized recommendations and targeted marketing campaigns.

  -  **Operational Excellence:** Streamline operations to ensure timely deliveries, maintain high-quality standards, and optimize inventory management.

  -  **Maximize revenue from high-value customers.** Integrate and analyze customer interaction and transaction data to derive actionable insights and stay ahead of market trends.


**Use-cases**

1. **Personalized Marketing Campaigns:**  Tailor marketing efforts using customer data to create personalized recommendations and targeted campaigns.

2. **Customer Churn Prediction:** Identify at-risk customers with predictive models and implement retention strategies to reduce churn.

3. **Sales Performance Analysis:** Monitor and analyze sales data through interactive dashboards to identify trends and optimize marketing strategies.


**Solution**

**Sales 360 Data Product:** The Sales 360 data product is a structured dataset that contains comprehensive information about various entities within the organization. It serves as a central repository for product data, facilitating efficient management, analysis, and decision-making processes related to product operations, logistics, and customer engagement.


## Source Aligned Data Product

 <center> ![source align](/products/data_product/templates/source_align_dp.png) </center>
 <center> BigQuery Align Data Product </center>

**Pre-requisites**

To create the Data Product within DataOS, following requirements were needed:

- Necessary permissions to create and manage Data Products.

- Basic understanding of Data Product principles and lifecycle management.

## Design Phase

The individual responsible for designing the Sales 360 data product is the Data Product Owner.

### **Define entities and schema**

For our use case, we define the following entities: Customer, Product, Transaction, Order and Channel.


### **Data Understanding and Exploration**

To plan things in the design phase, we need to first look up at the various  data that is going to be integrated and will be making `Sales360` data product.

For this project, we aim to create a Sales 360 data product that will integrate various tables from BigQuery sources. These sources must be connected to DataOS using [Depot](/resources/depot).

**Create a Depot**

Creating a bigquery depot with json file of the credentails of the client's warehouse.

<details>

  <summary>bigquery depot manifest file</summary>

```yaml title="bigquery_depot.yml" hl_lines="18"
--8<-- "examples/products/data/sales_360/sales_depot.yml"
```
</details>

**Extract the Metadata**

To explore the metadata of the tables you can run a scanner. You can then access the metadata on [Metis UI](/interfaces/metis). The Scanner manifest file is shown below:

<details>

  <summary>scanner manifest file</summary>

```yaml title="scanner.yml"
--8<-- "examples/products/data/sales_360/scanner.yml"
```
</details>


**Explore the Data**

Now for data exploration, you can query the data using the workbench. To query the data on the workbench without moving the data you first need to create a Minerva or a Themis cluster that will target the Depot. By applying the below manifest file, you can create the cluster.


<details>

  <summary>cluster manifest file</summary>

```yaml title="cluster01.yml"
--8<-- "examples/products/data/sales_360/sales_cluster.yml"
```
</details>

To interact with the newly created `salesbq` Cluster in Workbench:

-  **Access the Cluster:** Open Workbench and select the `salesbq` cluster.
-  **Execute Queries:** Choose the catalog, schema, and tables, then run your query using the 'Run' button.
-  **Retrieve Results:** View the query results in the pane below the input area.

For more details, refer to the [Workbench](/interfaces/) documentation.

### **Data Product Architectural Design**

Once you've explored the data, the next step is to plan the architectural design. For example, In our case, the  Data Sources are Bigquery and Postgres to connect with  this sources we will need to create two Depots. The flare job will then use this depot and will faciliate easy ingestion and transformation from source to icebase. After ingestion, the data will must go through profiling and pass all the defined quality checks we will discuss this in detail in Build Phase. Then our data product will be ready to be used in a Analytical Platform.d

<center> ![Architectural Diagram](/products/data_product/templates/architecture.png) </center> 

### **Data Product Prototype**

Here we will define our Input, Output, Transformations and SLOs.

  - **Input** acts as an intermediary connecting diverse data sources. You can define as many input ports as you would like for each database. Here our input is bigquery depot.

  - **Transformation** is where you enrich the data to make it more useable  accurate and realiable. The stack we used for transformation is **`flare`**. The transformation stops involved were:

    - **Read Input from BigQuery:** Ingest raw data as is from Bigquery, with the only transformation being the conversion of cases to lower case.

    - **Joined Customer and Transaction Tables:** Integrated data from the Customer and Transaction tables to identify customer-churn.

    - **Orders enriched table** Integrated data from Customer, Product, Transaction and Orders table to create a Orders-enriched table.
    
  -  **Output** is defined as our complete data product which is our order enriched table ready to be consumed and can also be delivered to different platforms for different purpose like streamlit for creating data applications and [superset](/interfaces/superset) for data visualization, and [lens](/interfaces/lens) for data modeling.

    - **Streamlit App:** for customer churn details.

    - **Sales 360 Lens:** Data model for StrideRight Shoes sales intelligence and sales analysis.

    - **Superset Dashboard** Sales intelligence dashboard.

  - **SLOs:** Defining quality and profiling expectations and access related conditions are defined here.

```yaml title="data_product.yml"
--8<-- "examples/products/data/sales_360/data_products/sales_360_dp.yml"
```

### **Data Product Scanner**

<details>
  <summary> data-product scanner </summary>

```yaml title="scanner_sales360.yml"
--8<-- "examples/products/data/sales_360/product_scanner.yml"
```
</details>

Now, you can see your newly created data product in [DPH](/interfaces/data_product_hub)

### **Performance target**

  - **Response Time Goals:** Achieve 95% of queries processed within 500 milliseconds.

  - **Throughput Targets:** Sustain 1000 tasks per minute during peak periods.

  - **Resource Utilization Limits:** Ensure CPU usage remains below 80%.

  - **Quality Metrics:** Maintain data accuracy at 99%.

  - **Scalability Objectives:** Accommodate a 50% increase in data volume without additional infrastructure.

  **Availability Standards:** Achieve 99.99% uptime monthly.

These targets guide system design and optimization efforts, ensuring technical capabilities meet business requirements for consistent performance and reliability.

### **Validation and Iteration**

After finalizing the design of the Data Product, it undergoes review sessions with key stakeholders and team members to verify compliance with defined requirements and goals. All modifications made during this phase are recorded to facilitate ongoing enhancements to the design.

Once the design aligns with requirements, the subsequent phase focuses on devloping the Data Product.

## Build Phase

This section involves the building and creating resources and stacks and all other capabilities of DataOS to fulfill the design phase requirements.

From the design phase and Data Product Architectural Design, it is clear which DataOS resources we require to build the Data Product, and these are Depot, Cluster, Scanner, Flare, Monitor, Pager, SODA. Let’s see how to create each one step by step. As we already explored the data we’ll directly jump into the data transformation step using Flare.

### **Data Ingestion and Transformation**

Ingesting and transforming following tables:

1. Transaction
2. Customer
3. Product

using super [dag](/resources/workflow/#workflow-and-directed-acyclic-graph-dag) where the only transformation is to change the case to lower case of all.

```yaml title="ingestion_super_dag.yml"
--8<-- "examples/products/data/sales_360/dag/ingestion.yml"
```

Here are the all mentioned ingested manifest files:

<details>

  <summary>All ingested manifest files</summary>

```yaml title="customer-ingests.yml"
--8<-- "examples/products/data/sales_360/ingestions/customer_ingest.yml"
```

  <summary>transactions manifest file</summary>

```yaml title="transaction-ingest.yml"
--8<-- "examples/products/data/sales_360/ingestions/transaction_ingest.yml"
```
  <summary>products manifest file</summary>

```yaml title="product-ingestion.yml"
--8<-- "examples/products/data/sales_360/ingestions/product_ingest.yml"
```

Now, using customer and transaction data we will create a customer churn table that will give us the total count of churned and not churned customer.

  <summary>customer-churn manifest file</summary>

```yaml title="customer-churn-ingestion.yml"
--8<-- "examples/products/data/sales_360/ingestions/customer_churn.yml"
```

Similarly, we will join transaction, product, customer and order table to get a order-enriced table.

  <summary>orders-enriched manifest file</summary>

```yaml title="orders-enriched-ingestion.yml"
--8<-- "examples/products/data/sales_360/ingestions/orders.yml"
```

</details>


### **Data Profiling**

After Ingestion and transformation, it's necessary that we perform profiling and quality checks on our data as designed in the design phase.

```yaml title="profiling_super_dag.yml"
--8<-- "examples/products/data/sales_360/dag/profiling.yml"
```
Here are all the mentioned profiling manifest files:

<details>
  <summary>All profiling manifest files</summary>

```yaml title="customer-profiling.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/customer_profile.yml"
```

  <summary>transactions-profile manifest file</summary>

```yaml title="transactions-profiling.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/transaction_profile.yml"
```

  <summary>products-profile manifest file</summary>

```yaml title="products-profiling.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/products_profile.yml"
```
</details>


### **Data Quality Checks**

```yaml title="quality_checks_super_dag.yml"
--8<-- "examples/products/data/sales_360/dag/quality_checks.yml"
```

Here are all the mentioned quality checks manifest files:


<details>
  <summary>All quality-checks manifest file</summary>

```yaml title="customer_quality.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/customer_quality.yml"
```
  <summary>transactions-quality-checks manifest file</summary>

```yaml title="transactions_quality.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/transaction_quality.yml"
```
  <summary>products-quality-checks manifest file</summary>

```yaml title="products_quality.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/products_quality.yml"
```
</details>


### **Data Observability**

<details>
  <summary>Ingestion monitor manifest file</summary>

```yaml title="transformation_and_ingestion_monitor.yml"
--8<-- "examples/products/data/sales_360/observability/monitor/ingestion-monitor.yml"
```

  <summary>Ingestion pager manifest file</summary>

```yaml title="transformation_and_ingestion_pager.yml"
--8<-- "examples/products/data/sales_360/observability/pagers/workflow_pager.yml"
```

  <summary>profiling-monitor manifest file</summary>

```yaml title="profiling_monitor.yml"
--8<-- "examples/products/data/sales_360/observability/monitor/profile_monitor.yml"
```

  <summary>profiling-monitor manifest file</summary>

```yaml title="profiling_pager.yml"
--8<-- "examples/products/data/sales_360/observability/pagers/profile_pager.yml"
```

  <summary>quality-monitor manifest file</summary>

```yaml title="quality_monitor.yml"
--8<-- "examples/products/data/sales_360/observability/monitor/quality_monitor.yml"
```

  <summary>quality-pager manifest file</summary>

```yaml title="quality_pager.yml"
--8<-- "examples/products/data/sales_360/observability/pagers/quality_pager.yml"
```
</details>


## Deploy Phase

Once you've created your data product with all its functionalities and insights, the next step is to ensure it reaches its intended audience through platforms like Metis and the Data Product Hub. To achieve this, running the Scanner becomes crucial.

## Monitoring and Iteration Phase

After deployment, monitor the Data Product's performance and continue to collect feedback. Iterate the process as needed to achieve the desired results. The improvements can include:

 - Enhancing the level of data quality.
 - Enriching the schema.

By following these steps, you can continuously improve your Data Product to better meet user needs and business objectives.


## Data Products Consumption

All the Data Visulaisationa tools such as Superset, PowerBI and Data Modelling tools such as Lens serve as a tool to consume the data products to derive the required actionable insights for which the data product was built.

### **Building Data Model**
 
**Create the Lens**

<center> ![Lens](/products/data_product/templates/lens.png) </center>
<center>  The Entity Relationship Diagram of the lens </center>


**Developing a Conceptual Data Model**

| Entity      | Fields and Dimensions                                                                                                                                     | Derived Dimensions                                                                                                                                                                              | Measure                                                                                               | Related To | Relationship |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------|--------------|
| Channel     | store_id, store_name, store_address, store_contact_email, store_contact_phone, platform_name, platform_url, country, currency, channel_type, nearest_offline_store |                                                                                                                                                                                                 | total_stores                                                                                          |            |              |
| Customer    | customer_id, first_name, last_name, gender, phone_number, email_id, birth_date, age, education_level, marital_status, number_of_children, register_date, occupation, annual_income, hobbies, degree_of_loyalty, social_class, mailing_street, city, state, country, zip_code | full_name, age_group                                                                                                                                                                            | total_customers, average_age                                                                          | Transaction| 1:N          |
| Products    | productid, skuid, productname, productcategory, subcategory, gender, price, cost, launchdate, designername, color, size, model                                 |                                                                                                                                                                                                 | total_products, average_price, total_cost, average_margin                                             |            |              |
| Transaction | transaction_id, customer_id, transaction_date, order_id, transaction_amount, payment_method, transaction_type, transaction_status, order_delivery_date, discounted_amount, shipping_amount, order_total_amount, discount_percentage, shipping_address, billing_address, promo_code, shipping_method, order_status, skuid, store_id | full_address, transaction_year, transaction_month, transaction_day, order_delivery_duration, discount_applied, shipping_cost_category                                                          | total_transactions, total_revenue, average_transaction_amount, total_discounted_amount, total_shipping_amount, total_order_amount, transaction_percentage_with_discount, ups_delivered_percentage, canceled_order_percentage, monthly_revenue_curr, monthly_revenue_prev | Products, Channel | N:1, N:1   |


<details> 
  <summary> lens</summary>
  
```yaml title="sales_360_lens.yml"
--8<-- "examples/products/data/sales_360/lens.yml"
```
</details>

### **Building Data Application**

This streamlit app will give you the details  of churned and not  churned customers so that all the customers who are going to churned can be retained bby contacting them and giving them special discounts.

<details>
  <summary>streamlit-app manifest file</summary>

```yaml title="app.py"
--8<-- "examples/products/data/sales_360/app/customer_churn.py"
```
</details>

**The Output:**

<center> ![Streamlit](/products/data_product/templates/streamlit.png) </center>

<center> The Streamit App for Customer Churn Details </center>


### **Building Dashboards**

<center> ![Superset](/products/data_product/templates/superset.png) </center>

<center> The Superset Dashboard for Sales 360 </center>