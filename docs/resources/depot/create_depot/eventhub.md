# Steps to create Eventhub Depot

To create an Eventhub Depot you must have the following details:

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

- **Endpoint**: The URL endpoint used to connect to your EventHub instance. This can be found in the Azure portal under your EventHub namespace settings. It is typically in the format `your-namespace-name.servicebus.windows.net`.

- **Eventhub Shared Access Key Name**: The name of the shared access key used to authenticate access to the EventHub. You can retrieve this from the Azure portal under your EventHub namespace’s "Shared Access Policies" section, where you can create or view existing access keys.

- **Eventhub Shared Access Key**: The actual shared access key used to authenticate with EventHub. This key is found alongside the "Shared Access Key Name" in the "Shared Access Policies" section of your EventHub namespace settings in the Azure portal. Ensure that this key is securely stored and handled.

## Create an Eventhub Depot

Eventhub is a streaming service platform. Streaming refers to the continuous and real-time transmission of data from a source to a destination. 

DataOS provides the capability to connect to Eventhub data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics. To create a Depot of Eventhub, in the type field you will have to specify the type 'EVENTHUB' and follow the below steps:

### **Step 1: Create an Instance Secret for securing Eventhub credentials**

Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/).

### **Step 2: Create an Eventhub Depot manifest file**

Begin by creating a manifest file to hold the configuration details for your Eventhub Depot.


```yaml 
name: ${{"sanityeventhub01"}}
version: v2alpha
type: depot
tags:
    - ${{Eventhub}}
    - ${{Sanity}}
layer: user
depot:
    type: "EVENTHUB"
    compute: ${{runnable-default}}
    eventhub:
    endpoint: ${{"sb://event-hubns.servicebus.windows.net/"}}
    external: ${{true}}
    secrets:
    - name: ${{eh-instance-secret-name}}-r
        allkeys: true

    - name: ${{eh-instance-secret-name}}-rw
        allkeys: true
```
To get the details of each attribute, please refer [to this link](/resources/depot/configurations).


### **Step 3: Apply the Depot manifest file**

Once you have the manifest file ready in your code editor, simply copy the path of the manifest file and apply it through the DataOS CLI by pasting the path in the placeholder, using the command given below:

=== "Command"

    ```bash Command
    dataos-ctl resource apply -f ${{yamlfilepath}}
    ```

=== "Alternative Command"

    ```bash Alternative command
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