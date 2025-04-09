# Steps to create ABFSS Depot

To create an ABFSS Depot you must have the following details:

## Pre-requisites specific to Depot creation

- **Tags:** A developer must possess the following tags, which can be obtained from a DataOS operator.

    ```bash
            NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
      ───────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
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

- **Storage Account Name**: The name of the Azure storage account used to store your data. This can be obtained from the Azure portal under your storage account settings or from the administrator managing your Azure resources.

- **Storage Account Key**: The key used to authenticate and access the Azure storage account. It is generated when the storage account is created and can be retrieved from the Azure portal under the "Access keys" section of your storage account.

- **Container**: The name of the container within the Azure storage account that holds your data. You can find this information in the Azure portal under the "Containers" section of your storage account, or it can be provided by your Azure administrator.

- **Relative Path**: The relative path to the specific data within the container. This path is relative to the root of the container and can be provided by the person managing the data stored in the container or found by navigating through the container in Azure Blob Storage.

- **Data Format Stored in the Container**: The format of the data stored in the container (e.g., Parquet, CSV, JSON). This should be specified during data storage and can be verified by reviewing the data files or by asking the administrator managing the data.

## Create an ABFSS Depot

Azure Blob File System Secure (ABFSS) is an object storage system. Object stores are distributed storage systems designed to store and manage large amounts of unstructured data.
DataOS enables the creation of a Depot of type 'ABFSS' to facilitate the reading of data stored in an Azure Blob Storage account. This Depot provides access to the storage account, which can consist of multiple containers. A container serves as a grouping mechanism for multiple blobs. It is recommended to define a separate Depot for each container. To create a Depot of type ‘ABFSS‘, follow the below steps:

### **Step 1: Create an Instance Secret for securing ABFSS credentials**

Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/index#abfss).

### **Step 2: Create an ABFSS Depot manifest file**

Begin by creating a manifest file to hold the configuration details for your ABFSS Depot and reference to the Instance Secrets.


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
  type: ABFSS                                       
  description: ${{description}}
  external: ${{true}}
  compute: ${{runnable-default}}
  secrets:
    - name: ${{abfss-instance-secret-name}}-r
      allkeys: true

    - name: ${{abfss-instance-secret-name}}-rw
      allkeys: true
  abfss:                                             
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

## Limit the data source's file format

Another important function that a Depot can play is to limit the file type that can read from and write to a particular data source. In the `spec` section of the config file, simply mention the `format` of the files you want to allow access to.

```yaml
depot:
  type: S3
  description: $${{description}}
  external: true
  spec:
    scheme: $${{s3a}}
    bucket: $${{bucket-name}}
    relativePath: "raw" 
    format: $${{format}}  # mention the file format, such as JSON
```

For file-based systems, if you define the format as ‘Iceberg’, you can choose the meta-store catalog between Hadoop and Hive. This is how you do it:

```yaml
depot:
  type: ABFSS
  description: "ABFSS Iceberg Depot for sanity"
  compute: runnable-default
  spec:
    account: 
    container: 
    relativePath:
    format: ICEBERG
    endpointSuffix:
    icebergCatalogType: Hive
```

If you do not mention the catalog name as Hive, it will use Hadoop as the default catalog for Iceberg format. Hive automatically keeps the pointer updated to the latest metadata version. If you use Hadoop, you have to manually do this by running the set metadata command as described on this page: [Set Metadata](https://dataos.info/resources/depot/lakehouse/).