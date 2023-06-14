# Workflow Creation Guide

Welcome to the Workflow Creation Guide. This section provides a step-by-step procedure on how to build a Workflow resource within the DataOS environment. The steps range from understanding the structure of a Workflow YAML file to configuring various sections, and ultimately applying it to create a resource within DataOS. Let's delve into the process of building a Workflow.

## Structure of a Workflow YAML File

### Configuring the Resource Section

A Workflow is a type of resource in DataOS. The first step in building a Workflow involves setting up the Resource Section. Below is the YAML configuration for the Resource Section:
```yaml
name: my-workflow # Resource (or Workflow) Name
version: v1 # Resource Manifest-Version
type: workflow # Resource Type
tags: # Resource Tags 
  - dataos:type:resource
  - dataos:type:workspace-resource
  - dataos:resource:workflow
description: This is a sample workflow YAML configuration # Resource Description
owner: iamgroot # Resource (or Workflow) Owner
```
For further customization options of the fields within the Resource Section, refer to the RESOURCE SECTION LINK.

### Configuring the Workflow Section

The Workflow Section holds configurations exclusive to the Workflow resource. In DataOS, you can implement two types of workflows: single-run and scheduled workflows, which differ in their YAML syntax.

#### Scheduled Workflow

A Scheduled Workflow triggers a series of jobs or tasks at particular intervals or predetermined times. To construct a scheduled workflow, specify the scheduling configurations in the schedule section, as illustrated below:
```yaml
workflow: # Workflow Section
    schedule: # Schedule Section
        cron: '/10 * * * *' # Cron Expression
    dag: # Directed Acyclic Graph
        {collection-of-jobs}
```

#### Single-Run Workflow

A Single-run workflow only executes once. A Workflow without a schedule section is a single-run workflow. Below is the YAML syntax for the same:
```yaml
workflow: # Workflow Section
    dag: # Directed Acyclic Graph
        {collection-of-jobs}
```
Depending on the requirements, choose between a scheduled or single-run workflow.

For more configuration options in the schedule section, refer to the [Workflow YAML Field Reference](./workflow-yaml-field-reference.md).

### Configuring the DAG Section

A DAG, or Directed Acyclic Graph, depicts the sequence and dependencies between various jobs. A DAG must contain at least one job.

#### Job 

A Job is a single processing task. A DAG may include multiple jobs linked in series or parallel to achieve a specific result. The YAML syntax for a job is as follows:
```yaml
  dag: # (Directed Acyclic Graph)
    - name: ${job1-name} # (Name of the Job1)
      spec: # (Specs of the Job1)
        stack: ${stack1:version} # (Stack Name and Version)
        compute: ${compute-name} # (Compute Name)
        stack1: # (Stack1 Specific Configurations)
          {stack1-specific-configuration}
    - name: ${job2-name} # (Name of Job2)
      spec: # (Specs of Job2)
        stack: ${stack2:version} # (Stack Name and Version)
        compute: ${compute-name} # (Compute Name)
        stack2: # (Stack2 Specific Configuration)
          {stack2-specific-configuration}
      dependencies: # (Job Dependency)
       - ${job1-name}
```
Actual configurations for a job vary across stacks. General configuration fields for a job are provided above.

## Applying the Workflow Resource YAML
After constructing a Workflow YAML, it's time to apply it and create a Workflow resource in the DataOS environment. This is achieved using the `apply` command:
```shell
dataos-ctl apply -f <yaml-file-path> -w <workspace>
```

Congratulations! You've successfully created a Workflow Resource. Now, you can explore various case-scenario for a Workflow resource.

<u>[Implementing Single Run Workflow](./Workflow/single-run-workflow.md)</u>

<u>[Scheduled or Cron Workflow](./Workflow/scheduled-or-cron-workflow.md)</u>

<u>[Executing Multiple Workflow YAMLs from Single One](./Workflow/executing-multiple-workflow-yamls-from-single-one.md)</u>