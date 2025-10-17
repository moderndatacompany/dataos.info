# Completeness checks

Ensuring data completeness is vital for maintaining the integrity and reliability of datasets. In Soda, completeness checks can be defined to monitor and enforce the presence of necessary data. Below are explanations and sample configurations for various types of completeness checks.


## Failed rows checks

Use failed rows check to explicitly get failed rows in your data.


**Check for failed rows:** Ensures failed rows are identified by executing a CTE or SQL query against your data, or by grouping failed check results by one or more categories.

```yaml
# Failed rows defined using SQL query
- failed rows:
    fail query: |
      SELECT DISTINCT geography_key
      FROM dim_customer AS customer
    attributes:
      category: Completeness
      title: Monitor failed rows in the customer table

# OR 

# Failed rows defined using a common table expression
- failed rows:
    samples limit: 50
    fail condition: total_children = '2' AND number_cars_owned >= 3
    attributes:
      category: Completeness
      title: Monitor rows that do not meet the specified condition
```

**Check for failed rows using a column parameter:** Identifies failed rows by executing a CTE or SQL query against your data with a specified column parameter.

```yaml
# With SQL query
- failed rows:
    name: Brand must be LUCKY DOG
    column: product_line
    fail query: |
      SELECT *
      FROM dim_product
      WHERE product_line LIKE '%LUCKY DOG%'
    attributes:
      category: Completeness
      title: Brand must not be LUCKY DOG

# With CTE
- failed rows:
    name: Brand must be LUCKY DOG
    column: product_line
    fail condition: brand LIKE '%LUCKY DOG%'
    attributes:
      category: Completeness
      title: Brand must not be LUCKY DOG
```


## Missing metrics

Use missing metrics in Soda checks to detect missing values in a dataset.

**Check for missing values in a column:** Ensure that a specific column does not contain any missing values.

In this example, the check verifies that the `customer_no` column has no missing entries.

```yaml
- missing_count(customer_no) = 0:
    name: Customer number should not have any missing values
    attributes:
      category: Completeness
      title: Ensure customer number is present in all records
```

**Check for missing values with specific missing indicators:** Identify missing values that are represented by specific indicators, such as 'NA' or 'n/a'.

The following check ensures that the `license_type` column does not contain 'NA' or 'n/a' as values.

```yaml
- missing_count(license_type) < 1:
    missing values: [NA, n/a]
    name: License type should not have 'NA' or 'n/a' as values
    attributes:
      category: Completeness
      title: Detect and handle specific missing value indicators in license type
```

**Check for missing values matching a regular expression:** Detects missing values that match a specific pattern, such as improperly formatted dates.

Here, the check identifies entries in the `license_expiry_date` column that match the specified regular expression, indicating potential missing or invalid data.

```yaml
- missing_count(license_expiry_date) = 0:
    missing regex: '(0?[0-9]|1[012])[/](0?[0-9]|[12][0-9]|3[01])[/](0000|(19|20)?\\d\\d)'
    name: License expiry date should not have improperly formatted dates
    attributes:
      category: Completeness
      title: Identify and address improperly formatted dates in license expiry date
```

**Check for missing values as a percentage of total entries:** Ensure that the percentage of missing values in a column does not exceed a specified threshold.

This check verifies that the `phone_number` column has no missing values, ensuring complete contact information.

```yaml
- missing_percent(phone_number) = 0:
    name: Phone number should not have any missing values
    attributes:
      category: Completeness
      title: Ensure phone number is present in all records
```

**Check for missing values in multiple columns:** Ensure that multiple columns do not contain any missing values.

These checks ensure that both `first_name` and `last_name` columns are complete, maintaining the integrity of personal information.

```yaml
- missing_count(first_name) = 0:
    name: First name should not have any missing values
    attributes:
      category: Completeness
      title: Ensure first name is present in all records

- missing_count(last_name) = 0:
    name: Last name should not have any missing values
    attributes:
      category: Completeness
      title: Ensure last name is present in all records
```

**Check for missing values with custom sample limits:** Limit the number of failed row samples collected for analysis when missing values are detected.

This check ensures that the `email_address` column does not have more than 50% missing values and limits the collection of failed row samples to 2 for analysis.

```yaml
- missing_percent(email_address) < 50:
    samples limit: 2
    name: Email address should not have more than 50% missing values
    attributes:
      category: Completeness
      title: Monitor and limit missing values in email address
```

### **List of missing metrics**

| **Metric** | **Column config keys** | **Description** | **Supported data types** |
| --- | --- | --- | --- |
| `missing_count` | `missing values` | The number of rows in a column that contain NULL values and any other user-defined values that qualify as missing. | number, text, time |
| *(same as above)* | `missing regex` | The number of rows in a column that contain NULL values and any other user-defined values that qualify as missing. | text |
| `missing_percent` | `missing values` | The percentage of rows in a column, relative to the total row count, that contain NULL values and any other user-defined values that qualify as missing. | number, text |
| *(same as above)* | `missing regex` | The percentage of rows in a column, relative to the total row count, that contain NULL values and any other user-defined values that qualify as missing. | text |

### **List of configuration keys**

The column configuration key:value pair defines what SodaCL ought to consider as missing values.

| **Column config key** | **Description** | **Values** |
| --- | --- | --- |
| `missing regex` | Specifies a regular expression to define your own custom missing values. | regex, no forward slash delimiters, string only |
| `missing values` | Specifies the values that Soda is to consider missing. | values in a list |

### **List of comparison symbols and phrases**

```
 =
 <
 >
 <=
 >=
 !=
 <>
 between
 not between
```

Incorporating these completeness checks into workflows enables proactive monitoring and maintenance of critical data fields, ensuring ongoing compliance with organizational data quality standards.
