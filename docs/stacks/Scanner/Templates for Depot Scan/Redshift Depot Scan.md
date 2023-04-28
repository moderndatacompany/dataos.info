# **Redshift Depot Scan**

DataOS allows you to connect to the Redshift database to access data from the tables using Depots. The Depot enables access to all schemas visible to the specified service in the configured database. You can scan metadata from a Redshift-type depot with Scanner workflows.

# **Requirements**

To scan the Redshift depot, you need the following:

1. Ensure that the depot is created for your Redshift database and you have `read` access for the depot.
2. `SVV_TABLE_INFO` View contains summary information for tables in the Redshift database and is visible only to superusers. You need permissions to query the view while scanning metadata from Scanner workflow.
3. Redshift user must grant `SELECT`privilege on table [SVV_TABLE_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLE_INFO.html) to fetch the metadata of tables and views.

# **Scanner Workflow**

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML. You can apply database, schema, and table filter patterns while scanning metadata
    
    we can run the Scanner workflow with or without a filter pattern. 
    
    ```yaml
    version: v1
    name: redshift-scanner2
    type: workflow
    tags:
      - redshift-scanner2.0
    description: The job scans schema tables and register metadata
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
                  # schemaFilterPattern:
                  #   includes:
                  #     - Public
                  # tableFilterPattern:
                  #   includes:
                  #     - Customer
    ```
    
    
    > 🗣️ FilterPatterns support Regex in include and exclude expressions.
    
    
    
2. After the successful workflow run, you can check the metadata of scanned Tables on Metis U for all schemas present in the database.
    
    > **Note:** Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
    > 
    
    
    > 🗣 Filtering for the Scanner workflow works on a hierarchy level; First, it will filter all given schemas and then the table in that schema if present.
    
    