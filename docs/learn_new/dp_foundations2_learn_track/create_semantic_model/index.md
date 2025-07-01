# Build a semantic model 

This guide outlines the end-to-end process for building and deploying a semantic model (Lens) For your data product. 

## Scenario

After you've established data connections and built robust data pipelines to process and transform raw data, the next step is to create a semantic model (Lens). Your objective is to transform raw data into a structured model that enables the generation of trusted, consistent metrics and KPIs. These metrics will be accessible through APIs and usable across business intelligence, AI, and embedded analytics tools.

## Quick concepts

Semantic models aim to represent data in a way that is easily understandable by business users. They provide a logical structure that defines key entities, their relationships.

**Importance of semantic models:**

- **Improved Data Accessibility:** Semantic models present data in a understandable way, using a common business language that enables users of all technical levels to access and use data effectively, promoting self-service in data product development.
- **Enhanced Data Discovery:** By organizing data clearly, semantic models simplify the process of discovering and exploring data, especially in large or complex datasets, helping users quickly find relevant information.
- **Easier Data Integration:** Semantic models define common meanings and relationships between data elements, making it easier to integrate and maintain consistency across various data sources and systems.
- **Support for Data Governance:** These models enforce data quality standards, ensuring accuracy and reliability, which is essential for regulatory compliance and maintaining trust in data products.
- **Empowering Business Users:** By simplifying technical complexities, semantic models allow business users to access and analyze data independently, fostering a data-driven culture and reducing reliance on IT teams.

Based on the identified goals of analysis, value objectives, and the key factors or drivers that will influence our value objectives, create the semantic model with the following steps.

<aside>

You can create semantic models directly from structured sources. However, if data comes from multiple or unstructured sources, you may need to collect, clean, and transform it into a usable format.

</aside>

## Creating the semantic model

Once your conceptual model is finalized, the next step is to implement it within the Lens framework. This process involves setting up a clear Lens folder structure, defining SQL scripts for data extraction, organizing tables, and implementing dimensions, measures, and metrics to reflect your business logic.

### **Step 1: Set Up the Semantic Model Folder Structure**

A well-structured directory is key to managing your model components.

🎯 Your Action:

Set up your model folder:

```

semantic_model
├── sqls
│   ├── customer.sql
│   ├── product.sql
│   └── purchase.sql
├── tables
│   ├── customer.yml
│   ├── product.yml
│   └── purchase.yml
├── views
│   ├── total_spend.yml
│   ├── purchase_frequency.yml
│   └── cross_sell_opportunities.yml
└── user_groups.yml

```

### **Step 2: Write SQL Scripts for Tables**

These SQL scripts extract relevant fields from your input datasets.

🎯 **Your Actions:**

1. Create SQL scripts for each entity.
2. Add SQL files to the `sqls` folder.

??? "customer.sql"

    ```sql
    # Replace xx with your initials
    SELECT 
        customer_id, 
        birth_year, 
        education, 
        marital_status, 
        income, 
        country 
    FROM 
        postgres.public.customer_data
    ```

??? "product.sql"
    ```sql
    # Replace xx with your initials
    select 
        customer_id as product_customer_id,
        product_id,
        product_category,
        product_name,
        price
    FROM
        postgresxx.public.product_data
    ```

??? "purchase.sql"

    ```sql
    # Replace xx with your initials
    SELECT
        customer_id as p_customer_id,
        cast(purchase_date as timestamp) as purchase_date,
        recency as recency_in_days,
        mntwines,
        mntmeatproducts,
        mntfishproducts,
        mntsweetproducts,
        mntgoldprods,
        mntfruits,
        numdealspurchases,
        numwebpurchases,
        numcatalogpurchases,
        numstorepurchases,
        numwebvisitsmonth,
        numwebpurchases + numcatalogpurchases + numstorepurchases + numstorepurchases as purchases,
        (mntwines+mntmeatproducts+mntfishproducts+mntsweetproducts+mntgoldprods+mntfruits) as spend
    FROM
        postgresxx.public.purchase_data
    ```


### **Step 3: Define Manifest Files for Tables**

This `tables` folder contains logical table definitions in YAML format. These definitions help structure your data into business entities.

#### **1. Table definition section**

This is the foundational section where you define the core table properties.

- **name:** Specifies the table name.

- **sql**: Points to the SQL defined in the `/sql` folder. for example: `customer.sql`

- **description:** Provides context about the table.

- **public:** Indicates whether the table is publicly accessible.

After defining the base table, you define measures, dimensions, joins and segments to provide meaningful analysis. Each section serves a specific purpose to ensure a well-structured and accessible data model.

#### **2. Joins section**

Defines relationships between tables, enabling connected data insights. The relationship could be `one-to-one`, `one-to-many`.

- **name:** The name of the table being joined.

- **relationship:** Specifies the relationship type (e.g., one-to-many).

- **sql:** Defines the join condition in SQL syntax.


#### **3. Dimensions section**

The Dimension section captures the attributes or fields of the table, detailing metadata and properties for each dimension. These attributes provide critical context and usability for downstream analysis. Here, you add (attributes like `customer_id`, `product_id`).

- **name:** Specifies the name of the dimension.

- **type:** Defines the data type of the dimension (e.g., number, string).

- **column:** Maps the dimension to the corresponding database column.

- **description:** Provides a brief explanation of the dimension.

- **primary_key:** Indicates whether the dimension is a primary key.

- **public:** Specifies if the dimension is publicly accessible.

- **meta.secure:** Ensures sensitive data is masked for specified user groups.

- **sql:** Custom SQL logic to create derived dimensions.

#### **4. Measures section**

The Measure section defines aggregated metrics derived from the table data  such as `total_customers`, `total_products`. These measures provide quantitative insights and often include policies to protect sensitive information. 

- **name:** Specifies the measure name.

- **sql:** Contains the aggregation logic.

- **type:** Indicates the data type of the measure (e.g., number, string).

- **description:** Provides additional details about the measure.

- **secure:** Highlights measures that include data policy logic to protect sensitive information. For instance, in the `customer` table a data policy is applied to secure the maritial_status column of the `product` table. The applied data policy redacts the data from the users in the ‘dataconsumer’ group. 


#### **5. Segments section**

The Segments section defines filters or conditions that segment data based on specific criteria, enabling the creation of subsets of the dataset for more granular analysis. Segments are often used to focus on specific groups of data that meet certain conditions, like customers from a particular region or products from a certain category.

In the YAML manifest, each segment is defined by:

- **name:** Specifies the segment's name, which serves as an identifier for the condition or subset of data. 

- **sql:** Contains the SQL logic or condition that defines the segment. The SQL condition is used to filter the data, ensuring that only the records that meet the condition are included in the segment. In the provided YAML example, the condition is {TABLE}.state = 'Illinois', which means only rows where the state column equals "Illinois" will be included in this segment.


🎯 **Your actions:**

1. In the tables folder, define logical table definitions in YAML format. The templates show how to define tables referencing the SQL scripts created in the previous step and defining dimensions, joins, measures, and segments.
2. Add these files to the `tables` folder.

<details>
<summary>Click to view YAML definition for the `customer` table</summary>

```yaml
tables:
  - name: customer
    sql: {{ load_sql('customer') }}
    description: "This table stores key details about the customers, including their personal information, income, and classification into different risk segments. It serves as the central reference point for customer-related insights."
    public: true

    joins:
      - name: purchase
        relationship: one_to_many
        sql: "{TABLE.customer_id}= {purchase.p_customer_id}"
        
    dimensions:   
      - name: customer_id
        type: number
        column: customer_id
        description: "The unique identifier for each customer."
        primary_key: true
        public: true


      - name: birth_year
        type: number
        column: birth_year
        description: "The birth year of the customer, used for demographic analysis and customer segmentation."

      - name: education
        type: string
        column: education
        description: "The educational level of the customer, which could be used for profiling and targeted campaigns."

      - name: marital_status
        type: string
        column: marital_status
        description: "The marital status of the customer, which may provide insights into purchasing behavior and lifestyle preferences."

      - name: income
        type: number
        column: income
        description: "The annual income of the customer in the local currency, which is often a key factor in market segmentation and purchasing power analysis."

      - name: country
        type: string
        column: country
        description: "The country where the customer resides, providing geographic segmentation and analysis opportunities."

      - name: customer_segments
        type: string
        sql: >
          CASE 
              WHEN random() < 0.33 THEN 'High Risk'
              WHEN random() < 0.66 THEN 'Moderate Risk'
              ELSE 'Low Risk'
          END AS 
        description: "Risk-based customer segments derived from the customer_id, used to categorize customers into high, moderate, and low risk groups for targeted campaigns or analysis."

    measures:
      - name: total_customers
        sql: "COUNT( Distinct {customer_id})"
        type: number
        description: "The total number of customers in the dataset, used as a basic measure of customer volume."

    segments:
      - name: country_india
        sql: country = 'India'
        description: This segment filters customers by a specific country India.
        meta:
          secure:
            user_groups:
              includes:
                - india
              excludes: 
                - default

      - name: country_usa
        sql: country = 'USA'
        description: This segment filters customers by a specific country USA.
        meta:
          secure:
            user_groups:
              includes:
                - usa
              excludes: 
                - default

```

</details>

<details>
<summary>Click to view YAML definition for the `product` table</summary>

```yaml
<details>
<summary>Click to view YAML definition for the `product` table</summary>

```yaml
tables:
  - name: product
    sql: {{ load_sql('product') }}
    description: "This table stores the product information."
    public: true
    dimensions:   
      - name: product_customer_id
        type: string
        column: product_customer_id
        description: "The unique identifier representing the combination of a customer and a product."

      - name: product_id
        type: string
        column: product_id
        description: "The unique identifier for the product associated with a customer."
        primary_key: true

      - name: product_category
        type: string
        column: product_category
        description: "The category of the product, such as Wines, Meats, Fish, etc."

      - name: product_name
        type: string
        column: product_name
        description: "The name of the product associated with the customer."

      - name: price
        type: number
        column: price
        description: "The price of the product assigned to the customer, in monetary units."

      - name: product_affinity_score
        sql: ROUND(50 + random() * 50, 2) 
        type: number
        description: "customer who purchases one product category will also purchase another category."

      - name: purchase_channel
        type: string
        sql: >
          CASE 
              WHEN random() < 0.33 THEN 'Web'
              WHEN random() < 0.66 THEN 'Store'
              ELSE 'Catalog'
          END
        description: "Describes how the purchase was made (e.g., Web, Store, Catalog)."
      
    measures:
      - name: total_products
        sql: product_id
        type: count_distinct
        description: "The number of products."
</details>


<details>
<summary>Click to view YAML definition for the `purchase.yaml` table</summary>

```yaml
tables:
  - name: purchase
    sql: {{ load_sql('purchase') }}
    description: "This table captures detailed purchase behavior of customers, including their transaction frequency, product category spends, and web interaction history. It serves as the foundation for customer segmentation, recency analysis, and churn prediction."
    public: true
    joins:
      - name: product
        relationship: many_to_one
        sql: "{TABLE.p_customer_id} = {product.product_customer_id} "

    dimensions:   
      - name: p_customer_id
        type: number
        column: p_customer_id
        description: "The unique identifier for a customer."
        primary_key: true


      - name: purchase_date
        type: time
        column: purchase_date
        description: "The date when the customer made their last purchase."

      - name: recency_in_days
        type: number
        column: recency_in_days
        description: "The number of days since the customer’s last purchase."
        public: false

      - name: mntwines
        type: number
        column: mntwines
        description: "The total amount spent by the customer on wine products."
        public: false

      - name: mntmeatproducts
        type: number
        column: mntmeatproducts
        description: "The total amount spent by the customer on meat products."
        public: false

      - name: mntfishproducts
        type: number
        column: mntfishproducts
        description: "The total amount spent by the customer on fish products."
        public: false

      - name: mntsweetproducts
        type: number
        column: mntsweetproducts
        description: "The total amount spent by the customer on sweet products."
        public: false

      - name: mntgoldprods
        type: number
        column: mntgoldprods
        description: "The total amount spent by the customer on gold products."
        public: false

      - name: mntfruits
        type: number
        column: mntfruits
        description: "The total amount spent by the customer on fruit products."
        public: false

      - name: numdealspurchases
        type: number
        column: numdealspurchases
        description: "The number of purchases made by the customer using deals or discounts."
        public: false

      - name: numwebpurchases
        type: number
        column: numwebpurchases
        description: "The number of purchases made by the customer through the web."
        public: false

      - name: numcatalogpurchases
        type: number
        column: numcatalogpurchases
        description: "The number of purchases made by the customer through catalogs."
        public: false

      - name: numstorepurchases
        type: number
        column: numstorepurchases
        description: "The number of purchases made by the customer in physical stores."
        public: false

      - name: numwebvisitsmont
        type: number
        column: numwebvisitsmont
        description: "The number of times the customer visited the website in the last month."
        public: false

      - name: purchases
        type: number
        column: purchases
        public: false

      - name: spend
        type: number
        column: spend
        public: false

      - name: country_name
        type: string
        sql: "{customer.country}"
        description: "The name of the country where the customer is located."

    measures:
      - name: recency
        sql: datediff(current_date,date(purchase_date))
        type: min 
        description: Number of days since the customers last purchase.

      - name: purchase_frequency
        sql: purchases
        type: sum 
        description: The number of purchases made by the customer in a specific period.

      - name: total_spend
        sql: spend
        type: sum 
        description: The total amount a customer has spent across all purchases.

      - name: average_spend
        sql: sum(spend)/nullif(sum(purchases),0)
        type: number 
        description: The average amount spent per transaction by the customer.   

      - name: churn_probability
        sql: "CASE WHEN {recency} < 30 AND {total_spend} > 500 THEN 0.9 WHEN {recency} BETWEEN 30 AND 90 AND {total_spend} BETWEEN 100 AND 500 THEN 0.5  WHEN {recency} > 90 OR {total_spend} < 100 THEN 0.2 ELSE 0.1  END"
        type: number
        description: "The predicted likelihood that a customer will churn, based on purchase behavior and recency."

      - name: cross_sell_opportunity_score
        sql: >
         sum((mntwines * 0.25 + mntmeatproducts * 0.2 + mntfishproducts * 0.15 + mntsweetproducts * 0.1 + mntgoldprods * 0.3 + mntfruits * 0.2))
          /sum(numwebpurchases + numcatalogpurchases + numstorepurchases + 1)
        description: "The potential for cross-selling a secondary product based on previous purchase patterns."
        type: number
```

</details>



### **Step 4: Define Manifest Files for Business Views**

The `views` folder contains business views, encapsulating the identified drivers and metrics to provide targeted insights.

#### **1. Meta section**

The Meta section provides essential metadata for the metric, which includes the title and tags. This section helps categorize the metric within specific domains, use cases, and tier.

#### **2. Metric Section**

The Metric section defines the actual measure being tracked and the rules for how it is calculated. This includes the expression, time window, and any exclusions.

#### **3. Tables Section**

The Tables section defines the data sources and the structure for the metric. It specifies the join paths, the relationships between different tables, and which columns should be included in the metric calculation.

🎯 **Your Actions:**

1. Create **business views** within the views folder using the given templates.
2. Add them to `views` folder.

<details>
<summary>Click to view YAML definition for the `Cross-Sell Opportunity Score` view</summary>

```yaml
views:
  - name: cross_sell_opportunity_score
    description: This metric calculate the potential for cross-selling a secondary product to customers based on past purchases. 
    public: true
    meta:
      title: Cross-Sell Opportunity Score
      tags:   
        - DPDomain.Marketing
        - DPUsecase.Customer Segmentation
        - DPUsecase.Product Recommendation
        - DPTier.Consumer Aligned
      metric:
        expression: "*/45  * * * *"
        timezone: "UTC"
        window: "day"
        excludes: 
          - mntwines
          - mntmeatproducts
          - mntfishproducts
          - mntsweetproducts
          - mntgoldprods
          - mntfruits
          - numwebpurchases
          - numcatalogpurchases
          - numstorepurchases
    tables:
      - join_path: purchase
        prefix: true
        includes:
          - cross_sell_opportunity_score
          - mntwines
          - mntmeatproducts
          - mntfishproducts
          - mntsweetproducts
          - mntgoldprods
          - mntfruits
          - numwebpurchases
          - numcatalogpurchases
          - numstorepurchases
          - customer_id
          - purchase_date

      - join_path: product
        prefix: true
        includes:
          - product_category
          - product_name
```
</details>

<details>
<summary>Click to view YAML definition for the `Purchase Frequency` view</summary>

```yaml
views:
  - name: purchase_frequency
    description: This metric calculates the average number of times a product is purchased by customers within a given time period
    public: true
    meta:
      title: Product Purchase Frequency
      tags:   
        - DPDomain.Marketing
        - DPUsecase.Customer Segmentation
        - DPUsecase.Product Recommendation
        - DPTier.Consumer Aligned
      metric:
        expression: "*/45  * * * *"
        timezone: "UTC"
        window: "day"
        excludes: 
         - purchases
    tables:
      - join_path: purchase
        prefix: true
        includes:
          - purchase_date
          - customer_id
          - purchase_frequency
          - purchases

      - join_path: product
        prefix: true
        includes:
          - product_category
          - product_name
```
</details>

<details>
<summary>Click to view YAML definition for the `Total Spend` view</summary>

```yaml
views:
  - name: total_spending
    description: This metric measures how many marketing campaigns a customer has engaged with. 
    public: true
    meta:
      title: Customer Spending by Product Category
      tags:   
        - DPDomain.Marketing
        - DPUsecase.Customer Segmentation
        - DPUsecase.Product Recommendation
        - DPTier.Consumer Aligned
      metric:
        expression: "*/45  * * * *"
        timezone: "UTC"
        window: "day"
        excludes: 
         - spend
    tables:
      - join_path: purchase
        prefix: true
        includes:
          - purchase_date
          - customer_id
          - total_spend
          - spend

      - join_path: product
        prefix: true
        includes:
          - product_category
          - product_name
```
</details>

### **Step 5: Define Access Control**

The `user_groups.yml` file manages access permissions for different user groups within your data model.

🎯 **Your Actions:**

1. Create a user_groups.yml file with the given template.
2. Define user groups and their API scopes.
3. Add users to each group.
4. Add a default group at the end.

```yaml
user_groups:
  - name: usa
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes: 
      - users:id:manishagrawal

  - name: india
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes: 
      - users:id:nandapage

  - name: default
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes: "*"
```

### **Step 6: Create a Lens Resource Manifest File**

This file is your blueprint for configuring your Lens Resource on DataOS. This file contains a meta section and a Lens Lens-specific section to define all the technical configurations, such as secrets, code base, repo, and source configuration that your Lens will be mapped to.

🎯 **Your Actions:**

1. Create a manifest file for your Lens Resource.
2. Provide metadata, source information, and secrets.
3. Specify URL and base directory.

```yaml
version: v1alpha
name: "productaffinity-xx"
layer: user
type: lens
tags:
  - lens
description: This semantic model provides comprehensive insights for product affinity analysis.
lens:
  compute: runnable-default
  secrets:
    - name: bitbucket-cred
      allKeys: true
  source:
    type: depot
    name: postgresxx
  repo:
    url: <url> # Ex: https://bitbucket.org/tmdc/product-affinity-training
    lensBaseDir: <basedir>  # Ex: product-affinity-training/build/semantic-model/model
    syncFlags:
      - --ref=main

  api:   # optional
    replicas: 1 # optional
    logLevel: info  # optional
    # envs:
    #   LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 500m
        memory: 500Mi
  worker: # optional
    replicas: 1 # optional
    logLevel: debug  # optional
    # envs:
    #   LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 500m
        memory: 500Mi
  router: # optional
    logLevel: info  # optional
    # envs:
    #   LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 500m
        memory: 500Mi

  metric:
    logLevel: info
```

### **Step 7: Push the code to Repo** 

Push the code to Repo and update the repo URL and base directory location under lens section.  Use clear commit messages to describe changes effectively.

<aside class="callout">
Don’t forget to replace placeholder values with your project-specific info and push changes to your repo with clear commit messages.
</aside>

## Next step

Your semantic model is now in place. The final milestone is to deploy your first consumer-aligned data product.

👉 [Deploy and Register Data Product](/learn_new/dp_foundations2_learn_track/deploy_sm/)

