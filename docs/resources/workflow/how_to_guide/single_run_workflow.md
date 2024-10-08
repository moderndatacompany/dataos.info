# Single-Run Workflow

A [Single-run Workflow](/resources/workflow/core_concepts/#single-run-workflow) represent a single-time execution of a sequence of jobs. It does not include a [`schedule`](/resources/workflow/configurations/#schedule) section.

<center>
  <img src="/resources/workflow/sample_workflow.svg" alt="Illustration of a Single-run Workflow">
  <figcaption>Illustration of a Single-run Workflow</figcaption>
</center>


**Code Snippet**

The following code snippet illustrates a [Workflow](/resources/workflow/) with two jobs. The first one executes upon [Flare](/resources/stacks/flare/) Stack that reads data from the `thirdparty01` [depot](/resources/depot/) in [batch mode](/resources/stacks/flare/case_scenario/#batch-jobs) and subsequently writes to the [`icebase`](/resources/depot/icebase/) [depot](/resources/depot/). Once the first job, completes it execution the second job starts execution, which does the profilling on the data using same flare stack.

???tip "Sample Single Run Workflow manifest"

    ```yaml title="workflow.yml"
    --8<-- "examples/resources/workflow/single_run_workflow.yml"
    ```


Here are it's workflow and profiling manifests to do a hands on:

???tip "Sample Workflows"

    ```yaml title="workflow.yml"
    --8<-- "examples/resources/workflow/workflow.yml"
    ```
    ```yaml title="profiling.yaml"
    --8<-- "examples/resources/workflow/profiling.yml"
    ```

