<!-- ---
title: "Exploring metadata of the semantic model "
sidebarTitle: "Cataloging"
description: "The following guide explains how both Metis UI and Data Product Hub allow data users to discover Lens Resources and it's semantic model."
--- -->

# Exploring metadata of the semantic model

The Lens can be discovered through the following platforms:

- [Metis](/resources/lens/cataloging/#exploring-the-semantic-model-and-lens-metadata-via-metis)

- [Data Product Hub](/resources/lens/cataloging/#exploring-the-semantic-model-and-lens-metadata-via-data-product-hub)

These tools enable effective discovery and cataloging, ensuring seamless access to data products across the organization.

## Exploring the semantic model and Lens metadata via Metis

Metis is a data cataloging platform that gathers metadata from Lens resources using the Scanner Stack, which connects to Lens components' exposed APIs to capture both historical and current data. After the data is collected, it is organized and cataloged within the Metis UI, providing an intuitive platform for seamless discovery, governance, and observability.

Key features to discover the Lens and it's metadata on Metis UI.

### **Activity Feeds**

<aside class="callout">
Activity feeds help understand how the data is changing within an organization.
</aside>

In the ‘All Activity’ section, the latest updates, conversations, and tasks that have been assigned can be accessed, helping users stay informed about ongoing changes to Lens resources.

With Activity Feeds for Lens Resource, users can:

* Inform stakeholders about significant changes in Lens resources by posting announcements.
* Follow updates from users, accounts, and conversations related to Lens resources.
* Stay informed in real-time about updates and modifications made to Lens resources.
* Take prompt action on specific updates to address and resolve issues related to Lens resources quickly.

<img src="/resources/lens/cataloging/all_activity.png" alt="Untitled(5)" style="max-width: 40rem; height: auto; border: 1px solid #000;">

### **Discovery**

Metis allows users to search and find Lens and related across the organization quickly, improving accessibility to data. One can easily discover Lens related netadata through:

**Search:** Use the search bar to search for specific Lens resources by name, such as `Productaffinity`.

<img src="/resources/lens/cataloging/metis_search.png" alt="Untitled(5)" style="max-width: 40rem; height: auto; border: 1px solid #000;">

#### **Filter pane**

**Search and Filter:** Quickly search and apply filters to find specific Lens resources like tables and models. To search and filter Lens resources:

* Navigate to the Resources tab in the Metis UI.
* Select Lenses from the available resource categories.
* Use the available filter options to refine your search by attributes such as Owner, Source, Tags, Tier, and Workspace.

<img src="/resources/lens/cataloging/metis_search.png" alt="Untitled(5)" style="max-width: 40rem; height: auto; border: 1px solid #000;">

**Advanced Search Filters:** Utilize advanced filtering options to narrow down results based on various attributes and metadata, helping you find exactly what you're looking for.

<img src="/resources/lens/cataloging/metis_advance_filter.png" alt="Untitled(5)" style="max-width: 40rem; height: auto; border: 1px solid #000;">

#### **Result pane**

Once the results are displayed, Lens resources will be listed. Users have the option to customize the view by filtering the list based on criteria such as 'Last Updated' or 'Relevance' and further sorting them on the basis of Ascending and Descending sorting order.

<img src="/resources/lens/cataloging/result_pane.png" alt="Untitled(5)" style="max-width: 40rem; height: auto; border: 1px solid #000;">


Each Lens in the list features a Card view that presents key information for that particular Lens:

| Attribute   | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| Name        | Lens name as defined in the resource YAML.                             |
| Owner       | Name of the user who created the Lens.                                 |
| Tier        | Tier associated with the importance and criticality of the Lens, such as Gold, Silver, etc. |
| Domain      | Associated domain, such as Finance, Marketing, etc.                         |
| Workspace   | Workspace where the Lens is created, like public or user-specific.     |
| Description | A description added to the Lens for its purpose.                        |

#### **Overview pane**

In the Card view, click anywhere except the Resource name provides a quick overview.

<Frame caption="Quick information">
  <img src="/resources/lens/cataloging/overview_pane.png" />
</Frame>

This includes the following quick reference information:

| Attribute       | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Name            | Name of Lens, clicking on it will open its detail view in a new tab.    |
| Workspace       | Workspace where Lens is created, like public or user-specific.          |
| Version         | Metadata version.                                                           |
| State           | Lens state such as Active or Deleted.                                   |
| Followers Count | Count of users who are following this Lens.                             |
| Last updated    | Date and time when the Lens was last updated.                           |
| Jobs            | Information about the jobs in the Lens.                                 |

#### **Details page**

In the Result or Overview pane, clicking on the name of the Lens opens the Lens Resource Details page, which includes:

<img src="/resources/lens/cataloging/detailed_page_overview.png" alt="Untitled(5)" style="max-width: 40rem; height: auto; border: 1px solid #000;">


| Attribute                 | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Resource Type             | Lens                                                                        |
| Meta Version              | Provides information on the latest Meta version. Click to see the version history and corresponding updates. |
| Updated                   | Provides last updated time                                                  |
| Follow                    | Gives the user an option to follow the Lens to receive updates and view its follower count. |
| Learn                     | Provides an option to learn more about this specific resource type          |
| Delete                    | Gives the user the option to delete the Lens (click on three dots to access this option). |
| Owner                     | Allows the user to edit the owner’s name                                    |
| Tier                      | Gives the user an option to add/edit the tier information                   |
| Domain                    | Allows the user to add a predefined domain name                             |
| Tags                      | Add/Remove tags/glossary terms/tag groups                                   |
| Request Tags Update (?)   | Request updates in tags and assign users to do it                          |
| Description               | Allows the user to edit the description                                     |
| Request Description Update (?) | Request updates in the description and assign users to do it            |
| Tasks                     | Option to view tasks created. In the side pane, the user will get the option to create a new task. |
| Conversations             | View conversations in the side pane. The user will get the option to start a new conversation by clicking on the ‘+’ sign. |

The subsequent tabs will provide you with more detailed information, as explained in the following sections.

**Details**

| Attribute           | Description                                                                |
|---------------------|----------------------------------------------------------------------------|
| Workspace           | Indicates the workspace within DataOS instance where the Lens is created  |
| Version             | Indicates the specific version or release of the DataOS Lens Resource     |
| State               | Represents the current state of the DataOS Lens Resource                  |
| Aggregate Status    | Consolidated status of the Lens Resource                                   |
| Compute             | Represents the compute resources associated with the Lens                 |
| Bundles             | The name of the bundle that is used to create the Lens                     |
| Builder State       | Represents the current state of the Lens builder                          |
| Runtime State       | Represents the current runtime state of the Lens                          |
| Lifecycle Event(s)  | Logs significant occurrences such as creation and deletion of the Lens    |

**Model**

The Model tab shows the lineage of the semantic model, displaying the tables it is derived from, along with the associated metrics.

**Permissions**

The Permissions tab shows user-specific access details, indicating whether a user has unrestricted access or if there are any restrictions on their permissions.

**Activity Feeds and Tasks**

This space compiles all activities, including tasks and conversations, providing users with a comprehensive overview.

**Runtime**

The Runtime tab shows details about the resource's operational instances, including name, type, workspace, and creation date, giving an overview of the Lens activity and deployment. Clicking on a Lens services run id will navigate you to the backend service of it.

**Manifest**

This section provides details about the manifest, a YAML configuration file that defines the setup of various DataOS Resources.

<aside class="callout">
To explore the input tables of the semantic model click on 'Explore Assets' button on Top.
</aside>


## Exploring the semantic model and Lens metadata via Data Product Hub

The Data Product Hub plays a key role in cataloging the semantic model of each Data Product. It captures detailed metadata, including the model's source, description, quality metrics, and relevant business context. 

1. The Data Product Hub provides a comprehensive view of data lineage in its ‘Overview’ tab. It tracks input datasets, the semantic model, output tables, and derived metrics, showing how tables contribute to specific metrics with visual connections.

    For instance, the image below illustrates how the source data, semantic model, output tables, and metrics like purchase_frequency are linked, offering a clear view of data flow and metric creation from the model.

    <img src="/resources/lens/cataloging/dph_lineage.png" alt="Untitled(5)" style="max-width: 40rem; height: auto; border: 1px solid #000;">


2. In the 'Semantic Model' tab, by default, the lineage of the tables used to create the semantic model and its downstream metric views is displayed. For users who want a deeper understanding, user's can view the full lineage, including the workflows used to derive the semantic model. Additionally, it stores model folder files, enabling developers to explore the model's creation and details.

    <img src="/resources/lens/cataloging/dph_sm_lineage.png" alt="Untitled(5)" style="max-width: 40rem; height: auto; border: 1px solid #000;">

3. The 'Metric' tab in the Data Product Hub shows detailed lineage for metrics, highlighting the tables that contributed to each one. For example, the lineage of the `cross_sell_opportunity_score` metric is displayed, showing its derivation from the purchase and product tables. Scrolling down reveals a detailed list of measures and dimensions.

    <img src="/resources/lens/cataloging/dph_metric_lineage.png" alt="Untitled(5)" style="max-width: 40rem; height: auto; border: 1px solid #000;">


4. The 'Quality' tab in the Data Product Hub catalogs the quality checks applied to both input and output datasets of the semantic model. These checks ensure data integrity by validating that the data meets predefined standards and accurately represents real-world values.

For example, an accuracy check on the `product_affinity_matrix` dataset ensures the average length of Category 1 exceeds a threshold of 4. As shown in the image below, the check passed with a 100% Service Level Objective (SLO), confirming data accuracy.

<img src="/resources/lens/cataloging/dph_quality_tab.png" alt="Untitled(5)" style="max-width: 40rem; height: auto; border: 1px solid #000;">

The Quality tab also tracks other checks such as Completeness Freshness etc., providing transparency into the data’s reliability for users.

