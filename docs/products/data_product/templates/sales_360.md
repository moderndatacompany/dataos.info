## Design Phase

### **Define Use-case**

The use case for this particular example is to analyze the Sales Performance.

purpose: The sales 360 data product is a structured dataset that contains comprehensive information about various entitities within the organization. It serves as a central repository for products data, facilitating efficient management, analysis, and decision-making processes related to products operations, logistics, and customer engagement.

## Data Understanding and Exploration

In the design phase of a data product, we define the scope and structure of the data product and plan its development. For this project, we aim to create a Sales 360 data product that will integrate various tables from multiple sources. These sources must be connected to DataOS using Depot.

For example, the customer and transaction data is in the bigquery warehouse of the client. Other sources includes postgres and snowflake.


### **Create a Depot**

Creating a bigquery depot with json file of the credentails of the client's warehouse.

```yaml title="bigquery_depot.yml" hl_lines="18"
version: v1
name: "salesbq"
type: depot
tags:
  - dropzone
  - bigquery
layer: user
depot:
  type: BIGQUERY
  description: "Google Cloud BigQuery"
  spec:
    project: dataos-ck-res-yak-dev
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      files:
        json_keyfile: ./secrets/gcs-bq.json
```


<!-- 
```bash
dataos-ctl apply -f ${{yamlfilepath}}
``` -->


<aside class="callout">

🗣 Note that, to be able to create the depot you must have the necessary permissions. You can contact the DataOS operator of your organization. Also, you  can either use  Instace-secret Resource to abstract senistive passwords or use a JSON key file.

</aside>

### **Extract the Metadata**

To explore the metadata of the tables you can run a scanner. You can then access the metadata on Metis UI. The Scanner manifest file is shown below:

```yaml title="scanner.yml"
version: v1
name: scan-depot
type: workflow
tags:
  - Scanner
title: {{Scan snowflake-depot}}
description: |
  {{The purpose of this workflow is to scan S3 Depot.}}
workflow:
  dag:
    - name: scan-snowflake-db
      title: Scan snowflake db
      description: |
        {{The purpose of this job is to scan gateway db and see if the scanner works fine with an S3 type of depot.}}
      tags:
        - Scanner
      spec:
        stack: scanner:2.0
        compute: runnable-default
        stackSpec:
          depot: ${salesbq} # depot name
```
Replace the placeholder with the actual depot name.

### **Explore the Data**

Now for data exploration, you can query the data using the workbench. To query the data on the workbench without moving the data you first need to create a Minerva or a Themis cluster that will target the Depot. By applying the below manifest file, you can create the cluster.

```yaml title="cluster01.yml"
version: v1
name: advancedminerva
type: cluster
description: cluster testing
tags:
  - cluster
  - advancedminerva
cluster:
  compute: advanced-query
  runAsUser: minerva-cluster
  maintenance:
    restartCron: '13 1 */2 * *'
  minerva:
    selector:
      users:
        - "**"
      sources:
        - "**"
    replicas: 5
    resources:
      requests:
        cpu: 14000m
        memory: 52Gi
    debug:
      logLevel: INFO
      trinoLogLevel: DEBUG
    coordinatorEnvs:
      CONF__config__query.max-memory-per-node: "38GB"
      CONF__config__query.max-memory: "300GB"
      CONF__config__query.client.timeout: 2m
      CONF__config__query.max-execution-time: 5m #total time taken including queued time + execution time
      CONF__config__query.max-run-time: 3m  #total completion time for query

    workerEnvs:
      CONF__config__query.max-memory-per-node: "38GB"
      CONF__config__query.max-memory: "300GB"
      CONF__config__query.client.timeout: 12m
      CONF__config__query.max-execution-time: 25m    #total time taken including queued time + execution time
      CONF__config__query.max-run-time: 3m        #total completion time for query

    depots:
      - address: dataos://crmbq:sales_360

    catalogs:
      - name: cache
        type: memory
        properties:
          memory.max-data-per-node: "128MB"
```

### **Data Product Architectural Design**

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

### **Performance target**

**Response Time Goals:** Achieve 95% of queries processed within 500 milliseconds.
**Throughput Targets:** Sustain 1000 tasks per minute during peak periods.
**Resource Utilization Limits:** Ensure CPU usage remains below 80%.
**Quality Metrics:** Maintain data accuracy at 99%.
**Scalability Objectives:** Accommodate a 50% increase in data volume without additional infrastructure.
**Availability Standards:** Achieve 99.99% uptime monthly.

These targets guide system design and optimization efforts, ensuring technical capabilities meet business requirements for consistent performance and reliability.

### **Validation and Iteration**

After finalizing the design of the Data Product, it undergoes review sessions with key stakeholders and team members to verify compliance with defined requirements and goals. All modifications made during this phase are recorded to facilitate ongoing enhancements to the design.

Once the design aligns with requirements, the subsequent phase focuses on constructing the Data Product.

## Develop

This section involves the building phase of the Data Product right from data connection to defining SLOs. Here we will be using different resources and stacks and all other capabilities of DataOS.

Before, start creating resources for data product make sure you hae permissions or appropraite use-cases assigned.

## Steps to Create a Data Product

From the design phase and Data Product Architectural Design, it is clear which DataOS resources we require to build the Data Product, and these are Depot, Cluster, Scanner, Flare, Policy, SODA Checks and Bundle. Let’s see how to create each one step by step. As we already explored the data we’ll directly jump into the data transformation step using Flare.

### **Create the Flare Job for data ingestion and data transformation**

The code snippet below demonstrates a Workflow involving a single Flare batch job that reads the input dataset from the bigquery depot, performs transformation using Flare Stack, and stores the output dataset in the Icebase Depot.

Ingesting and transforming following tables:

1. customer
2. transaction
3. product

where the only transformation is to chnage the case to lower case of all.

```yaml title="transaction-ingests"
version: v1
name: wf-transaction-ingestion
type: workflows
tags:
  - demo.transaxtion
  - Tier.Gold
  - Domain.Sales
description: This workflow is responsible for ingesting transaxtion  for analysis and insights from poss3 into Icebase.
workflow:
  title: transaxtion Ingestion Workflow
  dag:
    - name: transaxtion-ingestion
      description: This workflow is responsible for ingesting transaxtion  for analysis and insights from poss3 into Icebase.
      title: transaxtion Ingestion Workflow
      spec:
        tags:
          - demo.transaxtion
        stack: flare:4.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 1200m
            cores: 1
            memory: 1024m
          executor:
            coreLimit: 1200m
            cores: 1
            instances: 1
            memory: 1024m
          job:
            explain: true
            inputs:
              - name: transaction_input
                dataset: dataos://crmbq:sales_360/transaction_data?acl=rw
                format: Bigquery

            logLevel: INFO
            outputs:
              - name: transaction_final_dataset
                dataset: dataos://icebase:sales_analytics/transaction_data?acl=rw
                format: Iceberg
                description: The transaxtion table is a structured dataset that contains comprehensive information about various transaxtion within the organization. It serves as a central repository for transaxtion data, facilitating efficient management, analysis, and decision-making processes related to transaxtion operations, logistics, and transaxtion engagement.
                tags:
                   - demo.transaxtion
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                title: transaxtion set Ingestion
            steps:
              - sequence:
                  - name: transaction_final_dataset
                    sql: |
                      select * from transaction_input
                    functions:
                      - name: cleanse_column_names
                      - name: change_column_case
                        case: lower
```

```yaml title="customer-ingest.yml"
version: v1
name: wf-customer-ingestion
type: workflow
tags:
  - demo.customer
  - Tier.Gold
  - Domain.Sales
description: This workflow is responsible for ingesting customer  for analysis and insights from poss3 into Icebase.
workflow:
  title: customer Ingestion Workflow
  dag:
    - name: customer-ingestion
      description: This workflow is responsible for ingesting customer  for analysis and insights from poss3 into Icebase.
      title: customer Ingestion Workflow
      spec:
        tags:
          - demo.customer
        stack: flare:4.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 1200m
            cores: 1
            memory: 1024m
          executor:
            coreLimit: 1200m
            cores: 1
            instances: 1
            memory: 1024m
          job:
            explain: true
            inputs:
              - name: customer_input
                dataset: dataos://crmbq:sales_360/customer_data?acl=rw
                format: Iceberg

            logLevel: INFO
            outputs:
              - name: customer_final_dataset
                dataset: dataos://icebase:sales_analytics/customer_data?acl=rw
                format: Iceberg
                description: The customer table is a structured dataset that contains comprehensive information about various customer within the organization. It serves as a central repository for customer data, facilitating efficient management, analysis, and decision-making processes related to customer operations, logistics, and customer engagement.
                tags:
                   - demo.customer
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                title: customer set Ingestion
            steps:
              - sequence:
                  - name: customer_final_dataset
                    sql: |
                      select * from customer_input
                    functions:
                      - name: cleanse_column_names
                      - name: change_column_case
                        case: lower
```

```yaml title="product-ingestion.yml"
version: v1
name: wf-products-ingestion
type: workflow
tags:
  - demo.products
  - Tier.Gold
  - Domain.Sales
description: This workflow is responsible for ingesting products  for analysis and insights from poss3 into Icebase.
workflow:
  title: products Ingestion Workflow
  dag:
    - name: products-ingestion
      description: This workflow is responsible for ingesting products  for analysis and insights from poss3 into Icebase.
      title: products Ingestion Workflow
      spec:
        tags:
          - demo.products
        stack: flare:4.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 1200m
            cores: 1
            memory: 1024m
          executor:
            coreLimit: 1200m
            cores: 1
            instances: 1
            memory: 1024m
          job:
            explain: true
            inputs:
            - name: product_data
              dataset: dataos://snowflake:public/product
              format: snowflake
              options:
                sfWarehouse: "compute_wh"

            logLevel: INFO
            outputs:
              - name: products_final_dataset
                dataset: dataos://icebase:sales_analytics/products?acl=rw
                format: Iceberg
                description: The products table is a structured dataset that contains comprehensive information about various products within the organization. It serves as a central repository for products data, facilitating efficient management, analysis, and decision-making processes related to products operations, logistics, and customer engagement.
                tags:
                   - demo.products
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                title: products set Ingestion
            steps:
              - sequence:
                  - name: products_final_dataset
                    sql: |
                      SELECT
                        *
                      FROM
                        products_input
                    functions:
                      - name: cleanse_column_names
                      - name: change_column_case
                        case: lower
```

Now, using customer and transaction data we will create a customer churn table that will give us the total count of churned and not churned customer.

```yaml title="customer-churn-ingestion.yml"
version: v1
name: wf-customer-churn-ingestion
type: workflow
tags:
  - demo.customer
  - Tier.Gold
  - Domain.Sales
description: This workflow is responsible for ingesting customer  for analysis and insights from poss3 into Icebase.
workflow:
  title: customer Ingestion Workflow
  dag:
    - name: customer-ingestion
      description: This workflow is responsible for ingesting customer  for analysis and insights from poss3 into Icebase.
      title: customer Ingestion Workflow
      spec:
        tags:
          - demo.customer
        stack: flare:4.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 1200m
            cores: 1
            memory: 1024m
          executor:
            coreLimit: 1200m
            cores: 1
            instances: 1
            memory: 1024m
          job:
            explain: true
            inputs:
              - name: transactions_input
                dataset: dataos://bigquery:sales_360/transaction_data?acl=rw

              - name: customer_input
                dataset: dataos://icebase:sales_analytics/customer_data?acl=rw
                format: Iceberg

            logLevel: INFO
            outputs:
              - name: customer_final_dataset
                dataset: dataos://icebase:sales_analytics/customer_churn?acl=rw
                format: Iceberg
                description: The customer table is a structured dataset that contains comprehensive information about various customer within the organization. It serves as a central repository for customer data, facilitating efficient management, analysis, and decision-making processes related to customer operations, logistics, and customer engagement.
                tags:
                   - demo.customer
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                title: customer set Ingestion
            steps:
              - sequence:
                  - name: customer_final_dataset
                    sql: |
                      WITH customer_activity AS (
                        SELECT
                            c.customer_id,
                            MAX(t.transaction_date) AS last_transaction_date
                        FROM
                            customer_input c
                        LEFT JOIN
                            transactions_input t ON cast(c.customer_id as string) = t.customer_id
                        GROUP BY
                            c.customer_id
                        )

                        SELECT
                            CASE
                                WHEN last_transaction_date < DATE_SUB(CURRENT_DATE, 90) THEN 'Churned'
                                ELSE 'Not Churned'
                            END AS churn_status,
                            COUNT(*) AS customer_count
                        FROM
                            customer_activity
                        GROUP BY
                            CASE
                                WHEN last_transaction_date < DATE_SUB(CURRENT_DATE, 90) THEN 'Churned'
                                ELSE 'Not Churned'
                            END
                    functions:
                      - name: cleanse_column_names
                      - name: change_column_case
                        case: lower
```

For the orders data we will apply a complex join of multiple tables.

```yaml title="orders-ingestion.yml"
version: v1
name: wf-order-enriched-data
type: workflow
tags:
  - company.order_enriched
  - Tier.Gold
  - Domain.Finance
description: The job is to ingest order enriched data for company Retail Accelerator from Multiple Source into Icebase.
workflow:
  title: Order Enriched Data
  dag:
    - name: order-enriched-data
      description: The job is to ingest order enriched data for company Retail Accelerator from Multiple Source into Icebase.
      title: Order Enriched Data
      spec:
        tags:
          - company.order_enriched
        stack: flare:4.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 2200m
            cores: 2
            memory: 2824m
          executor:
            coreLimit: 3200m    
            cores: 2
            instances: 2
            memory: 4024m
          job:
            explain: true
            inputs:
              - name: transactions
                dataset: dataos://bigquery:sales_360/transaction?acl=rw

              - name: order_data
                dataset: dataos://postgres:retail_accelerator/order_data?acl=rw
                options:
                  driver: org.postgresql.Driver

              - name: order_line_item
                dataset: dataos://postgres:retail_accelerator/order_line_item?acl=rw
                options:
                  driver: org.postgresql.Driver

              - name: product
                dataset: dataos://bigquery:sales_360/product?acl=rw

              - name: customer
                dataset: dataos://bigquery:sales_360/customers?acl=rw  

            logLevel: INFO
            outputs:
              - name: final
                dataset: dataos://icebase:sales_analytics/order_enriched?acl=rw
                format: Iceberg
                description: The "order_enriched" table contains a dataset that has been augmented with additional information to provide deeper insights or to support more comprehensive analyses. This enrichment process involves integrating supplementary data from various sources or applying data transformation and enhancement techniques to the original dataset. Here are some common characteristics of an enriched table.
                tags:
                  - company.order_enriched
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                title: order enriched data

            steps:
              - sequence:
                  - name: transaction
                    sql: |
                      SELECT
                        transaction_id,
                        customer_id,
                        transaction_date,
                        order_id,
                        transaction_amount,
                        payment_method
                      FROM
                        transactions
                      WHERE
                        transaction_date <= CURRENT_TIMESTAMP
                        AND year(transaction_date) = 2024
                    functions:
                      - name: cleanse_column_names
                      - name: change_column_case 
                        case: lower

                  - name: orders
                    sql: |
                      SELECT
                        o.order_id,
                        customer_id,
                        o.order_date,
                        olt.productsku,
                        order_delivery_date,
                        order_total_amount,
                        shipping_method,
                        order_status
                      FROM
                        order_data o
                        LEFT JOIN order_line_item olt ON o.order_id = olt.order_id
                      WHERE
                        o.order_date <= CURRENT_TIMESTAMP
                        AND year(o.order_date) = 2024
                    functions:
                      - name: cleanse_column_names
                      - name: change_column_case 
                        case: lower


                  - name: order_trans
                    sql: |
                      SELECT
                        o.order_id,
                        o.customer_id,
                        o.productsku ,
                        o.order_date,
                        order_delivery_date,
                        order_total_amount,
                        shipping_method,
                        order_status,
                        transaction_id,
                        transaction_date,
                        transaction_amount,
                        payment_method,
                        product_category,
                        model_name,
                        brand_name,
                        product_name,
                        product_size
                      FROM
                        orders o
                        LEFT JOIN transaction t ON o.order_id = t.order_id
                        LEFT JOIN product p ON o.productsku = p.sku_id 
                    functions:
                      - name: cleanse_column_names
                      - name: change_column_case 
                        case: lower

                  - name: final
                    sql: |
                      SELECT
                        order_id,
                        ot.customer_id,
                        productsku ,
                        cast(order_date as timestamp) as order_date,
                        cast(order_delivery_date as timestamp) as order_delivery_date,
                        cast(order_total_amount as double) as order_total_amount,
                        shipping_method,
                        order_status,
                        transaction_id,
                        cast(transaction_date as timestamp) as transaction_date,
                        cast(transaction_amount as timestamp) as transaction_amount,
                        payment_method,
                        product_category,
                        model_name,
                        brand_name,
                        product_name,
                        product_size
                        first_name,
                        last_name,
                        gender,
                        phone_number,
                        email_id,
                        cast(age as int) as age,
                        city,
                        state,
                        country,
                        zip_code
                      FROM
                        order_trans ot
                        LEFT JOIN customer c ON ot.customer_id = c.customer_id
                    functions:
                      - name: cleanse_column_names
                      - name: change_column_case 
                        case: lower
```

### **Data Profiling and Quality checks**

After Ingestion and transformation, it's necessary that we perform profiling and quality checks on our data as designed in the design phase.


```yaml title="customer-profiling-quality-checks.yml"
name: wf-customer-churn-quality
version: v1
type: workflow
tags:
  - demo.customer-churn
  - Tier.Gold
  - Domain.Finance
description: The role involves conducting thorough and detailed quality analysis, including data assertion, of extensive customer churn data using the advanced features of the DataOS platform.
workspace: public
workflow:
  schedule:
    cron: '*/2 * * * *'
    concurrencyPolicy: Forbid
  dag:
    - name: customer-churn
      description: The role involves conducting thorough and detailed quality analysis, including data assertion, of customer churn enriched data using the advanced features of the DataOS platform.
      title: Customer Churn Quality Assertion 
      spec:
        stack:  soda+python:1.0 
        logLevel: INFO
        compute: runnable-default
        resources:
          requests:
            cpu: 1000m
            memory: 250Mi
          limits:
            cpu: 1000m
            memory: 250Mi
        stackSpec:
          inputs:
            - dataset: dataos://icebase:sales_analytics/customer_churn?acl=rw
              options:
                engine: minerva
                clusterName: system   
              checks:
              checks:
                - invalid_count(churn_status) <= 0:
                    valid regex: \b(?:Churned|Not Churned)\b

                - missing_count(churn_status) = 0 

                - missing_count(customer_count) = 0

                - schema:
                    name: Confirm that required columns are present
                    warn:
                      when required column missing: [churn_status, customer_count]
                    fail:
                      when required column missing:
                        - churn_status
                        - customer_count  
```

```yaml title="transaction-profiling-quality-checks.yml"
name: profile-transaction-data
version: v1
type: workflow
tags:
  - profile
description: this jobs profile data
workspace: public
workflow:
  dag:
    - name: sample-profile-soda-01
      title: Sample profile data
      spec:
        stack: soda+python:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 1000m
            memory: 250Mi
          limits:
            cpu: 1000m
            memory: 250Mi
        logLevel: INFO # WARNING, ERROR, DEBUG
        stackSpec:  
          inputs:
            - dataset: dataos://icebase:sales_analytics/transaction_data
              options:
                engine: minerva
                clusterName: system
              checks:
                - row_count between 10 and 10000
                - missing_count(transaction_id) = 0
                # - invalid_percent(phone_number) < 1 %:
                #     valid format: 603-706-2239
                - invalid_count(discount_percentage) = 0:
                    valid min: 0
                    valid max: 50
                - duplicate_count(transaction_id) = 0
                - schema:
                    name: Confirm that required columns are present
                    warn:
                      when required column missing: [transaction_date]
                    fail:
                      when required column missing: [order_id]
              profile:
                columns:
                  - "*"
            
```

```yaml title="orders-enriched-qualitychecks.yml"
name: wf-order-enriched-quality
version: v1
type: workflow
tags:
  - demo.orders
  - Tier.Gold
  - Domain.Finance
description: The role involves conducting thorough and detailed quality analysis, including data assertion, of extensive order enriched data using the advanced features of the DataOS platform.
workspace: public
workflow:
  schedule:
    cron: '*/2 * * * *'
    concurrencyPolicy: Forbid
  dag:
    - name: order-enriched
      description: The role involves conducting thorough and detailed quality analysis, including data assertion, of extensive order enriched data using the advanced features of the DataOS platform.
      title: Order Enriched Quality Assertion 
      spec:
        stack:  soda+python:1.0 
        logLevel: INFO
        compute: runnable-default
        resources:
          requests:
            cpu: 1000m
            memory: 250Mi
          limits:
            cpu: 1000m
            memory: 250Mi
        stackSpec:
          inputs:
            - dataset: dataos://icebase:sales_analytics/order_enriched?acl=rw
              options:
                engine: minerva
                clusterName: system   
              checks:
              checks:
                # - invalid_count(customer_id) = 0:
                #     valid regex: ^[A-Za-z0-9]{5}$

                - invalid_count(payment_method) <= 0:
                    valid regex: \b(?:Credit Card|Apple Pay|Debit Card|COD|PayPal)\b                

                - invalid_count(productsku) <= 0:
                    valid regex: ^SKU\d{7}$
                  
                - invalid_percent(email_id) < 10%:
                    valid regex: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

                - invalid_count(order_status) <= 0:
                    valid regex: \b(?:Delivered|Shipped|Processing|Canceled)\b                       

                - schema:
                    name: Confirm that required columns are present
                    warn:
                      when required column missing: [order_id, customer_id, order_status]
                    fail:
                      when required column missing:
                        - order_id
                        - customer_id
                        - productsku  
```

### **Create the Bundle for applying all the resources**

```yaml
# Resource meta section
name: dp-bundle
version: v1beta
type: bundle
layer: user 
tags: 
  - dataos:type:resource
description: this bundle resource is for a data product

# Bundle-specific section
bundle:

  # Bundle Workspaces section
  workspaces:
    - name: bundlespace1 # Workspace name (mandatory)
      description: this is a bundle workspace # Workspace description (optional)
      tags: # Workspace tags (optional)
        - bundle
        - sales_360
      labels: # Workspace labels (optional)
        purpose: testing
      layer: user # Workspace layer (mandatory)

  # Bundle Resources section
  resources:
    - id: flare-job
      file: /home/sales_360/data_products/flare.yaml
      
    - id: soda checks
      file: /home/sales_360/data_products/checks.yaml
      dependencies:
        - flare-job    
  # Manage As User
  manageAsUser: iamgroot
```

### **Create the Data Product manifest file**

After successfully executing the Bundle manifest, you’ll create a manifest file for the Data Product to which the bundle will be referred. 

Here we will define our Input, Output  and transformations.

The **Input** acts as an intermediary connecting diverse data sources. You can define as many input ports as you would like for each database. Here our input is depot that we define using UDL 

**Transformation** is where you enrich the data to make it more useable  accurate and realiable.

The **Output** is defined as our complete data product ready to be consumed and can also be delivered to different platforms for different purpose like streamlit and superset for data visualization, and lens for data modelling.

```yaml title="data_product.yml"
# Product meta section
name: sales_360 # Product name (mandatory)
version: v1alpha # Manifest version (mandatory)
type: data # Product-type (mandatory)
tags: # Tags (Optional)
  - data-product
  - dataos:type:product
  - dataos:product:data
description: the 360 view of the sales # Description of the product (Optional)
Purpose: This data product is intended to provide insights into the salesp for strategic decisions on cross-selling additional products. # purpose (Optional)
collaborators: # collaborators User ID (Optional)
  - thor
  - blackwidow
  - loki
owner: iamgroot # Owner (Optional)
refs: # Reference (Optional)
  - title: Data Product Hub # Reference title (Mandatory if adding reference)
    href: https://liberal-donkey.dataos.app/dph/data-products/all # Reference link (Mandatory if adding reference)
entity: product # Entity (Mandatory)
# Data Product-specific section (Mandatory)
v1alpha: # Data Product version
  data:
    resources: # Resource specific section(Mandatory)
      - name: bundle-dp # Resource name (Mandatory)
        type: bundle # Resource type (Mandatory)
        version: v1beta # Resource version (Mandatory)
        refType: dataos # Resource reference type (Mandatory)
        workspace: public # Workspace (Requirement depends on the resource type)
        description: this bundle resource is for a data product # Resource description (Optional)
        purpose: deployment of data product resources # Purpose of the required resource (Optional)   
    
    inputs:
      - description: S3 Depot
        purpose: source
        refType: dataos
        ref: dataos://s3depot:none/ga_data/
    
    outputs:
      - description: Icebase Depot
        purpose: consumption
        refType: dataos_address
        ref: dataos://icebase:google_analytics/ga_sessions_daily_data_raw    

```

## **Deploy**

Once you've created your data product with all its functionalities and insights, the next step is to ensure it reaches its intended audience through platforms like Metis and the Data Product Hub. To achieve this, running the Scanner becomes crucial.

```yaml title="scanner_sales360.yml"
```