# Using Iceberg table format in object storage Depots

In DataOS, object storage Depots (ABFSS, Amazon S3, GCS, WASBS) supports two different table formats: `iceberg` and `delta`.  This section focuses on the Iceberg table format.

## What does the Iceberg table format actually do?

The Iceberg format manages both the data (Parquet/ORC/Avro files) and the metadata (schemas, snapshots, partitions) in a structured, versioned layout across object storage. Here's how it works behind the scenes:

| Layer              | What It Does                                                                                                          |
| ------------------ | --------------------------------------------------------------------------------------------------------------------- |
| **Data Layer**     | Stores actual data files (e.g., Parquet). Immutable and columnar for efficient reads.                                 |
| **Metadata Layer** | Tracks schema, partitions, file locations, and snapshot history. Enables version control, rollback, and optimization. |
| **Catalog Layer**  | Provides a central registry to discover and access tables. Maps table names to metadata locations.                    |


With this layered architecture, Iceberg provides:

- Atomic operations for inserts, deletes, and updates, even across multiple partitions.

- **Schema evolution:** Add, drop, or rename columns without rewriting data.

- **Partition evolution:** Change the partition strategy over time with zero rewrites.

- **Snapshot-based time travel:** Query your data as it existed at any point in the past.

- **Efficient metadata pruning:** Only scan relevant files for each query.

In essence, Iceberg separates metadata from compute, enabling multiple engines (e.g., Spark, Trino) to safely and efficiently read/write to the same dataset concurrently.


## Supported object storage sources in DataOS

DataOS supports the Iceberg table format on the following object storage Depots:

=== "Amazon S3"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    description: ${{description}}
    tags:
        - ${{tag1}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: S3                                          
      external: ${{true}}
      secrets:
        - name: ${{s3-instance-secret-name}}-r
            allkeys: true

        - name: ${{s3-instance-secret-name}}-rw
            allkeys: true
      s3:                                            
        scheme: ${{s3a}}
        bucket: ${{project-name}}
        relativePath: ${{relative-path}}
        format: iceberg
        icebergCatalogType: hadoop
        metastoreType: rest
        metastoreUrl: http://lakehouse-svc.cluster.local:1000
        relativePath: ${{icebase}}        
        region: ${{us-gov-east-1}}
        endpoint: ${{s3.us-gov-east-1.amazonaws.com}}
    ```

=== "Azure Blob File System Secure (ABFSS)"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    description: ${{description}}
    tags:
      - ${{tag1}}
      - ${{tag2}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: ABFSS                                       
      external: ${{true}}
      compute: ${{runnable-default}}
      secrets:
        - name: ${{abfss-instance-secret-name}}-r
          allkeys: true
        - name: ${{abfss-instance-secret-name}}-rw
          allkeys: true
      abfss:                                             
        account: ${{account-name}}
        container: ${{container-name}}
        endpointSuffix: ${{windows.net}}
        format: iceberg
        icebergCatalogType: hadoop
        metastoreType: rest
        metastoreUrl: http://lakehouse-svc.cluster.local:1000
        relativePath: ${{icebase}}
    ```

=== "Google Cloud Storage (GCS)"

    ```yaml
    name: ${{"sanitygcs01"}}
    version: v2alpha
    type: depot
    description: ${{"GCS depot for sanity"}}
    tags:
      - ${{GCS}}
      - ${{Sanity}}
    layer: user
    depot:
      type: GCS
      compute: ${{runnable-default}}
      external: ${{true}}
      secrets:
        - name: ${{gcs-instance-secret-name}}-r
          allkeys: true

        - name: ${{gcs-instance-secret-name}}-rw
          allkeys: true  
      gcs:
        bucket: ${{"airbyte-minio-testing"}}
        relativePath: ${{"/sanity"}}
        format: iceberg
        icebergCatalogType: ${{}}
        metastoreUrl: ${{}}
        relativePath: ${{icebase}}
    ```

=== "Windows Azure Storage Blob Service (WASBS)"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    description: ${{description}}
    tags:
      - ${{tag1}}
      - ${{tag2}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: WASBS                                      
      external: ${{true}}
      compute: ${{runnable-default}}
      secrets:
        - name: ${{wasbs-instance-secret-name}}-r
          allkeys: true

        - name: ${{wasbs-instance-secret-name}}-rw
          allkeys: true
      wasbs:                                          
        account: ${{account-name}}
        container: ${{container-name}}
        relativePath: ${{relative-path}}
        format: iceberg
        icebergCatalogType: hadoop
        metastoreType: rest
        metastoreUrl: http://lakehouse-svc.cluster.local:1000
        relativePath: ${{icebase}}          
    ```


For each of these storage types, a Depot can be created with `format: iceberg` so that Iceberg table management is enabled in DataOS.




