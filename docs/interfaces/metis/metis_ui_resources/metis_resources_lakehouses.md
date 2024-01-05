# Lakehouses Metadata On Metis UI

<aside class="callout">
⚠️ This page guides you on exploring and managing metadata for Lakehouses on Metis. To learn in detail about the Lakehouse as a  DataOS Resource, refer to this <a href="/resources/">link</a>.

</aside>

Metis has integrated "Lakehouse" as a "Resource" type entity for storing metadata related to its configuration, such as compute used, depot used to refer, and metastore properties within DataOS. On selecting **Lakehouses,** the following information will appear on the screen:

![lakehouses.png](metis_resources_lakehouses/lakehouses.png)
<figcaption align = "center"> List of Lakehouses  </figcaption>

## Filter pane

The filter pane allows you to filter the list of Lakehouses on the basis of the following attributes:

| Attribute | Description |
| --- | --- |
| Advance Filter | Discover specific Lakehouse using the syntax editor with and/or conditions. |
| Show Deleted | Set the toggle to list deleted Lakehouses. |
| Owner | Filter the list for the specific owner. |

## Result pane

Here, Lakehouses will be listed. Users have the following options to customize how the list is displayed:

| Option | Description |
| --- | --- |
| Sorting | Choose the Sorting order
- Last updated
- Relevance |
| Sorting order | Ascending/Descending order. |
| Advance Search | Discover specific Lakehouse using the syntax editor with and/or conditions. |

Each Lakehouse resource in the list will have a Card view that displays the following information for that specific Lakehouse:

| Attribute | Description |
| --- | --- |
| Name | Lakehouse name, defined in the resource YAML. |
| Owner | Name of the user who created the Lakehouse. |
| Tier | Tier associated with the importance and criticality of Lakehouse, such as Gold, Silver, etc. |
| Domain | Associated domain, such as Finance, Marketing etc. |
| Workspace | Workspace where the Lakehouse is created, like public or user-specific. |
| State | State of the Lakehouse resource, such as Active or Deleted. |
| Description | A description, added to the Lakehouse for its purpose. |

## Overview pane

In the card view, click anywhere except the resource name to get the overview.

![lakehouse_overview.png](metis_resources_lakehouses/lakehouse_overview.png)
<figcaption align = "center"> Quick information  </figcaption>

This includes the following information for quick reference:

| Attribute | Description |
| --- | --- |
| Name | Name of Lakehouse created, clicking on it will open its detail view in the new tab. |
| Workspace | Workspace where Lakehouse is created like public or user-specific. |
| Version | Metadata version. |
| State | Lakehouse state such as Active or Deleted. |
| Followers Count | Count of users who are following this Lakehouse. |
| Last updated | Date and time information when the Lakehouse was last updated. |

## Details Page

In the Result or Overview pane, click on the name of the Lakehouse to open the Resource Details page, which includes:

![lakehouse_details.png](metis_resources_lakehouses/lakehouse_details.png)
<figcaption align = "center"> Comprehensive details  </figcaption>

### **Lakehouses Information**

In addition to basic Lakehouse information, the following details and options are provided.

| Attribute | Description |
| --- | --- |
| Resource Type | Lakehouse. |
| Meta Version | Provides information on the latest Meta version. Click to see the version history and corresponding updates.  |
| Last updated | Date and time information when the Lakehouse resource was last updated. |
| Follow | Gives the user an option to follow the specific resource type to receive updates and view its follower count. |
| Learn | Provides an option to learn more about this specific resource type. |
| Delete | Gives the user an option to delete the Lakehouse(click on three dots to access this option). |
| Owner | Allow the user to edit the owner’s name. |
| Tier | Gives the user an option to add/edit the tier information. |
| Domain | Allows the user to add the predefined domain name. |
| Tags | Add/Remove tags/glossary terms/tag groups. |
| Request Tags Update (?) | Request updates in tags for the resource and assign users to do it. |
| Description | Allows the user to edit the description. |
| Request Description Update (?) | Request updates in the description and assign users to do it. |
| Tasks | Option to view tasks created. In the side pane, the user will get the option to create a new task. |
| Conversations | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign. |

The subsequent **tabs** will provide you with more detailed information, as explained in the following sections.

### **Details**

| Attribute | Description |
| --- | --- |
| Workspace | Workspace where Lakehouse is created like public or user-specific. |
| Version | The specific version or release of the Resource |
| State | The current state of the Resource such as Active or Deleted. |
| Aggregate Status
 |  |
| Builder State |  |
| Compute | Name of the Compute Resource |
| Run As User |  |
| Lifecycle Events | Records the creation and deletion events related to the DataOS Lakehouse Resource. |

### **Activity Feeds & Tasks**

This space lists all activities, including tasks and conversations around the specific Lakehouse

### **Manifest**

This section offers comprehensive information regarding the Lakehouse's manifest. A manifest file, in this context, takes the form of a YAML configuration file. This file serves as the blueprint that defines the configuration settings for various DataOS Resources.