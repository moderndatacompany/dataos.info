# Fine tuning a Lens model

Lens offers multiple options at different layers that dynamically improve the performance of your query. These caches can be used to accelerate long-running scans and aggregate and filter operations.

You can adopt different caching approaches to fine-tune the performance of your Lens:

## Physical layer: Flash

Flash caches the results of the SQL view used to create Lens logical tables. This minimizes the data that needs to be queried, improving data retrieval efficiency. It is especially useful for storing frequently accessed or queried logical tables. Instead of querying the source and scanning large datasets repeatedly, Flash allows queries to retrieve results from the cache, delivering faster performance. To determine if logical tables in Lens should be cached with Flash, consider the following:

- **SQL complexity:** If the SQL view involves complex operations like aggregates, joins, and subqueries, caching may help reduce query processing time.

- **Data volume:** Large datasets may benefit from caching as it reduces the amount of data that needs to be retrieved and processed.

- **Source optimization**: If the source system struggles to handle complex queries efficiently, using Flash can enhance performance by caching the table.

**Example:** A query mapping the logical table sales to the source table f_sales is complex and scans through unnecessary data. Caching its result in Flash will allow faster retrieval of relevant data.

## Activation layer: Buffer (Cache)

The activation layer exposes views through various APIs (REST, SQL, GraphQL) to support data applications. These applications may have specific performance needs, and each SQL API call retrieves data directly from the source, which can lead to increased latency.

Pre-buffering frequently accessed views or subsets of views can reduce the latency of SQL API calls by caching the data, improving response times for operational applications. To determine if buffering is necessary, consider the following:

- **Performance requirements:** If the application requires fast data access, buffering can improve performance.
- **Frequency of access:** Frequently accessed views are good candidates for buffering.
- **Data volume:** Views with large datasets may benefit from caching to reduce retrieval time.

**Example:** A SQL API call frequently retrieves revenue, wallet_share, and source data for specific time periods. Buffering this data improves the speed of retrieval for these queries.

While the semantic layer provides these functionalities to accelerate and optimize query performance at different stages of the data flow, it is essential to follow best practices in data modeling to ensure optimal performance, including efficient SQL writing, logical table materialization, and caching strategies.

