# Metadata Tables in Lakehouse

Keep in mind that the metadata tables built into a DataOS Lakehouse storage are accessible using slightly different syntax depending on the query engine you are using, either [Minerva](/resources/cluster/#minerva) or [Themis](/resources/cluster/#themis). As Minerva uses TrinoSQL, while Themis uses SparkSQL, this page will provide syntaxes for both.

## `history` Metadata Table

The history table records the table’s evolution. Each of the four columns in this table provides unique insights into the table’s history.

| Field Name | Description | Data Type | Example Value |
| --- | --- | --- | --- |
| made_current_at | Represents the exact timestamp when the corresponding snapshot was made the current snapshot. This gives us a precise temporal marker for when changes to the table were committed. | timestamp with time zone | 2024-01-11 09:21:23.949 UTC |
| snapshot_id | This column serves as the unique identifier for each snapshot. This identifier enables us to track and reference specific snapshots within the table’s history. | bigint | 2399709541800220700 |
| parent_id | This column provides the unique ID of the parent snapshot of the current snapshot. This effectively maps out the lineage of each snapshot | bigint or NULL | 57819473453326215154 |
| is_current_ancestor | This column indicates whether a snapshot is an ancestor of the table’s current snapshot. This boolean value (true or false) helps identify snapshots that are part of the table’s state lineage and those invalidated from table rollbacks. | boolean | true |

You can use the history metadata table for data recovery and version control as well as to identify table rollbacks.
With a snapshot ID, you can restore your data and minimize potential data loss. In
case of any issues or errors, users can retrieve earlier versions of the data by referring
to the snapshot history. You can just query the table to get the snapshot prior to the
disaster you want to recover from. 

In the following code snippet, we run a query to get the snapshot_id from all snapshots prior to March 24th, 2024, which we can use to rollback the table to a snapshot before any incident that occurred on that date. 

```sql
SELECT snapshot_id
FROM icebase.retail."city$metadata_log_entries"
WHERE made_current_at < '2024-03-26 00:00:00'
ORDER BY made_current_at ASC
```

The data from this table can be used to identify a rollback of the table. This can be useful to identify when recovery actions have been taken when trying to build context for the table’s history. 

There are two signals to look for in the history table to identify a table rollback:

- Two or more snapshots have the same parent_id.
- Only one of those snapshots has is_current_ancestor set to true (true would mean it’s part of the current table history).

For example, based on the table information provided earlier, it can be inferred that there was a rollback in the table’s history at the given snapshot IDs (296410040247533565 and 2999875608062437345). This conclusion is drawn from the fact that snapshot 296410040247533565 is not a current ancestor and shares a parent with snapshot 2999875608062437345.
The following code snippet shows how to query all entries from the history metadata table:

```sql
--- Spark SQL for Themis Cluster
SELECT * FROM icebase.retail.city.history;
```

```sql
--- Trino for Minerva Cluster
SELECT * FROM icebase.retail."city$history"
```

## `metadata_log_entries` Metadata Table

The `metadata_log_entries` metadata table keeps track of the evolution of the table
by logging the metadata files generated during table updates. Each field within this
table holds significant information about the state of the table at a given point in time.

| Field Name | Description | Data Type | Example Value |
| --- | --- | --- | --- |
| timestamp | The timestamp field records the exact date and time when the metadata was updated. This timestamp serves as a temporal marker for the state of the table at that specific moment. | timestamp | 2023-07-28 10:43:57.487 |
| file | The file field indicates the location of the datafile that corresponds to that
particular metadata log entry. This location acts as a reference point to access the
actual data associated with the metadata entry. | string | …/v1.metadata.json |
| latest_snapshot_id | The latest_snapshot_id field provides the identifier of the most recent snapshot at
the time of the metadata update. It is a useful reference point for understanding the
state of the data when the metadata was updated. | int | 180260833656645300 |
| latest_schema_id | The latest_schema_id field contains the ID of the schema being used
when the metadata log entry was created. This gives context about the structure of the
data at the time of the metadata update. | int | 0 |
| latest_sequence_number | The latest_sequence_number field signifies the order of the metadata
updates. It is an incrementing count that helps track the sequence of metadata
changes over time. | int | 1 |

*Schema of the metadata-log-entries metadata table*

You can use the `metadata_log_entries` metadata table to find the latest snapshot with a previous schema. For example, maybe you made a change to the schema and now you want to go back to the previous schema. You’ll want to find the latest snapshot using that schema, which can be determined with a query that will rank the snapshots for each `schema_id` and then return only the top-ranked snapshot for each:

```sql
WITH Ranked_Entries AS (
 SELECT
 latest_snapshot_id,
 latest_schema_id,
 timestamp,
 ROW_NUMBER() OVER(PARTITION BY latest_schema_id ORDER BY timestamp
DESC) as row_num
 FROM
 icebase.retail.city.metadata_log_entries
 WHERE
 latest_schema_id IS NOT NULL
)
SELECT
 latest_snapshot_id,
 latest_schema_id,
 timestamp AS latest_timestamp
FROM
 Ranked_Entries
WHERE
 row_num = 1
ORDER BY
 latest_schema_id DESC;
```

The following code snippet will query all entries from this table:

```sql
--- Spark SQL for Themis Cluster
SELECT * FROM icebase.retail.city.metadata_log_entries;
```

```sql
--- Trino for Minerva Cluster
SELECT * FROM icebase.retail."city$metadata_log_entries"
```

## `snapshots` Metadata Table

The snapshots metadata table is essential for tracking dataset versions and histories. It maintains metadata about every snapshot for a given table, representing a consistent view of the dataset at a specific time. The details about each snapshot serve as a historical record of changes and portray the state of the dataset at the snapshot’s creation. The table includes several fields, each with a unique role.

| Field Name | Description | Data Type | Example Value |
| --- | --- | --- | --- |
| committed_at | The committed_at field signifies the precise timestamp when the snapshot was created, giving an indication of when the snapshot and its associated data state were committed. | timestamp | 2023-02-08 03:29:51.215 |
| snapshot_id | The snapshot_id field is a unique identifier for each snapshot. This field is crucial for distinguishing between the different snapshots and specific operations such as snapshot retrieval or deletion. | int | 57897183625154 |
| parent_id | The parent_id field links to the snapshot ID of the snapshot’s parent, providing context about the lineage of snapshots and allowing for the reconstruction of a historical sequence of snapshots. | int or null | NULL |
| operation | The operation field lists a string of the types of operations that occurred, such as
APPEND and OVERWRITE. | string | append
 |
| manifest_list | Further, the manifest_list field offers detailed insights into the files comprising the snapshot. It’s like a directory or inventory that keeps a record of all the datafiles associated with a given snapshot.  | string | …/table/metadata/snap-57897183999154-1.avro |
| summary | The summary field holds metrics about the snapshot, such as the number of added or deleted files, number of records, and other statistical data that provide a quick glance into the snapshot’s content. | map/struct | { added-records -> 400404, total-records -> 3000000,
added-data-files -> 300, total-data-files -> 500,
spark.app.id -> application_1520379268916_155055 } |

There are many possible ways to use the snapshots metadata table. One use case is to understand the pattern of data additions to the table. This could be useful in capacity planning or understanding data growth over time. Here is an SQL query that shows the total records added at each snapshot:

```sql
SELECT
 committed_at,
 snapshot_id,
 summary['added-records'] AS added_records
FROM
 catalog.table.snapshots;
```

Another use case for the snapshots metadata table is to monitor the types and frequency of operations performed on the table over time. This could be useful for understanding the workload and usage patterns of the table. Here is an SQL query that shows the count of each operation type over time:

```sql
SELECT
 operation,
 COUNT(*) AS operation_count,
 DATE(committed_at) AS date
FROM
 catalog.table.snapshots
GROUP BY
 operation,
 DATE(committed_at)
ORDER BY
 date;
```

The snapshots metadata table in Apache Iceberg serves as a valuable resource for managing dataset versions, supporting time-travel queries, and performing incremental processing, optimization, and replication. It enables users to effectively track changes, access historical states, and efficiently manage datasets.

The following SQL will allow you to query the snapshots table to see all of its data:

```sql
-- Spark SQL
SELECT * FROM my_catalog.table.snapshots;
```

```sql
-- Trino
SELECT * FROM "table$snapshots"
```

## `files` Metadata Table

The `files` metadata table showcases the current datafiles within a table and furnishes
detailed information about each of them, from their location and format to their
content and partitioning specifics.

*Schema of the files metadata table*

| Field Name | Description | Data Type | Example Value |
| --- | --- | --- | --- |
| content | The content field represents the type of content in the file, with a 0 signifying a datafile, 1 a position delete file, and 2 an equality delete file. | int | 0 |
| file_path | file_path gives the exact location of each file. This helps facilitate access to each data file when needed. | string | …/table/data/00000-3-8d6d60e8-d427-4809-bcf0-
f5d45a4aad96.parquet |
| file_format | The file_format field indicates the format of the data file, for instance, whether it’s a Parquet, Avro, or ORC file. | string | PARQUET |
| spec_id | The spec_id field corresponds to the partition spec ID that the file adheres to,
providing a reference to how the data is partitioned. | int | 0
 |
| partition | The partition field provides a representation of the datafile’s specific partition,
indicating how the data within the file is divided for optimized access and query
performance. | struct | {1999-01-01, 01} |
| record_count | The record_count field reports the number of records contained within each file,
giving a measure of the file’s data volume. | int | 1 |
| file_size_in_bytes | The file_size_in_bytes field provides the total size of the file in bytes. | int | 597 |
| columns_sizes | The column_sizes field furnishes the sizes of the individual columns. | map | [1 -> 90, 2 -> 62] |
| value_counts | The value_counts field provides the count of non-null values, in each column | map | [1 -> 1, 2 -> 1] |
| null_value_counts | The null_value_counts field provides the count of null values in each column. | map | [1 -> 0, 2 -> 0] |
| nan_value_counts | The nan_value_counts fields provide the count of NaN (Not a Number) values in each column. | map | [] |
| lower_bounds | The lower_bounds field holds the minimum value in each column, providing essential insights into the data range within each file. | map | [1 -> , 2 -> c] |
| upper_bounds | The upper_bounds field holds the maximum value in each column, providing essential insights into the data range within each file. | map | [1 -> , 2 -> c] |
| key_metadata | The key_metadata field contains implementation-specific metadata, if any exists. | binary | null |
| split_offsets | The split_offsets field provides the offsets at which the file is split into smaller segments for parallel processing. | list | [4] |
| equality_ids | The equality_ids field corresponds to the IDs relating to equality delete files, if any exist. | list | null |
| sort_order_id | The sort_order_id field corresponds to the IDs of the table’s sort order, if it has one. | int | null |

There are many possible use cases for the files metadata table, including determining whether a partition should be rewritten, identifying partitions that need data repair, finding the total size of a snapshot, and getting a list of files from a previous snapshot.

If a partition has many small files, it may be a good candidate for compaction to improve performance. The following query can help you break down each partition’s number of files and average file size to help identify partitions to rewrite:

```sql
SELECT
 partition,
 COUNT(*) AS num_files,
 AVG(file_size_in_bytes) AS avg_file_size
FROM
 catalog.table.files
GROUP BY
 partition
ORDER BY
 num_files DESC,
 avg_file_size ASC
```

Some fields probably shouldn’t have null values in your data. Using the files metadata table you can identify partitions or files that may have missing values in a much more lightweight operation than scanning the actual data. The following query returns the partition and filename of any files with null data in their third column:

```sql
SELECT
 partition, file_path
FROM
 catalog.table.files
WHERE
 null_value_counts['3'] > 0
GROUP BY
 partition
```

You can also use the files metadata table to sum all the file sizes to get a total size of
the snapshot:

```sql
SELECT sum(file_size_in_bytes) from catalog.table.files;
```

Using time travel you can get the list of files from a previous snapshot:

```sql
SELECT file_path, file_size_in_bytes
FROM catalog.table.files
VERSION AS OF <snapshot_id>;
```

The files metadata table in Apache Iceberg offers detailed information about individual data files, enabling granular data processing, schema management, lineage tracking, and data quality assurance. It is a valuable resource for various use cases, empowering users with enhanced data understanding and control. The following SQL allows you to pull up the data in the files table:

```sql
-- Spark SQL
SELECT * FROM my_catalog.table.files;
```

```sql
-- Trino
SELECT * FROM "table$files"
```

---