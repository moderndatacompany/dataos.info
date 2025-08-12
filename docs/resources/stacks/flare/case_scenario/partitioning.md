# Partitioning

Partitioning is a powerful data optimization technique used to improve query performance by physically organizing data based on the values of a specific column. Unlike simple sorting, partitioning separates records with different values into distinct data files, allowing queries to skip irrelevant files entirely.

## When to Use

Use partitioning when:

- You frequently filter data using the same column.

- The column has relatively low cardinality (i.e., limited number of distinct values).


<!-- This use case demonstrates how partitioning works in Flare when writing data to Iceberg and non-Iceberg data storage formats (e.g., Parquet and Kafka) to optimize query performance. -->

## Iceberg partitioning

- Iceberg supports partitioning based on timestamp granularity such as `year`, `month`, `day`, and `hour`, as well as categorical columns (e.g., `vendor_id`) with data types like `string`, `integer`, `long`. <!--, and potentially `double` (to be verified).--> Partitioning helps group rows together and speeds up query performance.

- Iceberg produces partition values by taking a column value and optionally transforming it. For example, it converts `timestamp` values into dates and extracts components such as `year`, `month`, `day`, `hour`, etc.

- Iceberg partition layouts can evolve as needed.

The following examples demonstrate the use of various partitioning modes.

### **Iceberg**

- Partition using type identity
    - Integer values
    - String values
- Partition using type timestamp
    - Year
    - Month
    - Day
    - Hour

**Example 1:** Partitioning by identity is used when a categorical column (e.g., `vendor_id`) is used to group data. When using an identity type, there is no need to specify the property name for the partition.

```yaml
partitionSpec:
    - type: identity    **# options tested: identity, year, month, day, hour**
      column: vendor_id # columns used - identity (vendor_id, one string column) & for rest date_col**
```

**Example 2:** In this example, partitioning is done by year using a timestamp column (`date_col`). Iceberg will automatically extract the year from the timestamp.

```yaml
partitionSpec:
    - type: year       # options tested: identity, year, month, day, hour
      column: date_col # columns used - identity (vendor_id, one string column) & for rest date_col of type timestamp
      name: year
```

**Example 3:** This example demonstrates nested partitioning, where data is first partitioned by social_class (identity type), followed by partitioning by year (`timestamp` type). The `social_class` must come first in the partition specification.

```yaml
partitionSpec:
    - type: identity  
      column: vendor_id   # columns used - identity (vendor_id, one string column) & for rest date_col**

    - type: year          # options tested: identity, year, month, day, hour
      column: date_col  
      name: year
```

## Non-Iceberg Partitioning (e.g., Parquet, Kafka)

In non-Iceberg data formats(such as `Parquet`), partitions are explicit and appear as a separate column in the table that must be supplied in every table write operation. For example, you need to provide the columns explicitly for the `year`, `month`, `hour` as a transformation from the timestamp column is not automatic.

For non-Iceberg formats such as Parquet, you are required to provide a categorical column as the partitioning criterion.

### **Parquet**

- Partition using type identity

**Example 1: Partitioning is done on identity on `vendor_id` column.**

```yaml
- sequence:
    - name: ny_taxi_ts
      outputType: Parquet
      outputOptions:
      saveMode: overwrite
      partitionBy:
        - vendor_id
  ```


Partitioned files are organized into folders based on the defined partitioning criteria. You can view them directly in the storage location or within the Workbench.

To verify the table's current partitions in Workbench, run the following command:

=== "Query"

      ```sql
      SELECT * FROM "catalog"."schema"."table$partitions"
      ```

=== "Example"

      ```sql
      SELECT * FROM "lakehouse"."retail"."city$partitions"   
      ```


## Flare Workflow for Partitioning

!!! note 

    When specifying the partition criterion for Iceberg, the 'partitionSpec' property should be defined as a child property under 'iceberg' section. Otherwise partitioning will not be performed as desired.

1. **Create the partitioning manifest file**

Use the following manifest file and make the necessary changes. 

```yaml
version: v1
name: workflow-ny-customer-partitioned-03
type: workflow
tags:
- Connect
- NY-Taxi
workspace: curriculum
description: The job ingests NY-Taxi data small files and write with partitioning on vendor_id
workflow:
  title: Connect NY Taxi
  dag:
    - name: nytaxi
      title: NY-taxi data ingester
      description: The job ingests NY-Taxi data from dropzone into raw zone
      spec:
        tags:
        - Connect
        - NY-Taxi
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
              - name: customer
                dataset: dataos://lakehouse:retail/customer?acl=r
                format: Iceberg
                isStream: false

            logLevel: INFO

            outputs:
              - name: ts_customer
                dataset: dataos://lakehouse:sample/partioning03?acl=rw
                format: Iceberg
                description: This is a customer dataset
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                        write.format.default: parquet
                        write.metadata.compression-codec: gzip
                    partitionSpec:
                      - type: identity      # options tested: string, integer, long
                        column: social_class   # columns used - identity (vendor_id, one string column)

                      - type: year      # options tested: string, integer, long
                        column: birthdate   # columns used - identity (vendor_id, one string column) 
                        name: yearly
                tags:
                    - Connect
                    - customer
                title: customer Data Partitioned Vendor

            steps:
              - sequence:
                - name: ts_customer
                  sql: SELECT *  FROM customer;
```



2. **Apply the Workflow using the following command:**

```bash
dataos-ctl resource apply  -f  <file-path>
```

3. **Get the status of the Workflow using:**

=== "Command"

      ```bash
      dataos-ctl resource get -t workflow -w <workspace_name>
      ```

=== "Example"

      For example, if your workflow is applied on sandbox (should be already existing workspace) the command will be:

      ```bash
      dataos-ctl resource get -t workflow -w sandbox
      ```


!!! tip "Best practices"

    - Choose partition keys that match your most common filter columns.

    - Avoid partitioning on high-cardinality fields (e.g., user_id, timestamp) unless combined with other strategies like bucketing.