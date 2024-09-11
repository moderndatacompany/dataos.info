# Flash

Flash is a Stack designed to manage and control query costs and performance within DataOS. It achieves this by caching datasets using an in-memory database system.

The Flash Stack is orchestrated using a [Service](/resources/service/) Resource. Each instance of a Flash Service is purpose-driven and tailored to specific consumption patterns.


## Features of Flash

Flash offers various features to enhance data handling and query performance. Here are some of the key capabilities that make Flash a powerful tool for optimizing data operations:

- **In-Memory Caching**: Utilizes an in-memory database to cache data for fast access. Reduces query response times and speeds up data retrieval.
- **Optimized Query Performance**: Enhances query execution efficiency by leveraging in-memory storage to handle frequent data requests. Improves overall system performance and reduces latency in data access.
- **Cost Control**: Provides mechanisms to manage and control query costs through efficient caching and data management. Lowers operational costs by minimizing the need for repeated data retrieval and computation.
- **Scalability**: Designed to handle increased loads by efficiently managing and serving cached data. Supports scalable data operations and high-traffic scenarios without compromising performance.
- **Efficient Data Management**: Optimizes data management processes through effective caching strategies. Streamlines data access and reduces the workload.

## How to create a Flash Service?

Flash enables caching datasets within an in-memory layer, enhancing data consumption efficiency. To leverage this functionality, you must create a Flash service that acts as the compute layer, working with data stored in Depots to optimize access and performance. [Please refer to this to create a Flash Service.](/resources/stacks/flash/flash_service/)

## Configurations

Understanding each attribute of the manifest file is essential to configuring Flash effectively. This section provides detailed descriptions of the manifest file, helping you create the Flash Service efficiently. For detailed information, [please refer to this section](/resources/stacks/flash/configurations/).

## Supported Data Sources

Flash supports BigQuery, Snowflake, Redshift, and Iceberg types of Depots. This section involves steps to configure Flash service for each of these Depots. For more details, [please refer to this](/resources/stacks/flash/data_sources/).

## Best Practices

This section involves best practices for configuring and optimizing the Flash Service to handle query processing efficiently and support concurrent query execution. It covers key areas such as indexing strategies, configuration parameters, and the use of persistent volumes. To learn more about best practices, please [refer to this](/resources/stacks/flash/best_practices/).

## Recipes

Following are some recipes to help you to configure Flash Service effectively.

- [How to use cached datasets in Lens Models?](/resources/stacks/flash/recipes/lens/)
- [How to set up Talos for Flash?](/resources/stacks/flash/recipes/talos/)

