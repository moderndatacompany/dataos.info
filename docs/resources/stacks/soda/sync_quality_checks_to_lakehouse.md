# Syndicating Soda Quality Check Results

Soda Stack performs data quality checks and writes the results to the `systemstreams:soda/quality_profile_results_03` stream , which are also populated on [Metis UI](/interfaces/metis/metis_ui_assets/metis_assets_tables/#data-quality).

These results can be syndicated to any external storage system, including Snowflake, Redshift, or PostgreSQL, depending on the integration needs. The steps below illustrate this process using a Lakehouse implementation. 

!!! info
    The stream address `systemstreams:soda/quality_profile_results_03` may vary depending on the environment. Contact the Database Administrator or a DataOS Operator to confirm the correct stream address.



By syndicating quality check results to Lakehouse, you can:

- Track data quality trends over time across all datasets.
- Build comprehensive data quality dashboards and scorecards.
- Monitor check outcomes (pass/fail/warning) for SLA compliance.
- Analyze metric values to understand data quality patterns.


## Understanding Quality Check Data

Soda quality checks validate data against defined rules and constraints. Each check execution generates:

- **Check Definition**: The specific quality rule being validated (e.g., "row_count between 100 and 1000")
- **Check Outcome**: Result status (passed, failed, warning)
- **Metrics**: Measured values (e.g., actual row count, missing count, duplicate count)
- **Category**: Type of quality check (Completeness, Accuracy, Validity, Uniqueness, Freshness, Schema)
- **Context**: Dataset identification (depot, collection, dataset, column)

This workflow extracts these elements from the nested Soda stream format and transforms them into a clean, queryable table structure.


## Workflow Architecture

The quality check sync workflow follows a five-stage transformation pipeline:

```
Soda Stream (Raw Data)
        ↓
[Step 1] Drop Unnecessary Columns
        ↓
[Step 2] Extract & Flatten Check Information
        ↓
[Step 3] Extract & Flatten Metrics Information
        ↓
[Step 4] Join Checks with Metrics
        ↓
[Step 5] Extract Category & Final Transformation
        ↓
Lakehouse (Iceberg Table)
```

---

## Complete Workflow Manifest

```yaml
# Quality Check Events Workflow
# Purpose: Process and aggregate quality check results from Soda stream into Lakehouse
name: quality-check-events-sync
version: v1
type: workflow
workflow:
  # Schedule workflow to run daily at 17:45
  schedule:
    cron: '45 17 * * *'
    concurrencyPolicy: Forbid
  dag:
    - name: dg-quality-cm-data
      spec:
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            # Input configuration - Read quality check results from Soda
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
                dataset: dataos://lakehouse:sys01/slo_quality_checks?acl=rw
                format: Iceberg
                options:
                  saveMode: overwrite
                  checkpointLocation: dataos://lakehouse:sys01/checkpoints/quality-checks/v1000?acl=rw
                  # Configure sorting by depot, collection, and dataset
                  sort:
                    mode: partition
                    columns:
                        - name: depot
                          order: desc
                        - name: collection
                          order: desc
                        - name: dataset
                          order: desc
                  # Configure Iceberg partitioning
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: depot
                      - type: identity
                        column: collection
                      - type: identity
                        column: dataset
            # Data processing pipeline
            steps:
              - sequence:
                  # Step 1: Remove system and unnecessary columns
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
                          - profiling
                          - queries
                          - runId
                      - name: cleanse_column_names

                  # Step 2: Extract and process check information
                  - name: checks_extracted
                    sql: select * from dropped_columns
                    functions:
                      - name: unfurl
                        expression: explode(checks) as checks_
                      - name: drop
                        columns:
                          - checks
                      - name: rename_all
                        columns:
                          metrics: metrics_value
                      - name: unfurl
                        expression: checks_.*
                      - name: drop
                        columns:
                          - checks_
                      - name: unfurl
                        expression: explode(metrics) as metrics_
                      - name: drop
                        columns:
                          - metrics

                  # Step 3: Extract and process metrics information
                  - name: metrics_extracted
                    sql: select dataos_run_id, metrics_value from checks_extracted
                    functions:
                      - name: unfurl
                        expression: explode(metrics_value) as metrics_value_
                      - name: drop
                        columns:
                          - metrics_value
                      - name: unfurl
                        expression: metrics_value_.*
                      - name: drop
                        columns:
                          - metrics_value_

                  # Step 4: Join checks and metrics data
                  - name: joined_checks_metrics
                    sql: |
                      SELECT
                        ce.dataos_run_id,
                        ce.job_name,
                        ce.scan_start_timestamp as timestamp,
                        ce.user_name,
                        ce.depot,
                        ce.collection,
                        ce.dataset,
                        ce.column,
                        ce.name as check_definition,
                        me.metric_name,
                        me.value as metric_value,
                        ce.outcome as check_outcome,
                        ce.resource_attributes as resource_attributes
                      FROM checks_extracted ce
                      LEFT JOIN metrics_extracted me
                        ON ce.dataos_run_id = me.dataos_run_id
                        AND ce.metrics_ = me.identity

                  # Step 5: Final transformation with category extraction
                  - name: final
                    sql: |
                      SELECT
                        dataos_run_id,
                        job_name,
                        timestamp,
                        user_name,
                        depot,
                        collection,
                        dataset,
                        column,
                        check_definition,
                        resource_attributes,
                        metric_name,
                        metric_value,
                        check_outcome,
                        attribute['value'] AS category
                      FROM joined_checks_metrics
                      LATERAL VIEW explode(resource_attributes) AS attribute
                      WHERE attribute['name'] = 'category'
```


## Configuration Breakdown

**Input Configuration**

```yaml
inputs:
  - name: soda
    dataset: dataos://systemstreams:soda/quality_profile_results_03
    isStream: false
    options:
      startingOffsets: earliest
```

**Key Points:**

- **`isStream: false`**: Processes all available data in batch mode for complete historical view
- **`startingOffsets: earliest`**: Reads all quality check results from the beginning of the stream

Use `startingOffsets: latest` for incremental processing of only new check results and `isStream: true` for continuous real-time processing (with appropriate checkpoint location).

**Output Configuration**

```yaml
outputs:
  - name: final
    dataset: dataos://lakehouse:sys01/slo_quality_checks_a?acl=rw
    format: Iceberg
    options:
      saveMode: overwrite
      checkpointLocation: dataos://lakehouse:sys01/checkpoints/quality-checks/v1000_a?acl=rw
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
```

**Key Points:**

- **`saveMode: overwrite`**: Replaces all data on each run (use `append` for incremental updates)
- **`checkpointLocation`**: Tracks processing progress; essential for exactly-once processing guarantees
- **Sorting**: Data is sorted within partitions by depot → collection → dataset for optimized query performance
- **Partitioning**: Three-level hierarchical partitioning enables efficient filtering:
    - Filter by `depot` → scans only relevant data source partitions
    - Filter by `collection` → scans only relevant schema/database partitions
    - Filter by `dataset` → scans only relevant table partitions



## Transformation Pipeline

### **Step 1: Drop Unnecessary Columns**

```yaml
- name: dropped_columns
  sql: SELECT * from soda
  functions:
    - name: drop
      columns:
        - __eventTime              # Stream event timestamp
        - __key                    # Stream message key
        - __producer_name          # Producer identifier
        - __messageProperties      # Message metadata
        - __publishTime            # Stream publish time
        - __topic                  # Pulsar topic name
        - automatedMonitoringChecks  # Automated monitoring data
        - clusterName              # Execution cluster
        - dataosResourceId         # DataOS resource ID
        - defaultDataSource        # Data source config
        - definitionName           # Check definition file
        - engine                   # Query engine used
        - hasFailures              # Boolean flag (redundant)
        - hasErrors                # Boolean flag (redundant)
        - hasWarnings              # Boolean flag (redundant)
        - logs                     # Execution logs
        - metadata                 # Additional metadata
        - profiling                # Profiling data (not needed for checks)
        - queries                  # SQL queries executed
        - runId                    # Run identifier
    - name: cleanse_column_names
```

This step removes columns that are not needed for quality check analysis:

- **Stream Metadata** (`__eventTime`, `__key`, `__topic`, etc.): System-level metadata from the Pulsar stream
- **Execution Metadata** (`clusterName`, `engine`, `runId`, etc.): Job execution details that don't add value to check analysis
- **Redundant Flags** (`hasFailures`, `hasErrors`, `hasWarnings`): Boolean flags that are derived from check outcomes
- **Profiling Data** (`profiling`): This workflow focuses on checks, not profiling statistics
- **Verbose Data** (`logs`, `queries`, `metadata`): Detailed execution information that clutters the output

The `cleanse_column_names` function standardizes column naming conventions (e.g., converting camelCase to snake_case).



### **Step 2: Extract and Process Check Information**

```yaml
- name: checks_extracted
  sql: select * from dropped_columns
  functions:
    - name: unfurl
      expression: explode(checks) as checks_
    - name: drop
      columns:
        - checks
    - name: rename_all
      columns:
        metrics: metrics_value
    - name: unfurl
      expression: checks_.*
    - name: drop
      columns:
        - checks_
    - name: unfurl
      expression: explode(metrics) as metrics_
    - name: drop
      columns:
        - metrics
```

This is the core transformation that flattens the nested check structure. Let's break it down:

**Explode Checks Array**

```yaml
- name: unfurl
  expression: explode(checks) as checks_
```

- One Soda scan can execute multiple quality checks
- `explode(checks)` creates one row per check execution
- **Example**: If a scan runs 5 checks, this creates 5 rows

**Rename Metrics Column**

```yaml
- name: rename_all
  columns:
    metrics: metrics_value
```

- The `checks` object has a `metrics` field (array of metric identifiers)
- We rename it to `metrics_value` to avoid naming conflicts
- This allows us to later join with the actual metric values

**Unfurl Check Object**

```yaml
- name: unfurl
  expression: checks_.*
```

- Extracts all fields from the `checks_` object into separate columns
- Creates columns like: `name`, `outcome`, `column`, `resource_attributes`, `metrics_value`, etc.
- **Example Output Columns**:
    - `name`: "row_count between 100 and 1000"
    - `outcome`: "passed"
    - `column`: "customer_id"
    - `resource_attributes`: [{name: "category", value: "Accuracy"}]

**Explode Metrics Array**

```yaml
- name: unfurl
  expression: explode(metrics) as metrics_
```

- The `metrics_value` field is an array of metric identifiers (strings)
- Each identifier references a metric in the separate `metrics` array
- `explode(metrics)` creates additional rows if a check uses multiple metrics
- **Example**: A check using both "row_count" and "missing_count" creates 2 rows

A flat table where each row represents one check execution for one metric identifier.


### **Step 3: Extract and Process Metrics Information**

```yaml
- name: metrics_extracted
  sql: select dataos_run_id, metrics_value from checks_extracted
  functions:
    - name: unfurl
      expression: explode(metrics_value) as metrics_value_
    - name: drop
      columns:
        - metrics_value
    - name: unfurl
      expression: metrics_value_.*
    - name: drop
      columns:
        - metrics_value_
```

This step extracts the actual metric values from the `metrics_value` array (which was originally the `metrics` array from the root level, not from checks). In the Soda stream structure:

- **`checks[].metrics`**: Contains metric *identifiers* (strings like "dataset-row_count")
- **`metrics[]`**: Contains actual metric *values* (objects with metric_name, value, identity)

We need to extract both and join them by their identity/identifier.

**Explode Metrics Array**

```yaml
- name: unfurl
  expression: explode(metrics_value) as metrics_value_
```

- Goes back to the original `metrics_value` array (from root level)
- Creates one row per metric object

**Unfurl Metric Object**

```yaml
- name: unfurl
  expression: metrics_value_.*
```

Extracts fields from each metric object:

  - `metric_name`: Name of the metric (e.g., "row_count", "missing_count")
  - `value`: The actual measured value (e.g., 1523, 45)
  - `identity`: Unique identifier to link with checks (e.g., "customer_table-row_count")

A separate table with metric details (metric_name, value, identity) linked by `dataos_run_id`.


### **Step 4: Join Checks and Metrics Data**

```yaml
- name: joined_checks_metrics
  sql: |
    SELECT
      ce.dataos_run_id,
      ce.job_name,
      ce.scan_start_timestamp as timestamp,
      ce.user_name,
      ce.depot,
      ce.collection,
      ce.dataset,
      ce.column,
      ce.name as check_definition,
      me.metric_name,
      me.value as metric_value,
      ce.outcome as check_outcome,
      ce.resource_attributes as resource_attributes
    FROM checks_extracted ce
    LEFT JOIN metrics_extracted me
      ON ce.dataos_run_id = me.dataos_run_id
      AND ce.metrics_ = me.identity
```

This critical step joins the check information with the actual metric values.

```sql
ON ce.dataos_run_id = me.dataos_run_id    -- Same scan execution
AND ce.metrics_ = me.identity              -- Matching metric identifier
```

**Example:**

- **Check Row**: check_definition="row_count > 100", metrics_="customer-row_count", outcome="passed"
- **Metric Row**: identity="customer-row_count", metric_name="row_count", value=1523
- **Joined Result**: check_definition="row_count > 100", metric_name="row_count", metric_value=1523, check_outcome="passed"


Some checks may not have associated metrics (e.g., schema checks, freshness checks that don't compute numeric values). LEFT JOIN ensures we keep all checks even if metrics are missing.

This step gives a unified table with check definitions, their outcomes, and the actual metric values measured.


### **Step 5: Extract Category and Final Transformation**

```yaml
- name: final
  sql: |
    SELECT
      dataos_run_id,
      job_name,
      timestamp,
      user_name,
      depot,
      collection,
      dataset,
      column,
      check_definition,
      resource_attributes,
      metric_name,
      metric_value,
      check_outcome,
      attribute['value'] AS category
    FROM joined_checks_metrics
    LATERAL VIEW explode(resource_attributes) AS attribute
    WHERE attribute['name'] = 'category'
```

This final step extracts the quality check category from the nested `resource_attributes` array.

**Understanding resource_attributes:**
```json
resource_attributes: [
  {name: "category", value: "Completeness"},
  {name: "title", value: "Ensure no missing birth dates"},
  {name: "custom_tag", value: "critical"}
]
```

**LATERAL VIEW explode() Explained:**
```sql
LATERAL VIEW explode(resource_attributes) AS attribute
```

- `explode()` creates one row per attribute in the array
- `LATERAL VIEW` allows us to reference both the original row and the exploded elements
- Each attribute becomes available as `attribute['name']` and `attribute['value']`

**Filtering for Category:**

```sql
WHERE attribute['name'] = 'category'
```

- Keeps only the row where attribute name is "category"
- Extracts the category value (Completeness, Accuracy, Validity, Uniqueness, Freshness, Schema)

The final transformation step provides a clean, flat table with all check details including the quality check category.


## Output Schema

When querying through Workbench, final output looks like following table:

| __metadata | dataos_run_id | job_name | timestamp | user_name | depot | collection | dataset | column | check_definition | resource_attributes | metric_name | metric_value | check_outcome | category |
|-----------|---------------|----------|-----------|-----------|-------|------------|---------|--------|------------------|---------------------|-------------|--------------|---------------|----------|
| {"_dataos_run_map...} | f5dwn3781ds0 | bikesales-quality | 2025-11-27T12:21:36+00:00 | iamgroot | icebase | sandbox | bikesales | sales_transaction_id | duplicate_count(sales_transaction_id) = 0 | [{"name":"category","value":"Uniqueness"},{"name":"description","value":"The sales_transaction_id column must not contain duplicate values."}] | duplicate_count | 0 | pass | Uniqueness |
| {"_dataos_run_map...} | f5dwn3781ds0 | bikesales-quality | 2025-11-27T12:21:36+00:00 | iamgroot | icebase | sandbox | bikesales | sales_transaction_id | duplicate_count(sales_transaction_id) = 0 | [{"name":"category","value":"Uniqueness"},{"name":"description","value":"The sales_transaction_id column must not contain duplicate values."}] | duplicate_count | 0 | pass | Uniqueness |
| {"_dataos_run_map...} | f5dwn3781ds0 | bikesales-quality | 2025-11-27T12:21:36+00:00 | iamgroot | icebase | sandbox | bikesales | sales_transaction_id | duplicate_count(sales_transaction_id) = 0 | [{"name":"category","value":"Uniqueness"},{"name":"description","value":"The sales_transaction_id column must not contain duplicate values."}] | duplicate_count | 0 | pass | Uniqueness |
| {"_dataos_run_map...} | f5dwn3781ds0 | bikesales-quality | 2025-11-27T12:21:36+00:00 | iamgroot | icebase | sandbox | bikesales | sales_transaction_id | duplicate_count(sales_transaction_id) = 0 | [{"name":"category","value":"Uniqueness"},{"name":"description","value":"The sales_transaction_id column must not contain duplicate values."}] | duplicate_count | 0 | pass | Uniqueness |
| {"_dataos_run_map...} | f5dwn3781ds0 | bikesales-quality | 2025-11-27T12:21:36+00:00 | iamgroot | icebase | sandbox | bikesales | sales_transaction_id | duplicate_count(sales_transaction_id) = 0 | [{"name":"category","value":"Uniqueness"},{"name":"description","value":"The sales_transaction_id column must not contain duplicate values."}] | duplicate_count | 0 | pass | Uniqueness |
| {"_dataos_run_map...} | f5dwn3781ds0 | bikesales-quality | 2025-11-27T12:21:36+00:00 | iamgroot | icebase | sandbox | bikesales | sales_transaction_id | duplicate_percent(sales_transaction_id) < 0.10 | [{"name":"category","value":"Validity"}] | duplicate_percent | 0.0 | pass | Validity |
| {"_dataos_run_map...} | f5dwn3781ds0 | bikesales-quality | 2025-11-27T12:21:36+00:00 | iamgroot | icebase | sandbox | bikesales | sales_transaction_id | duplicate_percent(sales_transaction_id) < 0.10 | [{"name":"category","value":"Validity"}] | duplicate_percent | 0.0 | pass | Validity |
| {"_dataos_run_map...} | f5dwn3781ds0 | bikesales-quality | 2025-11-27T12:21:36+00:00 | iamgroot | icebase | sandbox | bikesales | sales_transaction_id | duplicate_percent(sales_transaction_id) < 0.10 | [{"name":"category","value":"Validity"}] | duplicate_percent | 0.0 | pass | Validity |
| {"_dataos_run_map...} | f5dwn3781ds0 | bikesales-quality | 2025-11-27T12:21:36+00:00 | iamgroot | icebase | sandbox | bikesales | sales_transaction_id | duplicate_percent(sales_transaction_id) < 0.10 | [{"name":"category","value":"Validity"}] | duplicate_percent | 0.0 | pass | Validity |
| {"_dataos_run_map...} | f5dwn3781ds0 | bikesales-quality | 2025-11-27T12:21:36+00:00 | iamgroot | icebase | sandbox | bikesales | sales_transaction_id | duplicate_percent(sales_transaction_id) < 0.10 | [{"name":"category","value":"Validity"}] | duplicate_percent | 0.0 | pass | Validity |


The final output table contains the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `dataos_run_id` | String | Unique identifier for the Soda scan execution; links all checks from the same run |
| `job_name` | String | Name of the Soda job or workflow that executed the quality checks |
| `timestamp` | Timestamp | When the quality check scan was executed (from `scan_start_timestamp`) |
| `user_name` | String | DataOS user who triggered the quality check job |
| `depot` | String | Data source or depot identifier where the dataset resides (e.g., lakehouse, snowflake) |
| `collection` | String | Schema or database name containing the dataset being checked |
| `dataset` | String | Table or dataset name that was validated by the quality check |
| `column` | String | Column name being checked (NULL for dataset-level checks like row_count) |
| `check_definition` | String | The quality check rule definition (e.g., "row_count between 100 and 1000", "missing_count(email) = 0") |
| `resource_attributes` | Array | Full array of check attributes including category, title, and custom tags |
| `metric_name` | String | Name of the metric measured during the check (e.g., "row_count", "missing_count", "duplicate_count") |
| `metric_value` | Double | The actual measured value for the metric (e.g., 1523 rows, 45 missing values) |
| `check_outcome` | String | Result of the quality check: "passed", "failed", or "warning" |
| `category` | String | Quality dimension category: Completeness, Accuracy, Validity, Uniqueness, Freshness, or Schema |




<!--## Example Case Scenarios

### **1. Data Quality Dashboard**

Build a comprehensive quality dashboard:

```sql
-- Overall quality score by dataset
SELECT
  depot,
  collection,
  dataset,
  COUNT(*) as total_checks,
  SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) as passed_checks,
  SUM(CASE WHEN check_outcome = 'failed' THEN 1 ELSE 0 END) as failed_checks,
  ROUND(SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as quality_score
FROM dataos://lakehouse:sys01/slo_quality_checks_a
WHERE timestamp >= current_date() - INTERVAL 7 DAYS
GROUP BY depot, collection, dataset
ORDER BY quality_score ASC
```

### **2. Quality Trend Analysis**

Monitor quality trends over time:

```sql
-- Daily quality check pass rate
SELECT
  DATE(timestamp) as check_date,
  category,
  COUNT(*) as total_checks,
  SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) as passed_checks,
  ROUND(SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as pass_rate
FROM dataos://lakehouse:sys01/slo_quality_checks_a
WHERE timestamp >= current_date() - INTERVAL 30 DAYS
GROUP BY DATE(timestamp), category
ORDER BY check_date DESC, category
```

### **3. Failed Checks Monitoring**

Identify and investigate failed checks:

```sql
-- All failed checks in the last 24 hours
SELECT
  timestamp,
  depot,
  collection,
  dataset,
  column,
  check_definition,
  metric_name,
  metric_value,
  category
FROM dataos://lakehouse:sys01/slo_quality_checks_a
WHERE check_outcome = 'failed'
  AND timestamp >= current_timestamp() - INTERVAL 1 DAY
ORDER BY timestamp DESC
```

### **4. SLA Compliance Reporting**

Track compliance with data quality SLAs:

```sql
-- Critical checks SLA compliance (by category)
SELECT
  category,
  COUNT(*) as total_critical_checks,
  SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) as sla_compliant,
  ROUND(SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as sla_compliance_percent
FROM dataos://lakehouse:sys01/slo_quality_checks_a
WHERE timestamp >= current_date() - INTERVAL 30 DAYS
  AND check_definition LIKE '%critical%'  -- Assuming critical checks are tagged
GROUP BY category
HAVING sla_compliance_percent < 99.0  -- Alert if SLA < 99%
```

### **5. Dataset Health Scorecard**

Create a health scorecard for each dataset:

```sql
-- Dataset health by quality dimension
SELECT
  depot,
  collection,
  dataset,
  MAX(CASE WHEN category = 'Completeness' THEN
    ROUND(SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1)
  END) as completeness_score,
  MAX(CASE WHEN category = 'Accuracy' THEN
    ROUND(SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1)
  END) as accuracy_score,
  MAX(CASE WHEN category = 'Validity' THEN
    ROUND(SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1)
  END) as validity_score,
  MAX(CASE WHEN category = 'Uniqueness' THEN
    ROUND(SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1)
  END) as uniqueness_score,
  MAX(timestamp) as last_checked
FROM dataos://lakehouse:sys01/slo_quality_checks_a
WHERE timestamp >= current_date() - INTERVAL 7 DAYS
GROUP BY depot, collection, dataset
ORDER BY depot, collection, dataset
```

### **6. Anomaly Detection**

Identify unusual metric values:

```sql
-- Detect anomalies in metric values (e.g., sudden spike in missing values)
WITH metric_history AS (
  SELECT
    depot,
    collection,
    dataset,
    column,
    metric_name,
    DATE(timestamp) as check_date,
    AVG(metric_value) as avg_metric_value
  FROM dataos://lakehouse:sys01/slo_quality_checks_a
  WHERE metric_name = 'missing_count'
    AND timestamp >= current_date() - INTERVAL 30 DAYS
  GROUP BY depot, collection, dataset, column, metric_name, DATE(timestamp)
),
metric_stats AS (
  SELECT
    depot,
    collection,
    dataset,
    column,
    metric_name,
    AVG(avg_metric_value) as mean_value,
    STDDEV(avg_metric_value) as stddev_value
  FROM metric_history
  GROUP BY depot, collection, dataset, column, metric_name
)
SELECT
  mh.depot,
  mh.collection,
  mh.dataset,
  mh.column,
  mh.check_date,
  mh.avg_metric_value,
  ms.mean_value,
  ms.stddev_value,
  ROUND((mh.avg_metric_value - ms.mean_value) / NULLIF(ms.stddev_value, 0), 2) as z_score
FROM metric_history mh
JOIN metric_stats ms
  ON mh.depot = ms.depot
  AND mh.collection = ms.collection
  AND mh.dataset = ms.dataset
  AND mh.column = ms.column
  AND mh.metric_name = ms.metric_name
WHERE ABS((mh.avg_metric_value - ms.mean_value) / NULLIF(ms.stddev_value, 0)) > 3  -- 3 sigma anomaly
ORDER BY z_score DESC
``` 
-->


## Customization Guide


??? info "Customization Guide for Quality Check Results"

    **Adjust Save Mode**

    Choose between full refresh and incremental updates:

    ```yaml
    options:
      saveMode: overwrite   # Full refresh - replaces all data
      # OR
      saveMode: append      # Incremental - adds new data
    ```

    **When to Use Each:**

    - **overwrite**: Simple to maintain, ensures no duplicates, good for smaller datasets or complete reprocessing
    - **append**: More efficient for large historical datasets, requires deduplication logic

    **Change Output Location**

    Update the dataset path to your preferred location:

    ```yaml
    outputs:
      - name: final
        dataset: dataos://lakehouse:your_collection/your_table_name?acl=rw
        checkpointLocation: dataos://lakehouse:your_collection/checkpoints/quality-checks?acl=rw
    ```

    **Enable Scheduling**

    Uncomment and configure the schedule to run automatically:

    ```yaml
    workflow:
      schedule:
        cron: '45 17 * * *'              # Daily at 5:45 PM
        # cron: '0 */6 * * *'            # Every 6 hours
        # cron: '0 8 * * 1'              # Weekly on Monday at 8 AM
        concurrencyPolicy: Forbid         # Prevent overlapping runs
    ```

    **Scheduling Best Practices:**

    - Align with your Soda check execution frequency
    - Run after Soda checks complete (with appropriate delay)
    - Use `concurrencyPolicy: Forbid` to prevent concurrent executions

    **Add Custom Partitioning**

    Customize partitioning based on your query patterns:

    ```yaml
    iceberg:
      partitionSpec:
        - type: identity
          column: depot
        - type: identity
          column: collection
        - type: days            # Time-based partitioning
          column: timestamp
    ```

    **Filter Specific Data**

    Add filters to process only specific datasets or check results:

    ```yaml
    steps:
      - sequence:
          - name: filtered_data
            sql: |
              SELECT * FROM soda
              WHERE depot IN ('lakehouse', 'snowflake')
                AND scan_start_timestamp >= current_date() - INTERVAL 7 DAYS
    ```

    **Extract Additional Attributes**

    Extract more attributes from `resource_attributes`:

    ```yaml
    - name: final
      sql: |
        SELECT
          dataos_run_id,
          job_name,
          timestamp,
          depot,
          collection,
          dataset,
          column,
          check_definition,
          metric_name,
          metric_value,
          check_outcome,
          MAX(CASE WHEN attribute['name'] = 'category' THEN attribute['value'] END) as category,
          MAX(CASE WHEN attribute['name'] = 'title' THEN attribute['value'] END) as check_title,
          MAX(CASE WHEN attribute['name'] = 'priority' THEN attribute['value'] END) as priority
        FROM joined_checks_metrics
        LATERAL VIEW explode(resource_attributes) AS attribute
        WHERE attribute['name'] IN ('category', 'title', 'priority')
        GROUP BY dataos_run_id, job_name, timestamp, depot, collection, dataset,
                column, check_definition, metric_name, metric_value, check_outcome
    ```



## Best Practices

??? info "Best Practices for Quality Check Results"


    **Start with Batch Processing**
    
    Begin with `isStream: false` and `startingOffsets: earliest` to understand the data structure and volume, then optimize for streaming if needed.

    **Use Appropriate Save Modes**
    
    - **Development/Testing**: Use `saveMode: overwrite` for simplicity
    - **Production (Small Data)**: Use `saveMode: overwrite` with scheduled runs
    - **Production (Large Data)**: Use `saveMode: append` with deduplication logic

    **Leverage Partitioning**
    
    Always include partition columns (`depot`, `collection`, `dataset`) in your WHERE clauses:

    ```sql
    -- GOOD: Uses partitioning
    SELECT * FROM quality_checks
    WHERE depot = 'lakehouse' AND collection = 'retail' AND dataset = 'customer'

    -- BAD: Full table scan
    SELECT * FROM quality_checks
    WHERE column = 'email'
    ```

    **Monitor Workflow Execution**
    
    - Set up alerts for workflow failures
    - Monitor data freshness (time lag between check execution and sync)
    - Track row counts and data volume growth

    **Create Materialized Views**
    
    For frequently accessed queries, create materialized views:

    ```sql
    -- Daily quality summary view
    CREATE TABLE quality_summary_daily AS
    SELECT
      DATE(timestamp) as check_date,
      depot,
      collection,
      dataset,
      category,
      COUNT(*) as total_checks,
      SUM(CASE WHEN check_outcome = 'passed' THEN 1 ELSE 0 END) as passed_checks,
      SUM(CASE WHEN check_outcome = 'failed' THEN 1 ELSE 0 END) as failed_checks
    FROM dataos://lakehouse:sys01/slo_quality_checks_a
    GROUP BY DATE(timestamp), depot, collection, dataset, category
    ```

    **Implement Retention Policies**
    
    Archive or delete old data to manage storage costs:

    ```sql
    -- Delete data older than 90 days
    DELETE FROM dataos://lakehouse:sys01/slo_quality_checks_a
    WHERE timestamp < current_date() - INTERVAL 90 DAYS
    ```

    **Use Check Checkpoint Location**
    
    The `checkpointLocation` is critical for exactly-once processing:
    - Use a unique path for each workflow version
    - Never delete checkpoint data while workflow is active
    - Change checkpoint path when making breaking schema changes



## Troubleshooting

**Issue: Workflow Fails with "Cannot resolve column"**

Error message about unresolved columns during transformation

**Solution:**

- Verify column names match the actual Soda stream structure
- Check if `cleanse_column_names` is changing column names unexpectedly
- Use `explain: true` to see the query plan and identify the problematic column

```yaml
job:
  explain: true  # Enable to see full query plan
```

**Issue: Duplicate Records in Output**

Same check results appear multiple times

**Solution:**

**Option 1: Use overwrite mode**
```yaml
options:
  saveMode: overwrite
```

**Option 2: Add deduplication (for append mode)**
```sql
-- Add ROW_NUMBER() to keep only latest
SELECT * FROM (
  SELECT *,
    ROW_NUMBER() OVER (
      PARTITION BY dataos_run_id, check_definition, metric_name
      ORDER BY timestamp DESC
    ) as rn
  FROM dataos://lakehouse:sys01/slo_quality_checks_a
) WHERE rn = 1
```

**Issue: Missing Categories in Output**

Some checks have NULL category values

**Solution:**

- Verify that Soda checks have `category` attribute defined
- Check if `resource_attributes` contains the category:

```sql
-- Debug query to see all attributes
SELECT
  check_definition,
  resource_attributes
FROM joined_checks_metrics
WHERE depot = 'your_depot'
LIMIT 10
```

- If category is under a different attribute name, update the WHERE clause:

```yaml
WHERE attribute['name'] = 'your_category_field_name'
```

**Issue: Join Produces No Results**

`joined_checks_metrics` table is empty or has NULL metric values

**Solution:**

- Verify that `metrics_` column in `checks_extracted` matches `identity` column in `metrics_extracted`
- Add diagnostic query to check join keys:

```sql
-- Check join key values
SELECT DISTINCT metrics_ FROM checks_extracted LIMIT 10;
SELECT DISTINCT identity FROM metrics_extracted LIMIT 10;

-- Check if they match
SELECT
  ce.metrics_ as check_metric_id,
  me.identity as metric_identity,
  ce.dataos_run_id
FROM checks_extracted ce
LEFT JOIN metrics_extracted me
  ON ce.dataos_run_id = me.dataos_run_id
  AND ce.metrics_ = me.identity
WHERE me.identity IS NULL
LIMIT 10;
```

**Issue: Checkpoint Location Errors**

Error about checkpoint location being invalid or inaccessible

**Solution:**

- Ensure checkpoint location has `?acl=rw` permissions
- Use a unique checkpoint path for each workflow
- If changing workflow significantly, use a new checkpoint path:

```yaml
checkpointLocation: dataos://lakehouse:sys01/checkpoints/quality-checks/v1001_a?acl=rw
```

**Issue: LATERAL VIEW Syntax Error**

SQL syntax error on LATERAL VIEW statement

**Solution:**

- Ensure you're using Spark SQL syntax (Flare stack supports this)
- Verify array column is not NULL:

```sql
-- Add NULL check
FROM joined_checks_metrics
LATERAL VIEW explode(
  COALESCE(resource_attributes, array())  -- Handle NULL arrays
) AS attribute
WHERE attribute['name'] = 'category'
```




## Additional Links

- [Soda Stack Overview](/resources/stacks/soda/)
- [Syncing Soda Profiling Data to Lakehouse](/resources/stacks/soda/sync_profiling_data_to_lakehouse/)
- [Syncing Soda Queries Data to Lakehouse](/resources/stacks/soda/sync_queries_data_to_lakehouse/)
- [Monitor Resource](/resources/monitor/)
- [Quality Check Types](/resources/stacks/soda/quality_checks/)
