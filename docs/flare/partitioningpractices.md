# Partitioning Practices

## Overview

Data partitioning is a very common technique by that data stored in a persistent store is segregated into sections for faster queries and easy management. Partitioning your data helps reduce query costs and improve performance by limiting the amount of data query engines such as Minerva, need to scan in order to return the results for a specific query. Since it limits the volume of data scanned, dramatically accelerating queries.

Partitioning is a way to make queries faster by grouping similar rows together when writing.

This article will cover the  data partitioning  practices you need to know in order to optimize your analytics infrastructure for performance and to improve the storage of the dataset within DataOS. 
Data access operations on each partition take place over a smaller volume of data. Provided that the data is partitioned in a suitable way, this is much more efficient. Operations that affect more than one partition can execute in parallel. 


Data is commonly partitioned by timestamp – which could mean by hour, by minute or by day – and the size of the partition should depend on the type of query we intend to run. If most of our queries require data from the last 6 hours, we might want to use hourly partitioning rather than daily in order to scan less data.

We will see how to achieve partitioning with some of the existing technologies for large-scale data processing:

## Designing partitions

Data can be partitioned in different ways: horizontally, vertically, or functionally. The strategy you choose depends on the reason for partitioning the data, and the requirements of the applications and services that will access the data.

For an enterprise wide Data Lake, data partitioning is an important aspect that needs serious thought and consideration.
The three typical strategies for partitioning data are:

### Horizontal partitioning 

In this strategy, each partition holds a specific subset of the data, such as all the orders for a specific set of customers in an ecommerce application.
In this example, product inventory data is divided into pertitions based on the product key. Each partition holds the data for a contiguous range of partition keys (A-G and H-Z), organized alphabetically.


### Vertical partitioning

In this strategy each partition holds a subset of the fields for items in the data store. The fields are divided according to their pattern of use, such as placing the frequently accessed fields in one vertical partition and the less frequently accessed fields in another.

The most common use for vertical partitioning is to reduce the I/O and performance costs associated with fetching the items that are accessed most frequently. Figure 2 shows an overview of an example of vertical partitioning, where different properties for each data item are held in different partitions; the name, description, and price information for products are accessed more frequently than the volume in stock or the last ordered date.

**Name** | **Description** | **Price**
-------- | -------- | -------- |

**Volume in Stock** | **Last ordered Date**
-------- | -------- | 
In this example, the application regularly queries the product name, description, and price together when displaying the details of products to customers. The stock level and date when the product was last ordered from the manufacturer are held in a separate partition because these two items are commonly used together. This partitioning scheme has the added advantage that the relatively slow-moving data (product name, description, and price) is separated from the more dynamic data (stock level and last ordered date). 

Using this partitioning strategy, you can store sensitive (for example credit card )and other data on separate partition to maximize the security of sensitive data. 

### Functional partitioning

In this strategy data is aggregated according to distinct business area or service in the application. For example, an ecommerce system that implements separate business functions for invoicing and managing product inventory might store invoice data in one partition and product inventory data in another.

It’s important to note that the three strategies described here can be combined. They are not mutually exclusive and you should consider them all when you design a partitioning scheme. For example, you might divide data into shards and then use vertical partitioning to further subdivide the data in each shard. Similarly, the data in a functional partition may be split into shards (which may also be vertically partitioned).

You must evaluate and balance when designing a partitioning scheme that meets the overall data processing performance targets for your system.

## Good practices

The most important factor when implementing this partitioning strategy is the choice of partitioning key. It can be difficult to change the key after the system is in operation. The key must ensure that data is partitioned so that the workload is as even as possible across the partitions. 

The partition key you choose should minimize any future requirements to split large partition into smaller pieces, coalesce small partitions into larger partitions, or change the schema that describes the data stored in a set of partitions. These operations can be very time consuming.

## Designing partitions for scalability

It is vital to consider size and workload for each partition and balance them so that data is distributed to achieve maximum scalability. However, you must also partition the data so that it does not exceed the scaling limits of a single partition store.

Follow these steps when designing the partitions for scalability:

Analyze the application to understand the data access patterns, such as size of the result set returned by each query, the frequency of access, the inherent latency, and the server-side compute processing requirements. In many cases, a few major entities will demand most of the processing resources.
Based on the analysis, determine the current and future scalability targets such as data size and workload, and distribute the data across the partitions to meet the scalability target. In the horizontal partitioning strategy, choosing the appropriate shard key is important to make sure distribution is even. For more information see the Sharding pattern.
Make sure that the resources available to each partition are sufficient to handle the scalability requirements in terms of data size and throughput. For example, the node hosting a partition might impose a hard limit on the amount of storage space, processing power, or network bandwidth that it provides. If the data storage and processing requirements are likely to exceed these limits it may be necessary to refine your partitioning strategy or split data out further. For example, one scalability approach might be to separate logging data from the core application features by using separate data stores to prevent the total data storage requirements exceeding the scaling limit of the node. If the total number of data stores exceeds the node limit, it may be necessary to use separate storage nodes.
Monitor the system under use to verify that the data is distributed as expected and that the partitions can handle the load imposed on them. It could be possible that the usage does not match that anticipated by the analysis it may be possible to rebalance the partitions. Failing that, it may be necessary to redesign some parts of the system to gain the balance that is required.

## Designing partitions for query performance
When designing and implementing partitions, consider the following factors that affect :
Query performance can often be boosted by using smaller data sets and parallel query execution. Each partition should contain a small proportion of the entire data set, and this reduction in volume can improve the performance of queries. 
Follow these steps when designing the partitions for query performance:

 
Examine the business requirements to determine critical queries that must always perform quickly.
Monitor the system to identify any queries that perform slowly.
Establish which queries are performed most frequently. 


Design the partition key in a way that the application can easily find the partition if you are implementing horizontal partitioning. This prevents the query needing to scan through every partition.

The selection of partition key and row key values should be driven by the way in which the data is accessed. You should choose a partition key/row key combination that supports the majority of your queries.

The most efficient queries will retrieve data by specifying the partition key and the row key. Queries that specify a partition key  can be satisfied by scanning a single partition;  Queries that don't at least specify the partition key may require storage to scan every partition for your data.

Unfortunately, it is hard to decide for a silver bullet partitioning strategy, as future jobs might need to query the data in wildly different ways. Most probably, the engineering team maintaining the Data Lake might have to revisit their data partitioning strategies often.


## Partitioning in Iceberg

What does Iceberg do differently?
Other tables formats like Hive support partitioning, but Iceberg supports hidden partitioning.

Iceberg handles the tedious and error-prone task of producing partition values for rows in a table.
Iceberg avoids reading unnecessary partitions automatically. Consumers don’t need to know how the table is partitioned and add extra filters to their queries.
Iceberg partition layouts can evolve as needed.

Apache Iceberg is a relatively new, open source table format for storing petabyte-scale data sets. Iceberg fits easily into the existing big data ecosystem and currently has integration with Spark and Presto execution engines. Using a host of metadata kept on each table, Iceberg provides functions that are not traditionally available with other table formats. This includes schema evolution, partition evolution, and table version rollback — all possible without the need for costly table rewrites or table migration.

Iceberg handles all the details of partitioning and querying, and keeps track of the relationship between a column value and its partition without requiring additional columns.

Iceberg can partition timestamps by year, month, day, and hour granularity. It can also use a categorical column, like level in this logs example, to store rows together and speed up queries.

Iceberg produces partition values by taking a column value and optionally transforming it. Iceberg is responsible for converting event_time into event_date, and keeps track of the relationship.

Because Iceberg doesn’t require user-maintained partition columns, it can hide partitioning. Partition values are produced correctly every time and always used to speed up queries, when possible. Producers and consumers wouldn’t even see event_date.

Most importantly, queries no longer depend on a table’s physical layout. With a separation between physical and logical, Iceberg tables can evolve partition schemes over time as data volume changes. Misconfigured tables can be fixed without an expensive migration.

### Partition transform

### Partition evolution