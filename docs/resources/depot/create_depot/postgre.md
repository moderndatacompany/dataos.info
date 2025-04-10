# Steps to create Postgres Depot

To create a Postgres Depot you must have the following details:

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

- **Database name**: The name of the specific PostgreSQL database you want to connect to. This can be provided by the database administrator or found in the database management system where the database was created.

- **Hostname/URL of the server**: The hostname or URL of the server where the PostgreSQL database is hosted. This is typically an IP address or a fully qualified domain name (FQDN). You can obtain this from your database administrator or the team managing the PostgreSQL server.

- **Parameters**: Additional optional parameters are required for the connection, such as SSL settings or timeout configurations. These can be provided by the database administrator or found in your PostgreSQL server's documentation, depending on the connection requirements.

- **Username**: The username used for authentication to access the PostgreSQL database. This is created when the user account is set up and can be provided by the database administrator.

- **Password**: The password associated with the PostgreSQL username for authentication. This is set during user account creation and must be securely obtained from the database administrator if forgotten.

## Create a Postgres Depot

DataOS allows you to connect to a PostgreSQL database and read data from tables using Depots. A Depot provides access to all schemas visible to the specified user in the configured database. To create a Depot of type ‘POSTGRESQL‘, follow the below steps:

### **Step 1: Create an Instance Secret for securing Postgres credentials**

Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/data_sources/postgres/).

### **Step 2: Create a Postgres Depot manifest file**

Begin by creating a manifest file to hold the configuration details for your Postgres Depot. 

<aside class="callout">
🗣️ Use the below templates, if the self-signed certificate is enabled.
</aside>


```yaml 
name: ${{postgresdb}}
version: v2alpha
type: depot
layer: user
depot:
    type: JDBC                  
    description: ${{To write data to postgresql database}}
    external: ${{true}}
    secrets:
    - name: ${{sf-instance-secret-name}}-r
        allkeys: true

    - name: ${{sf-instance-secret-name}}-rw
        allkeys: true
    postgresql:                        
    subprotocol: "postgresql"
    host: ${{host}}
    port: ${{port}}
    database: ${{postgres}}
    params: #Required 
        sslmode: ${{disable}}
```


<aside class="callout">
🗣️ Use the below templates, if the self-signed certificate is not enabled.
</aside>


```yaml 
name: ${{depot-name}}
version: v2alpha
type: Depot
tags:
    - ${{tag1}}
owner: ${{owner-name}}
layer: user
Depot:
    type: POSTGRESQL
    description: ${{description}}
    external: true
    secrets:
    - name: ${{instance-secret-name}}-r
        allkeys: true

    - name: ${{instance-secret-name}}-rw
        allkeys: true
    postgresql:                                          
    host: ${{host}}
    port: ${{port}}
    database: ${{database-name}}
    params: # Optional
        ${{"key1": "value1"}}
        ${{"key2": "value2"}}
```


To get the details of each attribute, please refer [to this link](/resources/depot/configurations).
   

### Step 3: Apply the Depot manifest file

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