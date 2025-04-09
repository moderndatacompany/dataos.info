# Steps to create MYSQL Depot

To create a MySQL Depot you must have the following details:

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

- **Host URL and Parameters**: The URL or hostname of the MySQL server where the database is hosted. This is typically provided by the database administrator. Additional parameters (such as character set or connection timeout) may be needed based on the specific configuration of the MySQL server.

- **Port**: The port number used to connect to the MySQL server. By default, MySQL uses port `3306`, but this could vary if a custom port is configured. This information should be provided by the database administrator.

- **Username**: The username used to authenticate the connection to the MySQL database. This username is typically created by the database administrator and must have the necessary privileges to access the desired database.

- **Password**: The password associated with the provided username for authentication. The password is typically set when the username is created and must be kept secure. It is required to establish a successful connection to the database.

## Create a MySQL Depot

DataOS allows you to connect to a MySQL database and read data from tables using Depots. A Depot provides access to all tables within the specified schema of the configured database. You can create multiple Depots to connect to different MySQL servers or databases. To create a Depot of type ‘MYSQL‘, follow the below steps:

### **Step 1: Create an Instance Secret for securing MySQL credentials**


Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/index#abfss).

### **Step 2: Create a MySQL Depot manifest file**

Begin by creating a manifest file to hold the configuration details for your MySQL Depot.

**Use this template, if a self-signed certificate is enabled.**


```yaml 
name: ${{mysql01}}
version: v2alpha
type: depot
tags:
    - ${{dropzone}}
    - ${{mysql}}
layer: user
depot:
    type: MYSQL
    description: ${{"MYSQL Sample Database"}}
    mysql:
    subprotocol: "mysql"
    host: ${{host}}
    port: ${{port}}
    params: # Required
        tls: ${{skip-verify}}
    external: ${{true}}
    secrets:
    - name: ${{instance-secret-name}}-r
        keys: 
        - ${{instance-secret-name}}-r

    - name: ${{instance-secret-name}}-rw
        keys: 
        - ${{instance-secret-name}}-rw
```


**Use this template, if the self-signed certificate is not enabled.**


```yaml 

name: ${{"mysql01"}}
version: v2alpha
type: Depot
tags:
    - ${{dropzone}}
    - ${{mysql}}
layer: user
Depot:
    type: MYSQL
    description: ${{"MYSQL Sample data"}}
    mysql:
    host: ${{host}}
    port: ${{port}}
    external: true
    secrets:
    - name: ${{instance-secret-name}}-r
        keys: 
        - ${{instance-secret-name}}-r

    - name: ${{instance-secret-name}}-rw
        keys: 
        - ${{instance-secret-name}}-rw

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



### **Verify the Depot creation**

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