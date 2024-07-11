# Orchestrating Multiple Workflows from a Single Workflow

This section demonstrates how to orchestrate multiple workflows by referencing separate YAML files in a master Workflow YAML file. By following this approach, you can streamline complex data processing tasks into manageable pieces.

## Code Snippet

The code snippet below shows the master Workflow or  super dag (`super_dag.yaml`) that references two separate Workflows (stored in `workflow.yaml` and `profile.yaml`) by specifying the file path within the `file` attribute. 

<details>
<summary>Click here to view the code snippets</summary>

    ```yaml
    --8<-- "examples/resources/workflow/multiple_workflows_from_a_single_workflow.yaml"
    ```

<b>workeflow.yaml</b>

    ```yaml
    --8<-- "examples/resources/workflow/workflow.yml"
    ```

<b>profiling.yaml</b>

    ```yaml
    --8<-- "examples/resources/workflow/workflow.yml"
    ```
</details>


## Implementation Flow

- Save the above code snippets into separate YAML files.

- Once you do that mention the path (relative or absolute) of the `workflow.yaml` and `profiling.yaml` in the file property of the master file `super_dag.yaml`.

- Apply the `super_dag.yaml` command from the CLI.

When you apply the `super_dag.yaml` file, using CLI, it calls in the `workflow.yaml` file first and the `profiling.yaml` file second as the second file is dependent upon the first. The Workflow within the `workflow.yaml` writes the data from `icebase.retail.city` depot to `icebase.retail.city01`. Once that is done the second workflow is executed which does profiling on the same data from `icebase.retail.city01`. This finishes the two processing tasks by applying just one file.


