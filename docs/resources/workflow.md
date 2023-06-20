# Workflow

Workflow, within the DataOS, is a collection of jobs with directional dependencies. It defines a hierarchy based on a dependency mechanism.

You can visualize workflow as a representation of a DAG, while a DAG can be thought of as a collection of jobs and their dependencies and sets the context for when and how those jobs should be executed. You can have multiple jobs or even a single job within each DAG (there should be at least one). 

A job within a workflow defines a sequence of processing tasks in which each job runs in its own Kubernetes pod. This is done so that the computation of one job doesn't create a bottleneck for the others.

Each job within a DAG gets executed upon a particular Stack, an extension point within a job that adds new programming paradigms for the user, depending on what they need to do. For instance, if you want to perform data transformation, ingestion, or syndication, go with the Flare stack. DataOS, out-of-the-box, provides you with different stacks, such as Flare, Scanner, Alpha, and many more.

![Diagrammatic representation of a workflow](./workflow/workflow.svg)

<center><i>Diagrammatic representation of a workflow</i></center>

In the above workflow, `Job 1` runs first, as it has no dependencies. Once `Job 1` has finished, `Job 2` and `Job 3` run in parallel. Finally, once `Job 2` and `Job 3` have been completed, `Job 4` can run as it depends on both `Job 2` and `Job 3`. Finally, once `Job 4` has been completed `Job 5` can run.

The Directed Acyclic Graph may have multiple roots. It implies that the DAG within a workflow can not only have jobs but also workflows themselves stored in different places. This can allow for complex workflows to be split into manageable pieces. To know more about this scenario, click [here.](./workflow/executing_multiple_workflow_yamls_from_single_one.md)

## Types of Workflows

Workflows are either single-time run or schedulable. To schedule a workflow, you must add the `schedule` property, under which you define a `cron` and prepare it as a scheduled workflow or a cron workflow. The details related to the cron workflow properties are available in the below table. If you want to check out a case scenario for a cron or scheduled workflow, click [here.](./workflow/scheduled_or_cron_workflow.md)

## Syntax of a workflow

The code block below gives the YAML syntax for a single-time run workflow. You can learn what these key-value properties mean and how these are declared in the table below.

```yaml
workflow: #(Workflow Section)
  schedule: #(Schedule Section)
    cron: ${'*/10 * * * *'} #(Cron Expression)
    concurrencyPolicy: ${Allow} #(Concurrency Policy)
    startOn: ${2022-01-01T23:30:30Z} #(Start Time of Cron)
    endOn: ${2022-01-01T23:40:45Z} #(End Time of Cron)
    completeOn: ${2022-01-01T23:30:45Z} #(Completion Time of Cron)
  dag: #(Directed Acyclic Graph)
    - name: ${job1-name} #(Name of the Job1)
      spec: #(Specs of the Job1)
        stack: ${stack1:version} #(Stack Name and Version)
        compute: ${compute-name} #(Compute Name)
        stack1: #(Stack1 Specific Configurations)
          {stack1-specific-configuration}
    - name: ${job2-name} #(Name of Job2)
      spec: #(Specs of Job2)
        stack: ${stack2:version} #(Stack Name and Version)
        compute: ${compute-name} #(Compute Name)
        stack2: #(Stack2 Specific Configuration)
          {stack2-specific-configuration}
      dependencies: #(Job Dependency)
       - ${job1-name}
```
<center> <i>YAML Syntax of a Workflow Resource</i></center>

## Creating a Workflow
As you've familiarized yourself with the fundamentals of workflow syntax, it's time to delve deeper into coding, and craft your initial workflow. This section will guide you through each step of this exciting process. To begin your journey, please refer to the following guide by clicking on the link provided [here.](./workflow/creating_a_workflow.md)

## Workflow YAML Field Reference

The below table summarizes various properties within a Workflow YAML

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| `workflow` | object | None | None | Mandatory |
| `schedule` | object | None | None | Optional**  |
| `cron` | string | None | Any valid cron expression. | Optional**  |
| `concurrencyPolicy` | string | Allow | Allow/Forbid/Replace | Optional |
| `startOn` | string | None | Any time provided in ISO <br> 8601 format. | Optional |
| `endOn` | string | None | Any time provided in ISO <br> 8601 format. | Optional |
| `completeOn` | string | None | Any time provided in ISO <br> 8601 format. | Optional |
| `title` | string | None | Any valid string | Optional |
| `name` | string | None | Any string confirming <br>the regex [a-z0-9]\([-a-z0-9]*<br>[a-z0-9]) and length less <br> than or equal to 48 | Mandatory |
| `title` | string | None | Any string | Optional |
| `description` | string | None | Any string | Optional |
| `spec` | object | None | None | Mandatory |
| `runAsUser` | string | None | UserID of the Use Case <br>Assignee | Optional |
| `compute` | string | None | runnable-default or any <br> other custom compute <br> created by the user | Mandatory |
| `stack` | string | None | flare/toolbox/scanner/<br>alpha | Mandatory |
| `retry` | object | None | None | Optional |
| `count` | integer | None | Any positive integer | Optional |
| `strategy` | string | None | Always/OnFailure/<br>OnError/OnTransientError | Optional |
| `dependency` | string | None | Any job name within the workflow | Optional |

<i>Optional**:</i> Fields optional for single-run workflows, but Mandatory for Scheduled workflows.

To know more about the various fields, click [here.](./workflow/workflow_yaml_field_reference.md)


<aside style="background-color:#FFE5CC; padding:15px; border-radius:5px;">
📖 Best Practice: It is part of the best practice to add relevant `description` and `tags` for your workflow. While `description` helps to determine what the workflow will help you accomplish, `tags` can help in faster searching in Metis and Operations.
</aside>



## Case Scenarios

- [Implementing Single Run Workflow](./workflow/single_run_workflow.md)

- [Scheduled or Cron Workflow](./workflow/scheduled_or_cron_workflow.md)

- [Executing Multiple Workflow YAMLs from a Single One](./workflow/executing_multiple_workflow_yamls_from_single_one.md)




