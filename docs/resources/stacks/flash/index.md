---
title: Flash Stack
search:
  boost: 2
---

# Flash Stack

Flash is a Stack designed to manage and control query costs and performance within DataOS. It achieves this by caching datasets using an in-memory query processing layer.

The Flash Stack is orchestrated using a [Service](/resources/service/) Resource. Each instance of a Flash Service is purpose-driven and tailored to specific consumption patterns.

## Features of Flash

Flash provides various features to enhance data handling and query performance. The key capabilities include:

- **In-Memory Caching:** Utilizes an in-memory query processing layer to cache data for fast access, reducing query response times and speeding up data retrieval.
- **Optimized Query Performance:** Enhances query execution efficiency by leveraging in-memory storage to handle frequent data requests, improving overall system performance and reducing latency.
- **Cost Control:** Offers mechanisms to manage and control query costs through efficient caching and data management, minimizing the need for repeated data retrieval and computation, thereby reducing operational expenses.
- **Scalability:** Designed to handle increased loads by efficiently managing and serving cached data, supporting scalable data operations and high-traffic scenarios without compromising performance.
- **Efficient Data Management:** Optimizes data management processes through effective caching strategies, streamlining data access and reducing the workload on data sources.

## How to create a Flash Service?

Flash enables caching datasets within an in-memory layer, enhancing data consumption efficiency. To leverage this functionality, a Flash Service must be created, acting as the processing layer and working with data stored in Depots to optimize access and performance. For details on creating a Flash Service, [refer to this guide](/resources/stacks/flash/flash_service/).

## Configurations

Effective configuration of Flash requires understanding each attribute of the Flash Service manifest file. This section provides detailed descriptions to help in the creation of the Flash Service. For more information, [refer to this section](/resources/stacks/flash/configurations/).

## Supported data sources

Flash supports BigQuery, Snowflake, Redshift, and Depots with the Iceberg table format (DataOS Lakehouse, AWS S3, Azure ABFSS, Azure WASBS). This section includes steps for configuring the Flash Service for each of these Depots. For further details, [see this section](/resources/stacks/flash/data_sources/).

## Monitoring the cached dataset

The CPU and memory usage of the cached dataset in Flash can be monitored using the Inspection Web App. This tool provides details such as the number of users querying the cached data, the total number of queries executed, and specifics for each query, including user ID, execution time, and status (completed, in progress, or error encountered). For additional information, refer to the [documentation](/resources/stacks/flash/recipes/monitor/).

## Best Practices

This section outlines best practices for configuring and optimizing the Flash Service to efficiently handle query processing and support concurrent query execution. It covers key areas such as indexing strategies, configuration parameters, and the use of persistent volumes. To learn more about best practices, [refer to this section](/resources/stacks/flash/best_practices/).

## Do's and Dont's

Optimizing Flash for performance involves careful configuration of threads, memory limits, and external threads for I/O operations. It is essential to avoid over-indexing, oversaturating threads, and misconfiguring memory settings to prevent performance degradation. Tailoring settings to workload characteristics can yield significant performance gains. For the full list of best practices, see the detailed guide [here](/resources/stacks/flash/dos_and_donts/).

## Errors and Issues

### **Handling empty tables in Flash**

When attempting to create tables or views for datasets with zero records, Flash may encounter errors due to the absence of a schema. Flash relies on the data schema to generate tables/views, and empty tables prevent schema retrieval, causing failures. The recommended workaround involves inserting a dummy row into the table to generate the schema, which can be filtered out once real data is available. For more details on handling this issue, refer to the complete documentation [here](/resources/stacks/flash/handling_empty_tables/).


## Recipes

The following recipes assist in configuring the Flash Service effectively:

- [How to use cached datasets in Lens Models?](/resources/stacks/flash/recipes/lens/)
- [How to set up Talos for Flash?](/resources/stacks/flash/recipes/talos/)

