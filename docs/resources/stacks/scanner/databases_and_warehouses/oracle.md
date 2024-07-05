# Scanner for Oracle
## Requirements

- Credentials to connect to Oracle database.
- To extract metadata, the MySQL user needs to have access to the `INFORMATION_SCHEMA`.
- Metadata Scan is supported for 12c, 18c, 19c, and 21c versions.
- To ingest metadata from oracle user must have `CREATE SESSION` privilege for the user.

## Depot Scan Workflow

DataOS allows you to connect to a database with JDBC driver to read data from tables using Depot. You can also scan metadata from an Oracle-type depot with Scanner workflows.The Depot enables access to all schemas visible to the specified user in the configured database, Oracle. 

<aside class="callout">
🗣 Ensure that the depot is created for your Oracle database and you have `Read` access for the depot.

</aside>

You can apply database, schema, and table filter patterns while scanning metadata.

```yaml
version: v1
name: oracle-scanner
type: workflow
tags:
  - oracle-scanner
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: oracle-scanner
      description: The job scans schema from oracle-scanner tables and register metadata to metis2
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        compute: runnable-default
				runAsUser: metis
        stackSpec:
          depot: oracle01          #depo name/address
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

After the successful workflow run, you can check the metadata of scanned Tables on Metis UI for all schemas present in the database.

<!-- ## Non-Depot Scan Workflow

You need to provide source connection details and configuration settings, such as metadata type and filter patterns to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: This is source to be scanned; `mysql`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `MySQLSource`

### Source **Connection Properties**

- **Username**: Specify the User to connect to Oracle. It should have enough privileges to read all the metadata.
- **Password**: Password to connect to Oracle.
- **Host and Port**: Enter the fully qualified hostname and port number for your Oracle deployment in the Host and Port field.
- **Oracle Connection Type** : Select the Oracle Connection Type. The type can either be `Oracle Service Name` or `Database Schema`
    - **Oracle Service Name**: The Oracle Service name is the TNS alias that you give when you remotely connect to your database and this Service name is recorded in tnsnames.
    - **Database Schema**: The name of the database schema available in Oracle that you want to connect with.
- **Oracle instant client directory**: The directory pointing to where the `instantclient` binaries for Oracle are located. In the ingestion Docker image we provide them by default at `/instantclient`. If this parameter is informed (it is by default), we will run the **[thick oracle client](https://python-oracledb.readthedocs.io/en/latest/user_guide/initialization.html#initializing-python-oracledb)**. We are shipping the binaries for ARM and AMD architectures from **[here](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html)** and **[here](https://www.oracle.com/database/technologies/instant-client/linux-arm-aarch64-downloads.html)** for the instant client version 19.
- **Connection Options (Optional)**: Enter the details for any additional connection options that can be sent to Oracle during the connection. These details must be added as Key-Value pairs.
- **Connection Arguments (Optional)**: Enter the details for any additional connection arguments such as security or protocol configs that can be sent to Oracle during the connection. These details must be added as Key-Value pairs.
    - In case you are using Single-Sign-On (SSO) for authentication, add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "sso_login_url"`
    - In case you authenticate with SSO using an external browser popup, then add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "externalbrowser"`

### **Non-Depot Scan Workflow YAML**

In this example, sample source connection and configuration settings are provided.

```yaml

``` -->

> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
> 