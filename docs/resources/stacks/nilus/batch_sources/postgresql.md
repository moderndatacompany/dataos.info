# PostgreSQL

PostgreSQL is a widely adopted open-source relational database known for its reliability, scalability, and feature richness. Nilus supports PostgreSQL as a **batch ingestion source**, enabling users to move data efficiently into the DataOS Lakehouse or other supported destinations.

Nilus connects to PostgreSQL through **DataOS Depot**, which provides a managed, secure way to store and reuse connection configurations.

## Prerequisites

The following are the requirements for enabling Batch Data Movement in PostgreSQL:

### **Database User Permissions**

The connection user must have the following privileges on the source database:

```sql
GRANT CONNECT ON DATABASE <database_name> TO <username>;
GRANT SELECT ON ALL TABLES IN SCHEMA <schema_name> TO <username>;
```

### **Pre-created PostgreSQL Depot**

Ensure that a PostgreSQL Depot is already created with valid read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#expected output
INFO[0000] 🔍 get...
INFO[0000] 🔍 get...complete
| NAME             | VERSION | TYPE  | STATUS | OWNER      |
| ---------------- | ------- | ----- | ------ | ---------- |
| postgresdepot    | v2alpha | depot | active | usertest   |
```

If the Depot is not created, use the following manifest configuration template to create the PostgreSQL Depot:

??? note "PostgreSQL Depot Manifest"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    tags:
        - ${{tag1}}
        - ${{tag2}}
    layer: user
    depot:
      type: postgres
      external: true
    secrets:
        - name: ${{instance-secret-name}}-r
        allkeys: ${{true}}

        - name: ${{instance-secret-name}}-rw
        allkeys: ${{true}}
            
    ```

    !!! info
        Update variables such as `name`, `owner`, and `layer`, and contact the DataOS Administrator or Operator to obtain the appropriate secret name.




## Sample Workflow Config 

```yaml
name: nb-pg-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch workflow Sample for Postgres to S3 Lakehouse
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
            address: dataos://postgresdepot
            options:
              source-table: "public.customer"
          sink:
            address: dataos://lakehouse
            options:
              dest-table: pg_retail.batch_customer
              incremental-strategy: replace
```

!!! info
    Ensure that all placeholder values and required fields (e.g., source and sink address, source table name, primary key, etc.) are properly updated before applying the configuration to a DataOS workspace.

Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attribute Details 

Nilus supports the following source options for PostgreSQL:

| Option            | Required | Description                                                      |
| ----------------- | -------- | ---------------------------------------------------------------- |
| `source-table`    | Yes      | Name of the source table to read from                            |
| `schema`          | No       | Schema name if different from the default `public`               |
| `incremental-key` | No       | Column used for incremental batch ingestion (e.g., `updated_at`) |
| `interval-start`  | No       | Optional lower bound timestamp for incremental ingestion         |
| `interval-end`    | No       | Optional upper bound timestamp for incremental ingestion         |

!!! info
    Nilus supports incremental batch ingestion by using a column (e.g., `updated_at`) to identify new or updated rows. This reduces load on the source and ensures efficiency for large datasets.

    For incremental loads, a monotonically increasing column, either of type timestamp (such as `updated_at`) or a unique numeric sequential ID, should exist and be indexed.

