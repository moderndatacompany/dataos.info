# AWS Athena

**Amazon Athena** is a serverless, interactive query service that allows you to analyze data stored in Amazon S3 using standard SQL.

Nilus supports Athena as a **batch ingestion source**, enabling queries over S3 data (typically in **Parquet, ORC, or Iceberg format**) and movement of results into the DataOS Lakehouse or other supported destinations.

!!! info
    - AWS Athena does not support Depot. To configure connections, use service account credentials provided through the Instance Secret Resource in the URI.
    - Contact the DataOS Administrator or Operator to obtain configured URI and other required parameters.


## Prerequisites

The following are the requirements for enabling Batch Data Movement in AWS Athena:

1. **S3 Configuration**
     1. Ensure the S3 bucket exists.
     2. Proper IAM permissions (read, write if staging).
     3. Encryption and lifecycle policies are recommended.
2. **Athena Setup**
     1. Workgroup defined (`primary` by default).
     2. Query results location configured in S3.
     3. Glue Data Catalog is integrated with external tables.
3. **IAM Permissions**
     1. `AmazonAthenaFullAccess` or equivalent (restricted as per least privilege).
     2. `AmazonS3ReadOnlyAccess` for source buckets.
     3. Glue permissions (`GetDatabase`, `GetTable`, etc.).
4. **Required Parameters**
     1. `bucket`: S3 bucket containing the dataset (e.g., `my-bucket` or `s3://my-bucket`)
     2. `access_key_id`: AWS access key ID
     3. `secret_access_key`: AWS secret access key
     4. `region_name`: AWS region (e.g., `us-east-1`)
5. **Optional Parameters**
     1. `session_token`: Temporary AWS session token
     2. `workgroup`: Athena workgroup (default: `primary`)
     3. `profile`: AWS profile name (Nilus loads credentials from local AWS config)

## Sample Workflow Config

```yaml
name: nb-athena-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for AWS Athena to DataOS Lakehouse
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
            cpu: 400m
            memory: 512Mi
        stackSpec:
          source:
            address: athena://?bucket=my_bucket&profile=my_profile&region_name=us-east-1&workgroup=analytics
            options:
              source-table: analytics.orders
              incremental-key: updated_at
          sink:
            address: dataos://testaswlh
            options:
              dest-table: athena_retail.batch_orders
              incremental-strategy: replace

```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attribute Details

Nilus supports the following source options for AWS Athena:

| Option            | Required | Description                           |
| ----------------- | -------- | ------------------------------------- |
| `source-table`    | Yes      | Table name (`schema.table`)           |
| `incremental-key` | No       | Column used for incremental ingestion |
| `workgroup`       | No       | Athena workgroup (default: `primary`) |

!!! info "Core Concepts"
    

    1. **Data Storage**
        1. Athena queries external tables defined in **AWS Glue Catalog**.
        2. Data is typically stored as **columnar Parquet** files for efficiency.
    2. **Incremental Loading**
        1. Supported via timestamp/sequential ID columns (e.g., `last_updated_at`).
        2. Default incremental key: `submission_date_time`.
    3. **Cost Model**
        1. Athena charges **per TB scanned**.
        2. Partition pruning and columnar formats significantly reduce cost.


