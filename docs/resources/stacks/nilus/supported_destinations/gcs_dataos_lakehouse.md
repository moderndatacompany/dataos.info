# GCP-backed DataOS Lakehouse

DataOS Lakehouse is a Resource that merges Apache Iceberg table format with cloud object storage, yielding a fully managed storage architecture that blends the strengths of data lakes and data warehouses.&#x20;

The DataOS Lakehouse (GCP-backed) provides a secure, scalable, and cloud-native data storage and analytics layer built on Google Cloud Storage (GCS), using Apache Iceberg or Delta Lake as table formats.

The DataOS Lakehouse can be used as a sink to store both batch and change data capture (CDC) pipelines in Nilus. It provides a unified data storage layer where structured and semi-structured data can be written and consumed downstream.

Connections to the GCP Lakehouse are managed only through DataOS Depot, which centralizes authentication and storage configuration. Nilus writes batch and CDC data to a DataOS **Lakehouse** (Iceberg), addressed by providing UDL as:

```yaml
dataos://<lakehouse-name>
```

## Prerequisites 

The following configurations must be set up before using the GCP-backed DataOS Lakehouse:

### **Environment Variables**

For GCP-backed Lakehouse, following environment variables must be configured (via Depot and Instance-Secret):

| **Variable**             | **Description**                          |
| ------------------------ | ---------------------------------------- |
| `TYPE`                   | Must be set to `GCS`                     |
| `DESTINATION_BUCKET`     | GCS URL in format `gs://<bucket>/<path>` |
| `GCS_CLIENT_EMAIL`       | Service account email                    |
| `GCS_PROJECT_ID`         | GCP project ID                           |
| `GCS_PRIVATE_KEY`        | Service account private key              |
| `GCS_JSON_KEY_FILE_PATH` | Path to service account JSON key file    |
| `METASTORE_URL`          | (Optional) External metastore URL        |

!!! info
    Contact the DataOS Administrator or Operator to obtain configured Depot UDL.


### **Authentication Methods**

Nilus supports two authentication methods for GCP:

1. **Service Account JSON Key File**
     1. Standard GCP authentication method.
     2. JSON key must contain `private_key`, `client_email`, and `project_id`.
2. **HMAC Credentials(Hash-based Message Authentication Code)**
     1. `GCS_ACCESS_KEY_ID`: HMAC key ID
     2. `GCS_SECRET_ACCESS_KEY`: HMAC secret
     3. Useful for S3-compatible access scenarios.

### **Required GCP Setup**

1. **GCS Bucket**
     1. Create the target bucket.
     2. Configure access control (IAM roles, ACLs).
     3. Enable **versioning** and **lifecycle management** as needed.
2. **Service Account**
     1. Create service account.
     2. Generate JSON key file.
     3. Assign required roles:
      1. `roles/storage.objectViewer`
      2. `roles/storage.objectCreator`
      3. `roles/storage.admin` (if managing bucket metadata)
3. **Security**
     1. Configure IAM policies.
     2. Rotate keys regularly.
     3. Enable **audit logging** for storage operations.

## Sink configuration

=== "Syntax"
    ```yaml
    sink:
      address: dataos://${{lakehouse-name}}
      options:
        dest-table: ${{destination-table-name}}
        incremental-strategy: ${{incremental-strategy}}
    ```
=== "Example"
    ```yaml
    # Example of CDC for MongoDB to DataOS Lakehouse
    
    name: ncdc-mongo-test
    version: v1
    type: service
    tags:
        - service
        - nilus-cdc
    description: Nilus CDC Service for MongoDB to s3 Iceberg
    workspace: public
    service:
      servicePort: 9010
      replicas: 1
      logLevel: INFO
      compute: runnable-default
      resources:
        requests:
          cpu: 1000m
          memory: 536Mi
        limits:
          cpu: 1500m
          memory: 1000Mi
      stack: nilus:1.0
      stackSpec:
        source:
          address: dataos://testingmongocdc
          options:
            engine: debezium #mandatory for CDC; no need for batch
            collection.include.list: "sample.unnest"
            table.include.list: "sandbox.customers" #mandatory; can point to multiple tables using comma-separated values
            topic.prefix: "cdc_changelog" #mandatory; can be custom
            max-table-nesting: "0"
            transforms.unwrap.array.encoding: array
        sink:
          address: dataos://gcp_depot
          options:
            dest-table: retail
            incremental-strategy: append
                    
    ```

* `address` – UDL of Lakehouse to write into.
* `dest-table` – target `schema.table` (or table). (Table is optional for CDC service)
* `incremental-strategy` – `append` (typical for CDC).

## Sink Attributes Details

<table><thead><tr><th>Option</th><th>Required</th><th width="190.765625">Description</th><th>Callouts</th></tr></thead><tbody><tr><td><code>dest-table</code></td><td>yes</td><td>Destination table name in <code>schema.table</code> format</td><td></td></tr><tr><td><code>incremental-strategy</code></td><td>yes</td><td>Strategy for writes (<code>append</code>, <code>replace</code>, <code>merge</code>)</td><td>Merge requires <code>primary-key</code></td></tr><tr><td><code>primary-key</code></td><td>Required for merge</td><td>Column(s) used to deduplicate</td><td></td></tr></tbody></table>



