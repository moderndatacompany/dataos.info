# Cataloging of Scanner Stack

Metis has integrated "Workflows" as a "Resource Type" to store metadata related to various Workflows designed for different purposes. This includes Workflows such as metadata scanning for multiple Resources, quality checks, data pipeline, Flare jobs etc.

When selecting a Workflow, the following information is displayed on the screen:

<img src="/resources/stacks/scanner/scanner_img//01-catalogin-scanner.png"  class="center" style="width:45rem; display: block; margin: 0 auto; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />

## Filter pane

The filter pane allows the user to filter the list of Workflows based on the different attributes as discussed below:

| Attribute      | Description                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Advance Filter | Filter Workflows using the syntax editor, applying various criteria with 'and/or' conditions for a more refined search. |
| State          | Set the toggle to list active or deleted Workflows.                                                                     |
| Workspace      | Allows to filter Workflow based on the Workspace.                                                                       |
| Domain         | Allows users to filter Workflows based on the pre-defined domains                                                       |
| Owner          | Filter the list for the specific owners                                                                                 |
| Tag            | Filter the list for tags.                                                                                               |
| Tier           | Filter the list on the basis of tiers.                                                                                  |

## Result pane

In the Result pane, users have the following options to customize how the list is displayed:

| Option            | Description                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------- |
| **Sorting**       | **Last updated**: Sort by the most recently updated items. **Relevance**: Sort by relevance based on content. |
| **Sorting order** | **Ascending**: Sort from lowest to highest. **Descending**: Sort from highest to lowest.                      |

Each Workflow in the list will feature a card view that displays the following information for that particular Workflow:

| Attribute   | Description                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------- |
| Name        | Workflow name, defined in the resource YAML.                                                |
| Owner       | Name of the user who created the Workflow.                                                  |
| Tier        | Tier associated with the importance and criticality of Workflow, such as Gold, Silver, etc. |
| Domain      | Associated domain, such as Finance, Marketing etc.                                          |
| Description | Description added to the Workflow.                                                          |
| Workspace   | Name of the Workspace in which the Workflow existed                                         |
| State       | Status of the Workflow as Active or Deleted                                                 |

## Overview pane

In the card view, click anywhere except the resource name to get the overview.

<img src="/resources/stacks/scanner/scanner_img//02-catalogin-scanner.png"  class="center" style="width:45rem; display: block; margin: 0 auto; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />

For instance, the Overview pane gives the details of `system-metadata-sync` Scanner Workflow which are as follows:

| Attribute            | Description                                              |
| -------------------- | -------------------------------------------------------- |
| **Workspace**        | **System**                                               |
| **Version**          | 0.3                                                      |
| **State**            | Active                                                   |
| **Followers Count**  | Not available                                            |
| **Last Updated**     | December 12, 2024 at 02:00 PM by metis                   |
| **Jobs**             |                                                          |
| **fastbase-scanner** | Scans and publishes all datasets from fastbase to metis. |
| **icebase-scanner**  | Scans and publishes all datasets from icebase to metis.  |

## Detailed Page

When the user click on the name of the Workflow, the page redirects to the detailed page of that particular Workflow as shown below:

<img src="/resources/stacks/scanner/scanner_img//03-catalogin-scanner.png"  class="center" style="width:45rem; display: block; margin: 0 auto; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />

This page includes comprehensive details about the Workflow as shown in the above image.

### **Workflow Information**

In addition to basic Scanner information, the following details and options are provided.

| Attribute                      | Description                                                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| Resource Type                  | Workflow                                                                                                                  |
| Meta Version                   | Provides information on the latest Meta version.                                                                          |
| Last Updated                   | Date and time information when the Scanner Workflow was last updated.                                                     |
| Follow                         | Gives the user an option to follow the Scanner to receive updates and view its follower count.                            |
| Learn                          | Provides an option to learn more about this specific resource type                                                        |
| Delete                         | Gives the user the option to delete the Workflow (click on three dots to access this option).                             |
| Owner                          | Allow the user to edit the owner’s name.                                                                                  |
| Tier                           | Gives the user an option to add/edit the tier information.                                                                |
| Domain                         | Allows the user to add the predefined domain name.                                                                        |
| Description                    | Allows the user to edit the description                                                                                   |
| Tags                           | Add/Remove tags/glossary terms/tag groups.                                                                                |
| Type                           | Workflow type (Depends on the underlying data source)                                                                     |
| Layer                          | Name of the layer in which the Resource is deployed                                                                       |
| Request Tags Update (?)        | Request updates in tags and assign users to do it.                                                                        |
| Request Description Update (?) | Request updates in the description and assign users to do it                                                              |
| Tasks                          | Option to view tasks created. In the side pane, the user will get the option to create a new task                         |
| Conversations                  | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign |

The subsequent tabs will provide users with more detailed information, as explained in the following sections.

### **Details**

| Attribute        | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| Type             | Workflow type (Depends on the underlying data source)                     |
| Layer            | Name of the layer in which the Resource is deployed                       |
| Version          | The specific version or release of the DataOS Scanner Resource            |
| State            | Current state of the Resource                                             |
| Aggregate Status | Aggregate status active or not                                            |
| Builder state    | Weather Workflow is running or pending                                    |
| Run As User      | Authority granted to perform operations on behalf of the assigned user ID |

### **Activity Feeds & Tasks**

This space lists all activities, including tasks and conversations around the specific Workflow.

### **Manifest**

This section offers comprehensive information regarding the Workflow's manifest. A manifest file, in this context, takes the form of a YAML configuration file. This file serves as the blueprint that defines the configuration settings for various DataOS Resources.

### **Runtime/ Run History**

This section provides an overview of the Workflow's execution history. It offers a concise summary of past runs, allowing users to quickly access information about the Workflow's previous operations and performance.