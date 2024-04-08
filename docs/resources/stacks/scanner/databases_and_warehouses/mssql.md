# Scanner for MSSQL
You can scan metadata details such as schemas, tables, view details etc. from MSSQL with depot/non-depot Scanner workflows. In this document, find requirements and YAML configurations to connect to MSSQL for extracting entity metadata. 

## Requirements

- Credentials to connect to MSSQL database.
- To extract metadata, the MSSQL user needs to have access to the `INFORMATION_SCHEMA`.
- MSSQL User must grant `SELECT` privilege to fetch the metadata of tables and views.

## Depot Scan Workflow

DataOS allows you to connect to a database with JDBC driver to read data from tables using Depot. You can also scan metadata from an MSSQL-type depot with Scanner workflows.The Depot enables access to all schemas visible to the specified user in the configured database, MSSQL. 

<aside class="callout">
🗣 Ensure that the depot is created for your MSSQL database and you have `Read` access for the depot.

</aside>

You can apply database, schema, and table filter patterns while scanning metadata.

```yaml
version: v1
name: mssql-scanner2
type: workflow
tags:
  - mssql-scanner2.0
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: scanner2-mssql
      description: The job scans schema from Mssql depot tables and register metadata to metis2
      spec:
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        scanner:
          depot: mssql01
          sourceConfig:
            config:
              markDeletedTables: false
              includeTables: true
              includeViews: true
              databaseFilterPattern:
	              includes:
	                  - database1
	                  - database2
	                excludes:
	                  - database3
	                  - database4
	              schemaFilterPattern:
	                includes:
	                  - schema1
	                  - schema2
	                excludes:
	                  - schema3
	                  - schema4
	              tableFilterPattern:
	                includes:
	                  - table1
	                  - table2
	                excludes:
	                  - table3
	                  - table4
```

<!-- ## Non-Depot Scan Workflow

You need to provide source connection details and configuration settings, such as metadata type and filter patterns to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: This is source to be scanned; `mssql`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `MSSQLSource`

### Source **Connection Properties**

- **Type:** Specify source type**;** MSSQL
- **Connection Scheme**: Defines how to connect to MSSQL. We support `mssql+pytds`, `mssql+pyodbc`, and `mssql+pymssql`.
- **Username**: Specify the User to connect to MSSQL. It should have enough privileges to read all the metadata.
- **Password**: Password to connect to MSSQL.
- **Host and Port**: Enter the fully qualified hostname and port number for your MSSQL deployment in the Host and Port field.
- **URI String**: In case of a `pyodbc` connection.
- **Database (Optional)**: The database of the data source is an optional parameter, if you would like to restrict the metadata reading to a single database. If left blank, OpenMetadata ingestion attempts to scan all the databases.
- **Connection Options (Optional)**: Enter the details for any additional connection options that can be sent to MSSQL during the connection. These details must be added as Key-Value pairs.
- **Connection Arguments (Optional)**: Enter the details for any additional connection arguments such as security or protocol configs that can be sent to MSSQL during the connection. These details must be added as Key-Value pairs.
    - In case you are using Single-Sign-On (SSO) for authentication, add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "sso_login_url"`
    - In case you authenticate with SSO using an external browser popup, then add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "externalbrowser"`

### **Non-Depot Scan Workflow YAML**

In this example, sample source connection and configuration settings are provided.

```yaml

``` -->

> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI for all schemas present in the database.
> 

