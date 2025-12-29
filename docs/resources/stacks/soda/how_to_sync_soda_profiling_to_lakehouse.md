# Syncing SODA Profiling Data to Lakehouse

SODA Stack generates data quality checks and profiling results that are published to the `systemstreams:soda/quality_profile_results_03` stream. To enable further analysis, reporting, and modeling on this profiling data, you can sync it to your Lakehouse using Flare workflows.

!!! warning
    The stream address `systemstreams:soda/quality_profile_results_03` may vary depending on the environment. Contact the DBA or a DataOS Operator to confirm the correct stream address.

This guide demonstrates three approaches to sync SODA profiling data from the stream to Iceberg tables in your Lakehouse, progressing from simple to advanced:

1. **Raw Data Sync**: Extract all SODA stream data as-is without transformation.
2. **Basic Profiling Extraction**: Extract and flatten profiling metrics for analysis.
3. **Advanced Profiling with Derived Metrics**: Extract profiling data and calculate additional quality metrics.


The Workflows below demonstrate how to extract and transform this data for different use cases.

## Approach 1: Raw Data Sync

Use this approach when you want to:

- Preserve all raw SODA stream data without any transformation.

- Perform custom analysis and transformations downstream.

- Maintain full historical data for auditing or compliance.

### **Workflow Manifest**

```yaml
name: quality-check-events-sync
version: v1
type: workflow
workflow:
  schedule:                          # Schedule workflow to run daily at 17:45
    cron: '45 17 * * *'
    concurrencyPolicy: Forbid
  dag:
    - name: dg-raw-data
      spec:
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            # Input configuration - Read quality check results from SODA
            inputs:
              - name: soda
                dataset: dataos://systemstreams:soda/quality_profile_results_03
                isStream: false
                options:
                  startingOffsets: earliest
            logLevel: INFO
            # Output configuration - Write processed results to Iceberg
            outputs:
              - name: final
                dataset: dataos://icebase:sys01/raw_data?acl=rw
                format: Iceberg
                options:
                  saveMode: overwrite
                  checkpointLocation: dataos://icebase:sys01/checkpoints/quality-checks/raw_data?acl=rw

            # Data processing pipeline
            steps:
              - sequence:
                  - name: final
                    sql: SELECT * from soda
```

### **Key Configuration Points**

| Attribute | Description |
|-----------|-------------|
| `inputs.dataset` | Source SODA stream location: `systemstreams:soda/quality_profile_results_03` |
| `inputs.isStream` | Set to `false` to read as batch; `true` for continuous streaming |
| `inputs.options.startingOffsets` | `earliest` reads all historical data; `latest` reads only new data |
| `outputs.dataset` | Target Iceberg table location in your Lakehouse |
| `outputs.saveMode` | `overwrite` replaces data; `append` adds to existing data |
| `checkpointLocation` | Required for tracking processing progress (especially for streaming) |

### **Output Schema**

The output table contains all columns from the SODA stream. The SODA stream contains nested JSON structures with comprehensive quality check and profiling information. The raw data includes columns for metadata (`__metadata`, `__key`, `__topic`, `__messageid`, `__publishtime`, `__eventtime`, `__messageproperties`), dataset identification (`depot`, `collection`, `dataset`, `defaultdatasource`, `branchname`), execution context (`username`, `jobname`, `runid`, `dataosresourceid`, `dataosrunid`, `engine`, `clustername`, `servicetype`), timing information (`scanstarttimestamp`, `scanendtimestamp`, `datatimestamp`), quality check results (`checks`, `automatedmonitoringchecks`, `haserrors`, `hasfailures`, `haswarnings`), profiling statistics (`profiling`, `metrics`), execution details (`logs`, `queries`, `definitionname`), and additional metadata (`metadata`).


??? info "Detailed explanation of each column"

    **Dataset Identification**

    - **`depot`**: Data source or depot name where the dataset resides (e.g., icebase, snowflake).
    - **`collection`**: Schema or database name containing the dataset.
    - **`dataset`**: Table or dataset name being profiled or checked.
    - **`defaultdatasource`**: Default data source connection used for the SODA scan.
    - **`branchname`**: Branch name for versioned datasets (relevant for Iceberg branch-specific scans).

    **Execution Context**

    - **`username`**: DataOS user who triggered or owns the SODA job execution.
    - **`jobname`**: Name of the SODA job or Workflow that executed the quality checks.
    - **`runid`**: Unique identifier for the specific SODA scan run.
    - **`dataosresourceid`**: DataOS resource identifier for the SODA Workflow or Worker Resource.
    - **`dataosrunid`**: DataOS-level run identifier tracking the execution across the platform.
    - **`engine`**: Query engine used to execute the checks (e.g., minerva, themis).
    - **`clustername`**: Cluster name where the SODA checks were executed.
    - **`servicetype`**: Type of service or stack used (e.g., soda, soda+python).
    - **`definitionname`**: Name of the SODA check definition file or configuration used.

    **Timing Information**

    - **`scanstarttimestamp`**: Timestamp when the SODA scan began execution.
    - **`scanendtimestamp`**: Timestamp when the SODA scan completed execution.
    - **`datatimestamp`**: Timestamp representing the data snapshot or data freshness being checked.

    **Quality Check Results**

    - **`checks`**: Nested array containing all quality check definitions and their results (pass/fail/warning).
    - **`automatedmonitoringchecks`**: Array of automated monitoring checks configured for continuous quality monitoring(cloud service checks).
    - **`haserrors`**: Boolean flag indicating if any checks encountered errors during execution.
    - **`hasfailures`**: Boolean flag indicating if any quality checks failed their assertions.
    - **`haswarnings`**: Boolean flag indicating if any checks produced warnings.

    **Profiling and Metrics**

    - **`profiling`**: Nested structure containing column-level profiling statistics (avg, min, max, stddev, distinct counts, etc.).
    - **`metrics`**: Array of calculated metrics from checks (e.g., duplicate_count, duplicate_percent, row_count).

    **Execution Details**

    - **`logs`**: Nested array containing execution logs, error messages, and debug information from the SODA scan.
    - **`queries`**: Array of SQL queries executed during the scan for checks and profiling.
    - **`metadata`**: Additional metadata about the scan configuration and environment.

    **Stream Metadata (Pulsar/Kafka)**

    - **`__metadata`**: System-level metadata for the stream message.
    - **`__key`**: Message key used for partitioning in the stream.
    - **`__topic`**: Pulsar/Kafka topic name where the message was published.
    - **`__messageid`**: Unique message identifier in the stream.
    - **`__publishtime`**: Timestamp when the message was published to the stream.
    - **`__eventtime`**: Event timestamp associated with the message (application-level time).
    - **`__messageproperties`**: Additional properties or headers attached to the stream message.


## Approach 2: Basic Profiling Extraction


Use this approach when you need:

- Flattened, tabular profiling data for easy querying.

- Column-level statistics (averages, min/max, distinct counts, missing values).

- Clean, denormalized data for BI tools and dashboards.


### **Workflow Manifest**

??? note "Example Workflow Manifest"

    ```yaml
    version: v1
    name: wf-soda-profiling-sync
    type: workflow
    workflow:
      schedule:
        cron: '0 19 * * *'                      # 7PM IST Everyday
        concurrencyPolicy: Forbid
        timezone: Asia/Kolkata
      dag:
      - name: soda-profiling-sync
        spec:
          stack: flare:7.0
          compute: runnable-default
          stackSpec:
            driver:
              coreLimit: 2000m
              cores: 1
              memory: 2000m
            executor:
              coreLimit: 4000m
              cores: 2
              instances: 2
              memory: 5000m
            job:
              explain: true
              inputs:
                - name: soda
                  dataset: dataos://systemstreams:soda/quality_profile_results_03
                  isStream: false
                  options:
                    startingOffsets: earliest
              logLevel: INFO
              outputs:
                - name: profiling_final
                  dataset: dataos://icebase:sandbox/soda_quality_checks?acl=rw
                  format: Iceberg
                  options:
                    saveMode: overwrite
                    sort:
                      mode: partition
                      columns:
                          - name: depot
                            order: desc
                          - name: collection
                            order: desc
                          - name: dataset
                            order: desc
                    iceberg:
                      partitionSpec:
                        - type: identity
                          column: depot
                        - type: identity
                          column: collection
                        - type: identity
                          column: dataset

              steps:
                - sequence:
                    - name: dropped_columns
                      sql: SELECT * from soda
                      functions:
                        - name: drop
                          columns:
                            - __eventTime
                            - __key
                            - __producer_name
                            - __messageProperties
                            - __publishTime
                            - __topic
                            - automatedMonitoringChecks
                            - clusterName
                            - dataosResourceId
                            - defaultDataSource
                            - definitionName
                            - engine
                            - hasFailures
                            - hasErrors
                            - hasWarnings
                            - logs
                            - metadata
                            - queries
                            - checks
                            - runId
                        - name: cleanse_column_names

                    - name: profiling_extracted
                      sql: select * from dropped_columns
                      functions:
                        - name: unfurl
                          expression: explode(profiling) as profiling_
                        - name: drop
                          columns:
                            - profiling
                        - name: unfurl
                          expression: profiling_.*
                        - name: drop
                          columns:
                            - profiling_
                        - name: unfurl
                          expression: explode(column_profiles) as col_prof_
                        - name: drop
                          columns:
                            - column_profiles
                        - name: unfurl
                          expression: col_prof_.*
                        - name: drop
                          columns:
                            - col_prof_
                        - name: unfurl
                          expression: profile.*
                        - name: drop
                          columns:
                            - profile

                    - name: profiling_final
                      sql: SELECT
                            scan_start_timestamp AS timestamp,
                            user_name,
                            depot,
                            collection,
                            dataset,
                            column_name,
                            row_count,
                            avg,
                            avg_length,
                            distinct,
                            min,
                            min_length,
                            max,
                            max_length,
                            missing_count,
                            stddev,
                            sum,
                            variance,
                            mins,
                            maxs,
                            frequent_values,
                            histogram
                          FROM profiling_extracted
    ```

### **Transformation Pipeline**

The workflow performs three main transformation steps:

#### Step 1: Drop Unnecessary Columns

Removes metadata and system columns that are not needed for profiling analysis:

- Event metadata (`__eventTime`, `__key`, etc.)

- Job execution details (`logs`, `runId`, etc.)

- Check definitions and results (`checks`, `queries`)

#### Step 2: Unfurl Nested Profiling Structure

Flattens the nested JSON structure using the `unfurl` function:


1. Explodes the `profiling` array to create one row per profiling result.

2. Extracts fields from `profiling_` object.

3. Explodes the `column_profiles` array to create one row per column.

4. Extracts fields from `col_prof_` object.

5. Extracts fields from the `profile` object.

#### Step 3: Select Final Columns

Projects only the required profiling metrics into a clean, flat table structure.

### **Output Schema**

| Column | Type | Description |
|--------|------|-------------|
| `timestamp` | Timestamp | When the profiling scan was executed |
| `user_name` | String | User who ran the profiling job |
| `depot` | String | Data source identifier |
| `collection` | String | Schema or database name |
| `dataset` | String | Table or dataset name |
| `column_name` | String | Column being profiled |
| `row_count` | Long | Total number of rows in the dataset |
| `avg` | Double | Average value (numeric columns) |
| `avg_length` | Double | Average length (string columns) |
| `distinct` | Long | Number of distinct values |
| `min` | String | Minimum value |
| `min_length` | Integer | Minimum length (string columns) |
| `max` | String | Maximum value |
| `max_length` | Integer | Maximum length (string columns) |
| `missing_count` | Long | Number of missing/null values |
| `stddev` | Double | Standard deviation (numeric columns) |
| `sum` | Double | Sum of values (numeric columns) |
| `variance` | Double | Variance (numeric columns) |
| `mins` | Array | List of minimum values |
| `maxs` | Array | List of maximum values |
| `frequent_values` | Map | Most frequently occurring values |
| `histogram` | Map | Distribution histogram |

### **Partitioning Strategy**

The output table is partitioned by:

- `depot`: Enables efficient filtering by data source.

- `collection`: Enables efficient filtering by schema/database.

- `dataset`: Enables efficient filtering by table.

This partitioning strategy optimizes query performance when analyzing profiling data for specific datasets.


## Approach 3: Advanced Profiling with Derived Metrics


Use this approach when you need:

- Comprehensive data quality metrics including calculated percentages.

- Duplicate detection and uniqueness analysis.

- Coefficient of variation for understanding data distribution.

- Ready-to-use metrics for quality dashboards and monitoring.

### **Workflow Manifest**

??? note "Example Workflow Manifest"

    ```yaml
    version: v1
    name: soda-profiling-sync-vs
    type: workflow
    workflow:
      schedule:
        cron: '33 12 * * *'
        concurrencyPolicy: Forbid
        timezone: Asia/Kolkata
      dag:
        - name: soda-profiling-sync-vs
          spec:
            stack: flare:7.0
            compute: runnable-default
            stackSpec:
              driver:
                coreLimit: 8000m
                cores: 1
                memory: 5000m
              executor:
                coreLimit: 8000m
                cores: 2
                instances: 2
                memory: 7000m
              job:
                explain: true
                inputs:
                  - name: soda
                    dataset: dataos://systemstreams:soda/quality_profile_results_03
                    isStream: false
                    options:
                      startingOffsets: earliest
                logLevel: INFO
                outputs:
                  - name: profiling_metrics_final
                    dataset: dataos://icebase:sandbox/soda_quality_checks_data?acl=rw
                    format: Iceberg
                    options:
                      saveMode: append
                      sort:
                        mode: partition
                        columns:
                            - name: depot
                              order: desc
                            - name: collection
                              order: desc
                            - name: dataset
                              order: desc
                      iceberg:
                        partitionSpec:
                          - type: identity
                            column: depot
                          - type: identity
                            column: collection
                          - type: identity
                            column: dataset

                steps:
                  - sequence:
                        - name: dropped_columns
                          sql: SELECT * FROM soda
                          functions:
                            - name: drop
                              columns:
                                - __eventTime
                                - __key
                                - __producer_name
                                - __messageProperties
                                - __publishTime
                                - __topic
                                - automatedMonitoringChecks
                                - clusterName
                                - dataosResourceId
                                - defaultDataSource
                                - definitionName
                                - engine
                                - hasFailures
                                - hasErrors
                                - hasWarnings
                                - logs
                                - metadata
                                - queries
                                - runId
                            - name: cleanse_column_names

                        - name: profiling_extracted
                          sql: SELECT * FROM dropped_columns
                          functions:
                            - name: unfurl
                              expression: explode(profiling) as profiling_
                            - name: drop
                              columns:
                                - profiling
                            - name: unfurl
                              expression: profiling_.*
                            - name: drop
                              columns:
                                - profiling_
                            - name: unfurl
                              expression: explode(column_profiles) as col_prof_
                            - name: drop
                              columns:
                                - column_profiles
                            - name: unfurl
                              expression: col_prof_.*
                            - name: drop
                              columns:
                                - col_prof_
                            - name: unfurl
                              expression: profile.*
                            - name: drop
                              columns:
                                - profile

                        - name: profiling_flat
                          sql: |
                            SELECT
                              job_name,
                              scan_start_timestamp AS timestamp,
                              user_name,
                              depot,
                              collection,
                              dataset,
                              row_count,
                              column_name,
                              avg,
                              stddev,
                              missing_count,
                              `distinct` AS distinct_count
                            FROM profiling_extracted

                        - name: metrics_extracted
                          sql: SELECT  depot, collection, dataset, metrics FROM dropped_columns
                          functions:
                            - name: unfurl
                              expression: explode(metrics) as metrics_
                            - name: drop
                              columns:
                                - metrics
                            - name: unfurl
                              expression: metrics_.*
                            - name: drop
                              columns:
                                - metrics_

                        - name: dup_metrics_flat
                          sql: |
                            SELECT
                              depot,
                              collection,
                              dataset,
                              regexp_extract(identity, '-([^-]+)-duplicate_(count|percent)', 1) AS column_name,
                              MAX(CASE WHEN metric_name = 'duplicate_percent' THEN CAST(value AS DOUBLE) END) AS duplicate_percent,
                              MAX(CASE WHEN metric_name = 'duplicate_count'   THEN CAST(value AS DOUBLE) END) AS duplicate_count
                            FROM metrics_extracted
                            WHERE metric_name IN ('duplicate_percent', 'duplicate_count')
                              AND regexp_extract(identity, '-([^-]+)-duplicate_(count|percent)', 1) IS NOT NULL
                            GROUP BY
                              depot, collection, dataset,
                              regexp_extract(identity, '-([^-]+)-duplicate_(count|percent)', 1)

                        - name: profiling_metrics_final
                          sql: |
                            SELECT
                              p.job_name,
                              p.timestamp,
                              p.user_name,
                              p.depot,
                              p.collection,
                              p.dataset,
                              p.column_name,
                              p.row_count,

                              CASE
                                WHEN p.row_count IS NULL OR p.row_count = 0 THEN NULL
                                ELSE (p.missing_count * 100.0) / p.row_count
                              END AS null_percent,

                              CASE
                                WHEN p.row_count IS NULL OR p.row_count = 0 THEN NULL
                                ELSE (p.distinct_count * 100.0) / p.row_count
                              END AS distinct_percent,

                              CASE
                                WHEN d.duplicate_percent IS NOT NULL
                                  THEN (1.0 - d.duplicate_percent) * 100.0
                                WHEN d.duplicate_count IS NOT NULL AND p.row_count > 0
                                  THEN (1.0 - (d.duplicate_count / p.row_count)) * 100.0
                                ELSE NULL
                              END AS uniqueness_percent,

                              CASE
                                WHEN p.avg IS NULL OR p.avg = 0 OR p.stddev IS NULL THEN NULL
                                ELSE (p.stddev * 100.0) / p.avg
                              END AS coefficient_of_variation_percent

                            FROM profiling_flat p
                            LEFT JOIN dup_metrics_flat d
                              ON  p.depot = d.depot
                              AND p.collection = d.collection
                              AND p.dataset = d.dataset
                              AND lower(p.column_name) = lower(d.column_name)
    ```

### **Transformation Pipeline**

This workflow includes five main transformation steps:

#### Step 1: Drop Unnecessary Columns

Removes metadata and system columns that are not needed for profiling analysis:

- Event metadata (`__eventTime`, `__key`, etc.)

- Job execution details (`logs`, `runId`, etc.)

- Check definitions and results (`checks`, `queries`)


#### Step 2: Extract Profiling Data

Flattens the nested JSON structure using the `unfurl` function:


1. Explodes the `profiling` array to create one row per profiling result.

2. Extracts fields from `profiling_` object.

3. Explodes the `column_profiles` array to create one row per column.

4. Extracts fields from `col_prof_` object.

5. Extracts fields from the `profile` object.


#### Step 3: Flatten Profiling Data

Creates `profiling_flat` with essential metrics:


- Job and timing information.

- Dataset identifiers.

- Core statistics (avg, stddev, missing_count, distinct_count).

#### Step 4: Extract Duplicate Metrics

Extracts duplicate detection metrics from the `metrics` array:

- Uses regex to parse column names from metric identities.

- Pivots `duplicate_percent` and `duplicate_count` into columns.

- Groups by dataset and column.

#### Step 5: Calculate Derived Metrics

Joins profiling and duplicate metrics, then calculates:

**Null Percent**: Percentage of missing/null values
```sql
(missing_count * 100.0) / row_count
```

**Distinct Percent**: Percentage of unique values
```sql
(distinct_count * 100.0) / row_count
```

**Uniqueness Percent**: Percentage of non-duplicate values
```sql
(1.0 - duplicate_percent) * 100.0
-- OR
(1.0 - (duplicate_count / row_count)) * 100.0
```

**Coefficient of Variation**: Relative measure of data dispersion
```sql
(stddev * 100.0) / avg
```

### **Output Schema**

| Column | Type | Description |
|--------|------|-------------|
| `job_name` | String | Name of the SODA job that generated the profiling |
| `timestamp` | Timestamp | When the profiling scan was executed |
| `user_name` | String | User who ran the profiling job |
| `depot` | String | Data source identifier |
| `collection` | String | Schema or database name |
| `dataset` | String | Table or dataset name |
| `column_name` | String | Column being profiled |
| `row_count` | Long | Total number of rows in the dataset |
| `null_percent` | Double | Percentage of null/missing values (0-100) |
| `distinct_percent` | Double | Percentage of distinct values (0-100) |
| `uniqueness_percent` | Double | Percentage of non-duplicate values (0-100) |
| `coefficient_of_variation_percent` | Double | Relative standard deviation as percentage |

### Use Cases for Derived Metrics

- **Null Percent**: Monitor data completeness over time
- **Distinct Percent**: Identify columns with low cardinality
- **Uniqueness Percent**: Detect increasing duplicate rates
- **Coefficient of Variation**: Assess data consistency and outliers


## Customization Guide

??? info "Customization Guide for Syncing Profiling Data"

    **Adjusting Resource Allocation**

    Modify compute resources based on data volume:

    ```yaml
    driver:
      coreLimit: 8000m      # Increase for larger datasets
      cores: 1              # Keep at 1 for driver
      memory: 5000m         # Increase if OOM errors occur

    executor:
      coreLimit: 8000m      # Increase for faster processing
      cores: 2              # Increase for parallelism
      instances: 2          # Increase for larger datasets
      memory: 7000m         # Increase if OOM errors occur
    ```

    **Changing Output Location**

    Update the output dataset path to your desired location:

    ```yaml
    outputs:
      - name: profiling_final
        dataset: dataos://icebase:your_collection/your_table?acl=rw
        format: Iceberg
    ```

    **Modifying Save Mode**

    Choose the appropriate save mode:

    ```yaml
    options:
      saveMode: overwrite   # Replace all data (full refresh)
      # OR
      saveMode: append      # Add new data (incremental)
    ```

    **Adding Custom Partitioning**

    Customize partitioning strategy for your query patterns:

    ```yaml
    iceberg:
      partitionSpec:
        - type: identity
          column: depot
        - type: days          # Time-based partitioning
          column: timestamp
        - type: truncate      # Bucket partitioning
          column: dataset
          width: 10
    ```

    **Scheduling Options**

    Enable and customize the schedule:

    ```yaml
    workflow:
      schedule:
        cron: '0 19 * * *'              # Daily at 7PM
        # cron: '0 */4 * * *'           # Every 4 hours
        # cron: '0 0 * * 0'             # Weekly on Sunday
        concurrencyPolicy: Forbid       # Prevent overlapping runs
        timezone: Asia/Kolkata          # Set your timezone
    ```

    **Filtering Source Data**

    Add filters to process only specific datasets:

    ```yaml
    steps:
      - sequence:
          - name: filtered_data
            sql: |
              SELECT * FROM soda
              WHERE depot = 'your_depot'
              AND collection = 'your_collection'
              AND scan_start_timestamp >= current_date() - INTERVAL 7 DAYS
    ```



## Best Practices

??? info "Best Practices for Syncing Profiling Data"

    **1. Start with Raw Data Sync**
    
    Begin with Approach 1 to understand the data structure, then progress to Approaches 2 or 3 based on your needs.


    **2. Use Appropriate Save Modes**
    
    - Use `overwrite` for full refreshes or when data volume is small
    
    - Use `append` with proper deduplication logic for incremental loads

    **3. Monitor Resource Usage**
    
    - Start with default resources and adjust based on actual usage
    
    - Monitor memory and CPU utilization to optimize costs

    **4. Partition Strategically**
    
    - Partition by columns frequently used in WHERE clauses
    
    - Avoid over-partitioning (too many small partitions)

    **5. Schedule Appropriately**
    
    - Align schedule with SODA profiling job frequency
    
    - Consider data freshness requirements vs. compute costs

    **6. Test Before Production**
    
    - Test workflows with `startingOffsets: latest` first
    
    - Validate output data structure and completeness
    
    - Use smaller datasets or filters during initial testing


## Troubleshooting

**Issue: Out of Memory Errors**

**Solution**: Increase driver/executor memory:
```yaml
driver:
  memory: 8000m
executor:
  memory: 10000m
```

**Issue: Slow Performance**

**Solution**: Increase parallelism:
```yaml
executor:
  cores: 4
  instances: 4
```

**Issue: Duplicate Data in Append Mode**

**Solution**: Add deduplication logic:
```sql
SELECT DISTINCT * FROM your_table
-- OR use window functions to keep latest record
```

**Issue: Missing Columns in Output**

**Solution**: Verify the source data structure and adjust the unfurl expressions to match the actual nested structure.


## Additional Links 

For more information on working with SODA Stack, see:

- [SODA Stack Overview](/resources/stacks/soda/)
- [Syncing SODA Queries Data to Lakehouse](/resources/stacks/soda/sync_queries_data_to_lakehouse/)
- [Syncing SODA Quality Check Results to Lakehouse](/resources/stacks/soda/sync_quality_checks_to_lakehouse/)
