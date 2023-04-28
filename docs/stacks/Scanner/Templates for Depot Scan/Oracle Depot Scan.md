# **Oracle Depot Scan**

DataOS allows you to connect to the Oracle database to access data from the tables using Depots. The Depot enables access to all schemas visible to the specified service in the configured database. You can scan metadata from an Oracle-type depot with Scanner workflows.

# **Requirements**

To scan the Oracle depot, you need the following:

1. Ensure that the depot is created for your Oracle database and you have `read` access for the depot.
2. You should have enough access to fetch the required metadata from your Oracle database.
3. Metadata Scan is supported for 12c, 18c, 19c, and 21c versions. 

# **Scanner Workflow**

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML. You can apply database, schema, and table filter patterns while scanning metadata.
    
    
    > 💡 FilterPatterns support regex in include and exclude expressions.
    
    we can run the Scanner workflow with or without a filter pattern. 
    
    ```yaml
    version: v1
    name: oracle-scanner
    type: workflow
    tags:
      - oracle-scanner
    description: The job scans schema tables and register metadata
    workflow:
      dag:
        - name: oracle-scanner
          description: The job scans schema from oracle-scanner tables and register metadata to metis2
          spec:
            tags:
              - scanner
            stack: scanner:2.0
            compute: runnable-default
    				runAsUser: metis
            scanner:
              depot: oracle01          #depo name/address
              # sourceConfig:
              #   config:
              #     schemaFilterPattern:
              #       exclude:
              #         - outln
              #     tableFilterPattern:
              #       includes:
              #         - cdb_xs_audit_trail
    ```
    
2. After the successful workflow run, you can check the metadata of scanned Tables on Metis UI for all schemas present in the database.
    
    
    > **Note:** Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
    > 
    


    > 🗣 Filtering for the Scanner workflow works on a hierarchy level; First, it will filter all given schemas and then the table in that schema if present.