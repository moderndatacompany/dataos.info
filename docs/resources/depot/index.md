---
title: Depot
search:
  boost: 4
---

# :resources-depot: Depot

Depot in DataOS is a [Resource](/resources/) used to connect different data sources to DataOS by abstracting the complexities associated with the underlying source system (including protocols, credentials, and connection schemas). It enables users to establish connections and retrieve data from various data sources, such as file systems (e.g., AWS S3, Google GCS, Azure Blob Storage), data lake systems, database systems (e.g., Redshift, SnowflakeDB, Bigquery, Postgres), and event systems (e.g., Kafka, Pulsar) without moving the data. 

<div class="grid cards" markdown>

-   :material-format-list-bulleted-type:{ .lg .middle } **How to create and manage a Depot?**

    ---

    Create Depots to set up the connection between DataOS and data source.

    [:octicons-arrow-right-24: Create Depot](/resources/depot/#how-to-create-a-depot)


-   :material-script-text-outline:{ .lg .middle } **How to utilize Depots?**

    ---

    Utilize Depots to work on your data.

    [:octicons-arrow-right-24: Utilizing Depots](/resources/depot/#how-to-utilize-depots)



-   :material-clock-fast:{ .lg .middle } **Depot Templates**

    ---

    Depot example usage.

    [:octicons-arrow-right-24: Configuration Template](/resources/depot/#templates-of-depot-for-different-source-systems)


-   :material-console:{ .lg .middle } **Data Integration**

    ---

    Depots support various data sources within DataOS.


    [:octicons-arrow-right-24: Supported Connectors](/resources/depot/#data-integration-supported-connectors-in-dataos)
     
</div>

Within DataOS, the hierarchical structure of a data source is represented as follows:

<div style="text-align: center;">
  <img src="/resources/depot/udl.png" alt="Hierarchical Structure of a Data Source within DataOS" style="border:1px solid black; width: 60%; height: auto;">
  <figcaption><i>Hierarchical Structure of a Data Source within DataOS</i></figcaption>
</div>


The Depot serves as the registration of data locations to be made accessible to DataOS. Through the Depot Service, each source system is assigned a unique address, referred to as a **Uniform Data Link (UDL)**. The UDL grants convenient access and manipulation of data within the source system, eliminating the need for repetitive credential entry. The UDL follows this format:

<center><b><span style="font-size: 20px;"><code>dataos://[depot]:[collection]/[dataset]</code></span></b></center>



<aside class="callout">

🗣 Depot Service is a DataOS Service that manages the Depot Resource. It facilitates in-depth introspection of Depots and their associated storage engines. Once a Depot is created, users can obtain comprehensive information about the datasets contained within, including details such as constraints, partition, indexing, etc.

</aside>

Leveraging the UDL enables access to datasets and seamless execution of various operations, including data transformation using various Clusters and [Policy](/resources/policy/) assignments.

Once this mapping is established, Depot Service automatically generates the Uniform Data Link (UDL) that can be used throughout DataOS to access the data. As a reminder, the UDL has the format: `dataos://[depot]:[collection]/[dataset]`.

For a simple file storage system, "Collection" can be analogous to "Folder," and "Dataset" can be equated to "File." The Depot's strength lies in its capacity to establish uniformity, eliminating concerns about varying source system terminologies.

Once a Depot is created, all members of an organization gain secure access to datasets within the associated source system. The Depot not only facilitates data access but also assigns **default** [Access Policies](/resources/policy/) to ensure data security. Moreover, users have the flexibility to define and utilize custom [Access Policies](/resources/policy/) for the Depot and [Data Policies](/resources/policy/) for specific datasets within the Depot.

<aside class="callout">
 🗣️ Depot provides 'access' to data, meaning that data remains within the source system and is neither moved nor duplicated. However, DataOS offers multiple Stacks such as Flare, Benthos, etc. to perform ingestion, querying, syndication, and copying if the need arises.

</aside>



## How to create a Depot?
To create a Depot in DataOS, simply compose a manifest configuration file for a Depot and apply it using the DataOS [Command Line Interface (CLI)](/interfaces/cli/).

### **Structure of a Depot manifest**


<center>
  <img src="/resources/depot/depot_yaml.png" alt="Structure of a Depot manifest" style="width:40rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Structure of a Depot manifest</i></figcaption>
</center>

To know more about the attributes of Depot manifest Configuration, refer to the link: [Attributes of Depot manifest](/resources/depot/configurations/).

### **Prerequisites**

Before proceeding with Depot creation, it is essential to ensure that you possess the required authorization. To confirm your eligibility, execute the following commands in the CLI:

```bash
dataos-ctl user get
# Expected Output
INFO[0000] 😃 user get...                                
INFO[0000] 😃 user get...complete                        

      NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS    
───────────────┼─────────────┼────────┼──────────────────────┼────────────────────
  IamGroot     │ iamgroot    │ person │ iamgroot@tmdc.io     │ roles:id:data-dev,  
               │             │        │                      │ roles:id:operator,  
               │             │        │                      │ roles:id:system-dev, 
               │             │        │                      │ roles:id:user,    
               │             │        │                      │ users:id:iamgroot
```
To create Depots, ensure that you possess the following tags.

- `roles:id:user`
- `roles:id:data-dev`
- `roles:id:system-dev`


<aside class="callout">
🗣 If you do not possess these tags, contact the DataOS Operator or Administrator within your organization to assign you the necessary tag or the use case for the creation of the Depot.

</aside>

### **Create a manifest file**
The manifest configuration file for a Depot can be divided into four main sections: [Resource section](#configure-resource-section), [Depot-specific section](#configure-depot-specific-section), [Connection Secrets section](#configure-connection-secrets-section), and [Specifications section](#configure-spec-section¶). Each section serves a distinct purpose and contains specific attributes.

**Configure Resource section**

The Resource section of the manifest configuration file consists of attributes that are common across all resource types. The following snippet demonstrates the key-value properties that need to be declared in this section:

=== "v1"
    ```yaml
    name: $${{mydepot}}
    version: v1 
    type: Depot 
    tags: 
      - $${{dataos:type:resource}}
    description: $${{This is a sample Depot YAML configuration}} 
    owner: $${{iamgroot}}
    layer: user
    ```

=== "v2alpha"
    ```yaml
    name: $${{mydepot}}
    version: v2alpha 
    type: Depot 
    tags: 
      - $${{dataos:type:resource}}
    description: $${{This is a sample Depot YAML configuration}} 
    owner: $${{iamgroot}}
    layer: user
    ```

For more details regarding attributes in the Resource section, refer to the link: [Attributes of Resource Section.](/resources/manifest_attributes/)

**Configure Depot-specific section**

The Depot-specific section of the configuration file includes key-value properties specific to the Depot-type being created. Each Depot type represents a Depot created for a particular data source. Multiple Depots can be established for the same data source, and they will be considered as a single Depot type. The following snippet illustrates the key values to be declared in this section:

```yaml
depot:   
  type: $${{BIGQUERY}}                  
  description: $${{description}}
  external: $${{true}}                  
  source: $${{bigquerymetadata}} 
  compute: $${{runnable-default}}
  connectionSecrets:
    {}
  specs:
    {}
```

The table below elucidates the various attributes in the Depot-specific section:

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`depot`](/resources/depot/configurations/#depot) | object | none | none | mandatory |
| [`type`](/resources/depot/configurations/#type) | string | none | ABFSS, WASBS, REDSHIFT,<br> S3, ELASTICSEARCH, EVENTHUB, PULSAR, BIGQUERY, GCS, JDBC, MSSQL, MYSQL, OPENSEARCH, ORACLE, POSTGRES, SNOWFLAKE | mandatory |
| [`description`](/resources/depot/configurations/#description) | string | none | any string | mandatory |
| [`external`](/resources/depot/configurations/#external) | boolean | false | true/false | mandatory |
| [`source`](/resources/depot/configurations/#source) | string | Depot name | any string which is a valid Depot name | optional |
| [`compute`](/resources/depot/configurations/#compute) | string | runnable-default | any custom Compute Resource | optional |
| [`connectionSecret`](/resources/depot/configurations/#connectionSecret) | object | none | varies between data sources | optional |
| [`spec`](/resources/depot/configurations/#spec) | object | none | varies between data sources | mandatory |


**Configure connection Secrets section**

The configuration of connection secrets is specific to each Depot type and depends on the underlying data source. The details for these connection secrets, such as credentials and authentication information, should be obtained from your enterprise or data source provider. For commonly used data sources, we have compiled the connection secrets [here.](/resources/depot/depot_config_templates/) Please refer to these templates for guidance on how to configure the connection secrets for your specific data source.

<aside class="callout">
🗣 The credentials you use here need to have access to the schemas in the configured database.

</aside>

**Examples**

Here are examples demonstrating how the key-value properties can be defined for different Depot-types:


=== "BigQuery"
    For [BigQuery](/resources/depot/depot_config_templates/google_bigquery/), the `connectionSecret` section of the configuration file would appear as follows:
    ```yaml 
    #Properties depend on the underlying data source
    connectionSecret:                    
      - acl: rw                        
        type: key-value-properties
        data:
          projectid: $${{project-name}}
          email: $${{email-id}}
        files:
          json_keyfile: $${{secrets/gcp-demo-sa.json}} #JSON file containing the credentials to read-write 
      - acl: r                        
        type: key-value-properties
        files:
          json_keyfile: $${{secrets/gcp-demo-sa.json}} #JSON file containing the credentials to read-only`  
    ```
=== "AWS S3"
    This is how you can declare connection secrets to create a Depot for [AWS S3](/resources/depot/depot_config_templates/amazon_s3/) storage:

    ```yaml
    connectionSecret:                     
      - acl: rw                         
        type: key-value-properties
        data:                           #credentials required to access aws
          awsaccesskeyid: $${{AWS_ACCESS_KEY_ID}}
          awsbucketname: $${{bucket-name}}
          awssecretaccesskey: $${{AWS_SECRET_ACCESS_KEY}}
    ```

=== "JDBC"
    For accessing [JDBC](/resources/depot/depot_config_templates/jdbc/), all you need is a username and password. Check it out below:

    ```yaml
    connectionSecret:
      - acl: rw
        type: key-value-properties
        data:                            #for JDBC, the credentials you get from the data source should have permission to read/write schemas of the database being accessed 
          username: $${{username}}
          password: $${{password}}
    ```


The basic attributes filled in this section are provided in the table below:

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`acl`](/resources/depot/configurations/#acl) | string | none | r/rw | mandatory |
| [`type`](/resources/depot/configurations/#type) | string | none | key-value properties | mandatory |
| [`data`](/resources/depot/configurations/#data) | object | none | fields within data varies between data sources | mandatory |
| [`files`](/resources/depot/configurations/#files) | string | none | valid file path | optional |

</center>


**Alternative approach: using Instance Secret**

[Instance Secret](/resources/instance_secret/) is also a [Resource](/resources/) in DataOS that allows users to securely store sensitive piece of information such as username, password, etc. Using Secrets in conjunction with [Depots](/resources/depot/), [Stacks](/resources/stacks/) allows for decoupling of sensitive information from Depot and Stack YAMLs. For more clarity, let’s take the example of MySQL data source to understand how you can use Instance Secret Resource for Depot creation:

- Create an Instance Secret file with the details on the connection secret:

``` yaml
name: $${{mysql-secret}}
version: v1      
type: instance-secret
instance-secret:
  type: key-value-properties
  acl: rw
  data:
    connection-user: $${{user}}
    connection-password: $${{password}}
```

- Apply this YAML file on DataOS CLI

``` shell
dataos-ctl apply -f $${{path/instance_secret.yaml}}
```


For example, if a user wishes to create a MySQL Depot, they can define a Depot configuration file as follows:

<details>
<summary>YAML Configuration File</summary>

```yaml

name: mysql05
version: v1
type: Depot
tags:
  - dropzone
  - mysql
layer: user
depot:
  type: MYSQL
  description: "MYSQL Sample data"
spec:
  host: $${{host}}
  port: $${{port}}
external: true
dataosSecrets:
  - name: Depotsecret-r
    keys:
      - Depotsecret-r

  - name: Depotsecret-rw
    keys:
      - Depotsecret-rw
```

By referencing the name of the Instance Secret, "mysql-secret," users can easily incorporate the specified credentials into their Depot configuration. This approach ensures the secure handling and sharing of sensitive information.

</details>

To learn more about Instance Secrets as a Resource and their usage, refer to the documentation [here](/resources/instance_secret/).

**Configure spec section**

The `spec` section in the manifest configuration file plays a crucial role in directing the Depot to the precise location of your data and providing it with the hierarchical structure of the data source. By defining the specification parameters, you establish a mapping between the data and the hierarchy followed within DataOS.

Let's understand this hierarchy through real-world examples:


=== "BigQuery"


    In the case of BigQuery, the data is structured as "Projects" containing "Datasets" that, in turn, contain "Tables". In DataOS terminology, the "Project" corresponds to the "Depot", the "Dataset" corresponds to the "Collection", and the "Table" corresponds to the "Dataset".

    Consider the following structure in [BigQuery](/resources/depot/depot_config_templates/google_bigquery/):

    - Project name: `bigquery-public-data` (Depot)
    - Dataset name: `covid19_usa` (Collection)
    - Table name: `datafile_01` (Dataset)

    The UDL for accessing this data would be `dataos://bigquery-public-data:covid19_usa/datafile_01`.

    In the YAML example below, the necessary values are filled in to create a [BigQuery](/resources/depot/depot_config_templates/google_bigquery/) Depot:

    <details>
    <summary> Bigquery Depot manifest Configuration </summary>

    ```yaml
    name: covidbq
    version: v1
    type: Depot
    tags:
      - bigquery
    layer: user
    Depot:
      type: BIGQUERY
      description: "Covid public data in Google Cloud BigQuery"
      external: true
      spec:
        project: bigquery-public-data
    ```
    </details>

    In this example, the Depot is named "covidbq" and references the project "bigquery-public-data" within Google Cloud. As a result, all the datasets and tables within this project can be accessed using the UDL `dataos://covidbq:<collection name>/<dataset name>`.

    By appropriately configuring the specifications, you ensure that the Depot is accurately linked to the data source's structure, enabling seamless access and manipulation of datasets within DataOS.

=== "Amazon S3"

    Depot provides flexibility in mapping the hierarchy for file storage systems. Let's consider the example of an [Amazon S3](/resources/depot/depot_config_templates/amazon_s3/) bucket, which has a flat structure consisting of buckets, folders, and objects. By understanding the hierarchy and utilizing the appropriate configurations, you can effectively map the structure to DataOS components.

    ![Bucket](/resources/depot/create_depot_2.png)
    <center><i>Amazon S3 Bucket Structure</i></center>


    Here's an example of creating a Depot named 's3depot' that maps the following structure:

    - Bucket: `abcdata` (Depot)
    - Folder: `transactions` (Collection)
    - Objects: `file1` and `file2` (Datasets)

    In the YAML configuration, specify the bucket name and the relative path to the folder. The manifest example below demonstrates how this can be achieved:

    ``` yaml
    name: s3depot
    version: v1
    type: Depot
    tags:
      - S3
    layer: user
    Depot:
      type: S3
      description: "AWS S3 Bucket for dummy data"
      external: true
      spec:
        bucket: "abcdata"
        relativePath:
    ```
    If you omit the `relativePath` in the manifest configuration, the bucket itself becomes the Depot in DataOS. In this case, the following UDLs can be used to read the data:

    - `dataos://s3depot:transactions/file1`
    - `dataos://s3depot:transactions/file2`

    Additionally, if there are objects present in the bucket outside the folder, you can use the following UDLs to read them:

    - `dataos://s3depot:none/online-transaction`
    - `dataos://s3depot:none/offline-transaction`

    <aside class="callout">
    🗣️ The name 'none' is used for the collection in this case since there is no three-level ordinal hierarchy. The objects 'online-transaction' and 'offline-transaction' are directly accessed as datasets in the S3 bucket.
    </aside>


    However, if you prefer to treat the 'transactions' folder itself as another object within the bucket rather than a folder, you can modify the UDLs as follows:

    - `dataos://s3depot:none/transactions/file1`
    - `dataos://s3depot:none/transactions/file2`

    In this case, the interpretation is that there is no collection in the bucket, and 'file1' and 'file2' are directly accessed as objects with the path '/transactions/file1' and '/transactions/file2'.

    When configuring the manifets file for S3, if you include the `relativePath` as shown below, the 'transactions' folder is positioned as the Depot:

    ``` yaml
    name: s3depot
    version: v1
    type: Depot
    tags:
      - S3
    layer: user
    Depot:
      type: S3
      description: "AWS S3 Bucket for dummy data"
      external: true
      spec:
        bucket: "abcdata"
        relativePath: "/transactions"
    ```    

    Since the folder ‘transactions’ in the bucket has now been positioned as the Depot, two things happen.

    First, you cannot read the object files online-transaction and offline-transaction using this Depot.

    Secondly with this setup, you can read the files within the 'transactions' folder using the following UDLs:

    - `dataos://s3depot:none/file1`
    - `dataos://s3depot:none/file2`

    <aside class="callout">
    🗣️ When writing data to a source system, names like 'none' or 'system' cannot be used for the collection. Therefore, the output of a Flare job cannot have an address like <code>dataos://${{depot name}}:none/${{dataset name}}</code> or <code>dataos://${{depot name}}:system/${{dataset name}}</code>.
    </aside>

=== "Kafka"

    For accessing data from [Kafka](/resources/depot/depot_config_templates/kafka/), where the structure consists of a broker list and topics, the `spec` section in the YAML configuration will point the Depot to the broker list, and the datasets will map to the topic list. The format of the manifest file will be as follows:
    ``` yaml
    Depot:
      type: KAFKA
      description: ${{description}}
      external: true
      spec:
        brokers:
          - ${{broker1}}
          - ${{broker2}}
    ```
### **Apply Depot YAML**

Once you have the manifest file ready in your code editor, simply copy the path of the manifest file and apply it through the DataOS CLI, using the command given below:

``` shell
dataos-ctl apply -f ${{yamlfilepath}}
```

## **How to manage a Depot?**

### **Verify Depot creation**

To ensure that your Depot has been successfully created, you can verify it in two ways:

- Check the name of the newly created Depot in the list of Depots where you are named as the owner:

``` shell
dataos-ctl get -t depot
```

- Alternatively, retrieve the list of all Depots created in your organization:

``` shell
dataos-ctl get -t depot -a
```

You can also access the details of any created Depot through the DataOS GUI in the [Operations App](/interfaces/operations/) and [Metis UI](/interfaces/metis/).

### **Delete Depot**

<aside class="callout">
📖 <strong>Best Practice:</strong> As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.
</aside>


If you need to delete a Depot, use the following command in the DataOS CLI:

``` shell
dataos-ctl delete -t depot -n ${{name of Depot}}
```


By executing the above command, the specified Depot will be deleted from your DataOS environment.

## **How to utilize Depots?**

Once a Depot is created, you can leverage its Uniform Data Links (UDLs) to access data without physically moving it. The UDLs play a crucial role in various scenarios within DataOS.

### **Work with Stacks**

Depots are compatible with different Stacks in DataOS. [Stacks](/resources/stacks/) provide distinct approaches to interact with the system and enable various programming paradigms in DataOS. Several Stacks are available that can be utilized with Depots, including [Scanner](/resources/stacks/scanner/) for introspecting Depots, [Flare](/resources/stacks/flare/) for data ingestion, transformation, syndication, etc., [Benthos](/resources/stacks/benthos/) for stream processing and [Data Toolbox](/resources/stacks/data_toolbox/) for managing [Icebase](/resources/depot/icebase/) DDL and DML. 

[Flare](/resources/stacks/flare/) and [Scanner](/resources/stacks/scanner/) Stacks are supported by all Depots, while [Benthos](/resources/stacks/benthos/), the stream-processing Stack, is compatible with read/write operations from streaming Depots like [Fastbase](/resources/depot/fastbase/) and Kafka Depots.

The UDL references are used as addresses for your input and output datasets within the manifest configuration file.

### **Limit data source's file format**

Another important function that a Depot can play is to limit the file type which you can read from and write to a particular data source. In the `spec` section of manifest config file, simply mention the `format` of the files you want to allow access for.

``` yaml
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
For File based systems, if you define the format as ‘Iceberg’, you can choose the meta-store catalog between Hadoop and Hive. This is how you do it:

``` yaml
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
If you do not mention the catalog name as Hive, it will use Hadoop as the default catalog for Iceberg format.


<center>
  <img src="/resources/depot/depot_catalog.png" alt="Flow when Hive is chosen as the catalog type" style="width:40rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Flow when Hive is chosen as the catalog type</i></figcaption>
</center>

Hive, automatically keeps the pointer updated to the latest metadata version. If you use Hadoop, you have to manually do this by running the set metadata command as described on this page: [Set Metadata](/resources/depot/icebase/).

### **Scan and catalog metadata**

By running the [Scanner](/resources/stacks/scanner/), you can scan the metadata from a source system via the Depot interface. Once the metadata is scanned, you can utilize [Metis](/interfaces/metis/) to catalog and explore the metadata in a structured manner. This allows for efficient management and organization of data resources.

### **Add Depot to Cluster sources to query the data**

To enable the [Minerva](/resources/cluster/#minerva) Query Engine to access a specific source system, you can add the Depot to the list of sources in the [Cluster](/resources/cluster/). This allows you to query the data using the DataOS [Workbench](/interfaces/workbench/). 

### **Create Policies upon Depots to govern the data**

[Access](/resources/#access-policy) and [Data Policies](/resources/#data-policy) can be created upon Depots to govern the data. This helps in reducing data breach risks and simplifying compliance with regulatory requirements. Access Policies can restrict access to specific Depots, collections, or datasets, while Data Policies allow you to control the visibility and usage of data.

### **Building data models**

You can use Lens to create Data Models on top of Depots and explore them using the [Lens App UI](/interfaces/lens/).

## **Supported storage architectures in DataOS**

DataOS Depots facilitate seamless connectivity with diverse storage systems while eliminating the need for data relocation. This resolves challenges pertaining to accessibility across heterogeneous data sources. However, the escalating intricacy of pipelines and the exponential growth of data pose potential issues, resulting in cumbersome, expensive, and unattainable storage solutions. In order to address this critical concern, DataOS introduces support for two distinct and specialized storage architectures - [Icebase](/resources/depot/icebase/) Depot, the Unified Lakehouse designed for OLAP data, and [Fastbase](/resources/depot/fastbase/) Depot, the Unified Streaming solution tailored for handling streaming data.

### **Icebase**

Icebase-type Depots are designed to store data suitable for OLAP processes. It offers built-in functionalities such as [schema evolution](/resources/depot/icebase/#schema-evolution), [upsert commands](/resources/depot/icebase/#creating-and-getting-datasets), and [time-travel capabilities](/resources/depot/icebase/#maintenance-snapshot-modelling-and-metadata-listing) for datasets. With Icebase, you can conveniently perform these actions directly through the DataOS CLI, eliminating the need for additional Stacks like [Flare](/resources/stacks/flare/). Moreover, queries executed on data stored in Icebase exhibit enhanced performance. For detailed information, refer to the Icebase [page](/resources/depot/icebase/).

### **Fastbase**

Fastbase type Depots are optimized for handling streaming data workloads. It provides features such as [creating](/resources/depot/fastbase/#create-a-dataset) and [listing topics](/resources/depot/fastbase/#list-topics), which can be executed effortlessly using the DataOS CLI. To explore Fastbase further, consult the [link](/resources/depot/fastbase/).

## **Data integration - Supported connectors in DataOS**

The catalogue of data sources accessible by one or more components within DataOS is provided on the following page: [Supported Connectors in DataOS](/resources/depot/list_of_connectors/).


## **Templates of Depot for different source systems**

To facilitate the creation of Depots accessing commonly used data sources, we have compiled a collection of pre-defined manifest templates. These templates serve as a starting point, allowing you to quickly set up Depots for popular data sources. 

To make the process of creating a Depot configuration easier, we provide a set of predefined templates for various data sources. These templates serve as a starting point for configuring your Depot based on the specific data source you are working with. Simply choose the template that corresponds to your organization's data source and follow the instructions provided to fill in the required information.

<aside class=callout>

🗣️ When using these templates, you will need to populate the key-value properties in the manifest file with the appropriate values for your data source. This requires a basic understanding of your organization's data infrastructure and the necessary credentials or connection details.

</aside>

You can access these templates by visiting the following tabs:


=== "Data <br> Warehouse"

    === "Amazon Redshift"

        DataOS provides the capability to establish a connection with the Amazon Redshift database. We have provided the template for the manifest file to establish this connection. To create a Depot of type ‘REDSHIFT‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"
            ```yaml title="redshift_v1.yaml"
            --8<-- "examples/resources/depot/data_warehouse/redshift/redshift_v1.yaml"
            ```

            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.            

        === "Instance Secret Reference"
            ```yaml title="redshift_v2alpha.yaml" 
            --8<-- "examples/resources/depot/data_warehouse/redshift/redshift_v2alpha.yaml"
            ```

            Follow these steps to create the Depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
        

        **Requirements**
        To establish a connection with Redshift, the following information is required:

        - Hostname
        - Port
        - Database name
        - User name and password

        Additionally, when accessing the Redshift Database in Workflows or other DataOS Resources, the following details are also necessary:

        - Bucket name where the data resides
        - Relative path
        - AWS access key
        - AWS secret key

    === "Google BigQuery"

        DataOS enables the creation of a Depot of type 'BIGQUERY' to read data stored in BigQuery projects. Multiple Depots can be created, each pointing to a different project. To create a Depot of type 'BIGQUERY', utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="bigquery_v2alpha.yaml" 
            --8<-- "examples/resources/depot/data_warehouse/bigquery/bigquery_v1.yaml"
            ```
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.            

        === "Instance Secret Reference"

            ```yaml title="bigquery_v2alpha.yaml" 
            --8<-- "examples/resources/depot/data_warehouse/bigquery/bigquery_v2alpha.yaml"
            ```
            Follow these steps to create the Depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.


        **Requirements**
        To establish a connection with BigQuery, the following information is required:

        - Project ID: The identifier of the BigQuery project.
        - Email ID: The email address associated with the BigQuery project.
        - Credential properties in JSON file: A JSON file containing the necessary credential properties.
        - Additional parameters: Any additional parameters required for the connection.

    === "Snowflake"
        DataOS provides integration with Snowflake, allowing you to seamlessly read data from Snowflake tables using Depots. Snowflake is a cloud-based data storage and analytics data warehouse offered as a Software-as-a-Service (SaaS) solution. It utilizes a new SQL database engine designed specifically for cloud infrastructure, enabling efficient access to Snowflake databases. To create a Depot of type 'SNOWFLAKE', you can utilize the following YAML template as a starting point:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="snowflake_v2alpha.yaml" 
            --8<-- "examples/resources/depot/data_warehouse/snowflake/snowflake_v1.yaml"
            ```   
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="snowflake_v2alpha.yaml" 
            --8<-- "examples/resources/depot/data_warehouse/snowflake/snowflake_v2alpha.yaml"
            ```
            Follow these steps to create the Depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection to Snowflake and create a Depot, you will need the following information:

        - Snowflake Account URL: The URL of your Snowflake account.
        - Snowflake Username: Your Snowflake login username.
        - Snowflake User Password: The password associated with your Snowflake user account.
        - Snowflake Database Name: The name of the Snowflake database you want to connect to.
        - Database Schema: The schema in the Snowflake database where your desired table resides.    
   

=== "Lakehouse or <br> Data Lake"

    === "Amazon S3"
        DataOS provides the capability to establish a connection with the Amazon S3 buckets. We have provided the template for the manifest file to establish this connection. To create a Depot of type ‘S3‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="s3_v1.yaml" 
            --8<-- "examples/resources/depot/lakehouse/amazon_s3/s3_v1.yaml"
            ```  
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="s3_v2alpha.yaml" 
            --8<-- "examples/resources/depot/lakehouse/amazon_s3/s3_v2alpha.yaml"
            ```
            Follow these steps to create the Depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Amazon S3, the following information is required:

        - AWS access key ID
        - AWS bucket name
        - Secret access key
        - Scheme
        - Relative Path
        - Format


    
    === "ABFSS"

        DataOS enables the creation of a Depot of type 'ABFSS' to facilitate the reading of data stored in an Azure Blob Storage account. This Depot provides access to the storage account, which can consist of multiple containers. A container serves as a grouping mechanism for multiple blobs. It is recommended to define a separate Depot for each container. To create a Depot of type ‘ABFSS‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="abfss_v1.yaml" 
            --8<-- "examples/resources/depot/lakehouse/abfss/abfss_v1.yaml"
            ``` 
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="abfss_v2alpha.yaml" 
            --8<-- "examples/resources/depot/lakehouse/abfss/abfss_v2alpha.yaml"
            ```
            Follow these steps to create the Depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Azure ABFSS, the following information is required:

        - Storage account name
        - Storage account key
        - Container
        - Relative path
        - Data format stored in the container    

    === "WASBS"

        DataOS enables the creation of a Depot of type 'WASBS' to facilitate the reading of data stored in Azure Data Lake Storage. This Depot enables access to the storage account, which can contain multiple containers. A container serves as a grouping of multiple blobs. It is recommended to define a separate Depot for each container.To create a Depot of type ‘WASBS‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="wasbs_v1.yaml" 
            --8<-- "examples/resources/depot/lakehouse/wasbs/wasbs_v1.yaml"
            ``` 
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="wasbs_v2alpha.yaml" 
            --8<-- "examples/resources/depot/lakehouse/wasbs/wasbs_v2alpha.yaml"
            ```
            Follow these steps to create the Depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Azure WASBS, the following information is required:

        - Storage account name
        - Storage account key
        - Container
        - Relative path
        - Format            



    === "GCS"

        DataOS provides the capability to connect to Google Cloud Storage data using Depot. To create a Depot of Google Cloud Storage, in the type field you will have to specify type 'GCS', and utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="gcs_v1.yaml" 
            --8<-- "examples/resources/depot/lakehouse/gcs/gcs_v1.yaml"
            ```
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="gcs_v2alpha.yaml" 
            --8<-- "examples/resources/depot/lakehouse/gcs/gcs_v2alpha.yaml"
            ```
            Follow these steps to create the Depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics.

        **Requirements**

        To establish a connection with Google Cloud Storage (GCS), the following information is required:

        - GCS Bucket
        - Relative Path
        - GCS Project ID
        - GCS Account Email
        - GCS Key

    === "Icebase"

        DataOS provides the capability to establish a connection with the Icebase Lakehouse over Amazon S3 or other object storages. We have provided the template for the manifest file to establish this connection. To create a Depot of type ‘S3‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="icebase_v1.yaml" 
            --8<-- "examples/resources/depot/lakehouse/icebase/icebase_v1.yaml"
            ``` 
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="icebase_v2alpha.yaml" 
            --8<-- "examples/resources/depot/lakehouse/icebase/icebase_v2alpha.yaml"
            ```
            Follow these steps to create the Depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.


        **Requirements**

        To establish a connection with Amazon S3, the following information is required:

        - AWS access key ID
        - AWS bucket name
        - Secret access key
        - Scheme
        - Relative Path
        - Format    

=== "Streaming <br> Source"

    === "Apache pulsar"

        DataOS provides the capability to create a Depot of type 'PULSAR' for reading topics and messages stored in Pulsar. This Depot facilitates the consumption of published topics and processing of incoming streams of messages. To create a Depot of type 'PULSAR,' utilize the following template:

        === "Inline Credentials"

            ```yaml title="pulsar_v1.yaml" 
            --8<-- "examples/resources/depot/streaming_source/apache_pulsar/pulsar_v1.yaml"
            ``` 
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Pulsar, the following information is required:

        - Admin URL
        - Service URL

    === "Eventhub"

        DataOS provides the capability to connect to Eventhub data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics. To create a Depot of Eventhub, in the type field you will have to specify type 'EVENTHUB', and utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="eh_v1.yaml" 
            --8<-- "examples/resources/depot/streaming_source/eventhub/eh_v1.yaml"
            ``` 
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="eh_v2alpha.yaml" 
            --8<-- "examples/resources/depot/streaming_source/eventhub/eh_v2alpha.yaml"
            ```
            Follow these steps to create the Depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Eventhub, the following information is required:

        - Endpoint
        - Eventhub Shared Access Key Name
        - Eventhub Shared Access Key   

    === "Kafka"

        DataOS allows you to create a Depot of type 'KAFKA' to read live topic data. This Depot enables you to access and consume real-time streaming data from Kafka. To create a Depot of type 'KAFKA', utilize the following template:

        === "Inline Credentials"

            ```yaml title="kafka_v1.yaml" 
            --8<-- "examples/resources/depot/streaming_source/kafka/kafka.yaml"
            ``` 
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        - To connect to Kafka, you need:

        - To establish a connection to Kafka, you need to provide the following information:

        - KAFKA broker list: The list of brokers in the Kafka cluster. The broker list enables the Depot to fetch all the available topics in the Kafka cluster.
        Schema Registry URL

=== "NoSQL <br> Database"

    === "Elasticsearch"

        DataOS provides the capability to connect to Elasticsearch data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics. To create a Depot of type ‘ELASTICSEARCH‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="es_v1.yaml" 
            --8<-- "examples/resources/depot/nosql_db/elasticsearch/es_v1.yaml"
            ``` 
            Follow these steps to create the Depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="es_v2alpha.yaml" 
            --8<-- "examples/resources/depot/nosql_db/elasticsearch/es_v2alpha.yaml"
            ```  
            Follow these steps to create the Depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Elasticsearch, the following information is required:

        - Username
        - Password
        - Nodes (Hostname/URL of the server and ports)


    === "MongoDB"

        DataOS allows you to connect to MongoDB using Depot, enabling you to interact with your MongoDB database and perform various data operations. You can create a MongoDB Depot in DataOS by providing specific configurations. To create a Depot of type 'MONGODB', use the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline credentials"

            === "Via username and password"

                ```yaml title="mongo_v1.yaml" 
                --8<-- "examples/resources/depot/nosql_db/mongodb/mongo_v1.yaml"
                ```  
            === "Via certification"

                ```yaml title="mongo_cert.yaml" 
                --8<-- "examples/resources/depot/nosql_db/mongodb/mongo_cert.yaml"
                ``` 
            === "Via VPC endpoint"

                ```yaml title="mongo_vpce.yaml" 
                --8<-- "examples/resources/depot/nosql_db/mongodb/mongo_vpce.yaml"
                ``` 


            Follow these steps to create the Depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.


        === "Instance Secret reference"

            ```yaml title="mongo_v2alpha.yaml" 
            --8<-- "examples/resources/depot/nosql_db/mongodb/mongo_v2alpha.yaml"
            ```  
            Follow these steps to create the Depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.


        **Requirements**

        To connect to MongoDB using DataOS and create a MongoDB Depot, the following information is required:

        - Subprotocol: The Subprotocol of the MongoDB Server
        - Nodes: Node
        - Username: The username for authentication.
        - Password: The password for authentication.
        - `.crt` file (for creating Depot via certification)
        - `.cert` file (for creating Depot via VPC endpoint)
        - `key_store_file` (for creating Depot via certification or VPC endpoint)
        - `trust_store_file` (for creating Depot via certification or VPC endpoint)


    === "Opensearch"

        DataOS provides the capability to connect to Opensearch data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics. To create a Depot of Opensearch, in the type field you will have to specify type ‘ELASTICSEARCH‘, and utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="os_v2alpha.yaml" 
            --8<-- "examples/resources/depot/nosql_db/opensearch/os_v1.yaml"
            ```  
            Follow these steps to create the Depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.


        === "Instance Secret Reference"

            ```yaml title="os_v1.yaml" 
            --8<-- "examples/resources/depot/nosql_db/opensearch/os_v2alpha.yaml"
            ```
            Follow these steps to create the Depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Opensearch, the following information is required:

        - Username
        - Password
        - Nodes (Hostname/URL of the server and ports)


=== "Relational <br> Database"

    === "JDBC"

        DataOS provides the capability to establish a connection to a database using the JDBC driver in order to read data from tables using a Depot. The Depot facilitates access to all schemas visible to the specified user within the configured database. To create a Depot of type ‘JDBC‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="jdbc_v1.yaml" 
            --8<-- "examples/resources/depot/relational_db/jdbc/jdbc_v1.yaml"
            ``` 
            Follow these steps to create the Depot:

            - **Step 1**: Create a manifest file.
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="jdbc_v2alpha.yaml" 
            --8<-- "examples/resources/depot/relational_db/jdbc/jdbc_v2alpha.yaml"
            ```  
            Follow these steps to create the Depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**
        To establish a JDBC connection, the following information is required:

        - Database name: The name of the database you want to connect to.
        - Subprotocol name: The subprotocol associated with the database (e.g., MySQL, PostgreSQL).
        - Hostname/URL of the server, port, and parameters: The server's hostname or URL, along with the - port and any additional parameters needed for the connection.
        - Username: The username to authenticate the JDBC connection.
        - Password: The password associated with the provided username.

        **Self-signed Certificate (SSL/TLS) Requirement**

        If you are connecting to relational databases using the JDBC API and encounter self-signed certificate (SSL/TLS) requirements, you can disable encryption by modifying the YAML configuration file. Simply provide the necessary details for the subprotocol, host, port, database, and use the params field to specify the appropriate parameters for your specific source system as shown below:

        === "v1"

            ``` yaml
            spec:             # version v1
              subprotocol:
              host: 
              port: 
              database:
              params:
            #use params for JDBC type connections where self-signed certificates have been enabled
            ```
        === "v2alpha"

            ``` yaml
            jdbc:             # version v2alpha
              subprotocol:
              host: 
              port: 
              database:
              params:
            #use params for JDBC type connections where self-signed certificates have been enabled

            ```

        The particular specifications to be filled within params depend on the source system.

    === "MySQL"

        DataOS allows you to connect to a MySQL database and read data from tables using Depots. A Depot provides access to all tables within the specified schema of the configured database. You can create multiple Depots to connect to different MySQL servers or databases. To create a Depot of type ‘MYSQL‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        **Use this template, if self-signed certificate is enabled.**


        === "Inline Credentials"

            ```yaml title="mysql_v1.yaml" 
            --8<-- "examples/resources/depot/relational_db/mysql/mysql_v1.yaml"
            ``` 
            Follow these steps to create the Depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI. 

        === "Instance Secret Reference"

            ```yaml title="mysql_v2alpha.yaml" 
            --8<-- "examples/resources/depot/relational_db/mysql/mysql_v2alpha.yaml"
            ```  
            Follow these steps to create the Depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To connect to a MySQL database, you need the following information:

        - Host URL and parameters: The URL or hostname of the MySQL server along with any additional parameters required for the connection.
        - Port: The port number used for the MySQL connection.
        - Username: The username for authentication.
        - Password: The password for authentication.

        **If self-signed certificates are not being used** by your organization, you can omit the params section within the spec:
            
        === "Inline Credentials"
        
            ``` yaml
            name: ${{"mysql01"}}
            version: v1
            type: Depot
            tags:
              - ${{dropzone}}
              - ${{mysql}}
            layer: user
            Depot:
              type: MYSQL
              description: ${{"MYSQL Sample data"}}
              spec:
                host: ${{host}}
                port: ${{port}}
              external: true
              connectionSecret:
                - acl: rw
                  type: key-value-properties
                  data:
                    username: ${{username}}
                    password: ${{password}}
            ```      

        === "Instance Secret Reference"

            ``` yaml
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
                  allkeys: true

                - name: ${{instance-secret-name}}-rw
                  allkeys: true
            ```


    === "Microsoft SQL server"

        DataOS allows you to connect to a Microsoft SQL Server database and read data from tables using Depots. A Depot provides access to all tables within the specified schema of the configured database. You can create multiple Depots to connect to different SQL servers or databases. To create a Depot of type ‘SQLSERVER‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        **Use this template, if self-signed certificate is enabled.**

        === "Inline Credentials"

            ```yaml title="mssql_v1.yaml" 
            --8<-- "examples/resources/depot/relational_db/mssql_server/mssql_v1.yaml"
            ```         
            Follow these steps to create the Depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.            

        === "Instance Secret Reference"

            ```yaml title="mssql_v2alpha.yaml" 
            --8<-- "examples/resources/depot/relational_db/mssql_server/mssql_v2alpha.yaml"
            ```  
            Follow these steps to create the Depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
      

        **Requirements**
        To connect to a Microsoft SQL Server database, you need the following information:

        - Host URL and parameters: The URL or hostname of the SQL Server along with any additional parameters required for the connection.
        - Database schema: The schema in the database where your tables are located.
        - Port: The port number used for the SQL Server connection.
        - Username: The username for authentication.
        - Password: The password for authentication.

        If self-signed certificates are not being used by your organization, you can omit the params section within the spec:

        === "Inline Credentials"

            ``` yaml
            name: ${{mssql01}}
            version: v1
            type: Depot
            tags:
              - ${{dropzone}}
              - ${{mssql}}
            layer: user
            Depot:
              type: JDBC
              description: ${{MSSQL Sample data}}
              spec:
                subprotocol: sqlserver
                host: ${{host}}
                port: ${{port}}
                database: ${{database}}
                params: ${{'{"key":"value","key2":"value2"}'}}
              external: ${{true}}
              connectionSecret:
                - acl: rw
                  type: key-value-properties
                  data:
                    username: ${{username}}
                    password: ${{password}}
            ```

        === "Instance Secret Reference"

            ``` yaml
            name: ${{mssql01}}
            version: v2alpha
            type: Depot
            tags:
              - ${{dropzone}}
              - ${{mssql}}
            layer: user
            Depot:
              type: JDBC
              description: ${{MSSQL Sample data}}
              jdbc:
                subprotocol: sqlserver
                host: ${{host}}
                port: ${{port}}
                database: ${{database}}
                params: ${{'{"key":"value","key2":"value2"}'}}
              external: ${{true}}
              secrets:
                - name: ${{instance-secret-name}}-r
                  allkeys: true

                - name: ${{instance-secret-name}}-rw
                  allkeys: true
            ```

    === "Oracle"

        DataOS allows you to connect to an Oracle database and access data from tables using Depots. A Depot provides access to all schemas within the specified service in the configured database. You can create multiple Depots to connect to different Oracle servers or databases. To create a Depot of type ‘ORACLE‘, you can use the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="oracle_v1.yaml" 
            --8<-- "examples/resources/depot/relational_db/oracle/oracle_v1.yaml"
            ```  
            Follow these steps to create the Depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
                  
        === "Instance Secret Reference"

            ```yaml title="oracle_v2alpha.yaml" 
            --8<-- "examples/resources/depot/relational_db/oracle/oracle_v2alpha.yaml"
            ```  
            Follow these steps to create the Depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
      


        **Requirements**

        To connect to an Oracle database, you need the following information:

        - URL of your Oracle account: The URL or hostname of the Oracle database.
        - User name: Your login user name.
        - Password: Your password for authentication.
        - Database name: The name of the Oracle database.
        - Database schema: The schema where your table belongs.



    === "PostgreSQL"

        DataOS allows you to connect to a PostgreSQL database and read data from tables using Depots. A Depot provides access to all schemas visible to the specified user in the configured database. To create a Depot of type ‘POSTGRESQL‘, use the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the Depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](/resources/instance_secret/) as `secrets` or `dataosSecrets`.      
        </aside>

        **Use this templates, if self-signed certificate is enabled.**

        === "Inline Credentials"

            ```yaml title="ps_v1.yaml" 
            --8<-- "examples/resources/depot/relational_db/postgre/ps_v1.yaml"
            ```
            Follow these steps to create the Depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
      
        === "Instance Secret Reference"

            ```yaml title="ps_v2alpha.yaml" 
            --8<-- "examples/resources/depot/relational_db/postgre/ps_v2alpha.yaml"
            ```  
            Follow these steps to create the Depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about Instance Secret, refer to [Instance Secret](/resources/instance_secret/). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
      

        **Requirements**
        To create a Depot and connect to a PostgreSQL database, you need the following information:

        - Database name: The name of the PostgreSQL database.
        - Hostname/URL of the server: The hostname or URL of the PostgreSQL server.
        - Parameters: Additional parameters for the connection, if required.
        - Username: The username for authentication.
        - Password: The password for authentication.

        **If self-signed certificates are not being used** by your organization, for connection to these storage systems, then you do not need to write additional parameters within the spec section.

        === "Inline Credentials"

            ``` yaml
            name: ${{depot-name}}
            version: v1
            type: Depot
            tags:
              - ${{tag1}}
            owner: ${{owner-name}}
            layer: user
            Depot:
              type: POSTGRESQL
              description: ${{description}}
              external: true
              connectionSecret:                               
                - acl: rw
                  type: key-value-properties
                  data:
                    username: ${{postgresql-username}}
                    password: ${{posgtresql-password}}
                - acl: r
                  type: key-value-properties
                  data:
                    username: ${{postgresql-username}}
                    password: ${{postgresql-password}}
              spec:                                          
                host: ${{host}}
                port: ${{port}}
                database: ${{database-name}}
                params: # Optional
                  ${{"key1": "value1"}}
                  ${{"key2": "value2"}}
            ```

        === "Instance Secret Reference"

            ``` yaml
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
