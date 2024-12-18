# Uniqueness checks

Ensuring data uniqueness is essential for maintaining the integrity and reliability of datasets. In Soda, uniqueness checks can be defined to monitor and enforce the absence of duplicate records. Below are explanations and sample configurations for various types of uniqueness checks.

**1. Check for duplicate values in a column:** Ensure that a specific column does not contain any duplicate values.

In the following example, the check verifies the `customer_no` column has no duplicate entries, ensuring each customer number is unique.

```yaml
- duplicate_count(customer_no) = 0:
    name: Customer numbers should be unique
    attributes:
      category: Uniqueness
      title: Ensure each customer number is unique
```

**2. Check for duplicate values across multiple columns:** Ensure that combinations of values across multiple columns are unique.

The following check ensures the combination of `first_name`, `last_name`, and `birth_date` is unique across all records, preventing duplicate entries for individuals.


```yaml
- duplicate_count(first_name, last_name, birth_date) = 0:
    name: Combination of first name, last name, and birth date should be unique
    attributes:
      category: Uniqueness
      title: Ensure no duplicate records based on name and birth date
```

**3. Check for duplicate values with a tolerance threshold:** Allow a certain percentage of duplicate values in a column.

Here, the check ensures the `email` column has less than 1% duplicate values, allowing for minimal duplication.

```yaml
- duplicate_percent(email) < 1%:
    name: Email addresses should have less than 1% duplicates
    attributes:
      category: Uniqueness
      title: Limit duplicate email addresses to less than 1%
```

**4. Check for duplicate values with custom sample limits:** Limit the number of failed row samples collected for analysis when duplicates are detected.

This check verifies the `phone_number` column has no duplicate values and limits the collection of failed row samples to 5 for analysis.

```yaml
- duplicate_count(phone_number) = 0:
    samples limit: 5
    name: Phone numbers should be unique
    attributes:
      category: Uniqueness
      title: Ensure each phone number is unique and limit sample collection
```

**5. Check for duplicate values with custom filters:** Apply a filter to assess the uniqueness of specific subsets of data.

The following configuration checks that records with a `status` of 'completed' in the `transaction_id` column are unique, ensuring no duplication in completed transactions.

```yaml
- duplicate_count(transaction_id) = 0:
    filter: status = 'completed'
    name: Completed transactions should have unique IDs
    attributes:
      category: Uniqueness
      title: Ensure each completed transaction ID is unique
```

Incorporating uniqueness checks into workflows enables proactive monitoring and maintenance of data distinctness, ensuring compliance with organizational data quality standards.

