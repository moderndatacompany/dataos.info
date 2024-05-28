# How to use Iceberg metadata tables to extract insights in Lakehouse storage?

Merging Apache Iceberg metadata tables enables the extraction of enriched insights and enhances the efficiency of data management processes. Here's an exploration of how such integrations can be applied across various scenarios.

## Extract Information on All Files in a Given Snapshot

To confirm the accurate addition of records, observe storage growth in specific snapshots, and more, you can retrieve the metadata of all files within a snapshot with this SQL command:

```sql
SELECT file.*, entry.snapshot_id
FROM icebase.retail.city.entries AS entry
JOIN icebase.retail.city.files AS file
ON entry.data_file.file_path = file.file_path
WHERE entry.status = 1 AND entry.snapshot_id = <your_snapshot_id>;
```

## Obtain a Comprehensive Log of a Data File's History

For insights into the addition, deletion, and presence of a file throughout its lifecycle, including table operation states, the following SQL query can be employed. It also facilitates the identification of operations involving the file, along with details from entries and manifests tables for further context:

```sql
SELECT entry.snapshot_id, entry.sequence_number, entry.status, manifest.added_snapshot_id,
manifest.deleted_data_files_count, manifest.added_data_files_count
FROM icebase.retail.table.entries AS entry
JOIN catalog.table.manifests AS manifest
ON entry.snapshot_id = manifest.added_snapshot_id
WHERE entry.data_file.file_path = '<your_file_path>'
ORDER BY entry.sequence_number ASC;
```

## Monitor Table Evolution by Partition Across Snapshots

This query aids in understanding partition evolution over snapshots, tracking metrics such as file addition count and file size growth by partition:

```sql
SELECT entry.snapshot_id, file.partition, COUNT(*) AS files_added
FROM catalog.table.entries AS entry
JOIN catalog.entries.files AS file
ON entry.data_file.file_path = file.file_path
WHERE entry.status = 1
GROUP BY entry.snapshot_id, file.partition;
```

## Supervise Files Linked to a Specific Branch

For those utilizing table branching, this query helps in monitoring specific branches for storage and optimization purposes, fetching files from the current snapshot of a selected branch:

```sql
SELECT ref.name as branch_name, file.*
FROM catalog.table.refs AS ref
JOIN catalog.table.entries AS entry
ON ref.snapshot_id = entry.snapshot_id
JOIN catalog.table.files AS file
ON entry.data_file.file_path = file.file_path
WHERE ref.type = 'BRANCH' AND ref.name = '<your_branch_name>';
```

## Identify File Variations Between Two Table Branches

To determine the distinct files between two branches, the following query merges the results of two subqueries, showcasing unique files in both branches:

```sql
-- files in branch1 but not in branch2
SELECT 'branch1' as branch, file.*
FROM catalog.table.refs AS ref1
JOIN catalog.table.entries AS entry1
ON ref1.snapshot_id = entry1.snapshot_id
JOIN catalog.table.files AS file
ON entry1.data_file.file_path = file.file_path
WHERE ref1.type = 'BRANCH' AND ref1.name = 'branch1'
AND file.file_path NOT IN (
 SELECT file2.file_path
 FROM catalog.table.refs AS ref2
 JOIN catalog.table.entries AS entry2
ON ref2.snapshot_id = entry2.snapshot_id
JOIN catalog.table.files AS file2
ON entry2.data_file.file_path = file2.file_path
WHERE ref2.type = 'BRANCH' AND ref2.name = 'branch2'
)
UNION ALL
-- files in branch2 but not in branch1
SELECT 'branch2' as branch, file.*
FROM catalog.table.refs AS ref1
JOIN catalog.table.entries AS entry1
ON ref1.snapshot_id = entry1.snapshot_id
JOIN catalog.table.files AS file
ON entry1.data_file.file_path = file.file_path
WHERE ref1.type = 'BRANCH' AND ref1.name = 'branch2'
AND file.file_path NOT IN (
 SELECT file2.file_path
 FROM catalog.table.refs AS ref2
JOIN catalog.table.entries AS entry2
ON ref2.snapshot_id = entry2.snapshot_id
JOIN catalog.table.files AS file2
ON entry2.data_file.file_path = file2.file_path
WHERE ref2.type = 'BRANCH' AND ref2.name = 'branch1'
)
```

## Track Branch Storage Growth by Latest Snapshot

To manage storage costs efficiently, especially in branches with significant experimental data ingestion, this query provides insights into data volume added to the latest snapshot of each branch:

```sql
SELECT ref.name as branch_name, entry.snapshot_id, SUM(file.file_size_in_bytes) as
total_size_in_bytes
FROM catalog.table.refs AS ref
JOIN catalog.table.entries AS entry
ON ref.snapshot_id = entry.snapshot_id
JOIN catalog.table.files AS file
ON entry.data_file.file_path = file.file_path
WHERE ref.type = 'BRANCH'
GROUP BY ref.name, entry.snapshot_id
ORDER BY ref.name, entry.snapshot_id;
```