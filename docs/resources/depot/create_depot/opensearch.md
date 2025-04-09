# Steps to create Opersearch Depot

To create an Opensearch Depot you must have the following details:

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

- **Username**: The username used to authenticate and access the OpenSearch cluster. This is typically set up by the OpenSearch admin and assigned to users with specific access permissions.

- **Password**: The password associated with the OpenSearch username for authentication. This is created during user setup and should be securely retrieved from the OpenSearch admin if not known.

- **Nodes (Hostname/URL of the server and ports)**: The addresses of one or more OpenSearch nodes, including the hostname or URL and the port (e.g., `node1.opensearch.example.com:9200`). These nodes are part of the cluster and are necessary to establish the connection. This information can be obtained from the OpenSearch admin or by referring to the cluster's configuration details.

## Create an Opensearch Depot

DataOS provides the capability to connect to Opensearch data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics. To create a Depot of Opensearch, in the type field you will have to specify type ‘ELASTICSEARCH‘,  follow the below steps:

### **Step 1: Create an Instance Secret for securing Opensearch credentials**

Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/index#abfss).

### **Step 2: Create an Opensearch Depot manifest file**

Begin by creating a manifest file to hold the configuration details for your Opensearch Depot. A Depot can be created in two ways: either by directly specifying the credentials inline within the same manifest file or by creating an Instance Secret containing those credentials and referencing the Instance Secret by name in the Depot manifest file.



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
    type: OPENSEARCH           
    description: ${{description}}
    external: ${{true}}
    secrets:
    - name: ${{sf-instance-secret-name}}-r
        allkeys: true

    - name: ${{sf-instance-secret-name}}-rw
        allkeys: true
    elasticesearch:                           
    nodes:
        - ${{nodes}}
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