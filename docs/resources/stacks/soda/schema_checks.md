# Schema checks

Maintaining a consistent and accurate schema is essential for data integrity and the reliability of downstream processes. In Soda, schema checks can be defined to monitor and enforce schema consistency. Below are explanations and sample configurations for various types of schema checks.

**1. Check for required columns:** Verify that specific columns are present in the dataset, ensuring it meets business or operational requirements. This check helps confirm that essential data is included for processing and analysis.

In this example, the check issues a warning if either `customer_name` or `premise_code` columns are missing, indicating potential issues in data completeness.

```yaml
- schema:
    name: Ensure essential columns are present
    warn:
      when required column missing: [customer_name, premise_code]
    attributes:
      category: Schema
      title: Essential columns should be present for meaningful analytics
```

**2. Check for forbidden columns:** This check identifies and flags columns that should not exist in the dataset, typically due to being deprecated, sensitive, or irrelevant. It helps maintain data quality by ensuring that unwanted or insecure columns are not included in the dataset.

The following check fails if `credit_card_number` or `social_security_number` columns are found, helping to enforce data governance policies.

```yaml
- schema:
    name: Detect forbidden columns
    fail:
      when forbidden column present: [credit_card_number, social_security_number]
    attributes:
      category: Schema
      title: Forbidden columns should not be present to ensure data compliance
```

**3. Check for correct column data types:** This check ensures that each column in the dataset adheres to the expected data type. Verifying the correct data types helps prevent errors in data processing, improves data consistency, and ensures accurate analysis and reporting.

The following check issues a warning if `site_number` is not an integer or `premise_code` is not a string, ensuring data type consistency.

```yaml
- schema:
    name: Validate column data types
    warn:
      when wrong column type:
        site_number: integer
        premise_code: string
    attributes:
      category: Schema
      title: Columns should have appropriate data types to prevent processing errors
```

**4. Check for column order:** This check verifies that columns are arranged in a specified order, which might be required for certain applications or data processing tasks.

The following check issues a warning if `customer_name` is not the first column or `premise_code` is not the second, maintaining the desired column sequence.

```yaml
- schema:
    name: Verify column order
    warn:
      when wrong column index:
        customer_name: 1
        premise_code: 2
    attributes:
      category: Schema
      title: Columns should appear in the specified order
```


**5. Check for column name patterns:** This check enables the identification of columns whose names match specific patterns. It is useful for detecting columns that may be deprecated, sensitive, or follow a particular naming convention. By applying name patterns, one can ensure compliance with naming standards or flag columns that require attention due to their naming structure.

The following check issues a warning if any column names end with `_temp` or start with `old_`, indicating potential issues with outdated or temporary columns.


```yaml
- schema:
    name: Detect columns with specific name patterns
    warn:
      when forbidden column present: ['%_temp', 'old_%']
    attributes:
      category: Schema
      title: Columns with deprecated name patterns should not be present
```

**6. Check for column presence with wildcards:** This check allows to verify if columns matching specific patterns or partial names exist in the dataset, using wildcard characters. It is particularly useful when column names vary but follow a common naming convention.

The following check issues a warning if columns ending with `_id` or starting with `address_` are missing, ensuring that key columns are included.

```yaml
- schema:
    name: Ensure presence of columns matching patterns
    warn:
      when required column missing: ['%_id', 'address_%']
    attributes:
      category: Schema
      title: Columns matching specified patterns should be present
```

Incorporating these schema checks into workflows enables proactive monitoring and maintenance of the structural integrity of datasets, ensuring alignment with organizational data quality standards.

