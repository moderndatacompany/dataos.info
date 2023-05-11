# MySQL Depot Scan

DataOS allows you to connect to the MySQL database to access data from the tables using Depots. The  Depot enables access to all schemas visible to the specified service in the configured database. You can scan metadata from an MySQL-type depot with Scanner workflows.

## Requirements

To scan the MySQL depot, you need the following:

1. Ensure that the depot is created and you have `read` access for the depot.
2. You should have access to the `INFORMATION_SCHEMA`table.
3. Metadata Scan is supported for MySQL (version 8.0.0 or greater)

## Scanner Workflow

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML. You can apply database, schema, and table filter patterns while scanning metadata.
    
    You can run the Scanner workflow with or without a filter pattern. 
    
    ```yaml
    version: v1
    name: mysql-scanner
    type: workflow
    tags:
      - mysql-scanner
    description: The job scans schema tables and register metadata
    workflow:
      dag:
        - name: mysql-scanner
          description: The job scans schema from MySQL depot tables and register metadata to metis2
          spec:
            tags:
              - scanner
            stack: scanner:2.0
            compute: runnable-default
    				runAsUser: metis
            scanner:
              depot: mysql01
              # sourceConfig:
              #   config:
              #     schemaFilterPattern:
              #       includes:
              #         - Mysql
              #         - Performance_Schema
              #     tableFilterPattern:
              #       includes:
              #         - Accounts
              #         - global_status
              #         - EVENT
              #         - user
    ```
    
    
    > 🗣️ FilterPatterns support Regex in include and exclude expressions.
    
<br>
    
2. After the successful workflow run, you can check the metadata of scanned Tables on Metis UI for all schemas in the database.
    
     
    
    > Note: Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
    > 
    
    > 🗣 The FilterPatterns  work on the regex pattern.Filtering for the Scanner workflow works on a hierarchy level; First, it will filter all given schemas and then the table in that schema if present.