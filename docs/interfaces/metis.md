# Metis

Metis is a metadata manager, cataloging service, and database within DataOS to realize discoverability and observability capabilities for your enterprise data. With Metis, you gain comprehensive insights into both the technical and business context of your data. It goes beyond mere data storage and organization, providing a holistic view that enables you to understand the intricacies and relationships within your data ecosystem. Metis ensures that your organization’s vast collection of assets is easy to navigate and searchable.

**Metadata Manager**

The component that manages both technical and business metadata is the Metadata manager. This specialized component handles the change events related to metadata, and facilitates the retrieval of metadata. It ensures efficient access and utilization of critical information associated with the data. Some examples of the kind of information metadata reflects are author, date created, date modified, file size, and much more. 

> Technical metadata is information on the format and structure of the data, schemas, models, data lineage, data profile, or access permissions. Business metadata is about table and column definitions, data quality rules, and business glossary terms.
> 

**Cataloging Service**

Metis facilitates the cataloging and documentation of metadata. It captures essential information about data assets, such as data source, data type, data quality, data transformations, relationships, and other relevant attributes. This documentation helps users understand and interpret the data.

Cataloging involves the process of consolidating metadata from disparate source systems into a unified repository, with the goal of surfacing that information for the users of the system.

Cataloging empowers users to quickly locate and access relevant data, assess its quality and suitability for specific use cases, and leverage the insights derived from the consolidated metadata.

**Database**

Metadata is generated every time data is captured at a source, accessed by users, moved through a transformation, profiled, cleansed, or analyzed. Metis captures this metadata using Rest API connectors to a wide range of data services and stores it in the database, Metis DB. 

Metis keeps comprehensive details about datasets, jobs, tags, data relationships, transformations, and user interactions. 

<aside class="callout">
🗣 All metadata, whether about datasets, jobs, tags or any aspect is stored as separate metadata entities in the Metis DB. Additionally, the database also stores the interconnections and relationships between these entities. It also stores change events for metadata i.e. differences between the current and last version of an entity.

</aside>

## Metis Features

DataOS Metis as a whole assists you in discovering and exploring data assets across the organization. Apart from this, it allows you to govern, observe, and monitor the data systems fully and enables you to prevent and fix data problems in increasingly complex data scenarios. It enables business users to classify data sets and flag sensitive or confidential information so as to follow privacy regulations by applying DataOS policies.

To learn in detail about these features, click on the page below.

[Metis Features](metis/metis_features.md)

## Metis UI

Metis provides an interface (Metis UI) where you can effortlessly navigate through vast data repositories, locate relevant datasets, and efficiently explore the associated metadata. 

For more understanding of Metis UI and how to perform various functionalities such as exploring and discovering data assets, starting conversations for collaboration, and many more, check out the link below.

[Explore Metis UI](metis/explore_metis_ui.md)