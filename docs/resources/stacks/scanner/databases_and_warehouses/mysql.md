# Scanner for MySQL
You can scan metadata details, such as schemas, tables, view details, etc., from MSSQL with depot/non-depot Scanner workflows. In this document, you will find requirements and YAML configurations to connect to MySQL for extracting entity metadata. 

## Requirements

- Credentials to connect to the MySQL database.
- To extract metadata, the MySQL user needs to have access to the `INFORMATION_SCHEMA`.
- Metadata Scan is supported for MySQL (version 8.0.0 or greater)
- MySQL user must grant `SELECT` privilege to fetch the metadata of tables and views.

## Depot Scan Workflow

DataOS allows you to connect to a database with the JDBC driver to read data from tables using Depot. You can also scan metadata from a MySQL-type depot with the  Scanner workflows. The Depot enables access to all schemas visible to the specified user in the configured database, MySQL. 

<aside class="callout">
🗣 Ensure that the depot is created for your MySQL database and that you have `read` access to the depot.

</aside>

You can apply database, schema, and table filter patterns while scanning metadata.

```yaml
version: v1
name: mysql-scanner
type: workflow
tags:
  - mysql-scanner
description: The workflow scans schema tables and registers metadata
workflow:
  dag:
    - name: mysql-scanner
      description: The job scans schema from MySQL depot tables and registers metadata to metis2
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        compute: runnable-default
				runAsUser: metis
        stackSpec:
          depot: mysql01
          sourceConfig:
            config:
              markDeletedTables: false
              includeTables: true
              includeViews: true
              databaseFilterPattern:
	              includes:
	                  - database1
	                  - database2
	              schemaFilterPattern:
	                includes:
	                  - schema1
	                  - schema2
	              tableFilterPattern:
	                includes:
	                  - table1
	                  - table2
	             
```

<!-- ## Non-Depot Scan Workflow

The non-depot Scanner workflow will help you connect with MySQL to extract metadata details. You need to provide source connection details and configuration settings, such as metadata type and filter patterns, to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: This is source to be scanned; `mysql`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `MySQLSource`

### **Source Connection Properties**

- **Username**: Specify the User to connect to MySQL. It should have enough privileges to read all the metadata.
- **Password**: Password to connect to MySQL.
- **Host and Port**: Enter the fully qualified hostname and port number for your MySQL deployment in the Host and Port field.
- **databaseName**: Optional name to give to the database in OpenMetadata. If left blank, we will use default as the database name.
- **databaseSchema**: databaseSchema of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single databaseSchema. When left blank, OpenMetadata Ingestion attempts to scan all the databaseSchema.
- **sslCA**: Provide the path to ssl ca file.
- **sslCert**: Provide the path to ssl client certificate file (ssl_cert).
- **sslKey**: Provide the path to ssl client certificate file (ssl_key).
- **Connection Options (Optional)**: Enter the details for any additional connection options that can be sent to Athena during the connection. These details must be added as Key-Value pairs.
- **Connection Arguments (Optional)**: Enter the details for any additional connection arguments such as security or protocol configs that can be sent to Athena during the connection. These details must be added as Key-Value pairs.
    - In case you are using Single-Sign-On (SSO) for authentication, add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "sso_login_url"`
    - In case you authenticate with SSO using an external browser popup, then add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "externalbrowser"`

### Non-Depot Scan Workflow YAML

In this example, sample source connections and configuration settings are provided.

```yaml

``` -->

> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
> 

