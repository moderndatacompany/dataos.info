# Accuracy checks

Maintaining data accuracy is crucial for ensuring the integrity and reliability of datasets. In Soda, accuracy checks can be defined to monitor and enforce data correctness. Below are explanations and sample configurations for various types of accuracy checks.

**1. Check for row count within a specific range:** Ensure that the number of records in your dataset falls within an expected range.

In the following example, the check verifies that the dataset contains between 1 and 170 records, ensuring it meets expected volume criteria.

```yaml
- row_count between 1 and 170:
    name: Dataset should have between 1 and 170 records
    attributes:
      category: Accuracy
      title: Validate dataset size
```

**2. Check for average length of a text column:** Ensures the average length of entries in a text column meets a minimum threshold.

The following check ensures the `address` column has an average length greater than 16 characters, indicating sufficient detail in address entries.

```yaml
- avg_length(address) > 16:
    name: Address should have an average length greater than 16 characters
    attributes:
      category: Accuracy
      title: Validate average length of address entries
```

**3. Check for maximum value in a numeric column:** Ensure the maximum value in a numeric column does not exceed a specified limit.

Here, the check verifies the `order_amount` column does not have values exceeding 10,000, ensuring orders remain within expected financial limits.

```yaml
- max(order_amount) <= 10000:
    name: Order amount should not exceed 10,000
    attributes:
      category: Accuracy
      title: Validate maximum order amount
```

**4. Check for minimum value in a numeric column:** Ensures the minimum value in a numeric column meets a specified threshold.

This check ensures the `age` column has no values less than 18, enforcing a minimum age requirement.

```yaml
- min(age) >= 18:
    name: Age should be at least 18
    attributes:
      category: Accuracy
      title: Validate minimum age requirement
```

**5. Check for sum of values in a numeric column:** Ensure the sum of values in a numeric column does not exceed a specified limit.

The following check verifies the sum of the `discount` column is less than 120, ensuring discounts remain within acceptable limits.

```yaml
- sum(discount) < 120:
    name: Total discount should be less than 120
    attributes:
      category: Accuracy
      title: Validate total discount amount
```

**6. Check for percentile value in a numeric column:** Ensure that a specific percentile value in a numeric column meets a specified threshold.

The following check verifies the 95th percentile of the `size` column is greater than 50, ensuring that the majority of size values meet the expected threshold.

```yaml
- percentile(size, 0.95) > 50:
    name: 95th percentile of size should be greater than 50
    attributes:
      category: Accuracy
      title: Validate upper percentile of size values
```

**7. Reference check for value consistency across datasets:** Ensures that values in a column of one dataset exist in a column of another dataset, maintaining referential integrity.

In the following example, the check verifies that every value in the `city` column exists in the `site_state_name` column of the `site_check1` dataset, ensuring consistency across datasets.

```yaml
- values in (city) must exist in site_check1 (site_state_name):
    name: City values should exist in site_state_name of site_check1
    attributes:
      category: Accuracy
      title: Validate referential integrity between city and site_state_name
```

**8. Cross check for row count consistency between datasets:** Ensures the number of records in one dataset matches the number in another, verifying consistency across datasets.

This check compares the row count of the current dataset with that of `site_check1`, ensuring both datasets have the same number of records, which is crucial for data integrity.

```yaml
- row_count same as site_check1:
    name: Dataset should have the same number of records as site_check1
    attributes:
      category: Accuracy
      title: Validate row count consistency between datasets
```

By incorporating these accuracy checks into your workflows, you can proactively monitor and maintain the correctness of your datasets, ensuring they meet your organization's data quality standards.