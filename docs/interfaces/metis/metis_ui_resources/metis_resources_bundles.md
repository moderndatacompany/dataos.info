# Metadata of Bundles on Metis UI
<aside class="callout">
🗣 This page guides you on exploring and managing metadata for Bundles on Metis. To learn in detail about the Cluster as a Resource, refer to this <a href="/resources/">link</a>.
</aside>

Metis has integrated "Bundle" as a "Resource" type for storing metadata related to the collection of Resources deployed as part of a bundle. On selecting **Bundle,** the following information will appear on the screen:

![bundles.png](metis_resources_bundles/bundles.png)
<figcaption align = "center"> List of bundles </figcaption>

## Filter pane

The filter pane allows you to filter the list of Bundles on the basis of the following attributes:

| Attribute | Description |
| --- | --- |
| Advance Search | Filter Bundles using the syntax editor, applying various criteria with 'and/or' conditions for a more refined search. |
| Show Deleted | Set the toggle to list deleted Bundle. |
| Tag | Filter the list for tags. |
| Tier | Filter the list for tiers. |

## Result pane

Here, Bundle resources will be listed. Users have the following options to customize how the list is displayed:

| Option | Description |
| --- | --- |
| Sorting Order | Choose the Sorting order
- Last updated
- Relevance |
|  | Ascending/Descending order. |

Each bundle resource in the list will have a Card view that displays the following information for that specific bundle:

| Attribute | Description |
| --- | --- |
| Name | Bundles name defined in the resource YAML. |
| Owner | Name of the user who created the Bundle. |
| Tier | Tier associated with the importance and criticality of Bundle, such as Gold, Silver, etc. |
| Domain | Associated domain, such as Finance, Marketing etc. |
| Description | A description added to the Bundle for its purpose. |
| Tags | Associated tags |

## Overview pane

In the card view, click anywhere except the resource name to get the overview.

![bundle_overview.png](metis_resources_bundles/bundle_overview.png)
<figcaption align = "center"> Quick information  </figcaption>

This includes the following quick reference information:

| Attribute | Description |
| --- | --- |
| Name | Name of Bundle, clicking on it will open its detail view in the new tab |
| Layer | Name of the layer in which the Resource is deployed |
| Version | Resource version |
| State | Bundle state such as Active or Deleted |
| Followers Count | Count of users who are following this Bundle |
| Last updated | Date and time information when the Bundle was last updated  |

## Details Page

In the Result or Overview pane, click on the name of the Bundle to open the Details page, which includes:

![bundle_details.png](metis_resources_bundles/bundle_details.png)
<figcaption align = "center"> Comprehensive details  </figcaption>

### **Bundle Information**

In addition to basic Bundle information, the following details and options are provided.

| Attribute | Description |
| --- | --- |
| Resource Type | Bundle |
| Meta Version | Provides information on the latest Meta version. Click to see the version history and corresponding updates.  |
| Last updated | Date and time information when the Bundle was last updated  |
| Follow | Gives the user an option to follow the Bundle to receive updates and view its follower count. |
| Learn | Provides an option to learn more about this specific resource type |
| Delete | Gives the user the option to delete the Bundle (click on three dots to access this option). |
| Owner | Allow the user to edit the owner’s name. |
| Tier | Gives the user an option to add/edit the tier information. |
| Domain | Allows the user to add the predefined domain name. |
| Tags | Add/Remove tags/glossary terms/tag groups. |
| Request Tags Update (?) | Request updates in tags and assign users to do it. |
| Description | Allows the user to edit the description. |
| Request Description Update (?) | Request updates in the description and assign users to do it. |
| Tasks | Option to view tasks created. In the side pane, the user will get the option to create a new task. |
| Conversations | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign. |

The subsequent tabs will provide you with more detailed information, as explained in the following sections.

### **Details**

| Attribute | Description |
| --- | --- |
| Layer | Name of the layer in which the Resource is deployed |
| Version | The specific version or release of the DataOS Depot Resource |
| State | Current state of the Resource |
| Aggregate Status |  |
| Builder state |  |
| Workspaces |  |
| Life Cycle Event(s) | Logs significant occurrences such as creation and deletion |

### **Resources**
**Dag**

A Directed Acyclic Graph (DAG) is a conceptual representation of a sequence of Resources. In a DAG, these resources are deployed in the order of their dependencies.

![bundle_resources.png](metis_resources_bundles/bundle_resources.png)

**List**

In this section, you can view a list of Resources, along with their names, descriptions and types, that are part of the Bundle.

### **Activity Feeds & Tasks**

This space lists all activities, including tasks and conversations around the specific bundle resource.

### **Manifest**

This section offers comprehensive information regarding the bundle's manifest. A manifest file, in this context, takes the form of a YAML configuration file. This file serves as the blueprint that defines the configuration settings for various DataOS Resources.