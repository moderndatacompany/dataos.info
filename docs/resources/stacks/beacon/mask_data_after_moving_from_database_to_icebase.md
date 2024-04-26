# Mask Data After Moving from Database to Icebase

This article explains the steps to access Sales transaction data in PostgreSQL, a relational database in the DataOS storage. We need to create a Beacon service that enables you to access this database through PostgreSQL REST API. We can also enforce DataOS governance policies for the secure access of the data in PostgreSQL.

## Connect with Sample Data

In this tutorial, you learn how to create a database in PostgreSQL and through a Beacon service,  update it  and ingest the sample data in it:

1. Create SQL files
2. Create Database Resource in DataOS
3. Create Beacon Service 
4. Sample Sales Data Ingestion

### **Create SQL Files**

This is to create a table in the PostgreSQL database:

1. Create a migration folder.

2. Create Up and Down SQL files.

a. In up.sql, write the code to create tables, alter tables, and create functions & triggers.

b. In down.sql, we drop, truncate, delete tables, functions & triggers.

3. Test your SQL commands on local Postgre instance. <0001_initial.up.sql> in this case.

> **Note**: Naming of SQL files must be <anything>.up.sql &  <anything>.down.sql format, name them in sequence when you have to run more than one up or down file for same database for the update.
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

### **Create Database Resource in DataOS**

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

### **Create Beacon Service YAML**

This service will allow you to access the database to perform CRUD operations. While defining a service, you have to provide inputs for the properties such as **Replicas & ingress** to ****configure the incoming port for the service to allow access to DataOS resources from external links, destination URL and path, etc.

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
    PGRST_OPENAPI_SERVER_PROXY_URI: https://<dataos-context>/salesdata/api/v1
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

### **Sample Sales Data Ingestion**

You need to create a workflow to ingest sales data given in JSON format to the Postgres database.

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
dataos-ctl apply -f /home/arike/Desktop/Everything_Folder/Beacon/ingestion.yaml 
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

## Register Metadata

Run the following Scanner YAML to register the metadata for your data source with Metis. It will capture schema details such as table names, constraints, primary keys, etc., for this external data source. This will allow you to run queries on the data in DataOS.

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

## Create Access and Mask Policy

We are creating access and mask policies in this use case. To apply these policies, you have to revoke default access for the dataset and then allow users having a specific tag to access data and mask the sensitive data.

> **Note:** You need ‘Operator’ level permissions to create policy.
> 
- Open the source code editor and create the following YAML files. 

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

- Use the `apply` command to create the Depot resource in DataOS.