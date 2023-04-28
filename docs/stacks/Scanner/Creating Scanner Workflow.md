# **Creating Scanner Workflow**

This tutorial walks you through the steps you need to take to create and run a workflow to scan metadata.

# **Prerequisites**

1. Check required permissions to create a workflow
    
    If you are aware of the concept of a workflow, continue reading the next section.
    
    To learn more about a workflow in the DataOS context, click [her](../../Transformation/Workflow.md)e. 
    
2. Permission to run the (Scanner) workflow (such as `roles:direct:metis` tag).
    
    
    > 🗣 You can contact the DataOS system administrator to assign you the ‘admin’ role from Metis UI.
    
3. Include the property `runAsUser: metis` under the `spec` section in the Scanner YAML.
4. DataOS CLI (Command Line Interface) to run the workflow
    
    If CLI is already installed on your system, move to the next step. In case it's not installed, refer to the [CLI installation steps](../../Getting%20Started%20-%20DataOS%20Documentation/Data%20Management%20Capabilities/CLI.md). 
    

# **Creating YAML Configuration**

This example shows the steps to configure and run a workflow to scan the data sources for the given depot-Icebase.

1. Create a workflow YAML file. 
2. In the YAML file, provide the workflow properties, such as version, name, description, tags, etc.
    
    ```yaml
    version: v1                  # Resource Manager API version
    name: <workflow name>        # Scanner workflow name
    type: workflow 
    owner: <owner name>          # Optional property
    tags:
      - tag1
      - tag2
    description: <workflow description for what type of metadata is being extracted>
    ```
    
3. Define the Scanner job properties in the dag, such as job name, description, stack used, etc.
    
    ```yaml
      workflow:
        dag:
          - name: <job name>        # name of the job 
            description: <job description>    
            spec:
              tags:
                - tag
              stack: scanner:2.0           # name and version of the stack used
              compute: runnable-default    # default compute for running workflows
              runAsUser: metis
              scanner: 
    ```
    
4. Under the ‘**Scanner**’ stack (in the above YAML code script), provide the **configuration settings** specific to the underlying source to be scanned, such as config types, connection types, sourceConfig, etc. ****
    
    
    > 🗣 These properties vary for the underlying metadata source to be scanned, and you have to choose only the properties which are applicable to the metadata source. To learn more about these properties, refer to [Supported Scanner Workflows](../Scanner.md).

<br>

5. Save the YAML file and copy its path. The path could be either relative or absolute.

# **Running Workflow**

Use the `apply` command to run the above workflow.

```yaml
dataos-ctl apply -f <path/filename> -w <name of the workspace>
```

# **Deleting Workflow**

After your job is successfully run, it is a good practice to delete the workflow from the environment to clear up resources faster. The workflow, otherwise, will keep floating in the environment for three days before it gets auto-cleaned.

```yaml
dataos-ctl delete -t workflow -w <name of the workspace> -n <name of the workflow>

```