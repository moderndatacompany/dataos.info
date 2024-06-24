# End to end use-case to back a streamlit application via Database resource

Our goal is to back a Streamlit app with Database resource. This app will provide insights on the product data contained in the database. We will start by creating an initial schema migration and set up a database resource, configure a depot for data transfer, migrate data from IceBase to Database, validate with a cluster setup, and finally, dockerize and deploy the Streamlit app using Alpha Stack. To achieve this, follow this step by step guide


For this process, we need to maintain a folder with the following structure in the IDE:

``` shell
project-directory/
├── app/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── database/
│   ├── migrations/
│   │   └── initial_schema.sql
├── flare.yaml
├── depot.yaml
├── cluster.yaml
├── service.yaml
└── container.yaml
```

<aside class="callout">

💡 If you already have a database that you want to use, feel free to <a href="https://dataos.info/resources/database/how_to_guide/back_streamlit_via_database/#create_a_database_manifest"> skip to the next step </a>.

</aside>

## Create Database schema migration

We will begin by creating a new migration that includes only the schema, without any initial data. For that, Create a folder named `migration` and in it create a `schema_migration` file.

```sql title="schema_migration.up.sql" 
--8<-- "examples/resources/database/use_case/schema_migration.up.sql"
```

## Create the Database manifest

Following the schema setup, we will create a database resource based on the schema. 

```yaml title="product_database.yaml"
--8<-- "examples/resources/database/use_case/product_database.yml"
```
=== "Command"

    ```bash
    dataos-ctl resource apply -f ${manifest-file-path} -w ${workspace-name}
    ```

=== "Example"

    ```bash
    dataos-ctl resource apply -f iamgroot/product/product_database.yaml -w curriculum
    # Expected Output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying(curriculum) productdb:v1:database...  
    INFO[0001] 🔧 applying(curriculum) productdb:v1:database...updated 
    INFO[0001] 🛠 apply...complete  
    ```

### **Check the workflow of the created Database**

=== "Command"

    ```bash
    dataos-ctl resource get -t workflow  -w ${workspace-name}
    ```

=== "Example"

    ```bash
    dataos-ctl resource get -t workflow -w curriculum
    # Expected Output
    ➜  DatabaseUseCase dataos-ctl apply -f database.yaml 
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             

                    NAME               | VERSION |   TYPE   | WORKSPACE | STATUS |  RUNTIME  |     OWNER       
    -----------------------------------|---------|----------|-----------|--------|-----------|-----------------
      productdb-2-m-database           | v1      | workflow | curriculum    | active | running   | iamgroot  
    ```

When you create a database a depot automatically gets created with the name {your_db}database. for e.g., if your database name is productdb the depot name will be like `productdbdatabase` which you can fetch using `get` command.

=== "Command"

    ```bash
    dataos-ctl resource get -t depot
    ```

=== "Example"

```bash hl_lines="9"
dataos-ctl resource get -t depot
#Expected_Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

         NAME         | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME |     OWNER       
----------------------|---------|-------|-----------|--------|---------|----------------- 
  customersdbdatabase | v1      | depot |           | active |         | iamgroot  
  productdbdatabase   | v1      | depot |           | active |         | iamgroot  
```
Don't forget to note down the database, host, port and subprotocol from this Resources as it will be needed to create a depot that can connect with our PostgreSQL Database.

The Resource YAML can be viewed on [Operations](/interfaces/operations) App by following these steps.

To access the Resource YAML, follow these steps within the Operations App:

1. Navigate to Operations: Open the Operations application interface.

2. Go to User Space: Navigate to the User Space section.

3. Search for Depot: Look for the automatically generated depot named productdbdatabase.

4. View Resource YAML: Click on "Resource YAML" to view detailed configuration and specifications of the productdbdatabase depot.

<center>
![productdbdatabase Resource YAML](/resources/database/productdb.png)
</center>
<center> <i>Spec Section of productdb Resource YAML</i> </center>

## Create a Beacon Service

Now, Create a Beacon Service to expose the PostgreSQL database on API. 

```yaml title="product_database.yaml" hl_lines="14"
--8<-- "examples/resources/database/use_case/product_service.yml"
```
Replace dataos_fqdn with the current value of your DataOS Fully Qualified Domain Name (FQDN). 

you can now access the PostgreSQL database using the exposed API by

To validate the outcome, execute a request to the designated URL as higlihted in the above manifest:

A successful response with no errors indicates that the database has been successfully initialized with no data initally.

<aside class='callout'>Service creation is an optional step used solely for verifying database creation or to check if the schema has been successfully written to the database.</aside>

## Create the Depot manifest

Next, a depot will be established to connect PostgreSQL Database with DataOS. This depot will serves as an intermediary to facilitate data movement from from icebase depot to product database depot which is backed by postgreSQL Database.

Here we need information of the following attributes:

- Database name: The name of the PostgreSQL database. Here, `productdb`
- Hostname/URL of the server: The hostname or URL of the PostgreSQL server. 
- Parameters: Additional parameters for the connection, if required.
- Username: The username for authentication, here it is `postgres`
- Password: The password for authentication, which you need to ask to your respective DevOps team.

This  information can be copied from Resource YAML, which would look like following after configuration

``` yaml
database: productdb
host: usr-db-dataos-ck-vgji-liberaldo-dev.postgres.database.azure.com
port: 5432
subprotocol: postgresql
```

```yaml title="product_database_depot.yml" 
--8<-- "examples/resources/database/use_case/product_depot.yaml"
```

Here, we will be using cluster to check whether we are able to query the database using workbench.


## Create a Flare job manifest

After succesful creation of PostgreSQL Database Depot. Now, We will migrate data from IceBase to the database via Flare stack.

```yaml
--8<-- "examples/resources/database/use_case/product_flare.yml"
```

## Create the Cluster manifest

To verify the successful movement of the data from Icebase to productdb database, we will set up a cluster. This cluster will allow us to query the data using a workbench. Successful querying will confirm that the data has been correctly migrated.

```yaml title="product_database_cluster.yaml "hl_lines="17"
--8<-- "examples/resources/database/use_case/product_cluster.yml"
```

<aside class='callout'>Cluster creation is an optional step used solely for verifying database creation or to check if the schema has been successfully written to the database.</aside>

Now, In the same directory, let's create a folder named `application` in it we will create a `requirements.txt`, `app.py`, and a `Dockerfile`.

Before moving to deploy streamlit in DataOS. You can download this zip folder to replicate the streamlit application. To download click [here](/resources/database/application.zip)   

## Add dependencies to your requirements file

In the application folder, let's create a create a `requirements.txt` file, preferably pinning its version (replace x.x.x with the version you want installed):

```text title="requirements.txt"
trino==0.316.0
pandas==1.3.5
streamlit==1.13.0
```

## Write your Streamlit app

Write the desired streamlit app `app.py` configure it with the connection details

???tip title="app.py"
 
    ```yaml
    --8<-- "examples/resources/database/001_migration.up.sql"
    ```
Configure the Streamlit App section to connect with trigo

## docker