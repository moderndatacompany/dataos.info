# Actions

> The Data Maintenance Actions are only supported in DataOS Internal Storage Depot, Icebase.

Maintenance of any Iceberg table is challenging; therefore, DataOS internal depot Icebase gives users in-built capabilities to manage and maintain metadata files and data. In DataOS, these operations can be performed using Flare stack. The service in Flare is offered through `actions`. 

The `actions` section within a YAML is defined as follows:

```yaml
version: v1 # Version
name: manifest # Name of the Workflow
type: workflow # Type of Resource (Here its workflow)
workflow: # Workflow Section
  dag:
    - name: actions # Name of the Job
      spec: # Specs
        stack: flare:4.0 # Stack is Flare (so it's a Flare Job)
        compute: runnable-default # Compute
        flare: # Flare Stack specific Section
          job: # Job Section
            explain: true # Explain
            inputs: # Inputs Section
              - name: inputDataset # Input Dataset Name
                dataset: dataos://icebase:actions/data?acl=rw # Input UDL
								format: Iceberg # Dataset Format
            logLevel: INFO # Loglevel
            actions: # Flare Action
								{} # Action Definition/Properties
```

Following are the different actions that can be accomplished using Flare in DataOS:

- `rewrite_dataset`
- `rewrite_manifest`
- `expire_snapshots`
- `remove_orphans`
- `delete_from_dataset`

The configurations for the different actions and their definitions are provided in the below section:

## Rewrite Dataset

> Supported in both Flare Stack Versions `flare:3.0` and `flare:4.0`.

Iceberg format within Icebase depots tracks each data file in a table. More data files lead to more metadata stored in manifest files, and small data files cause an unnecessary amount of metadata and less efficient queries from file open costs. 

The data files can be compacted in parallel within Icebase depots using Flare’s `rewrite_dataset` action. This will combine small files into larger files to reduce metadata overhead and runtime file open costs. The `rewrite_dataset` action definition for `flare:4.0` is given below:

```yaml
actions:
  - name: rewrite_dataset # Name of the Action
    input: <input-dataset-name> # Input dataset name
    options: # Options
      properties: # Properties
        "target-file-size-bytes": "<target-file-size>" # Target File Size in Bytes
```

The `rewrite_dataset` action is beneficial in the case of streaming, where small data files can be compacted into larger files to improve query performance. To explore a case scenario on how to compact files using the `rewrite_dataset` action, refer to [Rewrite Dataset](../Case%20Scenario/Rewrite%20Dataset.md).

## Rewrite Manifest

> Supported in both Flare Stack Versions `flare:3.0` and `flare:4.0`.

DataOS internal depot, Icebase uses metadata in its manifest list and manifest files to speed up query planning and to prune unnecessary data files. Some tables can benefit from rewriting manifest files to make locating data for queries much faster. The metadata tree functions as an index over a table’s data. Manifests in the metadata tree are automatically compacted in the order they are added, which makes queries faster when the write pattern aligns with read filters. For example, writing hourly-partitioned data as it arrives is aligned with time-range query filters. The `rewrite_manifest` action definition for `flare:4.0` is given below:

```yaml
actions:
  - name: rewrite_manifest # Name of the Action
    input: <input-dataset-name> # Input Dataset Name
```

A case scenario illustrating the implementation of the `rewrite_manifest` action is given, refer to [Rewrite Manifest Files](../Case%20Scenario/Rewrite%20Manifest%20Files.md).

## Expire Snapshots

> Supported in both Flare Stack Versions `flare:3.0` and `flare:4.0`

Each write to an Iceberg table within Icebase depots creates a new snapshot, or version, of a table. Snapshots can be used for time-travel queries, or the table can be rolled back to any valid snapshot. Snapshots accumulate until they are expired by Flare’s `expire_snapshots` action. The `expire_snapshots` action definition for `flare:4.0` is as follows:

```yaml
actions:
  - name: expire_snapshots # Name of the Action
    input: <input-dataset-name> # Input Dataset Name
    options: # Options
      expireOlderThan: "<date-in-unix-format-as-a-string>" # Timestamp in Unix Format (All Snapshots older than timestamp are expired)
```

Regularly expiring snapshots is recommended to delete data files that are no longer needed, and to keep the size of table metadata small. To view a case scenario for `expire_snapshots` action, refer to [Expire Snapshots](../Case%20Scenario/Expire%20Snapshots.md).

## Remove Orphans

> Supported in both Flare Stack Version `flare:3.0` and  `flare:4.0`.

While executing Flare Jobs upon Icebase depots, job failures can leave files that are not referenced by table metadata, and in some cases, normal snapshot expiration may not be able to determine if a file is no longer needed and delete it.

To clean up these ‘orphan’ files under a table location older than a specified timestamp, we can use Flare’s `remove_orphans` action. The below code block shows the definition for `remove_orphans` action for `flare:4.0`:

```yaml
actions:
  - name: remove_orphans # Name of Action
    input: <input-dataset-name> # Name of Input Dataset
    options: # Options
      olderThan: "<timestamp>" # Time to be provided in Unix Format
```

Refer to [Remove Orphans](../Case%20Scenario/Remove%20Orphans.md) to view a case scenario depicting the use of `remove_orphans` action.

## Delete from Dataset

> Supported in Flare Stack Version `flare:4.0`only.

The `delete_from_dataset` action removes data from tables. The action accepts a filter provided in the `deleteWhere` property to match rows to delete. If the delete filter matches entire partitions of the table, Iceberg format within the Icebase depot will perform a metadata-only delete. If the filter matches individual rows of a table, then only the affected data files will be rewritten. The syntax of the `delete_from_dataset` action is provided below:

```yaml
actions:
  - name: delete_from_dataset # Name of the Action
    input: <input-dataset-name> # Input Dataset Name
    deleteWhere: "<condition>" # Delete where the provided condition is true
```

The `delete_from_dataset` can be used in multiple configurations, which have been showcased in the case scenarios, refer to [Delete from Dataset](../Case%20Scenario/Delete%20from%20Dataset.md).

> 🗣️ Note: When using a GCS-based environment, use the dataset address with the `acl=rw` query parameter (e.g. `dataos://icebase:actions/random_users_data?acl=rw`). This is because GCS generates two credentials with different permissions: one with only read access and one with both read and write access. Flare actions need write access to create files, so if you don't specify `acl=rw`, Flare will default to read-only access and prevent you from updating or creating files. <br>
    
  ```yaml
    inputs:
      - name: inputDf
        dataset: dataos://icebase:actions/random_users_data?acl=rw
        format: Iceberg
  ```

A possible Error if you miss `acl` is given here.