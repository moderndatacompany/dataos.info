# Depot

Depot in DataOS is a resource that simplifies the process of accessing data from different sources by abstracting away the complexities of protocols, credentials, and connection schemas. It acts as a bridge between DataOS and the data sources, allowing you to connect and access data from various types of storage systems such as object storage (e.g., Amazon S3, Azure Blob Storage), streaming sources (e.g., Pulsar), and databases (e.g., PostgreSQL, MySQL, BigQuery, NoSQL).

<style>
    blockquote {
        background-color: #F6F3F8;
    }
</style>

<blockquote style="color: black;">
The Depot serves as the registration mechanism for data locations within DataOS. Through the Depot Service, each source system is assigned a unique address, known as a Universal Data Link (UDL). With the UDL in hand, you can conveniently access and manipulate datasets within the source system without the need to re-enter credentials. The UDL follows the format:
</blockquote>

    

<center> `dataos://[depot]:[collection]/[dataset]` </center>

By leveraging the UDL, you gain direct access to datasets and can seamlessly perform various operations, such as data transformation, policy assignment, and more.

The specific composition of the UDL address depends on the source system being accessed. For example, in a Relational Database, the term "Schema" may be used instead of "Collection," and "Table" may replace "Dataset." Similarly, in a simple file storage system, "Collection" can correspond to "Folder," and "Dataset" can correspond to "File." The beauty of the Depot lies in its ability to provide uniformity, eliminating the need to worry about these differing nomenclatures. 

Once a depot is created, all members of your organization gain secure access to datasets within the associated source system. The depot not only facilitates data access but also assigns **default access policies** to ensure data security. Additionally, you have the flexibility to define and utilize custom Access Policies for the depot and Data Policies for specific datasets within the depot.

<aside style="background-color:#FAF3DD; padding:15px; border-radius:5px;">
🗣️  It is worth noting that the Depot provides 'access' to data, meaning that data is neither moved away from the source system nor duplicated. However, if the need arises, DataOS offers the capability to perform such tasks as well.
</aside>


## Depot Service

Depot Service is a DataOS service that manages the Depot resource.

- It provides users with a powerful and scalable API/JDBC-based query interface, enabling direct querying of stored data. The interface is backed by a dataframe-based SQL engine, allowing for efficient data retrieval and analysis. With the Depot Service, users can leverage the Minerva query engine, DataOS stacks, Lens, and other components of DataOS to interact with their data.
- The Depot Service also facilitates in-depth introspection of depots and their associated storage engines. Once a depot is created, users can obtain comprehensive information about the datasets contained within, including details such as dictionary, constraints, partition, and indexing. For a detailed understanding of this process, please refer to the [Scanner](./stacks/scanner.md) stack documentation.

To explore the full range of capabilities offered by the Depot Service, please visit the following page: [Depot Service](./depot/depot_service.md)

## Create Depot

Creating a depot in DataOS is a streamlined process facilitated by the use of YAML configuration files. To establish a depot, simply compose a YAML configuration file and apply it using the DataOS Command Line Interface (CLI). Please refer to the following documentation to know more:

[Create Depot](./depot/create_depot.md)

## Use Depot

Once a depot is created, you can leverage the Universal Data Links (UDLs) associated with it to access data without the need to physically move it. These UDLs play a crucial role in different components of DataOS. For instance, within the Flare stack, you can specify UDLs as the addresses of your input and output datasets.

Consider the following excerpt from a YAML file that represents a Flare workflow:

```yaml
# A section of the complete YAML file for a Flare workflow 
       inputs:                                               
         - name: customer_connect
           dataset: dataos://crmbq:demo/customer_profiles # Example of input UDL
       outputs:
         - name: output01
           depot: dataos://filebase:raw01 # Example of output UDL
```

In DataOS, Stacks serve as programming paradigms and extension points for runnable resources like Workflows and Services. While this may sound daunting, think of stacks as distinct approaches to interact with the system, enabling you to perform various actions in DataOS. We offer several Stacks that can be utilized within these primitives, such as Scanner for introspecting depots and Toolbox for managing Icebase DDL and DML. To delve deeper into the stacks and their functionalities, please visit the following [link.](./stacks.md).

### **Compatibility of Depots with Stacks**

Take a look at the table given below. It shows which of the different Depot Types are supported with which Stacks of DataOS.

<center>

| **Depot Type** | **Flare** | **Benthos** | **Minerva** | **Scanner** |
|---|---|---|---|---|
Amazon S3 | RW/PUSHDOWN^ | <span style="color:maroon">WIP</span> | <span style="color:green">READ</span> | <span style="color:blue">YES</span> |
Amazon Redshift	| RW/PUSHDOWN	| <span style="color:maroon">WIP</span>	| <span style="color:green">READ</span> | <span style="color:blue">YES</span> |
Apache Kafka	| RW	| <span style="color:green">READ</span>	| <span style="color:green">READ</span>	| <span style="color:blue">YES</span> |
Apache Pulsar	| RW/PUSHDOWN |	<span style="color:green">READ</span>	| <span style="color:green">READ</span>	| <span style="color:blue">YES</span> |
Azure Blob File Storage	| RW/PUSHDOWN^	| <span style="color:maroon">WIP</span>	| <span style="color:green">READ</span>	| <span style="color:blue">YES</span> |
BigQuery |	RW/PUSHDOWN	| <span style="color:maroon">WIP</span>	| <span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
Elasticsearch |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span>	| <span style="color:blue">YES</span> |
Google Cloud Storage |	RW/PUSHDOWN^ |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
JDBC |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
MSSQLSERVER |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
MySQL |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
Oracle |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
PostgreSQL |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
Redis |	WIP |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
Snowflake |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |

</center>

**RW**: read & write  |  **WIP**: work in progress  |  **PUSHDOWN**: Is pushdown of queries supported  |  **PUSHDOWN^**: Pushdown is supported only for Parquet format


In case you do not know what Pushdown is, do not worry. We got you! Learn it here: [Minerva](./cluster.md)

> Furthermore, using Depots significantly reduces the data breach risks and makes the life of the Infosec division of your enterprise easier.
> 

## Managed and Unmanaged Depots

In DataOS, we distinguish between managed and unmanaged depots based on their characteristics and supported functionalities.

### **Managed Depots**

A managed depot refers to a depot that utilizes internal storage options provided by DataOS. Currently, we offer three types of managed depots by default:

Within DataOS, we provide different types of depots that fall into the managed category. These depots leverage internal storage options to facilitate efficient data handling. Currently, we offer three default managed depots:

#### **Icebase**

Icebase is designed to store data suitable for OLAP processes. It qualifies as a managed depot because it offers built-in functionalities such as schema evolution, upsert commands, and time-travel capabilities for datasets. With Icebase, you can conveniently perform these actions directly through the DataOS CLI, eliminating the need for additional stacks like Flare or Data Toolbox. Moreover, queries executed on data stored in Icebase exhibit enhanced performance. For detailed information, refer to the Icebase [page.](./depot/icebase.md)

#### **Fastbase**

Fastbase is optimized for handling streaming data workloads. As a managed depot, it provides features such as creating and listing topics, which can be executed effortlessly using the DataOS CLI. To explore Fastbase further, consult the [link.](./depot/fastbase.md)

### **Unmanaged Depot**

For unmanaged depots, the available functionalities are dependent on the connected source system. DataOS acts as an intermediary, facilitating connection management, secrets, and credentials abstraction while relying on the capabilities offered by the underlying source system.


<aside style="background-color:#F8ECDF; padding:15px; border-radius:5px;">
📖 Best Practice: As part of best practices, it is recommended to regularly delete resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs

</aside>

## Depot Configuration Templates

To facilitate the creation of depots accessing commonly used data sources, we have compiled a collection of pre-defined YAML configuration files. These templates serve as a starting point, allowing you to quickly set up depots for popular data sources. You can access the list of these templates by visiting the following page:

[Depot Config Templates](./depot/depot_config_templates.md)
