# Snowflake

You can scan metadata details such as schemas, tables, view details, etc., from SNOWFLAKE with depot/non-depot Scanner workflows. In this document, you will find requirements and YAML configurations to connect to SNOWFLAKE for extracting entity metadata. 

## Requirements

1. To ingest basic metadata, snowflake user must have at least `USAGE` privileges on required schemas.
2. While running the usage workflow, Metis fetches the query logs by querying  `snowflake.account_usage.query_history` table. For this the snowflake user should be granted the `ACCOUNTADMIN` role (or a role granted IMPORTED PRIVILEGES on the database).
3. If ingesting tags, the user should also have permissions to query `snowflake.account_usage.tag_references`. For this the snowflake user should be granted the `ACCOUNTADMIN` role (or a role granted IMPORTED PRIVILEGES on the database)
4. If during the ingestion you want to set the session tags, note that the user should have `ALTER SESSION` permissions.

## Depot Scan Workflow

DataOS allows you to connect to a database with JDBC driver to read data from tables using Depot. You can also scan metadata from an SNOWFLAKE-type depot with Scanner workflows.The Depot enables access to all schemas visible to the specified user in the configured database, SNOWFLAKE. 

<aside style="background-color:#FFE5CC; padding:15px; border-radius:5px;">
🗣 Ensure that the depot is created for your SNOWFLAKE database and you have `Read` access for the depot.

</aside>

**Depot Scan Workflow YAML**

You can apply database, schema, and table filter patterns while scanning metadata.

```yaml
version: v1                                            
name: snowflake03-scanner2                              
type: workflow
tags:
  - snowflake03-scanner2.0
description: The job scans schema of tables and register their metadata
workflow:
  dag:
    - name: scanner2-snowflake03                        
      description: The job scans schema from snowflake03 depot tables and register their metadata on metis2
      spec:
        stack: scanner:2.0                              
        compute: runnable-default 
        runAsUser: metis                      
        scanner:
          depot: snowflake03       # Depot name or address
          sourceConfig:
            config:
          #     schemaFilterPattern:
          #       includes:
          #         - Public
          #     tableFilterPattern: 
          #       includes:
          #         - department
          #         - ^EMPLOYEE
              markDeletedTables: false
              includeTables: true
              includeViews: true
```

## Non-Depot Scan Workflow

The non-depot Scanner workflow will help you connect with SNOWFLAKE to extract metadata details. You need to provide source connection details and configuration settings, such as metadata type and filter patterns, to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: This is source to be scanned; `snowflake`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `MySnowflakeSource`

### **Source Connection Properties**

- **Username**: Specify the User to connect to Snowflake. It should have enough privileges to read all the metadata.
- **Password**: Password to connect to Snowflake.
- **Account**: Snowflake account identifier uniquely identifies a Snowflake account within your organization, as well as throughout the global network of Snowflake-supported cloud platforms and cloud regions. If the Snowflake URL is `https://xyz1234.us-east-1.gcp.snowflakecomputing.com`, then the account is `xyz1234.us-east-1.gcp`.
- **Role (Optional)**: You can specify the role of user that you would like to ingest with, if no role is specified the default roles assigned to user will be selected.
- **Warehouse**: Snowflake warehouse is required for executing queries to fetch the metadata. Enter the name of warehouse against which you would like to execute these queries.
- **Database (Optional)**: The database of the data source is an optional parameter, if you would like to restrict the metadata reading to a single database. If left blank, OpenMetadata ingestion attempts to scan all the databases.
- **Private Key (Optional)**: If you have configured the key pair authentication for the given user you will have to pass the private key associated with the user in this field. You can checkout **[this](https://docs.snowflake.com/en/user-guide/key-pair-auth)** doc to get more details about key-pair authentication.
    - The multi-line key needs to be converted to one line with `\n` for line endings i.e. `----BEGIN ENCRYPTED PRIVATE KEY-----\nMII...\n...\n-----END ENCRYPTED PRIVATE KEY-----`
- **Snowflake Passphrase Key (Optional)**: If you have configured the encrypted key pair authentication for the given user you will have to pass the paraphrase associated with the private key in this field. You can checkout **[this](https://docs.snowflake.com/en/user-guide/key-pair-auth)** doc to get more details about key-pair authentication.
- **Include Temporary and Transient Tables**: Optional configuration for ingestion of `TRANSIENT` and `TEMPORARY` tables, By default, it will skip the `TRANSIENT` and `TEMPORARY` tables.
- **Connection Options (Optional)**: Enter the details for any additional connection options that can be sent to Snowflake during the connection. These details must be added as Key-Value pairs.
- **Connection Arguments (Optional)**: Enter the details for any additional connection arguments such as security or protocol configs that can be sent to Snowflake during the connection. These details must be added as Key-Value pairs.
    - In case you are using Single-Sign-On (SSO) for authentication, add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "sso_login_url"`
    - In case you authenticate with SSO using an external browser popup, then add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "externalbrowser"`

**Depot Scan Workflow YAML**

In this example, sample source connections and configuration settings are provided.

```yaml
version: v1
name: scanner2-snowflake-depot-k
type: workflow
tags:
  - scanner
  - snowflake
description: The job scans schema tables and register data
workflow:
  dag:
    - name: scanner2-snowflake-depot-job
      description: The job scans schema from snowflake tables and register data to metis2
      spec:
        tags:
          - scanner2
        stack: scanner:2.0
        compute: runnable-default
				runAsUser: metis
        scanner:
          type: snowflake
          source: sampleXyz
          sourceConnection:               # source connection properties       
            config:
              type: Snowflake
              username: <username>
              password: <password>
              warehouse: WAREHOUSE
              account: NB48718.central-india.azure
          sourceConfig:                   # source configuration properties
            config:
              type: DatabaseMetadata
              schemaFilterPattern:
                excludes:
                  - mysql.*
                  - information_schema.*
                  - performance_schema.*
                  - sys.*
              markDeletedTables: false
```

> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
