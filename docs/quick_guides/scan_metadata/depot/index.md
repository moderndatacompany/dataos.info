# Scanning Metadata using Depot

!!! info "Information"
    This guide explains the steps to create a Scanner Workflow using DataOS Depot to connect to the metadata source and extract the metadata of various entities. It enables you to scan all datasets referenced by a Depot. 

## Quick Steps

Follow the below steps:

<center>
<div style="text-align: center;">
<img src="/quick_guides/scan_metadata/depot/4_scan_depot.png" alt="Steps to create Scanner Workflow" style="border: 1px solid black;">
</div>
</center>

## Scanner Workflow using a Depot
You need to provide the Depot name or address to establish a connection to the data source.

### **Source Data in Snowflake**
For illustration purposes, we will connect with the Snowflake data source.

![data source](/quick_guides/scan_metadata/depot/snowflake_data.png)


### **Step 1: Check Required Permissions** 

1. To scan metadata from the Snowflake source system, the Snowflake user must have USAGE privileges on required schemas.
   ![data source](/quick_guides/scan_metadata/depot/permission_snowflake.png)

    <aside class="callout">  
     The required permissions and privileges will change according to the data source. For more about data source-specific permissions, refer to the [Scanner](/resources/stacks/scanner/#supported-data-sources) documentation.

    </aside>

2. To run the Scanner workflow, a user must have Metis admin access or a grant for the “Run as Scanner User” use case.

3. Ensure the Depot for Snowflake is created and you have Read access. If it does not exist, then create a Depot.

### **Step 2: Create a Depot to Connect with Snowflake**
We will connect with a data source by creating a Depot and then will use the Depot to scan the metadata for the entities.
 
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

### **Step 3: Write Scanner Workflow with Filter Patterns**
Let us build a Scanner workflow to scan the data source. The workflow includes the `depot name` and `filter patterns`. Filter patterns enable you to control whether or not to include databases/schemas/tables as part of metadata ingestion.

1. Provide the workflow properties, such as version, name, description, tags, etc., in the YAML file.  

2. Provide the Depot name or address(Universal Data Link) to connect to the data source.

3. Specify `schemaFilterPattern` and `tableFilterPattern` to filter schemas/tables which are of interest. 

4. Use `includes:` and `excludes:` to specify schema/table names or a regex rule to include/exclude tables while scanning the schema.

```yaml
version: v1
name: snowflake-scanner-test                               
type: workflow
tags:
  - snowflake-scanner-test
description: The workflow scans the schema of tables and registers their metadata
workflow:
  dag:
    - name: scanner2-snowflake
      description: The job scans schema from sanity snowflake Depot tables and registers their metadata on metis2
      spec:
        stack: scanner:2.0                            
        compute: runnable-default
        stackSpec:
          depot: snowflaketestsource 
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

<aside class="callout">
🗣 In this case, database filters are not used because the Snowflake Depot is created for the specific database. To configure the Depot in our DataOS cataloging structure, you will need the Snowflake source URL and the database name. (SNOWFLAKE_SAMPLE_DATA)

</aside>

### **Step 4: Check Metadata Source Created on Metis**

On Metis UI, go to Settings > Databases to access it.

![sfdatasource on metis.png](/quick_guides/scan_metadata/depot/snowflake_scanned.png)

**Scanned Database**

Click on the database.

![snowflake databases.png](/quick_guides/scan_metadata/depot/snowflake_databases.png)

**Scanned Tables on Metis using `includes` Filter Pattern**

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

**Schema of the Scanned Customer Table (validate with the source)**

![Cust schema on Metis.png](/quick_guides/scan_metadata/depot/cust_schema_on_metis.png)

**Scanned Tables on Metis using `excludes` Filter Pattern**

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

The metadata for all other tables was scanned.

![snowflake tables for exclude filter.png](/quick_guides/scan_metadata/depot/snowflake_tables_exclude_filter.png)

## More Examples with `regex` Filter Pattern

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


To know more about how to specify filters in different scenarios, refer to [Filter Pattern Examples](/resources/stacks/scanner/creating_scanner_workflows/filter_pattern_examples/).

## Scheduling Scanner Workflow Run

Scanner workflows are either single-time run or scheduled to run at a specific cadence. To schedule a workflow, you must add the schedule property defining a cron in `workflow` section.
```yaml
workflow:
  title: scheduled Scanner Workflow
  schedule: 
    cron: '*/2 * * * *'  #every 2 minute  [Minute, Hour, day of the month ,month, dayoftheweek]
    concurrencyPolicy: Allow #forbid/replace
    endOn: 2024-11-01T23:40:45Z
    timezone: Asia/Kolkata
```
To learn more about these properties, refer to [Schedulable workflows](/resources/workflow/how_to_guide/scheduled_workflow/).