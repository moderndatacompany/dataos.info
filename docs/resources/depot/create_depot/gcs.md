# Steps to create GCS Depot


To create a GCS Depot you must have the following details:

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

- **GCS Bucket**: The name of the Google Cloud Storage bucket you want to access. You can find the bucket name in the Google Cloud Console under the "Storage" section, where all your buckets are listed.

- **Relative Path**: The path to the specific file or directory within the GCS bucket. This path can be obtained by navigating to the file or directory in the Google Cloud Console and copying the relative path from the bucket.

- **GCS Project ID**: The unique identifier of the Google Cloud project associated with the GCS bucket. This can be found in the Google Cloud Console under "Project Info" on your project dashboard.

- **GCS Account Email**: The email address associated with the Google Cloud service account that has access to GCS. This can be found in the IAM & Admin section of the Google Cloud Console under the "Service Accounts" tab.

- **GCS Key**: The JSON key file associated with the Google Cloud service account used for authentication. You can download this key by going to the IAM & Admin \> Service Accounts section in the Google Cloud Console, selecting the service account, and clicking "Add Key" \> "JSON".

## Create a GCS Depot

DataOS provides the capability to connect to Google Cloud Storage data using Depot. To create a Depot of Google Cloud Storage follow the below steps:

### **Step 1: Create an Instance Secret for securing GCS credentials**


Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/index#abfss).

### **Step 2: Create a GCS Depot manifest file**

Begin by creating a manifest file to hold the configuration details for your GCS Depot.



```yaml 
name: ${{"sanitygcs01"}}
version: v2alpha
type: depot
tags:
    - ${{GCS}}
    - ${{Sanity}}
layer: user
depot:
    type: GCS
    description: ${{"GCS depot for sanity"}}
    compute: ${{runnable-default}}
    gcs:
    bucket: ${{"airbyte-minio-testing"}}
    relativePath: ${{"/sanity"}}
    external: ${{true}}
    secrets:
    - name: ${{gcs-instance-secret-name}}-r
        allkeys: true

    - name: ${{gcs-instance-secret-name}}-rw
        allkeys: true
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

    ```bash Command
    dataos-ctl delete -t depot -n ${{name of Depot}}
    ```

=== "Alternative Command"

    ```bash Alternative command
    dataos-ctl delete -f ${{path of your manifest file}}
    ```



By executing the above command, the specified Depot will be deleted from your DataOS environment.