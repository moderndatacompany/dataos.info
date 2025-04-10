# Steps to Create Pulsar Depot

To create a Pulsar Depot you must have the following details:

## Pre-requisites specific to Depot creation

- **Tags:** A developer must possess the following tags, which can be obtained from a DataOS operator.

    ```bash
            NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
        ─────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
        Iamgroot     │   iamgroot  │ person │   iamgroot@tmdc.io   │ roles:id:data-dev,                            
                     │             │        │                      │ roles:id:user,                  
                     │             │        │                      │ users:id:iamgroot  
    ```

- **Use cases:** Alternatively, instead of assigning tags, a developer can create a Depot if an operator grants them the "Manage All Instance-level Resources of DataOS in the user layer" use case through Bifrost Governance.![](/usecase2.png)

    <center>
    <img src="/resources/depot/usecase2.png" alt="Bifrost Governance" style="width:60rem; border: 1px solid black; padding: 5px;" />
    <figcaption><i>Bifrost Governance</i></figcaption>
    </center>

## Pre-requisites specific to the source system

- **Admin URL**: The administrative endpoint URL of your Apache Pulsar cluster. This URL is used to perform administrative operations on the cluster. You can obtain this from the Pulsar admin or from the configuration details of the Pulsar cluster, typically provided during setup or accessible in the deployment documentation.

- **Service URL**: The service endpoint URL of your Apache Pulsar cluster. This URL is used by producers and consumers to connect to the cluster and exchange messages. You can retrieve this from the Pulsar admin or by referring to the connection details in the Pulsar cluster configuration.

## Create a Pulsar Depot

DataOS provides the capability to create a Depot of type 'PULSAR' for reading topics and messages stored in Pulsar. This Depot facilitates the consumption of published topics and the processing of incoming streams of messages. To create a Depot of type 'PULSAR', follow the below steps:

### **Step 1: Create a Pulsar Depot manifest file**

Create a manifest file to hold the configuration details for your Pulsar Depot.

```yaml 
name: ${{depot-name}}
version: v1
type: depot
tags:
    - ${{tag1}}
    - ${{tag2}}
owner: ${{owner-name}}
layer: user
depot:
    type: PULSAR       
    description: ${{description}}
    external: ${{true}}
    spec:              
    adminUrl: ${{admin-url}}
    serviceUrl: ${{service-url}}
    tenant: ${{system}}
# Ensure to obtain the correct tenant name and other specifications from your organization.
```

To get the details of each attribute, please refer [to this link](/resources/depot/configurations).
   


### **Step 2: Apply the Depot manifest file**

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