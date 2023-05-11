# Querying Heterogeneous Data Sources

Organizations store their large amounts of data in several databases and storage systems, such as relational databases (MySQL, SQL Server, PostgreSQL) and object storage systems (S3, HDFS, Azure). Now the challenge faced by organizations is to quickly access the right data to create meaningful insights from stored data.

Minerva simplified this by enabling the querying of relational and non-relational databases and object stores via SQL. You can now run SQL queries across data stored in relational, non-relational, object, and custom data sources and get the desired data for further analysis.

The most significant advantage is that the users don't need to know each database's specific query or data language.

This article aims to discuss how we can configure different depots/connectors to run heterogeneous queries with complex joins across different data sources, how to configure the Minerva cluster to access these data sources, and how you can configure policies to protect sensitive information when running Minerva queries.

# Introduction to the Use Case

This article demonstrates a use case where the customer and sales transaction data are fetched from the different data sources [Azure MS-SQL and PostgreSQL database], and a Minerva Cluster is created to run analytical queries with joins. The query is written using DataOS Workbench.

# Steps performed to solve the use case

1. Prepare the data sources with sample data
2. Create Depots to access data from the above data sources
3. Create Minerva Cluster
4. Run the queries on Workbench targeted to the newly created cluster
5. Show the query output as a result of performing join for the data from two different data sources

## Prepare the Data Sources for the use case

- [Customer Data in Microsoft Azure Page](Querying%20Heterogeneous%20Data%20Sources/Customer%20Data%20in%20Microsoft%20Azure.md)

- [Sales Data in PostgreSQL Database Page](Querying%20Heterogeneous%20Data%20Sources/Sales%20Data%20in%20PostgreSQL%20Database.md)

## Create Depots

You need to create depots to access the sample data stored in Microsoft Azure and PostgreSQL. 

1. Open the source code editor and create the following YAML files.

    <u>Microsoft Azure SQL Database Depot</u>

    ```yaml
    version: v1beta1
    name: "azuresqldb"                      # Name of the Depot
    type: depot
    tags:
      - mssql
    layer: user
    depot:
      type: JDBC                             # Depot type
      description: "Azure SQL DB containing Customer and Productdata"
      spec:
        subprotocol: "sqlserver"             # Infromation from Connection String
        host: "weekly-expense.database.windows.net"
        port: 1433
        database: weekly-expense-database
      external: true
      connectionSecret:
        - acl: rw                           # Access Control Level 
          type: key-value-properties
          data:
            username: ##### 
            password: #######
    ```

    PostgreSQL Database Up Yaml

    ```yaml
    version: v1beta1
    name: postgresqldb                                         # database name 
    type: database
    description: Sample database created for testing.
    tags:
      - book
    database:
      migrate:
        includes:
          - ./Migration    # all up & down sql files.
        command: up
    ```

1. Use the `apply` command to create the Depot resource in DataOS.

    ```bash
    ~$ dataos-ctl apply -f /home/arike/Desktop/Everything_Folder/Azure/Azure_sql_depot.yaml 
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying azuresqldb:v1beta1:depot...       
    🚨 v1beta1 has been replaced by versions v1 for type depot 🚨
    please update as v1beta1 will be deprecated in the next release, and auto-migrate will be disabled
    INFO[0002] 🔧 applying azuresqldb:v1:depot...updated     
    INFO[0002] 🛠 apply...complete
    ```

    You can see the created depot on DataOS UI under Datanet > Depots.

    <img src="Querying%20Heterogeneous%20Data%20Sources/Untitled_(3).png" 
      alt="Picture"
      style="display: block; margin: auto" />

    > Note: In the same way as shown for Azure SQL Database Depot, you need to use the `apply` command to create a depot to access PostgreSQL sales data.
    > 

## Create Minerva Cluster

To run your queries, you need a Minerva cluster. To enhance the performance of *your*
 analytics workloads, *choose* appropriately sized clusters, or create a new dedicated cluster for your requirements. In this example, a new cluster is created with the steps given below.

> Note: You need ‘Operator’ level permissions to create cluster resources in DataOS.
> 
1. Open source code editor and create the cluster YAML.

    ```yaml
    name: samplesports #cluster name
    version: v1beta1
    type: cluster                        # Resource Type
    tags:
      - cluster
    description: Cluster to expose Azure Sql DB and Postgre Depots
    cluster:
      runAsApiKey: <API KEY>            # Replace with API Key
      compute: query-default
      minerva:
        replicas: 1 
        routingGroup: sqlddatabases  # routing group name (eg adhoc RG and minervaa and minervab is cluster name)
        doNotBroadcast: false
        resources: # resources configuration
          requests:
            cpu: 2000m
            memory: 2Gi
          limits:
            cpu: 2000m
            memory: 2Gi
        depots:                           # depots to access the data in this cluster
          - address: dataos://azuresqldb:dbo
          - address: dataos://postgresqldatabase
        debug:
          logLevel: INFO
          trinoLogLevel: ERROR
    ```

1. Use the `apply` command to create the Cluster resource in DataOS. You can see the created cluster on DataOS UI under Workbench > Cluster.

    <img src="Querying%20Heterogeneous%20Data%20Sources/sample0.png" 
        alt="Picture"
        style="display: block; margin: auto" />

    Under Catalogue, you can see your data sources.

    <img src="Querying%20Heterogeneous%20Data%20Sources/MicrosoftTeams-image_(55).png" 
      alt="Picture"
        style="display: block; margin: auto" />

1. Write a query to view the data.

    The following query shows the customer data from the Microsoft Azure data source.

    <img src="Querying%20Heterogeneous%20Data%20Sources/Untitled.png" 
      alt="Picture"
        style="display: block; margin: auto" />

    The following query shows the sales data from the PostgreSQL data source.

    <img src="Querying%20Heterogeneous%20Data%20Sources/sample1.png" 
      alt="Picture"
        style="display: block; margin: auto" />

# Analytical Query from Heterogeneous Data Sources

This query will perform the join on the data from both data sources.

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

<img src="Querying%20Heterogeneous%20Data%20Sources/MicrosoftTeams-image_(54).png" 
        alt="Picture"
        style="display: block; margin: auto" />

## More Scenarios

Once you set up the database access and cluster, you can perform analyses of the data for more insights. Here are some of the example scenarios and respective queries.

```sql

-- Highest Selling Products as Per Quantity
SELECT A.productkey, C.productname, sum(A.orderquantity) as total_order FROM "postgresqldbdatabase"."public".sales  as A
left join "azuresqldb"."dbo".customers as B
on A.customerkey = B.customerkey
left join "azuresqldb"."dbo".products_data as C
on A.productkey = C.productkey
group by 1,2
order by 3 desc
limit 5;

-- Highest Sales as per Territory
SELECT A.territorykey, sum(A.orderquantity) as total_order FROM "postgresqldbdatabase"."public".sales  as A
join "azuresqldb"."dbo".customers as B
on A.customerkey = B.customerkey
group by 1
order by 2 desc
limit 5;

-- Avg discount on most selling products
SELECT A.productkey,C.productname,sum(A.orderquantity) as total_order, avg(cast(C.discountinpercentage as int)) as discount
FROM "postgresqldbdatabase"."public".sales  as A
left join "azuresqldb"."dbo".customers as B
on A.customerkey = B.customerkey
left join "azuresqldb"."dbo".products_data as C
on A.productkey = C.productkey
group by 1,2
order by 3 desc
limit 5;

-- Avg discount on least selling products
SELECT A.productkey,C.productname,sum(A.orderquantity) as total_order, avg(cast(C.discountinpercentage as int)) as discount
FROM "postgresqldbdatabase"."public".sales  as A
left join "azuresqldb"."dbo".customers as B
on A.customerkey = B.customerkey
left join "azuresqldb"."dbo".products_data as C
on A.productkey = C.productkey
group by 1,2
order by 3 asc
limit 5;

-- Most quantity purchased by single customers and avg discount given
SELECT A.productkey,C.productname,sum(A.orderquantity) as total_order, avg(cast(C.discountinpercentage as int)) as discount,B.customername
FROM "postgresqldbdatabase"."public".sales  as A
left join "azuresqldb"."dbo".customers as B
on A.customerkey = B.customerkey
left join "azuresqldb"."dbo".products_data as C
on A.productkey = C.productkey
group by 1,2,5
order by 3 desc
limit 5;

-- Most profitable products by Revenue
SELECT C.productname,round(sum((C.productprice - (C.productprice*cast(C.discountinpercentage as int)/100)) - C.productcost),2) as Revenue,sum(A.orderquantity) as total_order
FROM "postgresqldbdatabase"."public".sales  as A
left join "azuresqldb"."dbo".customers as B
on A.customerkey = B.customerkey
left join "azuresqldb"."dbo".products_data as C
on A.productkey = C.productkey
group by 1
order by 2 desc
limit 5;
```