# **Creating Depot Scan Workflow**

In order to create and run a Scanner workflow for metadata ingestion, we will follow the steps to create a YAML configuration that will connect to the source through depot and scan the entities.

# **Prerequisites**

Before running depot-scan workflow, you should make sure that you have the following: 

1. Depot created for the underlying source
2. Permission to access the depot
3. Permission to run the (Scanner) workflow (such as `roles:direct:metis` tag)
    
    
    > 🗣 You can contact the DataOS system administrator to assign you the ‘admin’ role from Metis UI.
    
    
4. Include the property `runAsUser: metis` under the `spec` section in the Scanner YAML.

# **Creating YAML Configuration**

Learn how to configure and run a workflow to scan the data sources for the given depot.

1. Create a workflow YAML file. 
2. In the YAML file, provide the workflow properties, such as version, name, description, tags, etc.
    
    ```yaml
    version: v1                  # Resource Manager API version
    name: scanner2-icebase-k     # Scanner workflow name
    type: workflow
    tags:
      - scanner
      - icebase
    description: The workflow scans a depot and saves the metadata to Metis DB
    
    ```
    
3. Define the Scanner job configuration properties in the dag.
    
    ```yaml
      workflow:
      dag:
        - name: scanner2-icebase-job         # name of the job
          description: The job scans schema from icebase tables and registers as datasets to metis2
          spec:
            tags:
              - scanner2
            stack: scanner:2.0               # name and version of the stack used
            compute: runnable-default        # default compute for running workflows
            runAsUser: metis                 # Metis user can run the Scanner
    ```
    
4. Under the ‘**Scanner**’ stack, provide the **following:**

   - **depot**: Give the name or address of the depot. Depot provides a reference to the source from which metadata is read/ingested. The Scanner job will scan all the datasets referred by a depot. Depot keeps connection details and secrets, so you do not need to give them explicitly in Scanner YAML.
        
      > Scanner workflow will automatically create a source (with the same name as the depot name or source name given in the Depot YAML) where the scanned metadata is saved within Metastore. On Metis UI, sources are listed for data sources, dashboards, workflows, and ML models. Clicking on them will show the metadata for the respective source names.
          > 
      
      
      > 🗣 On Metis UI, under the source name (same as the depot name), you can see the information about all the datasets scanned for a depot.
    
    
      ```yaml
              stack: scanner:2.0
              compute: runnable-default
              runAsUser: metis
              scanner:
                depot: dataos://icebase          # depot name or address        
      ```
    
  1. **sourceConfig**: Provide a set of configurations specific to the source **type** under `source configuration` to customize and control metadata scanning. These properties depend on the underlying metadata source. Specify them under the `config` section.
        - **FilterPattern**: Specify `schemaFilterPattern` and `tableFilterPattern` to filter schemas/tables which are of interest.
            
            `includes:` and `excludes:` are used to filter target schemas/tables. For example, you can specify a table name or a regex rule to include/exclude tables while scanning the schema and registering with Metis.
            
            The schema and table filters work in cases where the metadata source is RDBMS/Warehouse, like Oracle, Snowflake, etc. 
            
            ```yaml
            stack: scanner:2.0
            compute: runnable-default
            runAsUser: metis
            scanner:
               depot: dataos://icebase
               sourceConfig:
                 config:
                   schemaFilterPattern:
                     includes:
                       - <schemaname>
            					 - <regex>
                      - some_prefix_*
                     excludes:
                      - <schemaname>    
                   tableFilterPattern: 
                     includes:
                      - <tablename>
            		      - <regex>
                      - some_prefix_*
                     excludes:
                      - <tablename>
                      - <regex>
                   markDeletedTables: false
                   includeTables: true
                   includeViews: true    
            ```
            
5. Save the YAML file and copy its path. The path could be either relative or absolute.

# **Running Workflow**

Use the `apply` command to run the above workflow.

```bash
dataos-ctl apply -f <path/filename> -w <name of the workspace>
```

# **Deleting Workflow**

After your job is successfully run, it is a good practice to delete the workflow from the environment. The workflow, otherwise, will keep floating in the environment for three days.

```bash
dataos-ctl delete -t workflow -w <name of the workspace> -n <name of the workflow>

```

# **Metadata on Metis UI**

On a successful run, you can view the captured information about these datasets on Metis UI Home page under the `Sources` section.


> 🗣 When you have unwanted metadata scanned for the entities, getting rid of them is possible on Metis UI. You can delete the metadata of scanned schema, table, etc. Please note that you should have sufficient permissions.