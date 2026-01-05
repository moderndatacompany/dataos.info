# Syndicating Soda Queries Data

As part of executing quality checks and profiling scans, Soda Stack generates SQL queries against datasets. These queries are captured and logged in the `systemstreams:soda/quality_profile_results_03` stream. This data can be syndicated to storage platforms such as Snowflake, Redshift, or PostgreSQL for downstream analysis. 

This guide demonstrates the process using a DataOS Lakehouse as the target system. The same query data is also available in [Metis](/interfaces/metis/metis_ui_assets/metis_assets_tables/).



!!! info
    The stream address `systemstreams:soda/quality_profile_results_03` may vary depending on the environment. Contact the Database Administrator or a DataOS Operator to confirm the correct stream address.


By syndicating queries data to Lakehouse, you can:

- Monitor SQL query execution patterns across all Soda scans.
- Track query success and failure rates by dataset.
- Debug Soda check failures by analyzing failed queries.
- Understand query volume and performance trends.
- Identify datasets with frequent query issues.
- Optimize Soda check configurations based on query patterns.

## Understanding Soda Queries Data

Soda quality checks and profiling operations translate into SQL queries that execute against your data sources. For example:

**Quality Check:**
```yaml
checks:
  - row_count between 100 and 1000
```

**Generated SQL Query:**
```sql
SELECT COUNT(*) FROM customer_table
```

**Profiling Request:**
```yaml
profile:
  columns:
    - customer_id
    - email
```

**Generated SQL Queries:**
```sql
SELECT AVG(customer_id), STDDEV(customer_id), MIN(customer_id), MAX(customer_id) FROM customer_table
SELECT COUNT(DISTINCT email), COUNT(*) FROM customer_table WHERE email IS NULL
```

Each Soda scan execution generates multiple queries stored in the `queries` array. This workflow extracts these queries, normalizes them, tracks their success/failure status, and aggregates statistics for monitoring.


## Workflow Architecture

The queries sync workflow follows a streamlined transformation pipeline:

```
Soda Stream (Raw Data)
        ↓
Complex Transformation with 3 CTEs(Common Table Expression):
  ├─ CTE 1: Explode & Normalize Queries
  ├─ CTE 2: Determine Query Status
  └─ CTE 3: Aggregate Query Statistics
        ↓
Lakehouse (Iceberg Table)
```



## Complete Workflow Manifest

```yaml
name: queries-data-workflow
version: v1
type: workflow

workflow:
  schedule:
    cron: '15 11 * * *'
    concurrencyPolicy: Forbid

  dag:
    - name: queries-data
      spec:
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            logLevel: INFO

            inputs:
              - name: soda
                dataset: dataos://systemstreams:soda/quality_profile_results_03
                isStream: false
                options:
                  startingOffsets: earliest

            outputs:
              - name: final
                dataset: dataos://lakehouse:sandbox/queries_data?acl=rw
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
                  - name: final
                    sql: |
                      WITH exploded AS (
                        SELECT
                          a.dataset,
                          a.depot,
                          a.collection,
                          a.clustername,
                          a.branchname,
                          a.username,
                          to_timestamp(a.datatimestamp, "yyyy-MM-dd'T'HH:mm:ssXXX") AS event_time,
                          lower(regexp_replace(q.sql, '\\s+', ' ')) AS sql_norm,
                          q.exception AS exception
                        FROM soda a
                        LATERAL VIEW OUTER explode(a.queries) qv AS q
                        WHERE q.sql IS NOT NULL
                      ),
                      query_status AS (
                        SELECT
                          dataset,
                          depot,
                          collection,
                          clustername,
                          branchname,
                          username,
                          event_time,
                          sql_norm,
                          MAX(CASE WHEN exception IS NOT NULL AND trim(exception) <> '' THEN 1 ELSE 0 END) AS has_failure
                        FROM exploded
                        GROUP BY
                          dataset, depot, collection, clustername, branchname, username, event_time, sql_norm
                      )
                      SELECT
                        clustername,
                        depot,
                        collection,
                        dataset,
                        username,
                        event_time,
                        COUNT(*) AS total_queries,
                        SUM(CASE WHEN has_failure = 0 THEN 1 ELSE 0 END) AS successful_queries,
                        SUM(CASE WHEN has_failure = 1 THEN 1 ELSE 0 END) AS failed_queries
                      FROM query_status
                      GROUP BY
                        dataset, depot, collection, clustername, branchname, username, event_time
                      ORDER BY
                        event_time DESC,
                        total_queries DESC
```



## Configuration Breakdown


### **Input Configuration**

```yaml
inputs:
  - name: soda
    dataset: dataos://systemstreams:soda/quality_profile_results_03
    isStream: false
    options:
      startingOffsets: earliest
```

**Key Points:**

- **Same Source**: Reads from the same Soda stream as quality checks and profiling workflows
- **Batch Mode**: `isStream: false` processes all historical query data
- **Complete Data**: `startingOffsets: earliest` ensures all queries since stream inception are included

### **Output Configuration**

```yaml
outputs:
  - name: final
    dataset: dataos://lakehouse:sandbox/queries_data?acl=rw
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
```

**Key Points:**

- **`saveMode: append`**: Adds new query statistics to existing data (ideal for incremental monitoring)
- **Partitioning**: Three-level partitioning by depot → collection → dataset for efficient querying
- **Sorting**: Within each partition, data is sorted for optimal read performance


## Transformation Pipeline Explained

**Complex Query Aggregation**

This step uses a single SQL statement with three Common Table Expressions (CTEs) to extract and aggregate query data.

CTE 1: Explode and Normalize Queries:

```sql
WITH exploded AS (
  SELECT
    a.dataset,
    a.depot,
    a.collection,
    a.clustername,
    a.branchname,
    a.username,
    to_timestamp(a.datatimestamp, "yyyy-MM-dd'T'HH:mm:ssXXX") AS event_time,
    lower(regexp_replace(q.sql, '\\s+', ' ')) AS sql_norm,
    q.exception AS exception
  FROM soda a
  LATERAL VIEW OUTER explode(a.queries) qv AS q
  WHERE q.sql IS NOT NULL
)
```

Extract and normalize individual queries from the nested `queries` array.

**Key Operations:**

1. **LATERAL VIEW OUTER explode()**

    ```sql
    LATERAL VIEW OUTER explode(a.queries) qv AS q
    ```

    - `explode(a.queries)`: Converts the `queries` array into separate rows (one row per query)
    - `LATERAL VIEW`: Enables referencing both the original row (`a.*`) and exploded elements (`q.*`)
    - `OUTER`: Preserves rows even if `queries` array is NULL or empty
    - **Result**: If a Soda scan executed 5 queries, this creates 5 rows

2. **Timestamp Parsing**

    ```sql
    to_timestamp(a.datatimestamp, "yyyy-MM-dd'T'HH:mm:ssXXX") AS event_time
    ```

    - Converts ISO 8601 timestamp string to proper timestamp type
    - Format: `"2024-01-15T10:30:00+05:30"` → `TIMESTAMP '2024-01-15 10:30:00'`
    - Enables time-based filtering and aggregation

3. **SQL Normalization**

    ```sql
    lower(regexp_replace(q.sql, '\\s+', ' ')) AS sql_norm
    ```

    - **Why Normalize?** Same logical query may have different whitespace:
    
      ```sql
      "SELECT COUNT(*) FROM customer"
      "SELECT   COUNT(*)   FROM    customer"
      "select count(*) from customer"
      ```

    - **Step 1** - `regexp_replace(q.sql, '\\s+', ' ')`: Replace multiple spaces/tabs/newlines with single space
    - **Step 2** - `lower()`: Convert to lowercase
    - **Result**: All three examples become `"select count(*) from customer"`
    - **Benefit**: Enables grouping identical queries regardless of formatting

4. **Exception Extraction**

    ```sql
    q.exception AS exception
    ```

    - Each query object has an `exception` field
    - Contains error message if query failed, NULL if successful
    - Used to determine query success/failure status

**Example Input/Output:**

**Input (Soda Stream Record):**
```json
{
  "depot": "lakehouse",
  "collection": "retail",
  "dataset": "customer",
  "datatimestamp": "2024-01-15T10:30:00Z",
  "queries": [
    {
      "sql": "SELECT COUNT(*) FROM customer",
      "exception": null
    },
    {
      "sql": "SELECT  AVG(age),  STDDEV(age)  FROM  customer",
      "exception": null
    },
    {
      "sql": "SELECT COUNT(DISTINCT email) FROM customer",
      "exception": "Syntax error at line 1"
    }
  ]
}
```

**Output (exploded CTE - 3 rows):**

```
depot    | collection | dataset  | event_time           | sql_norm                                      | exception
---------|------------|----------|----------------------|-----------------------------------------------|---------------------------
lakehouse  | retail     | customer | 2024-01-15 10:30:00  | select count(*) from customer                 | NULL
lakehouse  | retail     | customer | 2024-01-15 10:30:00  | select avg(age), stddev(age) from customer    | NULL
lakehouse  | retail     | customer | 2024-01-15 10:30:00  | select count(distinct email) from customer    | Syntax error at line 1
```


CTE 2: Determine Query Status: 

```sql
query_status AS (
  SELECT
    dataset,
    depot,
    collection,
    clustername,
    branchname,
    username,
    event_time,
    sql_norm,
    MAX(CASE WHEN exception IS NOT NULL AND trim(exception) <> '' THEN 1 ELSE 0 END) AS has_failure
  FROM exploded
  GROUP BY
    dataset, depot, collection, clustername, branchname, username, event_time, sql_norm
)
```

Group by normalized SQL to determine if any execution of that query failed.

**Key Operations:**

1. **Failure Detection Logic**
    ```sql
    MAX(CASE WHEN exception IS NOT NULL AND trim(exception) <> '' THEN 1 ELSE 0 END) AS has_failure
    ```

    - **Checks two conditions**:
      - `exception IS NOT NULL`: Exception field has a value
      - `trim(exception) <> ''`: Exception is not an empty string (after trimming whitespace)
    - **Returns**: 1 if query has an exception, 0 if successful
    - **MAX() aggregation**: If the same query runs multiple times in a scan, mark as failed if ANY execution failed

2. **Grouping by Normalized SQL**
    ```sql
    GROUP BY dataset, depot, collection, clustername, branchname, username, event_time, sql_norm
    ```
    - Groups identical queries (same `sql_norm`) from the same scan execution
    - Enables detecting if the same query was retried or executed multiple times
    - Preserves context (who ran it, when, on which dataset)

**Example Scenario:**

**Input (exploded CTE):**
```
dataset  | event_time           | sql_norm                          | exception
---------|----------------------|-----------------------------------|---------------------------
customer | 2024-01-15 10:30:00  | select count(*) from customer     | NULL
customer | 2024-01-15 10:30:00  | select count(*) from customer     | NULL        (retry)
customer | 2024-01-15 10:30:00  | select avg(age) from customer     | NULL
customer | 2024-01-15 10:30:00  | select sum(revenue) from customer | Division by zero
customer | 2024-01-15 10:30:00  | select sum(revenue) from customer | Division by zero (retry)
```

**Output (query_status CTE):**

```
dataset  | event_time           | sql_norm                          | has_failure
---------|----------------------|-----------------------------------|-------------
customer | 2024-01-15 10:30:00  | select count(*) from customer     | 0
customer | 2024-01-15 10:30:00  | select avg(age) from customer     | 0
customer | 2024-01-15 10:30:00  | select sum(revenue) from customer | 1
```

- The `count(*)` query that ran twice is grouped into one row with `has_failure=0` (both successful)
- The `sum(revenue)` query that failed twice is grouped into one row with `has_failure=1` (at least one failed)


CTE 3: Final Aggregation: 

```sql
SELECT
  clustername,
  depot,
  collection,
  dataset,
  username,
  event_time,
  COUNT(*) AS total_queries,
  SUM(CASE WHEN has_failure = 0 THEN 1 ELSE 0 END) AS successful_queries,
  SUM(CASE WHEN has_failure = 1 THEN 1 ELSE 0 END) AS failed_queries
FROM query_status
GROUP BY
  dataset, depot, collection, clustername, branchname, username, event_time
ORDER BY
  event_time DESC,
  total_queries DESC
```

Aggregate query execution statistics per Soda scan (by dataset, user, time).

**Key Operations:**

1. **Count Total Queries**
    ```sql
    COUNT(*) AS total_queries
    ```
    - Counts distinct normalized queries executed in a scan
    - Each row in `query_status` represents one unique query
    - **Example**: If a scan ran 5 different queries, `total_queries = 5`

2. **Count Successful Queries**
    ```sql
    SUM(CASE WHEN has_failure = 0 THEN 1 ELSE 0 END) AS successful_queries
    ```
    - Sums up queries where `has_failure = 0` (no exceptions)
    - **Example**: If 3 out of 5 queries succeeded, `successful_queries = 3`

3. **Count Failed Queries**
    ```sql
    SUM(CASE WHEN has_failure = 1 THEN 1 ELSE 0 END) AS failed_queries
    ```
    - Sums up queries where `has_failure = 1` (had exceptions)
    - **Example**: If 2 out of 5 queries failed, `failed_queries = 2`

4. **Grouping by Scan Execution**
    ```sql
    GROUP BY dataset, depot, collection, clustername, branchname, username, event_time
    ```
    - Each unique combination represents one Soda scan execution
    - Aggregates all queries from that scan into summary statistics

5. **Ordering Results**
    ```sql
    ORDER BY event_time DESC, total_queries DESC
    ```
    - Latest scans first (`event_time DESC`)
    - Within same time, scans with more queries first (`total_queries DESC`)
    - Helps quickly identify recent or query-heavy scan executions

**Example Final Output:**

**Input (query_status CTE):**
```
depot    | collection | dataset  | username | event_time           | sql_norm                          | has_failure
---------|------------|----------|----------|----------------------|-----------------------------------|-------------
lakehouse  | retail     | customer | john_doe | 2024-01-15 10:30:00  | select count(*) from customer     | 0
lakehouse  | retail     | customer | john_doe | 2024-01-15 10:30:00  | select avg(age) from customer     | 0
lakehouse  | retail     | customer | john_doe | 2024-01-15 10:30:00  | select stddev(age) from customer  | 0
lakehouse  | retail     | customer | john_doe | 2024-01-15 10:30:00  | select sum(revenue) from customer | 1
lakehouse  | retail     | customer | john_doe | 2024-01-15 10:30:00  | select max(price) from customer   | 1
```

**Output (Final aggregation):**
```
depot    | collection | dataset  | username | event_time           | total_queries | successful_queries | failed_queries
---------|------------|----------|----------|----------------------|---------------|--------------------|-----------------
lakehouse  | retail     | customer | john_doe | 2024-01-15 10:30:00  | 5             | 3                  | 2
```

**Interpretation:**

- This Soda scan executed 5 distinct queries
- 3 queries succeeded (count, avg, stddev)
- 2 queries failed (sum, max)
- Query success rate = 3/5 = 60%



## Output Schema

When querying through Workbench, final output looks like following table:

| __metadata | clustername | depot | collection | dataset | username | event_time | total_queries | successful_queries | failed_queries |
|-----------|-------------|-------|------------|---------|----------|------------|---------------|--------------------|----------------|
| {"_dataos_run_mapper...} | miniature | postgresmrab | public | customer_data_mrab | jhondoe | 2025-12-22 13:07:06.000 UTC | 25 | 25 | 0 |
| {"_dataos_run_mapper...} | system | lakehouse | sandbox | soda_quality_checks_02 | iamgroot | 2025-12-15 12:09:31.000 UTC | 16 | 16 | 0 |
| {"_dataos_run_mapper...} | system | lakehouse | sandbox | soda_quality_checks_02 | iamgroot | 2025-12-15 12:06:29.000 UTC | 1 | 0 | 1 |
| {"_dataos_run_mapper...} | system | lakehouse | sandbox | soda_quality_checks_02 | iamgroot | 2025-12-15 12:04:55.000 UTC | 1 | 0 | 1 |
| {"_dataos_run_mapper...} | system | lakehouse | sandbox | soda_quality_checks_02 | iamgroot | 2025-12-15 12:01:33.000 UTC | 1 | 0 | 1 |
| {"_dataos_run_mapper...} | system | lakehouse | sandbox | soda_quality_checks_02 | iamgroot | 2025-12-15 11:50:40.000 UTC | 1 | 0 | 1 |
| {"_dataos_run_mapper...} | miniature | postgresmrab | public | customer_data_mrab | jhondoe | 2025-12-22 13:05:14.000 UTC | 1 | 0 | 1 |
| {"_dataos_run_mapper...} | miniature | postgresmrab | public | customer_data_mrab | jhondoe | 2025-12-19 14:59:37.000 UTC | 25 | 25 | 0 |
| {"_dataos_run_mapper...} | miniature | postgresmrab | public | customer_data_mrab | jhondoe | 2025-12-19 13:40:00.000 UTC | 25 | 25 | 0 |
| {"_dataos_run_mapper...} | system | lakehouse | sandbox | soda_quality_checks_data | iamgroot | 2025-12-16 09:49:09.000 UTC | 38 | 38 | 0 |


The final output table contains the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `clustername` | String | Cluster where Soda scan was executed (e.g., minerva, themis) |
| `depot` | String | Data source or depot identifier where queries were executed (e.g., lakehouse, snowflake) |
| `collection` | String | Schema or database name containing the dataset |
| `dataset` | String | Table or dataset name against which queries were executed |
| `username` | String | DataOS user who triggered the Soda scan |
| `event_time` | Timestamp | When the Soda scan was executed (parsed from `datatimestamp`) |
| `total_queries` | Long | Total number of distinct SQL queries executed during the scan |
| `successful_queries` | Long | Number of queries that completed successfully (without exceptions) |
| `failed_queries` | Long | Number of queries that encountered errors or exceptions |


<!-- ## Example Case Scenarios

### **1. Query Success Rate Monitoring**

Monitor overall query health across all Soda scans:

```sql
-- Daily query success rate
SELECT
  DATE(event_time) AS scan_date,
  SUM(total_queries) AS total_queries,
  SUM(successful_queries) AS successful_queries,
  SUM(failed_queries) AS failed_queries,
  ROUND(SUM(successful_queries) * 100.0 / SUM(total_queries), 2) AS success_rate_percent
FROM dataos://lakehouse:sandbox/queries_data
WHERE event_time >= current_date() - INTERVAL 30 DAYS
GROUP BY DATE(event_time)
ORDER BY scan_date DESC
```

### **2. Identify Problematic Datasets**

Find datasets with frequent query failures:

```sql
-- Datasets with highest query failure rates
SELECT
  depot,
  collection,
  dataset,
  SUM(total_queries) AS total_queries,
  SUM(failed_queries) AS total_failed,
  ROUND(SUM(failed_queries) * 100.0 / SUM(total_queries), 2) AS failure_rate_percent,
  COUNT(DISTINCT event_time) AS scan_count
FROM dataos://lakehouse:sandbox/queries_data
WHERE event_time >= current_date() - INTERVAL 7 DAYS
GROUP BY depot, collection, dataset
HAVING SUM(failed_queries) > 0
ORDER BY failure_rate_percent DESC
LIMIT 20
```

### **3. Query Volume Analysis**

Understand query volume patterns:

```sql
-- Query volume by dataset
SELECT
  depot,
  collection,
  dataset,
  COUNT(DISTINCT event_time) AS scan_executions,
  SUM(total_queries) AS total_queries_executed,
  ROUND(AVG(total_queries), 1) AS avg_queries_per_scan,
  MAX(total_queries) AS max_queries_single_scan
FROM dataos://lakehouse:sandbox/queries_data
WHERE event_time >= current_date() - INTERVAL 30 DAYS
GROUP BY depot, collection, dataset
ORDER BY total_queries_executed DESC
LIMIT 20
```

### **4. User Activity Monitoring**

Track which users are running Soda scans:

```sql
-- User query activity
SELECT
  username,
  COUNT(DISTINCT CONCAT(depot, '.', collection, '.', dataset)) AS distinct_datasets_scanned,
  COUNT(*) AS total_scan_executions,
  SUM(total_queries) AS total_queries,
  SUM(failed_queries) AS total_failures,
  ROUND(SUM(failed_queries) * 100.0 / SUM(total_queries), 2) AS failure_rate_percent
FROM dataos://lakehouse:sandbox/queries_data
WHERE event_time >= current_date() - INTERVAL 30 DAYS
GROUP BY username
ORDER BY total_scan_executions DESC
```

### **5. Cluster Performance Comparison**

Compare query execution across clusters:

```sql
-- Cluster-wise query performance
SELECT
  clustername,
  COUNT(*) AS total_scans,
  SUM(total_queries) AS total_queries,
  ROUND(AVG(total_queries), 1) AS avg_queries_per_scan,
  SUM(successful_queries) AS successful_queries,
  SUM(failed_queries) AS failed_queries,
  ROUND(SUM(failed_queries) * 100.0 / SUM(total_queries), 2) AS failure_rate_percent
FROM dataos://lakehouse:sandbox/queries_data
WHERE event_time >= current_date() - INTERVAL 7 DAYS
GROUP BY clustername
ORDER BY total_scans DESC
```

### **6. Scan Reliability Tracking**

Identify scans with consistent failures:

```sql
-- Datasets with multiple failed scans
SELECT
  depot,
  collection,
  dataset,
  COUNT(*) AS total_scans,
  SUM(CASE WHEN failed_queries > 0 THEN 1 ELSE 0 END) AS scans_with_failures,
  ROUND(SUM(CASE WHEN failed_queries > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS scan_failure_rate_percent,
  MAX(event_time) AS last_scan_time
FROM dataos://lakehouse:sandbox/queries_data
WHERE event_time >= current_date() - INTERVAL 30 DAYS
GROUP BY depot, collection, dataset
HAVING SUM(CASE WHEN failed_queries > 0 THEN 1 ELSE 0 END) > 2
ORDER BY scan_failure_rate_percent DESC
```

### **7. Time-based Query Patterns**

Analyze query execution patterns by time:

```sql
-- Hourly query execution patterns
SELECT
  HOUR(event_time) AS execution_hour,
  COUNT(*) AS scan_count,
  SUM(total_queries) AS total_queries,
  ROUND(AVG(total_queries), 1) AS avg_queries_per_scan,
  ROUND(SUM(failed_queries) * 100.0 / SUM(total_queries), 2) AS failure_rate_percent
FROM dataos://lakehouse:sandbox/queries_data
WHERE event_time >= current_date() - INTERVAL 7 DAYS
GROUP BY HOUR(event_time)
ORDER BY execution_hour
``` 

-->



## Customization Guide

??? info "Customization Guide for syncing Queries Data"

    **Adjust Save Mode**


    Choose between append and overwrite:

    ```yaml
    options:
      saveMode: append      # Add new data incrementally
      # OR
      saveMode: overwrite   # Replace all data on each run
    ```

    **Recommendation:** Use `append` for continuous monitoring, `overwrite` for testing or periodic full refresh.

    **Change Output Location**


    Update the dataset path:

    ```yaml
    outputs:
      - name: final
        dataset: dataos://lakehouse:your_collection/your_table_name?acl=rw
    ```

    **Enable Scheduling**


    Uncomment and configure the schedule:

    ```yaml
    workflow:
      schedule:
        cron: '15 11 * * *'              # Daily at 11:15 AM
        # cron: '0 */4 * * *'            # Every 4 hours
        # cron: '0 2 * * 1'              # Weekly on Monday at 2 AM
        concurrencyPolicy: Forbid         # Prevent concurrent runs
    ```

    **Add Column Filtering**


    Filter unnecessary columns in the pass-through stage:

    ```yaml
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
    ```

    **Add Time-based Filtering**


    Process only recent data:

    ```yaml
    - name: soda_raw
      sql: |
        SELECT * FROM dropped_columns
        WHERE to_timestamp(datatimestamp, "yyyy-MM-dd'T'HH:mm:ssXXX") >= current_date() - INTERVAL 7 DAYS
    ```

    **Capture Actual SQL Text**


    Store actual SQL queries (not just counts):

    ```yaml
    - name: final
      sql: |
        WITH exploded AS (
          -- ... (same as before)
        )
        SELECT
          clustername,
          depot,
          collection,
          dataset,
          username,
          event_time,
          sql_norm,                           -- Include normalized SQL
          COUNT(*) AS execution_count,
          MAX(CASE WHEN exception IS NOT NULL THEN 1 ELSE 0 END) AS has_failure,
          MAX(exception) AS sample_exception  -- Include exception message
        FROM exploded
        GROUP BY clustername, depot, collection, dataset, username, event_time, sql_norm
        ORDER BY event_time DESC
    ```

    **Note:** This creates more granular output (one row per query instead of per scan) but provides deeper insights.

    

## Best Practices

??? info "Best Practices for syncing Queries Data"

    **1. Use Append Mode for Monitoring**

    For continuous monitoring, use `saveMode: append` to build historical trend data:

    ```yaml
    options:
      saveMode: append
    ```

    Add deduplication logic if needed:
    ```sql
    SELECT DISTINCT * FROM dataos://lakehouse:sandbox/queries_data
    WHERE event_time >= current_date() - INTERVAL 30 DAYS
    ```

    **2. Schedule After Soda Scans**

    Schedule this workflow to run after your Soda check workflows complete:

    ```yaml
    schedule:
      cron: '15 11 * * *'  # If Soda checks run at 11:00 AM, run this at 11:15 AM
    ```

    **3. Leverage Partitioning**

    Always filter by partition columns for optimal performance:

    ```sql
    -- GOOD: Uses partitioning
    SELECT * FROM queries_data
    WHERE depot = 'lakehouse' AND collection = 'retail' AND dataset = 'customer'

    -- BAD: Full table scan
    SELECT * FROM queries_data
    WHERE username = 'john_doe'
    ```

    **4. Create Alerting Rules**

    Set up alerts for high failure rates:

    ```sql
    -- Alert when failure rate exceeds 10%
    SELECT
      depot,
      collection,
      dataset,
      failed_queries,
      total_queries,
      ROUND(failed_queries * 100.0 / total_queries, 2) AS failure_rate
    FROM dataos://lakehouse:sandbox/queries_data
    WHERE event_time >= current_timestamp() - INTERVAL 1 DAY
      AND failed_queries * 100.0 / total_queries > 10.0
    ```

    **5. Monitor Query Volume Growth**

    Track query volume to optimize Soda check configurations:

    ```sql
    -- Identify checks generating too many queries
    SELECT
      depot,
      collection,
      dataset,
      AVG(total_queries) AS avg_queries_per_scan
    FROM dataos://lakehouse:sandbox/queries_data
    WHERE event_time >= current_date() - INTERVAL 7 DAYS
    GROUP BY depot, collection, dataset
    HAVING AVG(total_queries) > 20  -- Threshold
    ORDER BY avg_queries_per_scan DESC
    ```

    **6. Correlate with Check Results**

    Join with quality check results to understand impact:

    ```sql
    -- Correlate failed queries with failed checks
    SELECT
      q.depot,
      q.collection,
      q.dataset,
      q.event_time,
      q.failed_queries,
      c.check_outcome,
      c.check_definition
    FROM dataos://lakehouse:sandbox/queries_data q
    JOIN dataos://lakehouse:sys01/slo_quality_checks_a c
      ON q.depot = c.depot
      AND q.collection = c.collection
      AND q.dataset = c.dataset
      AND DATE(q.event_time) = DATE(c.timestamp)
    WHERE q.failed_queries > 0
      AND c.check_outcome = 'failed'
    ```


## Troubleshooting

**Issue: No Data in Output Table**

Workflow succeeds but output table is empty

**Solution:**

**Check 1: Verify queries exist in source**
```sql
SELECT
  dataset,
  size(queries) AS query_count
FROM dataos://systemstreams:soda/quality_profile_results_03
LIMIT 10
```

**Check 2: Verify WHERE clause**
```sql
-- The workflow filters WHERE q.sql IS NOT NULL
-- Check if queries have SQL text
SELECT
  dataset,
  queries
FROM dataos://systemstreams:soda/quality_profile_results_03
WHERE queries IS NOT NULL AND size(queries) > 0
LIMIT 5
```

**Check 3: Check timestamp parsing**
```sql
-- Verify datatimestamp format
SELECT
  datatimestamp,
  to_timestamp(datatimestamp, "yyyy-MM-dd'T'HH:mm:ssXXX") AS parsed_timestamp
FROM dataos://systemstreams:soda/quality_profile_results_03
LIMIT 10
```

**Issue: Incorrect Query Counts**

Query counts don't match expected values

**Solution:**

**Debug: Check exploded CTE**
Add intermediate output to see exploded queries:

```yaml
- name: debug_exploded
  sql: |
    SELECT
      dataset,
      depot,
      collection,
      event_time,
      sql_norm,
      exception
    FROM (
      SELECT
        a.dataset,
        a.depot,
        a.collection,
        to_timestamp(a.datatimestamp, "yyyy-MM-dd'T'HH:mm:ssXXX") AS event_time,
        lower(regexp_replace(q.sql, '\\s+', ' ')) AS sql_norm,
        q.exception AS exception
      FROM soda_raw a
      LATERAL VIEW OUTER explode(a.queries) qv AS q
      WHERE q.sql IS NOT NULL
    )
    ORDER BY event_time DESC
    LIMIT 100
```

Output this to a separate table to inspect the intermediate results.

**Issue: LATERAL VIEW Syntax Error**

Spark SQL error about LATERAL VIEW syntax

**Solution:**

- Ensure you're using Flare stack (Spark SQL), not another query engine
- Verify the `LATERAL VIEW OUTER explode()` syntax:

```sql
-- Correct syntax
LATERAL VIEW OUTER explode(a.queries) qv AS q

-- Common mistake (missing OUTER)
LATERAL VIEW explode(a.queries) AS q
```

**Issue: Timestamp Parsing Errors**

Error about invalid timestamp format

**Solution:**
Check the actual `datatimestamp` format in your stream:

```sql
SELECT DISTINCT datatimestamp
FROM dataos://systemstreams:soda/quality_profile_results_03
LIMIT 10
```

Adjust the format string if needed:
```sql
-- If format is: 2024-01-15T10:30:00Z
to_timestamp(a.datatimestamp, "yyyy-MM-dd'T'HH:mm:ss'Z'")

-- If format is: 2024-01-15T10:30:00+05:30
to_timestamp(a.datatimestamp, "yyyy-MM-dd'T'HH:mm:ssXXX")

-- If format is: 2024-01-15 10:30:00
to_timestamp(a.datatimestamp, "yyyy-MM-dd HH:mm:ss")
```

**Issue: Duplicate Records**

Same scan appears multiple times with identical statistics

**Solution:**

**Option 1: Use overwrite mode**
```yaml
options:
  saveMode: overwrite
```

**Option 2: Add deduplication**
```sql
SELECT DISTINCT
  clustername,
  depot,
  collection,
  dataset,
  username,
  event_time,
  total_queries,
  successful_queries,
  failed_queries
FROM dataos://lakehouse:sandbox/queries_data
```

**Issue: High Failure Rates**

Most queries showing as failed

**Solution:**

**Investigate exceptions:**
Modify the final SQL to capture exception details:

```sql
WITH exploded AS (
  SELECT
    a.dataset,
    a.depot,
    lower(regexp_replace(q.sql, '\\s+', ' ')) AS sql_norm,
    q.exception AS exception
  FROM soda_raw a
  LATERAL VIEW OUTER explode(a.queries) qv AS q
  WHERE q.sql IS NOT NULL
)
SELECT
  depot,
  dataset,
  sql_norm,
  exception,
  COUNT(*) AS occurrence_count
FROM exploded
WHERE exception IS NOT NULL AND trim(exception) <> ''
GROUP BY depot, dataset, sql_norm, exception
ORDER BY occurrence_count DESC
LIMIT 20
```

This helps identify the most common query failures.



## Additional Links

- [Soda Stack Overview](/resources/stacks/soda/)
- [Syncing Quality Check Results to Lakehouse](/resources/stacks/soda/sync_quality_checks_to_lakehouse/)
- [Syncing Profiling Data to Lakehouse](/resources/stacks/soda/sync_profiling_data_to_lakehouse/)
- [Flare Stack](/resources/stacks/flare/)
- [Monitor Resource](/resources/monitor/)
