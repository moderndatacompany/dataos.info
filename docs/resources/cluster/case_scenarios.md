# Case Scenarios

## Multi-Cluster Setup

In scenarios where a single cluster is insufficient to handle the query load or specific performance issues arise, multiple Minerva clusters can be created. The following example demonstrates a typical configuration for a multi-cluster setup:

<details><summary>Sample YAML Configuration</summary>

```yaml
- version: v1                           # Cluster 1
  name: minervab
  type: cluster
  description: the default minerva cluster b
  tags:
    - cluster
    - minerva
  cluster:
    nodeSelector:
      "dataos.io/purpose": "query"
    toleration: query
    runAsApiKey: api-key
    minerva:
      replicas: 2
      resources:
        limits:
          cpu: 2000m
          memory: 4Gi
        requests:
          cpu: 2000m
          memory: 4Gi
      debug:
        logLevel: INFO
        trinoLogLevel: ERROR
      depots:
        - address: dataos://icebase:default
          properties:
            iceberg.file-format: PARQUET
            iceberg.compression-codec: GZIP
            hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
            hive.parquet.use-column-names: "true"
        - address: dataos://filebase:default
          properties:
            hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
            hive.parquet.use-column-names: "true"
        - address: dataos://kafka:default
          properties:
            kafka.empty-field-strategy: "ADD_DUMMY"
            kafka.table-description-supplier: "confluent"
            kafka.default-schema: "default"
            kafka.confluent-subjects-cache-refresh-interval: "5s"
            kafka.confluent-schema-registry-url: "http://schema-registry.caretaker.svc.cluster.local:8081"
      catalogs:               
        - name: redshift
          type: redshift
          properties:
            connection-url: "jdbc:redshift://URL:PORT/DB"
            connection-user: "USERNAME"
            connection-password: "PASSWORD"
        - name: oracle
           type: oracle
           properties:
             connection-url: "jdbc:oracle:thin:@URL:PORT/DB"
             connection-user: "USERNAME"
             connection-password: "PASSWORD"
        - name: cache
          type: memory
          properties:
            memory.max-data-per-node: "128MB"

- version: v1
  name: minervabc                          # Cluster 2
  type: cluster
  description: the default minerva cluster c
  tags:
    - cluster
    - minerva
  cluster:
    nodeSelector:
      "dataos.io/purpose": "query"
    toleration: query
    runAsApiKey: api-key
    minerva:
      replicas: 2
      resources:
        limits:
          cpu: 2000m
          memory: 4Gi
        requests:
          cpu: 2000m
          memory: 4Gi
      debug:
        logLevel: INFO
        trinoLogLevel: ERROR
      depots:
        - address: dataos://icebase:default
          properties:
            iceberg.file-format: PARQUET
            iceberg.compression-codec: GZIP
            hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
            hive.parquet.use-column-names: "true"
        - address: dataos://filebase:default
          properties:
            hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
            hive.parquet.use-column-names: "true"
      catalogs:               
        - name: redshift
          type: redshift
          properties:
            connection-url: "jdbc:redshift://URL:PORT/DB"
            connection-user: "USERNAME"
            connection-password: "PASSWORD"
        - name: oracle
          type: oracle
          properties:
            connection-url: "jdbc:oracle:thin:@URL:PORT/DB"
            connection-user: "USERNAME"
            connection-password: "PASSWORD"
        - name: cache
          type: memory
          properties:
            memory.max-data-per-node: "128MB"
```
</details>

This case scenario focuses on configuring different depots to run heterogeneous queries with complex joins across different data sources, setting up a Minerva cluster to access these data sources, and configuring policies to protect sensitive information during Minerva queries. Here, customer and sales transaction data are fetched from different data sources, such as an Azure MS-SQL database and a PostgreSQL database. A Minerva Cluster is created to run analytical queries with joins, and the queries are written using DataOS Workbench.

## Implementation Flow

The following steps were taken to solve the use case:

- Preparing the data sources with sample data
- Creating Depots to access data from the data sources
- Creating a Minerva Cluster
- Running queries on Workbench targeting the created cluster
- Showing the query output resulting from performing joins on data from different sources

### **Prepare the Data Sources**

To prepare for the use case, customer data was stored in a Microsoft Azure SQL database, and sales data was stored in a PostgreSQL database. 

#### **Azure SQL Database**

This article explains the steps to access data from Azure SQL Database, which is a relational database-as-a-service (DBaaS) in the Microsoft Cloud (Azure), and register metadata with DataOS Metis.

**Connect with Sample Data**

In this tutorial, you learn how to use the Azure portal and connect with the sample data in it:

1. Log in to the [Azure portal](https://portal.azure.com/).
2. Set up a server-level IP firewall rule using the Azure portal.
3. Connect to the sample database. 
4. Access sample table with customer data.
5. Show the customer data.
6. Copy the connection string for the database. You will need a connection string to create a depot resource in DataOS to access this data.

The following steps are performed:

1. On **Microsoft Home**, click on **SQL databases**. 

![azur home.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e29342d3-4673-4eb3-9e16-c4e74d9ccad8/azur_home.png)

1. Select on the sample database.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7ee274d2-7631-4c2c-8838-0a876cf7df71/Untitled.png)

1. Click on **Set server firewall**.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e14c5fad-62f9-4fb0-a133-d6eb7d12920b/Untitled.png)

1. This will give you **start and endpoints** of access for you server.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3a773345-c7b0-4e21-8c48-742590b49b21/Untitled.png)

1. Login to the **Query Editor**.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b6f3479a-2c66-4deb-a707-29c55d6db636/Untitled.png)

1. You can see the sample tables available. In this use case, we have used Customers and Products_data tables.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e50c6c48-51e5-403a-9a2e-e84cfe817b45/Untitled.png)

1. Click on the **Connection** String. Copy the **JDBC** details for authentication.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/95dbd4a7-8a0a-4697-bcf0-4bd50f3b8be4/Untitled.png)

# Register the Metadata

Run the following Scanner YAML to register the metadata for your data source with Metis. It will capture schema details such as table names, constraints, primary keys, etc., for this external data source. This will allow you to run queries on the data.

```yaml
version: v1beta1
name: scanner-azure-sql-db    # Name of workflow 
type: workflow                # Type of YAML
tags:                        
  - scanner
  - azure-sql-db
description: Scans metadata of Azure SQL Database tables for dbo schema and registers them as datasets on Datanet  
workflow: 
  dag:
    - name: azure-sql-db-scanner     # Name of the job shown on Runnables(Dag)
      description: The job scans metadata of Azure SQL Database tables for dbo schema and registers them as datasets  
      spec:
        tags:                   
          - azure-sql-db
        stack: scanner               # Name of stack that will process the data
        scanner:
          depot: dataos://azuresqldb:dbo
```

This article explains the steps to access Sales transaction data in PostgreSQL, a relational database in the DataOS storage. We need to create a Beacon service that enables you to access this database through PostgreSQL REST API. We can also enforce DataOS governance policies for the secure access of the data in PostgreSQL.

# Connect with Sample Data

In this tutorial, you learn how to create a database in PostgreSQL and through a Beacon service,  update it  and ingest the sample data in it:

1. Create SQL files
2. Create Database Resource in DataOS
3. Create Beacon Service 
4. Sample Sales Data Ingestion

## Create SQL Files

This is to create a table in the PostgreSQL database:

1. Create a migration folder.

2. Create Up and Down SQL files.

a. In up.sql, write the code to create tables, alter tables, and create functions & triggers.

b. In down.sql, we drop, truncate, delete tables, functions & triggers.

3. Test your SQL commands on local Postgre instance. <0001_initial.up.sql> in this case.

> 📌 **Note**: Naming of SQL files must be <anything>.up.sql &  <anything>.down.sql format, name them in sequence when you have to run more than one up or down file for same database for the update.
> 
> 
> Name every column type according to PostgreSQL data type.
> 

```sql
CREATE TABLE IF NOT EXISTS sales_transactions
(
ProductKey  int, 
CustomerKey  int,
TerritoryKey  int, 
OrderLineItem  int, 
OrderQuantity  int,
Foreign key (PorductKey,CustomerKey)
 );
```

## **Create Database Resource in DataOS**

This is to create a database in PostgreSQL:

1. Open the source code editor and create a `database.yaml` file providing the database name and the full path of the migration folder containing SQL files.

```yaml
version: v1beta1
name: postgresqldbdatabase        # database name               
type: database
description: Sample sales database created 
tags:
  - sales
database:
  migrate:
    includes:
      - ./Migration      # all up & down sql files.
    command: up          # in case of drop table, write down.
```

2. After creating database YAML, run *apply* command on DataOS CLI to create database resource in DataOS.

```bash
dataos-ctl apply -f database.yaml
```

## **Create Beacon Service YAML**

This service will allow you to access the database to perform CRUD operations. While defining a service, you have to provide inputs for the properties such as **Replicas & ingress** to ****configure the incoming port for the service to allow access to DataOS resources from external links, destination URL and path, etc.

To learn more about creating Beacon service, click here.

[Creating a Beacon Service](https://www.notion.so/Beacon-d235f61b5eaf419fba60fbcfe2364d62?pvs=21)

1. Open the source code editor and create the following YAML file.

```yaml
version: v1beta1
name: salesdata    # service name
type: service
tags:
  - service
service:
  replicas: 2
  ingress:
    enabled: true
    stripPath: true
    path: /salesdata/api/v1   # how your URL going to appear.
    noAuthentication: true
  stack: beacon+rest
  envs:
    PGRST_OPENAPI_SERVER_PROXY_URI: https://flowing-husky.dataos.app/salesdata/api/v1
                                    # environment URL + path: /citybase/api/v1
  beacon:
    source:
      type: database
      name: postgresqldbdatabase
      workspace: public
  topology:
  - name: database
    type: input
    doc: Sales database connection
  - name: rest-api
    type: output
    doc: serves the database (containing sales data) as a RESTful API
    dependencies:
    - database
```

2. Run the `apply` command on DataOS CLI to create the **service** resource for the database.

3. We can check the API through any browser or with **Postman**.

## Sample Sales Data Ingestion

You need to create a workflow to ingest sales data given in JSON format to the Postgres database.

To learn more, click here.

[Creating Flare Workflow](https://www.notion.so/Create-your-first-Flare-Workflow-796bafba119c4322a4426889638a093d?pvs=21)

1. Open source code editor and create the following `dataingestion.yaml` file providing the source for reading from and destination for writing data. 
2. Run the `dataingestion.yaml` to ingest sample data to Postgres.

```yaml
version: v1beta1
name: sales-transactions
type: workflow 
tags:
- Connect
- sales_data 
description: The job ingests sales transactions  data in JSON format into raw zone
workflow:
  title: sales_transactions_data
  dag:
    - name: sales
      title: connect sales transactions data
      spec: 
        tags:
            - Connect_jobs
            - transactions_connect
        stack: flare:3.0
        envs:
          HERA_URL: "https://enough-kingfish.dataos.app/hera/api"
          DEPOT_SERVICE_URL: "https://enough-kingfish.dataos.app/ds/api/v2"
        flare:
          driver:
              coreLimit: 2000m
              cores: 2
              memory: 2500m
          executor:
              coreLimit: 1500m    
              cores: 2
              instances: 1
              memory: 2000m
          job:
            explain: true
            inputs:                     # JSON file
              - name: sales_tranactions
                dataset: dataos://thirdparty01:retail/Transactions_data?acl=rw  
                format: JSON
            logLevel: ERROR
            outputs:                    # PostgreSQl Database
              - name: output01
                depot: dataos://postgresqldbdatabase:public?acl=rw     
                driver: org.postgresql.Driver
            steps:
                 - sink:
                    - sequenceName: sales_transactions
                      datasetName: sales
                      outputName: output01
                      outputType: JDBC
                      description: This dataset gives you details of all sports sales transactions table  and their corresponding attributes.
                      tags:
                        - sales transactions table data
                        - sportsdatasets
                      outputOptions:
                        saveMode: overwrite
                   sequence: 
                    - name: sales_transactions_0
                      sql: select * from  sales_tranactions
                      functions :
                         - name: any_date
                           column: OrderDate
                           asColumn: Order_Date
                         - name: any_date
                           column: StockDate
                           asColumn : StockDate
                         - name : drop 
                           columns: 
                               - OrderDate
                         - name : set_type 
                           columns: 
                              ProductKey : int 
                              CustomerKey : int
                              TerritoryKey : int 
                              OrderLineItem : int 
                              OrderQuantity : int 
                    - name: sales_transactions 
                      sql: >
                            select *,
														row_number() over (order by OrderNumber) as primary_key
                            from sales_transactions_0
```

2. Run the `apply` command on DataOS CLI.

```bash
~$ dataos-ctl apply -f /home/arike/Desktop/Everything_Folder/Beacon/ingestion.yaml 
INFO[0000] 🛠 apply...                                   
INFO[0001] 🔧 applying(public) sales-transactions:v1beta1:workflow... 
🚨 v1beta1 has been replaced by versions v1 for type workflow 🚨
please update as v1beta1 will be deprecated in the next release, and auto-migrate will be disabled
INFO[0007] 🔧 applying(public) sales-transactions:v1:workflow...created 
INFO[0007] 🛠 apply...complete                           
arike@arike-ThinkPad-E15-Gen-2:~$ dataos-ctl -t workflow -w public get 
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

         NAME        | VERSION |   TYPE   | WORKSPACE | STATUS  | RUNTIME |   OWNER     
---------------------|---------|----------|-----------|---------|---------|-------------
  sales-transactions | v1      | workflow | public    | pending |         | arikerawat  

arike@arike-ThinkPad-E15-Gen-2:~$ dataos-ctl -t workflow -w public -n sales-transactions get runtime -r
INFO[0000] 🔍 workflow...                                
INFO[0001] 🔍 workflow...complete                        

         NAME        | VERSION |   TYPE   | WORKSPACE |          TITLE          |   OWNER     
---------------------|---------|----------|-----------|-------------------------|-------------
  sales-transactions | v1      | workflow | public    | sales_transactions_data | arikerawat  

  JOB NAME |   STACK    |           JOB TITLE            | JOB DEPENDENCIES  
-----------|------------|--------------------------------|-------------------
  sales    | flare:2.0  | connect sales transactions     |                   
           |            | data                           |                   
  system   | dataos_cli | System Runnable Steps          |                   

  RUNTIME | PROGRESS |          STARTED          | FINISHED  
----------|----------|---------------------------|-----------
  running | 2/3      | 2022-09-06T12:59:44+05:30 |           

            NODE NAME            | JOB NAME |              POD NAME              | DATA PLANE |     TYPE     |       CONTAINERS        |   PHASE    
---------------------------------|----------|------------------------------------|------------|--------------|-------------------------|------------
  sales-execute                  | sales    | sales-transactions-n0q5-3146761932 | hub        | pod-workflow | main                    | running    
  sales-n0q5-0906072944-driver   | sales    | sales-n0q5-0906072944-driver       | hub        | pod-flare    | spark-kubernetes-driver | running    
  sales-start-rnnbl              | sales    | sales-transactions-n0q5-1166669586 | hub        | pod-workflow | wait,main               | succeeded  
  sales-transactions-start-rnnbl | system   | sales-transactions-n0q5-2168764226 | hub        | pod-workflow | wait,main               | succeeded
```

# Register Metadata

Run the following Scanner YAML to register the metadata for your data source with Metis. It will capture schema details such as table names, constraints, primary keys, etc., for this external data source. This will allow you to run queries on the data in DataOS.

To learn more, click here.

[Scanner](https://www.notion.so/2768a3159d80488ea76b2864cf061152?pvs=21)

1. Open the source code editor and create the following YAML file.

```yaml
version: v1beta1
name: scanner-postgres-db    # Name of workflow 
type: workflow                # Type of YAML
tags:                        
  - scanner
  - postgres-db  
description: Scans metadata of postgres database tables and registers them as datasets on Datanet  
workflow: 
  dag:
    - name: postgres-db-scanner     # Name of the job shown on Runnables(Dag)
      description: The job scans metadata of postgres database tables and registers them as datasets  
      spec:
        tags:                     
          - postgres-database
        stack: scanner               # Name of stack that will process the data
        scanner:
          depot: dataos://postgresqldbdatabase:public
```

1. Use the `apply` command to create the resource in DataOS.

# Create Access and Mask Policy

We are creating access and mask policies in this use case. To apply these policies, you have to revoke default access for the dataset and then allow users having a specific tag to access data and mask the sensitive data.

To learn more, click here.

[Policy Implementation](https://www.notion.so/Policy-4336fd8b49a64671bd60b617ff14a638?pvs=21)

> **Note:** You need ‘Operator’ level permissions to create policy.
> 
1. Open the source code editor and create the following YAML files. 

**Access Policy**

```yaml
name: access-for-postgresqldb
version: v1
type: policy
description: Policy to access data from depot postgresqldbdatabase:public for user tag postgresqldb:user
layer: user
policy:
  access:
    subjects:
      tags:
        - dataos:u:postgresqldb:user
    predicates:
      - read
      - write
      - update
      - delete
      - create
    objects:
      paths:
        - dataos://postgresqldbdatabase:public/*
    allow: true
```

**Mask Policy**

```yaml
name: mask-columns
version: v1
type: policy
layer: user
description: "data policy to hash pii columns by name"
owner:
policy:
  data:
    type: mask
    priority: 99
    depot: azuresqldb
    collection: dbo
    dataset: customers
    selector:
      user:
        match: any
        tags:
          - "dataos:u:user"
      column:
        names:
          - "birthdate"
          - "emailaddress"
    mask:
      operator: hash
      hash:
        algo: sha256
```

1. Use the `apply` command to create the Depot resource in DataOS.

### **Create Depots**

Depots were created to access the sample data stored in the Microsoft Azure SQL database and the PostgreSQL database. 

- The Azure SQL Database Depot was created using the following YAML configuration:

    ```yaml
    version: v1
    name: "azuresqldb"
    type: depot
    tags:
    - mssql
    layer: user
    depot:
    type: JDBC
    description: "Azure SQL DB containing Customer and Product data"
    spec:
        subprotocol: "sqlserver"
        host: "weekly-expense.database.windows.net"
        port: 1433
        database: weekly-expense-database
    external: true
    connectionSecret:
        - acl: rw
        type: key-value-properties
        data:
            username: #####
            password: #######
    ```

- Similarly, a depot was created to access the sales data in the PostgreSQL database.

## Create Minerva Cluster

A Minerva Cluster was created to facilitate the execution of queries. The cluster was appropriately sized to meet the performance requirements of analytical workloads. The following steps were followed:

## Run Analytical Queries from Heterogeneous Data Sources

Queries were written and executed on the Minerva Cluster to perform analytical tasks involving data from different sources. For example, a query was executed to retrieve the highest valuable customers based on order quantity. The join operation was performed on data from the PostgreSQL sales data and the Azure SQL customer data.

Additional query examples for scenarios such as highest selling products, highest sales by territory, average discount on most selling products, average discount on least selling products, and most quantity purchased by single customers with average discount are given at the end.

These queries leverage the capabilities of Minerva to perform complex joins and aggregations on heterogeneous data sources, enabling organizations to derive valuable insights from their data.

<aside>

<b>Note:</b> The complete queries and their respective outputs are available in the original article.

</aside>

## More Scenarios

Once you have set up the database access and cluster, you can perform various analyses on the data to gain more insights. Here are some additional example scenarios and their corresponding queries:

**Highest Selling Products by Quantity**

```sql
SELECT A.productkey, C.productname, SUM(A.orderquantity) AS total_order
FROM "postgresqldbdatabase"."public".sales AS A
LEFT JOIN "azuresqldb"."dbo".customers AS B ON A.customerkey = B.customerkey
LEFT JOIN "azuresqldb"."dbo".products_data AS C ON A.productkey = C.productkey
GROUP BY 1, 2
ORDER BY 3 DESC
LIMIT 5;
```

**Highest Sales by Territory**

```sql
SELECT A.territorykey, SUM(A.orderquantity) AS total_order
FROM "postgresqldbdatabase"."public".sales AS A
JOIN "azuresqldb"."dbo".customers AS B ON A.customerkey = B.customerkey
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;
```

**Average Discount on Most Selling Products**

```sql
SELECT A.productkey, C.productname, SUM(A.orderquantity) AS total_order, AVG(CAST(C.discountinpercentage AS INT)) AS discount
FROM "postgresqldbdatabase"."public".sales AS A
LEFT JOIN "azuresqldb"."dbo".customers AS B ON A.customerkey = B.customerkey
LEFT JOIN "azuresqldb"."dbo".products_data AS C ON A.productkey = C.productkey
GROUP BY 1, 2
ORDER BY 3 DESC
LIMIT 5;
```

**Average Discount on Least Selling Products**

```sql
SELECT A.productkey, C.productname, SUM(A.orderquantity) AS total_order, AVG(CAST(C.discountinpercentage AS INT)) AS discount
FROM "postgresqldbdatabase"."public".sales AS A
LEFT JOIN "azuresqldb"."dbo".customers AS B ON A.customerkey = B.customerkey
LEFT JOIN "azuresqldb"."dbo".products_data AS C ON A.productkey = C.productkey
GROUP BY 1, 2
ORDER BY 3 ASC
LIMIT 5;
```

**Most Quantity Purchased by Single Customers and Average Discount Given**

```sql
SELECT A.productkey, C.productname, SUM(A.orderquantity) AS total_order, AVG(CAST(C.discountinpercentage AS INT)) AS discount, B.customername
FROM "postgresqldbdatabase"."public".sales AS A
LEFT JOIN "azuresqldb"."dbo".customers AS B ON A.customerkey = B.customerkey
LEFT JOIN "azuresqldb"."dbo".products_data AS C ON A.productkey = C.productkey
GROUP BY 1, 2, 5
ORDER BY 3 DESC
LIMIT 5;
```

**Most Profitable Products by Revenue**

```sql
SELECT C.productname, ROUND(SUM((C.productprice - (C.productprice * CAST(C.discountinpercentage AS INT) / 100)) - C.productcost), 2) AS revenue, SUM(A.orderquantity) AS total_order
FROM "postgresqldbdatabase"."public".sales AS A
LEFT JOIN "azuresqldb"."dbo".customers AS B ON A.customerkey = B.customerkey
LEFT JOIN "azuresqldb"."dbo".products_data AS C ON A.productkey = C.productkey
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;
```

These queries demonstrate the ability to perform advanced analytics on data from heterogeneous sources using Minerva Cluster. Organizations can derive valuable insights, such as identifying top-selling products, analyzing sales performance by territory, evaluating average discounts, and more.

By leveraging the power of Minerva and its capabilities to query diverse data sources, organizations can make data-driven decisions and unlock the full potential of their data assets.

