
![Lakehouse Icon](/resources/lakehouse/lakehouse_icon.svg){ align=left }

# Lakehouse

Lakehouse, is a [DataOS Resource](/resources/) that integrates Apache Iceberg table format and cloud object storage to provide a fully managed storage solution. It emulates traditional data warehouses, enabling table creation with defined schemas, data manipulation via various tools, and data access regulation through the DataOS Governance engine, [Heimdall](/architecture/#heimdall).

<aside class="callout">

🗣️ Unlike traditional object storage or Data Lake depots that are instantiated at the <a href="/resources/types_of_dataos_resources/#instance-level-resources">Instance-level</a>, Lakehouses are created at the <a href="/resources/types_of_dataos_resources/#workspace-level-resources">Workspace-level</a>.

</aside>


<div class="grid cards" markdown>

-   :material-format-list-bulleted-type:{ .lg .middle } **Key Features of a Lakehouse**

    ---

    DataOS Lakehouse adds several Relational Data Warehouse-like features to your existing data lakes.

    [:octicons-arrow-right-24: Key features](#key-features-of-a-lakehouse)


-   :material-clock-fast:{ .lg .middle } **Structure of a Lakehouse manifest**

    ---

    A Lakehouse manifest file includes multiple sections with attributes that must be configured for creating a Lakehouse instance.

    [:octicons-arrow-right-24: Structure](#structure-of-a-lakehouse-manifest)

-   :material-clock-fast:{ .lg .middle } **How to setup a Lakehouse?**

    ---

    Create a new Lakehouse with your existing object storage and get up and running in minutes.

    [:octicons-arrow-right-24: Getting started](#how-to-create-a-lakehouse)

-   :material-script-text-outline:{ .lg .middle } **How to configure a Lakehouse manifest file?**

    ---

    The Lakehouse Resource manifest file offers several configurable attributes that could be configured for various use-cases.

    [:octicons-arrow-right-24:  Lakehouse attributes](/lakehouse/manifest_attributes/)

-   :material-console:{ .lg .middle } **How to manage datasets in a Lakehouse?**

    ---

    Various CLI commands related to performing DDL/DML operations on datasets in a Lakehouse.
    
    [:octicons-arrow-right-24:  Command reference](/lakehouse/command_reference/)

-   :material-console:{ .lg .middle } **Case Scenarios**

    ---

    Learn how to accompolish a specific task in a Lakehouse.
    
    [:octicons-arrow-right-24:  Case scenarios](/lakehouse/#case-scenario/)

</div>


## Key Features of a Lakehouse

DataOS Lakehouse adds several Relational Data Warehouse-like featueres to a data lake. This section will walk you through some of them.

**Managed Storage**

DataOS Lakehouse offers a fully managed storage solution. It utilizes Apache Iceberg tables and cloud object storage, mimicking traditional warehouse functionalities.

**Computing Environment Flexibility**

Supports a multitude of computing environments for cloud-native storage. Users can deploy various processing engines, including DataOS native stacks such as [Flare](/resources/stacks/flare/), [Soda](/resources/stacks/soda/), etc.

**Apache Iceberg Integration**

Incorporates a hosted implementation of Apache Iceberg REST catalog, facilitating interaction with DataOS Lakehouse through Iceberg REST catalog API.

## Structure of a Lakehouse manifest

```yaml hl_lines="1-10 12-16 18-32 34-36 38-40"
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

    # Storage configuration (3)
    storage:
      type: s3
      s3:
        bucket: dataos-lakehouse   
        relativePath: /test
      secrets:
        - name: alphaomega0public0storage-r
          keys:
            - alphaomega0public0storage-r
          allkeys: true 
        - name: alphaomega0public0storage-rw
          keys:
            - alphaomega0public0storage-rw
          allkeys: true  
    
    # Metastore configuration (4)
    metastore:
      type: "iceberg-rest-catalog"
    
    # Query engine configuration (5)
    queryEngine:
      type: themis
```


1.  **Resource meta section** within a manifest file comprises metadata attributes universally applicable to all [Resource-types](/resources/types_of_dataos_resources/). To learn more about how to configure attributes within this section, refer to the link: [Attributes of Resource meta section](/resources/resource_attributes/).

2.  **Lakehouse-specific section** within a manifest file comprises attributes specific to the Lakehouse Resource. This section is further subdivided into: Storage, Metastore, and Query Engine section. To learn more about how to configure attributes of Lakehouse-specific section, refer the link: [Attributes of Lakehouse-specific section](/resources/lakehouse/manifest_attributes/).

3.  **Storage configuration**

4.  **Metastore configuration**

5.  **Query Engine configuration**


## How to create a Lakehouse?

Data developers can create a Lakehouse Resource by creating a YAML manifest and applying it via the DataOS [CLI](/interfaces/cli/).

### **Prerequisites**

#### **Object Storage account**

To successfully create a Lakehouse, data developers need access to an object storage solution. It's essential to have the storage credentials and define the access level—either read or read-write—based on your specific requirements. Supported object storage solutions include:

- Azure Blob File System Storage (ABFSS)
- Windows Azure Storage Blob Service (WASBS)
- Amazon Simple Storage Service (Amazon S3)
- Google Cloud Storage (GCS)

#### **Get an Operator tag**

Setting up a Lakehouse instance involves setting up [Cluster](/resources/cluster/) in the hindsight which requires the `roles:id:operator` tag. 

#### **Create Instance Secrets**

Instance-secrets allow data developers to securely store critical information, including data source credentials and other sensitive data, in the Heimdall vault for accessibility throughout the entire DataOS instance. To create an instance-secret, data developers must create an Instance-secret manifest and deploy it using the DataOS CLI.

**Instance-secret manifest file**

The Instance-secret manifest file must include the data source credentials for one of the supported object storage solutions (ABFSS, WASBS, Amazon S3, or GCS), along with the appropriate level of access control configuration (r or rw). 

The configuration of the manifest file will differ based on the storage solution and the access level determined for your use case. The variations for these configurations are detailed below

<div class="grid" markdown>

=== "ABFSS"

    To create an instance-secret for securely accessing ABFSS, the following details are required:

      - `${abfss-depot-name}`: Define the name of your ABFSS depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing and the `acl`(access control list) is `rw`, then the instance secret name will be `alpha0testing0storage`.
      - `${description}`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
      - `${azure-endpoint-suffix}`: The endpoint suffix for your Azure storage account, which varies by cloud environment. 
      - `${azure-storage-account-key}`: The access key for your Azure storage account. This key is essential for authentication and must be kept secure.
      - `${azure-storage-account-name}`: The name of your Azure storage account. This name is used in conjunction with the endpoint suffix to form the base URL for your ABFSS resources.
    
    Ensure that you replace each placeholder (e.g., `${abfss-depot-name}`, `${azure-endpoint-suffix}`) with the actual values pertaining to your Azure account and ABFSS configuration. 

    === "Read-only instance-secret"
        ```yaml title="instance_secret_abfss_read.yaml"
        --8<-- "examples/resources/lakehouse/abfss/resource_instance_secret_abfss_read.yaml"
        ```
    === "Read-write instance-secret"
        ```yaml title="instance_secret_abfss_read_write.yaml"
        --8<-- "examples/resources/lakehouse/abfss/resource_instance_secret_abfss_read_write.yaml"
        ```

=== "WASBS"

    To create an instance-secret for securely accessing WASBS, the following details are required:

      - `${wasbs-depot-name}`: Define the name of your WASBS depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing, then the `${gcs-depot-name}` will be alpha0testing0storage.
      - `${description}`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
      - `${azure-endpoint-suffix}`: The endpoint suffix for your Azure storage account, which varies by cloud environment. 
      - `${azure-storage-account-key}`: The access key for your Azure storage account. This key is essential for authentication and must be kept secure.
      - `${azure-storage-account-name}`: The name of your Azure storage account. This name is used in conjunction with the endpoint suffix to form the base URL for your WASBS resources.
    
    Ensure that you replace each placeholder (e.g., `${wasbs-depot-name}`, `${azure-endpoint-suffix}`) with the actual values pertaining to your Azure account and WASBS configuration. 

    === "Read-only instance-secret"
        ```yaml title="instance_secret_wasbs_read.yaml"
        --8<-- "examples/resources/lakehouse/wasbs/resource_instance_secret_wasbs_read.yaml"
        ```
    === "Read-write instance-secret"
        ```yaml title="instance_secret_wasbs_read_write.yaml"
        --8<-- "examples/resources/lakehouse/wasbs/resource_instance_secret_wasbs_read_write.yaml"
        ```

=== "GCS"

    To configure your instance-secret maniest for GCS access, you'll need to gather the following details:

      - `${gcs-depot-name}`:  Define the name of your GCS depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing, then the `${gcs-depot-name}` will be alpha0testing0storage.
      - `${description}`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
      - `${project-id}`: The unique identifier of the Google Cloud project that your GCS bucket resides in. You can find this information in the Google Cloud Console under the 'Project Info' section.
      - `${email}`:  The email address associated with the Google Cloud service account that will be used for accessing GCS. This service account should have the necessary permissions to perform operations on the GCS bucket.
      - `${gcskey_json}`: The JSON key file of the Google Cloud service account. This file contains the private key and other credentials that are required for authenticating the service account. It can be obtained by creating a service account key in the Google Cloud Console.

    After collecting the above details, depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below. In the chosen template, replace the placeholders (`${gcs-depot-name}`, `${project-id}`, `${email}`, `${gcskey_json}`, and optionally `${description}`) with the actual values you gathered and save it locally on your system.

    === "Read-only instance-secret"
        ```yaml title="instance_secret_gcs_read.yaml"
        --8<-- "examples/resources/lakehouse/gcs/resource_instance_secret_gcs_read.yaml"
        ```
    === "Read-write instance-secret"
        ```yaml title="instance_secret_gcs_read_write.yaml"
        --8<-- "examples/resources/lakehouse/gcs/resource_instance_secret_gcs_read_write.yaml"
        ```
=== "S3"

    To create an instance-secret for securely accessing Amazon S3, the following details are required:

      - `${s3-depot-name}`: Define the name of your S3 depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing, then the `${gcs-depot-name}` will be alpha0testing0storage.
      - `${description}`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
      - `${access-key-id}`: Your access key ID. This key serves as an identifier for your IAM user or role.
      - `${aws-access-key-id`}: AWS-specific access key ID, required for authenticating requests made to AWS services.
      - `${aws-secret-access-key}`: The secret access key for AWS. It's used in conjunction with the AWS access key ID to sign programmatic requests to AWS.
      - `${secret-key}`: The secret key associated with your access key ID. Together, they authenticate requests to AWS services.
    
    Ensure that you replace each placeholder (e.g., `${depot-name}`, `${accesskeyid}`) with the actual values pertaining to your AWS account and S3 configuration. 

    === "Read-only instance-secret"
        ```yaml title="instance_secret_s3_read.yaml" 
        --8<-- "examples/resources/lakehouse/s3/resource_instance_secret_s3_read.yaml"
        ```
    === "Read-write instance-secret"
        ```yaml title="instance_secret_s3_read_write.yaml"
        --8<-- "examples/resources/lakehouse/s3/resource_instance_secret_s3_read_write.yaml"
        ```

</div>

**Apply the Instance-secret manifest file**

After creating the manifest file for the Instance-secret Resource, apply it using the DataOS CLI to instantiate the Resource-instance in the DataOS environment. To apply the Lakehouse YAML file, utilize the [`apply`](/interfaces/cli/command_reference/#apply) command.

```shell
dataos-ctl apply -f ${manifest-file-path}
``` 

The `${manifest-file-path}` is a placeholder for the path to your manifest file. This can be either a relative path from your current directory or an absolute path. Ensure that you replace the placeholder (`${manifest-file-path}`) with the actual manifest file path.

Sample

```shell
dataos-ctl resource apply -f lakehouse/instance_secret_read.yaml 
```

**Verify Instance-secret creation**

To ensure that your Instance-secret has been successfully created, you can verify it in two ways:

Check the name of the newly created Instance-secret in the list of Instance-secret created by you using the `resource get` command:

```shell
dataos-ctl resource get -t instance-secret
```

Alternatively, retrieve the list of all Instance-secret created by all users in a particular domain by appending `-a` flag:

```shell
dataos-ctl resource get -t instance-secret -a
```

You can also access the details of any created Instance-secret through the DataOS GUI in the Resource tab of the  [Operations](/interfaces/operations/) app.

### **Procedure**

#### **Create a Lakehouse manifest file**

A Lakehouse YAML manifest can be structurally broken down into following sections:

- [Resource meta section](#resource-meta-section)
- [Lakehouse-specific section](#lakehouse-specific-section)
	- [Storage configuration](#storage-configuration)
	- [Metastore configuration](#metastore-configuration)
	- [Query Engine configuration](#query-engine-configuration)

#### **Resource meta section**

In DataOS, a Lakehouse is categorized as a [Resource-type](/resources/types_of_dataos_resources/). The Resource meta section within the YAML manifest encompasses attributes universally applicable to all Resource-types. The provided YAML codeblock elucidates the requisite attributes for this section: 

=== "Syntax"

    ```yaml title="resource_lakehouse_meta_section.yaml"
    # Resource-meta section
    name: ${resource-name}
    version: v1alpha
    type: lakehouse
    tags:
      - ${tag1}
      - ${tag2}
    description: ${description}
    owner: ${userid-of-owner}
    layer: user
    lakehouse:
      # attributes of lakehouse-specific section
    ```
=== "Sample"

    ```yaml title="sample_resource_lakehouse_meta_section.yaml"
    # Resource-meta section
    name: alphaomega
    version: v1alpha
    type: lakehouse
    tags:
      - Iceberg
      - Azure
    description: Icebase depot of storage-type S3
    owner: iamgroot
    layer: user
    lakehouse:
      # attributes of lakehouse-specific section
    ```

For more information about the various attributes in Resource meta section, refer to the [Attributes of Resource meta section](/resources/resource_attributes/).

#### **Lakehouse-specific section**

The Lakehouse-specific section encompasses attributes specific to the Lakehouse Resource:

=== "Basic configuration"

    The basic configuration of a manifest snippet includes only the essential attributes required for establishing a Lakehouse.

    === "Syntax"

        ```yaml title="lakehouse_specific_section_basic_syntax.yaml"
        lakehouse:
          type: iceberg
          compute: ${compute-name}
          iceberg:
            # Storage section 
            storage:
              type: s3/gcs/abfss/wasbs # possible value: s3, gcs, wasbs, abfss
              s3/gcs/abfss/wasbs:
                ${source-specific-attributes}

          # For S3
              # s3:
              #   bucket: ${bucket-name}
              #   relativePath: ${relative-path}

          # For ABFSS
              # abfss:
              #   account: ${account}
              #   container: ${container}
              #   relativePath: ${relativepath}
              #   endpointSuffix: ${endpointsuffix}
              #   format: Iceberg
          # For WASBS
              # wasbs:
              #   account: ${account}
              #   container: ${container}
              #   relativePath: ${relativepath}
              #   endpointSuffix: ${endpointsuffix}
              #   format: Iceberg
          # For GCS
              # gcs:
              #   bucket: ${gcs-bucket}
              #   relativePath: ${relative-path}
              #   format: Iceberg 

            # Metastore section 
            metastore:
              type: ${metastore-type}
              # ...other Metastore-specific attributes
            # Query engine section 
            queryEngine:
              type: ${query-engine-type}
              # ...other Query-engine-specific attributes
        ```
    === "Sample"

        For S3 bucket, the lakehouse-specific section is as follows:

        ```yaml title="lakehouse_specific_section_basic_sample.yaml"
        lakehouse:
          type: iceberg
          compute: query-default
          iceberg:
            storage:
              type: s3
              s3:
                bucket: lakehouse-bucket
                relativePath: /lakehouse 
              secrets:
                - name: alphaomega0public0storage-r
                  keys:
                    - alphaomega0public0storage-r
                  allkeys: true    
                - name: alphaomega0public0storage-rw
                  keys:
                    - alphaomega0public0storage-rw
                  allkeys: true 
            metastore:
              type: iceberg-rest-catalog
            queryEngine:
              type: themis
        ```

    <center>

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`lakehouse`](/resources/lakehouse/manifest_attributes/#lakehouse) | mapping | none | none | mandatory |
    | [`type`](/resources/lakehouse/manifest_attributes/#type) | string | none | `iceberg` | mandatory |
    | [`compute`](/resources/lakehouse/manifest_attributes/#compute) | string | none | `query-default` | mandatory |
    | [`iceberg`](/resources/lakehouse/manifest_attributes/#iceberg) | mapping | none | none | mandatory |
    | [`storage`](/resources/lakehouse/manifest_attributes/#storage) | mapping | none | none | mandatory |
    | [`metastore`](/resources/lakehouse/manifest_attributes/#metastore) | mapping | none | none | optional |
    | [`queryEngine`](/resources/lakehouse/manifest_attributes/#queryEngine) | mapping | none | none | optional |

    </center>


=== "Advanced configuration"

    The advanced configuration covers the full spectrum of attributes that can be specified within the Lakehouse-specific section a manifest for comprehensive customization.

    ```yaml title="lakehouse_specific_section_advanced.yaml"
    # Configuration for Lakehouse-specific section
    lakehouse:
      type: ABFSS                                 # Storage-type (mandatory)
      compute: runnable-default                   # Compute name (mandatory)
      runAsApiKey: abcdefghijklmnopqrstuvwxyz     # DataOS API key (optional)
      runAsUser: iamgroot                         # User ID of use-case assignee (optional)
      iceberg: 
        # Storage section: Comprises attributes specific to storage configuration
        storage:                                  # Storage section (mandatory)
          # ...attributes specific to storage configuration
        # Metastore section: Comprises attributes specific to metastore configuration
        metastore:                                # Metastore section (optional)
          # ...attributes specific to metastore configuration
        # Query Engine configuration (optional)
        queryEngine:                              
          # ...attributes specific to the query-engine configuration
    ```
    <center>

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`lakehouse`](/resources/lakehouse/manifest_attributes/#lakehouse) | mapping | none | none | mandatory |
    | [`type`](/resources/lakehouse/manifest_attributes/#type) | string | none | ABFSS, GCS, S3 | mandatory |
    | [`compute`](/resources/lakehouse/manifest_attributes/#compute) | string | none | any valid string | mandatory |
    | [`runAsApiKey`](/resources/lakehouse/manifest_attributes/#runasapikey) | string | none | any valid string | optional |
    | [`runAsUser`](/resources/lakehouse/manifest_attributes/#runasuser) | string | none | any valid string | optional |
    | [`iceberg`](/resources/lakehouse/manifest_attributes/#iceberg) | mapping | none | none | optional |
    | [`storage`](/resources/lakehouse/manifest_attributes/#storage) | mapping | none | none | mandatory in `iceberg` |
    | [`metastore`](/resources/lakehouse/manifest_attributes/#metastore) | mapping | none | none | optional in `iceberg` |
    | [`queryEngine`](/resources/lakehouse/manifest_attributes/#queryengine) | mapping | none | none | optional in `iceberg` |

    </center>

##### **Storage configuration**

The storage configuration is a fundamental aspect of defining a Lakehouse, ensuring data is stored efficiently and securely. Through the use of Instance-secrets, sensitive information like source credentials can be securely referred within the manifest file. The storage configuraiton encompass attributes specific to the object storage type (such as ABFSS, GCS, WASBS, or S3) and configuring access through securely managed secrets.

=== "Using Instance-secret"

    ```yaml
    storage: 
      depotName: depot name 			 # Name of depot (optional)
      type: abfss 					 # Object store type (mandatory)
      abfss/gcs/wasbs/s3: 			 # Depot type (optional)
        # ... attributes specific to depot-type
      secret: 
        - name: mysecret 			 # Secret Name (mandatory)
          workspace: public 		 # Workspace Name (optional)
          key: username 			 # Key (optional)
          keys: 					 # Keys (optional)
            - username
            - password
          allKeys: true 			 # All Keys (optional)
          consumptionType: envVars # Secret consumption type (optional)
    ```

    <center>

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`storage`](/resources/lakehouse/manifest_attributes/#storage) | object | none | none | mandatory |
    | [`depotName`](/resources/lakehouse/manifest_attributes/#depotname) | string | none | any valid string | optional |
    | [`type`](/resources/lakehouse/manifest_attributes/#type) | string | none | abfss | mandatory |
    | [`abfss/gcs/wasbs/s3`](/resources/lakehouse/manifest_attributes/#abfssgcswasbss3) | object | none | none | optional |
    | [`depot configuration`](/resources/lakehouse/manifest_attributes/#depotconfiguration) | object | none | none | as per depot type |
    | [`secret`](/resources/lakehouse/manifest_attributes/#secret) | object | none | none | mandatory |
    | [`name`](/resources/lakehouse/manifest_attributes/#name) (under `secret`) | string | none | any valid string | mandatory |
    | [`workspace`](/resources/lakehouse/manifest_attributes/#workspace) (under `secret`) | string | none | any valid string | optional |
    | [`key`](/resources/lakehouse/manifest_attributes/#key) (under `secret`) | string | none | any valid string | optional |
    | [`keys`](/resources/lakehouse/manifest_attributes/#keys) (under `secret`) | array | none | any valid strings | optional |
    | [`allKeys`](/resources/lakehouse/manifest_attributes/#allkeys) (under `secret`) | boolean | none | true/false | optional |
    | [`consumptionType`](/resources/lakehouse/manifest_attributes/#consumptiontype) (under `secret`) | string | none | envVars | optional |

    </center>

    Attributes-specific to the depot-type.


    === "ABFSS"

        ```yaml
        abfss:
          account: random 						# ABFSS Account (optional)
          container: alpha 						# Container (optional)
          endpointSuffix: new 					# End Point Suffix (optional)
          format: iceberg 						# File Format (optional)
          icebergCatalogType: hadoop 				# Iceberg Catalog Type (optional)
          metastoreType: iceberg-rest 			# Metastore type (optional)
          metastoreUrl: https://random-url.com	# Metastore URL (optional)
          relativePath: tmdc-dataos 				# Relative Path (optional)
        ```

        <center>

        | Attribute | Data Type | Default Value | Possible Value | Requirement |
        | --- | --- | --- | --- | --- |
        | [`abfss`](/resources/lakehouse/manifest_attributes/#abfss) | object | none | none | optional |
        | [`account`](/resources/lakehouse/manifest_attributes/#account) | string | none | any valid ABFSS account | optional |
        | [`container`](/resources/lakehouse/manifest_attributes/#container) | string | none | any valid container name | optional |
        | [`endpointSuffix`](/resources/lakehouse/manifest_attributes/#endpointsuffix) | string | none | any valid endpoint suffix | optional |
        | [`format`](/resources/lakehouse/manifest_attributes/#format) | string | none | any valid file format | optional |
        | [`icebergCatalogType`](/resources/lakehouse/manifest_attributes/#icebergcatalogtype) | string | none | any valid Iceberg catalog type | optional |
        | [`metastoreType`](/resources/lakehouse/manifest_attributes/#metastoretype) | string | none | any valid metastore type | optional |
        | [`metastoreUrl`](/resources/lakehouse/manifest_attributes/#metastoreurl) | string | none | any valid URL | optional |
        | [`relativePath`](/resources/lakehouse/manifest_attributes/#relativepath) | string | none | any valid relative path | optional |

        </center>

    === "GCS"

        ```yaml
        gcs:
          bucket: bucket-testing 					# GCS Bucket (optional)
          format: format 							# Format (optional)
          icebergCatalogType: hadoop 				# Iceberg Catalog Type (optional)
          metastoreType: iceberg-rest 			# Meta Store type (optional)
          metastoreUrl: https://random-url.com    # Meta Store URL (optional)
          relativePath: tmdc-dataos 				# Relative Path (optional)
        ```

        <center>

        | Attribute | Data Type | Default Value | Possible Value | Requirement |
        | --- | --- | --- | --- | --- |
        | [`gcs`](/resources/lakehouse/manifest_attributes/#gcs) | object | none | none | optional |
        | [`bucket`](/resources/lakehouse/manifest_attributes/#bucket) | string | none | any valid GCS bucket name | optional |
        | [`format`](/resources/lakehouse/manifest_attributes/#format) | string | none | any valid format | optional |
        | [`icebergCatalogType`](/resources/lakehouse/manifest_attributes/#icebergcatalogtype) | string | none | hadoop | optional |
        | [`metastoreType`](/resources/lakehouse/manifest_attributes/#metastoretype) | string | none | iceberg-rest | optional |
        | [`metastoreUrl`](/resources/lakehouse/manifest_attributes/#metastoreurl) | string | none | any valid URL | optional |
        | [`relativePath`](/resources/lakehouse/manifest_attributes/#relativepath) | string | none | any valid relative path | optional |

        </center>

    === "S3"

        ```yaml
        s3:
          bucket: bucket-testing	    		# GCS Bucket (optional)
          format: format 			 			# Format (optional)
          icebergCatalogType: hadoop  		# Iceberg Catalog Type (optional)
          metastoreType: iceberg-rest		    # Meta Store type (optional)
          metastoreUrl: iceberg-rest		    # Meta Store URL (optional)
          relativePath: tmdc-dataos			# Relative Path (optional)
          scheme: abcd 						# Scheme (optional)
        ```

        <center>

        | Attribute | Data Type | Default Value | Possible Value | Requirement |
        | --- | --- | --- | --- | --- |
        | [`s3`](/resources/lakehouse/manifest_attributes/#s3) | object | none | none | optional |
        | [`bucket`](/resources/lakehouse/manifest_attributes/#bucket) | string | none | any valid S3 bucket name | optional |
        | [`format`](/resources/lakehouse/manifest_attributes/#format) | string | none | any valid format | optional |
        | [`icebergCatalogType`](/resources/lakehouse/manifest_attributes/#icebergcatalogtype) | string | none | hadoop | optional |
        | [`metastoreType`](/resources/lakehouse/manifest_attributes/#metastoretype) | string | none | iceberg-rest | optional |
        | [`metastoreUrl`](/resources/lakehouse/manifest_attributes/#metastoreurl) | string | none | any valid URL | optional |
        | [`relativePath`](/resources/lakehouse/manifest_attributes/#relativepath) | string | none | any valid relative path | optional |
        | [`scheme`](/resources/lakehouse/manifest_attributes/#scheme) | string | none | any valid scheme | optional |

        </center>

    === "WASBS"

        ```yaml
        wasbs:
          account: random 						# WASBS Account (optional)
          container: alpha 						# Container (optional)
          endpointSuffix: new 					# End Point Suffix (optional)
          format: iceberg 						# File Format (optional)
          icebergCatalogType: hadoop 				# Iceberg Catalog Type (optional)
          metastoreType: iceberg-rest 			# Metastore type (optional)
          metastoreUrl: https://random-url.com	# Metastore URL (optional)
          relativePath: tmdc-dataos 				# Relative Path (optional)
        ```

        <center>

        | Attribute | Data Type | Default Value | Possible Value | Requirement |
        | --- | --- | --- | --- | --- |
        | [`wasbs`](/resources/lakehouse/manifest_attributes/#wasbs) | object | none | none | optional |
        | [`account`](/resources/lakehouse/manifest_attributes/#account) | string | none | any valid WASBS account | optional |
        | [`container`](/resources/lakehouse/manifest_attributes/#container) | string | none | any valid container name | optional |
        | [`endpointSuffix`](/resources/lakehouse/manifest_attributes/#endpointsuffix) | string | none | any valid endpoint suffix | optional |
        | [`format`](/resources/lakehouse/manifest_attributes/#format) | string | none | any valid file format | optional |
        | [`icebergCatalogType`](/resources/lakehouse/manifest_attributes/#icebergcatalogtype) | string | none | any valid Iceberg catalog type | optional |
        | [`metastoreType`](/resources/lakehouse/manifest_attributes/#metastoretype) | string | none | any valid metastore type | optional |
        | [`metastoreUrl`](/resources/lakehouse/manifest_attributes/#metastoreurl) | string | none | any valid URL | optional |
        | [`relativePath`](/resources/lakehouse/manifest_attributes/#relativepath) | string | none | any valid relative path | optional |

        </center>




##### **Metastore configuration**

The metastore plays a pivotal role in a Lakehouse, serving as the central repository for metadata about data structures like tables, views, and schemas. This metadata is crucial for data management tasks such as querying, data discovery, and schema validation. Configuring the metastore properly is essential for ensuring seamless access and manipulation of stored data.

The configuration of the metastore can be tailored to meet the specific needs of a Lakehouse, ranging from basic setups with minimal attributes to advanced configurations that leverage additional features for enhanced performance and scalability. The basic configuration requires specifying the metastore type, such as `iceberg-rest-catalog`, to define the underlying technology or service used for metadata storage. On the other hand, the advanced configuration allows for the specification of attributes like the number of replicas, autoscaling options, and resource allocation for CPU and memory, providing greater control over the metastore's performance and resource usage.

=== "Basic configuration"

    ```yaml
    metastore: 									  # Metastore section (optional)
      type: iceberg-rest-catlog 				  # Metastore type (mandatory)
    ```

    <center>

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`metastore`](/resources/lakehouse/manifest_attributes/#metastore) | mapping | none | none | optional |
    | [`type`](/resources/lakehouse/manifest_attributes/#type) | string | none | iceberg-rest-catlog | mandatory |
    
    </center>

=== "Advanced configuration"

    ```yaml
    metastore: 									  # Metastore section (optional)
      type: iceberg-rest-catlog 				  # Metastore type (mandatory)
      replicas: 2 							  # Number of replicas (optional)
      autoScaling: 							  # Autoscaling configuration (optional)
        enabled: true 						  # Enable autoscaling (optional)
        minReplicas: 2 						  # Minimum number of replicas (optional)
        maxReplicas: 4 					  	  # Maximum number of replicas (optional)
        targetMemoryUtilizationPercentage: 60 # Target Memory Utilization Percentage (optional)
        targetCPUUtilizationPercentage: 60 	  # Target CPU Utilization Percentage (optional)
      resources: 								  # CPU and memory resources (optional)
        requests: 
          cpu: 1Gi 						  # Requested CPU resources (optional)
          memory: 400m 					  # Requested Memory resources (optional)
        limits:
          cpu: 1Gi 						  # CPU resource limits (optional)
          memory: 400m 					  # Memory resource limits (optional)
    ```


    <center>

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`metastore`](/resources/lakehouse/manifest_attributes/#metastore) | mapping | none | none | optional |
    | [`type`](/resources/lakehouse/manifest_attributes/#type) | string | none | iceberg-rest-catlog | mandatory |
    | [`replicas`](/resources/lakehouse/manifest_attributes/#replicas) | integer | none | any valid positive integer | optional |
    | [`autoScaling`](/resources/lakehouse/manifest_attributes/#autoscaling) | mapping | none | none | optional |
    | [`enabled`](/resources/lakehouse/manifest_attributes/#enabled) | boolean | none | true/false | optional |
    | [`minReplicas`](/resources/lakehouse/manifest_attributes/#minreplicas) | integer | none | any valid integer | optional |
    | [`maxReplicas`](/resources/lakehouse/manifest_attributes/#maxreplicas) | integer | none | any valid integer | optional |
    | [`targetMemoryUtilizationPercentage`](/resources/lakehouse/manifest_attributes/#targetmemoryutilizationpercentage) | integer | none | any valid percentage | optional |
    | [`targetCPUUtilizationPercentage`](/resources/lakehouse/manifest_attributes/#targetcpuutilizationpercentage) | integer | none | any valid percentage | optional |
    | [`resources`](/resources/lakehouse/manifest_attributes/#resources) | mapping | none | none | optional |
    | [`requests`](/resources/lakehouse/manifest_attributes/#requests) | mapping | none | none | optional |
    | [`cpu`](/resources/lakehouse/manifest_attributes/#cpu) | string | none | any valid resource amount | optional |
    | [`memory`](/resources/lakehouse/manifest_attributes/#memory) | string | none | any valid resource amount | optional |
    | [`limits`](/resources/lakehouse/manifest_attributes/#limits) | mapping | none | none | optional |
    | [`cpu`](/resources/lakehouse/manifest_attributes/#cpu) | string | none | any valid resource amount | optional |
    | [`memory`](/resources/lakehouse/manifest_attributes/#memory) | string | none | any valid resource amount | optional |

    </center>

##### **Query Engine configuration**

The configuration of the query engine is a crucial component in tailoring the Lakehouse to meet specific data processing requirements. A query engine defines the computational backbone of the Lakehouse, enabling efficient data querying and processing capabilities. At its core, the query engine configuration outlines the type of engine to be used, such as Themis, along with optional specifications for resource allocation and operational parameters to optimize performance.

For general use cases, a basic configuration may suffice, requiring only the specification of the query engine type. This minimal setup is suitable for environments where default resource allocations and settings meet the Lakehouse's needs. However, advanced configurations offer a deeper level of customization. They allow administrators to specify detailed resource requests and limits for CPU and memory, ensuring that the query engine operates within designated resource boundaries for both efficiency and cost-effectiveness.

=== "Basic configuration"

    ```yaml
    queryEngine:
      type: themis
    ```
    <center>

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`queryEngine`](/resources/lakehouse/manifest_attributes/#queryengine) | object | none | none | mandatory |
    | [`type`](/resources/lakehouse/manifest_attributes/#type) | string | none | themis | mandatory |

    </center>

=== "Advanced configuration"

    ```yaml
    queryEngine:
      type: themis	 			
      resources: 					
        requests: 
          cpu: ${requested-cpu-resource}	 		
          memory: ${requested-memory-resource}	 
        limits:
          cpu: ${cpu-resource-limits}	 		
          memory: ${memory-resource-limits}
      themis: 			
        envs: 
          ${key1}: ${value1}
        themisConf:
          ${key1}: ${value1}
        spark: 
          driver:				
            memory: ${spark-driver-memory}
            cpu: ${spark-driver-cpu} 		
          executor: 		
            memory: ${spark-executor-memory}
            cpu: ${spark-executor-cpu}
            instanceCount: ${instance-count}
            maxInstanceCount: ${maximum-instance-count}
          sparkConf: 
            ${key1}: ${value1}				 
    ```
    <center>

    | Attribute | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`queryEngine`](/resources/lakehouse/manifest_attributes/#queryengine) | object | none | none | mandatory |
    | [`type`](/resources/lakehouse/manifest_attributes/#type) | string | none | themis | mandatory |
    | [`resources`](/resources/lakehouse/manifest_attributes/#resources) | object | none | none | optional |
    | [`requests`](/resources/lakehouse/manifest_attributes/#requests) | object | none | none | optional |
    | [`cpu`](/resources/lakehouse/manifest_attributes/#cpu) (under `requests`) | string | none | any valid CPU resource amount | optional |
    | [`memory`](/resources/lakehouse/manifest_attributes/#memory) (under `requests`) | string | none | any valid memory resource amount | optional |
    | [`limits`](/resources/lakehouse/manifest_attributes/#limits) | object | none | none | optional |
    | [`cpu`](/resources/lakehouse/manifest_attributes/#cpu) (under `limits`) | string | none | any valid CPU resource limit | optional |
    | [`memory`](/resources/lakehouse/manifest_attributes/#memory) (under `limits`) | string | none | any valid memory resource limit | optional |
    | [`themis`](/resources/lakehouse/manifest_attributes/#themisminerva) | object | none | none | optional |
    | [`envs`](/resources/lakehouse/manifest_attributes/#envs) | object | none | none | optional |
    | [`themisConf`](/resources/lakehouse/manifest_attributes/#themisconf) | object | none | none | optional |
    | [`spark`](/resources/lakehouse/manifest_attributes/#spark) | object | none | none | mandatory |
    | [`driver`](/resources/lakehouse/manifest_attributes/#driver) (under `spark`) | object | none | none | mandatory |
    | [`memory`](/resources/lakehouse/manifest_attributes/#memory) (under `driver`) | string | none | any valid memory amount | mandatory |
    | [`cpu`](/resources/lakehouse/manifest_attributes/#cpu) (under `driver`) | string | none | any valid CPU resource | mandatory |
    | [`executor`](/resources/lakehouse/manifest_attributes/#executor) (under `spark`) | object | none | none | mandatory |
    | [`memory`](/resources/lakehouse/manifest_attributes/#memory) (under `executor`) | string | none | any valid memory amount | mandatory |
    | [`cpu`](/resources/lakehouse/manifest_attributes/#cpu) (under `executor`) | string | none | any valid CPU resource | mandatory |
    | [`instanceCount`](/resources/lakehouse/manifest_attributes/#instancecount) (under `executor`) | integer | none | any valid integer | mandatory |
    | [`maxInstanceCount`](/resources/lakehouse/manifest_attributes/#maxinstancecount) (under `executor`) | integer | none | any valid integer | mandatory |
    | [`sparkConf`](/resources/lakehouse/manifest_attributes/#sparkconf) (under `spark`) | object | none | none | optional |

    </center>

??? tip "Sample Lakehouse manifest"

    ```yaml

    # Resource-meta section
    name: alphaomega
    version: v1alpha
    type: lakehouse
    tags:
      - Iceberg
      - Azure
    description: Icebase depot of storage-type S3
    owner: iamgroot
    layer: user

    # Lakehouse-specific section
    lakehouse:
      type: iceberg
      compute: runnable-default
      iceberg:
        storage:
          type: s3
          s3:
            bucket: dataos-lakehouse   
            relativePath: /test
          secrets:
            - name: alphaomega0public0storage-r
              keys:
                - alphaomega0public0storage-r
              allkeys: true 
            - name: alphaomega0public0storage-rw
              keys:
                - alphaomega0public0storage-rw
              allkeys: true    
        metastore:
          type: "iceberg-rest-catalog"
        queryEngine:
          type: themis
    ```

### **Apply the Lakehouse manifest**

After creating the manifest file for the Lakehouse Resource, it's time to apply it to instantiate the Resource-instance in the DataOS environment. To apply the Lakehouse manifest file, utilize the [`apply`](/interfaces/cli/command_reference/#apply) command.

```shell
dataos-ctl apply -f ${yaml config file path} - w ${workspace name}
```
Sample

```shell
dataos-ctl apply -f dataproducts/new-lakehouse.yaml -w curriculum
```



### **Verify Lakehouse Creation**

To ensure that your Lakehouse has been successfully created, you can verify it in two ways:

Check the name of the newly created Lakehouse in the list of lakehouses created by you in a particular Workspace:

```shell
dataos-ctl get -t lakehouse - w ${{workspace name}}
# Sample
dataos-ctl get -t lakehouse -w curriculum
```

Alternatively, retrieve the list of all Lakehouses created in the Workspace by appending `-a` flag:

```shell
dataos-ctl get -t lakehouse -w ${{workspace name}} -a
# Sample
dataos-ctl get -t lakehouse -w curriculum
```

You can also access the details of any created Lakehouse through the DataOS GUI in the Resource tab of the  [Operations App.](/interfaces/operations/)

### **Deleting a Lakehouse**

Use the [`delete`](/interfaces/cli/command_reference/#delete) command to remove the specific Lakehouse Resource-instance from the DataOS environment. There are three ways to delete a Lakehouse as shown below.

**Method 1:** Copy the name to Workspace from the output table of the [`get`](/interfaces/cli/command_reference/#get) command and use it as a string in the delete command.

Command

```shell
dataos-ctl delete -i "${{name to workspace in the output table from get status command}}"
```

Example:

```shell
dataos-ctl delete -i "cnt-lakehouse-demo-01 | v1alpha | lakehouse | public"
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0001] 🗑 deleting(public) cnt-lakehouse-demo-01:v1alpha:lakehouse...
INFO[0003] 🗑 deleting(public) cnt-lakehouse-demo-01:v1alpha:lakehouse...deleted
INFO[0003] 🗑 delete...complete
```

**Method 2:** Specify the path of the YAML file and use the [`delete`](/interfaces/cli/command_reference/#delete) command.

Command:

```shell
dataos-ctl delete -f ${{file-path}}
```

Example:

```shell
dataos-ctl delete -f /home/desktop/connect-city/config_v1alpha.yaml
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0000] 🗑 deleting(public) cnt-lakehouse-demo-010:v1alpha:lakehouse...
INFO[0001] 🗑 deleting(public) cnt-lakehouse-demo-010:v1alpha:lakehouse...deleted
INFO[0001] 🗑 delete...complete
```

**Method 3:** Specify the Workspace, Resource-type, and Lakehouse name in the [`delete`](/interfaces/cli/command_reference/#delete) command.

Command:

```shell
dataos-ctl delete -w ${{workspace}} -t lakehouse -n ${{lakehouse name}}
```

Example:

```shell
dataos-ctl delete -w public -t lakehouse -n cnt-product-demo-01
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0000] 🗑 deleting(public) cnt-city-demo-010:v1alpha:lakehouse...
INFO[0001] 🗑 deleting(public) cnt-city-demo-010:v1alpha:lakehouse...deleted
INFO[0001] 🗑 delete...complete
```


## Attributes of Lakehouse manifest

The Attributes of Lakehouse manifest define the key properties and configurations that can be used to specify and customize Lakehouse Resources within a manifest file. These attributes allow data developers to define the structure and behavior of their Lakehouse Resources. For comprehensive information on each attribute and its usage, please refer to the link: [Attributes of Lakehouse manifest](/resources/lakehouse/manifest_attributes/).

## Lakehouse DDL/DML Command Reference

Various CLI commands related to performing DDL/DML operations on datasets in a Lakehouse: [Lakehouse command reference](/resources/lakehouse/command_reference/).

## Case Scenario

- [How to create a Lakehouse on ABFSS data source?](/resources/lakehouse/case_scenario/how_to_create_a_lakehouse_on_abfss_data_source/)
- [How to create a Lakehouse on WASBS data source?](/resources/lakehouse/case_scenario/how_to_create_a_lakehouse_on_wasbs_data_source/)
- [How to create a Lakehouse on S3 data source?](/resources/lakehouse/case_scenario/how_to_create_a_lakehouse_on_s3_data_source/)
- [How to create a Lakehouse on GCS data source?](/resources/lakehouse/case_scenario/how_to_create_a_lakehouse_on_gcs_data_source/)
- [How to create, fetch, and drop dataset in a Lakehouse using CLI commands?](/resources/lakehouse/command_reference/case_scenario_create_fetch_and_drop_dataset/)
- [How to perform Iceberg dataset maintainence in a Lakehouse using CLI commands?](/resources/lakehouse/command_reference/case_scenario_maintenance/)
- [How to perform partitioning on Lakehouse datasets using CLI commands?](/resources/lakehouse/command_reference/case_scenario_partitioning/)
- [How to perform schema evolution on Lakehouse datasets using CLI commands?](/resources/lakehouse/command_reference/case_scenario_schema_evolution/)
- [How to manipulate table properties of Lakehouse datasets using CLI commands?](/resources/lakehouse/command_reference/case_scenario_table_properties/)
