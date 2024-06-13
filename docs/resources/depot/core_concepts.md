Within DataOS, the hierarchical structure of a data source is represented as follows:

![Depot Hierarchy](/resources/depot/udl.png)
<center><i>Hierarchical Structure of a Data Source within DataOS</i></center>

The Depot serves as the registration of data locations to be made accessible to DataOS. Through the Depot Service, each source system is assigned a unique address, referred to as a **Uniform Data Link (UDL)**. The UDL grants convenient access and manipulation of data within the source system, eliminating the need for repetitive credential entry. The UDL follows this format:

<center><b><span style="font-size: 20px;"><code>dataos://[depot]:[collection]/[dataset]</code></span></b></center>


<aside class="callout">

🗣 Depot Service is a DataOS Service that manages the Depot Resource. It facilitates in-depth introspection of depots and their associated storage engines. Once a Depot is created, users can obtain comprehensive information about the datasets contained within, including details such as constraints, partition, indexing, etc.

</aside>

Leveraging the UDL enables access to datasets and seamless execution of various operations, including data transformation using various Clusters and [Policy](/resources/policy/) assignments.

Once this mapping is established, Depot Service automatically generates the Uniform Data Link (UDL) that can be used throughout DataOS to access the data. As a reminder, the UDL has the format: `dataos://[depot]:[collection]/[dataset]`.

For a simple file storage system, "Collection" can be analogous to "Folder," and "Dataset" can be equated to "File." The Depot's strength lies in its capacity to establish uniformity, eliminating concerns about varying source system terminologies.

Once a Depot is created, all members of an organization gain secure access to datasets within the associated source system. The Depot not only facilitates data access but also assigns **default** [Access Policies](/resources/policy/) to ensure data security. Moreover, users have the flexibility to define and utilize custom [Access Policies](/resources/policy/) for the depot and [Data Policies](/resources/policy/) for specific datasets within the Depot.

<aside class="callout">
 🗣️ Depot provides 'access' to data, meaning that data remains within the source system and is neither moved nor duplicated. However, DataOS offers multiple Stacks such as Flare, Benthos, etc. to perform ingestion, querying, syndication, and copying if the need arises.

</aside>

## **Supported Storage Architectures in DataOS**

DataOS Depots facilitate seamless connectivity with diverse storage systems while eliminating the need for data relocation. This resolves challenges pertaining to accessibility across heterogeneous data sources. However, the escalating intricacy of pipelines and the exponential growth of data pose potential issues, resulting in cumbersome, expensive, and unattainable storage solutions. In order to address this critical concern, DataOS introduces support for two distinct and specialized storage architectures - [Icebase](../resources/depot/icebase.md) Depot, the Unified Lakehouse designed for OLAP data, and [Fastbase](../resources/depot/fastbase.md) Depot, the Unified Streaming solution tailored for handling streaming data.

### **Icebase**

Icebase-type depots are designed to store data suitable for OLAP processes. It offers built-in functionalities such as [schema evolution](https://dataos.info/resources/depot/icebase/#schema-evolution), [upsert commands](https://dataos.info/resources/depot/icebase/#creating-and-getting-datasets), and [time-travel capabilities](https://dataos.info/resources/depot/icebase/#maintenance-snapshot-modelling-and-metadata-listing) for datasets. With Icebase, you can conveniently perform these actions directly through the DataOS CLI, eliminating the need for additional Stacks like [Flare](https://dataos.info/resources/stacks/flare/). Moreover, queries executed on data stored in Icebase exhibit enhanced performance. For detailed information, refer to the Icebase [page.](https://dataos.info/resources/depot/icebase/)

### **Fastbase**

Fastbase type-depots are optimized for handling streaming data workloads. It provides features such as [creating](https://dataos.info/resources/depot/fastbase/#create-dataset) and [listing topics](https://dataos.info/resources/depot/fastbase/#list-topics), which can be executed effortlessly using the DataOS CLI. To explore Fastbase further, consult the [link.](https://dataos.info/resources/depot/fastbase/)

## **Data Integration - Supported Connectors in DataOS**

The catalogue of data sources accessible by one or more components within DataOS is provided on the following page: [Supported Connectors in DataOS](https://dataos.info/resources/depot/list_of_connectors/)