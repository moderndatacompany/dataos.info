# Metadata of Stacks on Metis UI

<aside class="callout">
🗣 This page guides you on exploring and managing metadata for Stacks on Metis. To learn in detail about the Stack as a DataOS Resource, refer to this <a href="/resources/stacks/">link</a>.

</aside>

Metis has integrated "Stack" as a "Resource” type entity for storing metadata related to the unique attributes that define its capabilities within DataOS. On selecting **Stacks,** the following information will appear on the screen:

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_resources/metis_resources_stacks/stacks.png" alt="List of Stacks" style="border:1px solid black; width: 80%; height: auto">
    <figcaption>List of Stacks</figcaption>
  </div>
</center>


## Filter pane

The filter pane allows you to filter the list of Stacks on the basis of the following attributes:

| Attribute | Description |
| --- | --- |
| Advance Filter | Filter the Stacks using the syntax editor, applying various criteria with 'and/or' conditions for a more refined search. |
| Show Deleted | Set the toggle to list deleted Stacks. |
| Owner | Filter Stacks based on the users who created the Resource. |
| Tag | Filter Stacks for tags. |

## Result pane

Here, Stack (built-in as well as custom) resources will be listed. Users have the following options to customize how the list is displayed:

| Option | Description |
| --- | --- |
| Sorting | Choose the Sorting order
- Last updated
- Relevance |
| Sorting order | Ascending/Descending order. |

Each stack resource in the list will have a Card view that displays the following information for that specific stack:

| Attribute | Description |
| --- | --- |
| Name | Stacks name defined in the resource YAML. |
| Owner | Name of the user who created the Stack. |
| Tier | Tier associated with the importance and criticality of Stacks, such as Gold, Silver, etc. |
| Domain | Associated domains, such as Finance, Marketing etc. |
| Description | A description added to the Stacks for its purpose. |

## Overview pane

In the card view, click anywhere except the resource name to get the overview.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_resources/metis_resources_stacks/stack_overview.png" alt="Quick information" style="border:1px solid black; width: 80%; height: auto">
    <figcaption>Quick information</figcaption>
  </div>
</center>


This includes the following information for quick reference:

| Attribute | Description |
| --- | --- |
| Name | Name of Stack, clicking on it will open its detail view in the new tab. |
| Layer | Name of the layer in which the Resource is deployed. |
| Version | Resource version. |
| Reconciler | Refers to the reconciler component used for validating the stack, such as "flareLegacyStackManager", “beaconLegacyStackManager” |
| State | Stack state such as Active or Deleted. |
| Followers Count | Count of users who are following this Stack. |
| Last updated | Date and time information when the Stack was last updated by a user. |

## Details Page

In the Result or Overview pane, click on the name of the Stack to open the Resource Details page, which includes:

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_resources/metis_resources_stacks/stack_detail.png" alt="Comprehensive details" style="border:1px solid black; width: 80%; height: auto">
    <figcaption>Comprehensive details</figcaption>
  </div>
</center>


### Stacks Information

In addition to basic Stack information, the following details and options are provided.

| Attribute | Description |
| --- | --- |
| Resource Type | Stack |
| Meta Version | Provides information on the latest Meta version. Click to see the version history and corresponding updates.  |
| Last updated | Date and time information when the Stack was last updated. |
| Follow | Gives the user an option to follow the Stacks to receive updates and view its follower count. |
| Learn | Provides an option to learn more about this specific resource type. |
| Delete | Gives the user the option to delete the Stack (click on three dots to access this option). |
| Owner | Allow the user to edit the owner’s name. |
| Tier | Gives the user an option to add/edit the tier information. |
| Domain | Allows the user to add the predefined domain name. |
| Tags | Add/Remove tags/glossary terms/tag groups. |
| Request Tags Update (?) | Request updates in tags and assign users to do it. |
| Description | Allows the user to edit the description |
| Request Description Update (?) | Request updates in the description and assign users to do it |
| Tasks | Option to view tasks created. In the side pane, the user will get the option to create a new task |
| Conversations | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign |

The subsequent tabs will provide you with more detailed information, as explained in the following sections.

### Details

| Attribute | Description |
| --- | --- |
| Layer | Name of the layer in which the Stack Resource is deployed |
| Version | The specific version or release of the Resource |
| Reconciler | Specifies the reconciler responsible for managing this stack |
| SecretProjection.type | Describes how secrets are projected for this Stack |
| Dataos Stack Version | Version of the Stack |
| Flavor | Specifies the configuration or type of the Stack Resource within the DataOS environment. |
| State | The current state of the Resource |
| Aggregate Status
 |  |
| Builder State |  |
| Bundles | List of Bundle Resources containing the Stack |
| Life Cycle Events | Records the creation and deletion events related to the DataOS Stack Resource. |

### Activity Feeds & Tasks

This space lists all activities, including tasks and conversations around the specific stack resource.

### Manifest

This section offers comprehensive information regarding the Stack's manifest. A manifest file, in this context, takes the form of a YAML configuration file. This file serves as the blueprint that defines the configuration settings for various DataOS Resources.