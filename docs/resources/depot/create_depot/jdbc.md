# Steps to create JDBC Depot

To create a JDBC Depot you must have the following details:

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

- **Database Name**: The name of the database you want to connect to. This can be provided by the database administrator or found in the database management interface, where your desired database is listed.

- **Subprotocol Name**: The subprotocol specifies the type of database you are connecting to, such as `mysql`, `postgresql`, etc. This should match the JDBC driver you're using to establish the connection, and can typically be found in the documentation of the specific database or JDBC driver.

- **Hostname/URL of the Server**: The hostname or URL of the server where the database is hosted. This is typically provided by the database administrator or hosting service, and points to the location of your database.

- **Port**: The port number through which the database connection is made (e.g., `3306` for MySQL, `5432` for PostgreSQL). This information can also be obtained from the database administrator or found in the configuration of the database server.

- **Parameters**: Any additional connection parameters needed for the JDBC connection, such as SSL settings, timeouts, or specific options for the database connection. These can be found in the JDBC driver documentation or obtained from the database administrator if custom configurations are required.

- **Username**: The username used to authenticate the JDBC connection. This can be provided by the database administrator or set when the user account is created in the database management system.

- **Password**: The password associated with the provided username. This is typically set when the user account is created and must be securely stored or retrieved from a safe location if forgotten.

## Create a JDBC Depot

DataOS provides the capability to establish a connection to a database using the JDBC driver in order to read data from tables using a Depot. The Depot facilitates access to all schemas visible to the specified user within the configured database. To create a Depot of type ‘JDBC‘, follow the below steps:

### **Step 1: Create an Instance Secret for securing JDBC credentials**


Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/).

### **Step 2: Create a JDBC Depot manifest file**

Begin by creating a manifest file to hold the configuration details for your JDBC Depot.


```yaml 
name: ${{depot-name}}
version: v2alpha
type: depot
tags:
    - ${{tag1}}
owner: ${{owner-name}}
layer: user
depot:
    type: JDBC                                      
    description: ${{description}}
    external: ${{true}}
    secrets:
    - name: ${{sf-instance-secret-name}}-r
        allkeys: true

    - name: ${{sf-instance-secret-name}}-rw
        allkeys: true
    jdbc:                                           
    subprotocol: ${{subprotocol}}
    host: ${{host}}
    port: ${{port}}
    database: ${{database-name}}
    params:
        ${{"key1": "value1"}}
        ${{"key2": "value2"}}
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

### **Delete a Depot**

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