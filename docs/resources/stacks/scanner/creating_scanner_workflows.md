# Creating Scanner Workflows

## Prerequisites

1. Permission to run the Scanner workflow: A user must have either Operator level access (`roles:id:operator` tag) or grant to the “**Run as Scanner User”** use case.
  <aside class="callout">🗣 To obtain the required use case, please contact the DataOS system administrator.</aside>
     
2. Include the property `runAsUser: metis` under the `spec` section in the Scanner YAML.



## Creating Scanner YAML Configuration

1. Define resource properties such as name, version, type, owner etc. These properties are common for all resources. To learn more, refer to [Configuring the Resource Section](/resources/workflow/#configure-the-resource-section) page.
    
2. Scanner workflows are either single-time run or scheduled to run at a specific cadence. To schedule a workflow, you must add the `schedule` property, under which you define a `cron` To learn about these properties, refer to [Schedulable workflows](/resources/workflow/#scheduled-workflow).

    
3. Define the Scanner job properties in the `dag`, such as job name, description. 
    
4. Define the specification for stack and compute for the Scanner workflow. Also specify user ID of the use case assignee. The default value here is `metis`. but 'Run as a Scanner user' use case should be granted to run Scanner workflow. 

    
5. Under the ‘**Scanner**’ section, provide the data source connection details specific to the underlying source to be scanned.
    
    **For Depot Scan:** Depot provides a reference to the source from which metadata is read/ingested. 
    
    **`depot`**: Give the name or address of the depot. The Scanner job will scan all the datasets referred by a depot. Depot keeps connection details and secrets, so you do not need to give them explicitly in Scanner YAML.
    
    ```yaml
    stackSpec:
      depot: dataos://icebase       
    ```

    <aside class="callout">🗣 Scanner workflow will automatically create a source (with the same name as the depot name) where the scanned metadata is saved within Metastore.</aside>    
    
    
    **For Non-Depot Scan:** First, specify the following:
    
    **`type`**: This depends on the underlying data source. Values for type could be snowflake, bigquery, redshift, etc.
    
    **`source`**: Here you need to explicitly provide the source name where the scanned metadata is saved within Metastore. On Metis UI, sources are listed for databases, messaging, dashboards, workflows, ML models, etc. 
    
    ```yaml
    stackSpec:
      type: snowflake
      source: samplexyz 
    ```
    
    
     <aside class="callout"> 🗣 On Metis UI, sources are listed for data sources, dashboards, workflows, and ML models. Under the given source name, you can see the information about all the entities scanned for a data source.</aside>
   
    
    **`sourceConnection`**: When the metadata source is not referenced by the depot, you need to provide the source connection details and credentials **explicitly**. The properties in this section depend on the underlying metadata source, such as type, username, password, hostPort, project, email, etc. 
    
    ```yaml
    sourceConnection:
      config:
        type: Snowflake
        username: <username>
        password: <password>
        warehouse: WAREHOUSE
        account: NB48718.central-india.azure
    ```
    
    
    <aside class="callout"> 🗣 Connection details will depend on the underlying data source to be scanned. Click here to learn more about the data source specific configuration properties.</aside>
    
    
    
6. Provide a set of configurations specific to the source type under **`sourceConfig`** to customize and control metadata scanning. These properties depend on the underlying metadata source. Specify them under the `config` section.
    
    **`type`**: Specify config type; This is for type of metadata to be scanned, for databases/warehouses, the `type` is `DatabaseMetadata`.
    
    **`databaseFilterPattern`** : To determine which databases to include/exclude during metadata ingestion.
    
    **`schemaFilterPattern`** : To determine which schemas to include/exclude during metadata ingestion.
    
    **`tableFilterPattern`**: To determine which tables to include/exclude during metadata ingestion.
    
    **`topicFilterPattern`**: To determine which topics to include/exclude during metadata ingestion in case of messaging services.
    
    
        
    <aside class="callout"> 🗣 Filter patterns support Regex in `includes` and `excludes` expressions. </aside>
      
     Refer to [Filter Pattern Examples](creating_scanner_workflows/filter_pattern_examples.md)  for the example scenarios.
        
    
    **`markDeletedTables`**: Set this property to true to flag tables as soft-deleted if they are not present anymore in the source system. 
    
    **`ingestSampleData`**: Set this property to true to ingest sample data from the topics.
    
    **`markDeletedTopics`**: Set this property to true to flag topics as soft-deleted if they are not present anymore in the source system.
    
    **`enableDebugLog`**: Set the Enable Debug Log toggle to set the default log level to debug; 
    
        
    ### **Sample Depot Scan YAML File**
    
    <details><summary>Here is an example of YAML configuration to connect to the source through depot to extract entity metadata. The scanned metadata will be saved in Metis DB.</summary>
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
              stackSpec:
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
                      markDeletedTables: false   
                      includeTags: true
                      includeViews: true
      ```
    </details>
    
    ### **Sample Non-Depot Scan YAML File**
    
    <details><summary>In this example, connection details are given in the YAML configuration to connect to the source to extract entity metadata. The scanned metadata will be saved in Metis DB.</summary>
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
              stackSpec:
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
                      includeViews: true
      ```
    </details>
    
    <aside class="callout">🗣 To scan metadata from various data sources, you need certain permissions and access privileges as a data source user. These requirements are specific to each data source. Refer to [this]() section to learn more about them. </aside>
        
    After the successful workflow run, you can check the metadata of scanned entities on Metis UI for all schemas present in the database.

## Filter Pattern Examples
The scanner stack offers a range of filter patterns, including the Database Filter Pattern, Schema Filter Pattern, and Table Filter Pattern for data sources such as databases and data warehouses. Likewise, in the context of messaging pipelines, you can employ the topic filter pattern. Users can exercise control over metadata scanning by utilizing these filters. 

To know more about how to specify filters in different scenarios, refer to [Filter Pattern Examples](creating_scanner_workflows/filter_pattern_examples.md).    