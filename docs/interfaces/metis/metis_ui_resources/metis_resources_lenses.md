# Metadata of Lenses on Metis UI

<aside class="callout">
🗣 This page guides you on exploring and managing metadata for Lenses on Metis. 

</aside>

Metis has integrated "**Lens**" as a "Resource type" entity for storing metadata related to its entities. On selecting **Lens**, the following information will appear on the screen:

<div style="text-align: center;">
  <img src="/interfaces/metis/metis_ui_resources/metis_resources_lenses/lenses.png" alt="List of Lenses" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption>List of Lenses</figcaption>
</div>


## Filter pane

The filter pane allows you to filter the list of Lenses on the basis of the following attributes:

| Attribute | Description |
| --- | --- |
| Advance Filter | Filter Lenses using the syntax editor, applying various criteria with 'and/or' conditions for a more refined search. |
| Owner | Name of the user who created the Lens. |
| Source | Source on top of which Lens is created. |
| State | Lens state such as Active or Deleted. |
| Tags | Filter the list for tags. |
| Workspace | Workspace where the Lens is created, like public or user-specific. |

## Result pane

Here, Lenses will be listed. You can customize how the list is displayed. On top of the page, there are two options:

| Option | Description |
| --- | --- |
| Search Result | Count of Lenses |
| Sorting | Choose the Sorting order<br><ul><li>Last updated</li><br><li>Relevance</li><br><li>Ascending/Descending order</li></ul> |

Each Lens in the list will display the following information:

| Attribute | Description |
| --- | --- |
| Name | Lens name defined in the Resource manifest. |
| Owner | Name of the user who created the Lens. |
| Created | Time of creation of Lens |
| Tier | Tier associated with the importance and criticality of Lens, such as Gold, Silver, etc. |
| Domain | Associated domain, such as Finance, Marketing etc. |
| Workspace | Workspace where the Lens is created like public or user-specific. |
| State | Lens state such as Active or Deleted. |
| Description | A description added to the Lens for its purpose. |
| Tags | Associated tags |

## Overview pane

Click anywhere except the Lens name to view the overview pane. 

<div style="text-align: center;">
  <img src="/interfaces/metis/metis_ui_resources/metis_resources_lenses/lens_overview.png" alt="Quick information" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption>Quick information</figcaption>
</div>


This includes the following quick reference information:

| Attribute | Description |
| --- | --- |
| Name | Name of Lens, clicking on it will open its detail page in the new tab. |
| Workspace | Workspace where Lens is created like public or user-specific. |
| Version | Manifest Version |
| State | Lens state such as Active or Deleted. |
| Followers Count | Count of users who are following this Lens. |
| Last updated | Date and time information when the Lens was last updated. |

## Details Page

In the Result or Overview pane, click on the name of the Lens to open the Resource Details page, which includes:

<div style="text-align: center;">
  <img src="/interfaces/metis/metis_ui_resources/metis_resources_lenses/lens_details.png" alt="Comprehensive details" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption>Comprehensive details</figcaption>
</div>


### **Cluster Information**
In addition to basic Cluster information, the following details and options are provided.

| Attribute | Description |
| --- | --- |
| Explore in Studio | Opens up Lens Studio for exploring the deployed Lens |
| Iris | Opens up Iris dashboard |
| Explore Assets | Explore assets on top of which Lens is built |
| Meta Version | Provides information on the latest Meta version. Click to see the version history and corresponding updates.  |
| Created | Time of creation of Lens |
| Updated | Date and time information when the Lens was last updated  |
| Follow | Gives the user an option to follow the Lens to receive updates and view its follower count. |
| Learn | Provides an option to learn more about this specific resource type by redirecting to the documentation |
| Delete | Gives the user the option to delete the Lens (click on three dots to access this option). |
| Owner | Allow the user to edit the owner’s name. |
| Tier | Gives the user an option to add/edit the tier information. |
| Domain | Allows the user to add the predefined domain name. |
| Tags | Add/Remove tags/glossary terms/tag groups. |
| Request Tags Update (? icon) | Request updates in tags and assign users to do it. |
| Description | Allows the user to edit the description |
| Request Description Update (? icon) | Request updates in the description and assign users to do it |
| Tasks | Option to view tasks created. In the side pane, the user will get the option to create a new task |
| Conversations | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign |

The subsequent tabs will provide you with more detailed information, as explained in the following sections.

### **Details**

| Attribute | Description |
| --- | --- |
| Workspace | Workspace where Lens is created like public or user-specific |
| Version | The specific version or release of the DataOS Lens Resource manifest |
| State | Current state of the Resource such as Active or Deleted. |
| Aggregate Status | Aggregate status of Lens |
| Compute | Compute resources used for allocating processing power to Lens API instances, workers, and router |
| Run As User | Authority granted to perform operations on behalf of the assigned user ID |
| Life Cycle Events | Logs significant occurrences such as creation and deletion |

### **Model**

Renders a logical model of the deployed Lens.

### **Permissions**

Provides details related to the access permissions for the Lens.


### **Activity Feeds & Tasks**

This space lists all activities, including tasks and conversations around the specific Lens.

### **Runtime**

This section provides an overview of the Lens API Instances, Workers, and Router. 

<div style="text-align: center;">
  <img src="/interfaces/metis/metis_ui_resources/metis_resources_lenses/runtime.png" alt="Runtime information" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption>Runtime information</figcaption>
</div>


You can access more details by clicking on the link.

**{lens-name}-worker** 

This option provides information about the Lens Worker instances.

**{lens-name}-api**


This option provides information about the Lens API instances.

**{lens-name}-router**


This option provides information about the Lens Router instances.

### **Manifest**

This section offers comprehensive information regarding the Lens's manifest. A manifest file, in this context, takes the form of a YAML configuration file. This file serves as the blueprint that defines the configuration settings for various DataOS Resources. 
