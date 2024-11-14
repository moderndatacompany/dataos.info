# Exploration of semantic model

In this topic, we’ll walk you through navigating and understanding the associated semantic model of Data Product to explore data in Studio to understand how it aligns with business goals.

## Scenario

Imagine you’re a data analyst and want to analyze data product 'Product360', aiming to leverage data insights for performance tracking and customer behavior analysis. By exploring its semantic model on **Data Product Hub**, you plan to access and analyze cross-sell and upsell opportunities, which involves examining dimensions, measures, and metrics like **customer segments, product affinity scores,** and **total spending**. Let’s see how this exploration unfolds.

## Uncover insights from your Semantic Model

1. **Navigate to the ‘Explore’ option**
    
    On the Data Product details page, click the "Explore" button to navigate to the Studio in the Data Product Hub.
    
    ![exploration_page.png](/learn/dp_consumer_learn_track/explore_sm/exploration_page.png)
    
    Here, the interface displays various tabs.
    
    You observe three tabs given  **Studio**, **Model**, and **GraphQL** to analyze the data model for different purposes.
    
    ![sm_explore.png](/learn/dp_consumer_learn_track/explore_sm/sm_explore.png)
    
    Before exploring data via the semantic model in **Studio**, let us understand the model fully. 
    

## Access model for unpacking the data structure

You first decide to explore the Model. As you open the **Model** tab, you start exploring the structure of the Data Product, gaining insights into the connections and dependencies across datasets. 

### **Visualize Connections in the Graph View**

The **Graph** view offers a visual representation of the 'Product360' semantic model, showcasing how logical tables and entities are interconnected, with key metrics highlighting their relationships.

Explore entities like **Customer**, **Purchase**, and **Purchase Data** along with key metrics like **cross_sell_opportunity**, **total_spending**, and **purchase_frequency**. Metrics marked with a wave icon are derived from logical tables, showing their role in performance tracking. For example, **cross_sell_opportunity_score** is created using members from the **purchase_data** and **product** tables, while **purchase_history** and **total_spending** are built using dimensions and measures from these logical tables.

![model_schema.png](/learn/dp_consumer_learn_track/explore_sm/model_schema.png)

Click **Show Fullscreen** to explore the model easily. Then, use **Expand All** to view all measures, dimensions, entities, and metrics for detailed insights.

![schema_fullscreen.png](/learn/dp_consumer_learn_track/explore_sm/schema_fullscreen.png)

To examine the members of a single metric, say **total_spending. Y**ou hover over it and get the names of the dimensions and measures taken from purchase_data and the product table represented by the blue dashed line. The blue dashed lines highlight which dimensions and measures from the tables are utilized to calculate the **total-spending** metric. This referencing adopts a naming convention where each measure or dimension is prefixed with its table name, like `purchase_data_total_spend`. This convention and visual representation make it easy to understand the relationships and dependencies within the data model.

![metric_referennce.png](/learn/dp_consumer_learn_track/explore_sm/metric_referennce.png)

You click on a metric, say **cross_sell_oppurtunity_score,** which opens a side panel detailing all measures, segments, and dimensions within it. You can see each attribute's data type (numeric, string, date).

![customer_schema.png](/learn/dp_consumer_learn_track/explore_sm/customer_schema.png)

### **Explore Details in the Schema Section**

Under **Schema**, gain insight into the table structure, column names, data types, and primary keys. This detailed breakdown ensures that you have a thorough understanding of data hierarchies and access control.

![schema.png](/learn/dp_consumer_learn_track/explore_sm/schema.png)

Here you gain access to specific information about table structures, columns, data types, and relationships, deepening your understanding of how data is stored and connected within the Data Product. The **Overview** section gives you additional details, such as the Lens model’s name and user groups  (default), and the API scopes give the info on the level of access given to the users included in the group and the redacted fields for data security. Here, the group includes *, which means everyone provides access to all other members.

![schema_overview.png](/learn/dp_consumer_learn_track/explore_sm/71c9f0db-a619-4394-9139-630e0de7eb84.png)

You select a table **customer** to get more details on the table.

![customer_table.png](/learn/dp_consumer_learn_track/explore_sm/99e6316a-f97d-4c9a-885a-7c399e763d40.png)

The schema section shares the following details:

- **Table Name and Type**: The name **Customer** is shown along with its type which is a table.
- **Measures**: Here, **total_customers** provides a quantitative count of customers, with its data type and aggregation type shown.
- **Dimensions**: C**ustomer_id**, **country**, and **customer_segments** are categorized as data within the **Customer** table. You observe the key on the `customer_id` row, indicating that the `cusotmer_id` the primary key of the `customer` table.
- **Segments**: If available, pre-defined filters enhance granular analysis. Here, there are no segments defined, hence zero.
- **Additional Info**: Secured and redacted fields for sensitive data protection will be shown at the bottom as you set them in the Lens user groups and data policy manifest file.

Each element you explore reinforces your understanding of how data connects, ensuring you can confidently interact with and analyze the Data Product. 

### **Delve into Configuration in the Files Section**

View the underlying SQL, YAML files, and other resources to see the logic and structure of the data model.

This section contains all relevant SQL files, tables, views, and YAML files essential for defining the Lens. This resource proves invaluable as you explore the actual implementation and configuration of the model.

You begin examining the files available, recognizing that this is a crucial feature for developers who need access to the underlying code and metadata that powers the Data Product. As you look through the list, you see the YAML implementation files for the Lens model, which span all entities involved in your analysis.

If you want further details, notice the **Open in Metis** button in the top right corner. You click this button to access the semantic model artifact in Metis.

Engaging with the **Files** section, you understand the Data Product’s structure and logic, empowering you to effectively develop and manage your data workflows.

## Analyze data with Studio

You begin your exploration on the **Studio** tab, which opens by default when you access the Explore page. This interactive workspace is designed for data consumers who want to create queries to analyze and visualize data as tables, pivot tables, and charts- all without coding skills.

![studio_tab.png](/learn/dp_consumer_learn_track/explore_sm/studio_tab.png)

### **Checking Cluster health**

1. Hover over the cluster name, like **Minerva**, to view its details.

2. Toggle the **Watch** button to monitor cluster health. Close the window and you see a green dot indicating good health.  The Cluster is ready and you can proceed with further exploration, assured that any queries you run will perform smoothly.

    ![source_health.png](/learn/dp_consumer_learn_track/explore_sm/source_health.png)


### **Creating a query**

**Scenario: Total Customers by Country**

Let's analyze the total number of customers per country:

1. **Select** the `country` dimension and the `total_customers` measure.
    
    ![table.png](/learn/dp_consumer_learn_track/explore_sm/table.png)
    
2. Hit **Run Query** to generate the query result as table which you can change later in Chart.

![query_result.png](/learn/dp_consumer_learn_track/explore_sm/query_result.png)

3. Sort your data to see the top 5 countries by total customers. Use **Order By** with `total_customers` in descending order and limit the results to 
    
    ![order_by.png](/learn/dp_consumer_learn_track/explore_sm/order_by.png)
    

### **Saving your analysis as a Perspective**

Save your query result for later by clicking **Save Perspective**. Give it a meaningful name, like "Country-wise Total Customers," and save it.

![perspective.png](/learn/dp_consumer_learn_track/explore_sm/perspective.png)

Once you save any Perspective, it will be accessible to everyone and can be accessed in the Perspective section of Explore Studio.

 

![access_perspective.png](/learn/dp_consumer_learn_track/explore_sm/dc0927ba-08ae-4376-8e91-3e9743a31943.png)

<aside class="callout">
🗣

If you want to download the findings, click on the download ⬇️ icon next to the **Save Perspective** button to download it. It will ask you to download the table in various formats, such as csv, json, etc., as shown in the image below.

</aside>

### **Visualizing Data with Charts**

Transform your table into a visual story:

1. **Switch to the Chart** tab and select the chart type, Line, or Bar Chart.
    
    ![bar_chart.png](/learn/dp_consumer_learn_track/explore_sm/bar_chart.png)
    
2. When you select the 'Line Chart' option, the chart will change from a bar chart to a line chart. Configure the chart by toggling value labels for a clearer view.
    
    ![line_chart.png](/learn/dp_consumer_learn_track/explore_sm/line_chart.png)
    
3. But here, you are not able to see the actual values of each country, so to be able to display the value labels on top of each country, you click the '**Configure**' button as shown below:
    
    ![configure_button.png](/learn/dp_consumer_learn_track/explore_sm/configure_button.png)
    
    A pop window appears as you click on the Configure button; here, you click on the Value labels toggle to change the label from **Hidden** to **Top.**
    
    ![Series.png](/learn/dp_consumer_learn_track/explore_sm/Series.png)
    
    As you click on the Top button, the value labels are visible on top of the bars, as shown in the below image, giving you the exact count.
    
    ![chart_tab.png](/learn/dp_consumer_learn_track/explore_sm/chart_tab.png)
    
4. Now, you want to name both axes to make it more readable. For it, you click the Configure section and choose the Axes section in it.
    
    Now, you label both the axes with a suitable name as given in the following image:
    
    ![axes.png](/learn/dp_consumer_learn_track/explore_sm/axes.png)
    

5. Now, your graph is ready! After the chart is prepared, you will send this insight to one of your stakeholders. To do this, you click on the **Export** button, save it in JPEG format, and click the **Download** button.
    
    ![export_chart.png](/learn/dp_consumer_learn_track/explore_sm/export_chart.png)
    
    You can **hide specific fields** by clicking the **eye icon** next to the field name. This is useful for focusing on only the most relevant data points in your analysis.
    
6. When you're ready to start a new analysis, quickly **reset all selected dimensions and measures** by clicking the **Clear** button. This action will instantly deselect your previous choices, as shown in the image below:
 
    ![members.png](/learn/dp_consumer_learn_track/explore_sm/members.png)
 

### **Filtering Data**

After clearing all members, you move to analyze some data with filters on and want to get insight on the following scenario:

**Example:** Distribution of customer marital status for income above $50,000.

For this analysis, you choose the following members:

- **Measures:** total_customers
- **Dimensions:** marital_status, income
- **Filter condition(on Dimension):** Income > 50,000

![filter.png](/learn/dp_consumer_learn_track/explore_sm/filter.png)

<aside class="callout">
🗣

You need to first select the dimension you want to apply the filter to—only then will it appear as an option in the **Filter** section. You can also **hide the selected dimension** if you don't want it to be part of the query result.

</aside>

Here is the query result.

![query_results.png](/learn/dp_consumer_learn_track/explore_sm/query_results.png)

### **Using History for Quick Access**

If you want to revisit a query you ran an hour ago but didn't save as a Perspective, simply click on the **History** icon and select the relevant timestamp to return to that query.

![history.png](/learn/dp_consumer_learn_track/explore_sm/history.png)

To save a query from two days ago for future reference, click on the query, give it a name, and save it. You can easily access it whenever needed, as demonstrated here.

[history.gif](/learn/dp_consumer_learn_track/explore_sm/history.gif)

### **Creating a Pivot Table**

**Example:** Analyze the relationship between **customer segments**, **countries**, and **total spending**:

1. Select:
    - **Dimensions**: `customer_segments`, `country`
    - **Measure**: `total_spend`
2. Click **Run Query.** 
    
    ![query_for_pivot.png](/learn/dp_consumer_learn_track/explore_sm/query_for_pivot.png)
    
3. To make this more understandable, switch to the **Pivot** tab. Drag and drop your fields to rows and columns area.
    
    > The Pivot option is available only after running the query.
    > 
    
    ![pivot.gif](/learn/dp_consumer_learn_track/explore_sm/pivot.gif)
    
    This matrix will help the you identify:
    
    - High-risk customers by segment and country.
    - Which countries have the highest total spend.
    - Potential focus areas for cross-selling or customer retention efforts based on risk levels and regional data.
    
    To learn more about creating Pivot tables for query results, refer to the [quick start guide](https://dataos.info/quick_guides/eda_pivot/) on the topic.
    

## Integration with API

Some team members, who are developers working on a data-driven application, need a flexible and efficient way to query and retrieve specific data, a specific metric or a subset of data, from the system, . 

For teams needing to fetch data programmatically, the **Integration** tab provides options:

![integration_tab.png](/learn/dp_consumer_learn_track/explore_sm/integration_tab.png)

Let’s assume you must fetch the **total number of customers by country**. Rather than building REST endpoints, you can efficiently query the data using a **`curl`** command, **`GraphQL`**, or **`Postgres`**, depending on your preference. These methods allow you to retrieve data from a given endpoint and present it in a user-friendly format within your application.

First, select the following dimensions and measures:

- `total_customers`
- `country`

### **Using Curl**

To access your data over HTTP using `curl`, follow these steps:

1. **Copy the `curl` Command**
    
    Go to the **Integration** section and choose **Curl** option. Copy the provided Curl command and paste it into your terminal.
    
    ![using_curl.png](/learn/dp_consumer_learn_track/explore_sm/using_curl.png)
    
2. **Replace Placeholder**
You will notice a placeholder for `<api_key>` in the command. Replace it with your actual API key. This will allow you to fetch the required data for integration into your application.

### **Using GraphQL**

GraphQL is another option for querying data over HTTP. 

To use GraphQL:

1. Select **GraphQL** in integration options.
2. **Copy GraphQL Query**
    
    Click on **GraphQL** and copy the query provided.
    
3. **Test the Query**
    
    You can either paste the query into your terminal or click **Try it out** to test it in the GraphQL playground.
    
    ![graphql_tab.png](/learn/dp_consumer_learn_track/explore_sm/graphql_tab.png)
    

 4. **View Data in GraphQL Interface**

After testing, you can view the results in the GraphQL interface alongside the Studio tab.

![graphql.png](/learn/dp_consumer_learn_track/explore_sm/graphql.png)

You can now successfully integrate the query code into your application.

### **Using Postgres**

For those who prefer using the Postgres database, follow these steps:

1. **Copy Postgres Command**
    
    To interact with the Postgres database, copy the given PSQL client command and paste it into your terminal. When prompted for a password, enter your API key.
    
    ![postgres.png](/learn/dp_consumer_learn_track/explore_sm/postgres.png)
    
2. **Retrieve the API Key**
    
    To get the API key, click on the link in the password section of your connection details.
    
3. **Expected Output**
    
    Once you enter the command in the terminal, the following output confirms that the Postgres database connection was successful:
    
    ```bash
    psql (16.4 (Ubuntu 16.4-0ubuntu0.24.04.2), server 14.2 (Lens2/public:cross-sell-affinity v0.35.60-9))
    
    lens:public:cross-sell-affinity=>
    ```
    
    You can now interact with the Lens or semantic model using Postgres commands. For example, to list all tables in the connected database, use:
    
    ```yaml
    lens:public:cross-sell-affinity=> /dt
    ```
    
    **Expected Output:**
    
    ```yaml
                           List of relations
     Schema |             Name             | Type  |     Owner
    --------+------------------------------+-------+----------------
     public | cross_sell_opportunity_score | table | iamgroot
     public | customer                     | table | iamgroot
     public | product                      | table | iamgroot
     public | purchase_data                | table | iamgroot
     public | purchase_frequency           | table | iamgroot
     public | total_spending               | table | iamgroot
    
    ```
    
    ### **Additional PostgreSQL Commands for Reference**
    
    Here are some useful commands to interact with the Postgres database:
    
    | **Command** | **Description** | **Example** |
    | --- | --- | --- |
    | `\d [table_name]` | Show the schema and details of a specific table. | `\d customers` |
    | `\l` | List all databases in the PostgreSQL server. | `\l` |
    | `\du` | List all roles and users in the PostgreSQL server. | `\du` |
    | `\dn` | List all schemas in the database. | `\dn` |
    | `\dv` | List all views in the connected database. | `\dv` |
    | `\q` | Exit the PostgreSQL prompt. | `\q` |



## Next step

Learn more about the quality checks applied to ensure that Data Product meets data standards.

[Knowing the Quality of Data Products](/learn/dp_consumer_learn_track/dp_quality/)