# AzureSQL Depot Scan

DataOS allows you to connect to AzureSQL database to read data from tables using Depot. The Depot enables access to all schemas visible to the specified user in the configured database. You can scan metadata from an AzureSQL type depot with Scanner workflows.

## Requirements

To scan the JDBC type depot, you need the following:

1. Ensure that the depot is created for your Azure SQL database and you have `Read` access for the depot.
2. You should have enough access to fetch the required metadata from your database.

## Scanner Workflow

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML.
    
     You can apply database, schema, and table filter patterns while scanning metadata.
    
    ```yaml
    version: v1
    name: azuresql-scanner2
    type: workflow
    tags:
      - azuresql-scanner2.0
    description: The job scans schema tables and register metadata
    workflow:
      dag:
        - name: scanner2-azuresql
          description: The job scans schema from azuresql depot tables and register metadata to metis2
          spec:
            stack: scanner:2.0
            compute: runnable-default
            runAsUser: metis
            scanner:
              depot: azuresql
              # sourceConfig:
              #   config:
              #     databaseFilterPattern:
              #       includes:
              #         - <databasename> 
              #     schemaFilterPattern:
              #       excludes:
              #         - <schemaname>
              #     tableFilterPattern:
              #       includes:
              #         - <tablename>
    ```
    
    
    > 🗣️ Filterpatterns support Regex in include and exclude expressions.
    
<br>
    
2. After the successful workflow run, you can check the metadata of scanned Tables on Metis UI for all schemas present in the database.
    
    > Note: Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
    > 
    
    
    > 🗣 Filtering for the Scanner workflow works on a hierarchy level; First, it will filter all given schemas and then the table in that schema if present.
    
   