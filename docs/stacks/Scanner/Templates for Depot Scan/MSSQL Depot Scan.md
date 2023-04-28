# **MSSQL Depot Scan**

DataOS allows you to connect to the MSSQL database to access data from the tables using Depots. The  Depot enables access to all schemas visible to the specified service in the configured database. You can scan metadata from an MSSQL-type depot with Scanner workflows.

# **Requirements**

To scan the MSSQL depot, you need the following:

1. Ensure that the depot is created and you have `read` access for the depot.
2. You should have enough permissions to scan metadata.

# **Scanner Workflow**

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML. You can apply database, schema, and table filter patterns while scanning metadata. 
    
    ```yaml
    version: v1
    name: mssql-scanner2
    type: workflow
    tags:
      - mssql-scanner2.0
    description: The job scans schema tables and register metadata
    workflow:
      dag:
        - name: scanner2-mssql
          description: The job scans schema from Mssql depot tables and register metadata to metis2
          spec:
            stack: scanner:2.0
            compute: runnable-default
            runAsUser: metis
            scanner:
              depot: mssql01
              # sourceConfig:
              #   config:
              #     schemaFilterPattern:
              #       includes:
              #         - dbo
              #     tableFilterPattern:
              #       includes:
              #         - spt_
    ```
    
    
    > 🗣️ FilterPatterns support Regex for include and exclude expressions.
    
    
    
2. After the successful workflow run, you can check the metadata of scanned Tables on Metis UI for all schemas in the database.
    
    
    > **Note:** Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
    