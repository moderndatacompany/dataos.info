# Metis Features

Metis includes the following set of features to address all your metadata needs to facilitate discovery, governance, observability, and collaboration.

## Asset Exploration

## Deep Understanding of Data Assets

Metis keeps an inventory of your organization’s data assets. It gives a complete overview of the organization’s data assets in one place. Metis UI lets you know more about your different kinds of assets: tables, topics, dashboards, workflows, ML models, services, users, teams, etc. You can view the latest updates, conversations, and tasks assigned related to them in the ‘All Activity’ section.
 
<center>

![Know about your assets](./Screen_Shot_2022-10-11_at_4.11.30_PM.png)

</center>

<figcaption align = "center">Know about your assets</figcaption>
<br>

For example, suppose you want to know more about the tables; you can further drill down to answer the questions such as who created/updated it, understand what each column means, what type of data it contains, what transformations are applied and which datasets participated in the transformations, etc. 

For all your data assets, you can manage ownership. 
 
<center>

![Quick glance at all the relevant metadata of a data asset](./Screen_Shot_2022-10-11_at_4.22.15_PM.png)

</center>

<figcaption align = "center">Quick glance at all the relevant metadata of a data asset</figcaption>
<br>

## Asset Discovery

## Search and Filter

Metis's Advanced Search experience surfaces results across data assets, ML models, pipelines, dashboards, and more. Metis not only helps you to find and access data using search criteria for your assets, but it also allows you to filter these assets based on tags, tag tier, owner, etc. You can also perform an advanced search based on columns, tags, schema, and ownership. Metis integrates ElasticSearch to enable users to perform extremely fast searches in petabytes of data.
 
<center>

![Advanced search and filters to find your data assets](./Screen_Shot_2022-09-21_at_5.52.52_PM.png)

</center>

<figcaption align = "center">Advanced search and filters to find your data assets</figcaption>
<br>

## Lineage Information

Quickly understand the end-to-end journey of data by tracing lineage across datasets. You can get the details of data flow across workflows and the datasets they produce. Additionally, you can learn about the other dependent datasets.
 
<center>

![Lineage for the dataset](./Screen_Shot_2023-01-30_at_8.07.20_PM.png)

</center>

<figcaption align = "center">Lineage for the dataset</figcaption>
<br>

If you want to get more information about the job run history, resource info, and topology for the dataset, refer to the DataOS lineage solution: 
[Hera](../../Hera/Hera.md).

## Validity and Reliability

It is important to ensure that you are working with trusted and appropriate data.Sometimes input data sources contain invalid data or incorrect data. You need to validate the captured data to determine whether the data meets business requirements. It is critical for generating valuable, correct insights. Before going ahead with the analysis, you can understand the quality of the dataset to ensure the correctness and completeness of the data. 
 
<center>

![Data profiling summary](./Screen_Shot_2022-10-11_at_4.32.26_PM.png)

</center>

<figcaption align = "center">Data profiling summary</figcaption>
<br>

On Metis UI, You can check the reliability of your datasets by viewing information about the business-specific validation rules applied, passed, or failed.
 
<center>

![Data quality checks](./Screen_Shot_2022-10-11_at_4.28.28_PM.png)

</center>

<figcaption align = "center">Data quality checks</figcaption>
<br>

## Collaboration

## Adding Descriptive Metadata

Metis allows you and your data team to attach additional information with data assets, such as you can provide detailed descriptions for datasets & columns, add owners and relevant glossary terms as tags, etc. Descriptive Metadata then helps in faster asset discovery and filtering. With ownership information, you can contact the right person in your organization to get help with datasets for more understanding or in case of any irregularities or discrepancies. Descriptions added to the complex/nested data types will help in understanding and discovering. Announcements keep the stakeholders/owners informed about the latest updates. 

Data team members can also add notes, comments, and tasks to data assets facilitating smooth collaboration among stakeholders. 

To learn more, refer to
[Metis UI](../Metis%20UI/Metis%20UI.md).

## Defining Tag Tiers

Tags are labels that you attach to your data assets and their attributes which help in asset discovery. Metis allows you to define tag categories to organize and group the created tags and facilitates advanced search.
 
<center>

![Tag categories](./Screen_Shot_2022-10-11_at_5.44.08_PM.png)

</center>

<figcaption align = "center">Tag categories</figcaption>
<br>

For example, to capture the business importance of data, a tag category ‘tag tier’ is used. When a data asset is tagged with a tier tag, say Gold, all the upstream assets used for producing it, will also be labeled with the same tag. This will help upstream data asset owners to understand the critical purpose of their data being used.
 
<center>

![Tag tiers for business criticality](./Screen_Shot_2022-09-21_at_5.23.39_PM.png)

</center>

<figcaption align = "center">Tag tiers for business criticality</figcaption>
<br>

To learn more, refer to
[Metis UI](../Metis%20UI/Metis%20UI.md).

## Adding Glossaries

Glossaries describe business definitions and context for data. With the help of glossaries, Metis enables you to establish a common business language for your data assets.    

Once you add a category for your glossary as per the business requirement, you can add terms and descriptions to it and declare their synonyms. All these terms are available to be added as tags for your assets in the drop-down.

This facilitates self-service analytics as business users do not depend on data teams to identify their relevant data assets.
 
<center>

![Adding business terms to your dataset](./Screen_Shot_2022-09-26_at_11.22.58_PM.png)

</center>

<figcaption align = "center">Adding business terms to your dataset</figcaption>
<br>

To learn more about how to create a Glossary, refer to
[Metis UI](../Metis%20UI/Metis%20UI.md).

## Activity Feeds

This feature enables you to view a summary of data change events whenever your data assets are modified. You can view these changes for all the data assets of your ownership or for specific assets you are interested in.  
 
<center>

![Keeping track of activities for your data assets](./Screen_Shot_2022-09-21_at_4.31.37_PM.png)

</center>

<figcaption align = "center">Keeping track of activities for your data assets</figcaption>
<br> 

With activity feeds, you can easily accomplish the following:

- Inform stakeholders about the important changes in data assets by adding announcements.
- Follow users, accounts, and conversations having mentions.
- Learn, in a timely manner, about updates regarding data assets related to you.
- Take quick actions on specific updates to fix things in time.

## Roles and Policies

You can build roles and policies at the user and team levels. It involves grouping users and entitlements, called roles, according to business functions or activities as teams. Metis enables you to create multi-level teams and assign owners and roles.

[Screenshot to be added for showing multi-level teams]

 You can create new roles and assign multiple policies for accessing metadata.
 
<center>

![Roles for metadata operations](./Screen_Shot_2022-10-11_at_4.06.07_PM.png)

</center>

<figcaption align = "center">Roles for metadata operations</figcaption>
<br>

Metis maps the role to a set of permissions (policies) for metadata operations — i.e., what the role is allowed to do, like updating descriptions, tags, owners, and adding glossary terms. 
 
<center>

![Picture](./Screen_Shot_2022-10-17_at_5.57.03_PM.png)

</center>


You can add multiple rules to a policy for allowing/denying entity-level operations. 
 
<center>

![Multiple rules for a policy](./Screen_Shot_2022-10-11_at_4.04.02_PM.png)

</center>

<figcaption align = "center">Multiple rules for a policy</figcaption>
<br>

Rules can be defined with a condition (or a combination of conditions). These conditions allow you to configure access effectively for various scenarios at the team and user levels. A rule in a policy is applicable when it meets the condition(s). 

To learn more about creating and managing teams, roles, policies, and rules, refer to
[Metis UI](../Metis%20UI/Metis%20UI.md).

## Notifications

Metis allows you to integrate with tools such as Slack, Webhook, Microsoft Teams, etc. that receive all the data changes happening in your organization through APIs. This will generate organization-specific notifications when a change is made to data assets. For example, send an email to the governance team when a "PII" tag is added to any data asset or you found a change in the schema which can impact other datasets.
 
<center>

![Configuring Webhook for event-driven notification](./Screen_Shot_2022-10-11_at_3.22.05_PM.png)

</center>

<figcaption align = "center">Configuring Webhook for event-driven notification</figcaption>
<br>

## Metadata Versioning

This feature records changes in metadata. Metis maintains the version history that can help in debugging process. You can view the version history to see if a recent change led to some inconsistencies in the data. 
 
<center>

![Tracking changes in metadata](./Screen_Shot_2022-10-11_at_3.26.08_PM.png)

</center>

<figcaption align = "center">Tracking changes in metadata</figcaption>
<br>

## Deleted Entity Metadata

Metis keeps rich metadata for the entities, about their structures, descriptions, tags, owners, importance, etc. This metadata is also about lineage, usage, and profiling data. When an entity is deleted, you may lose all this valuable information and may experience broken metadata. Metis supports soft deletion, so these entities are not removed from the database but marked as deleted. Metis lets you choose to show deleted entities’ metadata to understand dependencies and fix broken metadata issues. Once deleted, these entities will not surface in search and exploration. 
 
<center>

![Deleted data on Metis UI](./Screen_Shot_2023-02-01_at_4.40.11_PM.png)

</center>

<figcaption align = "center">Deleted data on Metis UI</figcaption>
<br>