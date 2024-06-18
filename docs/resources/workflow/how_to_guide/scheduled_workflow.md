# Scheduled or Cron Workflow

The code snippet below illustrates a sample schedule Workflow for profiling using the [Flare](/resources/stacks/flare) Stack in output depots with [Iceberg file format with Hadoop Catalog type and REST Metastore.](/resources/depot#limit-data-sources-file-format). 


???tip "Click here to view the code snippet"

    ```yaml
    --8<-- "examples/resources/workflow/profiling.yml"
    ```

This code snippet will execute the profiling workflow in every 2 minutes on the given date.
