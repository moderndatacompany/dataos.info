# Azure Synapse

**Azure Synapse Analytics** is a cloud-based analytics service that integrates data warehousing and big data analytics.

Nilus supports Synapse as a **batch ingestion source** and **sink**, allowing seamless data movement between **Serverless SQL Pools** or **Dedicated SQL Pools** and the DataOS Lakehouse or other supported destinations.

## Prerequisites

The following are the requirements for enabling Batch Data Movement in Azure Synapse:

### **Authentication Method**

Nilus supports the following authentication methods:

* **SQL Authentication** (username/password)
* **Azure AD Access Token**
* **Managed Identity** (for integrated authentication)

### **Required Parameters**

The following are the required parameters:

* `username` : SQL or Azure AD user
* `password` : Password (for SQL authentication)
* `server` : Synapse workspace hostname
* `database` : Target database
* `driver` : ODBC driver (default: ODBC Driver 18 for SQL Server)

### **Required Permissions**

The following are the essential permissions:

* Database-level **CONNECT** and **USAGE**
* Schema-level **SELECT**
* Table-level **SELECT**

### **Pre-created Azure Synapse Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
|     NAME     | VERSION | TYPE  | STATUS | OWNER    |
| ------------ | ------- | ----- | ------ | -------- |
| synapsedepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create the MS SQL Server Depot:

??? note "Azure Synapse Depot Manifest"

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
        subprotocol: sqlserver
        host: synapse-test-batch.sql.azuresynapse.net   
        port: ${port}
        database: ${{database}}
      secrets:
        - name: ${{instance-secret-name}}-r
          allkeys: true
        - name: ${{instance-secret-name}}-rw
          allkeys: true
    ```

    !!! info
        * **Question:** What is the server name for synapse-test-batch?\
        **Answer:** The server name is defined by Starbust as `yourserver-ondemand.sql.azuresynapse.net`
        * Update variables such as `name`, `owner`, `compute`, `layer`,`host`, `port`, `database` etc., and contact the DataOS Administrator or Operator to obtain the appropriate secret name.


Nilus can also be directly connected to Synapse using a connection URI, enabling seamless integration with enterprise identity management systems. 
For instance:


```yaml
mssql://<username>:<token>@<host>:<port>/<database-name>?Authentication=ActiveDirectoryAccessToken
```

OR

```yaml
mssql://user:password@workspace.sql.azuresynapse.net:1433/database
```


## Sample Workflow Config

```yaml
name: nb-synapse-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for Azure Synapse to DataOS Lakehouse
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
            address: dataos://synapse_depot
            options:
              source-table: sales.orders
              incremental-key: modified_date
          sink:
            address: dataos://testawslh
            options:
              dest-table: synapse_retail.batch_orders
              incremental-strategy: append
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attribute Details

Nilus supports the following source options for Azure Synapse:

| Option            | Required | Description                           |
| ----------------- | -------- | ------------------------------------- |
| `source-table`    | Yes      | Table name (`schema.table`)           |
| `incremental-key` | No       | Column used for incremental ingestion |

!!! info "Core Concepts"
    

    1. **Serverless SQL Pool**
           1. Pay-per-query pricing model.
           2. Direct query execution over data in Azure Data Lake.
           3. Best suited for ad-hoc analytics and cost-sensitive workloads.
    2. **Dedicated SQL Pool**
           1. Pre-provisioned, scalable compute resources.
           2. Optimized for high-performance workloads.
           3. Supports distribution strategies, columnstore indexes, and workload isolation.
    3. **Incremental Loading**
           1. Supported using timestamp or sequential ID columns.
           2. Common key: `modified_date` or `last_updated_at`.


