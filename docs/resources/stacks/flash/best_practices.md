# Best Practices

This section outlines best practices for optimizing the Flash Service for efficient query processing and managing concurrent queries from multiple analysts without requiring service restarts or encountering performance issues.

## Adding indexes

To enhance query performance, indexes can be created on columns frequently used in `WHERE` clauses or `JOIN` conditions. Indexes enable faster data retrieval by quickly locating records based on specific criteria. The in-memory database supports two primary types of indexes:

### **Min-Max index (Zonemap)**

This index is automatically created for every column and is designed to speed up queries involving range searches, such as date ranges. By storing the minimum and maximum values for data blocks, the in-memory database can efficiently skip over data blocks that fall outside the specified range.

**Example:** For a table containing sales data with columns `id`, `amount`, and `sale_date`, the following query retrieves sales records within a specified date range:

```sql
SELECT * FROM sales WHERE sale_date BETWEEN '2024-01-01' AND '2024-01-31';
```

The Min-Max index on the `sale_date` column enables the in-memory database to bypass data blocks that do not fall within the specified date range.

For more information on the Min-Max Index, refer to [this section](/resources/stacks/flash/minmax/).

### **Adaptive Radix Tree (ART)**

ART indexes must be explicitly defined by the user. They are effective for queries involving exact matches or columns with many unique values, providing rapid lookups.

**Example:** For a table containing user records with a unique identifier `user_id`, the in-memory database automatically creates an ART index on this column. The following query finds a user by their ID:

```sql
SELECT * FROM users WHERE user_id = 12345;
```

The ART index allows the database to quickly locate the specified `user_id`, ensuring fast query execution.

For additional details on the ART Index, refer to [this section](/resources/stacks/flash/art/).

### **Creating and dropping indexes**

Additional indexes can be created on other columns to further improve query performance. Below are examples for creating and dropping indexes:

```sql
-- Syntax for creating an index:
CREATE INDEX index_name ON table_name(column_name);

-- Example:
CREATE INDEX idx_state ON sales_360(state);
```

To remove an index, use the `DROP INDEX` statement:

```sql
-- Syntax for dropping an index:
DROP INDEX index_name;

-- Example:
DROP INDEX idx_state;
```

## Adding configuration parameters

To optimize Flash for read-intensive queries and handle concurrent queries effectively, certain configuration parameters can be adjusted in the `INIT` section of the YAML configuration.

### **Threads and Worker threads**

The `threads` and `worker_threads` settings determine the number of threads the in-memory database uses for query execution. By default, these settings match the number of available CPU cores.

- **Threads:** Represents the maximum number of threads that the in-memory database will use for any operation.
- **Worker threads:** A subset of the total `threads`, dedicated specifically to computational tasks during query execution.

- Adjusting the number of threads beyond the physical cores may improve throughput by allowing more concurrent operations. However, it is critical to balance this adjustment to avoid over-saturating the CPU, which can lead to contention and degraded performance.
- **Thread contention:** Excessive threads competing for CPU resources may result in contention, causing delays as threads wait for CPU access.
- **Context switching:** Increasing threads beyond available memory can lead to frequent context switching, where the CPU alternates between threads. This overhead can reduce performance as time is spent managing threads rather than executing them.
- **Potential slowdown:** Overuse of threads may slow query execution if the management overhead outweighs the benefits of parallel processing.

### **External threads**

The `external_threads` parameter specifies the number of threads for operations involving external resources, such as reading from remote files. This setting is particularly useful for parallelizing I/O operations, such as data retrieval from cloud storage or external databases.

- Increasing the number of `external_threads` can boost performance in data-intensive applications.
- By default, `external_threads` is set to 1.

### **Example**

```sql
-- Define these in the ENV variable FLASH_CONFIG_INIT_SQL section of the service YAML.
-- Query to check existing settings:

SELECT * FROM duckdb_settings() WHERE name IN ('external_threads', 'memory_limit', 'threads', 'worker_threads');

-- Queries to adjust these settings:

SET threads = <number_of_threads>;
SET external_threads = <number_of_threads>;
SET worker_threads = <number_of_threads>;
```

## Using persistent volume

For workloads that exceed available memory, the in-memory databases use **spilling to disk**. This technique moves portions of data to disk when the dataset is too large for memory. Adding a **persistent volume** to the Flash Service enables effective management of such workloads. A persistent volume provides additional storage space for temporarily offloading data, allowing Flash to handle large datasets without exhausting memory resources.

The `persistentVolume` attribute can be added to the Flash Service manifest file as shown below:

<aside class="callout">
🗣 <b>Note:</b> Before using the `persistentVolume` attribute in the Flash service, a Volume Resource must be created.

```yaml
name: duckdb-vol  # Name of the Resource
version: v1beta  # Manifest version
type: volume  # Resource type
tags: 
  - dataos:volume 
  - volume 
description: Common attributes applicable to all DataOS Resources
owner: iamgroot
layer: user
volume:
  size: 1Gi  # Example: 100Gi, 50Mi, 10Ti, 500Mi
  accessMode: ReadWriteMany  # Options: ReadWriteOnce, ReadOnlyMany
  type: temp
```

For more details on the Volume Resource, please refer to [this documentation](https://dataos.info/resources/volume/).

</aside>

```yaml
name: flash-test-old-10gb
version: v1
type: service
tags:
  - service
description: Flash service
workspace: public
service:
  servicePort: 5433
  replicas: 1
  stack: flash+python:1.0
  persistentVolume:
    name: duckdb-vol
    directory: p_volume
  logLevel: debug
  compute: runnable-default
  resources:
    requests:
      cpu: 2
      memory: 1Gi
    limits:
      cpu: 2
      memory: 2Gi
  stackSpec:
    datasets:
      - address: dataos://icebase:flash/f_sales
        name: numerous

      - address: dataos://icebase:flash/product_data_master
        name: product

      - address: dataos://icebase:flash/site_check1
        name: site

      - address: dataos://icebase:flash/customer_data_master
        name: customer

    init:
      - CREATE TABLE IF NOT EXISTS d_customer AS (SELECT * FROM customer);
      - CREATE TABLE IF NOT EXISTS f_sales AS (SELECT * FROM numerous);
      - CREATE TABLE IF NOT EXISTS d_product AS (SELECT * FROM product);
      - CREATE TABLE IF NOT EXISTS d_site AS (SELECT * FROM site);
      - SELECT * FROM duckdb_settings() WHERE name IN ('external_threads', 'memory_limit', 'threads', 'worker_threads', 'checkpoint_threshold');
```