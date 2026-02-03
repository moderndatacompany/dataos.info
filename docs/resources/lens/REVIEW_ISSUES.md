# Comprehensive Review of Lens Documentation

This document contains all issues found during line-by-line review of the Lens documentation folder.

## Critical SQL Syntax Mismatches

### 1. DATE_PARSE Function - Not Standard SQL

**Issue:** `DATE_PARSE` is used in multiple files but it's NOT a standard SQL function. It's a Trino/Presto function, not BigQuery, Snowflake, or PostgreSQL.

**Files Affected:**
- `data_sources/bigquery.md` (lines 106, 281)
- `data_sources/snowflake.md` (line 281)
- `data_sources/postgres.md` (line 115)

**Current Code:**
```sql
CAST(DATE_PARSE(birth_date, '%d-%m-%Y') AS TIMESTAMP) AS birth_date,
```

**BigQuery Correct Syntax:**
```sql
CAST(PARSE_DATE('%d-%m-%Y', birth_date) AS TIMESTAMP) AS birth_date,
-- OR
CAST(DATETIME(PARSE_DATE('%d-%m-%Y', birth_date)) AS TIMESTAMP) AS birth_date,
```

**Snowflake Correct Syntax:**
```sql
CAST(TO_DATE(birth_date, 'DD-MM-YYYY') AS TIMESTAMP) AS birth_date,
-- OR
TRY_TO_TIMESTAMP(birth_date, 'DD-MM-YYYY') AS birth_date,
```

**PostgreSQL Correct Syntax:**
```sql
CAST(TO_DATE(birth_date, 'DD-MM-YYYY') AS TIMESTAMP) AS birth_date,
-- OR
CAST(birth_date::date AS TIMESTAMP) AS birth_date,
```

### 2. GROUP BY Clause Error in concepts.md

**File:** `concepts.md` (lines 238-240)

**Issue:** The SQL example uses `GROUP BY 2` but the SELECT clause has `city, COUNT(id)`, which means column 2 is `COUNT(id)`, not `city`. This is incorrect.

**Current Code:**
```sql
SELECT city, COUNT(id) AS count
FROM users
GROUP BY 2;
```

**Correct Code:**
```sql
SELECT city, COUNT(id) AS count
FROM users
GROUP BY city;
-- OR
SELECT city, COUNT(id) AS count
FROM users
GROUP BY 1;
```

**Note:** While `GROUP BY 1` would work (referring to the first column), `GROUP BY city` is clearer and more maintainable.

### 3. Incorrect SQL in concepts.md Example

**File:** `concepts.md` (lines 88-95)

**Issue:** The SQL example has syntax errors:
- Missing FROM clause structure
- Incorrect column references

**Current Code:**
```yaml
sql: >
  SELECT *
  FROM owner_id, email
  WHERE owner.owner_id = contacts.owner_id
```

**Issues:**
1. `FROM owner_id, email` is incorrect - should be `FROM owner` or proper table names
2. References `contacts.owner_id` but `contacts` table is not in FROM clause
3. Should be a proper JOIN or have both tables in FROM

**Suggested Fix:**
```yaml
sql: >
  SELECT *
  FROM owner
  LEFT JOIN contacts ON owner.owner_id = contacts.owner_id
```

## Spelling and Grammar Issues

### 1. Typo in index.md

**File:** `index.md` (line 62)

**Issue:** "Bigquery" should be "BigQuery" (capital Q)

**Current:** `- [Bigquery](/resources/lens/data_sources/bigquery/)`

**Correct:** `- [BigQuery](/resources/lens/data_sources/bigquery/)`

### 2. Typo in governance.md

**File:** `governance.md` (line 29)

**Issue:** "levManage Worker in System Workspacesel" appears to be corrupted text

**Current:** `Governance at the federated query engine levManage Worker in System Workspacesel can be applied in the following ways:`

**Correct:** `Governance at the federated query engine level can be applied in the following ways:`

### 3. Missing Space in lens_manifest_attributes.md

**File:** `lens_manifest_attributes.md` (line 61)

**Issue:** Missing space after colon in router section

**Current:**
```yaml
  router:
  logLevel: INFO
```

**Correct:**
```yaml
  router:
    logLevel: INFO
```

**Note:** Also check indentation - `logLevel` should be indented under `router`.

### 4. Inconsistent Capitalization

**File:** `index.md` (line 46)

**Issue:** "Power BI" should be "Power BI" (with space)

**Current:** `- **BI integration:** Lens improves interoperability through robust integration with Superset, Tableau,  and Power BI.`

**Correct:** `- **BI integration:** Lens improves interoperability through robust integration with Superset, Tableau, and Power BI.`

**Note:** Also remove extra space before "and".

## YAML Syntax Issues

### 1. Indentation Error in lens_manifest_attributes.md

**File:** `lens_manifest_attributes.md` (lines 58-59)

**Issue:** `description` is not properly indented under `depot:`

**Current:**
```yaml
depot:
  type: BIGQUERY                 
      description: ${{description}} # optional
```

**Correct:**
```yaml
depot:
  type: BIGQUERY
  description: ${{description}} # optional
```

### 2. Missing Indentation in lens_manifest_attributes.md

**File:** `lens_manifest_attributes.md` (lines 60-72)

**Issue:** `external`, `secrets`, and `bigquery` sections are not properly indented

**Current:**
```yaml
  external: ${{true}}
  secrets:
    - name: ${{bq-instance-secret-name}}-r
      allkeys: true

    - name: ${{bq-instance-secret-name}}-rw
      allkeys: true
  bigquery:  # optional                         
    project: ${{project-name}} # optional
```

**Correct:**
```yaml
  external: ${{true}}
  secrets:
    - name: ${{bq-instance-secret-name}}-r
      allKeys: true
    - name: ${{bq-instance-secret-name}}-rw
      allKeys: true
  bigquery:  # optional
    project: ${{project-name}} # optional
```

**Note:** Also `allkeys` should be `allKeys` (camelCase).

### 3. Inconsistent Property Names

**File:** `lens_manifest_attributes.md` (line 271)

**Issue:** Uses `allkeys` but should be `allKeys` (camelCase)

**Current:**
```yaml
    - name: github-r
      allkeys: true
```

**Correct:**
```yaml
    - name: github-r
      allKeys: true
```

## Knowledge Gaps and Conceptual Issues

### 1. Missing Information About SQL Dialect Differences

**Files:** `data_sources/bigquery.md`, `data_sources/snowflake.md`, `data_sources/postgres.md`

**Issue:** The documentation doesn't clearly explain that SQL functions differ between dialects. The examples use `DATE_PARSE` which doesn't exist in any of these databases.

**Recommendation:** Add a section explaining:
- BigQuery uses `PARSE_DATE()` for date parsing
- Snowflake uses `TO_DATE()` or `TRY_TO_TIMESTAMP()`
- PostgreSQL uses `TO_DATE()` or `::date` casting
- Trino/Presto uses `DATE_PARSE()` (if using Themis/Minerva)

### 2. Incomplete Example in concepts.md

**File:** `concepts.md` (lines 88-95)

**Issue:** The SQL example is incomplete and doesn't demonstrate the concept properly. It shows a malformed query.

**Recommendation:** Replace with a complete, working example that demonstrates the concept of using complex SQL in table definitions.

### 3. Missing Explanation of {TABLE} Variable

**File:** `concepts.md` (line 164)

**Issue:** The `{TABLE}` variable is used but not fully explained in the context of joins.

**Current:** Just shows usage without explaining when and why to use it.

**Recommendation:** Add explanation that `{TABLE}` refers to the current table being defined, which is especially useful in join conditions.

### 4. Inconsistent Table Naming in Examples

**File:** Multiple files

**Issue:** Examples sometimes use `table:` (singular) and sometimes `tables:` (plural) in YAML.

**Examples:**
- `concepts.md` line 79: `tables:` (correct)
- `concepts.md` line 124: `table:` (incorrect - should be `tables:`)
- `bigquery.md` line 124: `table:` (incorrect)

**Recommendation:** Standardize to always use `tables:` (plural) as it's an array.

## Punctuation and Formatting Issues

### 1. Missing Periods

**File:** `concepts.md` (line 42)

**Issue:** Missing period at end of sentence

**Current:** `A table is a logical construct used to define a real-world entity such as `customer`, `product.``

**Correct:** `A table is a logical construct used to define a real-world entity such as `customer`, `product`.`

### 2. Extra Spaces

**File:** `index.md` (line 46)

**Issue:** Double space before "and"

**Current:** `Superset, Tableau,  and PowerBI`

**Correct:** `Superset, Tableau, and Power BI`

### 3. Inconsistent Quotation Marks

**File:** `dos_and_donts.md` (line 26)

**Issue:** Uses single quotes in YAML example which the same file says to avoid

**Current:**
```yaml
SELECT * FROM'public."Site"'
```

**Issues:**
1. Missing space after FROM
2. Uses single quotes which the document says to avoid

**Correct:**
```sql
SELECT * FROM "public"."Site"
```

## Documentation Structure Issues

### 1. Duplicate Content

**File:** `best_practices.md` and `dos_and_donts.md`

**Issue:** There's significant overlap between these two files. Some content appears in both.

**Recommendation:** Consolidate or clearly differentiate:
- `best_practices.md` should focus on recommended approaches
- `dos_and_donts.md` should focus on common mistakes to avoid

### 2. Incomplete Error Documentation

**File:** `errors.md`

**Issue:** Very brief error documentation with only 4 errors listed. Many potential errors are not documented.

**Recommendation:** Expand with more common errors and their solutions.

## SQL API Documentation Issues

### 1. Incomplete SQL Example

**File:** `exploration_of_lens_using_sql_apis.md` (lines 221-224)

**Issue:** LIMIT and OFFSET are on separate lines which is unusual formatting

**Current:**
```sql
LIMIT 
    10
OFFSET 
    0
```

**Recommendation:** Format as:
```sql
LIMIT 10
OFFSET 0
```

### 2. Missing Explanation

**File:** `exploration_of_lens_using_sql_apis.md` (line 250)

**Issue:** Comment says "Additionally, it must be included in the GROUP BY clause" but the example doesn't show this

**Current:**
```
SELECT country
FROM customer;
```

**Recommendation:** Either remove the comment or add an example showing GROUP BY usage.

## BigQuery-Specific Issues

### 1. Incorrect Table Reference Format

**File:** `data_sources/bigquery.md` (lines 97-98)

**Issue:** Uses `"bigquery"."retail".channel` which is incorrect BigQuery syntax

**Current:**
```sql
FROM
  "bigquery"."retail".channel;
```

**Correct BigQuery Syntax:**
```sql
FROM
  `bigquery.retail.channel`
-- OR if using Trino/Themis connector:
FROM
  "bigquery"."retail"."channel"
```

**Note:** BigQuery uses backticks for identifiers, not double quotes. However, if going through Trino/Themis, the format might be different.

### 2. Missing BigQuery-Specific Functions Documentation

**File:** `data_sources/bigquery.md`

**Issue:** Doesn't mention BigQuery-specific functions that should be used:
- `PARSE_DATE()` instead of `DATE_PARSE()`
- `STRING_AGG()` for string aggregation (mentioned in best_practices.md but not here)
- `EXTRACT()` function usage

## Summary of Critical Issues

### Must Fix (SQL Syntax Errors):
1. Replace `DATE_PARSE()` with dialect-specific functions in all data source files
2. Fix `GROUP BY 2` error in concepts.md
3. Fix malformed SQL example in concepts.md (lines 88-95)

### Should Fix (YAML Syntax):
1. Fix indentation in lens_manifest_attributes.md
2. Standardize `table:` vs `tables:` usage
3. Fix `allkeys` vs `allKeys` inconsistency

### Should Fix (Documentation Quality):
1. Fix typos and grammar issues
2. Add missing explanations for SQL dialect differences
3. Expand error documentation
4. Fix formatting inconsistencies

### Nice to Have:
1. Consolidate duplicate content
2. Add more examples
3. Improve cross-references
