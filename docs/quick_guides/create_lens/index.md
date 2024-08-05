# Creating a Lens

!!! info "Information"
    This guide will walk you through the steps of setting up and utilizing a data analysis lens tailored for a sports retail scenario. By following this guide, you'll be able to explore sales, customer, and product data to gain valuable insights for optimizing business strategies and enhancing customer satisfaction.

In this short guide, you'll learn the following:

1. **Define Lens:** Define a lens tailored for sports retail data analysis, specifying metadata, entities, fields, dimensions, measures, relationships, and dynamic parameters.
2. **Deploy Lens:** Deploy the defined lens into the DataOS environment to make it accessible for analysis.
3. **Run Queries:** Utilize the deployed lens to run queries, analyze data, and extract valuable insights to optimize business strategies and enhance customer satisfaction.

By following these steps, you'll be able to effectively analyze your sports retail data and make informed decisions based on actionable insights. 

Let's get started!!!

## Defining Lens

In this step, we'll focus on creating a comprehensive Lens definition specifically designed for analyzing data from a sports retail store. We'll work on the following key aspects:

### **Step 1: Conceptual Data Model**

Identify entities, fields, dimensions, and measures relevant to our analysis and develop a conceptual data model. You also need to define the objectives of the data analysis and outline the key questions we aim to answer. 

**Analytical Objectives** 

The Sports Retail Store specializes in sports apparel, equipment, and gear. The store aims to gain deeper insights into its sales and customer data to optimize product offerings and marketing strategies. Key data questions include:

- Understanding customers: Average annual income, homeownership status
- Sales analysis: Total revenue, average order value, purchase frequency, profit analysis, and more.
- Issues with product quality and services: customer dissatisfaction, purchase returns

**Questions to seek answers for:**

- What is the total revenue generated from sales, categorized by country?
- What is the average order value for all transactions?
- What is the average frequency of purchases made by customers?
- What is the revenue generated for a specific month?
- What is the profit generated from each individual product?
- Which order is the most frequently placed?
- Who is the customer with the longest lifespan in terms of months?
- How do sales vary across different product categories on a yearly basis?
- How does the revenue compare between two specific months for each product sub-category?
- How many items were returned, categorized by country?

> By addressing these data questions, data-driven decisions can be made to enhance customer satisfaction, optimize product offerings, and improve overall business performance.
> 

**Let's explore the fundamental elements of Lens that enable us to create a conceptual view.**

**Entities**

Entities represent real-world objects or activities within your organization. In the case of Sports retail store, entities can be **Customers, Orders, Territories, Purchase returns.**

**Fields**

Fields uniquely identify attributes within entities. They map directly to columns in data tables and can include unique identifiers. For example, the unique `customerID` field uniquely identifies each customer entity.

**Dimensions**

Dimensions contain qualitative data that can be used to group and filter information. They provide insights into various aspects of business operations. For example, in a `Sales` dataset, dimensions could include `order_date`, `product_category`, or geographic location such as `city`. Dimensions allow for slicing and dicing data to gain different perspectives or aggregations.

**Relationships**

Relationships establish connections between entities, enabling seamless data querying and analysis across multiple datasets. In a business context, these connections define how entities interact with each other. For instance, the relationship between Customer and Sales typically represents a `one-to-many` relationship. Here, one customer can initiate multiple sales transactions, providing valuable insights into customer behavior and purchase patterns.

**Measures**

Measures constitute essential aggregated numerical values extracted from quantitative data, serving as vital metrics to gauge various aspects of business performance and customer satisfaction. Within the realm of retail, measures play a pivotal role in quantifying key performance indicators such as `total sales revenue` and `average order value`. Retailers leverage measures to delve into intricate details, such as the frequency of orders and the lifespan of customer engagement, enabling them to discern loyal customer segments and tailor strategies accordingly. 

Understanding and leveraging these measures empower analysts to uncover deeper insights into customer behavior, purchase patterns, and the overall dynamics driving business performance.

### **Step 2: Defining Data Elements for the Lens**

Based on the objective of the analysis, let us identify Entities, Dimensions, Measures, and Relationships for our use case.

1. Identify Entities, such as Customers, Sales, etc. To analyze customer dissatisfaction and product quality issues, we require records of purchased item returns. Similarly for country,
2. List Attributes for Each Entity.
3. Identify fields that uniquely represent each record. These unique identifiers help ensure that each record is distinct and can be easily referenced or linked to other related records.
    1. **Customer Entity:**
        - **`Customer_key`**: A unique identifier assigned to each customer.
        - Other potential unique fields: **`email_address`**, **`phone_number`**, or a combination of **`first_name`** and **`last_name`**.
    2. **Order Entity:**
        - **`order_number`**: A unique identifier for each order placed by a customer.
    3. **Product Entity:**
        - **`product_key`**: A unique identifier for each product.
    4. **Territory Entity:**
        - **`sales_territory_key`**:A unique identifier for each territory.
4. Identify relationships between entities.
5. Identify the measures are required for the analysis and their calculation logic.
6. Also consider derived dimensions. In some cases, you may need dimensions that don't directly exist in your dataset but can be derived from existing data using SQL expressions. For instance, you might calculate a "profit margin" dimension based on the "revenue" and "cost" columns. Define them under dimensions. Similarly, you can have a derived dimension, `full_name`, combining `first_name` and `last_name`.

- Here is the table:

    | Entity    | Fields and Dimensions                                                                                              | Measure                                                                                                                                           | Related To       | Relationship | Derived Dimensions                                                                                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Customer  | first_name, last_name, birth_date, gender, email_address, annual_income, total_children, education_level, occupation, home_owner, dob                     | total_customer, average_annual_income, count_home_owner                                                                                          |                  |              | full_name, customer_lifespan_in_year, customer_lifespan_in_month, average_order_value, average_purchase_frequency_rate, customer_lifetime_value, home_owner_bool_value  |
| Sales     | order_number, customer_key, order_date, inline_item_number, product_key, territory_key, order_quantities, order_line_item, category_name                  | total_revenue, number_of orders, number_of_customer, first_order, last_order, lifespan_in_year, lifespan_in_month, avg_order_value, avg_purchase_freq_rate, month1_revenue, month2_revenue, product_category_share_orders, date_wise_orders | Customer, Territory | N:1, N:1     |                                                                                                                                                                         |
| Product   | product_key, product_subcategory_key, product_name, product_description, product_sku, product_color, product_size, product_style, product_cost, product_price | profit                                                                                                                                            | Sales            | 1:N          |                                                                                                                                                                         |
| Returns   | return_date, product_key, territory_id, return_quantity                                                           |                                                                                                                                                   | Product, Territory | N:1, N:1     |                                                                                                                                                                         |
| Territory | sales_territory_key, region, country                                                                              |                                                                                                                                                   |                  |              |                                                                                                                                                                         |


### **Step 3: Creating Lens YAML**

Define a lens specifying metadata, entities, fields, dimensions, measures, relationships, and dynamic parameters.

To create a Lens, you need to configure the attributes of various sections within a Lens YAML. The sections are provided below:

- **Lens Meta section**
    
    
    | Attributes | Description |
    | --- | --- |
    | name | Name of the Lens |
    | description | Description for the Lens |
    | owner | Owner of the Lens |
    | tags | tags for discoverability |

- **Entities section**
    
    
    | Attribute | Description |
    | --- | --- |
    | name | Name of the entity |
    | description | description of an entity |
    | SQL | A query that runs against your data source to extract the entity table |
    | fields | Unique identifiers for an entity |
    | dimensions | Categorical or time-based data that helps in adding context to the measures |
    | measures | Aggregated columns are calculated using SQL expressions. Measures are the foundation for defining metrics. |
    | relationships | Defines the relationship of entities with other entities. An entity can be joined to other entities and have one-to-one, one-to-many, or many-to-one relationships. |

The Lens YAML skeleton is given below, which summarizes the properties of every Section. 

![lens-yaml-skeleton.png](/quick_guides/create_lens/lens_yaml_skeleton.png)


## Deploying Lens

With the YAML for the Lens being created, the next step is to deploy it into the DataOS environment to make it accessible for analysis. 

There are two ways to deploy the Lens.

### Using Postman

Postman will be used as the deployment tool. To get started, follow the steps:

**Step 1: Get the Environment Token or API Key**

- Get the environment token or API Key from the profile section of the current environment. To get the API Key from DataOS, click [here](/interfaces/#create-tokens).

**Step 2: Install Postman**

- Download and install Postman from the following [link](https://www.postman.com/downloads/): If you already have it installed, proceed to the next step.

**Step 3: Launching Postman**

- Launch the Postman application and create a workspace. Then, go to the **API**’s tab and establish a new one for HTTP Request.
    
    ![Screenshot 2024-04-05 at 2.04.50 PM.png](/quick_guides/create_lens/launch_postman.png)
    

**Step 4: Create a lens or update an existing Lens**.

1. In the ‘**Headers**’ section, add the following headers. Paste your API token here.
    
    ![image](/quick_guides/create_lens/headers.png)
    
2. Write Lens in the ‘**Body**’ Section. Choose ‘**raw**’ as the text format.
    
    ![postman_body.png](/quick_guides/create_lens/postman_body.png)
    
3. In the ‘**Param**’ section, select dryrun=false.
4. To upsert the Lens:
    - Select **PUT.**
    - Add the following URL - `https://{{dataos-instance}}/lens/api/v1/lenses?dryrun=false` and click on the ‘**Send**’ button.
        
        Example: *https://enough-kingfish.dataos.app/lens/api/v1/lenses?dryrun=false*
        
        ![postman_body.png](/quick_guides/create_lens/upsert_lens.png)
        
5. Finally, "**Send**" button is clicked to initiate the deployment.

### Using Python Script

Follow the steps given below to deploy Lens.

1. Make sure that python is installed on your system.
2. Create a Python script named  `python_lens.py`. Within this script, specify placeholders for  `{{api_token}}` , `{{dataos-instance}}` and `{{Lens yaml file path}}`.
    
    ```python
    import requests
    import json
    import yaml
    
    api_token = "{{api_token}}"
    
    url = "https://{{dataos-instance}}/lens/api/v1/lenses?dryrun=false"
    
    headers = {
        "Authorization": f"Bearer {{api_token}}",
        "Content-Type": "application/json"
    }
    
    # Load the YAML file
    with open('{{YAML FILE PATH}}', 'r') as file:
        body_yaml = file.read()
    
    # Parse the YAML into a dictionary
    body = yaml.safe_load(body_yaml)
    
    try:
        response = requests.put(url, headers=headers, data=json.dumps(body))
        
        if response.status_code == 200:
            print("PUT request successful!")
            print("Response content:", response.text)
        else:
            print(f"PUT request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    ```
    
3. Execute the file, and your Lens will be successfully deployed.

## **Accessing Lens**

Lens is created in DataOS environment, you can use it to gain insights from your data, run queries, generate visualizations, and perform various analyses. Access the deployed lens and explore data using the Lens Explorer UI and LQL.

After successfully deploying the Lens, you can initiate your exploration and querying process within the DataOS environment. You have two primary options for this:

1. **Lens Explorer**: Lens Explorer provides a user-friendly, low-code interface for exploring modeled ontologies. For more details, refer to the following link.
    
    [Quick Start Guide: Using Lens](/quick_guides/use_lens/) 
    
2. **Lens Query (Abstracted SQL)**: Alternatively, you can utilize Lens Query, an abstracted SQL query language, via the WorkBench tool for more advanced querying and exploration.