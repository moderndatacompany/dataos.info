# GCP-backed DataOS Lakehouse

The **DataOS Lakehouse (GCP-backed)** provides a secure, scalable, and cloud-native data storage and analytics layer built on **Google Cloud Storage (GCS)**, using **Apache Iceberg** or **Delta Lake** as table formats.

Nilus supports the Lakehouse as both a **source** and a **sink**, enabling efficient batch data movement to and from the DataOS ecosystem.

Connections to the GCP Lakehouse are managed only through **DataOS Depot**, which centralizes authentication and credentials by offering UDL as:

```yaml
dataos://<lakehouse-name>
```

## Prerequisites

Following are the requirements for enabling Batch Data Movement in GCP-backed DataOS Lakehouse:

### **Environment Variables**

For GCP-backed Lakehouse, the following environment variables must be set (via Depot or workflow):

| Variable                 | Description                              |
| ------------------------ | ---------------------------------------- |
| `TYPE`                   | Must be set to `GCS`                     |
| `DESTINATION_BUCKET`     | GCS URL in format `gs://<bucket>/<path>` |
| `GCS_CLIENT_EMAIL`       | Service account email                    |
| `GCS_PROJECT_ID`         | GCP project ID                           |
| `GCS_PRIVATE_KEY`        | Service account private key              |
| `GCS_JSON_KEY_FILE_PATH` | Path to service account JSON key file    |
| `METASTORE_URL`          | (Optional) External metastore URL        |

!!! info
    Contact the DataOS Administrator or Operator to obtain the configured Depot UDL.


### **Authentication Method**

Nilus supports authentication via HMAC credentials for GCP:

**HMAC Credentials(Hash-based Message Authentication Code)**

1. `GCS_ACCESS_KEY_ID`: HMAC key ID
2. `GCS_SECRET_ACCESS_KEY`: HMAC secret
3. Useful for S3-compatible access scenarios.

### **Required GCP Setup**

1. **GCS Bucket**
     1. Create the target bucket.
     2. Configure access control (IAM roles, ACLs).
     3. Enable **versioning** and **lifecycle management** as needed.
2. **Service Account**
     1. Create a service account.
     2. Generate JSON key file.
     3. Assign required roles:
      1. `roles/storage.objectViewer`
      2. `roles/storage.objectCreator`
      3. `roles/storage.admin` (if managing bucket metadata)
3. **Security**
     1. Configure IAM policies.
     2. Rotate keys regularly.
     3. Enable **audit logging** for storage operations.

## Sample Workflow Config

```yaml
name: nb-lh-gcs-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for GCS Lakehouse
workspace: research
workflow:
  dag:
    - name: nb-job-01
      spec:
        stack: nilus:1.0
        compute: runnable-default
        logLevel: INFO
        resources:
          requests:
            cpu: 500m
            memory: 512Mi
        stackSpec:
          source:
            address: dataos://gcs_lh_depot
            options:
              source-table: sales.orders
          sink:
            address: lakehouse://postgres_depot
            options:
              dest-table: retail.orders
              incremental-strategy: append
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```


## Supported Attribute Details

Nilus supports the following source options for GCP-backed DataOS Lakehouse:

| Option           | Required | Description                       |
| ---------------- | -------- | --------------------------------- |
| `source-table`   | Yes      | Table name (`schema.table`)       |
| `staging-bucket` | Optional | GCS bucket for staging operations |
| `metastore_url`  | No       | External metastore URL            |

!!! info "Core Concepts"
    

    * **Storage Formats**
        * **Iceberg**: schema evolution, partition pruning, time travel.
        * **Delta Lake**: ACID transactions, schema enforcement, version history.
        * **Parquet**: columnar file format underpinning both.
    * **Path Format**
      
      ```yaml
        gs://<bucket>/<relativePath>/<collection>/<dataset>
      ```




