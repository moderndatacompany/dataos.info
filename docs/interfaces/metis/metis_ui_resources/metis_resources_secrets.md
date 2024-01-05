# Secrets Metadata On Metis UI

<aside class="callout">
⚠️ This page guides you on exploring and managing metadata for Secrets on Metis. To learn in detail about the Secret as a DataOS Resource, refer to this <a href="/resources/secret/">link</a>.

</aside>

Metis has integrated "Secret" as a "Resource" type entity for storing metadata related to the source for which it is created, the specific workspace of its creation, and its current state within DataOS. On selecting **Secrets,** the following information will appear on the screen:

![secrets.png](metis_resources_secrets/secrets.png)
<figcaption align = "center"> List of Secrets  </figcaption>

## Filter pane

The filter pane allows you to filter the list of Secrets on the basis of the following attributes:

| Attribute | Description |
| --- | --- |
| Advance Filter | Filter the Secrets using the syntax editor, applying various criteria with 'and/or' conditions for a more refined search. |
| Show Deleted | Set the toggle to list deleted Secrets. |
| Workspace | Filter on the basis of workspace where the Secret is created, like public or user-specific. |
| Owner | Filter Secrets based on the users who created the Resource. |
| Tag | Filter Secrets for tags. |

## Result pane

Here, secrets will be listed. Users have the following options to customize how the list is displayed:

| Option | Description |
| --- | --- |
| Sorting | Choose the Sorting order
- Last updated
- Relevance |
| Sorting order | Ascending/Descending order. |

Each secret resource in the list will have a Card view that displays the following information for that specific secret:

| Attribute | Description |
| --- | --- |
| Name | Secret name, defined in the resource YAML. |
| Owner | Name of the user who created the secret. |
| Tier | Tier associated with the importance and criticality of Secrets, such as Gold, Silver, etc. |
| Domain | Associated domain, such as Finance, Marketing etc. |
| Workspace | Workspace where the secret is created, like public or user-specific. |
| Description | A description added to the Secret for its purpose. |

## Overview pane

In the card view, click anywhere except the resource name to get the overview.

![secret_overview.png](metis_resources_secrets/secret_overview.png)
<figcaption align = "center"> Quick information  </figcaption>

This includes the following information for quick reference:

| Attribute | Description |
| --- | --- |
| Name | Name of Secret created, clicking on it will open its detail view in the new tab. |
| Workspace | Workspace where secret is created like public or user-specific. |
| Version | Metadata version. |
| State | State of the Secret Resource such as Active or Deleted. |
| Followers Count | Count of users who are following this Secret Resource. |
| Last updated | Date and time information when the Secret was last updated. |

## Details Page

In the Result or Overview pane, click on the name of the secret to open the Resource Details page, which includes:

![secret_details.png](metis_resources_secrets/secret_details.png)
<figcaption align = "center"> Comprehensive details  </figcaption>

### **Secrets Information**

In addition to basic Secret information, the following details and options are provided.

| Attribute | Description |
| --- | --- |
| Resource Type | Secret. |
| Meta Version | Provides information on the latest Meta version. Click to see the version history and corresponding updates.  |
| Last updated | Date and time information when the Secret resource was last updated. |
| Follow | Gives the user an option to follow the specific resource type to receive updates and view its follower count. |
| Learn | Provides an option to learn more about this specific resource type. |
| Delete | Gives the user the option to delete the secret (click on three dots to access this option). |
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
| Workspace | Workspace where Secret is created like public or user-specific |
| Version | The specific version or release of the Resource |
| State | Current state of the Resource such as Active or Deleted. |
| Aggregate Status |  |
| Builder State |  |
| Life Cycle Events | Records significant events such as creation and deletion |

### **Activity Feeds & Tasks**

This space lists all activities, including tasks and conversations around the specific secret.

### **Manifest**

This section offers comprehensive information regarding the secret's manifest. A manifest file, in this context, takes the form of a YAML configuration file. This file serves as the blueprint that defines the configuration settings for various DataOS Resources.