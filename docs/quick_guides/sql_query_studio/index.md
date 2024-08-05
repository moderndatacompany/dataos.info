# Customize SQL and Aggregations with Studio 

!!! info "Information"
    In this quick guide, we'll explore the Studio feature of DataOS Workbench. Studio is designed to simplify the process of writing complex SQL queries.

Explore advanced techniques for customizing SQL statements and aggregations using the Studio feature. Whether you're a seasoned SQL pro or just getting started, Studio's intuitive interface will help you craft powerful SQL statements with ease.

Suppose you need to analyze sales data to identify trends over time. Instead of manually writing out SQL queries, Studio allows you to select the desired aggregates (like sum, average) and measures (like sales amount, quantity sold) from drop-down menus and generates SQL based on selection.

## Key Steps
Here are the essential steps to leverage the Studio feature.
<center>
<div style="text-align: center;">
<img src="/quick_guides/sql_query_studio/5_studio.png" alt="Steps to use Studio feature" style="border: 1px solid black;">
</div>
</center>

### **Step 1: Launching Studio**

Let's get hands-on with Studio! Start the **Workbench** App from DataOS Home and select the **catalog**, **schema**, and desired **table**. Click on the Studio icon, and in a moment, you will see its interface. 

![studio_feature.png](/quick_guides/sql_query_studio/studio_feature.png)

### **Step 2: Showing Raw Records**

Raw records represent the individual data entries in your dataset, containing raw, unprocessed information. 

Suppose you're analyzing a dataset containing Order data for a retail company. Examining the raw records in Studio lets you to view detailed information about each transaction, including the date, customer ID, product purchased, and order amount. This granular view will enable you to identify specific data for further analysis.

1. Click on **Raw Records**.
2. Select the columns of interest.
3. Click on the **Generate SQL** button. Studio will generate the SQL query for you.
4. Run the query to view the result.

![image](/quick_guides/sql_query_studio/raw_records.png)

### **Step 3: Performing Aggregate**

Studio simplifies data aggregation, enabling you to calculate sums, averages, counts, and more. It allows you to combine multiple data records into a single summary value, providing insights into overall trends and patterns within your dataset. 

1. In Studio, select measure. This is a quantitative attribute or metric that you want to analyze or aggregate, such as sales revenue, quantity sold, or customer count. From the drop-down, you can select the applicable aggregate functions for the columns.
    
    ![image](/quick_guides/sql_query_studio/aggregate.png)
    
2. Select Grouping Criterion.
    
    Grouping is a fundamental operation in data analysis that allows you to organize data based on specific criteria. In Studio, the "Group By" function enables you to group your data by **one or more attributes**, facilitating deeper analysis and comparison across different categories.
    
    ![grouping.png](/quick_guides/sql_query_studio/grouping.png)
    
3. Click on **Generate SQL.**
4. The process of generating SQL may take some time. 
5. Select the generated SQL query and Run the query.
    
    ![group_by_brand.png](/quick_guides/sql_query_studio/group_by_brand.png)
    

### **Step 4: Setting Time Interval for Grouping**

Granularity refers to the level of detail or refinement in your data analysis.  Studio allows you to adjust the granularity (such as daily, weekly, or monthly) of your analysis to suit your specific analytical needs. Let us explore sales performance at various levels of detail.

Suppose you want to analyze brand-wise sales data at different levels of granularity for sales trends. To find out the weekly brand-wise average sales amount for the last 30 days, follow the below steps.

1. Select "order_amount" as the measure.
2. Choose "Average" as the aggregation method.
3. Pick the "brand_name" column to group your data. It will allow you to aggregate sales data for each brand separately.
4. Choose the field representing time, such as "order_date" in this example.
5. Select the desired date range from the available options, such as 30 days for this example.
6. Set the granularity to Weekly.
7. Click on the “Generate SQL” button. Studio will automatically generate the SQL statement for you.
8. Run the query to view the results.

This way, you can get a comprehensive overview of revenue distribution across different brands for a specific period. 

![image](/quick_guides/sql_query_studio/time_interval.png)

### **Step 5: Filtering Data**

In Studio, filters enable you to refine your analysis by excluding irrelevant data or isolating specific segments of interest. 

**Adding rules and groups in filter conditions:**

1. **Add a Rule**:
    - Click the "Add Rule" button to create a new rule. Define the condition for the rule by selecting a field, operator, and value.
2. **Group Rules**:
    - If you have multiple rules and want to group them with logical operators (AND, OR), click the "Add Group" button.
    - Arrange the rules within the group by dragging and dropping them as needed.
    - Choose the logical operator (AND, OR) to define the relationship between the grouped rules.
3. **Nested Groups**:
    
    You can nest groups within other groups to create more complex filtering logic.
    
    - Click on the "Add Group" button within an existing group to create a nested group.
    - Define the conditions and logical operators for the nested group just like you did for the main group.

Let's assume you want to calculate the total order amount per region, but you also want to exclude certain records from the calculation, such as you are only interested in the age group (25-50). 

In Studio, follow the below steps to customize the SQL statement by adding a filter to exclude data points falling outside a defined range.

1. Click  **Aggregate**.
2. Select the desired measure from the drop-down.
3. Select fields for grouping. You can select multiple fields for nested groups.
4. Choose the field that represents time.
5. Specify filter condition with AND/OR operator.
6. Click **Generate SQL**.

    ![select_filters.png](/quick_guides/sql_query_studio/select_filters.png)

7. Run the generated query.
    
    ![image](/quick_guides/sql_query_studio/run_query.png)
    

So, whether you're crunching numbers for sales reports or finding patterns in your data, you can use Studio features to turn your SQL queries into actionable insights.