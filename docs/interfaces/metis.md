# Metis

Metis serves as a centralized hub for all types of metadata, offering a 360° view into every data product, covering a spectrum of data assets (ranging from tables to dashboards), and DataOS Resources such as Workflows, Services, Clusters, Policies, etc.

## **Unified Metadata Infrastructure**

Metis facilitates the cataloging and documentation of metadata for entities of your data ecosystem such as Products, Data Assets and DataOS Resources into a unified repository, aiming to offer a consolidated view. It also keeps updated information about the state of all the entities and their relationships.

Metadata is created as data goes through different stages, like when it's captured, used, moved through a transformation, checked, cleaned, or analyzed. Metis captures this metadata using Rest API connectors to a wide range of data services and stores it in the database, called Metis DB. 

It seamlessly combines the functionalities of a modern Data Catalog and an enterprise Resource Catalog, serving as a centralized repository for all products, data assets owned by the organization and DataOS resources deployed in the DataOS instance. Cataloging empowers users to swiftly locate and access pertinent data and Resources, enabling them to assess its quality and relevance for specific purposes. 

## Exploring Metadata on Metis UI

Metis UI is a collaborative interface for diverse data users to navigate through the data ecosystem in an enterprise. Metis UI helps users search, discover, understand, and trust **data products**, **data** **assets** (tables, pipelines, dashboards, etc.), and **DataOS Resources** (Workflows, Services, Stacks, etc.) that exist for the entire organization. Users can easily collaborate with other team members, inform them about the updates on these assets, observe the changes in the metadata through versions, and accomplish more.

![Metis UI](metis/metis.png)
<figcaption align = "center"> DataOS Metis App </figcaption>

The homepage of Metis UI showcases a comprehensive overview of activities related to your data entities. For detailed information about the metadata of these entities, refer to the following sections:

### **Data Products**

Metis acts as a catalog for Data Products, making the discovery of data products with all the necessary attributes documented. It offers detailed insights into the input, output & SLOs (Service Level Objectives) for every data product, along with all the governance policies & associated code, infrastructure resources used for creating it and more. Users can track the entire life cycle of data product creation.  A data consumer may use it to:

1. Identify data products by importance and criticality, such as Gold, Silver, etc. 
2. Understand quality aspects defined by Service Level Objectives (SLOs) to make informed decisions on selecting the appropriate data product for your needs.
3. Explore operational metadata for data products, such as data access rights, data creators, resources, purpose, source, and consumer-aligned outputs, etc.

You can explore metadata of Data Products by clicking [here](metis/metis_ui_products.md).
### **Data Assets**

Metis gathers metadata on your databases, dashboards, and messaging services by utilizing the Scanner stack.

For structured data sources, it captures schema details, including table/column names, their descriptions, constraints, and primary keys. it includes SLOs for the quality of assets, suggests sensitive tags, etc. In the context of messaging services, Metis stores information on topics, senders/recipients, and message content elements (such as message size and types like text, audio, or video). Likewise, for dashboard services, the metadata encompasses elements like dashboards, charts, owners, and more.

To know more about metadata attributes of Data Assets, click [here](metis/metis_ui_assets.md).

### **DataOS Resources**
Metis also collects metadata across your Workflows, Services, Clusters, Depots, etc., including their historical runtime and operations data, and saves it to the Metis DB to provide an aggregated view. 
It also grants access to historical and operational data about Resources, facilitating workload monitoring and troubleshooting, including a detailed exploration of pods and containers when necessary. This metadata helps in understanding how containers are orchestrated across various workloads, services, and clusters.

To explore metadata of DataOS Resources in detail, click [here](metis/metis_ui_resources.md).

<aside class="callout">
🗣 All metadata about datasets, jobs, tags, or any aspect is stored as separate metadata entities in the Metis DB. Additionally, the database also stores the interconnections and relationships between these entities. It also stores change events for metadata, i.e., differences between an entity's current and last version.

</aside>

## Understanding Metis Capabilities

Within a DataOS environment, Metis is a vital tool for discovering data products, exploring data assets and DataOS Resources, and improving the catalog experience for both business users and data developers. Metis additionally empowers users to add more business context to these entities. It allows users to govern, observe, and monitor the data systems fully and enables you to prevent and fix data problems in increasingly complex data scenarios. It also enables business users to classify data  and flag sensitive or confidential information so as to follow privacy regulations by applying DataOS policies.

To learn in detail about these features, click on the link below.

[Metis Key Features](metis/metis_features.md)

## Navigating Metis UI
To better understand Metis UI and how to perform various functionalities, click [here](metis/navigating_metis_ui_how_to_guide.md).












