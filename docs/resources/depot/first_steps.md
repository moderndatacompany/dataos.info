## How to create a Depot?
To create a Depot in DataOS, simply compose a manifest configuration file for a Depot and apply it using the DataOS [Command Line Interface (CLI)](/interfaces/cli/).

### **Structure of a Depot manifest**

![Structure of a Depot YAML](/resources/depot/depot_yaml.png)

To know more about the attributes of Depot manifest Configuration, refer to the link: [Attributes of Depot manifest](/resources/depot/configuration/).

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
🗣 If you do not possess these tags, contact the DataOS Operator or Administrator within your organization to assign you the necessary tag or the use case for the creation of the depot.

</aside>

### **Create a Manifest File**
The manifest configuration file for a Depot can be divided into four main sections: [Resource section](#configure-resource-section), [Depot-specific section](#configure-depot-specific-section), [Connection Secrets section](#configure-connection-secrets-section), and [Specifications section](#configure-spec-section¶). Each section serves a distinct purpose and contains specific attributes.

**Configure Resource Section**

The Resource section of the manifest configuration file consists of attributes that are common across all resource types. The following snippet demonstrates the key-value properties that need to be declared in this section:

=== "v1"
    ```yaml
    name: ${{mydepot}}
    version: v1 
    type: depot 
    tags: 
      - ${{dataos:type:resource}}
    description: ${{This is a sample depot YAML configuration}} 
    owner: ${{iamgroot}}
    layer: user
    ```

=== "v2alpha"
    ```yaml
    name: ${{mydepot}}
    version: v2alpha 
    type: depot 
    tags: 
      - ${{dataos:type:resource}}
    description: ${{This is a sample depot YAML configuration}} 
    owner: ${{iamgroot}}
    layer: user
    ```

For more details regarding attributes in the Resource section, refer to the link: [Attributes of Resource Section.](/resources/resource_attributes/)

**Configure Depot-specific Section**

The Depot-specific section of the configuration file includes key-value properties specific to the Depot-type being created. Each Depot type represents a Depot created for a particular data source. Multiple Depots can be established for the same data source, and they will be considered as a single depot type. The following snippet illustrates the key values to be declared in this section:

```yaml
depot:   
  type: ${{BIGQUERY}}                  
  description: ${{description}}
  external: ${{true}}                  
  source: ${{bigquerymetadata}} 
  compute: ${{runnable-default}}
  connectionSecrets:
    {}
  specs:
    {}
```

The table below elucidates the various attributes in the Depot-specific section:

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`depot`](./depot/depot_yaml_configuration_attributes.md#depot) | object | none | none | mandatory |
| [`type`](./depot/depot_yaml_configuration_attributes.md#type) | string | none | ABFSS, WASBS, REDSHIFT,<br> S3, ELASTICSEARCH, EVENTHUB, PULSAR, BIGQUERY, GCS, JDBC, MSSQL, MYSQL, OPENSEARCH, ORACLE, POSTGRES, SNOWFLAKE | mandatory |
| [`description`](./depot/depot_yaml_configuration_attributes.md#description) | string | none | any string | mandatory |
| [`external`](./depot/depot_yaml_configuration_attributes.md#external) | boolean | false | true/false | mandatory |
| [`source`](./depot/depot_yaml_configuration_attributes.md#source) | string | depot name | any string which is a valid depot name | optional |
| [`compute`](./depot/depot_yaml_configuration_attributes.md#compute) | string | runnable-default | any custom Compute Resource | optional |
| [`connectionSecret`](./depot/depot_yaml_configuration_attributes.md#connectionSecret) | object | none | varies between data sources | optional |
| [`spec`](./depot/depot_yaml_configuration_attributes.md#spec) | object | none | varies between data sources | mandatory |


**Configure Connection Secrets Section**

The configuration of connection secrets is specific to each Depot type and depends on the underlying data source. The details for these connection secrets, such as credentials and authentication information, should be obtained from your enterprise or data source provider. For commonly used data sources, we have compiled the connection secrets [here.](/resources/depot/depot_config_templates/) Please refer to these templates for guidance on how to configure the connection secrets for your specific data source.

<aside class="callout">
🗣 The credentials you use here need to have access to the schemas in the configured database.

</aside>

**Examples**

Here are examples demonstrating how the key-value properties can be defined for different depot-types:


=== "BigQuery"
    For [BigQuery](/resources/depot/depot_config_templates/google_bigquery.md), the `connectionSecret` section of the configuration file would appear as follows:
    ```yaml 
    #Properties depend on the underlying data source
    connectionSecret:                    
      - acl: rw                        
        type: key-value-properties
        data:
          projectid: ${{project-name}}
          email: ${{email-id}}
        files:
          json_keyfile: ${{secrets/gcp-demo-sa.json}} #JSON file containing the credentials to read-write 
      - acl: r                        
        type: key-value-properties
        files:
          json_keyfile: ${{secrets/gcp-demo-sa.json}} #JSON file containing the credentials to read-only`  
    ```
=== "AWS S3"
    This is how you can declare connection secrets to create a Depot for [AWS S3](/resources/depot/depot_config_templates/amazon_s3.md) storage:

    ```yaml
    connectionSecret:                     
      - acl: rw                         
        type: key-value-properties
        data:                           #credentials required to access aws
          awsaccesskeyid: ${{AWS_ACCESS_KEY_ID}}
          awsbucketname: ${{bucket-name}}
          awssecretaccesskey: ${{AWS_SECRET_ACCESS_KEY}}
    ```

=== "JDBC"
    For accessing [JDBC](/resources/depot/depot_config_templates/jdbc.md), all you need is a username and password. Check it out below:

    ```yaml
    connectionSecret:
      - acl: rw
        type: key-value-properties
        data:                            #for JDBC, the credentials you get from the data source should have permission to read/write schemas of the database being accessed 
          username: ${{username}}
          password: ${{password}}
    ```


The basic attributes filled in this section are provided in the table below:

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`acl`](./depot/depot_yaml_configuration_attributes.md#acl) | string | none | r/rw | mandatory |
| [`type`](./depot/depot_yaml_configuration_attributes.md#type) | string | none | key-value properties | mandatory |
| [`data`](./depot/depot_yaml_configuration_attributes.md#data) | object | none | fields within data varies between data sources | mandatory |
| [`files`](./depot/depot_yaml_configuration_attributes.md#files) | string | none | valid file path | optional |

</center>


**Alternative Approach: Using Instance Secret**

[Instance Secret](/resources/instance_secret/) is also a [Resource](https://dataos.info/resources/) in DataOS that allows users to securely store sensitive piece of information such as username, password, etc. Using Secrets in conjunction with [Depots](/resources/depot/), [Stacks](/resources/stacks/) allows for decoupling of sensitive information from Depot and Stack YAMLs. For more clarity, let’s take the example of MySQL data source to understand how you can use Instance Secret Resource for Depot creation:

- Create an Instance Secret file with the details on the connection secret:

``` yaml
name: ${{mysql-secret}}
version: v1      
type: instance-secret
instance-secret:
  type: key-value-properties
  acl: rw
  data:
    connection-user: ${{user}}
    connection-password: ${{password}}
```
- Apply this YAML file on DataOS CLI

``` shell
dataos-ctl apply -f ${{path/instance_secret.yaml}}
```


For example, if a user wishes to create a MySQL Depot, they can define a Depot configuration file as follows:

<details>
<summary>YAML Configuration File</summary>

```yaml

name: mysql05
version: v1
type: depot
tags:
  - dropzone
  - mysql
layer: user
depot:
  type: MYSQL
  description: "MYSQL Sample data"
spec:
  host: ${{host}}
  port: ${{port}}
external: true
dataosSecrets:
  - name: depotsecret-r
    keys:
      - depotsecret-r

  - name: depotsecret-rw
    keys:
      - depotsecret-rw
```

By referencing the name of the Instance Secret, "mysql-secret," users can easily incorporate the specified credentials into their Depot configuration. This approach ensures the secure handling and sharing of sensitive information.

</details>

To learn more about Instance Secrets as a Resource and their usage, refer to the documentation [here](/resources/instance_secret/)

**Configure Spec Section**

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
    type: depot
    tags:
      - bigquery
    layer: user
    depot:
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

    Depot provides flexibility in mapping the hierarchy for file storage systems. Let's consider the example of an [Amazon S3](/resources/depot/depot_config_templates/amazon_s3.md) bucket, which has a flat structure consisting of buckets, folders, and objects. By understanding the hierarchy and utilizing the appropriate configurations, you can effectively map the structure to DataOS components.

    ![Bucket](./depot/create_depot_2.png)
    <center><i>Amazon S3 Bucket Structure</i></center>


    Here's an example of creating a depot named 's3depot' that maps the following structure:

    - Bucket: `abcdata` (Depot)
    - Folder: `transactions` (Collection)
    - Objects: `file1` and `file2` (Datasets)

    In the YAML configuration, specify the bucket name and the relative path to the folder. The manifest example below demonstrates how this can be achieved:

    ``` yaml
    name: s3depot
    version: v1
    type: depot
    tags:
      - S3
    layer: user
    depot:
      type: S3
      description: "AWS S3 Bucket for dummy data"
      external: true
      spec:
        bucket: "abcdata"
        relativePath:
    ```
    If you omit the `relativePath` in the manifest configuration, the bucket itself becomes the depot in DataOS. In this case, the following UDLs can be used to read the data:

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

    When configuring the manifets file for S3, if you include the `relativePath` as shown below, the 'transactions' folder is positioned as the depot:

    ``` yaml
    name: s3depot
    version: v1
    type: depot
    tags:
      - S3
    layer: user
    depot:
      type: S3
      description: "AWS S3 Bucket for dummy data"
      external: true
      spec:
        bucket: "abcdata"
        relativePath: "/transactions"
    ```    

    Since the folder ‘transactions’ in the bucket has now been positioned as the depot, two things happen.

    First, you cannot read the object files online-transaction and offline-transaction using this depot.

    Secondly with this setup, you can read the files within the 'transactions' folder using the following UDLs:

    - `dataos://s3depot:none/file1`
    - `dataos://s3depot:none/file2`

    <aside class="callout">
    🗣️ When writing data to a source system, names like 'none' or 'system' cannot be used for the collection. Therefore, the output of a Flare job cannot have an address like <code>dataos://${{depot name}}:none/${{dataset name}}</code> or <code>dataos://${{depot name}}:system/${{dataset name}}</code>.
    </aside>

=== "Kafka"

    For accessing data from [Kafka](https://dataos.info/resources/depot/depot_config_templates/kafka/), where the structure consists of a broker list and topics, the `spec` section in the YAML configuration will point the depot to the broker list, and the datasets will map to the topic list. The format of the manifest file will be as follows:
    ``` yaml
    depot:
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

### **Verify Depot Creation**

To ensure that your depot has been successfully created, you can verify it in two ways:

- Check the name of the newly created depot in the list of depots where you are named as the owner:

``` shell
dataos-ctl get -t depot
```

- Alternatively, retrieve the list of all depots created in your organization:

``` shell
dataos-ctl get -t depot -a
```

You can also access the details of any created Depot through the DataOS GUI in the [Operations App](/interfaces/operations/) and [Metis UI](/interfaces/metis/).

### **Delete Depot**

<aside class="callout">
📖 <strong>Best Practice:</strong> As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.
</aside>


If you need to delete a depot, use the following command in the DataOS CLI:

``` shell
dataos-ctl delete -t depot -n ${{name of depot}}
```


By executing the above command, the specified depot will be deleted from your DataOS environment.
