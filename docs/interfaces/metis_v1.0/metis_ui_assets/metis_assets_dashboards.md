# Metis Assets- Dashboards

The Scanner workflow extracts information from the dashboard services using non-depot Scanner workflows. This metadata is about elements such as dashboards, charts, owners, etc. The collected metadata is stored in the Metis DB, and the Metis UI presents this wealth of information under the 'Dashboards' section. Users can efficiently locate, access, and interpret these assets and their associated data.

On selecting **Dashboards,** the following information will appear on the screen:

![image]()

## Filter pane

The filter pane allows you to filter the dashboards list on the basis of the following attributes:

| Attribute | Description |
| --- | --- |
| Advance Filter | Filter dashboards using the syntax editor, applying various criteria with 'and/or' conditions for a more refined search. |
| Show Deleted | Set the toggle to list deleted topics. |
| Domain | Select a domain like Marketing, or Finance, etc., to filter the Dashboard list for associated domains. |
| Owner | Filter the list on the basis of owners of the data asset |
| Source | Filter the list based on the source from which the dashboard data is obtained. |
| Tag | Filter the list for associated tags. |
| Tier | Filter the dashboard list based on the tier associated with the importance and criticality of the asset, such as Gold, Silver, etc. |
| Type | Filter the list based on the Source type scanned |

## Result pane

Here, assets will be listed. Users have the following options to customize how the list is displayed:

| Option | Description |
| --- | --- |
| Sorting | Choose the Sorting order
- Last updated
- Relevance |
|  | Ascending/Descending order |

Each dashboard in the list will feature a Card view that displays the following information for that particular dashboard:

| Attribute | Description |
| --- | --- |
| Name | Dashboard name  |
| Owner | Name of the user who created the dashboard |
| Tier | Tier associated with the importance and criticality of asset, such as Gold, Silver, etc. |
| Domain | Associated domain, such as Finance, Marketing etc. |
| Usage Percentile |  |
| Tags | Associated tags |
| Description | A description, added to the dashboard for its purpose |

## Overview pane

In the card view, click anywhere except the dashboard name to get the overview.

![image]()

This includes the following quick reference information:

| Attribute |  | Description |
| --- | --- | --- |
| Name |  | Name of the dashboard, clicking on it will open its detail view in the new tab. |
| Dashboard URL |  | URL to access the dashboard |
| Charts |  |  |
|  | Chart name and link | Chart link to access  |
|  | Type | Source Type |
|  | Tags | Associated tags |
|  | Description | Description of the chart |
| Data Models |  |  |

## Details Page

In the Result or Overview pane, click on the name of the chart to open the Asset Details page, which includes:

![image]()

### **Dashboard Information**

In addition to basic information on the topic, the following details and options are provided.

| Attribute | Description |
| --- | --- |
| Asset Type | Dashboard |
| Meta Version | Provides information on the latest Meta version. Click to see the version history and corresponding updates.  |
| Updated | Provides last updated time  |
| Follow | Gives the user an option to follow the asset to receive updates and view its follower count. |
| Learn | Link to documentation |
| Delete | Gives the user the option to delete the dashboard (click on three dots to access this option). |
| Announcements | Option to create an announcement for quick updates about the asset |
| Owner | Allow the user to edit the owner’s name. |
| Tier | Gives the user an option to add/edit the tier information. |
| Domain | Allows the user to add a predefined domain name. |
| Tags | Add/Remove tags/glossary terms/tag groups. |
| Request Tags Update (?) | Request updates in tags and assign users to do it. |
| Description | Allows the user to edit the description |
| Request Description Update (?) | Request updates in the description and assign users to do it. |
| Tasks | Option to view tasks created. In the side pane, the user will get the option to create a new task. |
| Conversations | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign. |

The subsequent **tabs** will provide you with more detailed information, as explained in the following sections.

### Details

| Attribute | Description |
| --- | --- |
| Chart Name | Name of the chart |
| Chart Type | Type of chart, e.g., bar chart, line chart, pie chart |
| Description | Description of the content or purpose of the chart |
| Tags | Relevant tags for easy categorization or search |

### **Activity Feeds & Tasks**

This section compiles all activities, including tasks and conversations about the underlying dashboard, providing users with a comprehensive overview.

### **Config**

### **Lineage**

Lineage represents the movement of stream data from source to destination and how it is transformed as it moves. It also gives you the option to configure upstream and downstream depth and nodes per layer.