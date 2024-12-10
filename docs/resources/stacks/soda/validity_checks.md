# Validity checks

Ensuring data validity is crucial for maintaining the integrity and reliability of datasets. In Soda, validity checks can be defined to monitor and enforce data correctness. Below are explanations and sample configurations for various types of validity checks.

**1. Check for invalid values based on a set of valid options:** This check verifies that values in the specified column belong to an acceptable set of predefined options.

<!-- Ensure that a column contains only values from a predefined set. -->

In the following example, the check verifies that the `status` column contains only 'active', 'inactive', or 'pending'.

```yaml
- invalid_count(status) = 0:
    valid values: [active, inactive, pending]
    name: Status should have valid values
    attributes:
      category: Validity
      title: Status column should contain only valid values
```

**2. Check for invalid values based on a regular expression:** Ensure that a column's values match a specific pattern.

The following check ensures that all entries in the `email` column match the standard email format.

```yaml
- invalid_count(email) = 0:
    valid regex: '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'
    name: Email should have a valid format
    attributes:
      category: Validity
      title: Email column should contain valid email addresses
```

**3. Check for invalid values based on length constraints:** This check ensure that a column's values meet specified length requirements.

Here, the check verifies that the `username` column contains values with a length between 5 and 15 character.

```yaml
- invalid_count(username) = 0:
    valid min length: 5
    valid max length: 15
    name: Username should have a valid length
    attributes:
      category: Validity
      title: Username should be between 5 and 15 characters long
```

**4. Check for invalid values based on numerical ranges:** This check ensures that numerical columns have values within a specified range.

The following check ensures that the `age` column contains values between 18 and 65.

```yaml
- invalid_count(age) = 0:
    valid min: 18
    valid max: 65
    name: Age should be within the valid range
    attributes:
      category: Validity
      title: Age should be between 18 and 65
```

**5. Check for invalid values based on format and length constraints:** It combines length constraint conditions for comprehensive checks.

The following check ensures that the `product_code` column matches the specified pattern and has a length of 8 characters.

```yaml
- invalid_count(product_code) = 0:
    valid regex: '^[A-Z]{3}-\\d{4}$'
    valid min length: 8
    valid max length: 8
    name: Product code should have a valid format and length
    attributes:
      category: Validity
      title: Product code should match the pattern and have a length of 8 characters
```

<!-- 
**8. Check for invalid values with custom error messages**

Provide custom error messages for better clarity when checks fail.

```yaml
- invalid_count(phone_number) = 0:
    valid regex: '^\\+\\d{1,3}-\\d{3}-\\d{3}-\\d{4}$'
    name: Phone number should have a valid format
    attributes:
      category: Validity
      title: Phone number should match the international format
```

This check ensures that the `phone_number` column matches the international format. -->

Incorporating these validity checks into workflows enables proactive monitoring and maintenance of dataset correctness, ensuring compliance with organizational data quality standards.

