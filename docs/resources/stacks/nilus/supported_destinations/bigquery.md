# BigQuery

BigQuery is Google Cloud’s fully managed, serverless cloud data warehouse. The Nilus connector supports BigQuery as a destination for both Change Data Capture (CDC) and Batch data movement, enabling real-time streaming–style upserts or scheduled bulk loads.

Nilus connects to BigQuery either via a direct connection URI or through DataOS Depot, which centralizes authentication, credentials, and connection details.

## Prerequisites

The following configurations must be set up before using the BigQuery:

### **Service Account Permissions**

The service account used for BigQuery connections must have the following roles:

* `roles/bigquery.dataViewer` (BigQuery Data Viewer)
* `roles/bigquery.jobUser` (BigQuery Job User)
* `roles/bigquery.user` (BigQuery User)
* `roles/bigquery.dataEditor` to create/update tables (BigQuery Editor)

### **Required Parameters**

| Parameter            | Description                                           |
| -------------------- | ----------------------------------------------------- |
| `project-name`       | Google Cloud project ID                               |
| `credentials_path`   | Path to service account JSON file                     |
| `credentials_base64` | Base64-encoded credentials JSON (alternative to path) |
| `location`           | Dataset location (default: `US`)                      |

!!! info
    - Prefer granting `jobUser` at **project** scope and `dataEditor` at **dataset** scope to keep privileges tight while allowing loads to run.
    - Contact the DataOS Administrator or Operator to obtain configured Depot UDL and other required parameters.

## Sink Configuration

=== "Syntax with Depot"
    ```yaml
    sink:
      address: dataos://bigquery_depot
      options:
        dest-table: retail.orders
        incremental-strategy: append
    ```
=== "Syntax without Depot"
    ```yaml
    sink:
      address: bigquery://<project-name>?credentials_path=/path/to/service/account.json&location=<location>
      options:
        dest-table: retail.orders
        incremental-strategy: append
        staging-bucket: "gs://your-bucket-name"  # Optional: GCS bucket for staging data
    ```
=== "Example"
    ```yaml
    name: nb-lh-aws-test-01
    version: v1
    type: workflow
    tags:
        - workflow
        - nilus-batch
    description: Nilus Batch Workflow Sample for AWS Lakehouse to BigQuery
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
                address: dataos://testawslh
                options:
                  source-table: sales.orders
              sink:
                address: bigquery://<project-name>?credentials_path=/path/to/service/account.json&location=<location>
                options:
                  dest-table: retail.orders
                  incremental-strategy: append
                  staging-bucket: "gs://your-bucket-name"  # Optional: GCS bucket for staging data
    ```

## Sink Attributes Details

Nilus supports the following BigQuery sink configuration options:

| Option                 | Required | Description                                    |
| ---------------------- | -------- | ---------------------------------------------- |
| `dest-table`           | Yes      | Destination table name in dataset.table format |
| `incremental-strategy` | Yes      | Strategy for writes (`append`, `replace`)      |
| `staging-bucket`       | Optional | GCS bucket for staging area                    |
