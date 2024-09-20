# Creating Data Model (Lens)

!!! info "Information"
    This guide offers step-by-step instructions to help you create a Lens model in DataOS, transforming your conceptual design into a functional data model. By following this guide, you'll learn how to structure and organize your data effectively, ensuring it meets your analytical and business needs.

## Key Steps

Follow the below steps to create a data model (Lens).

<center>
<div style="text-align: center;">
<img src="/quick_guides/create_data_model/5_create_data_model.png" alt="Steps to create a lens model" style="border: 1px solid black;">
</div>
</center>

<!-- ![5_create_data_model.png](/quick_guides/create_data_model/5_create_data_model.png) -->

## Pre-requisites

-  A code editor for creating manifest files (YAML) of the Lens model. 

## Step 1: Set Up Lens Model Folder

**Download the Lens Project Template** which includes the necessary folder hierarchy. Rename it as needed.

**Download:** [lens-project-template.zip](/resources/lens/lens_setup/lens-project-template.zip)

<aside class="callout">
🗣 When you download the template, you'll find a `docker-compose.yml` file included. This file is only needed if you plan to test your Lens model locally before deploying it to production.

</aside>

### **Model Folder Structure:**

The model folder structure is essential for managing your SQL scripts and business entity manifest files for your Lens model.

<div style="text-align: left; padding-left: 1em;">
<img src="/quick_guides/create_data_model/lens_model_folders.png" alt="flens_model_folders.png" style="max-width: 40%; height: auto; border: 1px solid #000;">
</div>

## Step 2: Define SQL Scripts for Tables

The `sqls` folder contains SQL scripts that extract relevant fields from your data source to create your model. Below are examples for Customer, Product, and Transactions data.

```yaml
SELECT
    *
FROM
    schema.table_name
```

**Example SQL Files**

For our data model, we are fetching Customer, Product, and Transaction data from DataOS lakehouse storage.

Here are the SQL scripts for the tables, identified as business objects during the conceptual design of our data model. This will help extract relevant fields from the source for our data model based on our analytical requirement.

<details><summary>Customer.sql</summary>
    
```sql
SELECT
    cast(customer_id AS varchar) AS customer_id,
    first_name,
    last_name,
    gender,
    phone_number,
    email_id,
    cast( date_parse(birth_date,'%d-%m-%Y') as timestamp) as birth_date,
    age,
    education_level,
    marital_status,
    number_of_children,
    cast(register_date as timestamp) as register_date,
    occupation,
    annual_income,
    hobbies,
    degree_of_loyalty,
    social_class,
    mailing_street,
    city,
    state,
    country,
    zip_code
FROM
    "icebase"."sales_360".customer
```
</details>
    
<details><summary>product.sql </summary>
    
```sql
SELECT
    productid,
    skuid,
    productname,
    productcategory,
    subcategory,
    gender,
    cast(price as double) as price,
    cast(cost as double) as cost,
    cast(launchdate as timestamp) as launchdate,
    designername,
    color,
    size,
    model
FROM
    "icebase"."sales_360".products
```
</details>
    
<details><summary>transactions.sql</summary>
    
```sql
SELECT
    transaction_id,
    customer_id,
    cast(transaction_date AS timestamp) AS transaction_date,
    order_id,
    transaction_amount,
    payment_method,
    transaction_type,
    transaction_status,
    cast(order_date AS timestamp) AS order_date,
    cast(order_delivery_date AS timestamp) AS order_delivery_date,
    discounted_amount,
    shipping_amount,
    order_total_amount,
    discount_percentage,
    shipping_address,
    billing_address,
    promo_code,
    shipping_method,
    order_status,
    skuid
FROM
    "icebase"."sales_360".transactions
```
</details>  

## Step 3: Define Manifest Files for Tables

This `tables` folder contains logical table definitions in YAML format. These definitions help structure your data into business entities. Each table represents an entity in your data model.

Here's a template for creating a manifest file for your data tables:

```yaml
tables:
  - name: table_name
    # Path of the sql file, example - {{table_name.sql}}
    sql: {{ load_sql('sql_sample') }}
    description: Table description
    # Set this property to true/false to control visibilty of table. 
    public: true # table will be visible to everyone

    # To establish relationship with other table (this will always create left join)
    joins:
      - name: target_table
        relationship: one_to_one
        sql: TABLE.dimension_name = target_table.dimension_name

    dimensions:
        # Name should follow snake-case format
      - name: dimension_name
        title: dimension_title
        description: Dimension description
        # Mapping of dimension to the specific column defined in the sql of the table 
        sql: dimension_sql
        # Data type of the dimension (types - time, string, number and boolean)
        type: dimension_type
        # To make this dimension primary key set to true
        primary_key: false
        # To make this dimension accessible set to true
        public: true
        # To associate additional key value properties
        meta:
          key: value

    measures:
      - name: measure_name
        title: measure_title
        description: Measure description
        # Define custome SQL snippet or map dimension
        sql: measure_sql
        # Set type for this measure (types - string,time,boolean,number,count,count_distinct,count_distinct_approx,sum,avg,min,max)
        type: string
        # To apply additional filters
        filters:
          - sql: "{TABLE}.dimension_name = 'dimension_value' "
        meta:
          key: value

    # To create frequently used complex filters 
    # And can also be used to apply row filter policy on a group of users
    segments:
      - name: segment_name
        public: true
        # SQL statement for filter
        sql: "{TABLE}.dimension_name = 'dimension_value'"
        meta:
          # To apply a pre-defined filter by default to user groups
          secure:
            user_groups:
              - default
```

Here is a breakdown of the sections in the YAML template:

**1. `tables`**

Provide the following information for the business entity included in the data model.

| Attribute | Description |
| --- | --- |
| `name` | The name of the table. |
| `sql` | Path to the SQL file defining the table’s data. |
| `description` | A brief description of what the table represents. |
| `public` | Indicates whether the table is visible to everyone (`true`) or restricted (`false`). |

**2. `joins`**

Defines relationships with other tables(entities), which will create left joins.

| Attribute | Description |
| --- | --- |
| `name` | The name of the target table for the join. |
| `relationship` | Type of relationship (e.g., `one_to_one`, `many_to_one`). |
| `sql` | SQL condition for the join, specifying how the tables are related. |

**3. `dimensions`**

Lists dimensions for the entity, which are attributes or categories.

| Attribute | Description |
| --- | --- |
| `name` | The name of the dimension. |
| `title` | User-friendly title for the dimension. |
| `description` | Brief description of the dimension. |
| `sql` | SQL expression or column mapping for the dimension. |
| `type` | Data type of the dimension (e.g., `time`, `string`, `number`, `boolean`). |
| `primary_key` | Indicates if this dimension is a primary key. |
| `public` | Specifies visibility of the dimension(`true` or `false`). |
| `meta` | Additional metadata for the dimension, such as custom key-value properties. |

**4. `measures`**

Defines the measures (aggregated values) identified for the entity.

| Attribute | Description |
| --- | --- |
| `name` | The name of the measure. |
| `title` | User-friendly title for the measure. |
| `description` | Brief description of the measure. |
| `sql` | SQL expression or custom snippet for calculating the measure. |
| `type` | The type of measure (e.g., `string`, `time`, `boolean`, `number`, `count`, `sum`, `avg`). |
| `filters` | Optional filters to apply to the measure. |
| `meta` | Additional metadata for the measure. |

**5. `segments`**

Defines segments/complex filters that can be used during analysis.

| Attribute | Description |
| --- | --- |
| `name` | The name of the segment. |
| `public` | Specifies visibility of the segment. |
| `sql` | SQL condition for the segment filter. |
| `meta` | This field is used to define custom metadata. Under secure, you can specify, as sub-property, the list of user groups to which the segment is applicable.  |


```yaml
meta:
  secure:
    user_groups: 
      includes:
        - type_analyst
      excludes:
        - default
```

<aside class="callout">
🗣 Mentioning a user group when defining segments automatically applies the filter criteria to that group.
</aside>
**Example YAML Files** 

Here are the manifest files of the tables for the business entities for our data model.

<details><summary>Customer</summary>
    
```yaml
tables:

    - name: customer
    sql: {{ load_sql('customer') }}
    description: Table containing information about customer records.
    
    joins:
        - name: transactions
        relationship: one_to_many
        sql: "{TABLE.customer_id} = {transaction.customer_id}"

    dimensions:
        - name: customer_id
        type: string
        description: Unique identifier for each customer.
        sql: customer_id
        primary_key : true
        public : true        

        - name: first_name
        type: string
        description: First name of the customer.
        sql: first_name

        - name: last_name
        type: string
        description: Last name of the customer.
        sql: last_name

        - name: gender
        type: string
        description: Gender of the customer.
        sql: gender

        - name: phone_number
        type: string
        description: Phone number of the customer.
        sql: phone_number

        - name: email_id
        type: string
        description: Email address of the customer.
        sql: email_id

        - name: birth_date
        type: time
        description: Birth date of the customer.
        sql: birth_date

        - name: age
        type: number
        description: Age of the customer.
        sql: age

        - name: education_level
        type: string
        description: Education level of the customer.
        sql: education_level

        - name: marital_status
        type: string
        description: Marital status of the customer.
        sql: marital_status

        - name: number_of_children
        type: number
        description: Number of children the customer has.
        sql: number_of_children

        - name: register_date
        type: time
        description: Date when the customer registered.
        sql: register_date

        - name: occupation
        type: string
        description: Occupation of the customer.
        sql: occupation

        - name: annual_income
        type: string
        description: Annual income of the customer.
        sql: annual_income
        meta:
            secure:
            func: redact
            user_groups:
                includes: "*" # secure for everyone
                excludes:
                - type_analyst   # except default        

        - name: hobbies
        type: string
        description: Hobbies of the customer.
        sql: hobbies

        - name: degree_of_loyalty
        type: string
        description: Degree of loyalty of the customer.
        sql: degree_of_loyalty

        - name: social_class
        type: string
        description: Social class of the customer.
        sql: social_class

        - name: mailing_street
        type: string
        description: Mailing street address of the customer.
        sql: mailing_street

        - name: city
        type: string
        description: City where the customer lives.
        sql: city

        - name: state
        type: string
        description: State where the customer lives.
        sql: state

        - name: country
        type: string
        description: Country where the customer lives.
        sql: country

        - name: zip_code
        type: number
        description: Zip code of the customer's address.
        sql: zip_code

        - name: age_group
        type: string
        sql: CASE
                WHEN age < 18 THEN 'Under 18'
                WHEN age BETWEEN 18 AND 35 THEN '18-35'
                WHEN age BETWEEN 36 AND 50 THEN '36-50'
                ELSE 'Above 50'
                END
        description: "Age group of the customer"

        - name: full_name
        type: string
        sql: CONCAT(first_name, ' ', last_name)
        description: "Full name of the customer"                    

    measures:
        
        - name: total_customers
        sql: customer_id
        type: count_distinct
        description: Total number of customers

        - name: average_age
        sql: age
        type: avg
        description: Average age of the customers

    segments:
        # - name: minor_age_customer
        #   public: true      
        #   sql: "{TABLE}.age_group = 'Under 18'"
        #   meta:
        #     secure:
        #       user_groups: 
        #         includes:
        #           - default
        #         excludes:
        #           - type_analyst      

        - name: loyal_customers
        public: true
        sql: "{TABLE}.degree_of_loyalty = 'Hard Core Loyals' " 
        meta:
            secure:
            user_groups: 
                includes:
                - type_analyst
                excludes:
                - default
```
</details>
    
<details><summary>Products</summary>
    
```yaml
tables:
    - name: products
    sql: {{ load_sql('products') }}
    description: Table containing information about customer records.
    
    dimensions:
        
        - name: productid
        type: string
        description: Unique identifier for each product.
        sql: productid
        primary_key : true
        public : true         

        - name: skuid
        type: string
        description: Unique identifier for each SKU.
        sql: skuid

        - name: productname
        type: string
        description: Name of the product.
        sql: productname

        - name: productcategory
        type: string
        description: Category to which the product belongs.
        sql: productcategory

        - name: subcategory
        type: string
        description: Subcategory to which the product belongs.
        sql: subcategory

        - name: gender
        type: string
        description: Target gender for the product.
        sql: gender

        - name: price
        type: number
        description: Price of the product.
        sql: price

        - name: cost
        type: number
        description: Cost to produce the product.
        sql: cost

        - name: launchdate
        type: time
        description: Launch date of the product.
        sql:  launchdate

        - name: designername
        type: string
        description: Name of the designer of the product.
        sql: designername

        - name: color
        type: string
        description: Color of the product.
        sql: color

        - name: size
        type: string
        description: Size of the product.
        sql: size

        - name: model
        type: string
        description: Model of the product.
        sql: model
        

    measures:
        
        - name: total_products
        sql: productid
        type: count_distinct
        description: Total number of products

        - name: average_price
        sql: price
        type: avg
        description: Average price of the products

        - name: total_cost
        sql: cost
        type: sum
        description: Total cost of all products

        - name: average_margin
        sql: AVG(price - cost)
        type: number
        description: "Average profit margin per product"
    
```
</details>
    
<details><summary>Transactions</summary>
    
```yaml
tables:
    - name: transactions
    sql: {{ load_sql('transactions') }}
    description: Table containing information about customer records.
    joins:
        - name: products
        relationship: many_to_one
        sql: "{TABLE.skuid}= {products.skuid}"           

    dimensions:
        - name: transaction_id
        type: string
        description: Unique identifier for each transaction.
        sql: transaction_id
        primary_key : true
        public : true          
        
        - name: customer_id
        type: string
        description: Unique identifier for each customer.
        sql: customer_id
        
        - name: transaction_date
        type: time
        description: The date and time when the transaction occurred.
        sql: transaction_date 
        
        - name: order_id
        type: string
        description: Unique identifier for each order.
        sql: order_id
        
        - name: transaction_amount
        type: number
        description: The amount of money involved in the transaction.
        sql: transaction_amount
        
        - name: payment_method
        type: string
        description: The method of payment used for the transaction.
        sql: payment_method
        
        - name: transaction_type
        type: string
        description: The type of transaction (e.g., purchase, refund).
        sql: transaction_type
        
        - name: transaction_status
        type: string
        description: The status of the transaction (e.g., completed, pending).
        sql: transaction_status
                
        
        - name: order_delivery_date
        type: time
        description: The date & time when the order is expected to be delivered.
        sql: order_delivery_date 
        
        - name: discounted_amount
        type: number
        description: The amount of discount applied to the order.
        sql: discounted_amount
        
        - name: shipping_amount
        type: number
        description: The cost of shipping for the order.
        sql: shipping_amount
        
        - name: order_total_amount
        type: number
        description: The total amount for the order with discounts and shipping.
        sql: order_total_amount
        public : false          

        
        - name: discount_percentage
        type: number
        description: The percentage of discount applied to the order.
        sql: discount_percentage
        
        - name: shipping_address
        type: string
        description: The address where the order is to be shipped.
        sql: shipping_address
        
        - name: billing_address
        type: string
        description: The address where the bill is to be sent.
        sql: billing_address
        
        - name: promo_code
        type: string
        description: The promotional code applied to the order, if any.
        sql: promo_code
        
        - name: shipping_method
        type: string
        description: The method of shipping used for the order.
        sql: shipping_method
        
        - name: order_status
        type: string
        description: The status of the order (e.g., processing, shipped).
        sql: order_status
        
        - name: skuid
        type: string
        description: The stock-keeping unit identifier.
        sql: skuid

        - name: full_address
        type: string
        sql: CONCAT(shipping_address, ' ', billing_address)
        description: Concatenation of the shipping and billing address

        - name: transaction_year
        type: number
        sql: YEAR(transaction_date)
        description: Year of the transaction

        - name: transaction_month
        type: number
        sql: MONTH(transaction_date)
        description: Month of the transaction

        - name: transaction_day
        type: number
        sql: DAY(transaction_date)
        description: Day of the transaction

        - name: order_delivery_duration
        type: number
        sql: COALESCE(DATE_DIFF('day',transaction_date,order_delivery_date),0)
        description: Number of days between order date and delivery date

        - name: discount_applied
        type: string
        sql: case when discounted_amount > 0 then 'true'
                else 'false' 
                end
        description: Indicates if a discount was applied to the transaction

        - name: shipping_cost_category
        type: string
        sql: CASE 
                        WHEN shipping_amount = 0 THEN 'Free Shipping'
                        WHEN shipping_amount < 10 THEN 'Low Cost Shipping'
                        ELSE 'High Cost Shipping'
                        END
        description: Category of shipping cost based on the amount
        
        
    measures:
        - name: total_transactions
        sql: transaction_id
        type: count_distinct
        description: Total number of transactions

        - name: total_revenue
        sql: SUM(transaction_amount)
        type: number
        description: Total revenue from transactions

        - name: average_transaction_amount
        sql: AVG(transaction_amount)
        type: number
        description: Average amount per transaction

        - name: total_discounted_amount
        sql: SUM(discounted_amount)
        type: number
        description: Total discounted amount on transactions

        - name: total_shipping_amount
        sql: SUM(shipping_amount)
        type: number
        description: Total shipping amount for transactions

        - name: total_order_amount
        sql: SUM(order_total_amount)
        type: number
        description: Total amount for orders

        - name: transaction_percentage_with_discount
        sql: COUNT(CASE WHEN discounted_amount > 0 THEN 1 END) * 100.0 / (COUNT( transaction_id)) 
        type: number
        description: Percentage of transsaction with discounts   

        - name: ups_delivered_percentage
        sql: (COUNT(CASE WHEN shipping_method = 'UPS' AND order_status = 'Delivered' THEN 1 END) * 100.0 / COUNT( order_id)) 
        type: number
        description:  The percentage the orders shipped by UPS and the order status is delivered    

        - name: canceled_order_percentage
        sql: (COUNT(CASE WHEN order_status = 'Canceled' THEN 1 END) * 100.0 / COUNT( order_id))
        type: number
        description:  The percentage of the orders cancelled  

        - name: monthly_revenue_curr
        type: sum
        sql: transaction_amount
        rolling_window:
            trailing: 1 month
            offset: end
    
        - name: monthly_revenue_prev
        type: sum
        sql: transaction_amount
        rolling_window:
            trailing: 1 month
            offset: start         

    segments:
        - name: paypal_transactions
        public: true      
        sql: "{TABLE}.payment_method = 'PayPal'" 
```
</details>
    

## Step 4: Define Manifest Files for Business Views
The `views` folder contains Views, encapsulating the identified drivers and metrics to provide targeted insights. These views can be tailored to your specific analytical needs.

Here is the template for defining views in YAML files. You can create multiple views according to your data model design.

```yaml
views:
  - name: view_name
    description: "purpose of the view"
    public: true
    #use meta property to define whether you want to export a view to IRIS board
    meta:
      #set this property to true if you want to export the view to IRIS board
      export_to_board: true
      board:
        #provide the time dimension to be used for displaying time-series
        timeseries: table_name.dimension_name 
    tables:
        # table name to be included in the view
      - join_path: table1
        # Set to true to add the table name as prefix to measure/dimension
        prefix: true
        # To include all or specific measures and dimensions
        includes: "*" #'*' will include all measure and dimensions of the table
        # To exclude specific measures and dimensions
        excludes:
          - measure
          - dimension
```

The YAML configuration contains the various attributes and nested sections. 

1. **`views`** 
    
    This section contains configurations for creating a view in your data model. Each view has the following attributes:
    
    | Attribute | Description |
    | --- | --- |
    | `name` | The name of the view. |
    | `description` | A description of the view's purpose or content. |
    | `public` | Indicates whether the view is publicly accessible. |
    | `meta` | Metadata related to the view, such as export settings. |

2. **`meta`**
    
    Within the `meta` section of the view, you can define additional metadata, including export settings and time zone information:
    
    | Attribute | Description |
    | --- | --- |
    | `export_to_iris` | Boolean flag indicating if the view should be exported to Iris. |
    | `iris` | Configuration related to Iris export settings. |
    | `timeseries` | Field used for time series data in Iris. |
    | `available_time_zones` | List of time zones available for time series data. |

3. **`tables`** 
    
    The `tables` section within a view specifies which tables are included in the view and how they should be joined:
    
    | Attribute | Description |
    | --- | --- |
    | `join_path` | The name of the table to include in the view. |
    | `prefix` | Boolean flag indicating if a prefix should be applied to the table’s columns. |
    | `includes` | List of columns to include from the table. |
    
**Example YAML Files**
    
Here are the manifest files for the business views identified for our data model as per the business requirement.
    
<details><summary>Product Analysis</summary>
        
```yaml
views:
    - name: product_analysis
    description: View containing transactions 360 degree information
    public: true
    meta:
        export_to_iris: true
        iris:
        timeseries: products.launchdate
        available_time_zones:
            - America/Los_Angeles
            - America/Chicago
            - America/New_York
            - Europe/London
            - Europe/Paris
            - Asia/Jerusalem
            - Europe/Moscow
            - Asia/Kolkata
            - Asia/Shanghai
            - Asia/Tokyo
            - Australia/Sydney

    tables:

        - join_path: products
        prefix: true
        includes:
            - productname
            - productcategory
            - designername
            - productid
            - launchdate
            - total_products
            - price          
            - cost
            - average_margin
            - average_price          
            - subcategory
```
</details>
        
<details><summary>Transactions Analysis </summary>
        
```yaml
views:
    - name: transaction_analysis
    description: View containing transactions 360 degree information
    public: true
    meta:
        export_to_iris: true
        iris:
        timeseries: transactions.transaction_date
        available_time_zones:
            - America/Los_Angeles
            - America/Chicago
            - America/New_York
            - Europe/London
            - Europe/Paris
            - Asia/Jerusalem
            - Europe/Moscow
            - Asia/Kolkata
            - Asia/Shanghai
            - Asia/Tokyo
            - Australia/Sydney

    tables:
        - join_path: transactions
        prefix: true
        includes:
            - total_transactions
            - transaction_id
            - total_revenue
            - transaction_amount
            - average_transaction_amount
            - transaction_date
            - order_id
            - payment_method
            - transaction_type
            - skuid
            - discount_applied
            - discounted_amount
            - customer_id

        - join_path: products
        prefix: true
        includes:
            - productname
            - productcategory
            - designername
            - productid
```
</details>
        

## Step 5: Define Access Permissions for Data Model

The `user_groups.yml` file manages access permissions for different user groups within your data model.

```yaml
user_groups:
  - name: default
    description: this is a default user group
    includes: "*"

```

Following is the user_groups manifest file for our data model.

```yaml
user_groups:
  - name: default
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes: "*"
  - name: type_analyst
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes:
      - users:id:aayushisolanki
      - users:id:piyushjoshi
      - users:id:nandapage
```

This is how folder structure looks like for our data model.

<div style="text-align: left; padding-left: 1em;">
<img src="/quick_guides/create_data_model/folder_structure_data_model.png" alt="folder_structure_data_model.png" style="max-width: 35%; height: auto; border: 1px solid #000;">
</div>

## Next Steps

[Test Your Data Model](/quick_guides/test_data_model/)

[Deploy Your Data Model](/quick_guides/deploy_data_model/)