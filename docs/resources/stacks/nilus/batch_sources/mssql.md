# MS SQL Server

Microsoft SQL Server is a widely used enterprise relational database management system (RDBMS) known for its performance, security, and integration with Microsoft services. Nilus supports SQL Server as a batch ingestion source, allowing users to move data efficiently into the DataOS Lakehouse or other supported destinations.

## Prerequisites

Following are the requirements for enabling Batch Data Movement in MS SQL Server:

### **Database User Permissions**

The connection user must be granted the following permissions:

```sql
GRANT CONNECT ON DATABASE [database_name] TO [username];
GRANT SELECT ON SCHEMA::[schema_name] TO [username];
GRANT SELECT ON [schema_name].[table_name] TO [username];
```

### **Pre-created SQL Server Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
|    NAME    | VERSION | TYPE  | STATUS | OWNER    |
| ---------- | ------- | ----- | ------ | -------- |
| mssqldepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create the MS SQL Server Depot:

??? note "MS SQL Depot Manifest"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    description: ${{description}}
    tags:
        - ${{tag1}}
        - ${{tag2}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: JDBC                                       
      external: ${{true}}
      compute: ${{runnable-default}}
      jdbc:
        subprotocol: ${{sqlserver}}
        host: ${{host}}
        port: ${{port}}
        database: ${{database}}
      secrets:
        - name: ${{instance-secret-name}}-r
          allkeys: true
        - name: ${{instance-secret-name}}-rw
          allkeys: true
    ```

    !!! info
        Update variables such as `name`, `owner`, `compute`, `layer`,`host`, `port`, `database` etc., and contact the DataOS Administrator or Operator to obtain the appropriate secret name.




SQL Server also supports Azure Active Directory (AAD) authentication, allowing integration with enterprise identity management systems. For Example:

```bash
mssql://<username>:<token>@<host>:<port>/<database-name>?Authentication=ActiveDirectoryAccessToken
```




## Sample Workflow Config

```yaml
name: nb-mssql-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for SQL Server to DataOS Lakehouse
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
            address: dataos://mssqldepot
            options:
              source-table: sales.orders
              incremental-key: LastModifiedDate
          sink:
            address: dataos://testinglh
            options:
              dest-table: mssql_retail.batch_orders
              incremental-strategy: replace
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attribute Details

Nilus supports the following source options for MSSQL Server:

| Option            | Required | Description                              |
| ----------------- | -------- | ---------------------------------------- |
| `source-table`    | Yes      | Table name in format `schema.table_name` |
| `incremental-key` | No       | Column used for incremental loading      |
| `interval-start`  | No       | Start timestamp for incremental load     |
| `interval-end`    | No       | End timestamp for incremental load       |

!!! info  "Nilus Incremental Loading for MSSQL Server"

    Nilus supports incremental loading for MSSQL Server using a monotonically increasing column, such as a timestamp or sequential ID. This allows Nilus to efficiently track and load new or updated rows based on value changes in this field.

