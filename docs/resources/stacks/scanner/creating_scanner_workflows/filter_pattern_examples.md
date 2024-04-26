# Filter Pattern Examples

The scanner stack offers a range of filter patterns, including the **`Database Filter Pattern`**, **`Schema Filter Pattern`**, and **`Table Filter Pattern`** for data sources such as databases and data warehouses. Likewise, in the context of messaging pipelines, you can employ the **`topic filter pattern`**. These filters enables users to exercise control over metadata scanning.

## Filter patterns

- **`databaseFilterPattern`**: Use this pattern to filter databases at the highest level. Specify the databases you want to include or exclude based on certain criteria. This filtering step will narrow down the scope of the subsequent filtering operations.

- **`schemaFilterPattern`**: Apply this pattern to filter schemas within the selected databases from the previous step. It allows you to include or exclude specific schemas based on your requirements. This filtering further refines the scope for the final step.

- **`tableFilterPattern`**: Finally, utilize this pattern to filter tables within the selected schemas. Specify the tables you want to include or exclude based on your criteria. This filtering step operates on the remaining schemas after applying the previous two filters.

<aside class="callout">
🗣 By combining all three filters, you can achieve a hierarchical filtering approach that successively narrows down the scope of the metadata scanning in the Scanner workflow. This ensures that only the desired databases, schemas, and tables are included in the workflow based on your specified criteria. If you do not explicitly specify any of these filters then all available entities are scanned.

</aside> 

## Configure Filters in Scanner YAML

 It's important to note that filters exclusively support regular expressions. This document will guide you through the use of different filter types by providing suitable regex patterns based on the given situation. Metadata filters can be configured in Scanner YAML under the `sourceConfig` section.

```yaml
sourceConfig:
  config:
    databaseFilterPattern:
      includes:
        - database1
        - database2
      excludes:
        - database3
        - database4
    schemaFilterPattern:
      includes:
        - schema1
        - schema2
      excludes:
        - schema3
        - schema4
    tableFilterPattern:
      includes:
        - table1
        - table2
      excludes:
        - table3
        - table4
```

<aside class="callout">
🗣 Note that the filter supports regex as `includes` OR `excludes`. When you specify a pattern in the `includes` section, the Scanner will evaluate which entities match the pattern and include them in the metadata scanning and entities that do not match the pattern will be automatically excluded. The same principle applies to the excludes section, where the Scanner excludes entities that match the specified pattern, while automatically including the rest.

</aside>


## Example Scenarios

Let us consider a scenario where we aim to ingest metadata from a Snowflake instance that comprises multiple databases, as shown below. These databases contain various schemas and tables. 

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

Use `databaseFilterPattern` to determine which databases to include/exclude during metadata ingestion.

**Example 1**

 In this particular example, our objective is to ingest metadata of all databases that include the term "SNOWFLAKE" in their names. To achieve this, we would apply the filter pattern **`.*SNOWFLAKE.*`** in the `includes` property. Consequently, this filter pattern will ensure the ingestion of databases such as  `SNOWFLAKE`, `SNOWFLAKE_SAMPLE_DATA` and `TEST_SNOWFLAKE_DB`.

```yaml
    sourceConfig:
      config:
        databaseFilterPattern:
          includes:
            - .*SNOWFLAKE.*
```

**Example 2**

If we want to scan only databases that start with `SNOWFLAKE`  then the filter pattern regex applied would be `^SNOWFLAKE.*` and they will include `SNOWFLAKE`, `SNOWFLAKE_SAMPLE_DATA`.

```yaml
sourceConfig:
      config:
        databaseFilterPattern:
          includes:
            - ^SNOWFLAKE.*
```

**Example 3**

 In order to exclusively scan the only database with name `SNOWFLAKE`, the filter pattern would be `^SNOWFLAKE$`

```yaml
sourceConfig:
      config:
        databaseFilterPattern:
          includes:
            - ^SNOWFLAKE$
```

**Example 4**

In this example, we want to ingest metadata of all databases for which the name starts with `TEST` OR ends with `DB` , then the filter pattern applied would be `^TEST` & `DB$` in the includes property. The scanning process will include databases such as  `TEST_SNOWFLAKEDB` & `DUMMY_DB`.

```yaml
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

**Example 1**

Let's consider a scenario where we want to scan the metadata from the "public" schema present in all databases. The filter pattern would be `public`. This will include the schema `public` present in databases  `SNOWFLAKE`  `SNOWFLAKE_SAMPLE_DATA`.

```yaml
sourceConfig:
  config:
    schemaFilterPattern:
      includes:
        - public
```

<aside class="callout">
🗣 When you mention name in the filter pattern, Scanner workflow will automatically convert the name to the filter pattern considering it as a prefix so the created regex will be `^public.*`

</aside>

**Example 2**

We wish to exclude the schema `TPCH_SF100` from metadata scanning. As this schema is present only in one database, you can use `excludes` property with the pattern `^TPCH_SF100$` . 

```yaml
sourceConfig:
  config:
    schemaFilterPattern:
      excludes:
        - ^TPCH_SF100$
```

**Example 3**

Suppose we intend to include all schemas that begin with the prefix "TPCH" in all databases. In this case, the appropriate regular expression (regex) to achieve this would be **`^TPCH.*`**. This regex pattern will result in the metadata scan of schemas such as `TPCH_SF1` and `TPCH_SF2` from the `SNOWFLAKE` database, as well as schemas like `TPCH_SF1`,  `TPCH_SF10`,  and `TPCH_SF100` from the `SNOWFLAKE_SAMPLE_DATA` database.

```yaml
sourceConfig:
  config:
    ...
    schemaFilterPattern:
      includes:
        - ^TPCH*
```

**Example 4**

We want to include only the schema TPCH_SF1 present in all the databases but not TPCH_SF100 or TPCH_SF1000.

```yaml
sourceConfig:
  config:
    ...
    schemaFilterPattern:
      includes:
        - ^TPCH_SF1$
```

### **Table Filter pattern**

Use `tableFilterPattern` to determine which tables to include/exclude during metadata ingestion.

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

**Example 1**

In this example, our objective is to scan only the table with the name `CUSTOMER` from all the schemas of `TEST_SPORTS_RETAIL` database. To achieve this, we can use the filter pattern **`^CUSTOMER$`**. By applying this pattern during the metadata scanning process, the tables named `CUSTOMER` from the `TEST_SPORTS_RETAIL.PUBLIC` and `TEST_SPORTS_RETAIL.INFORMATION` schemas will be included.

```yaml
sourceConfig:
  config:
    ...
    databaseFilterPattern:
      includes:
        - TEST_SPORTS_RETAIL 
    tableFilterPattern:
      includes:
        - ^CUSTOMER$
```

**Example 2**

In this example scenario, we want to scan all the tables having CUSTOMER in their name. We will use the filter pattern .*CUSTOMER.*.  This will result in scanning of all the tables such as `CUSTOMER`, `CUSTOMER_ONLINE`, `CUSTOMER_OFFLINE`, `LOYAL_CUSTOMER`, etc.

```yaml
sourceConfig:
  config:
    ...
    tableFilterPattern:
      includes:
        - .*CUSTOMER.*
```