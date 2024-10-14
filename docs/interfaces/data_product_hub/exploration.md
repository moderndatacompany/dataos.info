# Explore a Data Product

## **Data Product Exploration Button**

<<<<<<< HEAD
The **Exploration** button allows users to explore the data model ([Lens](/resources/lens/)) associated with the selected **Data Product**. By clicking this button, users can interact with the data model's pre-defined dimensions, measures, and segments, enabling them to visualize, filter, and analyze the data directly within the Lens. This provides an intuitive interface for business users and data analysts to explore the underlying data model without writing queries, offering insights through an easy-to-use exploratory environment.
=======
The **Exploration** button allows users to explore the **Lens model** associated with the selected **Data Product**. By clicking this button, users can interact with the data model's pre-defined dimensions, measures, and segments, enabling them to visualize, filter, and analyze the data directly within the Lens. This provides an intuitive interface for business users and data analysts to explore the underlying data model without writing queries, offering insights through an easy-to-use exploratory environment.
>>>>>>> 83f1c68a2524e022232f273f92e8edb848d70816

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(25).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i> Explore button </i></figcaption>
</center>
    
When you click on the **Explore** button, the **Explore Page** opens. The **Studio** tab is displayed by default, other tabs include Model and GraphQL. 

<center>
<img src="/interfaces/data_product_hub/exploration/annotely_image%20(2)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Data Product Hub Interface</i></figcaption>
</center>

## **1. Header and Page Context Information**

At the top of the page, you’ll always see the title of the Data Product you are exploring. For example, "Sales-360-data-product-v12," helps identify the specific version of the product.

<<<<<<< HEAD
- **Data Product Title**: At the top of the page, you’ll always see the title of the Data Product you are exploring. For example, "**Sales-360-data-product-v12**," helps identify the specific version of the product. On top of the title is the business unit or function for which Data Product was created, giving context on its origin. For instance, here, the business unit is Sales.
=======
- **Data Product Title**: At the top of the page, you’ll always see the title of the Data Product you are exploring. For example, "**Sales-360-data-product-v12**," helps identify the specific version of the product. On top of the title is the business unit or function for which data product was created, giving context on its origin. For instance, here, the business unit is Sales.
>>>>>>> 83f1c68a2524e022232f273f92e8edb848d70816
- **Description**: Below the title, a description gives an overview of the Data Product's purpose. In this case, it’s described as a "customer 360 view of the world."
- **Tier | Use-case |Team Information**: The header contains essential information, including the Data Product's tier (e.g., Aggregated, Source aligned, etc.), its primary use case (e.g., Demand Forecast, Performance monitoring, etc.), and the list of contributors or collaborators involved in creating and maintaining the product (e.g., Aakansha Jain, Darpan Vyas, etc.). This provides users with a clear understanding of the product's purpose and the key stakeholders behind it, ensuring transparency and context.

## **2. Star Button and BI Sync**

Star buttons let you favoritise the Data Product. In contrast, BI Sync opens the BI Sync functionality, which enables you to sync the Data Product to PowerBI, Tableau Cloud, Tableau Desktop, and Apache Superset.

## **3. Source Details**

When you click on the **Source** section, it displays details of the source on which the Lens model is built, and you can also check the source health. As you click on it, the following information is displayed.

- **Type**: Indicates the type of cluster source is linked to. In this case, the type is **Minerva.** It can either be **Themis or Flash.**
- **Dialect**: The query language or SQL dialect used for interacting with the data. For this product, the dialect is **Trino.**
<<<<<<< HEAD
- **Connection**: The connection string or URL links the Data Product to its source. This example defines the connection as **minerva://miniature**, indicating the internal connection point to the miniature cluster.
=======
- **Connection**: The connection string or URL links the data product to its source. This example defines the connection as **minerva://miniature**, indicating the internal connection point to the miniature cluster.
>>>>>>> 83f1c68a2524e022232f273f92e8edb848d70816
- **Database**: The database name is not explicitly shown in the given details, but this field would typically indicate the database within the system where the Data Product is stored.
- **Host**: Provides the host or context details where the data source is hosted. In this example, **tcp.liberal-donkey.dataos.app** is the context where the Data Product exists.
- **Watch:** To watch the health of the Cluster, Click on the watch button.

<center>
<img src="/interfaces/data_product_hub/exploration/annotely_image%20(1)%20(1).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Source health</i></figcaption>
</center>


As soon as you click on the **Watch** button, you can return to the source by clicking on the cross button to see the status of source health. Now, hover over the Cluster name **Minerva** here to see the health status. The green dot signals good health and that your query will run smoothly. In contrast, red signals that Cluster is not available.

<center>
<img src="/interfaces/data_product_hub/exploration/Screenshot%20from%202024-09-27 18-01-51.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Red signal: Cluster is not ready for queries</i></figcaption>
</center>


<center>
<img src="/interfaces/data_product_hub/exploration/Screenshot%20from%202024-09-27 18-00-34.png" alt="DPH" style="width:25rem; border: 1px solid black;" />
<figcaption><i>Green signal: Cluster is ready for queries</i></figcaption>
</center>


## **4. Navigation Tabs**

Further, It contains three tabs for exploring the Data Product in detail. 

- **Model Tab**
- **Studio Tab**
- **GraphQL Tab**

*Let’s first understand the default studio tab*

### Studio Tab

 When you first open the Explore page, the **Studio** tab is displayed by default. This tab provides an interactive workspace to design queries, view tables, pivot tables, charts, and more. It is the primary tool for exploring and visualizing data without technical coding.

This page is divided into **five primary sections**, each serving a specific purpose in the exploration and querying of Data Products:

- [Left Panel](https://www.notion.so/Data-Product-Exploration-831e609058fd46c4aa21d1ee59ef55aa?pvs=21)
- [Drop down Menu](https://www.notion.so/Data-Product-Exploration-831e609058fd46c4aa21d1ee59ef55aa?pvs=21)
- [Members and filters](https://www.notion.so/Data-Product-Exploration-831e609058fd46c4aa21d1ee59ef55aa?pvs=21)
- [Result Pane](https://www.notion.so/Data-Product-Exploration-831e609058fd46c4aa21d1ee59ef55aa?pvs=21)

## 5. Left Panel

Here are the key components in the sidebar navigation

- [Expand/Collapse All](https://www.notion.so/Data-Product-Exploration-831e609058fd46c4aa21d1ee59ef55aa?pvs=21)
- [History](https://www.notion.so/Data-Product-Exploration-831e609058fd46c4aa21d1ee59ef55aa?pvs=21)
- [Perspective](https://www.notion.so/Data-Product-Exploration-831e609058fd46c4aa21d1ee59ef55aa?pvs=21)

### **Expand/Collapse All**

An option to show or hide all the logical table Panel.

[The screen will expand as you click on Expand to show the logical table side panel.](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/53ba3ef2-ed6b-4932-a081-76f89f0c2684/expand_collapse.webm)

The screen will expand as you click on Expand to show the logical table side panel.

### **History**

The **History** section tracks the queries executed on a timestamp's data model. This allows users to revisit previous queries and review their selected dimensions, measures, filters, and results. It's beneficial for auditing, troubleshooting, or repeating previous analyses. 

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(26).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>History</i></figcaption>
</center>


For instance, a query might have been executed 32 minutes ago, using the **city dimension** and **total accounts measure** to analyze the total accounts across various cities. 

### **Perspectives**

In the **Data Product Exploration** interface, a user's query can be saved as a **Perspective**. A Perspective captures the current state of the query, including all selected dimensions, measures, metrics, filters, and any applied settings (e.g., time zones or limits). Once saved, Perspectives can be accessed at any time from the **Perspective** tab, allowing users to revisit or share their specific analyses without recreating the queries. By saving a Perspective, users can efficiently store and retrieve their specific analyses for continuous use or collaboration with team members.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(27).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Perspectives</i></figcaption>
</center>


Perspectives listed in the sales360 Data Product

### **How to Save and Use Perspectives?**

**Running a Query:** After selecting dimensions, measures, and running a query, you can save it to avoid re-configuring it later. For example, To find the total count of accounts in each city, select the **city dimension** and measure the **accounts count** from the **accounts** table. Click **Run Query Button.**

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(28).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Run query</i></figcaption>
</center>


**Saving a Perspective**: Once the query is complete, click the **Save Perspective** button (typically near the "Run Query" button).

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(29).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Save Persepectives</i></figcaption>
</center>


**Accessing Saved Perspectives**: After saving, the query will be available under the **Perspective** tab for the particular Data Product (e.g., **Sales 360**).

Users can click the **Perspective** tab and view all saved Perspectives, allowing them to reload the exact configuration of any previously saved query.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(30).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Accessing and reusing saved Persepective</i></figcaption>
</center>


**Re-running a Perspective**: To re-run a saved Perspective, select it from the list. This reloads the query and all settings and filters, making it easy to regenerate the results or apply new changes.

## **6. Drop-down Menu: logical table, Entities, Metrics**

The drop-down menu under **logical table** allows users to switch between logical table, Entities, or Metrics.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(31).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Drop down menu</i></figcaption>
</center>



### **logical table**

This is the default view in the sidebar. It shows a list of logical tables, which are structured datasets containing dimensions and measures. Logical tables are often used for performing queries, such as analyzing account data, product information, or sales figures.

**For** **example**, the above image contains three logical tables: account, product, and sales.

<center>
<img src="/interfaces/data_product_hub/exploration/Screenshot%20from%202024-09-23%2014-51-05.png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>logical table and Search bar</i></figcaption>
</center>

As you expand a particular table, you will see the list of all its dimensions and measures. In this case, the table named `account` is visible with various components such as **Measures** (e.g., `total_accounts`, `avg_rev_subquery`) and **Dimensions** (e.g., `city`, `address`).

**Search Bar**: Just below the logical table title, the search bar allows users to filter and quickly find specific tables, dimensions, or measures by typing keywords.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(32).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
</center>


*Besides, Logical tables the model also contains views. In the **Lens model**, users can create two types of **views**, each serving a different purpose and approach in how data is accessed and presented. Here's a differentiation between the two types of views:*

### **Entities**

**Entities** serve as a layer atop the data graph of tables, presenting an abstraction of the entire data model for consumers to interact with. They serve as a layer for defining metrics, providing a simplified interface for end-users to interact with key metrics instead of the entire data model. In an entity-first approach, views are built around entities in your data model. Views are built as denormalized tables, bringing measures and dimensions from multiple logical tables. They don’t have measures, dimensions, or segments of their own.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(33).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Entities</i></figcaption>
</center>


### **Metrics**

**Metrics** are presented as a **drop-down list option** allowing users to select from predefined key performance indicators (KPIs). These Metrics provide quantifiable measures crucial for assessing the performance of specific data points within the Data Product. For example, selecting the metric **aggregated_qtr_revenue_metric.sales_sales_aggregate_qtr_revenue_2024** would allow users to analyze quarterly revenue for different product brands.

### **How to Use Metrics in the UI**:

- **Step 1**: Click on the **Metrics** from the drop-down list in the left sidebar
- **Step 2**: Select the relevant metric based on your analysis needs. For example, if you are interested in tracking sales, you might select **aggregated_qtr_revenue_metric.sales_sales_aggregate_qtr_revenue_2024**.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(34).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Metircs</i></figcaption>
</center>


- **Step 3**: The selected metric will be added to your query. When combined with dimensions (like **sales source** or **product brand**), it will give you a complete performance view.
- **Step 4**: Run the query to get the results and review how the selected metric performs over time, across categories, or compared to benchmarks.
    
    In this case, the metric **aggregated_qtr_revenue_metric.sales_sales_aggregate_qtr_revenue_2024** is used along with two dimensions:
    
    1. **Sales Source**: Indicates whether the sales are from proof (alcoholic) or nonproof (non-alcoholic) products.
    2. **Product Brand**: Identifies the brand of the product sold.
    
    After running the query using this metric and dimensions, the result shows the revenue generated by each brand based on the sales source (proof/nonproof). 
    

## 7. Members and Filters

the **Members Tab** dynamically displays the dimensions and measures selected by the user from the list of available entities (such as "sales" or "account"). This tab allows users to track and manage the dimensions and measures used in a query.  One can unselect selected members using the **minus (-)** icon.  It also allows users to modify these selections with **visibility** and **filter** controls. The **Clear** button at the top of the **Members Tab** removes all selected dimensions and measures, resetting the query.

**Example**:

Suppose you select the dimension **`account, city`,** and measure **`account. Total_accounts`** will immediately appear in the **Members tab**, indicating that they are active in the query. Similarly, clicking on (-) sign will remove the selected member from the selection.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(35).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
</center>


- **Visibility Control**: An "eye" icon next to each member allows you to toggle the visibility of the selected dimension or measure in the query results.
    
    **Example**: If you hide the visibility of **`total_accounts`** using the "eye" icon, you will only see the **city names** in the query result, and the **total accounts** count will not be shown. This feature is useful when you want to focus on specific data points without deleting the measure entirely from the query.
    
    <center>
    <img src="/interfaces/data_product_hub/exploration/Screenshot%20from%202024-09-24%2012-04-00.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

    

- **Filtering Option**: A "filter" icon allows users to apply filters to the selected dimension or measure directly from the **Members Tab**.
    
    **Example**: If you click the filter icon on the **city** dimension and apply a filter that says **"city is not equal to Sacramento"**, the query result will show data for all cities **except Sacramento**. Once the filter is applied, click **Run Query** to see the filtered results.
    
    <center>
    <img src="/interfaces/data_product_hub/exploration/image%20(36).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>


## 8. Saving Queries

Query data and save them with a suitable name so they can be viewed later.

## **9. Result Display and Visualization Panel**

The **Result Display and Visualization Panel** is where users can choose how to view the outcomes of their queries. Once dimensions and measures are selected in the **Members Tab** and the query is executed, this panel offers multiple options for displaying the results. The panel provides flexible visual formats, allowing users to explore data in ways that best suit their analysis needs. Additionally, controls for **Timezone**, **Limit**, and **Offset** enable users to further customize how the data is presented, ensuring a comprehensive and user-friendly data exploration experience.

The following are the options for displaying the results:

- [Table](/interfaces/data_product_hub/exploration#table)
- [Chart](/interfaces/data_product_hub/exploration#chart)
- [Pivot](/interfaces/data_product_hub/exploration#pivot)
- [Integration](/interfaces/data_product_hub/exploration#integration)

### **Table**

 This option displays the query results in a tabular format. It’s ideal for users who prefer to see data in rows and columns for easy comparison and detailed analysis.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(37).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Table View</i></figcaption>
</center>


### **Chart**

This option allows users to visualize the query results in a graphical format. Various charts (e.g., bar, line, pie) can be used to display trends, comparisons, and distributions visually.


<center>
<img src="/interfaces/data_product_hub/exploration/Screenshot%20from%202024-09-24%2012-49-14.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Chart View</i></figcaption>
</center>

    

### **Pivot**

This option allows for interactive analysis. Users can group, summarize, and manipulate the data to create custom views and insights. Pivot tables are useful for dynamic data exploration.

<center>
<img src="/interfaces/data_product_hub/exploration/Screenshot%20from%202024-09-24 13-03-45.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Pivot View</i></figcaption>
</center>


### **Integration**

The **Integration** tab enables users to integrate the query results with other tools or services. This is particularly useful for exporting or connecting the data to external platforms for further processing or visualization. This gives data app developers the functionality to fetch real-time data and display it visually in the dashboard or create an application on top of it.


You can integrate the data model via:

- CURL
- GraphQL
- Postgres
- Source SQL

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(38).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>


For instance, You want to retrieve the total number of accounts grouped by city using an API, verify the output using a curl command, and then automate the process using Python. Here’s a practical example that demonstrates how to utilize the given curl command step-by-step, along with integrating it into a Python application workflow.

Steps to Follow:

**Step 1: Select Desired Measures and Dimensions** First, select the `total_account` measure and the `city` dimension from the side pane. As you select, the curl command for the particular query gets generated.  Here's the generated command:

```bash
curl --location 'https://lucky-eagle.dataos.app/lens2/api/public:purchasebehavior360/v2/load' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <api key here>' \
--data '{ "query": {
  "measures": [
    "account.total_accounts"
  ],
  "dimensions": [
    "account.city"
  ],
  "segments": [],
  "filters": [],
  "timeDimensions": [],
  "limit": 10,
  "offset": 0
} }'
```

**Step 2: Execute the Command in Your Terminal**

- Copy the entire command and replace YOUR_API_KEY with your actual API key.

- Open your terminal (Command Prompt on Windows or Terminal on macOS/Linux/Windows) and paste the modified command into your terminal and press Enter.

- The provided curl command retrieves data about the total accounts per city in json format. Here is your response will look like:

```json
{"query":{"measures":["account.total_accounts"],"dimensions":["account.city"],"segments":[],"filters":[],"timeDimensions":[],"limit":15,"offset":0,"timezone":"UTC","meta":{"secured":{"segments":[],"dimensions":[]}},"rowLimit":15},"data":[{"account.city":"Los Angeles","account.total_accounts":59},{"account.city":"Chicago","account.total_accounts":12},{"account.city":"Kansas City","account.total_accounts":11},{"account.city":"San Francisco","account.total_accounts":8},{"account.city":"New York","account.total_accounts":6},{"account.city":"Greenville","account.total_accounts":5},{"account.city":"Miami","account.total_accounts":5},{"account.city":"Philadelphia","account.total_accounts":5},{"account.city":"Houston","account.total_accounts":5},{"account.city":"Sacramento","account.total_accounts":4},{"account.city":"Omaha","account.total_accounts":4},{"account.city":"Cincinnati","account.total_accounts":3},{"account.city":"Jacksonville","account.total_accounts":2},{"account.city":"San Jose","account.total_accounts":2},{"account.city":"Spokane","account.total_accounts":2}],"lastRefreshTime":"2024-10-09T07:32:55.554Z","refreshKeyValues":[[{"refresh_key":"14403825"}]] 
```

- Check to ensure the output is correct and contains the expected data.

**Step 3: Integrate the Command into Your Application's Workflow** Once you've confirmed the output is correct, you can automate the data retrieval using a Python script with the requests library.

???tip "Python Script"

    ```python
    import requests
    import json
    import pandas as pd

    # API URL and headers
    url = 'https://lucky-possum.dataos.app/lens2/api/public:purchasebehavior360/v2/load'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer dG9rZW5fYWN0dWFsbHlfYWR2ZXJzZWx5X2luc3BpcmVkX3JvYmluLmVkY2VlNmU2LTJmNWQtNDdjNy05M2I1LThmNWFjN2MzZjEyNA=='  # Replace with your actual API key
    }

    # Define the payload for the API request
    payload = {
        "query": {
            "measures": ["account.total_accounts"],
            "dimensions": ["account.city"],
            "segments": [],
            "filters": [],
            "timeDimensions": [],
            "limit": 15,
            "offset": 0
        }
    }

    # Send the POST request to the API
    response = requests.post(url, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract relevant data
        account_data = data.get('data', [])
        
        # Convert to DataFrame for analysis or reporting
        df = pd.DataFrame(account_data)
        
        # Display the DataFrame
        print("City-wise Total Accounts:")
        print(df)

        # Optionally, save the DataFrame to a CSV file
        df.to_csv('city_account_data.csv', index=False)
        print("Data saved to city_account_data.csv")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}, Message: {response.text}")
    # Expected_Output

    City-wise Total Accounts:
        account.city  account.total_accounts
    0     Los Angeles                      59
    1         Chicago                      12
    2     Kansas City                      11
    3   San Francisco                       8
    4        New York                       6
    5         Houston                       5
    6    Philadelphia                       5
    7           Miami                       5
    8      Greenville                       5
    9      Sacramento                       4
    10          Omaha                       4
    11     Cincinnati                       3
    12     Fort Wayne                       2
    13         Denver                       2
    14    Minneapolis                       2
    Data saved to city_account_data.csv
    ```    

**Execution and Saving**:

- **Run Query Button**: Once dimensions and measures are selected, this button executes the query and updates the results in the selected view format (table, chart, pivot).
- **Save Perspective**: After running a query, users can save the configuration as a **Perspective** to easily return to the same query setup in the future.

## Model Tab

The Model tab offers insights into the underlying structure of the Data Product. It allows users to view and understand the data model, which is particularly useful for data architects or advanced users who need to know how different tables and fields are connected. This tab gives you a comprehensive view of relationships between datasets, enabling a better understanding of data lineage and dependencies.

**Left-side Navigation Panel**

The left-side navigation panel provides key options to explore the model in different ways:

- **Graph**: The default view, showing a visual lineage of how different tables and entities are interconnected. This interactive graph shows relationships between tables and views. Let us understand graph tab more with an detailed example.
- Our example has three main entities or logical tables: **account**, **sales**, and **product,** and two **metrics, conversion_rate and qtd_revenue,** represented by a wave-like icon. **Metrics** are derived from one or more logical tables to track performance or monitor trends, using defined measures and dimensions from these tables.The **Graph tab** visually displays how these logical tables and metrics are interconnected, providing an interactive way to explore data relationships and schema details.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(39).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

Here's how it works in more detail:

Further, when you click on any logical table or Metrics, a detailed tab opens on the side, displaying all the **defined measures and dimensions** within this table. Each attribute is accompanied by its **data type** (e.g., numeric, string, date) to understand the table's schema clearly. Let us dive deep into th**e sales logical table**

### **Sales (logical table):**

- This is a logical table containing information about **sales**.
- It shows how this table is connected to other entities in the system, such as **accounts**, **products**, and other metrics.
- When you click on the **sales** table, a detailed tab opens on the side, displaying all the **defined segments, measures, and dimensions** within this table. Each attribute is accompanied by its **data type** (e.g., numeric, string, date) to help you understand the table's schema clearly.

<!-- <center>
<img src="/interfaces/data_product_hub/exploration/dph_explorer_optimized_01.gif" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center> -->

<center>
<img src="/interfaces/data_product_hub/exploration/dph_explorer(1).gif" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

**Schema Breakdown**

- **Segments**: Subsets or groupings of sales data, such as **proof_sales** and **nonproof_sales**.
- **Measures**: Quantitative attributes that are crucial for calculations. Examples: **recency and frequency.**
- **Dimensions**: Categorical attributes that describe data segments or groupings. Examples: **invoice_no** **invoice_date.**
- You can explore more details by clicking on the **Schema** dropdown.

 *Let us also understand a Metric by giving an example.*

### **Metric**

Metrics are a type of view. All Metrics are represented by a wave-like icon resembling a formula, indicating that they are **Metrics**. **Metrics** are a type of **view** in the data model. Unlike logical tables, they do not have their dimensions or measures. Instead, they reference the dimensions and measures of **logical tables**. For example, the **conversion_rate** metric tracks the percentage of leads or prospects that convert into paying customers over a defined period (e.g., a month). However, It relies on fields from the **Sales Table.**

When a **metric** references a **measure** or **dimension** from a **logical table**, it adopts the naming convention `table_name + field_name`. This approach ensures that users can easily identify the origin of each measure or dimension used in a metric, promoting transparency and data lineage. For example, the measure **frequency** from the **Sales Table** is renamed **sales_frequency** when used in the **Conversion Rate Metric** to indicate its origin.

<center>
<img src="/interfaces/data_product_hub/exploration/Screenshot%20from%202024-10-01 18-32-47.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

<<<<<<< HEAD
=======

>>>>>>> 83f1c68a2524e022232f273f92e8edb848d70816
*Dashed blue lines visually indicate the relationships between the **Sales Table** and the **conversion_rate** metric. The lines highlight which **dimensions** and **measures** from the **Sales Table** are used to calculate the **conversion_rate** metric.*

Similarly,  **QTD Revenue** Metrics leverage fields from multiple logical tables—**Sales**, **Product**, and **Account**—to offer a rich, multi-dimensional view of performance. Using **join paths in the manifest file** ensures that fields are correctly referenced, maintaining clarity and consistency across the data model.

*The **blue dashed lines** in the graph visualization represent the relationships between the logical tables and the metrics, indicating how data from each table feeds into the metric calculations. This visual connection helps users understand how measures and dimensions from different sources contribute to the overall metric. All fields are prefixed with their respective table name (e.g., **sales_**, **product_**, **account_**), showing which fields from different tables are contributing to the metric.*


<center>
<img src="/interfaces/data_product_hub/exploration/Screenshot%20from%202024-10-01 18-39-56.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>


- **Schema**: This section contains detailed information about the structure of the tables, views, and entities within the data model. Users can view columns, data types, and relationships, making it easier to understand how data is stored and linked within the product.

### **Schema Section Components**

**Overview:** The **User Groups** section on the right panel details the access permissions applied to each user group and the API scopes that are granted. The **Security** section displays the redacted column name.

In this example, there are two user groups: **nonproof_analyst** and **default**. Both groups can access all API scopes, including **meta**, **data**, **graphql**, **jobs**, and **source**.

- The **nonproof_analyst** group includes a user identified by the tag `users:id:kanakgupta`.
- The **default** group includes all members, providing universal access to anyone not explicitly excluded from the model.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(40).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>


Further, when you click on the account table, The following sections are displayed.

1. **logical table Overview**:
    - **Table Name**: The logical table name (e.g., **account**) is displayed, providing context on the explored dataset.
    - **Table Type**: The type (e.g., **Table**) and whether it is **public** (True/False) are also indicated, providing insight into accessibility.
    - **Field Overview**: The schema section categorizes the table’s fields into **Measures**, **Dimensions**, and **Segments**, showing the **total number of each type**.
2. **Measures**:
    - Measures represent **quantitative** fields that are used in calculations or aggregations.
    - **Example**: The measure **total_accounts** in the **Account** table shows the total number of accounts. It is accompanied by information such as its data type (number), aggregation type (`count(distinct)`), and a brief description ("Total customers").
3. **Dimensions**:
    - Dimensions represent **qualitative** attributes used for categorization or grouping.
    - **Example**: Dimensions in the **Account** table include attributes like **customer_name**, **address**, **city**, and **state**. Each dimension is described by its data type (e.g., string, time), SQL reference, and a brief description explaining its purpose.
4. **Segments**:
    - If applicable, segments are listed, representing pre-defined filters within the table for more granular analysis.
5. **Additional Information**:
    - **Secure**: Indicates whether access to certain fields is restricted based on user permissions. For example, here, the email column is secured and redacted.
    - **Aliases**: Provides alternate names for fields if defined.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(41).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Account Table Schema</i></figcaption>
</center>


<center>
<img src="/interfaces/data_product_hub/exploration/image%20(42).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>The secure column header indicates that the Email column is redacted</i></figcaption>
</center>

One can explore the details on each table. For example, if we click on the account table, we can see details like the total number of measures and dimensions and details like whether the table is public or not. It also exposes the underlying data type, aggregate type, and its SQL.

<center>
<img src="/interfaces/data_product_hub/exploration/image%20(43).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

- **Files**: This contains all relevant SQL files, tables, views, and YAML files (e.g., user groups) necessary to define the **Lens**. Here, users can explore the actual implementation and configuration of the model, making it useful for developers or advanced users who need to see the code and metadata behind the Data Product.

For example, In the above image are the YAML Implementation files for the Lens model of the Data Product for all entities. One can also view the Lens artifact in the Metis by clicking on **Open in Metis** button in the right side corner 


<center>
<img src="/interfaces/data_product_hub/exploration/image%20(44).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>


## GraphQL Tab

For advanced users or developers, the **GraphQL** tab provides a powerful interface for writing and running GraphQL queries. GraphQL allows for precise data retrieval, giving you complete control over the structure of the data you receive. This is particularly useful when you need more complex or customized data extractions that go beyond the capabilities of the standard Studio interface.