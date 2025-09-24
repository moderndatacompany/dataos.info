# AWS-backed DataOS Lakehouse

The **DataOS Lakehouse (AWS-backed)** provides a secure, scalable, and cost-efficient data storage and analytics layer built on **Amazon S3** with **Apache Iceberg** as the table format.

Nilus supports the Lakehouse both as a **source** and a **sink**, enabling seamless batch data movement to and from the DataOS ecosystem.

Connections to the AWS Lakehouse are managed via **DataOS Depot**, which centralizes authentication and credentials by offering UDL as:

```yaml
dataos://<lakehouse-name>
```

## Prerequisites

The following are the requirements for enabling Batch Data Movement in AWS-backed DataOS Lakehouse:

### **Environment Variables**

For AWS-backed Lakehouse, the following environment variables must be configured (via Depot and Instance-Secret):

| Variable                | Description                             |
| ----------------------- | --------------------------------------- |
| `TYPE`                  | Must be set to `S3`                     |
| `DESTINATION_BUCKET`    | S3 bucket URL (`s3://bucket-name/path`) |
| `AWS_ACCESS_KEY_ID`     | AWS access key                          |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key                          |
| `AWS_REGION`            | AWS region (e.g., `us-east-1`)          |
| `AWS_ENDPOINT`          | (Optional) Custom S3 endpoint URL       |

!!! info
    Contact the DataOS Administrator or Operator to obtain the configured Depot UDL.


### **Required AWS Setup**

* **S3 Configuration**
    * Create an S3 bucket.
    * Apply appropriate IAM roles or access keys.
    * Enable encryption (KMS recommended).
    * Configure lifecycle policies if needed.
* **IAM Requirements**
    * `s3:GetObject`, `s3:ListBucket` for reads.
    * `s3:PutObject` for writes.
    * `kms:Decrypt` if using KMS encryption.
* **Region & Networking**
    * Ensure region alignment with workloads.
    * Configure cross-region access if applicable.
    * Use VPC endpoints for secure private access.

## Sample Workflow Config

```yaml
name: nb-lh-aws-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for AWS Lakehouse
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
            address: dataos://postgres_depot
            options:
              dest-table: retail.orders
              incremental-strategy: merge
              primary-key: order_id

```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


## Supported Attribute Details

Nilus supports the following source options for AWS-backed DataOS Lakehouse:

| Option         | Required | Description                                             |
| -------------- | -------- | ------------------------------------------------------- |
| `source-table` | Yes      | Table name in `schema.table` format                     |
| `aws_region`   | No       | Region (overrides Depot config)                         |
| `aws_endpoint` | No       | Custom S3 endpoint if required (overrides Depot config) |

!!! info "Core Concepts"

    * **Storage Format**
        * Data stored in **Apache Iceberg tables**.
        * Backed by Parquet files.
        * Supports schema evolution and time travel.
    * **Performance Features**
        * Predicate pushdown for efficient queries.
        * Partition pruning and column pruning.
        * Parallelized read/write.
        * Statistics-driven query optimization.
    * **Security**
        * IAM-based authentication.
        * Encrypted S3 endpoints.
        * Supports custom endpoints (e.g., MinIO, local S3-compatible stores).






