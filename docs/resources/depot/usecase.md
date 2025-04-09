# Integrating Customer Data to a Data Product in DataOS

This section involves a real-world scenario where a Depot is utilized for developing a Data Product.

## Scenario

A financial services company aims to leverage its customer data for credit card cross-selling. The company has a customer overview dataset stored in its finance service system (MSSQL), and it needs to integrate this data into the `FS Accelerator` Data Product within the DataOS ecosystem. A Data Product developer is responsible for setting up the data connection.

## Steps for Integration

### **1. Create an Instance Secret**

To create a Depot for data connection, first create an Instance Secret Resource to securely store the credentials of MSSQL.

<aside class="callout">
🗣️ Here, it is assumed that you are already familiar with the creation of an Instance Secret.
</aside>

=== "Read-only instance-secret"

    ```yaml
    name: mssqldepot-r 
    version: v1 # Manifest version
    type: instance-secret # Type of the Resource
    description: an instance secret for mssql # Purpose of the Instance-secret
    layer: user # DataOS layer
    instance-secret:
    type: key-value-properties # Secret type
    acl: r # Access control: 'r' for read-only
    data:
        username: db-user 
        password: 45678 

    ```
=== "Read-write instance secret"

    ```yaml 
    name: mssqldepot-rw 
    version: v1 # Manifest version
    type: instance-secret # Type of the Resource
    description: an instance secret for mssql # Purpose of the Instance-secret
    layer: user # DataOS layer
    instance-secret:
    type: key-value-properties # Secret type
    acl: rw # Access control: 'rw' for read-write
    data:
        username: db-user 
        password: 45678 
    ```


### **2. Create a Depot manifest file**



After creating an Instance Secret, next step is to create a manifest file for Depot.

```yaml 
name: mssqldepot
version: v2alpha
type: depot
tags:
- mssql
layer: user
depot:
type: JDBC
description: MSSQL data
jdbc:
    subprotocol: sqlserver
    host: ${{host}}
    port: ${{port}}
    database: ${{database}}
    params: # Required
    encrypt: false
external: true
hiveSync: false
secrets:
    - name: mssqldepot-r
    keys: 
        - mssqldepot-r

    - name: mssqldepot-rw
    keys: 
        - mssqldepot-rw

```


### **2. Apply the Depot manifest file**

Apply the Depot manifest file by executing the below command.

```bash
dataos-ctl apply -f /home/mssql\_depot.yaml
```

### **4. Validate the Depot**



Apply the below command to validate the Depot:

```bash
dataos-ctl resource get -t depot -n mssqldepot
```

Now this Depot is used to further develop the Data Product, to learn more about the Data Products, please refer [to this link](/products/data_product/).