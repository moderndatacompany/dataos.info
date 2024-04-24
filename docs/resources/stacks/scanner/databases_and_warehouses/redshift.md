# Scanner for Redshift

You can scan metadata from Redshift with depot/non depot Scanner workflows. In this document, find requirements and YAML configurations to connect to Redshift for extracting entity metadata. 

## Requirements

To scan metadata from a Redshift data source, you need the following:

1. Credentials to connect to Redshift database.
2. `SVV_TABLE_INFO` View contains summary information for tables in the Redshift database and is visible only to superusers. You need permissions to query the view while scanning metadata from Scanner workflow.
3. Redshift user must grant `SELECT`privilege on table [SVV_TABLE_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLE_INFO.html) to fetch the metadata of tables and views.

## Depot Scan Workflow

DataOS allows you to connect to a database with JDBC driver to read data from tables using Depot. You can also scan metadata from an REDSHIFT-type depot with Scanner workflows.The Depot enables access to all schemas visible to the specified user in the configured database, REDSHIFT. 

< aside class="callout">
🗣 Ensure that the depot is created for your MySQL database and you have `Read` access.</aside>

**Depot Scan Workflow YAML**

You can apply database, schema, and table filter patterns while scanning metadata.

```yaml
version: v1
name: redshift-scanner2
type: workflow
tags:
  - redshift-scanner2.0
description: The workflow scans schema tables and register metadata
workflow:
  dag:
    - name: scanner2-redshift
      description: The job scans schema from redshift depot tables and register metadata to metis2
      spec:
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        scanner:
          depot: demoprepredshift
          sourceConfig:
            config:
              markDeletedTables: false
              includeTables: true
              includeViews: false
              schemaFilterPattern:
                includes:
                  - Public
              tableFilterPattern:
                includes:
                  - Customer
```

## Non-Depot Scan Workflow

The non-depot Scanner workflow will help you to connect with Redshift to extract metadata details. You need to provide source connection details and configuration settings, such as metadata type and filter patterns to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: This is source to be scanned; `redshift`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `MyRedshiftSource`

### **Source Connection Properties**

- **Username**: Specify the User to connect to Redshift. It should have enough privileges to read all the metadata.
- **Password**: Password to connect to Redshift.
- **Database (Optional)**: The database of the data source is an optional parameter, if you would like to restrict the metadata reading to a single database.
- **Connection Options (Optional)**: Enter the details for any additional connection options that can be sent to Redshift during the connection. These details must be added as Key-Value pairs.
- **Connection Arguments (Optional)**: Enter the details for any additional connection arguments such as security or protocol configs that can be sent to Redshift during the connection. These details must be added as Key-Value pairs.
    - In case you are using Single-Sign-On (SSO) for authentication, add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "sso_login_url"`
    - In case you authenticate with SSO using an external browser popup, then add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "externalbrowser"`

**Non-Depot Scan Workflow YAML**

In this example, sample source connections and configuration settings are provided.

```yaml
version: v1
name: redshift-nd-scanner2
type: workflow
tags:
  - redshift-scanner
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: redshift-scanner2
      description: The job scans schema from redshift via non depot method to scan tables and register their metadata on metis2
      spec:
        tags:
          - scanner2
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        scanner:
          type: redshift
          source: RedshiftSource_ND
          sourceConnection:
            config:
              type: Redshift
              hostPort: tmdc-redshift.cccfst2pznzg.us-east-2.redshift.amazonaws.com:5439
              username: XXXXXX
              password: XXXXXXXXXXXXXX
              database: demoprep
              # If we want to iterate over all databases, set it to true
              # ingestAllDatabases: true
          sourceConfig:
            config:
              markDeletedTables: **false**
              includeTables: **true**
              includeViews: **true**
              # includeTags: true
              # databaseFilterPattern:
              #   includes:
              #     - database1
              #     - database2
              #   excludes:
              #     - database3
              #     - database4
              schemaFilterPattern:
                includes:
                  - Public
              #     - schema2
              #   excludes:
              #     - schema3
              #     - schema4
              # tableFilterPattern:
              #   includes:
              #     - table1
              #     - table2
              #   excludes:
              #     - table3
              #     - table4
```

> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
