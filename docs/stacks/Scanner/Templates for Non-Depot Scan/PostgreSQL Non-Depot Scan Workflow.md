# **PostgreSQL Non-Depot Scan Workflow**

The non-depot Scanner workflow will help you to connect with PostgreSQL to extract metadata details such as schemas, tables, view details etc.

# **Requirements**

- Credentials to connect to database.
- You should have both `CONNECT` and `SELECT`  privileges  on the PostgreSQL database.

# **Scanner Workflow**

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML. You need to provide source connection details and configuration settings such as  metadata type and filter patterns to include/exclude assets for metadata scanning.
    
    ```yaml
    version: v1
    name: postgres-nd-scanner2
    type: workflow
    tags:
      - postgres-nd-scanner2
    description: The job scans schema tables and register metadata
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
                  # database: database
              sourceConfig:
                config:
                  markDeletedTables: true
                  includeTables: true
                  includeViews: true
                  includeTags: true
                  databaseFilterPattern:
                    includes:
                      - postgres
                  #   excludes:
                  #     - database3
                  #     - database4
                  schemaFilterPattern:
                    includes:
                      - PUBLIC
                  #     - schema2
                  #   excludes:
                  #     - schema3
                  #     - schema4
                  tableFilterPattern:
                    includes:
                      - d_
                  #     - table2
                  #   excludes:
                  #     - table3
                  #     - table4
    ```
    

    > **Note:** Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
 
 

1. After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
    
    
    > 🗣 Filtering for the Scanner workflow works on a hierarchy level; First, it will filter all given schemas and then the table in that schema if present.
    
    