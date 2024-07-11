---
title: Instance Secret
search:
  boost: 2
---

# :resources-instancesecret: Instance Secret

An Instance Secret is a [DataOS Resource](/resources/) designed for securely storing sensitive information at the DataOS instance level. This encompasses sensitive information like usernames, passwords, certificates, tokens, and keys. The primary purpose of Instance Secret is to address the inherent exposure risk associated with directly embedding such confidential data within application code or manifest file (YAML configuration files).

Instance secrets establish a critical segregation between sensitive data and Resource definitions. This division minimizes the chances of inadvertent exposure during various Resource management phases, including creation, viewing, or editing. By leveraging Instance Secrets, data developers ensure the safeguarding of sensitive information, thereby mitigating security vulnerabilities inherent in their data workflows. 

Operators can exercise precise control over who can retrieve credentials from Secrets, if in your organisation any data developer need access to secrets you can assign them a 'read instance secret' use case using [Bifrost](/interfaces/bifrost/).

!!!tip "Instance Secret in the Data Product Lifecycle"

    In the Data Product Lifecycle, Instance Secrets play a crucial role in securely managing credentials and sensitive information. They are particularly useful when your data product requires:

    - **Secure Credential Management**: Storing and managing sensitive information such as usernames, passwords, API keys, or certificates securely within an instance. For example, an instance secret can securely store the credentials needed to connect to a database, ensuring that these credentials are not exposed in the codebase or configuration files.

    - **Access Control**: Ensuring that only authorized components and services within the instance can access the credentials. For instance, an instance secret can be used to provide a web application with the credentials to access a third-party service without exposing those credentials to the broader environment.

    - **Auditing and Compliance**: Maintaining a secure and auditable method of handling sensitive data, complying with security policies and regulatory requirements. Instance secrets ensure that credential usage is logged and can be monitored for compliance purposes.

    By using instance secrets, you can manage sensitive information securely and efficiently, mitigating the risk of exposing credentials while enabling seamless access for your applications and services.

<aside class="callout">

🗣️ In the DataOS ecosystem, there are two specialized Resources designed to protect sensitive information: Instance Secret and <a href="/resources/secret/">Secret</a>. The Instance Secret offers a wider scope, extending across the entirety of the <a href="/resources/types_of_dataos_resources/#instance-level-resources">DataOS Instance</a>. Resources within any Workspace can utilize Instance Secrets for securely retrieving sensitive data. In contrast, Secrets are limited to the <a href="/resources/types_of_dataos_resources/#workspace-level-resources">Workspace level</a>, accessible exclusively within a specific Workspace and only by Resources associated with that Workspace.
</aside>

## **Structure of an Instance Secret manifest**

The structure of the Instance Secret manifest file is outlined as follows:

![Instance Secret Manifest Structure](/resources/instance_secret/instance_secret_manifest_structure.jpg)


## Templates

To facilitate the creation of Instance Secret accessing commonly used data sources, we have compiled a collection of pre-defined manifest templates. These templates serve as a starting point.

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

---

## First Steps

Instance-secret Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/instance_secret/first_steps/).

## Configuration

Instance-secret can be configured to secure the credentials infromation in the form of key value pairs. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Instance Secret manifest](/resources/instance_secret/configuration/).


## Recipes

Below are some recipes to help you configure and utilize Instance Secret effectively:

[How to refer Instance Secret in other DataOS Resources?](/resources/instance_secret/how_to_guide/recipe_1/)

How to securely refer to sensitive information using Instance Secrets in various components such as Depots, Workflow, Worker, and Service?

How to access code from a private repository by referring credentials through instance secrets, ensuring secure access to sensitive code repositories?

How to create multiple instance secrets using a single manifest file, simplifying the management of secrets across different services?

---