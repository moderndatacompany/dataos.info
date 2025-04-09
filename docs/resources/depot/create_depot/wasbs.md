# Steps to create WASBS Depot

To create a WASBS Depot, you must have the following details:

## Pre-requisites specific to Depot creation

- **Tags:** A developer must possess the following tags, which can be obtained from a DataOS admin.

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

- **Storage Account Name**: The name of your Azure Storage account, which identifies your storage resource in Azure. You can retrieve this from the Azure portal by navigating to your Storage Account under the Storage Accounts service.

- **Storage Account Key**: The access key used to authenticate and access your Azure Storage account. This can be obtained from the Azure portal by selecting your Storage Account, navigating to the "Access Keys" section, and copying the required key. Ensure it is securely stored.

- **Container**: The name of the container within your Azure Storage account that holds the required data. You can find this in the Azure portal under your Storage Account by navigating to the "Containers" section.

- **Relative Path**: The specific path to the file or directory within the container. This is typically provided by the team managing the data or can be derived from the structure of your container in the Azure portal.

- **Format**: The data format of the files stored within the container, such as CSV, JSON, or Parquet. This information is usually known based on the type of data being stored and consumed. If unsure, consult the team responsible for the data.

## Create a WASBS Depot

DataOS enables the creation of a Depot of type 'WASBS' to facilitate the reading of data stored in Azure Data Lake Storage. This Depot enables access to the storage account, which can contain multiple containers. A container serves as a grouping of multiple blobs. It is recommended to define a separate Depot for each container. To create a Depot of type ‘WASBS‘, follow the below steps:

### **Step 1: Create an Instance Secret for securing WASBS credentials**

Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/index#abfss).

### **Step 2: Create a WASBS Depot manifest file**

Create a manifest file to hold the configuration details for your WASBS Depot.

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
    type: WASBS                                      
    description: ${{description}}
    external: ${{true}}
    compute: ${{runnable-default}}
    secrets:
    - name: ${{wasbs-instance-secret-name}}-r
        allkeys: true

    - name: ${{wasbs-instance-secret-name}}-rw
        allkeys: true
    wasbs:                                          
    account: ${{account-name}}
    container: ${{container-name}}
    relativePath: ${{relative-path}}
    format: ${{format}}
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