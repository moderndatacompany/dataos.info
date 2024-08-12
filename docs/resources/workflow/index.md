---
title: Workflow
search:
  boost: 8
---

# :resources-workflow: Workflow

The Workflow in DataOS serves as a [Resource](/resources/) for orchestrating data processing tasks with dependencies. It enables the creation of complex data workflows by defining a hierarchy based on a dependency mechanism. To know more about workflow, refer to the following link: [Core Concepts](/resources/workflow/core_concepts/).

!!!tip "Workflow in the Data Product Lifecycle"

    Workflows are integral to the **transformation phase** in the [Data Product Lifecycle](/products/data_product/). They are particularly useful when your transformation involves:

    - **Definite Execution**:sequences of tasks, jobs, or processes batch data, terminating upon successful completion or failure. For example, A workflow moving data from point A to point B.

    - **Execution Processes**: To process data in discrete chunks, in parallel or in a given ordered sequence of jobs in DAGs.

    - **Independent Processing**:  Performs data-transformation, ingestion, or syndication or automating job execution based on a cron expression.

## Structure of Workflow manifest


=== "Code"
    ```yaml title="worker_manifest_structure.yml"
    --8<-- "examples/resources/workflow/workflow.yml"
    ```


## First Steps

Workflow Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/workflow/first_steps/).

## Configuration

Workflows can be configured to autoscale and match varying workload demands, reference pre-defined Secrets and Volumes, and more. DataOS supports two types of Workflows: single-run and scheduled Workflow, each with its own YAML syntax. The specific configurations may vary depending on the use case. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Workflow manifest](/resources/workflow/configuration/).

## Recipes

Workflows orchestrate Stacks to accomplish myriad tasks. Below are some recipes to help you configure and utilize Workflows effectively:


- [How to implement Single-run Workflow?](/resources/workflow/how_to_guide/single_run_workflow/)

- [How to run a Cron Workflow or a Scheduled Workflow?](/resources/workflow/how_to_guide/scheduled_workflow/)

- [How to orchestrate multiple Workflows from a single Workflow?](/resources/workflow/how_to_guide/multiple_workflows_from_a_single_workflow/)

- [How to retry a job in the Workflow?](/resources/workflow/how_to_guide/retry_jobs/)

- [How to apply a workflow and get a runtime status of it using CLI Stack?](/resources/workflow/how_to_guide/apply_a_workflow_and_get_runtime_status_using_cli_stack/)
