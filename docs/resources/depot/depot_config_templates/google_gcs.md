# Google Cloud Storage (GCS)

DataOS provides the capability to connect to Google Cloud Storage data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics.

## Requirements

To establish a connection with Google Cloud Storage (GCS), the following information is required:

- GCS Bucket
- Relative Path
- GCS Project ID
- GCS Account Email
- GCS Key

## Template

To create a Depot of Google Cloud Storage, in the type field you will have to specify type 'GCS', and utilize the following template:

=== "v1"

    ```yaml
    name: {{"sanitygcs01"}}
    version: v1
    type: depot
    tags:
      - {{GCS}}
      - {{Sanity}}
    layer: user
    depot:
      type: GCS
      description: {{"GCS depot for sanity"}}
      compute: {{runnable-default}}
      spec:
        bucket: {{"airbyte-minio-testing"}}
        relativePath: {{"/sanity"}}
      external: {{true}}
      connectionSecret:
        - acl: {{rw}}
          type: key-value-properties
          data:
            projectid: {{$GCS_PROJECT_ID}}
            email: {{$GCS_ACCOUNT_EMAIL}}
          files:
            gcskey_json: {{$GCS_KEY_JSON}}
    ```
=== "v2alpha"

    ```yaml
    name: {{"sanitygcs01"}}
    version: v2alpha
    type: depot
    tags:
      - {{GCS}}
      - {{Sanity}}
    layer: user
    depot:
      type: GCS
      description: {{"GCS depot for sanity"}}
      compute: {{runnable-default}}
      gcs:
        bucket: {{"airbyte-minio-testing"}}
        relativePath: {{"/sanity"}}
      external: {{true}}
      connectionSecret:
        - acl: {{rw}}
          type: key-value-properties
          data:
            projectid: {{$GCS_PROJECT_ID}}
            email: {{$GCS_ACCOUNT_EMAIL}}
          files:
            gcskey_json: {{$GCS_KEY_JSON}}
    ```