# Sales 360 Data Product

The Sales 360 data product is a structured dataset that contains comprehensive information about various entities within the organization. It serves as a central repository for product data, facilitating efficient management, analysis, and decision-making processes related to product operations, logistics, and customer engagement.

## Define  Vision

The vision for the Sales 360 Data Product is to become the definitive source of truth for all sales-related data within the organization. This data product aims to:

  - Enable a deeper understanding of the factors driving sales performance.

  - Support continuous improvement and innovation in sales strategies and operations.

  - Enhance customer satisfaction and loyalty through better engagement and personalized experiences.

  - Drive sustainable growth and profitability by leveraging insights gained from the data product.

## Define Use-case

The primary use case for the Sales 360 Data Product is to analyze sales performance. This includes:

  - Tracking sales metrics such as revenue, units sold, and average transaction value.
  - Identifying the most and least profitable products and services.
  - Monitoring sales team performance and setting targets.
  - Understanding customer purchase history and preferences.
  - Analyzing the effectiveness of marketing campaigns and promotions.
  - Forecasting future sales based on historical data and market trends.

## Pre-requisites

To create the Data Product within DataOS, following requirements were needed:

- Necessary permissions to create and manage Data Products.

- Basic understanding of Data Product principles and lifecycle management.

## Design Phase

### **Data Understanding and Exploration**

In the design phase of a data product, we define the scope and structure of the data product and plan its development. To plan things in the design phase, we need to first look up at the various  data that is going to be integrated and will be making Sales360 data product.

For this project, we aim to create a Sales 360 data product that will integrate various tables from multiple sources. These sources must be connected to DataOS using Depot.

For example, here the source is bigquery warehouse. 

#### **Create a Depot**

Creating a bigquery depot with json file of the credentails of the client's warehouse.

```yaml title="bigquery_depot.yml" hl_lines="18"
--8<-- "examples/products/data/sales_360/sales_depot.yml"
```

#### **Extract the Metadata**

To explore the metadata of the tables you can run a scanner. You can then access the metadata on Metis UI. The Scanner manifest file is shown below:

```yaml title="scanner.yml"
--8<-- "examples/products/data/sales_360/scanner.yml"
```

#### **Explore the Data**

Now for data exploration, you can query the data using the workbench. To query the data on the workbench without moving the data you first need to create a Minerva or a Themis cluster that will target the Depot. By applying the below manifest file, you can create the cluster.

```yaml title="cluster01.yml"
--8<-- "examples/products/data/sales_360/sales_cluster.yml"
```

Now, to interact with  the newly created Cluster, execute the following steps:

- **Accessing the Cluster:** Upon launching the Workbench application, the user is required to select the desired Cluster. In this instance, the cluster identified as `salesbq` is chosen.

- **Execution of Queries**:
    - **Catalog, Schema, and Table Selection**: The user must select the appropriate catalog, schema, and tables within the Workbench interface.
    - **Query Execution**: After formulating the query, the user executes it by clicking the 'Run' button.
    - **Result Retrieval**: The outcomes of the executed query are displayed in the pane situated below the query input area.

For comprehensive details on the features and capabilities of Workbench, refer to the dedicated [Workbench](../interfaces/workbench.md) documentation.


#### **Data Product Architectural Design**

Once you've explored the data, the next step is to plan the architectural design. For example, In our case, the  Data Sources are Bigquery and Postgres to connect with  this sources we will need to create two Depots. The flare job will then use this depot and will faciliate easy ingestion and transformation from source to icebase. After ingestion, the data will must go through profiling and pass all the defined quality checks we will discuss this in detail in Build Phase. Then our data product will be ready to be used in a Analytical Platform.

```markdown
+-------------------------+                                     +-------------------+
|                         |                                     |                   |
|      Data Sources       +                                     |    Analytical     |
|     (Bigquery,          |                                     |    platforms      |
|      Postgres,          |                                     |                   |
|           etc.)         |                                     |                   |
+-----------+-------------+                                     +---------+---------+
            |                                                             ^
            |                                                             |
            |                                                             |
            |                                                             |
            v                                                             |
+-----------+-------------+      +-----------+-----------+      +---------+---------+
|                         |      |                       |      |                   |
|         Depot           +----->+     Workflow          +----->+     Objectives    |
+-------------------------+      | (Data Transformation) |      | (Quality Checks)  |
                                 +-----------------------+      |                   |
                                                                |                   |
                                                                +-------------------+
```

#### **Performance target**

  - **Response Time Goals:** Achieve 95% of queries processed within 500 milliseconds.

  - **Throughput Targets:** Sustain 1000 tasks per minute during peak periods.

  - **Resource Utilization Limits:** Ensure CPU usage remains below 80%.

  - **Quality Metrics:** Maintain data accuracy at 99%.

  - **Scalability Objectives:** Accommodate a 50% increase in data volume without additional infrastructure.

  **Availability Standards:** Achieve 99.99% uptime monthly.

These targets guide system design and optimization efforts, ensuring technical capabilities meet business requirements for consistent performance and reliability.

#### **Validation and Iteration**

After finalizing the design of the Data Product, it undergoes review sessions with key stakeholders and team members to verify compliance with defined requirements and goals. All modifications made during this phase are recorded to facilitate ongoing enhancements to the design.

Once the design aligns with requirements, the subsequent phase focuses on devloping the Data Product.

## Develop

This section involves the devloping the Data Product right from data connection to defining SLOs. Here we will be creating resources and stacks and all other capabilities of DataOS to fulfill the design phase requirements.

### **Steps to Create a Data Product**

From the design phase and Data Product Architectural Design, it is clear which DataOS resources we require to build the Data Product, and these are Depot, Cluster, Scanner, Flare, Policy, SODA Checks and Bundle. Let’s see how to create each one step by step. As we already explored the data we’ll directly jump into the data transformation step using Flare.

#### **Create the Flare Job for data ingestion and data transformation**

Ingesting and transforming following tables:

1. Transaction
2. Customer
3. Product

where the only transformation is to change the case to lower case of all.

```yaml title="transaction-ingests"
--8<-- "examples/products/data/sales_360/transaction_ingest.yml"
```

```yaml title="customer-ingest.yml"
--8<-- "examples/products/data/sales_360/customer_ingest.yml"
```

```yaml title="product-ingestion.yml"
--8<-- "examples/products/data/sales_360/product_ingest.yml"
```

Now, using customer and transaction data we will create a customer churn table that will give us the total count of churned and not churned customer.

```yaml title="customer-churn-ingestion.yml"
--8<-- "examples/products/data/sales_360/customer_churn.yml"
```

Alternatively you can also use the [dag](/resources/workflow/#workflow-and-directed-acyclic-graph-dag) of the workflows to run jobs in sequence in one manifest only.


#### **Create the Monitor for  observability of workflows**



#### **Data Profiling**

After Ingestion and transformation, it's necessary that we perform profiling and quality checks on our data as designed in the design phase.

```yaml title="customer-profiling-quality-checks.yml"
--8<-- "examples/products/data/sales_360/customer_profile.yml"
```

#### **Create the Monitor for observability of profiling**

```yaml title="customer-profiling-quality-checks.yml"
--8<-- "examples/products/data/sales_360/profile_monitor.yml"
```

#### **Data Quality Checks**

```yaml title="customer-profiling-quality-checks.yml"
--8<-- "examples/products/data/sales_360/profile_monitor.yml"
```


#### **Create the Bundle for applying all the resources**

```yaml
--8<-- "examples/products/data/sales_360/product_bundle.yml"
```

#### **Create the Data Product manifest file**

Here we will define our Input, Output  and transformations.

  - **Input** acts as an intermediary connecting diverse data sources. You can define as many input ports as you would like for each database. Here our input is depot that we define using UDL 

  - **Transformation** is where you enrich the data to make it more useable  accurate and realiable.

  -  **Output** is defined as our complete data product ready to be consumed and can also be delivered to different platforms for different purpose like streamlit and superset for data visualization, and lens for data modelling.

```yaml title="customer_data_product.yml"
--8<-- "examples/products/data/sales_360/sales_360_dp.yml"
```

## **Deploy**

Once you've created your data product with all its functionalities and insights, the next step is to ensure it reaches its intended audience through platforms like Metis and the Data Product Hub. To achieve this, running the Scanner becomes crucial.

```yaml title="scanner_sales360.yml"
--8<-- "examples/products/data/sales_360/product_scanner.yml"
```