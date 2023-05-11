# Snowflake Depot Scan

DataOS allows you to connect to the Snowflake database to access data from the tables using Depots. The  Depot enables access to all schemas visible to the specified service in the configured database. You can scan metadata from a SNOWFLAKE-type depot with Scanner workflows.

## Requirements

To scan the SNOWFLAKE depot, you need the following:

1. Ensure that the depot is created and you have ‘Read’ access for the depot.
2. To ingest basic metadata, snowflake user must have at least `USAGE` privileges on required schemas.
3. While running the usage workflow, Metis fetches the query logs by querying `snowflake.account_usage.query_history` table. For this the snowflake user should be granted the `ACCOUNTADMIN` role (or a role granted IMPORTED PRIVILEGES on the database).
4. If ingesting tags, the user should also have permissions to query `snowflake.account_usage.tag_references`. For this the snowflake user should be granted the `ACCOUNTADMIN` role (or a role granted IMPORTED PRIVILEGES on the database)
5. If during the ingestion you want to set the session tags, note that the user should have `ALTER SESSION` permissions.

## Scanner Workflow

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML. 
    
    You can run the Scanner workflow with or without a filter pattern. 
    
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
    
2. After the successful workflow run, you can check the metadata of scanned Tables on Metis UI for all schemas in the database.