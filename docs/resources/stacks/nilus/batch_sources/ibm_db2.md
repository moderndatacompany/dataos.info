---
search:
  exclude: true
---

# IBM DB2

!!! Warning
    IBM Db2 is not supported for Batch.



<!-- IBM Db2 is a relational database known for its high performance, scalability, and enterprise-grade reliability. Nilus supports Db2 as a **batch ingestion source**, enabling users to move data into the DataOS Lakehouse or other supported destinations.

!!! info
    IBM Db2 is not supported via Depot.


## Prerequisites 

The following are the requirements for enabling Batch Data Movement in IBM DB2:

### **Database User Permissions**

The connection user must have the following privileges on the source collection:

```sql
GRANT CONNECT ON DATABASE TO USER <username>;
GRANT SELECT ON TABLE <schema>.<table> TO USER <username>;
GRANT EXECUTE ON PACKAGE <package> TO USER <username>;
```

## Sample Workflow Config

```yaml
name: nb-db2-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for Db2 to DataOS Lakehouse
workspace: research
workflow:
  dag:
    - name: nb-job-01
      spec:
        stack: nilus:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
        logLevel: INFO
        stackSpec:
          source:
            address: dataos://db2depot
            options:
              source-table: "RETAIL.CUSTOMER"
              incremental-key: LAST_UPDATE_TS
          sink:
            address: dataos://testinglh
            options:
              dest-table: db2_retail.batch_customer
              incremental-strategy: replace

```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


## Supported Attribute Details

Nilus supports the following source options for IBM DB2:

| Option            | Required | Description                                              |
| ----------------- | -------- | -------------------------------------------------------- |
| `source-table`    | Yes      | Name of the source table in format `SCHEMA.TABLE`        |
| `incremental-key` | No       | Column used for incremental batch ingestion              |
| `interval-start`  | No       | Optional lower bound timestamp for incremental ingestion |
| `interval-end`    | No       | Optional upper bound timestamp for incremental ingestion |

!!! info
    Nilus supports incremental batch ingestion by using a monotonically increasing column (e.g., `LAST_UPDATE_TS`) to track new or updated rows.

    * The column must be indexed
    * The column must not be nullable
    -->
