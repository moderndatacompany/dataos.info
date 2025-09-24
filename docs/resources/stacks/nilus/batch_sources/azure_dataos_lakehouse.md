# Azure-backed DataOS Lakehouse

The **DataOS Lakehouse (Azure-backed)** provides a secure, scalable, and cloud-native data storage and analytics layer built on **Azure Data Lake Storage Gen2 (ABFSS)**, using **Apache Iceberg** or **Delta Lake** as table formats.

Nilus supports the Lakehouse as both a **source** and a **sink**, enabling efficient batch data movement to and from the DataOS ecosystem.

Connections to the Azure Lakehouse are managed only through **DataOS Depot**, which centralizes authentication and credentials by offering UDL as:

```yaml
dataos://<lakehouse-name>
```

## Prerequisites

Following are the requirements for enabling Batch Data Movement in Azure-backed DataOS Lakehouse:

### **Environment Variables**

For Azure-backed Lakehouse, the following environment variables must be set (via Depot or Instance Secret):

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

* **Storage Account**
    * Enable **hierarchical namespace** (for Data Lake Storage Gen2).
    * Configure **network access controls**.
    * Apply **encryption at rest** (Microsoft-managed or customer-managed keys).
* **Container**
    * Create the target container.
    * Configure **RBAC permissions**.
    * Enable **versioning** and **lifecycle management** as needed.
* **Security**
    * Rotate account keys regularly.
    * Implement firewall and VNet integration.
    * Use CORS if cross-service access is needed.

## Sample Workflow Config

```yaml
name: nb-lh-azure-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for Azure Lakehouse
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
            address: dataos://azure_lh_depot
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


## Supported Attribute Details

Nilus supports the following source options for Azure-backed DataOS Lakehouse:

| Option                       | Required               | Description                 |
| ---------------------------- | ---------------------- | --------------------------- |
| `source-table`               | Yes                    | Table name (`schema.table`) |
| `azure_storage_account_name` | Yes (via Depot/secret) | Storage account name        |
| `azure_storage_account_key`  | Yes (via Depot/secret) | Storage account key         |
| `metastore_url`              | No                     | External metastore URL      |

!!! info "Core Concepts"
    * **Storage Formats**
        * **Iceberg** (default): schema evolution, partition pruning, time travel.
        * **Delta Lake**: ACID transactions, schema enforcement, version history.
        * **Parquet**: columnar file format underpinning both.
    * **ABFSS Support**
        * Default endpoint suffix: `core.windows.net`.
        * Custom endpoint suffix supported (via Depot).
    * **Path format:**

      ```yaml
      abfss://<container>@<account>.dfs.<endpoint_suffix>/<relativePath>/<collection>/<dataset>
      ```






