# Azure-backed DataOS Lakehouse

DataOS Lakehouse is a Resource that merges Apache Iceberg table format with cloud object storage, yielding a fully managed storage architecture that blends the strengths of data lakes and data warehouses.&#x20;

The DataOS Lakehouse (Azure-backed) provides a secure, scalable, and cloud-native data storage and analytics layer built on Azure Data Lake Storage Gen2 (ABFSS), using Apache Iceberg or Delta Lake as table formats.

The DataOS Lakehouse can be used as a sink to store both batch and change data capture (CDC) pipelines in Nilus. It provides a unified data storage layer where structured and semi-structured data can be written and consumed downstream.

Connections to the Azure Lakehouse are managed only through DataOS Depot, which centralizes authentication and storage configuration. Nilus writes batch and CDC data to a DataOS **Lakehouse** (Iceberg), addressed by providing UDL as:

```yaml
dataos://<lakehouse-name>
```

## Prerequisites 

The following configurations must be set up before using the Azure-backed DataOS Lakehouse:

### **Environment Variables**

For Azure-backed Lakehouse, following environment variables must be configured (via Depot and Instance-Secret):

| Variable                     | Description                                                      |
| ---------------------------- | ---------------------------------------------------------------- |
| `TYPE`                       | Must be set to `ABFSS`                                           |
| `DESTINATION_BUCKET`         | ABFSS URL: `abfss://<container>@<account>.dfs.<endpoint_suffix>` |
| `AZURE_STORAGE_ACCOUNT_NAME` | Azure storage account name                                       |
| `AZURE_STORAGE_ACCOUNT_KEY`  | Azure storage account key                                        |
| `METASTORE_URL`              | (Optional) External metastore URL                                |

!!! info
    Contact the DataOS Administrator or Operator to obtain configured Depot UDL.


### **Required Azure Setup**

1. **Storage Account**
     1. Enable **hierarchical namespace** (for Data Lake Storage Gen2).
     2. Configure **network access controls**.
     3. Apply **encryption at rest** (Microsoft-managed or customer-managed keys).
2. **Container**
     1. Create the target container.
     2. Configure **RBAC permissions**.
     3. Enable **versioning** and **lifecycle management** as needed.
3. **Security**
     1. Rotate account keys regularly.
     2. Implement firewall and VNet integration.
     3. Use CORS if cross-service access is needed.

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
          address: dataos://azure_depot
          options:
            dest-table: retail
            incremental-strategy: append
    ```

* `address` – UDL of Lakehouse to write into.
* `dest-table` – target `schema.table` (or table) (Table is optional for CDC service)
* `incremental-strategy` – `append` (typical for CDC).

## Sink Attributes Details

| Option                 | Required           | Description                                        | Callouts                     |
| ---------------------- | ------------------ | -------------------------------------------------- | ---------------------------- |
| `dest-table`           | Yes                | Destination table name in `schema.table` format    |                              |
| `incremental-strategy` | Yes                | Strategy for writes (`append`, `replace`, `merge`) | Merge requires `primary-key` |
| `primary-key`          | Required for merge | Column(s) used to deduplicate                      |                              |

