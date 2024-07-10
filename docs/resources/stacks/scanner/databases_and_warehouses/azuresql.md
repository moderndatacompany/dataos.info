# Scanner for AzureSQL

You can scan metadata from AzureSQL with depot/non-depot Scanner workflows. In this document, find requirements and YAML configurations to connect to AzureSQL for extracting entity metadata.

## Requirements

To scan metadata from AzureSQL, you need the following:

1. Ensure that you have added your current IP address on Azure SQL firewall rules. Checkout **[this](https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure?view=azuresql#use-the-azure-portal-to-manage-server-level-ip-firewall-rules)** document on how to whitelist your IP using azure portal.
2. AzureSQL database user must grant `SELECT` privilege to fetch the metadata of tables and views.

## Depot Scan Workflow

DataOS allows you to connect to AzureSQL database using Depot. The Depot enables access to all schemas visible to the specified user in the configured database.

<aside class="callout">
🗣 Ensure that the depot is created for your Azure SQL database and you have `Read` access for the depot.

</aside>

### **Scanner YAML**

```yaml
version: v1
name: azuresql-scanner2
type: workflow
tags:
  - azuresql-scanner2.0
description: Scanner workflow to scan schema tables and register metadata in Metis DB
workflow:
  dag:
    - name: scanner2-azuresql
      description: The job scans schema from azuresql depot tables and register metadata to metis2
      spec:
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        stackSpec:
          depot: azuresql
          sourceConfig:                 # Apply filter as per requirement
            config:
              databaseFilterPattern:
                includes:
                  - <databasename> 
                excludes:
                  - <databasename> 
              schemaFilterPattern:
                includes:
                  - <schemaname>
                excludes:
                  - <schemaname>
              tableFilterPattern:
                includes:
                  - <schemaname>
                excludes:
                  - <schemaname>
```

<!-- ## Non-Depot Scan Workflow

You need to provide source connection details and configuration settings, such as metadata type and filter patterns to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: This is source to be scanned; `azuresql`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `AzuresqlSource`

### ** Source Connection Properties**

- **Username**: Specify the User to connect to AzureSQL. It should have enough privileges to read all the metadata.
- **Password**: Password to connect to AzureSQL.
- **Host and Port**: Enter the fully qualified hostname and port number for your AzureSQL deployment in the Host and Port field.
- **Database**: The database of the data source is an optional parameter, if you would like to restrict the metadata reading to a single database. If left blank, OpenMetadata ingestion attempts to scan all the databases.
- **Driver**: Connecting to AzureSQL requires ODBC driver to be installed. Specify ODBC driver name in the field. You can download the ODBC driver from **[here](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)**. In case of docker or kubernetes deployment this driver comes out of the box with version `ODBC Driver 18 for SQL Server`.
- **Connection Options (Optional)**: Enter the details for any additional connection options that can be sent to AzureSQL during the connection. These details must be added as Key-Value pairs.
- **Connection Arguments (Optional)**: Enter the details for any additional connection arguments such as security or protocol configs that can be sent to AzureSQL during the connection. These details must be added as Key-Value pairs.
    - In case you are using Single-Sign-On (SSO) for authentication, add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "sso_login_url"`
    - In case you authenticate with SSO using an external browser popup, then add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "externalbrowser"`

## Non-Depot Scan YAML

```yaml

``` -->