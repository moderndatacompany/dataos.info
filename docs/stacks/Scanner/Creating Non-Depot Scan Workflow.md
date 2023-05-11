# Creating Non-Depot Scan Workflow

In order to create and run a Scanner workflow for metadata ingestion, we will follow the steps to create a YAML configuration that will connect to the source and scan the entities. With this type of Scanner workflow, you must only provide the connection/credential details for the underlying data source within the YAML file.

## Prerequisites

Before running non-depot Scanner workflow, you should make sure that you have the following: 

1. Connection details (specific to underlying data source) such as project ID, email ID, account names, host port details, etc.
2. Credentials needed to access the data source.
3. Permission to run the Scanner workflow such as `users:id:metis` (Metis admin) tag.
4. Include the property `runAsUser: metis` under the `spec` section in the Scanner YAML.

## Creating Scanner Workflow for Non-Depot Scan

Learn how to configure and run a workflow to scan the data sources such as databases, dashboards, messaging services, etc.

1. Create a workflow YAML file. 
2. Provide the workflow properties, such as version, name, description, tags, etc.
    
    ```yaml
    version: v1
    name: scanner2-snowflake-depot-k          # Scanner workflow name
    type: workflow
    tags:
      - scanner
      - snowflake-depot
    description: The job scans schema tables and register data
    ```
    
3. Define the Scanner job configuration properties in the dag, such as job name, its description, stack used etc.
    
    ```yaml
      workflow:
      dag:
        - name: scanner2-snowflake-depot-job         # name of the job
          description: The job scans schema from snowflake tables and registers as datasets to metis2
          spec:
            tags:
              - scanner2
            stack: scanner:2.0              # name and version of the stack used
            compute: runnable-default       # default compute for running workflows
            runAsUser: metis
    ```
    
4. Under the ‘Scanner’ stack, provide the following: 
    -  type. This depends on the underlying data source. 
     - source: Provide the source name where the scanned metadata is saved within Metastore. By default, Scanner workflow pushes metadata to the Metis DB via the Metis API server. On Metis UI, sources are listed for dashboards, data sources, workflows, ML models, etc. Clicking on them will show the metadata for the respective source names.
        
        
        > 🗣 On Metis UI, under the given source name, you can see the information about all the entities scanned for a data source.
        
        
        
        ```yaml
                stack: scanner:2.0
                compute: runnable-default
                runAsUser: metis
                scanner:
                  type: snowflake
                  source: samplexyz        # sourcename where metadata will be saved
                  
        ```
        
5. When the metadata source is not referenced by the depot, you need to provide the `source connection` details and credentials explicitly. The properties in this section depend on the underlying metadata source, such as username, password, hostPort, project, email, etc. 
    
    > Enter the details for any additional connection arguments that can be sent to the metadata source while making the connection. These details must be added as Key-Value pairs.
    
    
    Here is an example of sourceConnection details for metadata source-Snowflake.
    
    ```yaml
    sourceConnection:
      config:
        type: Snowflake
        username: username
        password: password
        warehouse: WAREHOUSE
        account: NB48718.central-india.azure
    ```
    
    > 🗣 Connection details will depend on the underlying data source to be scanned. Click [here](./Creating%20Non-Depot%20Scan%20Workflow.md) to learn more about the specific configuration properties.
    
    <br>
    
6. Provide a set of configurations specific to the source type under `source configuration` to customize and control metadata scanning. These properties depend on the underlying metadata source. Specify them under the config section.
    - type: Specify config type; for example, in this case, the `type` is `DatabaseMetadata`.
    - FilterPattern: Specify which databases/ schemas/ tables/ charts/ dashboards/ topics are of interest.
        
        `include:` and `exclude:` are used to filter target entities. For example, you can specify a  table name or a regex rule to include/exclude tables while scanning the schema and registering with Metis.
        
        ```yaml
        sourceConfig:
          config:
            type: DatabaseMetadata
            databaseFilterPattern:
              includes:
                - TMDCSNOWFLAKEDB
            schemaFilterPattern:
              excludes:
                - mysql.*
                - information_schema.*
                - performance_schema.*
                - sys.*
            markDeletedTables: false
        ```
        
        
        > 🗣 Config type and filter patterns will vary according to the source to be scanned.  Click [here](./Creating%20Non-Depot%20Scan%20Workflow.md) to learn more about the specific configuration properties.

<br>

7. Save the YAML file and copy its path. The path could be either relative or absolute.

## Running Workflow

Use the `apply` command to run the above workflow.

```yaml
dataos-ctl apply -f <path/filename> -w <name of the workspace>
```

## Metadata on Metis UI

On a successful run, you can view the captured metadata for the given data source on Metis UI by referring to the `Sources`.

> 🗣 When you have unwanted metadata scanned for the entities, getting rid of them is possible on Metis UI. You can delete the metadata of scanned schema, table, etc. Please note that you should have sufficient permissions.