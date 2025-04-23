# Steps to create Bigquery Depot

To create a Bigquery Depot you must have the following details:

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

- **Project ID**: The unique identifier for your Google Cloud project used by BigQuery. You can find this in the Google Cloud Console under "Project Info" on your project dashboard.

- **Email ID**: The email address associated with the Google Cloud service account used to access BigQuery. This can be found in the IAM & Admin section of the Google Cloud Console under the "Service Accounts" tab, where the email is listed for each service account.

- **Credential Properties in JSON File**: A JSON file containing the necessary credential properties for authentication. This file is generated when you create a service account in Google Cloud. You can download it from the IAM & Admin \> Service Accounts section in the Google Cloud Console by selecting a service account and clicking "Add Key" \> "JSON".

- **Additional Parameters**: Any extra configuration parameters required to establish the connection, such as project settings or specific access scopes. These may be provided by the administrator or defined in the BigQuery API documentation based on the integration you are working with.

## Create a Bigquery Depot

DataOS enables the creation of a Depot of type 'Bigquery' to facilitate the reading of data stored in an Azure Blob Storage account. This Depot provides access to the storage account, which can consist of multiple containers. A container serves as a grouping mechanism for multiple blobs. It is recommended to define a separate Depot for each container. To create a Depot of type ‘ABFSS‘, follow the below steps:

### **Step 1: Create an Instance Secret for securing Bigquery credentials**

Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/data_sources/bigquery/)

### **Step 2: Create a Bigquery Depot manifest file**

Begin by creating a manifest file to hold the configuration details for your Bigquery Depot.



```yaml Instance Secret reference Depot manifest file
name: ${{depot-name}}
version: v2alpha
type: depot
tags:
    - ${{dropzone}}
    - ${{bigquery}}
owner: ${{owner-name}}
layer: user
depot:
    type: BIGQUERY                 
    description: ${{description}} # optional
    external: ${{true}}
    secrets:
    - name: ${{instance-secret-name}}-r
        keys: 
        - ${{instance-secret-name}}-r

    - name: ${{instance-secret-name}}-rw
        keys: 
        - ${{instance-secret-name}}-rw
    bigquery:  # optional                         
    project: ${{project-name}} # optional
    params: # optional
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

## Delete a Depot

<aside class="callout">
🗣️ As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.
</aside>

If you need to delete a Depot, use the following command in the DataOS CLI:

=== "Command"

    ```bash 
    dataos-ctl delete -t depot -n ${{name of Depot}}
    ```

=== "Alternative Command "

    ```bash 
    dataos-ctl delete -f ${{path of your manifest file}}
    ```



By executing the above command, the specified Depot will be deleted from your DataOS environment.