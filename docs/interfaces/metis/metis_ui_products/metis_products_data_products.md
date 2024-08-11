# Metadata of Data Products on Metis UI

Metis collects metadata of data products. The collected metadata is stored in the Metis DB, and the Metis UI presents this wealth of information under the '**Data Products**' section. Users can efficiently locate, access, and interpret Data Products and their associated data.

On selecting **Data Products**,the following information will appear on the screen:

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_products/metis_products_data_products/dps.png" alt="List of data products" style="border:1px solid black; width: 80%; height: auto"">
    <figcaption>List of data products</figcaption>
  </div>
</center>


## Filter pane

The filter pane allows you to filter the data products list on the basis of the following attributes:

| Attribute | Description |
| --- | --- |
| Advance Filter | Filter data products using the syntax editor, applying various criteria with 'and/or' conditions for a more refined search. |
| Show Deleted | Set the toggle to list deleted data products. |
| Owner | Name of the user for the data product |
| Tag | Filter the list for tags. |

## Result pane

Here, assets will be listed. Users have the following options to customize how the list is displayed:

| Option | Description |
| --- | --- |
| Sorting | Choose the Sorting order
- Last updated
- Relevance |
|  | Ascending/Descending order |

Each data product in the list will feature a Card view that displays the following information for that particular table:

| Attribute | Description |
| --- | --- |
| Name | Data product name  |
| Owner | Name of the user who created the data product. |
| Tier | Tier associated with the importance and criticality of asset, such as Gold, Silver, etc. |
| Domain | Associated domain, such as Finance, Marketing etc. |
| Version | Data product meta version |
| Description | A description added to the data product for its purpose. |

## Overview pane

In the Card view, click anywhere except the data product name to get the overview for quick reference.

<center>
  <div style="text-align: center;">
    <img src="interfaces/metis/metis_ui_products/metis_products_data_products/dp_overview.png" alt="Quick information on the side pane" style="border:1px solid black; width: 80%; height: auto"">
    <figcaption>Quick information on the side pane</figcaption>
  </div>
</center>


This includes the following quick reference information:

| Attribute | Description |
| --- | --- |
| Name | Name of the data product, clicking on it will open its detail view in the new tab. |
| Link | Link to open the details on Metis UI |
| Reference Links | Links to documents for the resources used to provide a better understanding of the data product. |

## Details Page

In the Result or Overview pane, click on the name of the data product to open the Details page, which includes comprehensive details such as meta version, last update time, follower count, documentation link, delete option, and various editing options for owner, tier, domain, tags, and description:

### Data Product Information

In addition to basic data product information, the following details and options are provided.

| Attribute | Description |
| --- | --- |
| Products Type | Data Product |
| Meta Version | Provides information on the latest Meta version. Click to see the version history and corresponding updates.  |
| Updated | Provides last updated time  |
| Follow | Gives the user an option to follow the data product to receive updates and view its follower count. |
| Learn | Link to documentation |
| Delete | Gives the user the option to delete the data product (click on three dots to access this option). |
| Announcements | Option to create an announcement for quick updates about data product |
| Owner | Allow the user to edit the owner’s name. |
| Tier | Gives the user an option to add/edit the tier information. |
| Domain | Allows the user to add a predefined domain name. |
| Tags | Add/Remove tags/glossary terms/tag groups. |
| Request Tags Update (?) | Request updates in tags and assign users to do it. |
| Description | Allows the user to edit the description |
| Request Description Update (?) | Request updates in the description and assign users to do it. |
| Tasks | Option to view tasks created. In the side pane, the user will get the option to create a new task. |
| Conversations | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign. |

The subsequent **tabs** on the Details Page provide more detailed information on schema, activity feeds and tasks, executed queries, data profiling, and data quality. These tabs offer in-depth insights into the structure, execution history, and quality of the selected data product.

### **Details**

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_products/metis_products_data_products/dp_details.png" alt="Comprehensive details for a product" style="border:1px solid black; width: 80%; height: auto"">
    <figcaption>Comprehensive details for a product</figcaption>
  </div>
</center>


### **Outputs**

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_products/metis_products_data_products/dp_outputs.png" alt="Outputs provided by data product" style="border:1px solid black; width: 80%; height: auto"">
    <figcaption>Outputs provided by data product</figcaption>
  </div>
</center>


### **SLOs**

You can view the list of Service Level objectives (quality tests) created for your data product to monitor the data quality and the status of each run. 

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_products/metis_products_data_products/dp_slo.png" alt="SLOs for data product" style="border:1px solid black; width: 80%; height: auto"">
    <figcaption>SLOs for data product</figcaption>
  </div>
</center>


Here, you will get the information about the tests designed as per the quality objectives set for your data product.

| Attribute | Description |
| --- | --- |
| SLO | Identifying label or title for the quality test objective. |
| Last Run Result | Outcome of the most recent quality test run for the specified attribute |
| Last Run | Date and time of the last execution of the quality test for the attribute. |

Click on the information icon to see the details of SLO. You can select the number of days to observe the trend.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_products/metis_products_data_products/dp_slodetails.png" alt="SLO details" style="border:1px solid black; width: 80%; height: auto"">
    <figcaption>SLO details</figcaption>
  </div>
</center>


### **Policies**

Here, you can get the information about the access rights for the resources of a data product. In case you dont have enough access rights then the applied policies will be listed for your information. You can contact administrator to get the access to the resources needed. The details include the resource name and policies applied and access information.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_products/metis_products_data_products/dp_policy.png" alt="Information about access rights" style="border:1px solid black;width: 80%; height: auto"">
    <figcaption>Information about access rights</figcaption>
  </div>
</center>


### **Lineage**

The lineage graph illustrates the relationships between workflows/jobs and derived datasets, providing a clear representation of how data entities are related and how they may have changed over time. You can get the details of data flow across workflows and the datasets they produce. Additionally, you can learn about the other dependent datasets. You can explore more by clicking on the dataset/workflow nodes of the lineage graph.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_products/metis_products_data_products/dp_lineage.png" alt="Data product lineage" style="border:1px solid black; width: 80%; height: auto"">
    <figcaption>Data product lineage</figcaption>
  </div>
</center>


### **Activity Feeds & Tasks**

This section compiles all activities, including tasks and conversations, providing users with a comprehensive overview.

### **Resources**

This tab displays information about the resources associated with your data product. The data product comprises these resources.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/metis/metis_ui_products/metis_products_data_products/dp_resources.png" alt="Resources in data product" style="border:1px solid black;width: 80%; height: auto"">
    <figcaption>Resources in data product</figcaption>
  </div>
</center>
