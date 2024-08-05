# Scanning Metadata using Depot

!!! info "Information"
    This guide explains how dataOS Depots are used to connect to the metadata source and extract the metadata of various entities. It enables you to scan all datasets referenced by a depot. You need to provide the depot name or address to establish a connection to the data source.

## Scanner Workflow using a Depot

We will connect with a data source by creating a Depot and then will use the depot to scan the metadata for the entities.

### **Source Data in Snowflake**
For illustration purpose, we will connect with Snowflake data source.

![data source](/quick_guides/scan_metadata/depot/snowflake_data.png)


### **Required Permissions** 

1. To scan metadata from Snowflake source system, the Snowflake user must have USAGE privileges on required schemas.
    ![data source](/quick_guides/scan_metadata/depot/permission_snowflake.png)

2. To run the Scanner workflow, a user must have Metis admin access or a grant for the “Run as Scanner User” use case.

3. Ensure the depot for Snowflake is created and you have Read access. If not exists then create a Depot.

### **Create a Depot to Connect with Snowflake**
 
1. Create a Depot manifest file.
Here is the Depot YAML containing the `warehouse`, `URL`, and `database` to connect to Snowflake. The  Depot enables access to all schemas in the configured database. 
```yaml
version: v1
name: snowflaketest
type: depot
tags:
  - connect
  - snowflaketest
layer: user
depot:
  type: SNOWFLAKE
  description: "Snowflake Sample data"
  spec:
    warehouse: COMPUTE_WH 
    url: nu75519.central-india.azure.snowflakecomputing.com 
    database: SNOWFLAKE_SAMPLE_DATA 
  external: true 
  source: SnowflakeTestSource 
  connectionSecret: 
    - acl: rw 
      type: key-value-properties 
      data: 
        username: iamgroot 
        password: *********
```

2. Apply this YAML file on DataOS CLI

```yaml

dataos-ctl apply -f ${{path/instance_secret.yaml}}
```

### **Write Scanner Workflow**
Let us build a Scanner workflow to scan the data source. The workflow includes the `depot name` and `filter patterns`. Filter patterns enable you to control whether or not to include databases/schemas/tables as part of metadata ingestion.

1. In the YAML file, provide the workflow properties, such as version, name, description, tags, etc. 

2. Provide the depot name or address(Universal Data Link) to connect to the data source.

3. Specify `schemaFilterPattern` and `tableFilterPattern` to filter schemas/tables which are of interest. 

4. Use `includes:` and `excludes:` to specify schema/table names or a regex rule to include/exclude tables while scanning the schema.

```yaml
scannertest.yaml
              
```

<aside class="callout">
🗣 In this case, database filters are not used because the Snowflake depot is created for the specific database. To configure the depot in our DataOS cataloging structure, you will need the Snowflake source URL and the database name. (SNOWFLAKE_SAMPLE_DATA)

</aside>

# Output

## Metadata Source Created on Metis

![sfdatasource on metis.png](/quick_guides/scan_metadata/depot/snowflake_scanned.png)

## Scanned Database

![snowflake databases.png](/quick_guides/scan_metadata/depot/snowflake_databases.png)

## Scanned Tables on Metis using `includes` Filter Pattern

```yaml
sourceConfig:
  config:
    schemaFilterPattern:
      includes:
        - TPCH_SF1$
    tableFilterPattern: 
      includes:
        - region
        - supplier
        - Customer
        - ORDERS
```

![snowflake tables included.png](/quick_guides/scan_metadata/depot/snowflake_tables_included.png)

## Schema of the Scanned Customer Table (validate with the source)

![Cust schema on Metis.png](/quick_guides/scan_metadata/depot/cust_schema_on_metis.png)

## Scanned Tables on Metis using `excludes` Filter Pattern

```yaml
sourceConfig:
  config:
    schemaFilterPattern:
      includes:
        - TPCH_SF1$
    tableFilterPattern: 
      excludes:
        - region
        - supplier
        - Customer
        - ORDERS
```

### The metadata for all other tables was scanned.

![snowflake tables for exclude filter.png](/quick_guides/scan_metadata/depot/snowflake_tables_exclude_filter.png)

# More Examples with `regex` Filter Pattern

1. To scan all the schemas in the **SNOWFLAKE_SAMPLE_DATA** database. 
    
    ```yaml
    sourceConfig:
      config:
        ...
        schemaFilterPattern:
          includes:
            - .TPCH_.*
    ```
    

1. To scan the table `CUSTOMER` within any schema present in the **SNOWFLAKE_SAMPLE_DATA** database**.**
    
    ```yaml
    sourceConfig:
      config:
        ...
        tableFilterPattern:
          includes:
            - ^CUSTOMER$
    ```
    
2. To scan the table with the name `CUSTOMER` within the  `TPCH_SF100`schema present in the **SNOWFLAKE_SAMPLE_DATA** database**.**
    
    ```yaml
    sourceConfig:
      config:
        ...
        useFqnForFiltering: true
        tableFilterPattern:
          includes:
            - .*\.TPCD_SF100\.CUSTOMER$
    ```


