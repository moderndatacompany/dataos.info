# Snowflake Non-Depot Scan Workflow

You can scan metadata from a SNOWFLAKE database with non-depot Scanner workflow.

## Requirements

To scan the SNOWFLAKE depot, you need the following:

1. Ensure that the depot is created and you have ‘Read’ access for the depot.
2. To ingest basic metadata, snowflake user must have at least `USAGE` privileges on required schemas.
3. While running the usage workflow, Metis fetches the query logs by querying `snowflake.account_usage.query_history` table. For this the snowflake user should be granted the `ACCOUNTADMIN` role (or a role granted IMPORTED PRIVILEGES on the database).
4. If ingesting tags, the user should also have permissions to query `snowflake.account_usage.tag_references`. For this the snowflake user should be granted the `ACCOUNTADMIN` role (or a role granted IMPORTED PRIVILEGES on the database)
5. If during the ingestion you want to set the session tags, note that the user should have `ALTER SESSION` permissions.

## Scanner Workflow

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML. You need to provide source connection details and configuration settings such as  metadata type and filter patterns to include/exclude assets for metadata scanning.
    
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
    

    > Note: Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
 
 
 
1. After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
    
    
    > 🗣 Filtering for the Scanner workflow works on a hierarchy level; First, it will filter all given schemas and then the table in that schema if present.
    
    