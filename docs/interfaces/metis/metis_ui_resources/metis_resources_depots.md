# Depots Metadata On Metis UI

<aside class="callout">
⚠️ This page guides you on exploring and managing metadata for Depots on Metis. To learn in detail about the Depot as a Resource, refer to this <a href="/resources/depot/">link</a>.

</aside>

Metis has integrated "Depot" as a "Resource type" for storing metadata related to connecting data sources, Compute resources defined for the depots, connection secrets, and more. On selecting **Depots,** the following information will appear on the screen:

![depots.png](metis_resources_depots/depots.png)
<figcaption align = "center"> List of Depots  </figcaption>

## Filter pane

The filter pane allows you to filter the list of Depots on the basis of the following attributes:

| Attribute | Description |
| --- | --- |
| Advance Filter | Filter Depots using the syntax editor, applying various criteria with 'and/or' conditions for a more refined search. |
| Show Deleted | Set the toggle to list deleted Depots. |
| Depotsource | Allows to filter Depot based on the Depot Source. |
| Domain | Allows users to filter Depots based on the pre-defined domains |
| Owner | Filter the list for the specific owners |
| Tag | Filter the list for tags. |
| Tier | Filter the list on the basis of tiers. |

## Result pane

Here, Depots will be listed. Users have the following options to customize how the list is displayed:

| Option | Description |
| --- | --- |
| Sorting | Choose the Sorting order
- Last updated
- Relevance |
| Sorting order | Ascending/Descending order. |

Each Depot in the list will feature a card view that displays the following information for that particular Depot:

| Attribute | Description |
| --- | --- |
| Name | Depot name, defined in the resource YAML. |
| Owner | Name of the user who created the Depot. |
| Tier | Tier associated with the importance and criticality of Depot, such as Gold, Silver, etc. |
| Domain | Associated domain, such as Finance, Marketing etc. |
| Description | Description added to the Depot. |

## Overview pane

In the card view, click anywhere except the resource name to get the overview.

![depot_overview.png](metis_resources_depots/depot_overview.png)
<figcaption align = "center"> Quick information  </figcaption>

| Attribute | Description |
| --- | --- |
| Name | Name of Depot, clicking on it will open its detail view in the new tab. |
| Type | Type of the DataOS Resource, (Depot in this case). |
| Layer | Name of the layer in which the Resource is deployed. |
| Version | Metadata version. |
| State | Depot state such as Active or Deleted. |
| Followers Count | Count of users who are following this Depot. |
| Last updated | Date and time information when the Depot was last updated. |
| Spec | Information about the mapping with the underlying storage structure- specifies the precise location of the data and provides the hierarchical structure in which the data is stored. |

## Details Page

In the Result or Overview pane, click on the name of the Depot to open the Resource Details page, which includes:

![depots_details.png](metis_resources_depots/depots_details.png)
<figcaption align = "center"> Comprehensive details  </figcaption>

### **Depot Information**

In addition to basic Depot information, the following details and options are provided.

| Attribute | Description |
| --- | --- |
| Resource Type | Depot |
| Meta Version | Provides information on the latest Meta version. Click to see the version history and corresponding updates.  |
| Last Updated | Date and time information when the Depot was last updated. |
| Follow | Gives the user an option to follow the Depot to receive updates and view its follower count. |
| Learn | Provides an option to learn more about this specific resource type |
| Delete | Gives the user the option to delete the Depot (click on three dots to access this option). |
| Owner | Allow the user to edit the owner’s name. |
| Tier | Gives the user an option to add/edit the tier information. |
| Domain | Allows the user to add the predefined domain name. |
| Description | Allows the user to edit the description |
| Tags | Add/Remove tags/glossary terms/tag groups. |
| Type | Depot type (Depends on the underlying data source) |
| Layer | Name of the layer in which the Resource is deployed |
| Request Tags Update (?) | Request updates in tags and assign users to do it. |
| Request Description Update (?) | Request updates in the description and assign users to do it |
| Tasks | Option to view tasks created. In the side pane, the user will get the option to create a new task |
| Conversations | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign |

The subsequent tabs will provide you with more detailed information, as explained in the following sections.

### **Details**

| Attribute | Description |
| --- | --- |
| Type | Depot type (Depends on the underlying data source) |
| Layer | Name of the layer in which the Resource is deployed |
| Version | The specific version or release of the DataOS Depot Resource |
| State | Current state of the Resource |
| Aggregate Status |  |
| Builder state |  |
| Run As User | Authority granted to perform operations on behalf of the assigned user ID |
| Configurations
- Requests
- Limits | CPU and Memory allocation |

### **Activity Feeds & Tasks**

This space lists all activities, including tasks and conversations around the specific depot.

### **Manifest**

This section offers comprehensive information regarding the depot's manifest. A manifest file, in this context, takes the form of a YAML configuration file. This file serves as the blueprint that defines the configuration settings for various DataOS Resources. 

### **Runtime**

This section provides an overview of the depot's execution history. It offers a concise summary of past runs, allowing users to quickly access information about the depot's previous operations and performance. Click on the link to know more details.

![depot_runtime.png](metis_resources_depots/depot_runtime.png)
<figcaption align = "center"> Runtime for file based and blob storage depots </figcaption>

You can access the following:

**Pod Details** 

This option provides information about the depot's underlying pods, including their configuration and status.

**Pod Manifest**

View a YAML configuration file defining the pod's settings and attributes, providing a clear view of its setup.

**Pod Logs**

Users can access logs generated by the depot's pods, helping to troubleshoot issues and monitor activity.

**Pod Usage**

This option will provide insights into how the pods are utilized, including resource consumption and performance metrics.

<aside class="callout">
🗣 Runtime information is particularly relevant for file-based and blob storage depots that do not inherently possess a built-in metastore.

</aside>