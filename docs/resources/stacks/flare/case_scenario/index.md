# Flare Job Case Scenarios in DataOS

## Batch Jobs

Batch jobs recompute all affected datasets during each run, ensuring full refresh and deterministic outcomes. They typically involve reading data from source depots, applying transformations, and writing to target depots.

For example Workflows, see the [batch job case scenario](/resources/stacks/flare/case_scenario/batch_jobs/).

---

## Stream Jobs

Stream jobs enable near real-time processing by ingesting data in continuous micro-batches. These jobs are suitable for time-sensitive use cases such as event tracking, system monitoring, and IoT data analysis.

Detailed configuration is available in the [streaming job case scenario](/resources/stacks/flare/case_scenario/streaming_jobs/).

---

## Incremental Jobs

Incremental jobs process only the rows or files that have changed since the last execution. This reduces compute cost and latency, making them ideal for frequently updated datasets.

Learn more in the [incremental job case scenario](/resources/stacks/flare/case_scenario/incremental_jobs/).

---

## Data Transformation Use Cases

Flare supports several advanced data transformation patterns:

* Perform versioned operations using [Iceberg branch read/write](/resources/stacks/flare/case_scenario/iceberg_branch_read_write/).
* Rerun historical data pipelines with [data replay](/resources/stacks/flare/case_scenario/data_replay/).
* Enable parallel job writes using [concurrent writes](/resources/stacks/flare/case_scenario/concurrent_writes/).
* Access data during execution with [query dataset for job in progress](/resources/stacks/flare/case_scenario/query_dataset_for_job_in_progress/).
* Apply conditional upserts using [merge into functionality](/resources/stacks/flare/case_scenario/merge_into_functionality/).

---

## Job Performance and Optimization

Flare jobs can be tuned to enhance execution efficiency and reduce resource usage. Techniques include optimizing transformation logic, adjusting compute configurations, and minimizing I/O.

Refer to [job optimization by tuning](/resources/stacks/flare/case_scenario/job_optimization_by_tuning/) for implementation guidance.

---

## Metadata and Data Management

DataOS supports metadata management to improve discoverability, governance, and reusability:

* Tag columns for semantic classification using [column tagging](/resources/stacks/flare/case_scenario/column_tagging/).
* Distribute datasets across environments with [data syndication](/resources/stacks/flare/case_scenario/syndication/).

---

## Iceberg Table Optimization

Efficient handling of data and metadata in Iceberg tables is critical to maintaining performance at scale. Over time, small files and redundant metadata can degrade query efficiency.

### **Compaction**

- Reduce the number of small files to improve scan performance using [data file compaction](/resources/stacks/flare/case_scenario/rewrite_dataset/).
- Manage metadata overhead with [manifest rewrite](/resources/stacks/flare/case_scenario/rewrite_manifest_files/).

### **Partitioning**

- Improve query efficiency through structured data organization with [partitioning](/resources/stacks/flare/case_scenario/partitioning/) 
- It also helps in improving query efficiency through schema evolution via [partition evolution](/resources/stacks/flare/case_scenario/partition_evolution/).

### **Bucketing and Caching**

- Enhance join and aggregation performance with [bucketing](/resources/stacks/flare/case_scenario/bucketing/).
- Speed up repeated reads using [caching](/resources/stacks/flare/case_scenario/caching/).

---

## Data Lifecycle and Maintenance

Maintaining Iceberg datasets involves regular cleanup and space optimization tasks. These actions are supported in DataOS-managed depots (Lakehouse only):

* Remove specific records using [delete from dataset](/resources/stacks/flare/case_scenario/delete_from_dataset/).
* Clean up unused metadata with [expire snapshots](/resources/stacks/flare/case_scenario/expire_snapshots/).
* Reclaim storage by deleting untracked files via [remove orphans](/resources/stacks/flare/case_scenario/remove_orphans/).

