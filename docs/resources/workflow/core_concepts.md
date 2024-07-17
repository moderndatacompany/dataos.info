## Workflow and Directed Acyclic Graph (DAG)

In DataOS, a Workflow represents a **Directed Acyclic Graph (DAG)**, where jobs are represented as nodes, and dependencies between jobs are represented as directed edges. The DAG structure provides a visual representation of the sequence and interdependencies of jobs within a Workflow. This facilitates efficient job execution by enabling parallel and sequential processing based on job dependencies.

Within a Workflow, a **job** encompasses a series of processing tasks, each executed within its dedicated Kubernetes Pod. This architectural design ensures that the computational workload of one job does not hinder the performance of others, effectively avoiding bottlenecks.

Furthermore, every job within a Directed Acyclic Graph (DAG) is associated with a specific [Stack](/resources/stacks/). A Stack serves as an extension point within a job, offering users the ability to leverage different programming paradigms based on their specific requirements. For instance, if your objective involves data transformation, ingestion, or syndication, utilizing the [Flare](/resources/stacks/flare/) Stack is recommended. DataOS provides a diverse range of pre-built stacks, including [Flare](/resources/stacks/flare/), [Scanner](/resources/stacks/scanner/) and more, enabling developers to seamlessly adopt various programming environments to suit their needs.

<center>

![Illustration of Workflow Resource](/resources/workflow/workflow_overview.png)

</center>

<center><i>Illustration of Workflow Resource</i></center>

In the above illustration, **Job 1** is the first job to be executed as it has no dependencies. Once **Job 1** completes, both **Job 2** and **Job 3** can run concurrently or parallely. Only after the successful completion of both **Job 2** and **Job 3**, **Job 4** becomes eligible for execution. Finally, **Job 5** can be executed sequentially after **Job 4** successfully finishes. This hierarchical structure ensures optimal job execution without creating bottlenecks.

<aside class=callout>
🗣️ A Directed Acyclic Graph may have multiple root nodes, which means that a Workflow can contain both jobs and other nested Workflows stored in different locations. This feature allows for the decomposition of complex workflows into manageable components. For more information on this scenario, refer to <a href="/resources/workflow/orchestrating_multiple_workflows_from_a_single_workflow/">Orchestrating Multiple Workflows from a Single Workflow.</a>
</aside>


## Types of Workflow

A Workflow in DataOS can be categorized as either [single-run](#single-run-workflow) or [scheduled workflow.](#scheduled-workflow)

### **Single-run Workflow**

Single-run Workflow represent a one-time execution of a sequence of jobs. These workflows do not include scheduling attributes and rely solely on the defined DAG structure and job dependencies. To explore a case scenario for a single-run Workflow, refer to the link: [How to implement Single-run Workflow?](/resources/workflow/how_to_guide/single_run_workflow/)

### **Scheduled Workflow** 

Scheduled Workflow enable the automated and recurring execution of jobs based on specified intervals or predetermined times. To schedule a Workflow, the `schedule` section or mapping along with the scheduling [attributes](/resources/workflow/yaml_configuration_attributes/#schedule) must be added to the Workflow YAML configuration. Scheduled Workflow provide a powerful mechanism for automating job execution based on a [cron](/resources/workflow/configuration/#cron) expression. To explore a case scenario for a Scheduled Workflow, refer to the link: [How to run a Cron or a Scheduled Workflow?](/resources/workflow/how_to_guide/scheduled_or_cron_workflow/)