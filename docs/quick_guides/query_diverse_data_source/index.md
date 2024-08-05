# Querying Diverse Data Sources with DataOS Workbench

!!! info "Information"
    This session focuses on leveraging DataOS Workbench to query diverse data sources effectively, enabling organizations to derive meaningful insights from vast amounts of data stored across various platforms.

Organizations handle vast amounts of data across various storage systems, such as relational databases (e.g., MySQL, SQL Server, PostgreSQL) and object storage systems (e.g., S3, HDFS, Azure). The challenge lies in swiftly accessing the right data to derive meaningful insights.

DataOS query engines simplify this process by allowing SQL queries across relational and non-relational databases and object stores. With Minerva and Themis clusters, users can query data stored in diverse sources without needing to learn each database's specific query language. It streamlines data access and analysis, making it easier to derive insights. DataOS Workbench provides a unified interface for querying and analyzing diverse datasets. 

## Key Steps

<center>
<div style="text-align: center;">
<img src="/quick_guides/query_diverse_data_source/3_federated_query.png" alt="Steps to write federated query" style="border: 1px solid black;">
</div>
</center>

## Querying Across Data Sources

Let's consider an example where you need to analyze sales data stored in a PostgreSQL database and customer data stored in Microsoft Azure to identify the Most valuable customers as per Order Quantity. With DataOS Workbench, you can seamlessly connect to these disparate data sources and write federated SQL queries to combine the relevant data.

### **Step 1: Connect to Data Sources**

Ensure that Depots for accessing data sources are created and the Minerva cluster is properly configured to access these sources.

For the above query, we need two depots to fetch data from different sources [Azure MS-SQL and PostgreSQL database]. We also need a Minerva Cluster to run analytical queries with joins. 


### **Step 2: Open Workbench App and Explore Data**

1. Select catalog. 
    Under **Catalog**, you can see your data sources.

    ![MicrosoftTeams-image (55).png](/quick_guides/query_diverse_data_source/diverse_data_sources.png)

2. Write a query to view the data. 

    The following query shows the customer data from the Microsoft Azure data source.

    ![Untitled](/quick_guides/query_diverse_data_source/azure_data.png)

    The following query shows the sales data from the PostgreSQL data source.

    ![sample1.png](/quick_guides/query_diverse_data_source/pg_data.png)

### **Step 3: Analytical Query on Heterogeneous Data Sources**

1. Combine data from different data sources using a federated SQL query. 

    This query will join the data from both data sources.

    ```sql
    -- Highest valuable customers as per Order Quantity
    SELECT B.customerkey, sum(A.orderquantity) as total_order FROM "postgresqldbdatabase"."public".sales  as A
    join "azuresqldb"."dbo".customers as B
    on A.customerkey = B.customerkey
    group by 1
    order by 2 desc
    limit 5;
    ```

    Here is the result of the above query that shows the most valuable customers as per order quantity.

    ![MicrosoftTeams-image (54).png](/quick_guides/query_diverse_data_source/query_result.png)