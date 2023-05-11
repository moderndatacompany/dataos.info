# Metis

Metis is a metadata manager, cataloging service, and database within the DataOS environment to realize discoverability and observability capabilities for your enterprise data. It conveys to you the technical and business context for your data by keeping metadata about it. 

## Metadata Manager

Metadata is essentially data about data. The component that manages Metadata is the Metadata manager. Some examples of what kind of information Metadata reflects are author, date created, date modified, file size, and much more. 

> Technical Metadata is information on the format and structure of the data, schemas, models, data lineage, data profile, or access permissions. Business Metadata is about table and column definitions, data quality rules, and business glossary terms.
> 

## Cataloging Service

Cataloging is bringing metadata from different source systems into one place and trying to create value out of it. In the big data landscape, the kind of data that is present in different source systems, columns within that data, and even the value of those columns, all this information is termed as data catalogs. 

## Database

Metadata is generated every time data is captured at a source, accessed by users, moved through a transformation, profiled, cleansed, and analyzed. Metis captures this metadata using Rest APIs supporting connectors to a wide range of data services and stores it in the database. Metis bears detailed information about every dataset, job, tag, the relation of data, transformations, and even user interactions and helps unlock the value of your data by improving that data’s discoverability and usability. 

> Metis ensures that your organization’s vast collection of assets is easy to navigate and searchable.


Metis provides an interface (Metis UI) where you can explore all your data assets and updates related to them. Data teams can access this information on Metis UI and use it in strategic and operational decision-making.


> 🗣 As it holds all the metadata-related information about the entire data, it is fondly called the Goddess of knowledge.


## Metis Features

DataOS Metis as a whole assists you in discovering and exploring data assets across the organization. Apart from this, it allows you to observe and monitor the data systems fully and enables you to prevent and fix data problems in increasingly complex data scenarios. Metadata management is a critical element in Data Governance. It enables business users to classify data sets and flag sensitive or confidential information so as to follow privacy regulations by applying DataOS policies.

To learn in detail about these features, refer to
[Metis Features](./Metis%20Features/Metis%20Features.md).

## How Metis Works

The metadata ingestion framework pulls metadata from various sources, processes it, and sends it to the Metis API Server The Metis UI represents a snapshot of this metadata and publishes the same in a catalog form. 

> 🗣 DataOS’s composable architecture enables you to run any catalog service, be it DataOS-native or external, on top of the Metis API.

To know more about how Metis performs metadata management to accomplish all the functionality mentioned in the previous section, refer to
[Architecture](./Architecture/Architecture.md).

For more understanding about Metis UI and how to perform various functionalities such as adding a glossary, starting conversations for collaboration, and many more, refer to
[Metis UI](./Metis%20UI/Metis%20UI.md).