# Min-Max (Zonemap) Index

A **Min-Max (Zonemap) Index** is a type of index that an in-memory database automatically creates for each column in a table to optimize query performance. It is designed to quickly filter out blocks of data that do not need to be scanned during query execution, significantly speeding up certain types of queries, particularly those that involve range filtering or exact value lookups.

## How does it work?

- **Data Blocks:** When the in-memory database stores data in a table, it organizes the data into blocks. Each block contains a subset of the rows in the table.
- **Min and Max Values:** For each block, the in-memory database automatically calculates and stores the minimum and maximum values of each column within that block. This information is stored in the Min-Max (Zonemap) Index.
- **Query Filtering:** When a query is executed, the in-memory database uses the Min-Max (Zonemap) Index to quickly determine whether a block contains any relevant data for the query. If the query is looking for a value that falls outside the range defined by the min and max values of a block, that block can be skipped entirely.

## Example

Consider a table `sales` with a column `sale_date` that stores the date of each sale. The table is divided into several blocks of data.

- **Block 1:** Contains `sale_date` values from `2024-01-01` to `2024-01-31`.
- **Block 2:** Contains `sale_date` values from `2024-02-01` to `2024-02-28`.
- **Block 3:** Contains `sale_date` values from `2024-03-01` to `2024-03-31`.

If you run a query like:

```sql
SELECT * FROM sales WHERE sale_date = '2024-02-15';
```

1. The in-memory database will first check the MinMax (Zonemap) Index for the `sale_date` column.
2. It will see that `2024-02-15` falls within the range of Block 2 but not within the ranges of Block 1 or Block 3.
3. As a result, the in-memory database can skip scanning Block 1 and Block 3 entirely, focusing only on Block 2, which greatly reduces the amount of data that needs to be processed.

### **Benefits**

- **Performance Improvement:** By allowing the in-memory database to skip blocks of data that do not match the query criteria, Min-Max indexes significantly speed up query execution, particularly for large datasets.
- **Automatic Creation:** Min-Max indexes are automatically created and maintained by an in-memory database for every column, so no manual intervention is required. This provides performance benefits without requiring explicit index management.
- **Efficient Filtering:** They are particularly effective for range queries (e.g., `BETWEEN`, `<`, `>`) and equality queries (`=`) because they quickly eliminate irrelevant data blocks.

### **Comparison**

- **Not a Full Index:** Unlike traditional indexes (like B-trees or hash indexes), Min-Max indexes do not store pointers to individual rows. Instead, they summarize the data within each block, making them less precise but much faster for broad filtering.
- **Space Efficiency:** Min-Max indexes are lightweight and do not require significant additional storage, as they only store two values (min and max) for each block.