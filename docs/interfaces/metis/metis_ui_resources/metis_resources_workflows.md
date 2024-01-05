# Workflows Metadata On Metis UI

<aside class="callout">
⚠️ This page guides you on exploring and managing metadata for Workflows on Metis. To learn in detail about the Workflow as a Resource, refer to this <a href="/resources/workflow/">link</a>.

</aside>

Metis has integrated "Workflow" as a "Resource”  type entity for storing metadata related to its source and transformations within DataOS. On selecting **Workflows,** the following information will be presented on the screen:

![workflows.png](metis_resources_workflows/workflows.png)
<figcaption align = "center"> List of Workflows  </figcaption>

## Filter pane

The filter pane allows you to refine the Workflow list based on the following attributes:

| Attribute | Description |
| --- | --- |
| Advance Filter | Utilize the syntax editor to filter workflows, applying various criteria with 'and/or' conditions for a more refined search. |
| Show Deleted | Toggle to list deleted workflows. |
| Workspace | Workspace where the Workflow is created, like public or user-specific. |
| Domain | Select a domain like Marketing, or Finance, etc., to filter the Workflow list for associated domains. |
| Owner | Name of the user who created the Workflow. |
| Tag | Filter the list for tags. |
| Tier | Filter the Workflow list based on the tier associated with the importance and criticality, such as Gold, Silver, etc. |

## Result pane

Here, Workflow resources will be listed. Users have the following options to customize how the list is displayed:

| Option | Description |
| --- | --- |
| Sorting | Choose the Sorting order, either by the
- Last updated time or 
- Relevance |
| Sorting order | Define the sorting order as Ascending/Descending |

Each Workflow in the list features a Card view that presents key information for that particular Workflow:

| Attribute | Description |
| --- | --- |
| Name | Workflow name as defined in the resource YAML. |
| Owner | Name of the user who created the Workflow. |
| Tier | Tier associated with the importance and criticality of workflow, such as Gold, Silver, etc. |
| Domain | Associated domain, such as Finance, Marketing etc. |
| Workspace | Workspace where the Workflow is created like public or user-specific. |
| Description | A description added to the Workflow for its purpose. |

## Overview Pane

In the Card view, click anywhere except the resource name provides a quick overview.

![workflow_overview.png](metis_resources_workflows/workflow_overview.png)
<figcaption align = "center"> Quick information  </figcaption>

This includes the following quick reference information:

| Attribute | Description |
| --- | --- |
| Name | Name of Workflow, clicking on it will open its detail view in the new tab. |
| Workspace | Workspace where Workflow is created like public or user-specific. |
| Version | Metadata version. |
| State | Workflow state such as Active or Deleted. |
| Followers Count | Count of users who are following this Workflow. |
| Last updated | Date and time information when the Workflow was last updated. |
| Jobs | Information about the jobs in the Workflow |

## Details Page

In the Result or Overview pane, clicking on the name of the Workflow opens the Resource Details page, which includes:

![wf_details.png](metis_resources_workflows/wf_details.png)
<figcaption align = "center"> Comprehensive details  </figcaption>

### **Workflow Information**

In addition to basic Workflow information, the following details and options are provided.

| Attribute | Description |
| --- | --- |
| Resource Type | Workflow |
| Meta Version | Provides information on the latest Meta version. Click to see the version history and corresponding updates.  |
| Updated | Provides last updated time  |
| Follow | Gives the user an option to follow the Workflow to receive updates and view its follower count. |
| Learn | Provides an option to learn more about this specific resource type |
| Delete | Gives the user the option to delete the Workflow (click on three dots to access this option). |
| Owner | Allow the user to edit the owner’s name. |
| Tier | Gives the user an option to add/edit the tier information. |
| Domain | Allows the user to add predefined domain name. |
| Tags | Add/Remove tags/glossary terms/tag groups. |
| Request Tags Update (?) | Request updates in tags and assign users to do it. |
| Description | Allows the user to edit the description |
| Request Description Update (?) | Request updates in the description and assign users to do it. |
| Tasks | Option to view tasks created. In the side pane, the user will get the option to create a new task. |
| Conversations | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign. |

The subsequent **tabs** will provide you with more detailed information, as explained in the following sections.

### **Details**

| Attribute | Description |
| --- | --- |
| Workspace | Indicates workspace within DataOS instance where Workflow is created |
| Version | Indicates the specific version or release of the DataOS Workflow Resource |
| State | Represents the current state of the DataOS Workflow Resource |
| Aggregate Status | Consolidated status of Workflow Resource |
| Builder State |  |
| Runtime State |  |
| Lifecycle Event(s) | Logs significant occurrences such as creation and deletion |

### **Jobs**

**Dag** 

A Directed Acyclic Graph (DAG) is a conceptual representation of a sequence of jobs or activities. In a DAG, these jobs are executed in the order of their dependencies.

![wf_jobs.png](metis_resources_workflows/wf_jobs.png)

**List**

In this section, you can view a list of jobs, along with their names and descriptions, that are part of the workflow.

Click on a job to learn more about the following:

- [Details](metis_resources_workflows.md)
- [Topology](metis_resources_workflows.md)
- [Lineage](metis_resources_workflows.md)

**Details**

| Attribute | Description |
| --- | --- |
| Stack | The version of the Stack  |
| Log Level |  |
| Compute |  |
| Run As User | Authority granted to perform operations on behalf of the assigned user ID |
| Configurations
- Requests
- Limits
 | CPU and Memory allocation |
| Stack Specification | A segment of the YAML file specifying the input, output, and steps for the transformation in the data processing job. |

**Topology**

This section represents the Dag (of Transformations)**,** outlining the steps defined in the Flare job. It may include one or more sequences for executing the steps necessary for performing transformations or applying Flare functions or commands. Each intermediate step in a sequence may generate a view referenced in subsequent actions or outputs. Here, users can view these sequences, SQL statements, and Flare functions used for transformations. 

![image](metis_resources_workflows/wf_job_topology.png)
<figcaption align = "center">Dag of transformations  </figcaption>

- Clicking on the **SQL statement** will display the following details on the side pane:
    
    ![image](metis_resources_workflows/wf_job_topology_sql.png)
    <figcaption align = "center"> SQL statement </figcaption>
    
    | Attribute | Description |
    | --- | --- |
    | Name | Name of the underlying selected entity |
    | Type | Type of selected entity within dag, such as step, function, frame, etc. |
    | Doc | Details provided for the SQL transformation defined in the step |
    | SQL | SQL statement to transform data |
    | Depends | Specifies the dependency |
- Clicking on the **data frame (intermediate view)** will display the following details on the side pane:
    
    ![image](metis_resources_workflows/wf_job_topology_frame.png)
    <figcaption align = "center"> Data frame details </figcaption>
    | Attribute | Description |
    | --- | --- |
    | Name | Name of the underlying selected entity |
    | Type | Type of selected entity within dag, such as step, function, frame, etc. |
    | Doc | Details provided for the transformation defined in the step |
    | Depends | Specifies the dependency |
- Clicking on the **Flare function** will display the following details on the side pane:
    
    | Attribute | Description |
    | --- | --- |
    | Name | Name of the selected entity |
    | Type | Type of selected entity within dag, such as step, function, frame, etc. |
    | Doc | Details provided for the Flare function defined in the step |
    | Depends | Specifies the dependency |

**Lineage**

The lineage graph visually portrays the relationships between workflows and derived datasets, offering a clear representation of how data entities are related and how they might have changed over time.

![image](metis_resources_workflows/wf_job_lineage.png)
<figcaption align = "center"> Relationship betwen workflows and generated datasets  </figcaption>

### **Activity Feeds & Tasks**

This space compiles all activities, including tasks and conversations, providing users with a comprehensive overview.

### **Manifest**

This section provides details about the manifest. A manifest file is a YAML configuration file that defines the configuration of various DataOS Resources.

### **Run History**

This section includes a summary of the workflow run history.

![wf_runhistory.png](metis_resources_workflows/wf_runhistory.png)
<figcaption align = "center">Workflow run history  </figcaption>

| Attribute | Description |
| --- | --- |
| Run ID | The unique identifier for the workflow run |
| Status | Runtime status of the workflow run, such as Succeeded, Running, Aborted, Failed |
| Started At | Date and time when workflow run |
| Duration | Duration of workflow run |

- Clicking on a workflow run will display the following options.
    
    #### **Run Details**
    
    To get the workflow run details, click **Run History** >> **RunID >> Logical Plan >> Job >> Run Details**
    
    ![Screen Shot 2023-09-13 at 8.03.09 PM.png](metis_resources_workflows/Screen_Shot_2023-09-13_at_8.03.09_PM.png)
    <figcaption align = "center"> Run details </figcaption>
    
    #### **Pod Details**
    
    To get the pod details, click Workflow **Run History** >> **RunID >> Physical Plan >> Node** 
    
    You can access pod details, pod usage, and pod logs
    
    ![Screen Shot 2023-09-13 at 8.06.25 PM.png](metis_resources_workflows/Screen_Shot_2023-09-13_at_8.06.25_PM.png)
    <figcaption align = "center"> Pod details </figcaption>
    
    #### **Resource Usage**
    
    To get the workflow run details, click **Run History** >> **RunID >> Job >> Resource Usage**
    
    ![Screen Shot 2023-09-13 at 7.47.31 PM.png](metis_resources_workflows/Screen_Shot_2023-09-13_at_7.47.31_PM.png)
    <figcaption align = "center"> Resource usage </figcaption>