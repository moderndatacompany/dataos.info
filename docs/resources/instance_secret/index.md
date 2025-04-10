---
title: Instance Secret
search:
  boost: 2
---

# Instance Secret

An Instance Secret is a [DataOS Resource](/resources/) designed for securely storing sensitive information at the DataOS Instance-level. The primary purpose of an Instance Secret is to address the inherent exposure risk associated with directly embedding such confidential data within application code or manifest files (YAML configuration files). This includes usernames, passwords, certificates, tokens, and keys. Instance Secrets establish a critical segregation between sensitive data and Resource definitions. This division minimizes inadvertent exposure during various Resource management phases, including creation, viewing, or editing.

DataOS Operators are generally responsible for creating and managing Instance Secrets for various sources within an organization. They exercise precise control over who can retrieve credentials. If any Data Product developer in the organization needs access to Instance Secrets, they can assign them relevant permission using the [Bifrost application](/interfaces/bifrost/).

!!!tip "Instance Secret in the Data Product Lifecycle"

    In the Data Product Lifecycle, Instance Secrets play a crucial role in securely managing credentials and sensitive information. They are particularly useful when your data product requires:

    - **Secure Credential Management**: Storing and managing sensitive information such as usernames, passwords, API keys, or certificates securely within an instance. For example, an instance secret can securely store the credentials needed to connect to a database, ensuring that these credentials are not exposed in the codebase or configuration files.

    - **Access Control**: Ensuring that only authorized components and services within the instance can access the credentials. For instance, an instance secret can be used to provide a web application with the credentials to access a third-party service without exposing those credentials to the broader environment.

    - **Auditing and Compliance**: Maintaining a secure and auditable method of handling sensitive data, and complying with security policies and regulatory requirements. Instance secrets ensure that credential usage is logged and can be monitored for compliance purposes.

    By using Instance Secrets, you can manage sensitive information securely and efficiently, mitigating the risk of exposing credentials while enabling seamless access to your applications and services.


<aside class="callout">
🗣️ In the DataOS ecosystem, there are two specialized Resources designed to protect sensitive information: Instance Secret and 
  <a href="/resources/secret/">Secret</a>. The Instance Secret offers a wider scope, extending across the entirety of the 
  <a href="/resources/types_of_dataos_resources/#Instance-level-resources">DataOS Instance</a>. Resources within any Workspace can 
  utilize Instance Secrets for securely retrieving sensitive data. In contrast, Secrets are limited to the 
  <a href="/resources/types_of_dataos_resources/#workspace-level-resources">Workspace level</a>, accessible exclusively within a 
  specific Workspace and only by Resources associated with that Workspace.
</aside>


## Structure of an Instance Secret manifest

The structure of the Instance Secret manifest file is outlined as follows:

<center>
<img src="/resources/instance_secret/is_structure.jpg" alt="Bifrost Governance" style="width:60rem; border: 1px solid black; padding: 5px;" />
<figcaption><i>Structure of Instance Secret manifest</i></figcaption>
</center>

## How to create an Instance Secret?

This section includes steps for creating the Instance Secret to secure credentials of commonly used data sources and hosted code repositories using DataOS CLI.

### **Data Sources**

If you want to store credentials for various data sources in an Instance Secret follow the steps given in the links below.

- [Azure Blob File System Secure (ABFSS)](/resources/depot/create_depot/abfss/)
- [Bigquery](/resources/depot/create_depot/bigquery/)
- [Elasticsearch](/resources/depot/create_depot/elasticsearch/)
- [Eventhub](/resources/depot/create_depot/eventhub/)
- [Google Cloud Storage (GCS)](/resources/depot/create_depot/gcs/)
- [Java Database Connectivity (JDBC)](/resources/depot/create_depot/jdbc/)
- [MongoDB](/resources/depot/create_depot/mongo/)
- [Microsoft SQL Server (MSSQL) or Azure SQL](/resources/depot/create_depot/mssql/)
- [MySQL](/resources/depot/create_depot/myssql/)
- [Opensearch](/resources/depot/create_depot/opensearch/)
- [Oracle](/resources/depot/create_depot/oracle/)
- [Postgres](/resources/depot/create_depot/postgres/)
- [Redshift](/resources/depot/create_depot/redshift/)
- [Simple Storage Service (Amazon S3)](/resources/depot/create_depot/s3/)
- [Snowflake](/resources/depot/create_depot/snowflake/)
- [Windows Azure Storage Blob Secure (WASBS)](/resources/depot/create_depot/wasbs/)

### **Repositories**

If you want to store credentials for hosted code repositories in an Instance Secret follow the steps given below.

- [AWS CodeCommit](/resources/depot/repositories/codecommit/)
- [Bitbucket](/resources/depot/repositories/bitbucket/)
- [Git](/resources/depot/repositories/git/)


## Configurations

Instance Secret can be configured to secure the credentials information through key-value pairs. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Instance Secret manifest](/resources/instance_secret/configurations/).

## How to use an Instance Secret?

An Instance Secret can be used to create a Depot for data source connections, Services, Workflows, or Workers. Refer to the link below for guidance on using an Instance Secret in various DataOS resources.

[How to refer to an Instance Secret in other DataOS Resources?](/resources/instance_secret/how_to_guide/recipe_1/)

## Best Practices

This section involves do's and don'ts for managing an Instance Secret.

- As an operator, it is recommended to assign a use case to a user rather than a tag, as use cases provide greater control over user permissions and enable more secure management of specific resources.

- Before deleting an Instance Secret, ensure that it is not being used by any other resources.

## FAQs


**1. Can I update an existing Instance Secret?**

Yes, you can update an Instance Secret by modifying its manifest file and re-applying it. However, ensure that dependent resources are updated accordingly. To update an Instance Secret after making changes in the manifest file, execute the following commands.

=== "apply command"

    ```bash 
    dataos-ctl resource apply -f {path-to-manifest-file} 
    ```

=== "update command"

    ```bash 
    dataos-ctl resource update -f {path-to-manifest-file}
    ```


**2. What happens if an Instance Secret is deleted?**

If an Instance Secret is deleted, any resources relying on it may lose access or experience failures. It is recommended to verify dependencies before deletion.


**3. How can I receive alerts if an Instance Secret is deleted?**
You can configure a **Monitor Resource** in DataOS along with a **Pager Resource** to receive notifications when an Instance Secret is deleted.


**4. Is there a way to restore a deleted Instance Secret?**

No, deleted secrets cannot be recovered. You must create a new Instance Secret and update all associated resources.


**5. Can multiple users access the same Instance Secret?**

Yes, anyone assigned a use case that grants permission to read an Instance Secret can access it.


**6. Can we create multiple Instance Secrets with the same name?**

No, for Instance Secrets, names must be unique. If you attempt to create a secret with a name that already exists, the system will prevent duplication. You may need to use a different name or update the existing secret if modifications are required.


**7. Where does the secrets get stored within DataOS?**

Within DataOS secrets get stored securely within the Heimdall (Heimdall001 DB). Heimdall is the governance engine for access control within DataOS, acting as the Policy Decision Point (PDP) for all authorization requests. It enforces security policies across datasets, API paths, and various applications and services, ensuring only authorized users and systems gain access. Heimdall supports both Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC), enabling flexible and fine-grained permissions. It logs every access request and decision for auditing and compliance, providing a transparent and secure framework for managing data and system interactions within DataOS.

