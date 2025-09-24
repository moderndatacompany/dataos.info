# Redshift

**Amazon Redshift** is a fully managed, petabyte-scale data warehouse service in AWS that allows fast query performance and scalability. Nilus supports Redshift as both a **batch ingestion source** and a **destination**, enabling seamless movement of data between Redshift and the DataOS Lakehouse or other supported sinks.

Nilus connects to Redshift either via a **direct connection URI** or through **DataOS Depot**, which centralizes authentication, credentials, and connection details.



## Prerequisites

Following are the requirements for enabling Batch Data Movement in Redshift:

### **Database User Permissions**

The Redshift user must be granted the following privileges:

```sql
-- Database-level access
GRANT USAGE ON DATABASE <database_name> TO <username>;

-- Schema-level access
GRANT USAGE ON SCHEMA <schema_name> TO <username>;

-- Table-level access
GRANT SELECT ON ALL TABLES IN SCHEMA <schema_name> TO <username>;

-- Additional
GRANT SELECT ON <schema_name>.<table_name> TO <username>;
```

### **Pre-created Redshift Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
| NAME          | VERSION | TYPE  | STATUS | OWNER    |
| ------------- | ------- | ----- | ------ | -------- |
| redshiftdepot | v2alpha | depot | active | usertest |
```

If the Depot is not created use the following manifest configuration template to create the Redshift Depot:

??? note "Redshift Depot Manifest"

    ```yaml
    name: ${{redshift-depot-name}}
    version: v2alpha
    type: depot
    tags:
        - ${{redshift}}
    description: ${{Redshift Sample data}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: REDSHIFT
      external: ${{true}}
      secrets:
        - name: ${{redshift-instance-secret-name}}-r
          allkeys: true
        - name: ${{redshift-instance-secret-name}}-rw
          allkeys: true
      redshift:
        host: ${{hostname}}
        subprotocol: ${{subprotocol}}
        port: ${{5439}}
        database: ${{sample-database}}
        bucket: ${{tmdc-dataos}}
        relativePath: ${{development/redshift/data_02/}}
    ```

    !!! info
        Update variables such as `name`, `owner`, and `layer`, and contact the DataOS Administrator or Operator to obtain the appropriate secret name.




## Sample Workflow Config

```yaml
name: nb-redshift-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for AWS Redshift to DataOS Lakehouse
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
            address: dataos://redshift_depot
            options:
              source-table: analytics.orders
              incremental-key: updated_at
          sink:
            address: dataos://testinglh
            options:
              dest-table: redshift_retail.batch_orders
              incremental-strategy: append
              aws_region: us-west-2
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attributes Details

Nilus supports the following source options for Redshift:

| Options           | Required | Description                                                 |
| ----------------- | -------- | ----------------------------------------------------------- |
| `source-table`    | Yes      | Table name (`schema.table`) or query prefixed with `query:` |
| `incremental-key` | No       | Column name for incremental ingestion                       |

!!! info
    **Incremental Loading**

    * Supported using timestamp or sequential ID columns (e.g., `updated_at`).
    * The default incremental key for usage tracking is `starttime`.


