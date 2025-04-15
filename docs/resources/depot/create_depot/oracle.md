# Steps to create Oracle Depot

To create an Oracle Depot you must have the following details:

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

- **URL of the Oracle account**: The URL or hostname of the Oracle database server where the database is hosted. This is typically provided by the database administrator and may include additional connection parameters.

- **Username**: The login username used to authenticate the connection to the Oracle database. This username is created by the database administrator and must have the appropriate permissions to access the desired database.

- **Password**: The password associated with the provided username for authentication. This is required to establish a secure connection and is typically set by the administrator or the user during account creation.

- **Database Name**: The name of the Oracle database you want to connect to. This is used to specify the target database within the Oracle server and is provided by the database administrator.

- **Database Schema**: The schema in the Oracle database where the desired tables are located. Schemas are logical containers for database objects like tables, views, and indexes, and this information helps you access the correct data.

## Create an Oracle Depot

DataOS allows you to connect to an Oracle database and access data from tables using Depots. A Depot provides access to all schemas within the specified service in the configured database. You can create multiple Depots to connect to different Oracle servers or databases. To create a Depot of type ‘ORACLE‘, follow the below steps:

### **Step 1: Create an Instance Secret for securing Oracle credentials**

Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/data_sources/oracle/).

### **Step 2: Create a Oracle Depot manifest file**

Begin by creating a manifest file to hold the configuration details for the Oracle Depot. 


```yaml 
name: ${{depot-name}}
version: v2alpha
type: depot
tags:
    - ${{dropzone}}
    - ${{oracle}}
layer: user
depot:
    type: ORACLE                                    
    description: ${{"Oracle Sample data"}}
    oracle:
    subprotocol: ${{subprotocol}} # for example "oracle:thin"                                     
    host: ${{host}}
    port: ${{port}}
    service: ${{service}}
    external: ${{true}}
    secrets:
    - name: ${{sf-instance-secret-name}}-r
        allkeys: true

    - name: ${{sf-instance-secret-name}}-rw
        allkeys: true
```

To get the details of each attribute, please refer [to this link](/resources/depot/configurations).
   

### **Step 3: Apply the Depot manifest file**

Once you have the manifest file ready in the code editor, simply copy the path of the manifest file and apply it through the DataOS CLI by pasting the path in the placeholder, using the command given below:

=== "Command"

    ```bash Command
    dataos-ctl resource apply -f ${{yamlfilepath}}
    ```

=== "Alternative Command"

    ```bash Alternative command
    dataos-ctl apply -f ${{yamlfilepath}}
    ```

## Verify the Depot creation

To ensure that the Depot has been successfully created, verify it in two ways:

- Check the name of the newly created Depot in the list of Depots created by the user:

    ```bash
    dataos-ctl get -t depot
    ```

- Additionally, retrieve the list of all Depots created in the organization:

    ```bash
    dataos-ctl get -t depot -a
    ```

Access the details of any created Depot through the DataOS GUI in the [Operations App](https://dataos.info/interfaces/operations/) and [Metis UI](https://dataos.info/interfaces/metis/).

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
    dataos-ctl delete -f ${{path of the manifest file}}
    ```

By executing the above command, the specified Depot will be deleted from the DataOS environment.