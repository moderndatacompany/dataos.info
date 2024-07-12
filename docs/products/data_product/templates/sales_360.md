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


<center> ![Architectural Diagram](/products/data_product/templates/architecture.png) </center> 

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

using super [dag](/resources/workflow/#workflow-and-directed-acyclic-graph-dag) where the only transformation is to change the case to lower case of all.

```yaml title="ingestion_super_dag.yml"
--8<-- "examples/products/data/sales_360/dag/ingestion.yml"
```

Here are the all mentioned ingested manifest files:

<details>
  <summary>config-customer-flare manifest file</summary>

```yaml title="transaction-ingests.yml"
--8<-- "examples/products/data/sales_360/customer_ingest.yml"
```
</details>


<details>
  <summary>config-transactions-flare manifest file</summary>

```yaml title="customer-ingest.yml"
--8<-- "examples/products/data/sales_360/transaction_ingest.yml"
```
</details>


<details>
  <summary>config-products-flare manifest file</summary>

```yaml title="product-ingestion.yml"
--8<-- "examples/products/data/sales_360/product_ingest.yml"
```
</details>


Now, using customer and transaction data we will create a customer churn table that will give us the total count of churned and not churned customer.

<details>
  <summary>config-customer-churn-flare manifest file</summary>

```yaml title="customer-churn-ingestion.yml"
--8<-- "examples/products/data/sales_360/customer_churn.yml"
```
</details>

#### **Create the Monitor and Pager for  observability of workflows**

<details>
  <summary>flare-transformation-and-ingestion-monitor manifest file</summary>

```yaml title="transformation_and_ingestion_monitor.yml"
--8<-- "examples/products/data/sales_360/observability/monitor/ingestion-monitor.yml"
```
</details>

<details>
  <summary>flare-transformation-and-ingestion-pager manifest file</summary>

```yaml title="transformation_and_ingestion_pager.yml"
--8<-- "examples/products/data/sales_360/observability/pagers/workflow_pager.yml"
```
</details>


#### **Data Profiling**

After Ingestion and transformation, it's necessary that we perform profiling and quality checks on our data as designed in the design phase.

```yaml title="profiling_super_dag.yml"
--8<-- "examples/products/data/sales_360/dag/profiling.yml"
```
Here are all the mentioned profiling manifest files:

<details>
  <summary>customer-profile manifest file</summary>

```yaml title="customer-profiling.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/customer_profile.yml"
```
</details>

<details>
  <summary>transactions-profile manifest file</summary>

```yaml title="transactions-profiling.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/transaction_profile.yml"
```
</details>

<details>
  <summary>products-profile manifest file</summary>

```yaml title="products-profiling.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/products_profile.yml"
```
</details>


#### **Create the Monitor and Pager for observability of profiling**

<details>
  <summary>profiling-monitor manifest file</summary>

```yaml title="profiling_monitor.yml"
--8<-- "examples/products/data/sales_360/profile_monitor.yml"
```
</details>

<details>
  <summary>profiling-monitor manifest file</summary>

```yaml title="profiling_pager.yml"
--8<-- "examples/products/data/sales_360/observability/pagers/profile_pager.yml"
```
</details>



#### **Data Quality Checks**



```yaml title="quality_checks_super_dag.yml"
--8<-- "examples/products/data/sales_360/dag/quality_checks.yml"
```

Here are all the mentioned quality checks manifest files:


<details>
  <summary>customer-quality-checks manifest file</summary>

```yaml title="customer_quality.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/customer_quality.yml"
```
</details>

<details>
  <summary>transactions-quality-checks manifest file</summary>

```yaml title="transactions_quality.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/transaction_quality.yml"
```
</details>

<details>
  <summary>products-quality-checks manifest file</summary>

```yaml title="products_quality.yml"
--8<-- "examples/products/data/sales_360/profiling_quality/products_quality.yml"
```
</details>


#### **Create the Monitor and Pager for observability of quality checks**

<details>
  <summary>quality-monitor manifest file</summary>

```yaml title="quality_monitor.yml"
--8<-- "examples/products/data/sales_360/observability/monitor/quality_monitor.yml"
```
</details>

<details>
  <summary>quality-pager manifest file</summary>

```yaml title="quality_pager.yml"
--8<-- "examples/products/data/sales_360/observability/pagers/quality_pager.yml"
```
</details>


#### **Create the Streamlit App for Data Consumer**

This streamlit app will give you the details  of churned and not  churned customers so that all the customers who are going to churned can be retained bby contacting them and giving them special discounts.

<details>
  <summary>streamlit-app manifest file</summary>

```yaml title="app.py"
--8<-- "examples/products/data/sales_360/customer_churn.py"
```
</details>

**The Output:**

<center> ![Streamlit](/products/data_product/templates/streamlit.png) </center>

<center> The Streamit App for Customer Churn Details </center>

#### **Create the Data Product manifest file**

Here we will define our Input, Output  and transformations.

  - **Input** acts as an intermediary connecting diverse data sources. You can define as many input ports as you would like for each database. Here our input is bigquery depot.

  - **Transformation** is where you enrich the data to make it more useable  accurate and realiable. The stack we used for transformation is **`flare`**. The transformation stops involved were:

    - **Read Input from BigQuery:** Ingest raw data as is from Bigquery, with the only transformation being the conversion of cases to lower case.

    - **Joined Customer and Transaction Tables:** Integrated data from the Customer and Transaction tables to identify customer-churn.
    
  -  **Output** is defined as our complete data product ready to be consumed and can also be delivered to different platforms for different purpose like streamlit and [superset](/interfaces/superset) for data visualization, and [lens](/interfaces/lens) for data modeling.

```yaml title="customer_data_product.yml"
--8<-- "examples/products/data/sales_360/sales_360_dp.yml"
```

## **Deploy**

Once you've created your data product with all its functionalities and insights, the next step is to ensure it reaches its intended audience through platforms like Metis and the Data Product Hub. To achieve this, running the Scanner becomes crucial.

```yaml title="scanner_sales360.yml"
--8<-- "examples/products/data/sales_360/product_scanner.yml"
```

Now, you can see your newly created data product in [DPH](/interfaces/data_product_hub)


## **Iterate**

Iterating a Data Product involves refining and enhancing it based on feedback, performance metrics, and evolving business requirements. If you need to iterate your Data Product based on feedback from data consumers, follow these steps:

  - Collect Feedback: Gather feedback from users and stakeholders regarding the Data Product's performance, usability, and effectiveness in solving the intended problem.

  - Analyze Feedback: Identify common issues and suggestions for improvements. Prioritize these based on impact and feasibility.

  - Plan Iteration: Define the scope of changes needed to address the feedback. Create a plan that includes tasks, timelines, and resources required for the iteration.

  - Implement Changes: Update the Data Product according to the iteration plan. This might involve modifying data sources, transformation logic, data models, or visualization techniques.

  - Validate Changes: Ensure that the changes meet the intended goals and do not introduce new issues. Validate the updated Data Product through testing and user acceptance.

  - Deploy Updated Product: Deploy the updated Data Product to the production environment.

  - Monitor and Iterate Again: After deployment, monitor the Data Product's performance and continue to collect feedback. Iterate the process as needed to achieve the desired results.

By following these steps, you can continuously improve your Data Product to better meet user needs and business objectives.