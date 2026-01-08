# AWS-backed DataOS Lakehouse

DataOS Lakehouse is a  Resource that merges Apache Iceberg table format with cloud object storage, complying a fully managed storage architecture that blends the strengths of data lakes and data warehouses.

The DataOS Lakehouse (AWS-backed) provides a secure, scalable, and cost-efficient data storage and analytics layer built on Amazon S3 with Apache Iceberg as the table format. It can be used as a sink to store both Batch and Change Data Capture (CDC) pipelines in Nilus. It provides a unified data storage layer where structured and semi-structured data can be written and consumed downstream.

Connections to the AWS Lakehouse are managed only through DataOS Depot, which centralizes authentication and credentials. Nilus writes batch and CDC data to a DataOS Lakehouse (Iceberg), addressed by providing UDL as:

```yaml
dataos://<lakehouse-name>
```

## Prerequisites 

The following configurations must be set up before using the AWS-backed DataOS Lakehouse:

### **Environment Variables**

For AWS-backed Lakehouse, following environment variables must be configured (via Depot and Instance-Secret):

| Variable                | Description                             |
| ----------------------- | --------------------------------------- |
| `TYPE`                  | Must be set to `S3`                     |
| `DESTINATION_BUCKET`    | S3 bucket URL (`s3://bucket-name/path`) |
| `AWS_ACCESS_KEY_ID`     | AWS access key                          |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key                          |
| `AWS_REGION`            | AWS region (e.g., `us-east-1`)          |
| `AWS_ENDPOINT`          | (Optional) Custom S3 endpoint URL       |

!!! info
    Contact the DataOS Administrator or Operator to obtain configured Depot UDL and other required parameters.


### **Required AWS Setup**

1. **S3 Configuration**
     1. Create S3 bucket.
     2. Apply appropriate IAM roles or access keys.
     3. Enable encryption (KMS recommended).
     4. Configure lifecycle policies if needed.
2. **IAM Requirements**
     1. `s3:GetObject`, `s3:ListBucket` for reads.
     2. `s3:PutObject` for writes.
     3. `kms:Decrypt` if using KMS encryption.
3. **Region & Networking**
     1. Ensure region alignment with workloads.
     2. Configure cross-region access if applicable.
     3. Use VPC endpoints for secure private access.

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
    description: Nilus CDC Service for Postgres to s3 Iceberg
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
          address: dataos://aws_depot
          options:
            dest-table: retail
            incremental-strategy: append
    ```

* `address` – UDL of Lakehouse to write into.
* `dest-table` – target `schema.table` (or table). (Table name is optional for CDC service)
* `incremental-strategy` – `append` (typical for CDC).
* Cloud region option (`aws_region` ) only when needed for cloud-specific routing.

??? note "Defining Partitions on Lakehouse Destination Datasets"
    Partitions can be defined on Lakehouse destination datasets using the `sink.options` field within a Nilus manifest file. Partitioning improves query performance and data organization by segmenting the dataset based on specified column values.

    ```yaml
    name: lh-partition-demo
    version: v1
    type: workflow
    tags:
      - workflow
      - nilus-batch
    description: Nilus Batch Service Sample
    workflow:
      dag:
        - name: partition-lakehouse
          spec:
            stack: nilus:1.0
            compute: runnable-default
            resources:
              requests:
                cpu: 100m
                memory: 256Mi
            logLevel: Info
            stackSpec:
              source:
                address: dataos://ncdcpostgres3
                options:
                  source-table: "public.customer"
              sink:
                address: dataos://demolakehouse
                options:
                  dest-table: "partition.pg_to_lh_2"
                  incremental-strategy: append
                  partition-by:
                    - column: updated_at
                      type: year
                      name: yearly_partition
                      index: 2
                    - column: premise
                      type: identity
                      name: identity_partition
                      index: 1
                    - column: city
                      type: bucket
                      bucket-count: 3
                      name: bucket_partition
                      index: 1
    ```
    
    The `partition-by` option defines how data is partitioned in the destination Lakehouse table. Each entry in the list represents a partitioning strategy based on a specific column. The attributes available for each partition definition include:
    
    - `column`: Specifies the column from the source dataset on which partitioning is applied.

    - `type`: Determines the partitioning strategy.(`year`, `identity`, `bucket`, etc. )

    - `name`: Defines a custom name for the partition. This name is used in the physical layout of the data within the destination.

    - `index`: Specifies the order in which partition keys are applied. Lower index values indicate higher priority in the partition hierarchy.

    - `bucket-count` (required for `bucket` type only): Indicates the total number of buckets into which the data will be distributed based on the hash of the column values.


## Sink Attributes Details

| Option                 | Required           | Description                                                | Callouts                     |
| ---------------------- | ------------------ | ---------------------------------------------------------- | ---------------------------- |
| `dest-table`           | Yes                | Destination table name in `schema.table` format            |                              |
| `incremental-strategy` | Yes                | Strategy for writes (`append`, `replace`, `merge`)         | Merge requires `primary-key` |
| `primary-key`          | Required for merge | Column(s) used to deduplicate                              |                              |
| `aws_region`           | Optional           | Only for AWS-backed setups if required by your environment |                              |



