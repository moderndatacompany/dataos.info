# Recipes of Scanner Stack

This section provides various recipes for executing the Scanner in different scenarios, offering detailed guidance on how to adapt the Scanner's functionality to specific use cases.

## Context and Problem Statement

In modern data ecosystems, enterprises require efficient mechanisms to scan, catalog, and manage metadata from various sources. Consider a scenario in which an organization is using Snowflake as a Data source for data storage and analytics. To streamline metadata ingestion, a Scanner Workflow is employed, enabling the organization to configure rules that specify which databases, schemas, and tables should be included or excluded. These configurations leverage regular expressions (regex) to define filter patterns that precisely control metadata ingestion.

Following examples provides guidance on configuring metadata filters in the Scanner Workflow manifest file. It explains how to apply regex-based filtering for databases, schemas, and tables, ensuring efficient metadata scanning.

## Example manifest configuration

Let the organization have the following structure:

```yaml
│
└─── TEST_SPORTS_RETAIL # DB Name
│   │
│   └─── PUBLIC # Schema Name
│   │   │
│   │   └─── CUSTOMER # Table Name
│   │   │
│   │   └─── CUSTOMER_ADDRESS # Table Name
│   │   │
│   │   └─── CUSTOMER_DEMOGRAPHICS # Table Name
│   │   │
│   │   └─── CALL_CENTER # Table Name
│   │
│   └─── INFORMATION # Schema Name
│       │
│       └─── ORDERS # Table Name
│       │
│       └─── REGION # Table Name
│       │
│       └─── CUSTOMER # Table Name
│
└─── RETAIL_DB # DB Name
    │
    └─── PUBLIC # Schema Name
        │
        └─── CUSTOMER_ONLINE # Table Name
        │
        └─── CUSTOMER_OFFLINE # Table Name
        │
        └─── LOYAL_CUSTOMER # Table Name
```

So the complete configuration file looks like :

```yaml
name: scanner2-snowflake-depot  # Name of the scanner workflow
version: v1  # Version of the workflow
type: workflow  # Specifies that this is a workflow
tags:
  - scanner  # Tagging as a scanner workflow
  - snowflake  # Tagging for Snowflake data source
description: The workflow scans Snowflake data source through depot scan  
# Description of the workflow

workflow:
  dag:
    - name: scanner2-snowflake-job  # Name of the scanner job
      description: The job scans schema datasets referred to by Snowflake Depot and registers in Metis2
      tags:
          - scanner2  # Tags related to the scanner job
      spec:
        stack: scanner:2.0  # Specifies the scanner stack version
        compute: runnable-default  # Defines the compute resource to be used for processing
        runAsUser: metis  # Specifies the user with execution privileges
        stackSpec:
          depot: snowflake03  # Name of the depot providing the source metadata
          sourceConfig:
            config:
              type: DatabaseMetadata  # Specifies that the source is a database metadata scan
              
              databaseFilterPattern:  # Filtering databases for metadata ingestion
                includes:
                  - ^TEST_SPORTS_RETAIL$  # Regex for including TEST_SPORTS_RETAIL database
                  - RETAIL_DB  
  # When User mention name in the filter pattern, Scanner workflow will automatically convert the name to the filter pattern considering it as a prefix so the created regex will be `^RETAIL_DB.*`
              
              schemaFilterPattern:  # Filtering schemas for metadata ingestion
                excludes:
                  - INFORMATION # Excluding INFORMATION schema 
                  
              tableFilterPattern:  # Filtering tables for metadata ingestion
                includes:
	                - .*CUSTOMER.*    # Including tables which contains CUSTOMER in their name
                
              markDeletedTables: false  # Do not mark deleted tables as soft-deleted
              includeTags: true  # Include metadata tags in the scan
              includeViews: true  # Include views in the metadata scan

```

!!! info

    Note that the filter supports regex as `includes` OR `excludes`. When a user specify a pattern in the `includes` section, the Scanner will evaluate which entities match the pattern and include them in the metadata scanning and entities that do not match the pattern will be automatically excluded. The same principle applies to the excludes section, where the Scanner excludes entities that match the specified pattern, while automatically including the rest.


By combining all three filters, user can achieve a hierarchical filtering approach that successively narrows down the scope of the metadata scanning in the Scanner Workflow. This ensures that only the desired databases, schemas, and tables are included in the Workflow based on user specified criteria. If the user do not explicitly specify any of these filters then all available entities are scanned.

## **Example Scenarios**

Let just consider a scenario where user aim to ingest metadata from a Snowflake instance that comprises multiple databases, as shown below. These databases contain various schemas and tables.

```yaml
│
└─── SNOWFLAKE # DB Name
│
└─── SNOWFLAKE_SAMPLE_DATA # DB Name
│
└─── TEST_SNOWFLAKE_DB # DB Name
│
└─── TEST_HEALTHCARE # DB Name
│
└─── TEST_SPORTS_RETAIL # DB Name
│
└─── TEST_DUMMY_DB # DB Name
│
└─── RETAIL_DB # DB Name

```

### **Database Filters**

Use `databaseFilterPattern` to determine which databases to include/exclude during metadata ingestion.

**Example 1:**

In this particular example, the objective is to ingest metadata of all databases that include the term "SNOWFLAKE" in their names. To achieve this, the filter pattern **`.*SNOWFLAKE.*`** would apply in the `includes` property. Consequently, this filter pattern will ensure the ingestion of databases such as  `SNOWFLAKE`, `SNOWFLAKE_SAMPLE_DATA` and `TEST_SNOWFLAKE_DB`.

```yaml
name: scanner2-snowflake-depot
version: v1
type: workflow
tags:
  - scanner
  - snowflake
description: The workflow scans Snowflake data source through depot scan
workflow:
  dag:
    - name: scanner2-snowflake-job
      description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
      tags:
          - scanner2
      spec:
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec:
          depot: dataos://snowflake03
          sourceConfig:
            config:
              databaseFilterPattern:
                includes:
                  - .*SNOWFLAKE.*
```

**Example 2:**

If user want to scan only databases that do not start with `SNOWFLAKE`  then the filter pattern regex applied would be `^SNOWFLAKE.*` and they will exclude `SNOWFLAKE`, `SNOWFLAKE_SAMPLE_DATA`.

```yaml
name: scanner2-snowflake-depot
version: v1
type: workflow
tags:
  - scanner
  - snowflake
description: The workflow scans Snowflake data source through depot scan
workflow:
  dag:
    - name: scanner2-snowflake-job
      description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
      tags:
          - scanner2
      spec:
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec:
          depot: dataos://snowflake03
          sourceConfig:
            config:
              databaseFilterPattern:
                excludes:
                  - ^SNOWFLAKE.*
```

**Example 3:**

In order to exclusively scan the only database with name `RETAIL_DB`, the filter pattern would be `^RETAIL_DB$`.

```yaml
name: scanner2-snowflake-depot
version: v1
type: workflow
tags:
  - scanner
  - snowflake
description: The workflow scans Snowflake data source through depot scan
workflow:
  dag:
    - name: scanner2-snowflake-job
      description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
      tags:
          - scanner2
      spec:
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec:
          depot: dataos://snowflake03
          sourceConfig:
            config:
              databaseFilterPattern:
                includes:
                  - ^RETAIL_DB$
```

**Example 4:**

When a user want to ingest metadata of all databases for which the name starts with `TEST` OR ends with `DB` , then the filter pattern applied would be `^TEST` & `DB$` in the includes property. The scanning process will include databases such as  `TEST_SNOWFLAKEDB ` `TEST_HEALTHCARE` `TEST_SPORTS_RETAIL` `TEST_DUMMY_DB` & `DUMMY_DB`.

```yaml
name: scanner2-snowflake-depot
version: v1
type: workflow
tags:
  - scanner
  - snowflake
description: The workflow scans Snowflake data source through depot scan
workflow:
  dag:
    - name: scanner2-snowflake-job
      description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
      tags:
          - scanner2
      spec:
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec:
          depot: dataos://snowflake03
          sourceConfig:
            config:
              databaseFilterPattern:
                includes: 
                  - ^SNOWFLAKE.*
                  - .*DB$
```

### **Schema Filters**

Schema filter patterns determine which schemas to include/exclude during metadata ingestion. These are just examples of schemas that could exist in a Snowflake instance, taken for demonstration purpose. The actual schemas and table names may vary based on your specific use case and requirements.

```yaml
  │
  └─── SNOWFLAKE # DB Name
  │   │
  │   └─── PUBLIC # Schema Name
  │   │
  │   └─── TPCH_SF1 # Schema Name
  │
  │   └─── TPCH_SF2 # Schema Name
  │   │
  │   └─── INFORMATION_SCHEMA # Schema Name
  │
  └─── SNOWFLAKE_SAMPLE_DATA # DB Name
  │   │
  │   └─── PUBLIC # Schema Name
  │   │
  │   └─── INFORMATION_SCHEMA # Schema Name
  │   │
  │   └─── TPCH_SF1 # Schema Name
  │   │
  │   └─── TPCH_SF10 # Schema Name
  │   │
  │   └─── TPCH_SF100 # Schema Name
```

**Example 1:**

Let's consider a scenario where user want to scan the metadata from the "public" schema present in all databases. The filter pattern would be `public`. This will include the schema `public` present in databases `SNOWFLAKE`  `SNOWFLAKE_SAMPLE_DATA`.

```yaml
name: scanner2-snowflake-depot
version: v1
type: workflow
tags:
  - scanner
  - snowflake
description: The workflow scans Snowflake data source through depot scan
workflow:
  dag:
    - name: scanner2-snowflake-job
      description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
      tags:
          - scanner2
      spec:
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec:
          depot: dataos://snowflake03
          sourceConfig:
            config:
              schemaFilterPattern:
                includes: 
                  - public
```

!!! info

    When user mention name in the filter pattern, Scanner Workflow will automatically convert the name to the filter pattern considering it as a prefix so the created regex will be `^public.*`


**Example 2:**

When user wish to exclude the schema `TPCH_SF100` from metadata scanning. As this schema is present only in one database,  `excludes` property can be used with the pattern `^TPCH_SF100$` .

```yaml
name: scanner2-snowflake-depot
version: v1
type: workflow
tags:
  - scanner
  - snowflake
description: The workflow scans Snowflake data source through depot scan
workflow:
  dag:
    - name: scanner2-snowflake-job
      description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
      tags:
          - scanner2
      spec:
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec:
          depot: dataos://snowflake03
          sourceConfig:
            config:
              schemaFilterPattern:
                excludes:
                  - ^TPCH_SF100$
```

**Example 3:**

Suppose user  intend to include all schemas that begin with the prefix "TPCH" in all databases. In this case, the appropriate regular expression (regex) to achieve this would be **`^TPCH.*`**. This regex pattern will result in the metadata scan of schemas such as `TPCH_SF1` and `TPCH_SF2` from the `SNOWFLAKE` database, as well as schemas like `TPCH_SF1`, `TPCH_SF10`, and `TPCH_SF100` from the `SNOWFLAKE_SAMPLE_DATA` database.

```yaml
name: scanner2-snowflake-depot
version: v1
type: workflow
tags:
  - scanner
  - snowflake
description: The workflow scans Snowflake data source through depot scan
workflow:
  dag:
    - name: scanner2-snowflake-job
      description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
      tags:
          - scanner2
      spec:
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec:
          depot: dataos://snowflake03
          sourceConfig:
            config:
              schemaFilterPattern:
                includes:
                  - ^TPCH*
```

**Example 4:**

Now if a user want to include only the schema TPCH\_SF1 present in all the databases but not TPCH\_SF100 or TPCH\_SF1000.

```yaml
name: scanner2-snowflake-depot
version: v1
type: workflow
tags:
  - scanner
  - snowflake
description: The workflow scans Snowflake data source through depot scan
workflow:
  dag:
    - name: scanner2-snowflake-job
      description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
      tags:
          - scanner2
      spec:
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec:
          depot: dataos://snowflake03
          sourceConfig:
            config:
              schemaFilterPattern:
                includes:
                  - ^TPCH_SF1$     # This will include all the schemas with exact name from all the databases
```

### **Table Filter pattern**

Use `tableFilterPattern` to determine which tables to include/exclude during metadata ingestion.

```yaml
│
└─── TEST_SPORTS_RETAIL # DB Name
│   │
│   └─── PUBLIC # Schema Name
│   │   │
│   │   └─── CUSTOMER # Table Name
│   │   │
│   │   └─── CUSTOMER_ADDRESS # Table Name
│   │   │
│   │   └─── CUSTOMER_DEMOGRAPHICS # Table Name
│   │   │
│   │   └─── CALL_CENTER # Table Name
│   │
│   └─── INFORMATION # Schema Name
│       │
│       └─── ORDERS # Table Name
│       │
│       └─── REGION # Table Name
│       │
│       └─── CUSTOMER # Table Name
│
└─── RETAIL_DB # DB Name
    │
    └─── PUBLIC # Schema Name
        │
        └─── CUSTOMER_ONLINE # Table Name
        │
        └─── CUSTOMER_OFFLINE # Table Name
        │
        └─── LOYAL_CUSTOMER # Table Name
```

**Example 1:**

In this example, the objective is to scan only the table with the name `CUSTOMER` from all the schemas of `TEST_SPORTS_RETAIL` database. To achieve this, the filter pattern **`^CUSTOMER$ `** can be used. By applying this pattern during the metadata scanning process, only the tables named `CUSTOMER` from the `TEST_SPORTS_RETAIL.PUBLIC` and `TEST_SPORTS_RETAIL.INFORMATION` schemas will be included.

```yaml
name: scanner2-snowflake-depot
version: v1
type: workflow
tags:
  - scanner
  - snowflake
description: The workflow scans Snowflake data source through depot scan
workflow:
  dag:
    - name: scanner2-snowflake-job
      description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
      tags:
          - scanner2
      spec:
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec:
          depot: dataos://snowflake03
          sourceConfig:
            config:
              databaseFilterPattern:
                includes:
                  - TEST_SPORTS_RETAIL   # The database filter include only the TEST_SPORTS_RETAIL database
              tableFilterPattern:
                includes:
                  - ^CUSTOMER$    # With this filter pattern only the CUSTOMER tables present in the differnt schemas of the TEST_SPORTS_RETAIL are ingested
```

**Example 2:**

In this example scenario, user want to scan all the tables having CUSTOMER in their name, filter pattern *` .*CUSTOMER.*`* will be used. This will result in scanning of all the tables such as `CUSTOMER`, `CUSTOMER_ONLINE`, `CUSTOMER_OFFLINE`, `LOYAL_CUSTOMER`, etc. from the entire database.

```yaml
name: scanner2-snowflake-depot
version: v1
type: workflow
tags:
  - scanner
  - snowflake
description: The workflow scans Snowflake data source through depot scan
workflow:
  dag:
    - name: scanner2-snowflake-job
      description: The job scans schema datasets referred to by Oracle Depot and registers in Metis2
      tags:
          - scanner2
      spec:
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec:
          depot: dataos://snowflake03
          sourceConfig:
            config:
              tableFilterPattern:
                includes:
                  - .*CUSTOMER.*
```