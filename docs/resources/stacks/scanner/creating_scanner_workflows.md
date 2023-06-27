# Creating Scanner Workflows

## Prerequisites

1. Permission to run the Scanner workflow: A user must have either Operator level access (`roles:id:operator` tag) or grant to the “**Run as Scanner User”** use case. 
    
    
    >  To obtain the required use case, please contact the DataOS system administrator.
    
  
    
2. Include the property `runAsUser: metis` under the `spec` section in the Scanner YAML.

## Building Blocks of Scanner Workflow

The below table summarizes various properties within a Scanner workflow YAML.

| Field | Example | Default Value | Requirement | Additional Details |
| --- | --- | --- | --- | --- |
| `stack` | `scanner` |  | Mandatory |  |
| `compute` | `mycompute` |`runnable-default`  | Mandatory |  |
| `runAsUser` | `metis` |  | Mandatory |  |
| `depot` |`dataos://icebase`|  | Mandatory | in case of Depot scan only. |
| `type` | `bigquery` | Source-specific | Mandatory | In case of non-Depot scan |
| `source` | `bigquery_metasource` |  | Mandatory | In case of non-Depot scan |
| `sourceConnection.config.type` | `BigQuery` | Source-specific | Mandatory | In case of non-Depot scan |
| `sourceConnection.config` | `username` `password` `hostport`| Source-specific | Mandatory | In case of non-Depot scan|
| `SourceConfig.type` |  `DatabaseMetadata`  `MessagingMetadata` |  | Mandatory | In case of non-Depot scan |
| `databaseFilterPattern` | `^SNOWFLAKE.*` |  | optional | Applicable only in case of Database/Warehouse data source |
| `schemaFilterPattern` | `^public$` |  | optional | Applicable only in case of Database/Warehouse data source |
| `tableFilterPattern` | `.*CUSTOMER.*` |  | optional | Applicable only in case of Database/Warehouse data source |
| `topicFilterPattern` | `foo` `bar` |  | optional | Applicable only in case of Messaging data source |
| `includeViews` | `true` `false` | `false` | optional | Applicable only in case of Database/Warehouse data source |
| `includeTables` | `true` `false` | `false` | optional | Applicable only in case of Database/Warehouse data source |
| `markDeletedTables` | `true` `false` | `false` | optional | Applicable only in case of Database/Warehouse data source |
| `markDeletedTablesFromFilterOnly`  | `true` `false` | `false` | optional | Applicable only in case of Database/Warehouse data source |
| `enableDebugLog` | `true` `false` | `false` | optional | All |
| `ingestSampleData` | `true` `false` | `false` | optional | Applicable only in case of Messaging data source |
| `markDeletedTopics` | `true` `false` | `false` | optional | Applicable only in case of Messaging data source |

## Creating Scanner YAML Configuration

1. Define resource properties. This properties are common for all resources. To learn more, refer to [this] page.
    
    ```yaml
    name: bqscanner
    version: v1
    type: workflow
    tags:
      - bigquery
      - scanner
    description: Scanner workflow to scan metadata from BigQuery
    owner: 
    workflow: 
    ```
    
2. Scanner workflows are either single-time run or scheduled to run at a specific cadence. To schedule a workflow, you must add the `schedule` property, under which you define a `cron` To learn about these properties, refer to [this] page.
    
    ```yaml
    workflow:
      title:
      schedule: 
        cron: '*/10 * * * *'
        concurrencyPolicy: Forbid
        startOn: 2023-01-01T23:30:30Z
        endOn: 2023-01-01T23:40:45Z
        completeOn: 2023-01-01T23:30:45Z
      dag:
    ```
    
3. Define the Scanner job properties in the `dag`, such as job name, description. 
    
    ```yaml
    workflow:
      dag:
        - name: <job name>        
          description: <job description>    
          spec:
            
    ```
    
4. Define the specification for stack and compute  for the Scanner workflow 
    
    `stack`: Name and version of the stack. 
    
    `compute`: Name of the compute resource for running workflows. Default value is `runnable-default`.
    
    `runAsUser`: User ID of the use case assignee. The default value here is `scanner`. but 'Run as a Scanner user' use case should be granted to run Scanner workflow.
    
    ```yaml
    			spec:
            stack: scanner:2.0           
            compute: runnable-default   
            runAsUser: metis
            scanner: 
    ```
    
5. Under the ‘**Scanner**’ section, provide the data source connection details specific to the underlying source to be scanned.
    
    **For Depot Scan:** Depot provides a reference to the source from which metadata is read/ingested. 
    
    `depot`: Give the name or address of the depot. The Scanner job will scan all the datasets referred by a depot. Depot keeps connection details and secrets, so you do not need to give them explicitly in Scanner YAML.
    
    ```yaml
    	  scanner:
    	    depot: dataos://icebase    #        
    ```
    
    
    > Scanner workflow will automatically create a source (with the same name as the depot name) where the scanned metadata is saved within Metastore.
    
    
    
    **For Non-Depot Scan: First, specify the** 
    
    `type`: This depends on the underlying data source. Values for type could be snowflake, bigquery, redshift, etc.
    
    `source`: Here you need to explicitly provide the source name where the scanned metadata is saved within Metastore. On Metis UI, sources are listed for databases, messaging, dashboards, workflows, ML models, etc. 
    
    ```yaml
    	scanner:
        type: snowflake
        source: samplexyz 
    ```
    
    
    > On Metis UI, sources are listed for data sources, dashboards, workflows, and ML models. Under the given source name, you can see the information about all the entities scanned for a data source.
    
   
    
    `sourceConnection`: When the metadata source is not referenced by the depot, you need to provide the source connection details and credentials **explicitly**. The properties in this section depend on the underlying metadata source, such as type, username, password, hostPort, project, email, etc. 
    
    ```yaml
    sourceConnection:
      config:
        type: Snowflake
        username: <username>
        password: <password>
        warehouse: WAREHOUSE
        account: NB48718.central-india.azure
    ```
    
    
    > Connection details will depend on the underlying data source to be scanned. Click here to learn more about the data source specific configuration properties.
    
    
    
6. Provide a set of configurations specific to the source type under ****`sourceConfig` to customize and control metadata scanning. These properties depend on the underlying metadata source. Specify them under the config section.
    
    `type`: Specify config type; This is for type of metadata to be scanned, for databases/warehouses, the `type` is `DatabaseMetadata`.
    
    `databaseFilterPattern` ****: To determine which databases to include/exclude during metadata ingestion.
    
    - `includes:` Add an array of regular expressions to this property in the YAML. The Scanner workflow will include any databases whose names match one or more of the provided regular expressions. All other databases will be excluded.
    - `excludes`: Add an array of regular expressions to this property in the YAML. The Scanner workflow will exclude any databases whose names match one or more of the provided regular expressions. All other databases will be included.
    
    `schemaFilterPattern` : To determine which schemas to include/exclude during metadata ingestion.
    
    - `includes`: Add an array of regular expressions to this property in the YAML. The Scanner workflow will include any schemas whose names match one or more of the provided regular expressions. All other schemas will be excluded.
    - `includes`: Add an array of regular expressions to this property in the YAML. The Scanner workflow will exclude any schemas whose names match one or more of the provided regular expressions. All other schemas will be included.
    
    `tableFilterPattern`: To determine which tables to include/exclude during metadata ingestion.
    
    - `includes`: Add an array of regular expressions to this property in the YAML. The Scanner workflow will include any tables whose names match one or more of the provided regular expressions. All other tables will be excluded.
    - `includes`: Add an array of regular expressions to this property in the YAML. The Scanner workflow will exclude any tables whose names match one or more of the provided regular expressions. All other tables will be included.
    
    `topicFilterPattern`: To determine which tables to include/exclude during metadata ingestion.
    
    - `includes`: Add an array of regular expressions to the `includes` property in the Scanner YAML. The Scanner workflow will include any tables whose names match one or more of the provided regular expressions. All other tables will be excluded.
    - `includes`: Explicitly exclude tables by adding an array of regular expressions to the `excludes` property in the Scanner YAML. The Scanner workflow will exclude any tables whose names match one or more of the provided regular expressions. All other tables will be included.
        
        
        > Filter patterns support Regex in `includes` and `excludes` expressions. Refer to [Filter Pattern Examples](creating_scanner_workflows/filter_pattern_examples.md)  page for the example scenarios.
        
    
    `markDeletedTables`: Set the Mark Deleted Tables property to true to flag tables as soft-deleted if they are not present anymore in the source system. 
    
    If a dataset is deleted from the source and hasn't been ingested in Metis during a previous scanner run, there will be no visible change in the scanned metadata on the Metis UI. However, if the deleted dataset has already been ingested in MetisDB from previous scanner runs, users can run a scanner workflow for the specific depot they want to scan with the **`markDeletedTables: true`** option in the workflow configuration. After a successful run, users can check the Metis UI to see the tables that have been marked as deleted.
    
    `markDeletedTablesfromFilterOnly`: Set this property to true to flag tables as soft-deleted if they are not present anymore within the filtered schema or database only. This flag is useful when you have more than one ingestion pipelines.
    
    `ingestSampleData`Set this property to true to ingest sample data from the topics.
    
    `markDeletedTopics`**:** Set this property to true to flag topics as soft-deleted if they are not present anymore in the source system.
    
    `enableDebugLog`Set the Enable Debug Log toggle to set the default log level to debug; 
    
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
        databaseFilterPattern:
          includes:
            - ^cust.*
        markDeletedTables: false
        includeTables: true
        includeViews: true
    ```
    
    ### **Sample Depot Scan YAML File**
    
    Here is an example of YAML configuration to connect to the source through depot to extract entity metadata. The scanned metadata will be saved in Metis DB.
    
    ```yaml
    name: scanner2-snowflake-depot
    version: v1
    type: workflow
    tags:
      - scanner
      - snowflake
    description: The workflow scans Snowflake data source through depot scan
    workflow:
      dag:
        - name: scanner2-snowflake-job
          description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
    			tags:
              - scanner2
          spec:
            stack: scanner:2.0               
            compute: runnable-default        
            runAsUser: metis                 
            scanner:
              depot: snowflake03             
              sourceConfig:
                config:
                  type: DatabaseMetadata         
                  databaseFilterPattern:
                    includes:
                      - <regex>
                    excludes:
                      - <regex>
                  schemaFilterPattern:
                    includes:
                      - <regex>
                    excludes:
                      - <regex>
                  tableFilterPattern:
                    includes:
    	                - <regex>
                    excludes:
                      - <regex>
                    markDeletedTables: false   # set to true if we want deleted tables information in Metis
                    includeTags: true
                    includeViews: true
    ```
    
    ### **Sample Non-Depot Scan YAML File**
    
    In this example, connection details are given in the YAML configuration to connect to the source to extract entity metadata. The scanned metadata will be saved in Metis DB.
    
    ```yaml
    version: v1
    name: scanner2-snowflake-non-depot
    type: workflow
    tags:
      - scanner
      - snowflake
    description: Non-Depot Scanner workflow to scan entity metadata and save it in Metis
    workflow:
      dag:
        - name: scanner2-snowflake-depot-job
          description: The job scans schema and Snowflake tables and register data to metis
          spec:
            tags:
              - scanner2
            stack: scanner:2.0               
            compute: runnable-default        
    				runAsUser: metis
            scanner:
              type: snowflake                
              source: sampleXyz              
              sourceConnection:                    
                config:
                  type: Snowflake
                  username: <username>
                  password: <password>
                  warehouse: WAREHOUSE
                  account: NB48718.central-india.azure
              sourceConfig:                  
                config:
                  type: DatabaseMetadata         
                  databaseFilterPattern:
                    includes:
                      - <regex>
                    excludes:
                      - <regex>
                  schemaFilterPattern:
                    includes:
                      - <regex>
                    excludes:
                      - <regex>
                  tableFilterPattern:
                    includes:
    	                - <regex>
                    excludes: 
                      - <regex>
                    markDeletedTables: false   # set to true if we want deleted tables information in Metis
                    includeTags: true
                    includeViews: true
    ```
    
    
    > To scan metadata from various data sources, you need certain permissions and access privileges as a data source user. These requirements are specific to each data source. Refer to [this]() section to learn more about them.
    
    
    
    After the successful workflow run, you can check the metadata of scanned Tables on Metis UI for all schemas present in the database.