# End to end use-case to query the data on workbench


## Create Database migration

```sql title="001_migration.up.sql" 
--8<-- "examples/resources/database/001_migration.up.sql"
```

```sql title="002_migration.up.sql"
--8<-- "examples/resources/database/002_insertion.up.sql"
```

## Create the Database manifest

```yaml title="database.yaml"
--8<-- "examples/resources/database/database.yaml"
```

## Create the Service manifest

Always update the `PGRST_OPENAPI_SERVER_PROXY_URI` with the latest dataos context.

```yaml title="service.yaml "hl_lines="14"
--8<-- "examples/resources/database/service.yaml"
```

## Create a Depot on the hosted Database Service

Once you have the Database Service up and running, the next step involves creating a Depot on the Postgres Database associated with that Service. This necessitates the formulation of a Postgres Depot Manifest. Detailed configuration specifications are available on the [PostgreSQL Depot config templates](/resources/depot/depot_config_templates/postgresql). In this specific context, certain attributes demand precise configuration, as outlined below:

In this specific context, certain attributes demand precise configuration, as outlined below:

  - Database name: The name of your PostgreSQL database.
  - Hostname/URL of the server: The hostname or URL of the PostgreSQL server.
  - Parameters: Additional parameters for the connection, if required.
  - Username: The username for authentication.
  - Password: The password for authentication.

The resulting manifest file after configuration for this specific context will appear as follows:

```yaml title="depot.yaml" "hl_lines="12-19"
--8<-- "examples/resources/database/depot.yaml"
```

### **Apply Depot manifest**

Once you have created a Depot manifest, simply copy the  or relative path of the manifest file and apply it through the DataOS CLI, using the command given below:

=== "Command"

      ``` yaml 
      dataos-ctl apply -f ${manifest file path} -w ${workspace-name}
      ```

=== "Example"

      ```yaml
      dataos-ctl apply -f depot.yaml -w curriculum
      ```

### **Verify Depot Creation**


=== "Command"

      ``` yaml
      dataos-ctl resources get -t depot  -w ${workspace-name}
      ```

=== "Example"

      ```yaml
      dataos-ctl apply -t depot 
      ```
      #Expected Output
      ```shell
      NAME         | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME |     OWNER       
    ----------------------|---------|-------|-----------|--------|---------|-----------------
      customersdb0curriculum  | v1      | depot |           | active |         | iamgroot
      customersdbdatabase | v1      | depot |           | active |         | iamgroot  
      databasetestdepot   | v1      | depot |           | active |         | iamgroot  
      ```

## Target a cluster 

Add Depot to Cluster Sources to enable the Minerva/Themis Query Engine to access database, you can create the Postgres [Depot](/resources/depot). This allows you to query the data and create dashboards using the DataOS Workbench and Atlas

Create a new Cluster manifest with specified depot address. Below is a sample Cluster manifest provided for reference.

```yaml title="cluster.yaml" hl_lines="16-18"
--8<-- "examples/resources/database/database_cluster.yaml"
```

### **Apply the Cluster manifest**

=== "Command"

    ```bash
    dataos-ctl resource apply -f ${cluster file name} 
    ```

=== "Example"

    ```bash
    dataos-ctl resource apply -f cluster.yaml 
    ```

### **Verify the creation**

=== "Command"

    ```bash
    dataos-ctl resource get -t cluster 
    ```

=== "Example"

    ```bash
    dataos-ctl resource get -t cluster
    ```
    #Expected Output
    ```shell
    NAME         | VERSION |  TYPE   | WORKSPACE | STATUS |   RUNTIME   |     OWNER       
    ----------------------|---------|---------|-----------|--------|-------------|-----------------
    databasetestcluster | v1      | cluster | public    | active | running:1 | iamgroot
    ```
    
## Use Bundle Resource

Alternatively, you can use [Bundle](resources/bundle) Resource to execute all Resources in one manifest file only.

The sample Bundle manifest is given below:

```yaml title="bundle.yaml"
--8<-- "examples/resources/database/bundle.yaml"
```

## Query from Workbench

To verify the successful execution of the query, navigate to the Workbench, then select the cluster, depot collections and dataset associated with the created database customersdb.

- **Catalog, Schema, and Table Selection**: The user must select the appropriate catalog, schema, and tables within the Workbench interface which here is `databasetestdepot` ,`public` and `customers` respectively .
- **Query Execution**: After formulating the query, the user executes it by clicking the 'Run' button.
- **Result Retrieval**: The outcomes of the executed query are displayed in the pane situated below the query input area.

<center> ![ Query Workbench](/resources/database/query_workbench.png) </center>

<center> Quering the customers database through Workbench</center>


For comprehensive details on the features and capabilities of Workbench, refer to the dedicated [Workbench](/interfaces/workbench) documentation.




