---
title: Lakehouse
search:
  boost: 2
---

# :resources-lakehouse: Lakehouse

Lakehouse is a [DataOS Resource](/resources/) that merges Apache Iceberg table format with cloud object storage, yielding a fully managed storage architecture that blends the strengths of data lakes and data warehouses. It enables a novel approach to system design, incorporating features typically found in data warehouses—such as the creation of tables with defined schemas, data manipulation using a variety of tools, and sophisticated data management capabilities—directly on top of cost-effective cloud storage in open formats.

<aside class="callout">

🗣️ The Lakehouse is designated as a <a href="/resources/types/#workspace-level-resources">Workspace-level</a> DataOS Resource. This classification enables the creation of separate Lakehouses within distinct Workspaces. 

</aside>


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **How to create and manage a Lakehouse?**

    ---

    Learn how to create and manage a Lakehouse in DataOS.

    [:octicons-arrow-right-24: Create and manage a Lakehouse](/resources/lakehouse/#how-to-create-and-manage-a-lakehouse)


-   :material-list-box-outline:{ .lg .middle } **How to configure the manifest file of Lakehouse?**

    ---

    Discover how to configure the manifest file of a Lakehouse by adjusting its attributes.

    [:octicons-arrow-right-24: Lakehouse attributes](/resources/lakehouse/configurations/)

-   :material-console:{ .lg .middle } **How to manage datasets in a Lakehouse?**

    ---

    Various CLI commands related to performing DDL/DML operations on datasets in a Lakehouse.
    
    [:octicons-arrow-right-24: Managing datasets in Lakehouse](/resources/lakehouse/command_reference/)

-   :material-content-duplicate:{ .lg .middle }  **How to use a Lakehouse in DataOS?**

    ---

    Explore examples showcasing the usage of Lakehouse Resource in various scenarios.
    
    [:octicons-arrow-right-24: Lakehouse usage recipes](/resources/lakehouse/#how-to-use-a-lakehouse-in-dataos)

</div>


## Key Features of a Lakehouse

The DataOS Lakehouse integrates essential features of Relational Data Warehouses with the scalability and adaptability of data lakes. Here's an outline of its core features:

- **Decoupled Storage from Compute**: The Lakehouse architecture decouples storage from computational resources, permitting independent scaling. This enables handling larger datasets and more simultaneous users efficiently.
- **ACID Transactions Support**: Essential for data integrity during simultaneous accesses, ACID transaction support ensures consistent and reliable data amidst concurrent operations.
- **Versatile Workload Management**: Designed to facilitate a range of tasks from analytics to machine learning, the Lakehouse serves as a unified repository, streamlining data management.
- **Flexible Computing Environments**: Supports a diverse array of cloud-native storage and processing environments, including DataOS native stacks like [Flare](/resources/stacks/flare/), [Soda](/resources/stacks/soda/), etc.
- **Openness and Standardization**: Embracing open file formats like Parquet ensures efficient data retrieval across various tools and platforms.
- **Branching Capabilities**: Employs Iceberg's branching features to support schema versioning and experimentation, enabling safe testing and iteration without affecting live data.

## Architecture of a Lakehouse

DataOS Lakehouse architecture comprises of several layers that come together to form a cohesive environment for data management. The layers are described below:

- **Storage**: Acts as the foundational storage layer, interfacing with the cloud storage services (e.g., GCS, ABFSS, WASBS, Amazon S3). It abstracts out the storage connection details by creating a [Depot](/resources/depot/) Resource on applying, while the credentials are securely referred using [Instance Secrets](/resources/instance_secret/). The Lakehouse storage, utilizes Parquet for efficiently handling large datasets, and employs the Iceberg format for table metadata management.
- **Metastore**: Facilitates access to metadata related to the stored data through the utilization of the Iceberg REST metastore. It exposes Iceberg catalogs, e.g. Hadoop and Hive, via REST metastore interfaces, thus facilitating metadata management.
- **Query Engine**: Provides the computing environment for running data queries and analytics. It supports the [Themis Query Engine](/resources/cluster/#themis) which is provisioned through the [Cluster Resource](/resources/cluster/).

Together, these layers come together to form the DataOS Lakehouse architecture, ensuring it not only serves as a repository for vast amounts of data but also as a powerful component for data analysis and insights.

## How to create and manage a Lakehouse?

### **Prerequisites**

Before proceeding with the Lakehouse creation, ensure the following prerequisites are met:

**Object Storage account**

Data developers need access to an object storage solution. Ensure you have the storage credentials ready with 'Storage Admin' access level. The following object storage solutions are supported:

- Azure Blob File System Storage (ABFSS)
- Windows Azure Storage Blob Service (WASBS)
- Amazon Simple Storage Service (Amazon S3)
- Google Cloud Storage (GCS)

**Access level permission**

To set up a Lakehouse in DataOS, besides possessing an object storage account with appropriate permissions, you also require specific tags or use-cases that authorize you to create and manage a Lakehouse within DataOS. 

<aside class="callout">
🗣 To acquire the necessary tags and use-cases, please contact the DataOS Operator in your organization.
</aside>

### **Creating a Lakehouse**

#### **Create Instance Secrets**

[Instance Secrets](/resources/instance_secret/) are vital for securely storing sensitive information like data source credentials. These Instance-secrets ensure that credentials are kept safe in the [Heimdall](/architecture/#heimdall) vault, making them accessible throughout the DataOS instance without exposing them directly in your Lakehouse manifest file. Here’s how you can create Instance-secrets:

**Steps to Create Instance Secrets**

- **Prepare the manifest file for Instance-secret:** You need to create a manifest file (YAML configuration file) that contains the source credentials for your chosen object storage solution ([ABFSS](/resources/instance_secret/#abfss), [WASBS](/resources/instance_secret/#wasbs), [Amazon S3](/resources/instance_secret/#s3), or [GCS](/resources/instance_secret/#gcs)). This file should also specify the level of access control (read-only ‘r’ or read-write ‘rw’) that the Lakehouse will have over the object storage. A sample Instance-secret manifest is provided below: 

    ???tip "Sample Instance Secret manifest file"
        
        ```yaml
        name: depotsecret-r # Resource name (mandatory)
        version: v1 # Manifest version (mandatory)
        type: instance-secret # Resource-type (mandatory)
        tags: # Tags (optional)
          - just for practice
        description: instance secret configuration # Description of Resource (optional)
        layer: user
        instance-secret: # Instance Secret mapping (mandatory)
          type: key-value-properties # Type of Instance-secret (mandatory)
          acl: r # Access control list (mandatory)
          data: # Data section mapping (mandatory)
            username: iamgroot
            password: yourpassword
        ```
        

    You can refer to the following link to get the [templates for the Instance-secret manifests for object stores](/resources/instance_secret/#object-store).

- **Applying the Manifest file using DataOS CLI:** Once your manifest file is ready, you can apply it using the [DataOS Command Line Interface (CLI)](/interfaces/cli/), by the following command:

    === "Command"
    
        ```shell
        dataos-ctl resource apply -f ${manifest-file-path} -w ${workspace}
        ```
    === "Example"

        ```shell
        dataos-ctl resource apply -f data_product/instance_secret.yaml -w curriculum
        ```
    
    Alternate command

    === "Command"

        ```shell
        dataos-ctl apply -f ${manifest-file-path} -w ${workspace}
        ```

    === "Example"

        ```shell
        dataos-ctl apply -f ../data_product/instance_secret.yaml -w curriculum
        ```

- **Verify Instance-secret creation:** To ensure that your Instance-secret has been successfully created, you can verify it in two ways:
    
    Check the name of the newly created Instance-secret in the list of Instance-secret created by you using the `resource get` command:
    
    ```shell
    dataos-ctl resource get -t instance-secret
    ```
    
    Alternatively, retrieve the list of all Instance-secret created by all users in a DataOS instance by appending `-a` flag:
    
    ```shell
    dataos-ctl resource get -t instance-secret -a
    ```
    
    You can also access the details of any created Instance-secret through the DataOS GUI in the Resource tab of the [Operations](/interfaces/operations/) app.
    

For more information about Instance-secret, refer to the documentation: [Instance-secret](/resources/instance_secret/).

#### **Draft a Lakehouse manifest file**

Once you have created Instance-secrets, now its time to create a Lakehouse by applying the Lakehouse manifest file using the [DataOS CLI](/interfaces/cli/). The Lakehouse manifest file is divided into several sections, each responsible for specifying different aspects of the Lakehouse. The sections are provided below:

- Resource meta section
- Lakehouse-specific section
    - Storage section
    - Metastore section
    - Query Engine section

A sample Lakehouse manifest file is provided below; the sections that make up the various parts of the manifest file are described after that.

???tip "Sample Lakehouse manifest file"

    ```yaml hl_lines="1-10 12-16 18-33 35-37 39-41"
    # Resource-meta section (1)
    name: alphaomega
    version: v1alpha
    type: lakehouse
    tags:
      - Iceberg
      - Azure
    description: Icebase depot of storage-type S3
    owner: iamgroot
    layer: user

    # Lakehouse-specific section (2)
    lakehouse:
      type: iceberg
      compute: runnable-default
      iceberg:

        # Storage section (3)
        storage:
          depotName: alphaomega
          type: s3
          s3:
            bucket: dataos-lakehouse   
            relativePath: /test
          secrets:
            - name: alphaomega-r
              keys:
                - alphaomega-r
              allkeys: true 
            - name: alphaomega-rw
              keys:
                - alphaomega-rw
              allkeys: true  
        
        # Metastore section (4)
        metastore:
          type: "iceberg-rest-catalog"
        
        # Query engine section (5)
        queryEngine:
          type: themis
    ```

    1.  **Resource meta section** within a manifest file comprises metadata attributes universally applicable to all [Resource-types](/resources/types_of_dataos_resources/). To learn more about how to configure attributes within this section, refer to the link: [Attributes of Resource meta section](/resources/manifest_attributes/).

    2.  **Lakehouse-specific section** within a manifest file comprises attributes specific to the Lakehouse Resource. This section is further subdivided into: Storage, Metastore, and Query Engine section. To learn more about how to configure attributes of Lakehouse-specific section, refer the link: [Attributes of Lakehouse-specific section](/resources/lakehouse/configurations/).

    3.  **Storage section** comprises attributes for storage configuration.

    4.  **Metastore section** comprises attributes for metastore configuration.

    5.  **Query Engine section** comprises attributes for query engine configuration.


**Resource meta section**

This section serves as the header of the manifest file, defining the overall characteristics of the Lakehouse Resource you wish to create. It includes attributes common to all [types of Resources](/resources/types/) in DataOS. These attributes help DataOS in identifying, categorizing, and managing the Resource within its ecosystem. The code block below describes the attributes of this section:

=== "Syntax"

    ```yaml
    # Resource-meta section
    name: ${resource-name} # mandatory
    version: v1alpha # mandatory
    type: lakehouse # optional
    tags: # optional
      - ${tag1}
      - ${tag2}
    description: ${description} # optional
    owner: ${userid-of-owner} # optional
    layer: user # optional
    ```

=== "Example"

    ```yaml
    # Resource-meta section
    name: lakehouse-s3 # mandatory
    version: v1alpha # mandatory
    type: lakehouse # mandatory
    tags: # optional
      - lakehouse
      - s3
    description: The manifest file for Lakehouse Resource # optional
    owner: iamgroot # optional
    layer: user # optional
    ```

Refer to the [Attributes of Resource meta section](/resources/manifest_attributes/) for more information about the various attributes in the Resource meta section.

**Lakehouse-specific section**

Following the Resource meta section, the Lakehouse-specific section contains configurations unique to the Lakehouse Resource. 

=== "Syntax"

    ```yaml
    lakehouse:
      type: ${lakehouse-type} # mandatory 
      compute: ${compute} # mandatory 
      runAsApiKey: ${dataos-apikey} # optional
      runAsUser: ${user-id} # optional
      iceberg: # mandatory
        storage: 
          # storage section attributes
        metaStore: 
          # metastore section attributes
        queryEngine: # 
          # query engine section attributes

    ```

=== "Example"

    ```yaml
    lakehouse:
      type: iceberg # mandatory 
      compute: query-default # mandatory 
      runAsApiKey: abcdefghijklmnopqrstuvwxyz # optional
      runAsUser: iamgroot # optional
      iceberg: # mandatory
        storage: 
          # storage section attributes
        metaStore:
          # metastore section attributes
        queryEngine:
          # query engine section attributes
    ```

<div style="text-align: center;" markdown="1">

| Attribute&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`lakehouse`](/resources/lakehouse/configurations/#lakehouse) | mapping | none | none | mandatory |
| [`type`](/resources/lakehouse/configurations/#type) | string | none | iceberg | mandatory |
| [`compute`](/resources/lakehouse/configurations/#compute) | string | none | valid query-type Compute Resource name  | mandatory |
| [`runAsApiKey`](/resources/lakehouse/configurations/#runasapikey) | mapping | api key of user applying the Lakehouse | any valid DataOS apikey | optional |
| [`runAsUser`](/resources/lakehouse/configurations/#runasuser) | string | user-id of owner | user-id of use-case assignee | optional |
| [`iceberg`](/resources/lakehouse/configurations/#iceberg) | mapping | none | none | mandatory |
| [`storage`](/resources/lakehouse/configurations/#storage) | mapping | none | valid storage configuration | mandatory |
| [`metaStore`](/resources/lakehouse/configurations/#metastore) | mapping | none | valid metastore configuration | optional |
| [`queryEngine`](/resources/lakehouse/configurations/#queryengine) | mapping | none | valid query engine configuration | optional |

</div>

This section is divided into three separate sections, each critical to the Lakehouse’s functionality: 

- Storage section
- Metastore section
- Query engine section

**Storage section**

This section of the Lakehouse manifest file specifies the connection to the underlying object storage solution (e.g., ABFSS, WASBS, Amazon S3, GCS). Instance-secrets enable the secure reference of sensitive data within the manifest. The Storage section's configurations facilitate the creation of a [Depot](/resources/depot/), abstracting the storage setup and ensuring secured data access in the object storage solution. This setup varies across different source systems, as detailed in the tabs below:

=== "ABFSS"

    To setup a Lakehouse on top of ABFSS source system, you need to configure the `storage` with `type: abfss`. The code block below elucidates the storage section configuration for 'ABFSS':

    === "Syntax"

        ```yaml
        storage:
          depotName: ${depot-name} # optional
          type: abfss # mandatory
          abfss: # optional
            account: ${abfss-account} # optional
            container: ${container} # optional
            endpointSuffix: ${endpoint-suffix}
            format: ${format} # optional
            icebergCatalogType: ${iceberg-catalog-type} # optional
            metastoreType: ${metastore-type} # optional
            metastoreUrl: ${metastore-url} # optional
            relativePath: ${relative-path} # optional
          secrets:
            - name: ${referred-secret-name} # mandatory
              workspace: ${secret-workspace} # optional 
              key: ${secret-key} # optional
              keys: # optional 
                - ${key1}
                - ${key2}
              allKeys: ${all-keys-or-not} # optional
              consumptionType: ${consumption-type} # optional
        ```

    === "Example"

        ```yaml
        storage:
          type: "abfss"
          abfss:
            depotName: abfsslakehouse
            account: abfssstorage
            container: lake01
            relativePath: "/dataos"
            format: ICEBERG
            endpointSuffix: dfs.core.windows.net
          secrets:
            - name: abfsslakehouse-rw
              keys:
                - abfsslakehouse-rw
              allkeys: true    
            - name: abfsslakehouse-r
              keys:
                - abfsslakehouse-r
              allkeys: true 
        ```
    The table below summarizes the attributes of 'abfss' storage configuration:
    <center>

    | Attribute&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`storage`](/resources/lakehouse/configurations/#storage) | mapping | none | none | mandatory |
    | [`depotName`](/resources/lakehouse/configurations/#depotname) | string | ${lakehouse-name}0<br>${workspace}0<br>storage | A valid string that matches<br> the regex pattern <br>`[a-z]([a-z0-9]*)`. Special <br>characters, except for<br> hyphens/dashes, are <br> not allowed. The maximum <br>length is 48 characters. | optional |
    | [`type`](/resources/lakehouse/configurations/#type_1) | string | none | abfss | mandatory |
    | [`abfss`](/resources/lakehouse/configurations/#abfss) | mapping | none | none | optional |
    | [`account`](/resources/lakehouse/configurations/#abfss) | string | none | valid ABFSS account | optional |
    | [`container`](/resources/lakehouse/configurations/#abfss) | string | none | valid container name | optional |
    | [`endpointSuffix`](/resources/lakehouse/configurations/#abfss) | string | none | valid endpoint suffix | optional |
    | [`format`](/resources/lakehouse/configurations/#abfss) | string | Iceberg | Iceberg | optional |
    | [`icebergCatalogType`](/resources/lakehouse/configurations/#abfss) | string | hadoop | hadoop, hive | optional |
    | [`metastoreType`](/resources/lakehouse/configurations/#abfss) | string | iceberg-rest-catalog | iceberg-rest-catalog | optional |
    | [`metastoreUrl`](/resources/lakehouse/configurations/#abfss) | string | none | valid URL | optional |
    | [`relativePath`](/resources/lakehouse/configurations/#abfss) | string | none | valid relative path | optional |
    | [`secret`](/resources/lakehouse/configurations/#secret) | mapping | none | none | mandatory |
    | [`name`](/resources/lakehouse/configurations/#name) | string | none | valid Secret name | mandatory |
    | [`workspace`](/resources/lakehouse/configurations/#workspace) | string | none | valid Workspace name and<br> must be less than '32'<br> chars and conform to<br> the following regex: <br>`[a-z]([-a-z0-9]*[a-z0-9])?` | optional |
    | [`key`](/resources/lakehouse/configurations/#key) | string | none | valid key | optional |
    | [`keys`](/resources/lakehouse/configurations/#keys) | list of strings | none | valid keys  | optional |
    | [`allKeys`](/resources/lakehouse/configurations/#allkeys) | boolean | false | true/false | optional |
    | [`consumptionType`](/resources/lakehouse/configurations/#consumptiontype) | string | envVars | envVars, propFile | optional |

    <i>Attributes of ABFSS storage configuration</i>

    </center>

=== "GCS"

    To setup a Lakehouse on top of GCS source system, you need to configure the `storage` with `type: gcs`. The code block below elucidates the storage section configuration for 'GCS':

    === "Syntax"

        ```yaml
        storage:
          depotName: ${depot-name} # optional
          type: gcs # mandatory
          gcs: # mandatory
            bucket: ${gcs-bucket} # mandatory
            format: ${format} # mandatory
            icebergCatalogType: ${iceberg-catalog-type} # optional
            metastoreType: ${metastore-type} # optional
            metastoreUrl: ${metastore-url} # optional
            relativePath: ${relative-path} # optional
          secrets:
            - name: ${referred-secret-name} # mandatory
              workspace: ${secret-workspace} # optional 
              key: ${secret-key} # optional
              keys: # optional 
                - ${key1}
                - ${key2}
              allKeys: ${all-keys-or-not} # optional
              consumptionType: ${consumption-type} # optional
        ```

    === "Example"

        ```yaml
        storage:
          depotName: gcslakehouse
          type: gcs
          gcs:
            bucket: gcsbucket
            relativePath: "/sanity"
            format: iceberg      
          secrets:
            - name: gcslakehouse-rw
              keys:
                - gcslakehouse-rw
              allkeys: true    
            - name: gcslakehouse-r
              keys:
                - gcslakehouse-r
              allkeys: true 
        ```

    The table below summarizes the attributes of 'gcs' storage configuration:
    <center>

    | Attribute&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`storage`](/resources/lakehouse/configurations/#storage) | mapping | none | none | mandatory |
    | [`depotName`](/resources/lakehouse/configurations/#depotname) | string | ${lakehouse-name}0<br>${workspace}0<br>storage | A valid string that matches<br> the regex pattern <br>`[a-z]([a-z0-9]*)`. Special <br>characters, except for<br> hyphens/dashes, are <br> not allowed. The maximum <br>length is 48 characters. | optional |
    | [`type`](/resources/lakehouse/configurations/#type) | string | none | gcs | mandatory |
    | [`gcs`](/resources/lakehouse/configurations/#gcs) | mapping | none | none | optional |
    | [`bucket`](/resources/lakehouse/configurations/#gcs) | string | none | valid GCS bucket name | optional |
    | [`format`](/resources/lakehouse/configurations/#gcs) | string | Iceberg | Iceberg | optional |
    | [`icebergCatalogType`](/resources/lakehouse/configurations/#gcs) | string | none | hadoop, hive | optional |
    | [`metastoreType`](/resources/lakehouse/configurations/#gcs) | string | iceberg-rest-catalog | iceberg-rest-catalog | optional |
    | [`metastoreUrl`](/resources/lakehouse/configurations/#gcs) | string | none | valid metastore URL | optional |
    | [`relativePath`](/resources/lakehouse/configurations/#gcs) | string | none | valid relative path | optional |
    | [`secret`](/resources/lakehouse/configurations/#secret) | mapping | none | none | mandatory |
    | [`name`](/resources/lakehouse/configurations/#name) | string | none | valid Secret name | mandatory |
    | [`workspace`](/resources/lakehouse/configurations/#workspace) | string | none | valid Workspace name and<br> must be less than '32'<br> chars and conform to<br> the following regex: <br>`[a-z]([-a-z0-9]*[a-z0-9])?` | optional |
    | [`key`](/resources/lakehouse/configurations/#key) | string | none | valid key | optional |
    | [`keys`](/resources/lakehouse/configurations/#keys) | list of strings | none | valid keys  | optional |
    | [`allKeys`](/resources/lakehouse/configurations/#allkeys) | boolean | false | true/false | optional |
    | [`consumptionType`](/resources/lakehouse/configurations/#consumptiontype) | string | envVars | envVars, propFile | optional |

    <i>Attributes of GCS storage configuration</i>

    </center>

=== "S3"

    To setup a Lakehouse on top of S3 source system, you need to configure the `storage` with `type: s3`. The code block below elucidates the storage section configuration for 'S3':

    === "Syntax"

        ```yaml
        storage:
          depotName: ${depot-name} # optional
          type: s3 # mandatory
          s3: # mandatory
            bucket: ${s3-bucket} # mandatory
            format: ${format} # mandatory
            icebergCatalogType: ${iceberg-catalog-type} # optional
            metastoreType: ${metastore-type} # optional
            metastoreUrl: ${metastore-url} # optional
            relativePath: ${relative-path} # optional
            scheme: ${scheme} # optional
          secrets:
            - name: ${referred-secret-name} # mandatory
              workspace: ${secret-workspace} # optional 
              key: ${secret-key} # optional
              keys: # optional 
                - ${key1}
                - ${key2}
              allKeys: ${all-keys-or-not} # optional
              consumptionType: ${consumption-type} # optional
        ``` 

    === "Example"

        ```yaml
        storage:
          depotName: s3test
          type: "s3"
          s3:
            bucket: lake001-dev        # "tmdc-dataos-testing"
            relativePath: /sanitys3       
          secrets:
            - name: s3test-rw
              keys:
                - s3test-rw
              allkeys: true    
            - name: s3test-r
              keys:
                - s3test-r
              allkeys: true 
        ``` 

    The table below summarizes the attributes of 's3' storage configuration:
    <center>

    | Attribute&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`storage`](/resources/lakehouse/configurations/#storage) | mapping | none | none | mandatory |
    | [`depotName`](/resources/lakehouse/configurations/#depotname) | string | ${lakehouse-name}0<br>${workspace}0<br>storage | A valid string that matches<br> the regex pattern <br>`[a-z]([a-z0-9]*)`. Special <br>characters, except for<br> hyphens/dashes, are <br> not allowed. The maximum <br>length is 48 characters. | optional |
    | [`type`](/resources/lakehouse/configurations/#type) | string | none | s3 | mandatory |
    | [`s3`](/resources/lakehouse/configurations/#s3) | mapping | none | none | optional |
    | [`bucket`](/resources/lakehouse/configurations/#s3) | string | none | valid S3 bucket name | optional |
    | [`format`](/resources/lakehouse/configurations/#s3) | string | Iceberg | Iceberg | optional |
    | [`icebergCatalogType`](/resources/lakehouse/configurations/#s3) | string | none | hadoop, hive | optional |
    | [`metastoreType`](/resources/lakehouse/configurations/#s3) | string | iceberg-rest-catalog | iceberg-rest-catalog | optional |
    | [`metastoreUrl`](/resources/lakehouse/configurations/#s3) | string | none | valid URL | optional |
    | [`relativePath`](/resources/lakehouse/configurations/#s3) | string | none | valid relative path | optional |
    | [`scheme`](/resources/lakehouse/configurations/#s3) | string | none | valid scheme (e.g., s3://) | optional |
    | [`secret`](/resources/lakehouse/configurations/#secret) | mapping | none | none | mandatory |
    | [`name`](/resources/lakehouse/configurations/#name) | string | none | valid Secret name | mandatory |
    | [`workspace`](/resources/lakehouse/configurations/#workspace) | string | none | valid Workspace name and<br> must be less than '32'<br> chars and conform to<br> the following regex: <br>`[a-z]([-a-z0-9]*[a-z0-9])?` | optional |
    | [`key`](/resources/lakehouse/configurations/#key) | string | none | valid key | optional |
    | [`keys`](/resources/lakehouse/configurations/#keys) | list of strings | none | valid keys  | optional |
    | [`allKeys`](/resources/lakehouse/configurations/#allkeys) | boolean | false | true/false | optional |
    | [`consumptionType`](/resources/lakehouse/configurations/#consumptiontype) | string | envVars | envVars, propFile | optional |

    <i>Attributes of S3 storage configuration</i>

    </center>

=== "WASBS"

    To setup a Lakehouse on top of WASBS source system, you need to configure the `storage` with `type: wasbs`. The code block below elucidates the storage section configuration for 'WASBS':

    === "Syntax"

        ```yaml
        storage:
          depotName: ${depot-name} # optional
          type: wasbs # mandatory
          wasbs: # optional
            account: ${abfss-account} # optional
            container: ${container} # optional
            endpointSuffix: ${endpoint-suffix}
            format: ${format} # optional
            icebergCatalogType: ${iceberg-catalog-type} # optional
            metastoreType: ${metastore-type} # optional
            metastoreUrl: ${metastore-url} # optional
            relativePath: ${relative-path} # optional
          secrets:
            - name: ${referred-secret-name} # mandatory
              workspace: ${secret-workspace} # optional 
              key: ${secret-key} # optional
              keys: # optional 
                - ${key1}
                - ${key2}
              allKeys: ${all-keys-or-not} # optional
              consumptionType: ${consumption-type} # optional
        ```

    === "Example"

        ```yaml
        storage:
          type: "wasbs"
          wasbs:
            depotName: wasbslakehouse
            account: wasbsstorage
            container: lake01
            relativePath: "/dataos"
            format: ICEBERG
            endpointSuffix: dfs.core.windows.net
          secrets:
            - name: wasbslakehouse-rw
              keys:
                - wasbslakehouse-rw
              allkeys: true    
            - name: wasbslakehouse-r
              keys:
                - wasbslakehouse-r
              allkeys: true 
        ```
    The table below summarizes the attributes of 'wasbs' storage configuration:
    <center>

    | Attribute&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`storage`](/resources/lakehouse/configurations/#storage) | mapping | none | none | mandatory |
    | [`depotName`](/resources/lakehouse/configurations/#depotname) | string | ${lakehouse-name}0<br>${workspace}0<br>storage | A valid string that matches<br> the regex pattern <br>`[a-z]([a-z0-9]*)`. Special <br>characters, except for<br> hyphens/dashes, are <br> not allowed. The maximum <br>length is 48 characters. | optional |
    | [`type`](/resources/lakehouse/configurations/#type) | string | none | wasbs | mandatory |
    | [`wasbs`](/resources/lakehouse/configurations/#abfss) | mapping | none | none | optional |
    | [`account`](/resources/lakehouse/configurations/#abfss) | string | none | valid ABFSS account | optional |
    | [`container`](/resources/lakehouse/configurations/#abfss) | string | none | valid container name | optional |
    | [`endpointSuffix`](/resources/lakehouse/configurations/#abfss) | string | none | valid endpoint suffix | optional |
    | [`format`](/resources/lakehouse/configurations/#abfss) | string | Iceberg | Iceberg | optional |
    | [`icebergCatalogType`](/resources/lakehouse/configurations/#abfss) | string | hadoop | hadoop, hive | optional |
    | [`metastoreType`](/resources/lakehouse/configurations/#abfss) | string | iceberg-rest-catalog | iceberg-rest-catalog | optional |
    | [`metastoreUrl`](/resources/lakehouse/configurations/#abfss) | string | none | valid URL | optional |
    | [`relativePath`](/resources/lakehouse/configurations/#abfss) | string | none | valid relative path | optional |
    | [`secret`](/resources/lakehouse/configurations/#secret) | mapping | none | none | mandatory |
    | [`name`](/resources/lakehouse/configurations/#name) | string | none | valid Secret name | mandatory |
    | [`workspace`](/resources/lakehouse/configurations/#workspace) | string | none | valid Workspace name and<br> must be less than '32'<br> chars and conform to<br> the following regex: <br>`[a-z]([-a-z0-9]*[a-z0-9])?` | optional |
    | [`key`](/resources/lakehouse/configurations/#key) | string | none | valid key | optional |
    | [`keys`](/resources/lakehouse/configurations/#keys) | list of strings | none | valid keys  | optional |
    | [`allKeys`](/resources/lakehouse/configurations/#allkeys) | boolean | false | true/false | optional |
    | [`consumptionType`](/resources/lakehouse/configurations/#consumptiontype) | string | envVars | envVars, propFile | optional |

    <i>Attributes of WASBS storage configuration</i>

    </center>

**Metastore section**

This section outlines the metastore configuration, which manages metadata for the data stored in the Lakehouse storage. It includes the metastore service type and detailed setup instructions.

Configurations range from simple, requiring just the metastore type (e.g., `iceberg-rest-catalog`), to complex, incorporating additional features for enhanced scalability and performance. Advanced configurations may detail the number of replicas, autoscaling capabilities, and specific resource allocations.

=== "Basic configuration"

    === "Syntax"

        ```yaml
        lakehouse:
          metastore:
            type: ${metasatore-type}
        ```
    === "Example"

        ```yaml
        lakehouse:
          metastore:
            type: iceberg-rest-catalog
        ```

    The table below elucidates the basic configuration attributes of Metastore section:

    <center>

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`metastore`](/resources/lakehouse/configurations/#metastore) | mapping | none | none | optional |
    | [`type`](/resources/lakehouse/configurations/#type) | string | none | iceberg-rest-catalog | mandatory |

    <i>Basic configuration attributes of Metastore section</i>
    </center>


=== "Advanced configuration"

    === "Syntax"

        ```yaml
        metastore:
          type: ${metastore-type} # mandatory
          replicas: ${number-of-replicas}
          autoScaling:
            enabled: ${enable-autoscaling}
            minReplicas: ${minimum-number-of-replicas}
            maxReplicas: ${maximum-number-of-replicas}
            targetMemoryUtilizationPercentage: ${target-memory-utilization-percentage}
            targetCPUUtilizationPercentage: ${target-cpu-utilization-percentage}
          resources:
            requests:
              cpu: ${requested-cpu-resource}
              memory: ${requested-memory-resource}
            limits:
              cpu: ${requested-cpu-resource}
              memory: ${requested-memory-resource}
        ```

    === "Example"

        ```yaml
        metastore:
          type: iceberg-rest-catalog # mandatory
          replicas: 2
          autoScaling:
            enabled: true
            minReplicas: 2
            maxReplicas: 4
            targetMemoryUtilizationPercentage: 60
            targetCPUUtilizationPercentage: 60
          resources:
            requests:
              cpu: 1Gi
              memory: 400m
            limits:
              cpu: 2Gi
              memory: 1000m
        ```

    The table below elucidates the basic configuration attributes of Metastore section:

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`metastore`](/resources/lakehouse/configurations/#metastore) | mapping | none | none | optional |
    | [`type`](/resources/lakehouse/configurations/#type_2) | string | none | iceberg-rest-catalog | mandatory |
    | [`replicas`](/resources/lakehouse/configurations/#replicas) | integer | none | any valid positive integer | optional |
    | [`autoscaling`](/resources/lakehouse/configurations/#autoscaling) | mapping | none | none | optional |
    | [`enabled`](/resources/lakehouse/configurations/#enabled) | boolean | false | true/false | optional |
    | [`minReplicas`](/resources/lakehouse/configurations/#minreplicas) | integer | none | any valid integer | optional |
    | [`maxReplicas`](/resources/lakehouse/configurations/#maxreplicas) | integer | none | any valid integer greater than `minReplicas` | optional |
    | [`targetMemoryUtilizationPercentage`](/resources/lakehouse/configurations/#targetmemoryutilizationpercentage) | integer | none | any valid percentage | optional |
    | [`targetCPUUtilizationPercentage`](/resources/lakehouse/configurations/#targetcpuutilizationpercentage) | integer | none | any valid percentage | optional |
    | [`resources`](/resources/lakehouse/configurations/#resources) | mapping | none | none | optional |
    | [`requests`](/resources/lakehouse/configurations/#requests) | mapping | none | none | optional |
    | [`limits`](/resources/lakehouse/configurations/#limits) | mapping | none | none | optional |
    | [`cpu`](/resources/lakehouse/configurations/#cpu) | string | none | any valid resource amount | optional |
    | [`memory`](/resources/lakehouse/configurations/#memory) | string | none | any valid resource amount | optional |

    <i>Advanced configuration attributes of Metastore section</i>
    </center>

**Query Engine section**

The query engine section facilitates the creation of a [Cluster Resource](/resources/cluster/), enabling data queries against the Lakehouse storage. Currently, only the [Themis query engine](/resources/cluster/#themis) is supported.

Basic configurations might be adequate for standard use cases, outlining merely the type of query engine. For environments demanding more precise resource management, advanced configurations offer customization options, including specific CPU and memory requests and limits, to ensure the query engine operates efficiently within set resource constraints.


=== "Basic configuration"

    === "Syntax"

        ```yaml
        queryEngine:
          type: ${query-engine-type}
        ```
    === "Example"

        ```yaml
        queryEngine:
          type: themis
        ```

    The table below elucidates the basic configuration attributes of Metastore section:

    <center>

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`queryEngine`](/resources/lakehouse/configurations/#queryengine) | mapping | none | none | optional |
    | [`type`](/resources/lakehouse/configurations/#type) | string | none | themis | mandatory |

    <i>Basic configuration attributes of Query Engine section</i>
    </center>


=== "Advanced configuration"

    === "Syntax"

        ```yaml
        queryEngine:
          type: ${query-engine-type} # mandatory
          resources:
            requests:
              cpu: ${requested-cpu-resource}
              memory: ${requested-memory-resource}
            limits:
              cpu: ${requested-cpu-resource}
              memory: ${requested-memory-resource}
          themis:
            envs:
              ${environment-variables}
            themisConf:
              ${themis-configuration}
            spark:
              driver: 
                resources:
                  requests:
                    cpu: ${requested-cpu-resource}
                    memory: ${requested-memory-resource}
                  limits:
                    cpu: ${requested-cpu-resource}
                    memory: ${requested-memory-resource}
                instanceCount: ${instance-count} # mandatory
                maxInstanceCount: ${max-instance-count} # mandatory
              executor:
                resources:
                  requests:
                    cpu: ${requested-cpu-resource}
                    memory: ${requested-memory-resource}
                  limits:
                    cpu: ${requested-cpu-resource}
                    memory: ${requested-memory-resource}
                instanceCount: ${instance-count} # mandatory
                maxInstanceCount: ${max-instance-count} # mandatory
              sparkConf:
                ${spark-configuration}
          storageAcl: ${storage-acl} # mandatory
        ```

    === "Example"

        ```yaml
        queryEngine:
          type: themis # mandatory
          resources:
            requests:
              cpu: 1000m
              memory: 2Gi
            limits:
              cpu: 2000m
              memory: 4Gi
          themis:
            envs:
              alpha: beta
            themisConf:
              "kyuubi.frontend.thrift.binary.bind.host": "0.0.0.0"
              "kyuubi.frontend.thrift.binary.bind.port": "10101"
            spark:
              driver: 
                resources:
                  requests:
                    cpu: 1Gi
                    memory: 400m
                  limits:
                    cpu: 2Gi
                    memory: 1000m
                instanceCount: 2 # mandatory
                maxInstanceCount: 3 # mandatory
              executor:
                resources:
                  requests:
                    cpu: 1Gi
                    memory: 400m
                  limits:
                    cpu: 2Gi
                    memory: 1000m
                instanceCount: 2 # mandatory
                maxInstanceCount: 3 # mandatory
              sparkConf:
                spark.dynamicAllocation.enabled: true
          storageAcl: r # mandatory
        ```

    The table below elucidates the advanced configuration attributes of Query Engine section:

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`queryEngine`](/resources/lakehouse/configurations/#queryengine) | mapping | none | none | mandatory |
    | [`type`](/resources/lakehouse/configurations/#type) | string | none | themis | mandatory |
    | [`resources`](/resources/lakehouse/configurations/#resources) | mapping | none | none | optional |
    | [`requests`](/resources/lakehouse/configurations/#requests) | mapping | none | none | optional |
    | [`cpu`](/resources/lakehouse/configurations/#cpu) | string | none | any valid CPU resource amount | optional |
    | [`memory`](/resources/lakehouse/configurations/#memory) | string | none | any valid memory resource amount | optional |
    | [`limits`](/resources/lakehouse/configurations/#limits) | mapping | none | none | optional |
    | [`cpu`](/resources/lakehouse/configurations/#cpu) | string | none | any valid CPU resource limit | optional |
    | [`memory`](/resources/lakehouse/configurations/#memory) | string | none | any valid memory resource limit | optional |
    | [`themis`](/resources/lakehouse/configurations/#themis) | mapping | none | none | optional |
    | [`envs`](/resources/lakehouse/configurations/#envs) | mapping | none | none | optional |
    | [`themisConf`](/resources/lakehouse/configurations/#themisconf) | mapping | none | none | optional |
    | [`spark`](/resources/lakehouse/configurations/#spark) | mapping | none | none | mandatory |
    | [`driver`](/resources/lakehouse/configurations/#driver) | mapping | none | none | mandatory |
    | [`memory`](/resources/lakehouse/configurations/#memory) | string | none | any valid memory amount | mandatory |
    | [`cpu`](/resources/lakehouse/configurations/#cpu) | string | none | any valid CPU resource | mandatory |
    | [`executor`](/resources/lakehouse/configurations/#executor) | mapping | none | none | mandatory |
    | [`memory`](/resources/lakehouse/configurations/#memory) | string | none | any valid memory amount | mandatory |
    | [`cpu`](/resources/lakehouse/configurations/#cpu) | string | none | any valid CPU resource | mandatory |
    | [`instanceCount`](/resources/lakehouse/configurations/#instancecount) | integer | none | any valid integer | mandatory |
    | [`maxInstanceCount`](/resources/lakehouse/configurations/#maxinstancecount) | integer | none | any valid integer | mandatory |
    | [`sparkConf`](/resources/lakehouse/configurations/#sparkconf) | mapping | none | none | optional |

    <i>Advanced configuration attributes of Query Engine section</i>
    </center>

#### **Apply the Lakehouse manifest**

After creating the manifest file for the Lakehouse Resource, it's time to apply it to instantiate the Resource-instance in the DataOS environment. To apply the Lakehouse manifest file, utilize the [`apply`](/interfaces/cli/command_reference/#apply) command.

=== "Command"

    ```shell
    dataos-ctl apply -f ${manifest-file-path} - w ${workspace}
    ```

=== "Example"

    ```shell
    dataos-ctl apply -f dataproducts/new-lakehouse.yaml -w curriculum
    ```

The links provided below showcase the process of creating Lakehouse for a particular data source:

- [How to create a Lakehouse on ABFSS data source?](/resources/lakehouse/usage_examples/how_to_create_a_lakehouse_on_abfss_data_source/)
- [How to create a Lakehouse on WASBS data source?](/resources/lakehouse/usage_examples/how_to_create_a_lakehouse_on_wasbs_data_source/)
- [How to create a Lakehouse on S3 data source?](/resources/lakehouse/usage_examples/how_to_create_a_lakehouse_on_s3_data_source/)
- [How to create a Lakehouse on GCS data source?](/resources/lakehouse/usage_examples/how_to_create_a_lakehouse_on_gcs_data_source/)

### **Managing a Lakehouse**

#### **Verify Lakehouse Creation**

To ensure that your Lakehouse has been successfully created, you can verify it in two ways:

Check the name of the newly created Lakehouse in the list of lakehouses created by you in a particular Workspace:

```shell
dataos-ctl get -t lakehouse - w ${workspace name}
```

Sample

```shell
dataos-ctl get -t lakehouse -w curriculum
```

Alternatively, retrieve the list of all Lakehouses created in the Workspace by appending `-a` flag:

```shell
dataos-ctl get -t lakehouse -w ${workspace name} -a
# Sample
dataos-ctl get -t lakehouse -w curriculum
```

You can also access the details of any created Lakehouse through the DataOS GUI in the Resource tab of the  [Operations](/interfaces/operations/) app.

#### **Deleting a Lakehouse**

Use the [`delete`](/interfaces/cli/command_reference/#delete) command to remove the specific Lakehouse Resource Instance from the DataOS environment. As shown below, there are three ways to delete a Lakehouse.

**Method 1:** Copy the Lakehouse name, version, Resource-type and Workspace name from the output of the [`get`](/interfaces/cli/command_reference/#get) command seperated by '|' enclosed within quotes and use it as a string in the delete command.

Command

```shell
dataos-ctl delete -i "${identifier string}"
```

Example

```shell
dataos-ctl delete -i "cnt-lakehouse-demo-01 | v1alpha | lakehouse | public"
```

Output

```shell
INFO[0000] 🗑 delete...
INFO[0001] 🗑 deleting(public) cnt-lakehouse-demo-01:v1alpha:lakehouse...
INFO[0003] 🗑 deleting(public) cnt-lakehouse-demo-01:v1alpha:lakehouse...deleted
INFO[0003] 🗑 delete...complete
```

**Method 2:** Specify the path of the YAML file and use the [`delete`](/interfaces/cli/command_reference/#delete) command.

Command

```shell
dataos-ctl delete -f ${manifest-file-path}
```

Example

```bash
dataos-ctl delete -f /home/desktop/connect-city/config_v1alpha.yaml
```

Output

```bash
INFO[0000] 🗑 delete...
INFO[0000] 🗑 deleting(public) cnt-lakehouse-demo-010:v1alpha:lakehouse...
INFO[0001] 🗑 deleting(public) cnt-lakehouse-demo-010:v1alpha:lakehouse...deleted
INFO[0001] 🗑 delete...complete
```

**Method 3:** Specify the Workspace, Resource-type, and Lakehouse name in the [`delete`](/interfaces/cli/command_reference/#delete) command.

Command

```shell
dataos-ctl delete -w ${workspace} -t lakehouse -n ${lakehouse name}
```

Example

```shell
dataos-ctl delete -w public -t lakehouse -n cnt-product-demo-01
```

Output

```shell
INFO[0000] 🗑 delete...
INFO[0000] 🗑 deleting(public) cnt-city-demo-010:v1alpha:lakehouse...
INFO[0001] 🗑 deleting(public) cnt-city-demo-010:v1alpha:lakehouse...deleted
INFO[0001] 🗑 delete...complete
```

## How to configure the manifest file of Lakehouse?

The Attributes of Lakehouse manifest define the key properties and configurations that can be used to specify and customize Lakehouse Resources within a manifest file. These attributes allow data developers to define the structure and behavior of their Lakehouse Resources. For comprehensive information on each attribute and its usage, please refer to the link: [Attributes of Lakehouse manifest](/resources/lakehouse/configurations/).

## How to manage Lakehouse Resource and datasets using CLI?

This section provides a comprehensive guide for managing Lakehouse Resource and inspecting datasets stored in Lakehouse storage. Utilizing the `dataset` command, users can perform a wide array of Data Definition Language (DDL)-related tasks, streamlining operations such as adding or removing columns, editing dataset metadata, and listing snapshots, among others. To learn more about these commands, refer to the link: [Lakehouse Command Reference](/resources/lakehouse/command_reference/).

## How to use a Lakehouse in DataOS?

- [How to ensure high data quality in Lakehouse Storage using the Write-Audit-Publish pattern?](/resources/lakehouse/usage_examples/write_audit_publish_pattern_in_lakehouse_storage/)
- [Iceberg Metadata Tables in Lakehouse](/resources/lakehouse/iceberg_metadata_tables/)
- [How to use Iceberg metadata tables to extract insights in Lakehouse storage?](/resources/lakehouse/using_metadata_tables_to_extract_insights_in_lakehouse/)
- [How to create, fetch, and drop dataset in a Lakehouse using CLI commands?](/resources/lakehouse/command_reference/case_scenario_create_fetch_and_drop_dataset/)
- [How to perform Iceberg dataset maintainence in a Lakehouse using CLI commands?](/resources/lakehouse/command_reference/case_scenario_maintenance/)
- [How to perform partitioning on Lakehouse datasets using CLI commands?](/resources/lakehouse/command_reference/case_scenario_partitioning/)
- [How to perform schema evolution on Lakehouse datasets using CLI commands?](/resources/lakehouse/command_reference/case_scenario_schema_evolution/)
- [How to manipulate table properties of Lakehouse datasets using CLI commands?](/resources/lakehouse/command_reference/case_scenario_table_properties/)