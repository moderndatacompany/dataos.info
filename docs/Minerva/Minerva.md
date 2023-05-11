# Minerva

Allowing data to be consumed by anyone with granular access controls is the philosophy on which DataOS is designed. Minerva is our query engine that will enable you to access your data for business insights. Minerva query engine gives users the ability to query various datasets through a single platform. You can also run your analytical/exploration workloads with long-running queries. Minerva is an interactive query engine based on Trino.

Minerva makes it easy to analyze big data using SQL; you can query data across different databases without worrying about their configuration and data formats. It enables high-performance SQL access to various heterogeneous data sources, including traditional relational databases Oracle, PostgreSQL, MySQL, and Redshift, and other data sources such as Kafka and Cassandra.

Minerva enables you to run hundreds of memory, I/O, and CPU-intensive queries concurrently. For such query load, a single Minerva cluster is insufficient, and you must create multiple clusters which can scale to hundreds of worker nodes while efficiently utilizing cluster resources.

To learn more, refer to
[Architecture Overview](Minerva/Architecture%20Overview.md).

DataOS supports creating your own custom compute resources for varied querying needs. In an enterprise system, the demand for computing resources varies from time to time. In such a scenario, resources need to be provisioned to handle the increase/decrease in demand. To know more, refer to the next section.

## Minerva Clusters with Custom Compute

DataOS enables you to [create the Minerva clusters](Minerva/Architecture%20Overview/Creating%20Minerva%20Clusters.md) with optimized resources and tune them as per the query workload. With a properly tuned Minerva cluster, you can significantly improve the query execution and reduce the response time.

To learn more about configuring and tuning resources when you run complex queries with big data on Minerva, read 
[Cluster Tuning](Minerva/Cluster%20Tuning.md).

To create an [on-demand compute](Minerva/On-Demand%20Computing.md) type, you need to know which cluster needs to run on a specific kind of machine. You need to understand what kind of computing works best on various types of queries. To learn more, read 
[Cluster Configuration Scenarios](Minerva/Cluster%20Configuration%20Scenarios.md).

You can choose Minerva clusters from [Workbench](../Getting%20Started%20-%20DataOS%20Documentation/Data%20Management%20Capabilities/GUI/GUI%20Applications/Workbench.md) as per the compute requirement.

## Performance Tuning

The following information may help you to optimize Minerva query execution if your cluster is facing a specific performance problem. Ream more at
[Performance Tuning](Minerva/Performance%20Tuning.md).

## Connecting with Data Sources

Minerva query engine offers a large variety of connectors, for example, MySQL, PostgreSQL, Oracle, and Redshift. These properties in the DataOS setup file will mount the connector as the Catalog. This catalog contains schemas and references your data source via a connector.

Using these connectors, you can Perform most data analyses with data in place. Move only the data that needs to be operationalized. That means you can query and explore data from these data sources without bringing it to DataOS.

Minerva parses and analyzes the SQL query you pass in, creates an optimized query execution plan that includes the data sources, and then schedules worker nodes that are able to intelligently query the underlying databases. Read here to know about
[Connectors Configuration Page](Minerva/Connectors%20Configuration.md).

To know more about the connectors available to access data from different data sources, click [Trino](https://trino.io/docs/current/connector.html).

## Running Queries

There are multiple ways to interact with Minerva. [Minerva CLI](Minerva/Minerva%20Client.md) is a command line-based interactive interface for running your queries. For the UI-based query interface, you can use [Workbench](../Getting%20Started%20-%20DataOS%20Documentation/Data%20Management%20Capabilities/GUI/GUI%20Applications/Workbench.md), where you can run SQL queries on your data assets.

Apart from that, you can also use some of the popular BI analytics platforms to access data from DataOS, which is exposed through Minerva URL. To know more about integration with these tools, click on [Tableau](../Integration%20&%20Ingestion/Tableau.md) and [PowerBI](../Integration%20&%20Ingestion/Power%20BI.md). Read more at
[Minerva Client](Minerva/Minerva%20Client.md).

## Querying Data from Heterogeneous Data Sources

You can set up Minerva clusters that can process data from many different data sources even within a single query. This empowers you to query different databases with different schemas in the same SQL statement simultaneously.

You can even perform joins on the data from various systems that support storing structured and unstructured data. This capability reduces the complexity of integrating multiple systems.

To learn more, refer to
[Querying Heterogeneous Data Sources Page](Minerva/Querying%20Heterogeneous%20Data%20Sources.md).

## Optimizing Query Execution

To gain more reliability and cost savings while dealing with various analytical workloads in DataOS, here are some of the considerations which can help you accelerate your queries on Minerva. Read more on
[Query Optimization Page](Minerva/Query%20Optimization.md).

Minerva can push down the processing of queries, or parts of queries, into the connected data source for improved query performance. This means that a specific predicate, aggregation function, or other operation is passed through to the underlying database or storage system for processing.

## Governance Layer

Whenever a SQL query is fired from any sources (viz Workbench, Atlas, Minerva-CLI, Blender, JDBC, or Lens), it is directed to [Gateway Service](../Security/Heimdall%20Capabilities/Gateway%20Service.md), which reads and analyses the query and tables it contains before sending it to Minerva clusters for execution.  It provides the data policy decisions such as Masking and Filtering policies to be applied. The query is then forwarded to the Minerva cluster, where execution takes place.

During execution, Minerva directs it to the DataOS policy manager, [Heimdall](../Security/Heimdall%20Capabilities.md). Here the query is inspected for all the applicable policy restrictions. It is then directed to Minerva for policy implementation to ensure the availability of data to the right stakeholders protecting your organization's data assets from unauthorized access.

Minerva primarily executes the query for data access policy against the user tags, manages cluster access, and also reports to the users when the query is rejected or exceptions from clusters are encountered.

- [On-Demand Computing](Minerva/On-Demand%20Computing.md)

- [Configuration Properties](Minerva/Configuration%20Properties.md)

- [Create Minerva Clusters](Minerva/Create%20Minerva%20Clusters.md)