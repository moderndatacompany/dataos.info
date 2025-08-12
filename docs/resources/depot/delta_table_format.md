# Using Delta table format in object storage Depots

In DataOS, object storage Depots (ABFSS, Amazon S3, GCS, WASBS) supports two different table formats: `iceberg` and `delta`.  This section focuses on the Delta table format.

## What does the Delta table format actually do?

At its core, Delta table format adds a transactional metadata layer to cloud object storage, enabling ACID-compliant operations for Parquet files. In DataOS, when you configure a Depot with `format: delta`, you're enabling data ingestion using Delta-compatible read and write [Flare jobs](/resources/stacks/flare/).

<aside class="callout">
🗣️ Delta table format is supported only for read and write Flare jobs.
You cannot query Delta tables in Workbench or via SQL-based interactive interfaces.
For query support across multiple engines (Spark, Trino), use `format: iceberg`.
</aside>

**In DataOS:**

- Use `format: delta` in a Depot to enable Delta table format support (best with Spark).

- Use `format: iceberg` in a Depot to enable Iceberg table format support (works with Spark, Trino, and more).


## Supported object storage sources in DataOS for Delta table format

DataOS supports the Delta table format on the following object storage Depots:

=== "Amazon S3"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    tags:
        - ${{tag1}}
    owner: ${{owner-name}}
    layer: user
    description: ${{description}}
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
        format: delta
        region: ${{us-gov-east-1}}
        endpoint: ${{s3.us-gov-east-1.amazonaws.com}}
    ```

=== "Azure Blob File System Secure (ABFSS)"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    tags:
      - ${{tag1}}
      - ${{tag2}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: ABFSS
      description: ${{description}}
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
        format: delta
        relativePath: ${{delta}}
    ```

=== "Google Cloud Storage (GCS)"

    ```yaml
    name: ${{"sanitygcs01"}}
    version: v2alpha
    type: depot
    tags:
      - ${{GCS}}
      - ${{Sanity}}
    layer: user
    depot:
      type: GCS
      description: ${{"GCS depot for sanity"}}
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
        format: delta
    ```

=== "Windows Azure Storage Blob Service (WASBS)"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    tags:
      - ${{tag1}}
      - ${{tag2}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: WASBS
      description: ${{description}}
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
        format: delta
    ```

For each of these storage types, a Depot can be created with `format: delta` so that Delta table management is enabled in DataOS.