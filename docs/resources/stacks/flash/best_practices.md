This section involves best practices that help you optimize the Flash Service for efficient query processing and handle concurrent queries from multiple analysts without service restarts or performance issues.

## Adding Indexes

To optimize query performance, you can create indexes on the columns that you often use in your WHERE clauses or JOIN conditions. Indexes help speed up query performance by quickly locating data based on certain criteria. The in-memory database uses two main types of indexes as given below:

### **Min-Max Index (Zonemap)**

This index is automatically created for every column. Its primary purpose is to speed up queries that involve range searches, such as date ranges. By storing the minimum and maximum values for data blocks, the in-memory database can quickly skip over blocks that do not fall within the specified range. 

**Example**: Suppose you have a table of sales data with columns `id`, `amount`, and `sale_date`. You can run a query to find sales within a specific date range:

```sql
SELECT * FROM sales WHERE sale_date BETWEEN '2024-01-01' AND '2024-01-31';
```

The in-memory database can use the Min-Max index on the `sale_date` column to skip blocks of data that do not fall within the specified date range.

To learn more about the Min-Max Index, please [refer to this](/resources/stacks/flash/minmax/).

### **Adaptive Radix Tree (ART)**

Unlike the Min-Max index, ART indexes need to be explicitly defined by the user. They are designed to enhance performance for queries that involve exact matches or queries on columns with many unique values, as it allow for rapid lookup.

**Example**: If you have a table of users with a unique identifier `user_id`, the in-memory database automatically creates an ART index on this column. When you run a query to find a user by their ID, the in-memory database  can quickly locate the row using the ART index:

```sql
SELECT * FROM users WHERE user_id = 12345;
```

For instance, if you have a query to find a user by their unique ID, the in-memory database can use the ART index to quickly locate the user, ensuring fast and efficient query execution.

To learn more about the ART Index, please [refer to this](/resources/stacks/flash/art/).

### Creating and Dropping Indexes

You can create additional indexes on other columns to further enhance query performance. For example, to create an index on the `state` column in the `sales_360` table:

```sql
#Syntax
CREATE INDEX index_name ON table_name(column_name);

#Example
CREATE INDEX idx_state ON sales_360(state);
```

To drop an index, you can use the `DROP INDEX` statement:

```sql
# Syntax
DROP INDEX index_name;

#Example
DROP INDEX idx_state;
```

## Adding Configuration Parameters

To further optimize Flash for efficient read query processing and handle concurrent queries effectively, you can customize several key configuration parameters that can be defined in the INIT section of the YAML.

### **Threads and Worker Threads**

The `threads` and `worker_threads` settings determine the number of threads the in-memory database can use for executing queries. By default, these are set to the number of available CPU cores. 

<aside class="callout">
🗣 In the in-memory databases, <strong>threads</strong> are units of work that help speed up data processing and query execution by allowing multiple tasks to be performed simultaneously. <br>
<ul>
    <li><strong>Threads:</strong> Threads represent the upper limit on the number of threads the in-memory database will use for any operation (not just the execution of queries).</li>
    <li><strong>Worker Threads:</strong> Worker Threads are a subset of the total <code>threads</code> available and are dedicated to the computational tasks required to execute a query.</li>
</ul>
</aside>

- Increasing the number of threads beyond the number of physical cores can help improve throughput by allowing more concurrent operations.
- Manually adjusting these parameters, you can conduct performance tests to determine the optimal configuration for your specific use case. This experimentation can reveal insights into how the in-memory database performs under different thread counts, allowing you to find a sweet spot that balances performance and resource usage. However, this must be balanced with the risk of over-saturating the CPU, which could lead to contention and reduced performance.
- **Thread Contention:** Multiple threads competing for the same CPU resources can lead to thread contention, where threads spend time waiting for CPU access rather than executing tasks. This can further degrade performance, especially in CPU-bound workloads.
- **Context Switching:** With more threads than available memory, the operating system will engage in context switching, where it alternates between threads to give the appearance of parallel execution. However, context switching adds overhead and can reduce overall performance due to the CPU spending time switching between threads rather than executing them.
- **Potential Slowdown:** Instead of improving performance, increasing the number of threads beyond the number of available memory may slow down the execution of queries, as the overhead of managing too many threads outweighs the benefits of parallel execution.

### **External Threads**

The `external_threads` setting specifies the number of threads that can be used for operations involving external resources, such as reading data from remote files. 

- This setting is beneficial when the in-memory database needs to perform I/O operations that can be parallelized, such as fetching data from cloud storage or other databases.
- Increasing the number of external threads can improve performance in data-intensive applications.
- By default, it is set to 1.

### **Example**

```sql
#You can define these inside the ENV variable FLASH_CONFIG_INIT_SQL section of the
#service YAML
#Query to check the existing setting:

select * from duckdb_settings() where name in ('external_threads','memory_limit','threads','worker_threads');

#Queries to change these settings:

set threads = <number_of_threads>;
set external_threads = <number_of_threads>;
set worker_threads = <number_of_threads>;
```

## Using Persistent Volume

Larger-than-memory workloads in the in-memory databases are managed by using a technique called **spilling to disk**. When a dataset is too large to fit into the computer’s memory, the in-memory databases move some of the data to the hard drive or SSD temporarily. To handle this effectively, you can add a **persistent volume** to the Flash Service. A persistent volume acts as extra storage space that Flash uses to store parts of the dataset on disk, allowing it to work with larger datasets without running out of memory. This setup ensures Flash can process and manage large datasets smoothly, even when they exceed the available memory.

You can add the `persistentVolume` attribute in the Flash Service manifest file, as given below:

<aside class="callout">
🗣 Note: Before using the <code>persistentVolume</code> attribute in the Flash service, the Volume Resource must be created as shown below.

```yaml
name: duckdb-vol # Name of the Resource
version: v1beta # Manifest version of the Resource
type: volume # Type of Resource
tags: # Tags for categorizing the Resource
  - dataos:volume # Tags 
  - volume # Additional tags
description: Common attributes applicable to all DataOS Resources
owner: kanakgupta
layer: user
volume:
  size: 1Gi  #100Gi, 50Mi, 10Ti, 500Mi
  accessMode: ReadWriteMany  #ReadWriteOnce, ReadOnlyMany.
  type: temp
```

To know more about Volume Resource, please <a href="https://dataos.info/resources/volume/" target="_blank">refer to this</a>.

</aside>

```yaml
name: flash-test-old-10gb
version: v1
type: service
tags:
  - service
description: flash service
workspace: public
service:
  servicePort: 5433
  replicas: 1
  stack: flash+python:1.0
  # envs:
  #   FLASH_CONFIG_INIT_SQL: "set threads=5; set worker_threads=5"
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
      - create table if not exists d_customer as  (select * from customer)
      - create table if not exists f_sales  as (select * from numerous  )
      - create table if not exists d_product as (select * from product)
      - create table if not exists d_site as (select * from site)
      - select * from duckdb_settings() where name in ('external_threads','memory_limit','threads','worker_threads','checkpoint_threshold')

#join sales s2 on s.item_no = s2.item_no
```