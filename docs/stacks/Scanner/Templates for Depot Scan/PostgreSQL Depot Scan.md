# PostgreSQL Depot Scan

DataOS allows you to connect to the PostgreSQL database to access data from the tables using Depots. The Depot enables access to all schemas visible to the specified service in the configured database. You can scan metadata from an PostgreSQL depot with Scanner workflows.

## Requirements

To scan the PostgreSQL depot, you need the following:

1. Ensure that the depot is created for your PostgreSQL database and you have `read` access for the depot.
2. You should have enough access to fetch the required metadata from your PostgreSQL database.
3. The user needs to have both `CONNECT` and `SELECT`  privileges  on the database.

## Scanner Workflow

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB. 

1. Create and apply the Scanner YAML. You can apply database, schema, and table filter patterns while scanning metadata
    
    we can run the Scanner workflow with or without a filter pattern. 
    
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
            scanner:
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
    
  
    > 💡 FilterPatterns supports  Regex in include and exclude expressions.
    
    
    
2. After the successful workflow run, you can check the metadata of scanned Tables on Metis U for all schemas present in the database.
    
    
    > Note: Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
    > 
    
    
    > 🗣 Filtering for the Scanner workflow works on a hierarchy level; First, it will filter all given schemas and then the table in that schema if present.
    
    