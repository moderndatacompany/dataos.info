# Exploration of Semantic Model

!!! info "Overview"
    Learn how to explore and understand a Data Product’s semantic model in DataOS using Studio. This helps you connect data structure with business goals.

## 📘 Scenario

Imagine you’re a data analyst and want to analyze data product 'Product Affinity', aiming to leverage data insights for performance tracking and customer behavior analysis. By exploring its semantic model on Data Product Hub, you plan to access and analyze cross-sell and upsell opportunities, which involves examining dimensions, measures, and metrics like `customer_segments`, `product affinity scores`,and `total spending`. 

## Quick concepts

'Lens' is a key DataOS Resource in creating and implementing semantic models. Here’s what makes them powerful:

1. **Physical data sources**  
   Semantic models connect to a variety of physical data sources, such as Postgres, BigQuery, and Redshift. Knowing the origin helps you understand how the semantic model organizes it into logical structures.

2. **Lakehouse (Optional)**  
   For large datasets, you may unify data from multiple sources, making it easier to manage and query data. Consider storing the aggragated data to Lakehouse, a managed storage architecture that blends the strengths of both data lakes and data warehouses.

3. **Logical tables**  
   A semantic model maps physical data (from data sources or Lakehouse) to logical tables establishing relationships between data entities—making your work faster and clearer.

4. **Table properties**  
   When creating logical tables, SQL and key properties like schema, data types, and constraints are specified.

5. **Data quality and transformation**  
   Semantic models incorporate tools for ensuring high data quality and transforming raw data into user-friendly formats. By maintaining accuracy, consistency, and reliability, semantic models ensure that the data is ready for exploration.

6. **Metrics**  
   Semantic models define meaningful metrics to track performance or key business indicators.

7. **Consumption ports**  
   Semantic models enable versatile data consumption options, such as BI tools and APIs for seamless integration with GraphQL and Studio for advanced analytics.


## Uncover insights from Semantic Model

Exploring semantic models allows you to understand the data flow, relationships within the data, and the transformations that drive insights.

**Navigate to the ‘Explore’ option**
    
1. On the Data Product details pageand click 'Explore' to navigate to the Studio in the Data Product Hub.

    ![exploration_page.png](/learn/dp_consumer_learn_track/explore_sm/exploration_page.png)

2. You'll land in the Explore view with tabs: Studio, Model, and GraphQL.

    ![sm_explore.png](/learn/dp_consumer_learn_track/explore_sm/sm_explore.png)

Before exploring data via the semantic model in Studio, let us understand the model fully. 
    

## Access model to unpack data structure

You first decide to explore the Model. As you open the Model tab, you start exploring the structure of the Data Product, gaining insights into the connections and dependencies across datasets. 

### **Visualize connections in Graph view**

The **Graph** view offers a visual representation of the 'Product Affinity' semantic model, showcasing how logical tables and entities are interconnected, with key metrics highlighting their relationships.

Explore entities like `Customer`, `Product`, and `Purchase` Data along with key metrics like `cross_sell_opportunity`, `total_spending`, and `purchase_frequency`. Metrics marked with a wave icon are derived from logical tables, showing their role in performance tracking. For example, `cross_sell_opportunity_score` is created using members from the `purchase` and `product` tables, while `purchase_history` and `total_spending` are built using dimensions and measures from these logical tables.

![model_schema.png](/learn/dp_consumer_learn_track/explore_sm/model_schema.png)

Click 'Show Fullscreen' to explore the model easily. Then, use 'Expand All' to view all measures, dimensions, entities, and metrics for detailed insights.

To examine the members of a single metric, say `total_spending`. You hover over it and get the names of the dimensions and measures taken from purchase_data and the product table represented by the blue dashed line. The blue dashed lines highlight which dimensions and measures from the tables are utilized to calculate the metric. This referencing adopts a naming convention where each measure or dimension is prefixed with its table name, like `purchase_total_spend`. This convention and visual representation make it easy to understand the relationships and dependencies within the data model.

![metric_referennce.png](/learn/dp_consumer_learn_track/explore_sm/metric_referennce.png)

You click on a metric, say `cross_sell_oppurtunity_score`, which opens a side panel detailing all measures, segments, and dimensions within it. You can see each attribute's data type (numeric, string, date).

![customer_schema.png](/learn/dp_consumer_learn_track/explore_sm/customer_schema.png)

### **Explore details in Schema section**

Under 'Schema', gain insight into the table structure, column names, data types, and primary keys. This detailed breakdown ensures that you have a thorough understanding of data hierarchies and access control.

![schema.png](/learn/dp_consumer_learn_track/explore_sm/schema.png)

The 'Overview' section gives you additional details, such as the Lens model’s name and user groups  (default), and the API scopes give the info on the level of access given to the users included in the group and the redacted fields for data security. Here, the group includes *, which means everyone provides access to all other members.

![schema_overview.png](/learn/dp_consumer_learn_track/explore_sm/schema_overview.png)

You select a table `customer` to get more details on the table.

![customer_table.png](/learn/dp_consumer_learn_track/explore_sm/customer_table.png)

The schema section shares the following details:

**Quick schema insights**

- **Name & Type**: E.g., `Customer` table.
- **Measures**: Like `total_customers` with count logic.
- **Dimensions**: Fields like `customer_id` (primary key), `country`, `segments`.
- **Segments**: Optional pre-defined filters for granular analysis.
- **Additional Info**: Displays redacted fields and user access as you set them in the Lens user groups and data policy manifest file.

### **Explore configuration in Files section**

View all relevant SQL files, tables, views, and YAML files essential for defining the Lens. This resource helps you explore the actual implementation and configuration of the model. You can click the 'Open in Metis' button in the top right corner to access the semantic model artifact in Metis.

## Analyze data with Studio

Start in the 'Studio' tab—an interactive, no-code workspace to query and visualize data as tables, charts, and pivots.

![studio_tab.png](/learn/dp_consumer_learn_track/explore_sm/studio_tab.png)

### **Checking Cluster health**

1. Hover over the cluster name, like Minerva, to view its details.

2. Toggle the Watch button to monitor cluster health. Close the window and you see a green dot indicating good health.  The Cluster is ready and you can proceed with further exploration, assured that any queries you run will perform smoothly.

    ![source_health.png](/learn/dp_consumer_learn_track/explore_sm/source_health.png)


### **Creating a query**

Let's analyze the total number of customers per country:

1. Select the `country` dimension and the `total_customers` measure.
    
    ![table.png](/learn/dp_consumer_learn_track/explore_sm/table.png)
    
2. Hit Run Query to generate the query result as table which you can change later in Chart.

    ![query_result.png](/learn/dp_consumer_learn_track/explore_sm/query_result.png)

3. Sort your data to see the top 5 countries by total customers. Use Order By with `total_customers` in descending order and limit the results to 
    
    ![order_by.png](/learn/dp_consumer_learn_track/explore_sm/order_by.png)
    

### **Saving analysis as a Perspective**

Save your query result for later by clicking 'Save Perspective'. Give it a meaningful name, like 'Country-wise Total Customers,' and save it.

![perspective.png](/learn/dp_consumer_learn_track/explore_sm/perspective.png)

Once you save any Perspective, it will be accessible to everyone and can be accessed in the Perspective section of Explore Studio.

![access_perspective.png](/learn/dp_consumer_learn_track/explore_sm/access_paerspective.png)

<aside class="callout">
🗣️ If you want to download the findings, click on the download ⬇️ icon next to the 'Save Perspective' button to download it. It will ask you to download the table in various formats, such as csv, json, etc., as shown in the image below.

</aside>

### **Visualizing data with charts**

Transform your table into a visual story:

1. Switch to the Chart tab and select the chart type, Line, or Bar Chart.
    
    ![bar_chart.png](/learn/dp_consumer_learn_track/explore_sm/bar_chart.png)
    
2. When you select the 'Line Chart' option, the chart will change from a bar chart to a line chart. Configure the chart by toggling value labels for a clearer view.
    
    ![line_chart.png](/learn/dp_consumer_learn_track/explore_sm/line_chart.png)
    
3. But here, you are not able to see the actual values of each country, so to be able to display the value labels on top of each country, you click the 'Configure' button as shown below:
    
    ![configure_button.png](/learn/dp_consumer_learn_track/explore_sm/configure_button.png)
    
    A pop window appears as you click on the Configure button; here, you click on the Value labels toggle to change the label from Hidden to Top.
    
    ![Series.png](/learn/dp_consumer_learn_track/explore_sm/Series.png)
    
    As you click on the Top button, the value labels are visible on top of the bars, as shown in the below image, giving you the exact count.
    
    ![chart_tab.png](/learn/dp_consumer_learn_track/explore_sm/chart_tab.png)
    
4. Now, you want to name both axes to make it more readable. For it, you click the Configure section and choose the Axes section in it.
    
    Now, you label both the axes as given in the following image:
    
    ![axes.png](/learn/dp_consumer_learn_track/explore_sm/axes.png)
    

5. Now, your graph is ready! After the chart is prepared, you will send this insight to one of your stakeholders. To do this, you click on the 'Export' button, save it in JPEG format, and click the 'Download' button.
    
    ![export_chart.png](/learn/dp_consumer_learn_track/explore_sm/export_chart.png)
    
    You can 'hide specific fields' by clicking the 'eye icon' next to the field name. This is useful for focusing on only the most relevant data points in your analysis.
    
6. When you're ready to start a new analysis, quickly reset all selected dimensions and measures by clicking the 'Clear' button. This action will instantly deselect your previous choices, as shown in the image below:
 
    ![members.png](/learn/dp_consumer_learn_track/explore_sm/members.png)
 

### **Filtering data**

After clearing all members, you move to analyze some data with filters on and want to get insight on the following scenario:

**Example:** Distribution of customer marital status for income above $50,000.

For this analysis, you choose the following members:

- **Measures:** total_customers
- **Dimensions:** marital_status, income
- **Filter condition(on Dimension):** Income > 50,000

![filter.png](/learn/dp_consumer_learn_track/explore_sm/filter.png)

<aside class="callout">
🗣️
To apply a filter, first select the dimension you want to filter—this will make it available as an option in the 'Filter' section. If you don’t want the selected dimension to appear in the query result, you can hide it.

</aside>

Here is the query result.

![query_results.png](/learn/dp_consumer_learn_track/explore_sm/query_results.png)

### **Using History for Quick Access**

If you want to revisit a query you ran an hour ago but didn't save as a Perspective, simply click on the 'History' icon and select the relevant timestamp to return to that query.

![history.png](/learn/dp_consumer_learn_track/explore_sm/history.png)

To save a query from two days ago for future reference, click on the query, give it a name, and save it. You can easily access it whenever needed, as demonstrated here.

![history.gif](/learn/dp_consumer_learn_track/explore_sm/history.gif)

### **Creating a Pivot Table**

**Example:** Analyze the relationship between customer segments, countries, and total spending:

1. Select:
    - **Dimensions**: `customer_segments`, `country`
    - **Measure**: `total_spend`
2. Click Run Query. 
    
    ![query_for_pivot.png](/learn/dp_consumer_learn_track/explore_sm/query_for_pivot.png)
    
3. To make this more understandable, switch to the Pivot tab. Drag and drop your fields to rows and columns area.
    
    > The Pivot option is available only after running the query.
    > 
    
    ![pivot.gif](/learn/dp_consumer_learn_track/explore_sm/pivot.gif)
    
    This matrix will help you identify:
    
    - High-risk customers by segment and country.
    - Which countries have the highest total spend.
    - Potential focus areas for cross-selling or customer retention efforts based on risk levels and regional data.
    
    To learn more about creating Pivot tables for query results, refer to the [Quick start guide](https://dataos.info/quick_guides/eda_pivot/) on the topic.
    

## Integration with API

<aside class="callout"> ⚠️ <b>Developer-Focused Section</b>: This content is specifically intended for <b>developers</b> or <b>technical users</b> who want to integrate data programmatically into apps, pipelines, or services using APIs.  

If you're a <b>business user</b> exploring data through visual tools (like dashboards or Studio), you can skip this section—no action needed.
</aside>

👉 Developers: [Click here to learn more about API Integeration →](/learn/dp_consumer_learn_track/explore_sm/api_integration/)

## Self-check quiz

**1. What does the Studio tab in DataOS allow you to do?**

&nbsp;&nbsp;A. View data lineage <br>
&nbsp;&nbsp;B. Write Python scripts <br>
&nbsp;&nbsp;C. Run drag-and-drop queries and visualize results <br>
&nbsp;&nbsp;D. Edit data pipelines <br>

**2. What does the ‘Save Perspective’ option help with?**

&nbsp;&nbsp;A. Archives old datasets <br>
&nbsp;&nbsp;B. Schedules automated reports <br>
&nbsp;&nbsp;C. Saves your query view for future reuse <br>
&nbsp;&nbsp;D. Deletes previous charts <br>

**3. A stakeholder requests a downloadable chart of total customers by country. What's the best approach?**

&nbsp;&nbsp;A. Write a SQL query in Metis <br>
&nbsp;&nbsp;B. Use the Studio tab → Chart view → Configure labels → Download <br>
&nbsp;&nbsp;C. Use the GraphQL tab <br>
&nbsp;&nbsp;D. Explore it in the Files section <br>

**4. While performing analysis, you wrote a query yesterday in Studio but forgot to save. How can you retrieve it?**

&nbsp;&nbsp;A. It’s lost unless exported <br>
&nbsp;&nbsp;B. Use the Graph View<br>
&nbsp;&nbsp;C. Go to Studio → History tab → Locate by timestamp <br>
&nbsp;&nbsp;D. Check in API logs<br>

**5. You want to filter high-income customers for a marketing campaign analysis. Which steps should you follow?**

&nbsp;&nbsp;A. Select only total_customers and click Run<br>
&nbsp;&nbsp;B. Apply filter income > 50000 in Studio <br>
&nbsp;&nbsp;C. Use Pivot before filtering<br>
&nbsp;&nbsp;D. Create a new semantic model<br>

**6. While analyzing total spending by segment and country, you need a visual summary. What tool should you use?** 

&nbsp;&nbsp;A. Pivot tab in Studio <br>
&nbsp;&nbsp;B. Files tab in Model<br>
&nbsp;&nbsp;C. Postgres terminal<br>
&nbsp;&nbsp;D. Explore via GraphQL<br>

## Next step

Now that you understand your data model, move on to learning how DataOS enforces Data Product Quality.

👉 [Knowing the Quality of Data Products](/learn/dp_consumer_learn_track/dp_quality/)