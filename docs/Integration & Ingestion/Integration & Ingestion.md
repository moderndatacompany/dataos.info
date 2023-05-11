# Integration & Ingestion

DataOS connects with all structured, semi-structured & unstructured data sources seamlessly at any volume & velocity across the enterprise. The open standards allow you to integrate with external tools & applications without any patching or fixing. 

We believe that the underlying structure of an enterprise’s Data Management infrastructure should automatically provide users with access to data rather than users having to hunt for it when the need arises. 

With this tenet in mind, DataOS provides you with variegated primitives and components to securely access all the data within your organization, irrespective of its type and format. Concurrently, you can also syndicate the data from source systems to BI tools and Web Applications. This way DataOS provides you with exhaustive Data Integration capabilities. 

## Depot

Depots are a core primitive of DataOS, which enable you to read and write data from & to various on-prem and cloud data sources without worrying about the underlying protocols, credentials and connection details. Refer here to create & use
[Depot](Integration%20&%20Ingestion/Depot.md).

To create a Depot addressing a source system, the source must satisfy several conditions. You can learn more about these constraints in [Depot Service](About%20DataOS/Primitives%20Resources/Depot%20Service%20%5BWIP%5D.md). For instance, a data source which is not a storage system, such as Web APIs, will not support the creation of a Depot. To connect to data from such sources, you can use Airbyte and Rclone.

> Depot connects you to the data source. In order to ingest or transform data - after the creation of a depot, you will have to use DataOS Primitives named Workflow or Service. Jump to the [Transformation](Transformation.md) section to learn about those.
> 

## Airbyte

Airbyte allows you to ingest data from pre-built as well as custom-made connectors, from high-volume databases to the long tail of API sources. You can directly access and start using Airbyte from DataOS GUI itself, refer to
[Airbyte](Integration%20&%20Ingestion/Airbyte.md).

## Rclone

Enable data movement into the cloud or between cloud storages with additional abilities like backup, restore, mirror, etc.
Impatience is never a good look. Information coming in soon!

## Scanner

Metadata retrieval or extraction is the process of requesting and retrieving metadata from a metadata endpoint. These metadata endpoints can be data sources, dashboards, messaging, and lineage services.

Metadata extraction is accomplished by the DataOS Scanner stack. You can write Scanner workflows in the form of a sequential YAML for a pull-based metadata extraction system built into DataOS for a wide variety of sources in your data stack.
To know the details, refer to
[Scanner](Integration%20&%20Ingestion/Scanner.md).

## Integrations with External Applications

While you can build your own apps on top of DataOS, it also integrates with many existing products. The reverse-ETL capabilities of DataOS allow you to activate your data as and when you need it and without learning to use new BI tools. To connect DataOS with some of the commonly used tools, you can use the links below:

- [Power BI](Integration%20&%20Ingestion/Power%20BI.md)

- [Tableau](Integration%20&%20Ingestion/Tableau.md)

- [SPSS Statistics](Integration%20&%20Ingestion/SPSS%20Statistics.md)

- [Hightouch](Integration%20&%20Ingestion/Hightouch.md)