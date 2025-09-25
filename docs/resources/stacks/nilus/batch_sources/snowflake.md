# Snowflake

Snowflake is a cloud-native data warehouse known for its elasticity, scalability, and ability to handle structured and semi-structured data. Nilus supports Snowflake as both a **batch ingestion source** and a **destination**, enabling seamless data movement between Snowflake and the DataOS Lakehouse or other supported systems.



## Prerequisites

The following are the requirements for enabling Batch Data Movement in Snowflake:

### **Database User Permissions**

The Snowflake user must be granted the following privileges:

```sql
-- Database access
GRANT USAGE ON DATABASE <database_name> TO <username>;
GRANT USAGE ON SCHEMA <schema_name> TO <username>;
GRANT SELECT ON ALL TABLES IN SCHEMA <schema_name> TO <username>;

-- Warehouse access
GRANT USAGE ON WAREHOUSE <warehouse_name> TO <username>;

-- Role requirements
GRANT ROLE <role_name> TO USER <username>;
```

### **Pre-created Snowflake Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
|      NAME      | VERSION | TYPE  | STATUS | OWNER    |
| -------------- | ------- | ----- | ------ | -------- |
| snowflakedepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create the Snowflake Depot:

??? note "Snowflake Depot Manifest"

    ```yaml
    name: ${{snowflake-depot}}
    version: v2alpha
    type: depot
    description: ${{snowflake-depot-description}}
    tags:
        - ${{tag1}}
        - ${{tag2}}
    layer: user
    depot:
      type: snowflake
      external: true
      secrets:
        - name: ${{snowflake-instance-secret-name}}-r
          allkeys: true
        - name: ${{snowflake-instance-secret-name}}-rw
          allkeys: true
      snowflake:
        warehouse: ${{warehouse-name}}
        url: ${{snowflake-url}}
        database: ${{database-name}}
        account: ${{account-name}}
        role: ${{snowflake-role}} # optional but recommended
        schema: ${{schema-name}}
    ```

    !!! info
        Update variables such as `name`, `owner`, and `layer`, and contact the DataOS Administrator or Operator to obtain the appropriate secret name.




## Sample Workflow Config

```yaml
name: snowflake-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for Snowflake to DataOS Lakehouse
workspace: public
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
            address: dataos://snowflake_depot
            options:
              source-table: analytics.orders
              incremental-key: LAST_MODIFIED_AT
          sink:
            address: dataos://lakehouse
            options:
              dest-table: snowflake_retail.batch_orders
              incremental-strategy: append
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.

Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```


## Supported Attribute Details

Nilus supports the following source options for Snowflake:

| `source-table`    | Yes | Table name in format `schema.table_name`        |
| ----------------- | --- | ----------------------------------------------- |
| `incremental-key` | No  | Column used for incremental ingestion           |
| `interval-start`  | No  | Lower bound timestamp for incremental ingestion |
| `interval-end`    | No  | Upper bound timestamp for incremental ingestion |

!!! info "Core Concepts"
    

    * **Warehouse Requirement:** A running warehouse is required for all queries. Warehouse size and configuration directly affect ingestion performance.
    * **Incremental Loading:** Nilus supports incremental ingestion using a monotonically increasing column (such as `LAST_MODIFIED_AT`).

