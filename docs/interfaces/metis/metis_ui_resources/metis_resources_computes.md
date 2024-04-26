# Metadata of Computes on Metis UI

<aside class="callout">
🗣 This page guides you on exploring and managing metadata for Computes on Metis. To learn in detail about the Compute as a  DataOS Resource, refer to this <a href="/resources/compute/">link</a>.

</aside>

Metis has integrated "Compute" as a "Resource” type entity for storing metadata pertaining to its attributes, real-time status, user engagements, manifest details, and more. This metadata plays a crucial role in tracking and management of resources within the Metis platform.

On selecting **Computes,** the following information will appear on the screen:

![computes.png](metis_resources_computes/computes.png)
<figcaption align = "center"> List of compute resources </figcaption>

## Filter pane

The filter pane allows you to filter the list of Computes on the basis of the following attributes:

| Attribute | Description |
| --- | --- |
| Advance Filter | Filter Computes using the syntax editor, applying various criteria with 'and/or' conditions for a more refined search. |
| Show Deleted | Set the toggle to list deleted Computes. |
| Domain | Domain associated |
| Owner | Filter the list based on the user who created the Worker Resource. |
| Tier | Filter the list for tiers. |

## Result pane

Here, compute resources will be listed. Users have the following options to customize how the list is displayed:

| Option | Description |
| --- | --- |
| Sorting | Choose the Sorting order
- Last updated
- Relevance |
| Sorting order | Ascending/Descending order. |

Each compute resource in the list will have a Card view that displays the following information for that specific compute:

| Attribute | Description |
| --- | --- |
| Name | Compute name defined in the resource YAML. |
| Owner | Name of the user who created the Compute. |
| Tier | Tier associated with the importance and criticality of Compute, such as Gold, Silver, etc. |
| Domain | Associated domain, such as Finance, Marketing etc. |
| Description | A description added to the Compute for its purpose. |

## Overview pane

In the card view, click anywhere except the resource name to get the overview.

![compute_overview.png](metis_resources_computes/compute_overview.png)
<figcaption align = "center"> Quick information  </figcaption>

This includes the following quick reference information:

| Attribute | Description |
| --- | --- |
| Name | Name of Compute, clicking on it will open its detail view in the new tab. |
| Layer | Name of the layer in which the Resource is deployed. |
| Version | Metadata version. |
| State | Compute state such as Active or Deleted. |
| Followers Count | Count of users who are following this Compute. |
| Last updated | Date and time information when the Compute was last updated. |

## Details Page

In the Result or Overview pane, click on the name of the Compute to open the Resource Details page, which includes:

![compute_details.png](metis_resources_computes/compute_details.png)
<figcaption align = "center"> Comprehensive details </figcaption>

### **Compute Information**

In addition to basic Compute information, the following details and options are provided.

| Attribute | Description |
| --- | --- |
| Resource Type | Compute. |
| Meta Version | Provides information on the latest Meta version. Click to see the version history and corresponding updates.  |
| Last updated | Date and time information when the Compute was last updated. |
| Follow | Gives the user an option to follow the Compute to receive updates and view its follower count. |
| Learn | Provides an option to learn more about this specific resource type. |
| Delete | Gives the user the option to delete the Compute (click on three dots to access this option). |
| Owner | Allow the user to edit the owner’s name. |
| Tier | Gives the user an option to add/edit the tier information. |
| Domain | Allows the user to add the predefined domain name. |
| Layer | Name of the layer in which the Resource is deployed. |
| Data Plane | DataOS data plane, Hub. |
| State | Compute state such as Active or Deleted. |
| Tags | Add/Remove tags/glossary terms/tag groups. |
| Request Tags Update (?) | Request updates in tags and assign users to do it. |
| Description | Allows the user to edit the description. |
| Request Description Update (?) | Request updates in the description and assign users to do it. |
| Tasks | Option to view tasks created. In the side pane, the user will get the option to create a new task. |
| Conversations | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign. |

The subsequent **tabs** will provide you with more detailed information, as explained in the following sections.

### **Details**

| Attribute | Description |
| --- | --- |
| Layer | Name of the layer in which the Compute Resource is deployed |
| Version | The specific version or release of the Resource |
| Data Plane |  |
| State | The current state of the Resource |
| Aggregate Status
 |  |
| Builder State |  |
| Life Cycle Events | Records the creation and deletion events related to the DataOS Stack Resource. |

### **Activity Feeds & Tasks**

This space lists all activities, including tasks and conversations around the specific Compute resource.

### **Manifest**

This section offers comprehensive information regarding the Compute's manifest. A manifest file, in this context, takes the form of a YAML configuration file. This file serves as the blueprint that defines the configuration settings for various DataOS Resources.