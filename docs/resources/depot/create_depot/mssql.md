# Steps to create MSSQL Depot

To create a MSSQL Depot you must have the following details:

## Pre-requisites specific to Depot creation

- **Tags:** A developer must possess the following tags, which can be obtained from a DataOS operator.

    ```bash
            NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
        ─────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
        Iamgroot     │   iamgroot  │ person │   iamgroot@tmdc.io   │ roles:id:data-dev,                            
                     │             │        │                      │ roles:id:user,                  
                     │             │        │                      │ users:id:iamgroot  
    ```

- **Use cases:** Alternatively, instead of assigning tags, a developer can create a Depot if an operator grants them the "Manage All Instance-level Resources of DataOS in the user layer" use case through Bifrost Governance.

    <center>
    <img src="/resources/depot/usecase2.png" alt="Bifrost Governance" style="width:60rem; border: 1px solid black; padding: 5px;" />
    <figcaption><i>Bifrost Governance</i></figcaption>
    </center>


## Pre-requisites specific to the source system

- **Host URL and Parameters**: The URL or hostname of the SQL Server where the database is hosted. This is typically provided by the database administrator. Additional connection parameters (such as encryption settings or timeout values) might be needed depending on the specific requirements of the SQL Server and the connection method.

- **Database Schema**: The schema in the Microsoft SQL Server where your tables and other database objects are located. This can be provided by the database administrator, and it helps define the structure and organization of the data within the database.

- **Port**: The port number used to connect to the SQL Server. The default port for Microsoft SQL Server is `1433`, but it might vary depending on the configuration. This information can be obtained from the database administrator.

- **Username**: The username used for authentication to the Microsoft SQL Server. This is typically provided by the database administrator or set up by the user account when created in the SQL Server.

- **Password**: The password associated with the provided username for authentication. This password is securely stored and is required for establishing the connection to the SQL Server. It can be set when the user account is created and should be securely retrieved if forgotten.

## Create a MSSQL Depot

DataOS allows you to connect to a Microsoft SQL Server database and read data from tables using Depots. A Depot provides access to all tables within the specified schema of the configured database. You can create multiple Depots to connect to different SQL servers or databases. To create a Depot of type ‘SQLSERVER‘, follow the below steps:

### **Step 1: Create an Instance Secret for securing MSSQL credentials**

Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/).

### **Step 2: Create a MSSQL Depot manifest file**

Begin by creating a manifest file to hold the configuration details for your MSSQL Depot.

**Use the below template, if the self-signed certificate is enabled.**


```yaml
name: ${{depot-name}}
version: v2alpha
type: depot
tags:
    - ${{tag1}}
    - ${{tag2}}
owner: ${{owner-name}}
layer: user
depot:
    type: ABFSS                                       
    description: ${{description}}
    external: ${{true}}
    compute: ${{runnable-default}}
    secrets:
    - name: ${{abfss-instance-secret-name}}-r
        allkeys: true

    - name: ${{abfss-instance-secret-name}}-rw
        allkeys: true
    abfss:                                             
    account: ${{account-name}}
    container: ${{container-name}}
    relativePath: ${{relative-path}}
    format: ${{format}}
```



**Use the template, if the self-signed certificate is not enabled.**


```yaml 
name: ${{mssql01}}
version: v2alpha
type: depot
tags:
    - ${{dropzone}}
    - ${{mssql}}
layer: user
depot:
    type: JDBC
    description: ${{MSSQL Sample data}}
    jdbc:
    subprotocol: ${{sqlserver}}
    host: ${{host}}
    port: ${{port}}
    database: ${{database}}
    params: # Required
        encrypt: ${{false}}
    external: ${{true}}
    hiveSync: ${{false}}
    secrets:
    - name: ${{sf-instance-secret-name}}-r
        allkeys: true

    - name: ${{sf-instance-secret-name}}-rw
        allkeys: true
```

To get the details of each attribute, please refer [to this link](/resources/depot/configurations).
   


### **Step 3: Apply the Depot manifest file**

Once you have the manifest file ready in your code editor, simply copy the path of the manifest file and apply it through the DataOS CLI by pasting the path in the placeholder, using the command given below:

=== "Command"

    ```bash 
    dataos-ctl resource apply -f ${{yamlfilepath}}
    ```
=== "Alternative Command"

    ```bash 
    dataos-ctl apply -f ${{yamlfilepath}}
    ```



## Verify the Depot creation

To ensure that your Depot has been successfully created, you can verify it in two ways:

- Check the name of the newly created Depot in the list of Depots where you are named as the owner:

    ```bash
    dataos-ctl get -t depot
    ```

- Additionally, retrieve the list of all Depots created in your organization:

    ```bash
    dataos-ctl get -t depot -a
    ```

You can also access the details of any created Depot through the DataOS GUI in the [Operations App](https://dataos.info/interfaces/operations/) and [Metis UI](https://dataos.info/interfaces/metis/).

## Delete a Depot

<aside class="callout">
🗣️ As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.
</aside>

If you need to delete a Depot, use the following command in the DataOS CLI:

=== "Command"

    ```bash 
    dataos-ctl delete -t depot -n ${{name of Depot}}
    ```
=== "Alternative Command"

    ```bash 
    dataos-ctl delete -f ${{path of your manifest file}}
    ```



By executing the above command, the specified Depot will be deleted from your DataOS environment.