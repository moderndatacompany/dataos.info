# Min-Max (Zonemap) Index

A **Min-Max (Zonemap) Index** is an automatically generated index that improves query performance in an in-memory database. It helps quickly filter out irrelevant blocks of data during query execution, particularly in queries involving range filtering or exact value lookups. This index is created for each column in a table to optimize data retrieval, reducing the need to scan unnecessary data.

## How does it work?

- **Data Blocks:** The in-memory database organizes table data into blocks. Each block holds a subset of rows from the table.
- **Min and Max Values:** For each block, the database calculates and stores the minimum and maximum values for every column within that block. These values are stored in the Min-Max (Zonemap) Index.
- **Query Filtering:** During query execution, the database references the Min-Max Index to determine whether a block contains relevant data. If the query seeks values outside the min and max range of a block, that block is skipped entirely, reducing the amount of data scanned.

## Example

Consider a table `sales` with a column `sale_date` that tracks when each sale occurred. The data is divided into several blocks:

- **Block 1:** `sale_date` values from `2024-01-01` to `2024-01-31`.
- **Block 2:** `sale_date` values from `2024-02-01` to `2024-02-28`.
- **Block 3:** `sale_date` values from `2024-03-01` to `2024-03-31`.

If a query is executed to find sales on a specific date:

```sql
SELECT * FROM sales WHERE sale_date = '2024-02-15';
```

1. The database checks the Min-Max Index for the `sale_date` column.
2. It determines that `2024-02-15` falls within the range of Block 2 but not Block 1 or Block 3.
3. As a result, the database skips scanning Block 1 and Block 3 and focuses only on Block 2, improving query efficiency.

## Benefits

- **Performance Improvement:** By skipping data blocks that fall outside the query criteria, Min-Max indexes reduce the volume of data that needs to be scanned, significantly speeding up query execution for large datasets.
- **Automatic Creation:** Min-Max indexes are automatically created and maintained for each column, so there is no need for manual intervention or explicit index management.
- **Efficient Filtering:** These indexes are especially useful for range queries (e.g., `BETWEEN`, `<`, `>`) and equality queries (`=`), as they efficiently eliminate irrelevant blocks.

## Comparison

- **Not a Full Index:** Unlike traditional indexes such as B-trees or hash indexes, Min-Max indexes do not store pointers to individual rows. Instead, they summarize data at the block level, making them faster for broad filtering but less precise for individual row lookups.
- **Space Efficiency:** Min-Max indexes are lightweight, requiring minimal storage since they only store two values (min and max) per block.