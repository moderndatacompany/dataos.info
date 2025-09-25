# MySQL

MySQL is one of the most widely used open-source relational database management systems (RDBMS). Nilus supports MySQL as a batch ingestion source, enabling you to move data efficiently into the DataOS Lakehouse or other supported destinations.

## Prerequisites

The following are the requirements for enabling Batch Data Movement in MySQL:

### **Database User Permissions**

The connection user must have the following privileges:

```sql
-- Database access
GRANT SELECT ON <database_name>.* TO '<username>'@'<host>';

-- For specific tables
GRANT SELECT ON <database_name>.<table_name> TO '<username>'@'<host>';
```

### **Pre-created PostgreSQL Depot** 

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
|   NAME     | VERSION | TYPE  | STATUS | OWNER    |
| ---------- | ------- | ----- | ------ | -------- |
| mysqldepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create the MySQL Depot:

??? note "MySQL Depot Manifest"

    ```yaml
    name: ${{mysqldepot}}
    version: v2alpha
    type: depot
    description: ${{"MYSQL Sample Database"}}
    tags:
        - ${{dropzone}}
        - ${{mysql}}
    layer: user
    depot:
      type: MYSQL
      external: ${{true}}
      secrets:
        - name: ${{mysql-instance-secret-name}}-r
          allkeys: true
        - name: ${{mysql-instance-secret-name}}-rw
          allkeys: true 
            - ${{mysql-instance-secret-name}}-rw
      mysql:
        subprotocol: "mysql"
        host: ${{host}}
        port: ${{port}}
        params: # Required
          tls: ${{skip-verify}}
    ```

    !!! info
        Update variables such as `name`, `owner`, and `layer`, and contact the DataOS Administrator or Operator to obtain the appropriate secret name.




## Sample Workflow Config

```yaml
name: nb-mysql-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for MySQL to DataOS Lakehouse
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
            cpu: 200m
            memory: 256Mi
        stackSpec:
          source:
            address: dataos://mysql_depot
            options:
              source-table: sales.orders
              incremental-key: updated_at
          sink:
            address: dataos://testawslh
            options:
              dest-table: mysql_retail.batch_orders
              incremental-strategy: replace
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```


## Supported Attribute Details 

Nilus supports the following source options for MySQL:

| `source-table`    | Yes | Name of the source table (format: `schema.table_name`) |
| ----------------- | --- | ------------------------------------------------------ |
| `incremental-key` | No  | Column for incremental ingestion                       |
| `interval-start`  | No  | Lower bound timestamp for incremental load             |
| `interval-end`    | No  | Upper bound timestamp for incremental load             |

!!! info
    MySQL supports incremental ingestion using a monotonically increasing column (e.g., updated_at). Nilus automatically filters rows between interval-start and interval-end.

