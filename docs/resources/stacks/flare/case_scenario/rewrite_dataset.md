# Rewrite Dataset

DataOS managed depot, Lakehouse built on top of Iceberg format can compact data files in parallel using Flare’s `rewrite_dataset` [action](/resources/stacks/flare/configurations/#rewrite_dataset). This will combine small files into larger files to reduce metadata overhead and runtime file open costs.

!!! tip

    It is recommended to use the Flare 5.0 for `rewrite-dataset` action job.

## Attribute configuration

| Attributes     | Type   | Description |
|---------------|--------|-------------|
| `strategy`      | string | Name of the compaction strategy. Supported values: `binpack` (default) or `sort`. |
| `sort_order`    | string | Defines sort order. For Z-ordering, use: `zorder(col1,col2)`. For regular sorting, use: `ColumnName SortDirection NullOrder` (e.g., `col1 ASC NULLS LAST`). Defaults to the table's current sort order. |
| [`properties`](/resources/stacks/flare/case_scenario/rewrite_dataset/)    | mapping    | Configuration properties to be used during the compaction action. |
| `where`         | string | Predicate string used to filter which files are eligible for rewriting. All files that may contain matching data will be considered. |

## strategy



## Properties

| Attributes                         | Default Value           | Description |
|-----------------------------------|--------------------------|-------------|
| max-concurrent-file-group-rewrites | 5                        | Maximum number of file groups that can be rewritten in parallel. |
| partial-progress.enabled           | false                    | Enables committing file groups incrementally before the full rewrite is finished. Useful for partitions larger than available memory. |
| partial-progress.max-commits       | 10                       | Maximum number of commits allowed when partial progress is enabled. |
| target-file-size-bytes             | 536870912                | Target output file size in bytes (default is 512 MB). |
| rewrite-all                        | false                    | Force rewriting of all provided files, overriding other options. |
| max-file-group-size-bytes          | 107374182400 (100 GB)    | Largest amount of data that should be rewritten in a single file group. Helps split very large partitions into smaller, rewritable chunks to avoid cluster resource limits. |



## Examples

### **Binpack strategy**

The binpack strategy is the default behavior in Iceberg when no explicit sorting strategy is provided. This strategy simply combines files without any global sorting or specific field-based sorting.


Rewrite the data files in table `lakehouse:retail/pos_store_product_cust` using the default rewrite algorithm of bin-packing to combine small files and also split large files according to the default write size of the table.

```yaml
version: v1 # Version
name: rewrite # Name of the Workflow
type: workflow # Type of Resource (Here its a workflow)
tags: # Tags
  - Rewrite
workflow: # Workflow Specific Section
  title: Compress iceberg data files # Title of the DAG
  dag: # DAG (Directed Acyclic Graph)
    - name: rewrite # Name of the Job
      title: Compress iceberg data files # Title of the Job
      spec: # Specs
        tags: # Tags
          - Rewrite
        stack: flare:5.0 # Stack Version (Here its Flare stack Version 5.0)
        compute: runnable-default # Compute 
        stackSpec: # Flare Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Name of Input Dataset
                dataset: dataos://lakehouse:retail/pos_store_product_cust?acl=rw # Dataset UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: rewrite_dataset # Name of the action
                input: inputDf # Input Dataset Name   # defaults to bin packing
```


### **Binpack strategy with `target-file-size-byte`**

The target-file-size-bytes property is typically used in conjunction with the binpack strategy in Iceberg.

target-file-size-bytes defines the desired size for the output files when performing a compaction or rewrite operation.

When you perform a binpack operation, the data files are merged or "packed" together, aiming to achieve the target file size. It doesn't perform sorting of data across files but simply combines smaller files into larger ones while aiming to hit the file size defined by target-file-size-bytes.

The following code snippet demonstrates the compression of Iceberg data files for a given input dataset, `inputDf`, stored in a DataOS Depot. The compression process aims to reduce the file size to a specified target size in bytes, denoted by the variable `target-file-size-bytes`.

```yaml
version: v1 # Version
name: rewrite # Name of the Workflow
type: workflow # Type of Resource (Here its a workflow)
tags: # Tags
  - Rewrite
workflow: # Workflow Specific Section
  title: Compress iceberg data files # Title of the DAG
  dag: # DAG (Directed Acyclic Graph)
    - name: rewrite # Name of the Job
      title: Compress iceberg data files # Title of the Job
      spec: # Specs
        tags: # Tags
          - Rewrite
        stack: flare:5.0 # Stack Version (Here its Flare stack Version 5.0)
        compute: runnable-default # Compute 
        stackSpec: # Flare Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Name of Input Dataset
                dataset: dataos://lakehouse:retail/pos_store_product_cust?acl=rw # Dataset UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: rewrite_dataset # Name of the action
                input: inputDf # Input Dataset Name 
                options: # Options
                  properties: # Properties
                    "target-file-size-bytes": "2500048" # Target File Size in Bytes
```


###  **binpack strategy with `where` filter condition**


Since the where clause is specified (id = 3 and name = "foo"), the query will select the files that contain data matching the filter condition (id = 3 and name = "foo"), and only those files will be rewritten.

```yaml
version: v1 # Version
name: rewrite # Name of the Workflow
type: workflow # Type of Resource (Here its a workflow)
tags: # Tags
  - Rewrite
workflow: # Workflow Specific Section
  title: Compress iceberg data files # Title of the DAG
  dag: # DAG (Directed Acyclic Graph)
    - name: rewrite # Name of the Job
      title: Compress iceberg data files # Title of the Job
      spec: # Specs
        tags: # Tags
          - Rewrite
        stack: flare:5.0 # Stack Version (Here its Flare stack Version 5.0)
        compute: runnable-default # Compute 
        stackSpec: # Flare Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Name of Input Dataset
                dataset: dataos://lakehouse:retail/pos_store_product_cust?acl=rw # Dataset UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: rewrite_dataset # Name of the action
                input: inputDf # Input Dataset Name   #defaults to bin packing ? check the file zie to verify if file is 512 MB.
                options: # Options
                  where: 'id = 3 and name = "foo"'
``` 




### **Regular sorting**

Rewrite the data files in table `lakehouse:retail/pos_store_product_cust` by sorting all the data on id and name using the same defaults as bin-pack to determine which files to rewrite.

Provide the following information in right order (ColumnName, Order, NUllOrder):

- ColumnName: The column to sort by.

- SortDirection: Can be either `ASC` (ascending) or `DESC` (descending).

- NullOrder: Specifies how to handle null values:

     - `NULLS FIRST`: This places all rows with NULL values at the beginning of the sorted data.

     - `NULLS LAST`: This places all rows with NULL values at the end of the sorted data.

```yaml
version: v1 # Version
name: rewrite # Name of the Workflow
type: workflow # Type of Resource (Here its a workflow)
tags: # Tags
  - Rewrite
workflow: # Workflow Specific Section
  title: Compress iceberg data files # Title of the DAG
  dag: # DAG (Directed Acyclic Graph)
    - name: rewrite # Name of the Job
      title: Compress iceberg data files # Title of the Job
      spec: # Specs
        tags: # Tags
          - Rewrite
        stack: flare:5.0 # Stack Version (Here its Flare stack Version 5.0)
        compute: runnable-default # Compute 
        stackSpec: # Flare Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Name of Input Dataset
                dataset: dataos://icebase:retail/pos_store_product_cust?acl=rw # Dataset UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: rewrite_dataset # Name of the action
                input: inputDf # Input Dataset Name   #defaults to bin packing ? check the file zie to verify if file is 512 MB.
                options: # Options
                  strategy: sort
                  sort_order: (id, ASC NULLS FIRST).     #(id, Order NullOrder).
```


### **Z-Order sorting**

Z-ordering sorts data based on multiple columns (e.g., `product_type` and `store_location`) to optimize query performance by clustering related data together. This reduces the number of files scanned during queries.

In a retail dataset (`lakehouse:retail/pos_store_product_cust`), Z-ordering by product_type and store_location helps efficiently query sales data for specific combinations of these fields.

```yaml
version: v1 # Version
name: rewrite # Name of the Workflow
type: workflow # Type of Resource (Here its a workflow)
tags: # Tags
  - Rewrite
workflow: # Workflow Specific Section
  title: Compress iceberg data files # Title of the DAG
  dag: # DAG (Directed Acyclic Graph)
    - name: rewrite # Name of the Job
      title: Compress iceberg data files # Title of the Job
      spec: # Specs
        tags: # Tags
          - Rewrite
        stack: flare:5.0 # Stack Version (Here its Flare stack Version 5.0)
        compute: runnable-default # Compute 
        stackSpec: # Flare Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Name of Input Dataset
                dataset: dataos://lakehouse:retail/pos_store_product_cust?acl=rw # Dataset UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: rewrite_dataset # Name of the action
                input: inputDf # Input Dataset Name   #defaults to bin packing ? check the file zie to verify if file is 512 MB.
                options: # Options
                  strategy: sort
                  sortOrder: zorder(product_type, store_location)
```

## Pros and Cons of using different strategies

| Strategy   | What it does | Pros | Cons |
|------------|--------------|------|------|
| **Binpack** | Combines files only; no global sorting (will do local sorting within tasks) | This offers the fastest compaction jobs. | Data is not clustered. |
| **Sort**    | Sorts by one or more fields sequentially prior to allocating tasks (e.g., sort by field a, then within that, sort by field b) | Data clustered by often queried fields can lead to much faster read times. | This results in longer compaction jobs compared to binpack. |
| **Z-order** | Sorts by multiple fields that are equally weighted, prior to allocating tasks (X and Y values in this range are in one grouping; those in another range are in another grouping) | If queries often rely on filters on multiple fields, this can improve read times even further. | This results in longer-running compaction jobs compared to binpack. |
