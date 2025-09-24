# Databricks

**Databricks** is a cloud-based data and AI platform built on top of Apache Spark, providing a unified environment for data engineering, machine learning, and analytics.

Nilus supports Databricks as both a **batch ingestion source** and **sink**, enabling seamless data exchange between Databricks SQL Warehouses (formerly SQL Endpoints) and the DataOS Lakehouse or other supported destinations.

## Prerequisites

The following are the requirements for enabling Batch Data Movement in Databricks:

### **Authentication**

* **Personal Access Token (PAT)** required for direct connections.
* Tokens must have appropriate scope for warehouse and data access.
* Token rotation is recommended for security.

### **SQL Warehouse Access**

* An **active SQL warehouse** must be available.
* Appropriate **USAGE and SELECT permissions** must be granted on the warehouse, catalog, schema, and tables.

### **Required Parameters**

* `token`: Personal Access Token (PAT)
* `server_hostname`: Databricks workspace hostname (e.g., `dbc-123abc-def.cloud.databricks.com`)
* `http_path`: SQL warehouse HTTP path (e.g., `/sql/1.0/warehouses/abc123def456`)
* `catalog`: (Optional) Unity Catalog name
* `schema`: (Optional) Schema name within catalog

### **Source Address**

Nilus connects to Databricks via a Direct connection URI as shown below:

```yaml
address: databricks://<token>@<server_hostname>/<http_path>?catalog=main&schema=default
```

## Sample Workflow Config

```yaml
name: nb-databricks-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for Databricks SQL Warehouse to DataOS Lakehouse
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
            address: databricks://<token>@dbc-123abc-def.cloud.databricks.com/sql/1.0/warehouses/abc123def456?catalog=main&schema=default
            options:
              source-table: analytics.orders
              incremental-key: last_updated_at
          sink:
            address: dataos://testawslh
            options:
              dest-table: databricks_retail.batch_orders
              incremental-strategy: replace
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.




## Supported Attribute Details

Nilus supports the following source options for Databricks:

| Option            | Required | Description                                |
| ----------------- | -------- | ------------------------------------------ |
| `source-table`    | Yes      | Table name in `schema.table` format        |
| `incremental-key` | No       | Column name used for incremental ingestion |



!!! info "Core Concepts"
    

    1. **SQL Warehouses**
        * All queries run against a Databricks SQL warehouse.
        * Warehouse size and configuration impact ingestion performance.
    2. **Unity Catalog Integration**
        * Fully supported for governance and access control.
        * Catalog and schema can be specified in a URI.
    3. **Incremental Loading**
        * Supported using timestamp or sequential ID columns.
        * Common incremental column: `last_updated_at`.
        * For system usage tracking, the default incremental key is `start_time`.




