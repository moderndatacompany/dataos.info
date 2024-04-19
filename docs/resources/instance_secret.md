---
title: Instance Secret
search:
  boost: 2
---

# :resources-instancesecret: Instance Secret

An Instance Secret is a [DataOS Resource](/resources/) designed for securely storing sensitive information at the DataOS instance level. This encompasses sensitive information like usernames, passwords, certificates, tokens, and keys. The primary purpose of Instance Secret is to address the inherent exposure risk associated with directly embedding such confidential data within application code or manifest file (YAML configuration files). 

Instance secrets establish a critical segregation between sensitive data and Resource definitions. This division minimizes the chances of inadvertent exposure during various Resource management phases, including creation, viewing, or editing. By leveraging Instance Secrets, data developers ensure the safeguarding of sensitive information, thereby mitigating security vulnerabilities inherent in their data workflows.

<aside class="callout">

🗣️ In the DataOS ecosystem, there are two specialized Resources designed to protect sensitive information: Instance Secret and <a href="/resources/secret/">Secret</a>. The Instance Secret offers a wider scope, extending across the entirety of the <a href="/resources/types_of_dataos_resources/#instance-level-resources">DataOS Instance</a>. Resources within any Workspace can utilize Instance Secrets for securely retrieving sensitive data. In contrast, Secrets are limited to the <a href="/resources/types_of_dataos_resources/#workspace-level-resources">Workspace level</a>, accessible exclusively within a specific Workspace and only by Resources associated with that Workspace.
</aside>


<div class="grid cards" markdown>

-   :material-format-list-bulleted-type:{ .lg .middle } **How to create and manage an Instance Secret?**

    ---

    Learn how to create and manage an Instance secret in DataOS.

    [:octicons-arrow-right-24: Create and manage an Instance Secret](/resources/instance_secret/#how-to-create-an-instance-secret)


-   :material-script-text-outline:{ .lg .middle } **How to refer an Instance Secret in other DataOS Resources?**

    ---

    Discover how to use Instance Secrets to securely refer sensitive information in other DataOS Resources.

    [:octicons-arrow-right-24: Referring Instance Secrets](/resources/instance_secret/#how-to-refer-instance-secret-in-other-dataos-resources)


-   :material-clock-fast:{ .lg .middle } **Types of Instance Secrets**

    ---

    Different types of Instance Secret securely store diverse sensitive data, addressing specific needs like key-value pairs, certificates, etc.

    [:octicons-arrow-right-24: Types of Instance Secret](/resources/instance_secret/#types-of-instance-secret)


-   :material-console:{ .lg .middle } **Instance Secret Templates**

    ---

    Explore manifest file templates of various data source-specific Instance Secrets like Bigquery, PostgreSQL, Google Cloud Storage, and many more.

    

    [:octicons-arrow-right-24: Example](/resources/instance_secret/#instance-secret-templates)
     
</div>



## How to create and manage an Instance Secret?

To create an Instance Secret Resource in DataOS, ensure you have access to the [DataOS Command Line Interface (CLI)](../interfaces/cli.md) and the required permissions. Then, follow the provided steps to complete the creation process efficiently and securely.

### **Structure of an Instance Secret manifest file**

The structure of the Instance Secret manifest file is outlined as follows:

![Instance Secret Manifest Structure](/resources/instance_secret/instance_secret_manifest_structure.jpg)


### **Create an Instance Secret manifest file**

Begin by creating a manifest file that will hold the configuration details for your Instance Secret. A sample manifest is provided below:

???tip "Sample Instance Secret manifest"

    ```yaml title="sample_instance_secret_manifest.yaml"
    # Resource meta section
    name: depotsecret-r # Resource name (mandatory)
    version: v1 # Manifest version (mandatory)
    type: instance-secret # Resource-type (mandatory)
    tags: # Tags (optional)
    - just for practice
    description: instance secret configuration # Description of Resource (optional)
    layer: user

    # Instance Secret-specific section
    instance-secret: # Instance Secret mapping (mandatory)
      type: key-value-properties # Type of Instance-secret (mandatory)
      acl: r # Access control list (mandatory)
      data: # Data section mapping (mandatory)
        username: iamgroot
        password: yourpassword
    ```


#### **Resource meta section**

The Instance Secret manifest comprise of a Resource meta section that outlines essential metadata attributes applicable to all Resource-types. Note that within this section some attributes are optional, while others are mandatory.

```yaml
# Resource meta section
name: ${depotsecret-r} # Resource name (mandatory)
version: v1 # Manifest version (mandatory)
type: instance-secret # Resource-type (mandatory)
tags: 
  - ${new instance secret} # Tags (optional)
  - ${resource}
description: ${resource description} # Description (optional)
owner: ${iamgroot} # Owner's DataOS UserID (optional)
layer: ${user} # Layer (optional)
instance-secret: # Instance-secret specific section
```
<center><i>Resource meta section of the manifest file</i></center>

For more information about the various attributes in Resource meta section, refer to the [Attributes of Resource meta section](/resources/resource_attributes/).

#### **Instance Secret specific section**

This section focuses on Instance Secret attributes, outlining details such as Instance Secret `type`, `acl`(access control list), sensitive `data` to be stored. Additionally, it allows for the optional inclusion of file paths of sensitive information to be stored using the `files` attribute.

```yaml
instance-secret: # Instance-secret specific section
  type: ${{key-value-properties}} # Type of Instance-secret (mandatory)
  acl: ${{r|rw}} # Access control list (mandatory)
  data: # Data section mapping (either files or data is required)
    ${{username: iamgroot}}
    ${{password: abcd1234}}
  files: # Manifest file path (either files or data is required)
    ${{xyz: /home/instance-secret.yaml}}
```
<center><i>Instance-secret specific section of the manifest file</i></center>

The table below summarizes the attributes of Instance-secret specific section:

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`instance-secret`](/resources/instance_secret/manifest_attributes/#instance-secret) | mapping | none | none | mandatory |
| [`type`](/resources/instance_secret/manifest_attributes/#type) | string | none | cloud-kernel, key-value, key-value-properties, certificates | mandatory |
| [`acl`](/resources/instance_secret/manifest_attributes/#acl) | string | none | r, rw | mandatory |
| [`data`](/resources/instance_secret/manifest_attributes/#data) | mapping | none | none | mandatory |
| [`files`](/resources/instance_secret/manifest_attributes/#files) | string | none | file-path | optional |


For more information about the various attributes in Instance Secret specific section, refer to the [Attributes of Instance Secret specific section](/resources/instance_secret/manifest_attributes/).



### **Apply the Instance Secret manifest**

To create an Instance Secret Resource-instance within the DataOS, use the `apply` command. When applying the manifest file from the DataOS CLI, make sure you don't specify Workspace as Instance Secrets are [Instance-level Resource](/resources/types_of_dataos_resources/#instance-level-resources). The `apply` command is as follows:

=== "Command"
    ```shell
    dataos-ctl resource apply -f ${path/instance_secret.yaml}
    ```
    Alternate
    ```shell
    dataos-ctl apply -f ${path/instance_secret.yaml}
    ```
=== "Example Usage"
    ```shell
    dataos-ctl apply -f depot_secret.yaml
    ```
    Alternate
    ```shell
    dataos-ctl apply -f depot_secret.yaml
    ```
    Expected output:

    ```shell
    $ dataos-ctl apply -f depot_secret.yaml
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying depotsecret-r:v1:instance-secret... 
    INFO[0004] 🔧 applying depotsecret-r:v1:instance-secret...created 
    INFO[0004] 🛠 apply...complete
    ```

### **Managing an Instance-Secret**

#### **Validate the Instance Secret**

To validate the proper creation of the Instance Secret Resource within the DataOS environment, employ the `get` command. Execute the following command to ascertain the existence of the Instance Secret Resource:

=== "Command"
    - To get the details of instance-secret created by the user who applies the instance-secret, use the following command:

        ```shell
        dataos-ctl resource get -t instance-secret
        ```
        Alternate

        ```shell
        dataos-ctl get -t instance-secret
        ```
    - To get the details of instance-secret created by all the users within the DataOS Instance, use the above command with `-a` flag:

        ```shell
        dataos-ctl resource get -t instance-secret -a
        ```
        Alternate

        ```shell
        dataos-ctl get -t instance-secret -a
        ```


=== "Example Usage"

    ```shell
    dataos-ctl get -t instance-secret
    ```
    Alternate
    ```shell
    dataos-ctl resource get -t instance-secret -a
    ```
    Expected Output
    ```shell
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             

            NAME     | VERSION |      TYPE       | WORKSPACE | STATUS |  RUNTIME  |  OWNER             
    -----------------|---------|-----------------|-----------|--------|-----------|------------------------------
         depotsecret | v1      | instance-secret |           | active |           | iamgroot               
    ```


#### **Delete the Instance Secret**

<aside class="callout">
🗣️ Before you can delete an Instance Secret, you need to make sure there are no other Resources dependent on it. For example, if a Depot has a dependency on an Instance Secret, trying to delete that Instance Secret will cause an error. So, you'll need to remove the Depot first, and then you can delete the Instance Secret. This rule applies to not just Depot, but all dependent Resources, such as Workflow, Service, Worker, etc.

<details><summary>Error</summary>
The following error will be thrown if any Resource has a dependency on Instance Secret as shown below.

Example usage:

```shell
dataos-ctl delete -t instance-secret -n sampleinstsecret
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstsecret:v1:instance-secret... 
INFO[0001] 🗑 deleting sampleinstsecret:v1:instance-secret...error 
WARN[0001] 🗑 delete...error                             
ERRO[0001] Invalid Parameter - failure deleting instance resource : cannot delete resource, it is a dependency of 'depot:v2alpha:sampleinstdepot'
```
</aside>

To remove the Instance Secret Resource from the DataOS environment, utilize the `delete` command. Execute the following command to initiate the deletion process:

**Deleting using the -t (type) and -n (name) flag**

=== "Command"

    ```shell
    dataos-ctl resource delete -t ${resource-type} -n ${resource-name}
    ```
    Alternate
    ```shell
    dataos-ctl delete -t ${resource-type} -n ${resource-name}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl resource delete -t instance-secret -n myinstance_secret
    ```
    Alternate
    ```shell
    dataos-ctl delete -t instance-secret -n myinstance_secret
    ```


**Deleting using the -i (identifier) flag**

=== "Command"

    ```shell
    dataos-ctl resource delete -i ${resource-name:version:resource-type}
    ```
    Alternate
    ```shell
    dataos-ctl resource delete -i ${resource-name:version:resource-type}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl delete -i myinstance_secret:v1:instance-secret
    ```
    Expected output
    ```shell
    dataos-ctl delete -t instance-secret -n sampleinstsecret
    INFO[0000] 🗑 delete...                                  
    INFO[0000] 🗑 deleting sampleinstsecret:instance-secret...nothing 
    INFO[0000] 🗑 delete...complete
    ```

## Types of Instance Secrets

When creating Instance Secret Resource, you can specify its type using the `type` field within the `instance-secret` section. The Instance Secret type is used to facilitate programmatic handling of the Secret data.

DataOS provides several built-in types for some common usage scenarios. These types vary in terms of the validations performed and the constraints DataOS imposes on them.

| Instance Secret Type | Description |
| --- | --- |
| `cloud-kernel` | This type stores arbitrary user-defined data in the form of key-value pair as a Kubernetes Secret with the same name as the Instance Secret Resource. |
| `key-value` | This type stores arbitrary user-defined data as key-value pairs within an Instance Secret, with each pair being encoded separately in base64 format. |
| `key-value-properties` | This type conserves arbitrary user-defined data as an Instance Secret by transforming multiple key-value pairs into a singular key-value pair, which is then encoded in base64 format. |
| `certificates` | This is an instance secret type used to securely store certificates, which are often necessary for secured communication in the system.  |


For a more detailed analysis of each type and to explore the syntax, please navigate the below tabs.

=== "cloud-kernel"

    The cloud-kernel instance secret type means that a Kubernetes secret will be created with the same name as the Instance Secret Resource.

    **Syntax**

    ```yaml title="instance_secret_type_cloud_kernel.yaml"
    --8<-- "examples/resources/instance_secret/types_of_instance_secret/cloud_kernel.yaml"
    ```

=== "key-value"


    This Instance Secret type is for storing simple pairs of keys and values. They are stored in Heimdall vault.

    **Syntax**

    ```yaml title="instance_secret_type_key_value.yaml"
    --8<-- "examples/resources/instance_secret/types_of_instance_secret/key_value.yaml"
    ```

    When you store an Instance Secret as a key-value type, the system passes the instance secret in the format they are stated, without any alterations.

=== "key-value-properties"

    This type is similar to key-value, but the difference lies in the way the system passes the data. In the key-value-properties type, the system passes all the key-value pairs as one single field, while in the case of the key-value type, they are passed as separate fields.

    **Syntax**

    ```yaml title="instance_secret_type_key_value_properties.yaml"
    --8<-- "examples/resources/instance_secret/types_of_instance_secret/key_value_properties.yaml"
    ```

=== "certificates"

    This type is used to store TLS certificates and keys. The most common usage scenario is Ingress resource termination, but this type is also sometimes used with other resources.

    **Syntax**

    ```yaml  title="instance_secret_type_certificates.yaml"
    --8<-- "examples/resources/instance_secret/types_of_instance_secret/certificates.yaml"
    ```

## How to refer Instance Secret in other DataOS Resources?

To access the stored secret data in DataOS, you can reference them in your code using the `dataosSecrets` attribute. This identifier ensures secure referencing of Instance Secrets across different Resources, enhancing system security and operational integrity.

**Syntax**

```yaml
dataosSecrets:
  - name: ${your-instance-secret-name}-r|rw # Mandatory
    workspace: ${instance-secret-workspace} # Optional
    key: ${key of your instance-secret} # Optional, used when only single key is required.
    keys:            # Optional, used when multiple key is required.
      - ${instance secret_key}
      - ${instance secret-key}
    allKeys: ${true-or-false} # Optional
    consumptionType: ${envVars} # Optional, possible values: envVars, propfile and file.
```

=== "Referring Instance Secret in Depot"

    To refer to an instance-secret in Depots, follow these steps:

    1. **Ensure Creation of Instance-Secret:** First, make sure you have created the respective instance-secret.

    2. **Use `dataosSecrets` Identifier:** In the depot manifest, use the `dataosSecrets` identifier to refer to the instance-secret.

    For read-only access to a depot, create read-only secrets. For read-write access, create both read and read-write instance-secrets. This is necessary because when providing someone else access to the Depot, you can grant either read or read-write access using either CLI or Bifrost UI. For either type of access, the person will have access to the respective instance-secret.

    === "Read-only Instance Secret"

        ```yaml title="read_instance_secret.yaml"
        --8<-- "examples/resources/instance_secret/referencing_instance_secret_in_depot/sample_secret_r.yaml"
        ```

    === "Read-write Instance Secret"

        ```yaml title="read_write_instance_secret.yaml"
        --8<-- "examples/resources/instance_secret/referencing_instance_secret_in_depot/sample_secret_rw.yaml"
        ```

    Now while creating the manifest file for your Depot, ensure to include a reference to the Instance Secret using the `dataosSecrets` identifier, instead of directly specifying the secret using the `connectionSecrets` attribute:

    === "Depot"

    ```yaml title="depot.yaml"
    --8<-- "examples/resources/instance_secret/referencing_instance_secret_in_depot/sample_depot.yaml"
    ```

<aside class="callout">

🗣️ To ensure controlled access for read-write, it is essential to create two Instance Secrets: one with acl:r for read-only access and another with acl:rw for both read and write access and refer to both Instance-Secrets in a Depot as shown above. This enables precise management of permissions for different levels of access.

</aside>

## Instance Secret Templates


<div class="grid" markdown>

=== "Object Store"

    Object stores are distributed storage systems designed to store and manage large amounts of unstructured data. Instance-Secrets can configured to securely store sensitive information of the following object stores:

    === "ABFSS"

        The manifest files provided below are the templates for securely storing ABFSS credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_abfss_read.yaml"
            --8<-- "examples/resources/instance_secret/abfss/abfss_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_abfss_read_write.yaml"
            --8<-- "examples/resources/instance_secret/abfss/abfss_rw.yaml"
            ```

        To configure the template, the details required are provided below. Ensure that you replace each placeholder (e.g., `${abfss-depot-name}`, `${azure-endpoint-suffix}`) with the actual values pertaining to your Azure account and ABFSS configuration. 

          - `name`: Define the name of your Instance secret `${abfss-depot-name}-${acl}`. For instance, if your `${abfss-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.
          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `azureendpointsuffix`: The endpoint suffix for your Azure storage account. 
          - `azurestorageaccountkey`: The access key for your Azure storage account.
          - `azurestorageaccountname`: The name of your Azure storage account. This name is used in conjunction with the endpoint suffix to form the base URL for your ABFSS resources.
    
        

    === "WASBS"

        The manifest files provided below are the templates for securely storing WASBS credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_wasbs_read.yaml"
            --8<-- "examples/resources/instance_secret/wasbs/wasbs_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_wasbs_read_write.yaml"
            --8<-- "examples/resources/instance_secret/wasbs/wasbs_rw.yaml"
            ```

        To configure the above WASBS instance-secret templates, the details required are provided below. Ensure that you replace each placeholder (e.g., `${wasbs-depot-name}`, `${azure-endpoint-suffix}`) with the actual values pertaining to your Azure account and WASBS configuration. 

          - `name`: Define the name of your Instance secret `${wasbs-depot-name}-${acl}`. For instance, if your `${wasbs-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.
          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `azureendpointsuffix`: The endpoint suffix for your Azure storage account. 
          - `azurestorageaccountkey`: The access key for your Azure storage account. 
          - `azurestorageaccountname`: The name of your Azure storage account. This name is used in conjunction with the endpoint suffix to form the base URL for your WASBS resources.

    === "GCS"

        The manifest files provided below are the templates for securely storing GCS credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_gcs_read.yaml"
            --8<-- "examples/resources/instance_secret/gcs/gcs_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_gcs_read_write.yaml"
            --8<-- "examples/resources/instance_secret/gcs/gcs_rw.yaml"
            ```

        To configure the above GCS instance-secret templates, the details required are provided below. In the chosen template, replace the placeholders (`${gcs-depot-name}`, `${project-id}`, `${email}`, `${gcskey_json}`, and optionally `${description}`) with the actual values.

          - `name`: Define the name of your Instance secret `${gcs-depot-name}-${acl}`. For instance, if your `${gcs-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.
          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `projectid`: The unique identifier of the Google Cloud project that your GCS bucket resides in. You can find this information in the Google Cloud Console under the 'Project Info' section.
          - `email`:  The email address associated with the Google Cloud service account that will be used for accessing GCS. This service account should have the necessary permissions to perform operations on the GCS bucket.
          - `gcskey_json`: The JSON key file of the Google Cloud service account. This file contains the private key and other credentials that are required for authenticating the service account. It can be obtained by creating a service account key in the Google Cloud Console.


    === "S3"

        The manifest files provided below are the templates for securely storing GCS credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_s3_read.yaml" 
            --8<-- "examples/resources/instance_secret/s3/s3_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_s3_read_write.yaml"
            --8<-- "examples/resources/instance_secret/s3/s3_rw.yaml"
            ```

        To configure the above S3 instance-secret templates, the details required are provided below. Ensure that you replace each placeholder (e.g., `${s3-depot-name}`, `${access-key-id}`) with the actual values pertaining to your AWS account and S3 configuration. 

          - `name`: Define the name of your Instance secret `${s3-depot-name}-${acl}`. For instance, if your `${s3-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.
          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `access-key-id`: Your access key ID. This key serves as an identifier for your IAM user or role.
          - `awsaccesskeyid`: AWS-specific access key ID, required for authenticating requests made to AWS services.
          - `awssecretaccesskey`: The secret access key for AWS. It's used in conjunction with the AWS access key ID to sign programmatic requests to AWS.
          - `secretkey`: The secret key associated with your access key ID. Together, they authenticate requests to AWS services.

=== "Data Warehouse"

    A data warehouse serves as a centralized repository for structured data, enabling efficient query and analysis. Instance-Secrets can be configured for securely storing credentials for the Amazon Redshift, Snowflake, and Google Bigquery Warehouses in the following ways:

    === "Bigquery"

        The manifest files provided below are the templates for securely storing Google Bigquery credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_bigquery_read.yaml" 
            --8<-- "examples/resources/instance_secret/bigquery/bigquery_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_bigquery_read_write.yaml"
            --8<-- "examples/resources/instance_secret/bigquery/bigquery_rw.yaml"
            ```
        
        To create an instance-secret for securely storing Google BigQuery credentials, the details required are provided below. Ensure that you replace each placeholder (e.g., `${bigquery-depot-name}`, `${projectid}`, `${email}`) with the actual values pertaining to your Google Cloud account and BigQuery configuration.

          - `name`: Define the name of your Instance secret `${bigquery-depot-name}-${acl}`. For instance, if your `${bigquery-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.
  
          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `projectid`: Your BigQuery project ID. This identifier is associated with your Google Cloud project and is required for authenticating requests made to BigQuery services.

          - `email`: The email ID associated with your BigQuery account. This information is essential for specifying the user account that will be used to access BigQuery resources.

          - `json_keyfile`: The JSON key file of the Google Cloud service account. This file contains the private key and other credentials that are required for authenticating the service account. It can be obtained by creating a service account key in the Google Cloud Console.

        
    === "Redshift"

        The manifest files provided below are the templates for securely storing Amazon Redshift credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_redshift_read.yaml" 
            --8<-- "examples/resources/instance_secret/redshift/redshift_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_redshift_read_write.yaml"
            --8<-- "examples/resources/instance_secret/redshift/redshift_rw.yaml"
            ```

        To create an instance-secret for securely storing Amazon Redshift credentials, the details required are provided below. Ensure that you replace each placeholder (e.g., ${redshift-depot-name}, ${username}, ${access key}) with the actual values pertaining to your Redshift and AWS account configuration.

          - `name`: Define the name of your Instance secret `${redshift-depot-name}-${acl}`. For instance, if your `${redshift-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your Redshift username. This is the identifier for your Redshift user account.

          - `password`: The password associated with your Redshift username. It is used for authenticating requests to your Redshift cluster.

          - `awsaccesskey`: AWS-specific access key ID, required for authenticating requests made to AWS services, including Redshift.

          - `awssecretaccesskey`: The secret access key for AWS. It's used in conjunction with the AWS access key ID to sign programmatic requests to AWS, including Redshift.

    === "Snowflake"

        The manifest files provided below are the templates for securely storing Snowflake credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_snowflake_read.yaml" 
            --8<-- "examples/resources/instance_secret/snowflake/snowflake_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_snowflake_read_write.yaml"
            --8<-- "examples/resources/instance_secret/snowflake/snowflake_rw.yaml"
            ```


        To create an instance-secret for securely storing Snowflake credentials, the details required are provided below. Ensure that you replace each placeholder (e.g., `${snowflake-depot-name}`, `${username}`) with the actual values pertaining to your Snowflake account configuration.

          - `name`: Define the name of your Instance secret `${snowflake-depot-name}-${acl}`. For instance, if your `${snowflake-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your Snowflake username. This is the identifier for your Snowflake user account.

          - `password`: The password associated with your Snowflake username. It is used for authenticating requests to your Snowflake account.

        

=== "SQL Database"

    SQL databases are typically centralized systems designed for structured data, organized into tables with a predefined schema. Instance-Secrets are configured to securely access and interact with the respective SQL databases.

    === "MySQL"

        The manifest files provided below are the templates for securely storing MySQL credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_mysql_read.yaml" 
            --8<-- "examples/resources/instance_secret/mysql/mysql_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_mysql_read_write.yaml"
            --8<-- "examples/resources/instance_secret/mysql/mysql_rw.yaml"
            ```


        To create an instance-secret for securely storing MySQL credentials, the details required are provided below. Ensure that you replace each placeholder (e.g., `${mysql-depot-name}`, `${username}`) with the actual values pertaining to your MySQL account configuration.

          - `name`: Define the name of your Instance secret `${mysql-depot-name}-${acl}`. For instance, if your `${mysql-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your MySQL username. This is the identifier for your MySQL user account.

          - `password`: The password associated with your MySQL username. It is used for authenticating requests to your MySQL database.

    === "MSSQL"

        The manifest files provided below are the templates for securely storing MSSQL credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_mssql_read.yaml" 
            --8<-- "examples/resources/instance_secret/mssql/mssql_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_mssql_read_write.yaml"
            --8<-- "examples/resources/instance_secret/mssql/mssql_rw.yaml"
            ```


        To create an instance-secret for securely storing MSSQL credentials, the details required are provided below. Ensure that you replace each placeholder (e.g., `${mssql-depot-name}`, `${username}`) with the actual values pertaining to your MSSQL account configuration.

          - `name`: Define the name of your Instance secret `${mssql-depot-name}-${acl}`. For instance, if your `${mssql-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your MSSQL username. This is the identifier for your MSSQL user account.

          - `password`: The password associated with your MSSQL username. It is used for authenticating requests to your MSSQL database.

    === "JDBC"

        The manifest files provided below are the templates for securely storing JDBC credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_jdbc_read.yaml" 
            --8<-- "examples/resources/instance_secret/jdbc/jdbc_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_jdbc_read_write.yaml"
            --8<-- "examples/resources/instance_secret/jdbc/jdbc_rw.yaml"
            ```

        To create an instance-secret for securely storing JDBC credentials, the details required are provided below. Ensure that you replace each placeholder (e.g., `${jdbc-depot-name}`, `${username}`) with the actual values pertaining to your JDBC account configuration.

          - `name`: Define the name of your Instance secret `${jdbc-depot-name}-${acl}`. For instance, if your `${jdbc-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your JDBC username. This is the identifier for your database user account when connecting via JDBC.

          - `password`: The password associated with your JDBC username. It is used for authenticating requests when connecting to the database via JDBC.

    === "Oracle"

        The manifest files provided below are the templates for securely storing Oracle credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_oracle_read.yaml" 
            --8<-- "examples/resources/instance_secret/oracle/oracle_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_oracle_read_write.yaml"
            --8<-- "examples/resources/instance_secret/oracle/oracle_rw.yaml"
            ```


        To create an instance-secret for securely storing Oracle credentials, the details required are provided below. Ensure that you replace each placeholder (e.g., `${oracle-depot-name}`, `${username}`) with the actual values pertaining to your Oracle account configuration.

          - `name`: Define the name of your Instance secret `${oracle-depot-name}-${acl}`. For instance, if your `${oracle-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your Oracle username. This is the identifier for your Oracle user account.

          - `password`: The password associated with your Oracle username. It is used for authenticating requests to your Oracle database.

    === "Postgres"

        The manifest files provided below are the templates for securely storing Postgres credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_postgres_read.yaml" 
            --8<-- "examples/resources/instance_secret/postgres/postgres_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_postgres_read_write.yaml"
            --8<-- "examples/resources/instance_secret/postgres/postgres_rw.yaml"
            ```

        To create an instance-secret for securely storing Postgres credentials, the details required are provided below. Ensure that you replace each placeholder (e.g., `${postgres-depot-name}`, `${username}`) with the actual values pertaining to your Postgres account configuration.

          - `name`: Define the name of your Instance secret `${postgres-depot-name}-${acl}`. For instance, if your `${postgres-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your PostgreSQL username. This is the identifier for your PostgreSQL user account.

          - `password`: The password associated with your PostgreSQL username. It is used for authenticating requests to your PostgreSQL database.
        
=== "NoSQL Database"

    NoSQL databases are designed for flexible, distributed data storage, accommodating unstructured or semi-structured data. Instance-Secrets are configured to securely access and interact with the respective NonSQL databases. 

    === "MongoDB"


        The manifest files provided below are the templates for securely storing MongoDB credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_mongodb_read.yaml" 
            --8<-- "examples/resources/instance_secret/mongodb/mongodb_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_mongodb_read_write.yaml"
            --8<-- "examples/resources/instance_secret/mongodb/mongodb_rw.yaml"
            ```

        To create an instance-secret for securely storing MongoDB credentials, the details required are provided below. Ensure that you replace each placeholder (e.g., `${mongodb-depot-name}`, `${username}`) with the actual values pertaining to your MongoDB account configuration.

          - `name`: Define the name of your Instance secret `${mongodb-depot-name}-${acl}`. For instance, if your `${mongodb-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your MongoDB username. This is the identifier for your MongoDB user account.

          - `password`: The password associated with your MongoDB username. It is used for authenticating requests to your MongoDB database.

        
=== "Streaming"

    Streaming refers to the continuous and real-time transmission of data from a source to a destination. nstance-Secrets are configured to securely access and interact with the respective Streaming platforms. 

    === "Eventhub" 

        The manifest files provided below are the templates for securely storing Eventhub credentials. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_eventhub_read.yaml" 
            --8<-- "examples/resources/instance_secret/eventhub/eventhub_r.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_eventhub_read_write.yaml"
            --8<-- "examples/resources/instance_secret/eventhub/eventhub_rw.yaml"
            ```

        To create an instance-secret for securely storing Eventhub credentials, the details required are provided below. Ensure that you replace each placeholder (e.g., `${eventhub-depot-name}`, `${EH_SHARED_ACCESS_KEY_NAME}`) with the actual values pertaining to your Azure Event Hub configuration.

          - `name`: Define the name of your Instance secret `${eventhub-depot-name}-${acl}`. For instance, if your `${eventhub-depot-name}` is alpha and the `acl`(access control list) is `rw`, then the instance secret `name` will be `alpha-rw`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `eh_shared_access_key_name`: Your Azure Event Hub shared access key name. This is the identifier for your Event Hub.

          - `eh_shared_access_key`: The shared access key associated with your Azure Event Hub. It is used for authenticating requests to your Event Hub.

</div>