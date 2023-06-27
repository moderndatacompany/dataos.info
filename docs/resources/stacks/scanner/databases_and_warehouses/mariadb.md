# MariaDB

ou can scan metadata details such as schemas, tables, view details etc. from MariaDB with depot/non-depot Scanner workflows. In this document, find requirements and YAML configurations to connect to MariaDB for extracting entity metadata. 

## Requirements

- Credentials to connect to MariaDB database.
- To extract metadata, the MariaDB user needs to have access to the `INFORMATION_SCHEMA`. By default a user can see only the rows in the `INFORMATION_SCHEMA` that correspond to objects for which the user has the proper access privileges.

## Depot Scan Workflow

DataOS allows you to connect to a database with JDBC driver to read data from tables using Depot. The Depot enables access to all schemas visible to the specified user in the configured database, MariaDB. You can scan metadata from an JDBC-type depot with Scanner workflows.


<aside style="background-color:#FFE5CC; padding:15px; border-radius:5px;">
Ensure that the depot is created for your MariaDB database and you have `Read` access for the depot.
</aside>


**Depot Scan Workflow YAML**

You can apply database, schema, and table filter patterns while scanning metadata.

```yaml
version: v1
name: mariadb-scanner2
type: workflow
tags:
  - mariadb-scanner2.0
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: scanner2-mariadb
      description: The job scans schema from mariadb depot tables and register metadata to metis2
      spec:
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        scanner:
          depot: mariadb01
          # sourceConfig:
          #   config:
          #     schemaFilterPattern:
          #       includes:
          #         - mariadb     
          #   
```


## Non-Depot Scan Workflow

You need to provide source connection details and configuration settings, such as metadata type and filter patterns, to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: This is the source to be scanned; `mariadb`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `MariaDBSource`

### **Source Connection Properties**

- **Type:** Specify source type**;** `MariaDB`
- **Username**: Specify the User to connect to MariaDB. It should have enough privileges to read all the metadata.
- **Password**: Password to connect to MariaDB.
- **Host and Port**: Enter the fully qualified hostname and port number for your MariaDB deployment in the Host and Port field.
- **databaseSchema**: databaseSchema of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single databaseSchema.
- **Connection Options (Optional)**: Enter the details for any additional connection options that can be sent to MariaDB during the connection. These details must be added as Key-Value pairs.
- **Connection Arguments (Optional)**: Enter the details for any additional connection arguments such as security or protocol configs that can be sent to MariaDB during the connection. These details must be added as Key-Value pairs.
    - In case you are using Single-Sign-On (SSO) for authentication, add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "sso_login_url"`
    - In case you authenticate with SSO using an external browser popup, then add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "externalbrowser"`

**Non-Depot Scan Workflow YAML**


In this example, sample source connection and configuration settings are provided.

```yaml
version: v1
name: scanner2-mariadb                           # Scanner workflow name
type: workflow
tags:
  - scanner
  - mariadb
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: scanner2-mariadb                           
      description: The job scans schema from mariadb tables and registers their metadata to metis2
      spec:
        tags:
          - scanner2
        stack: scanner:2.0                            
        compute: runnable-default                     
        runAsUser: metis
        scanner:
          type: mariadb
          source: MariaDBSource
          sourceConnection:
            config:
              type: MariaDB
              username: xxxxxx
              password: xxxxxxxxxxxxxxxxxxxxx
              hostPort: mariadbdev.cb98qlrtcmrz.us-east-1.rds.amazonaws.com:3306
              # databaseSchema: schema
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

> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
