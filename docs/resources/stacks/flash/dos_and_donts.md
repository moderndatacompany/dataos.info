# Do's and Dont's for Flash Configuration

To maximize the performance of Flash services, it is crucial to follow best practices regarding configuration, indexing, memory management, and thread optimization. This guide outlines key actions to take and avoid when working with Flash.

## Do’s:

### **1. Optimize threads for performance**
- **DO** adjust the `threads` and `worker_threads` parameters based on the number of available CPU cores and workload requirements. Conduct performance testing to determine the optimal thread configuration.
- **DO** balance the number of threads carefully to avoid oversaturating CPU resources. Performance testing will help you find the right balance between performance and resource utilization.

### **2. Set memory limits appropriately**
- **DO** configure memory limits to ensure that Flash handles large datasets and concurrent queries without running into out-of-memory (OOM) errors. Make sure sufficient memory is allocated to manage both query execution and caching.

### **3. Adjust external threads for I/O operations**
- **DO** increase the `external_threads` setting for queries involving external data sources (e.g., cloud storage or remote files) to improve performance for I/O-bound workloads.

### **4. Use persistent volumes for larger-than-memory workloads**
- **DO** configure persistent volumes for handling datasets that exceed available memory. This enables efficient disk-based storage for DuckDB, ensuring Flash can handle large datasets by spilling to disk when necessary.

### **5. Test different query configurations**
- **DO** experiment with various query patterns, indexing strategies, and configuration settings to identify the most efficient approach for your workload. Fine-tuning these elements based on workload characteristics can lead to significant performance improvements.

## Don’ts:

### **1. Don’t use Flash to model data**
- **DON’T** use Flash as a data modeling tool. Flash is designed to accelerate query performance, not to function as a database. Load data into Flash using simple `SELECT *` queries and use Lens for modeling the data based on your specific use case.

### **2. Avoid over-indexing**
- **DON’T** create Adaptive Radix Tree (ART) indexes unnecessarily on columns with low selectivity or columns that are infrequently queried. Over-indexing can slow down insert and update operations.
- **DON’T** create indexes on columns that already benefit from zonemap indexing unless there is a clear need for additional ART indexes.

### **3. Avoid oversaturating threads**
- **DON’T** configure `threads` and `worker_threads` to values far exceeding the number of available CPU cores. Excess threads can lead to contention and context switching, reducing overall system performance.
- **DON’T** over-allocate threads in multi-user environments without understanding the potential impact on performance, particularly under heavy workloads.

### **4. Don’t ignore thread contention**
- **DON’T** increase the number of threads without monitoring CPU load and contention, especially for CPU-intensive tasks. Excessive threading can result in diminishing returns or even degrade performance.

### **5. Avoid misconfiguring memory settings**
- **DON’T** allocate insufficient memory to the Flash service. This can lead to performance bottlenecks, frequent out-of-memory errors, and increased query latency.

### **6. Avoid using non-selective columns for ART indexing**
- **DON’T** use ART indexes on columns with low cardinality or those that do not significantly benefit from selective querying. Such indexes provide minimal performance improvement and may negatively impact overall performance.

### **7. Don’t overlook I/O optimization**
- **DON’T** neglect adjusting the `external_threads` setting when handling I/O-heavy queries. Inadequate configuration can cause bottlenecks when retrieving data from external sources.

### **8. Don’t ignore query patterns**
- **DON’T** assume that default indexing and configuration settings will work for all use cases. Tailor the configuration and indexing strategy based on the specific query patterns and the characteristics of your dataset to achieve optimal performance.