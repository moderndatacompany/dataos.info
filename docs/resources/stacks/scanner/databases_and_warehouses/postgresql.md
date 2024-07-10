# Scanner for PostgreSQL
You can scan metadata from PostgreSQL with depot/non-depot Scanner workflows. In this document, find requirements and YAML configurations to connect to PostgreSQL for extracting entity metadata. 

## Requirements

To scan the PostgreSQL depot, you need the following:

- The user should have both `CONNECT` and `SELECT`  privileges  on the database.

## Depot Scan Workflow 
DataOS allows you to connect to a database with JDBC driver to read data from tables using Depot. You can also scan metadata from an POSTGRES-type depot with Scanner workflows.The Depot enables access to all schemas visible to the specified user in the configured database, PostGRES.

<aside class="callout">
Ensure that the depot is created for your PostgreSQL database and you have `read` access for the depot.
</aside>
**Depot Scan Workflow YAML**


```yaml
version: v1
name: demopreppostgres-scanner2
type: workflow
tags:
  - demopreppostgres-scanner2.0
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: scanner2-demopreppostgres
      description: The job scans schema from demopreppostgres depot tables and register metadata to metis2
      spec:
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        stackSpec:
          depot: demopreppostgres          # Postgres depot name
          # sourceConfig:
          #   config:
          #     schemaFilterPattern:
          #       includes:
          #         - Public
          #     tableFilterPattern:
          #       includes:
          #         - F_delivery
          #         - d_
```

## Non Depot Scan Workflow

You need to provide source connection details and configuration settings, such as metadata type and filter patterns to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: This is the source to be scanned; `postgres`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `PostgresSource_ND01`

### **Source Connection Properties**

- **Username**: Specify the User to connect to Postgres. It should have enough privileges to read all the metadata.
- **Password**: Password to connect to Postgres.
- **Host and Port**: Enter the fully qualified hostname and port number for your Postgres deployment in the Host and Port field.
- **Connection Options (Optional)**: Enter the details for any additional connection options that can be sent to Postgres during the connection. These details must be added as Key-Value pairs.
- **Connection Arguments (Optional)**: Enter the details for any additional connection arguments such as security or protocol configs that can be sent to Postgres during the connection. These details must be added as Key-Value pairs.
    - In case you are using Single-Sign-On (SSO) for authentication, add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "sso_login_url"`
    - In case you authenticate with SSO using an external browser popup, then add the `authenticator` details in the Connection Arguments as a Key-Value pair as follows: `"authenticator" : "externalbrowser"`

**Non-Depot Scan Workflow YAML**

```yaml
version: v1
name: postgres-nd-scanner2
type: workflow
tags:
  - postgres-nd-scanner2
description: The workflow scans schema tables and register metadata
workflow:
  dag:
    - name: postgres-scanner2-01
      description: The job scans schema from postgres database and register metadata to metis2
      spec:
        tags:
          - scanner2.0
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        scanner:
          type: postgres
          source: PostgresSource_ND01
          sourceConnection:
            config:
              type: Postgres
              username: postgres
              password: <password>
              hostPort: postgres.cdn8jsf4zhwg.us-east-1.rds.amazonaws.com:5432
          sourceConfig:
            config:
              markDeletedTables: true
              includeTables: true
              includeViews: true
              databaseFilterPattern:
                includes:
                  - postgres
              schemaFilterPattern:
                includes:
                  - PUBLIC
              tableFilterPattern:
                includes:
                  - d_
```

> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
