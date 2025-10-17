# Validity checks

Ensuring data validity is crucial for maintaining the integrity and reliability of datasets. In Soda, validity checks can be defined to monitor and enforce data correctness. Below are explanations and sample configurations for various types of validity checks.

**Check for invalid values based on a set of valid options:** This check verifies that values in the specified column belong to an acceptable set of predefined options.

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

**Check for invalid values based on a regular expression:** Ensure that a column's values match a specific pattern.

The following check ensures that all entries in the `email` column match the standard email format.

```yaml
- invalid_count(email) = 0:
    valid regex: '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'
    name: Email should have a valid format
    attributes:
      category: Validity
      title: Email column should contain valid email addresses
```

**Check for invalid values based on length constraints:** This check ensure that a column's values meet specified length requirements.

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

**Check for invalid values based on numerical ranges:** This check ensures that numerical columns have values within a specified range.

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

**Check for invalid values based on format and length constraints:** It combines length constraint conditions for comprehensive checks.

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


**Some other Examples**

```yaml
# Check for valid values
- invalid_count(customer_id) = 0:
    invalid regex: ^(?!\d{8}$).+$
    attributes:
      category: Validity
- invalid_count(email_address) = 0:
    valid format: email
    attributes:
      category: Validity
- invalid_percent(english_education) = 0:
    valid length: 100
    attributes:
      category: Validity
- invalid_percent(total_children) <= 2:
    valid max: 6
    attributes:
      category: Validity
- invalid_percent(marital_status) = 0:
    valid max length: 10
    attributes:
      category: Validity
- invalid_count(number_cars_owned) = 0:
    valid min: 1
    attributes:
      category: Validity
- invalid_percent(marital_status) = 0:
    valid min length: 1
    attributes:
      category: Validity
- invalid_count(house_owner_flag) = 0:
    valid values: [0, 1]
    attributes:
      category: Validity



# a check with a fixed threshold
- invalid_count(email_address) = 0:
    valid format: email
    attributes:
      category: Validity
      title: Fixed threshold
# a check with a relative threshold
- invalid_percent(english_education) < 3%:
      valid max length: 100
    attributes:
      category: Validity
      title: Relative threshold
```


**Relative threshold**

When Soda scans a column in your dataset, it automatically separates all values in the column into one of three categories:

- missing
- invalid
- valid

Soda then performs two calculations. The sum of the count for all categories in a column is always equal to the total row count for the dataset.
`missing_count(column_name) + invalid_count(column_name) + valid_count(column_name) = row_count`
Similarly, a calculation that uses percentage always adds up to a total of 100 for the column.
`missing_percent(name) + invalid_percent(name) + valid_percent(name) = 100`
These calculations enable you to write checks that use **relative thresholds**.

In the example above, the invalid values of the `english_education` column must be less than three percent of the total row count, or the check fails.

Percentage thresholds are between 0 and 100, not between 0 and 1.
    

### **List of validity metrics**

| **Metric** | **Column config keys** | **Description** | **Supported data types** |
| --- | --- | --- | --- |
| `invalid_count` | `invalid format`, `invalid values`, `valid format`, `valid length`, `valid max`, `valid max length`, `valid min`, `valid min length`, `valid values` | The number of rows in a column that contain values that are not valid. | number, text, time |
| *(same as above)* | `invalid regex`, `valid regex` | The number of rows in a column that contain values that are not valid. | text |
| `invalid_percent` | `invalid format`, `invalid values`, `valid format`, `valid length`, `valid max`, `valid max length`, `valid min`, `valid min length`, `valid values` | The percentage of rows in a column, relative to the total row count, that contain values that are not valid. | number, text, time |
| *(same as above)* | `invalid regex`, `valid regex` | The percentage of rows in a column, relative to the total row count, that contain values that are not valid. | text |



### **List of configuration keys**

The column configuration key:value pair defines what SodaCL ought to consider as valid values.

| **Column config key** | **Description** | **Values** |
| --- | --- | --- |
| **invalid format** | Defines the format of a value that Soda ought to register as invalid.  Only works with columns that contain data type **TEXT**.   | See **List of valid formats**. |
| **invalid regex** | Specifies a regular expression to define your own custom invalid values. | regex, no forward slash delimiters |
| **invalid values** | Specifies the values that Soda ought to consider invalid. | — |
| **valid format** | Defines the format of a value that Soda ought to register as valid.  Only works with columns that contain data type **TEXT**.   | See **List of valid formats**. |
| **valid length** | Specifies a valid length for a string.  Works with columns that contain data type **TEXT**, and also with **INTEGER** on most databases, where implicit casting from string to integer is supported.  **Note:** PostgreSQL does not support this behavior, as it does not implicitly cast strings to integers for this use case. | integer |
| **valid max** | Specifies a maximum numerical value for valid values. | integer or float |
| **valid max length** | Specifies a valid maximum length for a string.  Only works with columns that contain data type **TEXT**. | integer |
| **valid min** | Specifies a minimum numerical value for valid values. | integer or float |
| **valid min length** | Specifies a valid minimum length for a string.  Only works with columns that contain data type **TEXT**. | integer |
| **valid regex** | Specifies a regular expression to define your own custom valid values. | regex, no forward slash delimiters |
| **valid values** | Specifies the values that Soda ought to consider valid. | values in a list |




### **List of valid formats**

- Though table below lists valid formats, the same apply for invalid formats.
- Valid formats apply *only* to columns using data type **TEXT**, not DATE or NUMBER.


| **Format** | **Description / Example** |
| --- | --- |
| **credit card number** | Four four-digit numbers separated by spaces.  Four four-digit numbers separated by dashes.  Sixteen-digit number.  Four five-digit numbers separated by spaces. |
| **date eu** | Validates date only, not time.  `dd/mm/yyyy` |
| **date inverse** | Validates date only, not time.  `yyyy/mm/dd` |
| **date iso 8601** | Validates date and/or time according to ISO 8601 format.  Example: `2021-04-28T09:00:00+02:00` |
| **date us** | Validates date only, not time.  `mm/dd/yyyy` |
| **decimal** | Number uses a `,` or `.` as a decimal indicator. |
| **decimal comma** | Number uses `,` as a decimal indicator. |
| **decimal point** | Number uses `.` as a decimal indicator. |
| **email** | `name@domain.extension` |
| **integer** | Number is whole. |
| **ip address / ipv4 address** | Four whole numbers separated by `.` |
| **ipv6 address** | Eight values separated by `:` |
| **money** | A money pattern with currency symbol + decimal point or comma + currency abbreviation. |
| **money comma** | A money pattern with currency symbol + decimal comma + currency abbreviation. |
| **money point** | A money pattern with currency symbol + decimal point + currency abbreviation. |
| **negative decimal** | Negative number uses a `,` or `.` as a decimal indicator. |
| **negative decimal comma** | Negative number uses `,` as decimal indicator. |
| **negative decimal point** | Negative number uses `.` as decimal indicator. |
| **negative integer** | Number is negative and whole. |
| **negative percentage** | Negative number is a percentage. |
| **negative percentage comma** | Negative number is a percentage with a `,` decimal indicator. |
| **negative percentage point** | Negative number is a percentage with a `.` decimal indicator. |
| **percentage** | Number is a percentage. |
| **percentage comma** | Number is a percentage with a `,` decimal indicator. |
| **percentage point** | Number is a percentage with a `.` decimal indicator. |
| **phone number** | Examples:  `+12 123 123 1234`  `123 123 1234`  `+1 123-123-1234`  `+12 123-123-1234`  `+12 123 123-1234`  `555-2368`  `555-ABCD` |
| **positive decimal** | Positive number uses a `,` or `.` as a decimal indicator. |
| **positive decimal comma** | Positive number uses `,` as decimal indicator. |
| **positive decimal point** | Positive number uses `.` as decimal indicator. |
| **positive integer** | Number is positive and whole. |
| **positive percentage** | Positive number is a percentage. |
| **positive percentage comma** | Positive number is a percentage with a `,` decimal indicator. |
| **positive percentage point** | Positive number is a percentage with a `.` decimal indicator. |
| **time 12h** | Validates against the 12-hour clock.  `hh:mm:ss` |
| **time 12h nosec** | Validates against the 12-hour clock.  `hh:mm` |
| **time 24h** | Validates against the 24-hour clock.  `hh:mm:ss` |
| **time 24h nosec** | Validates against the 24-hour clock.  `hh:mm` |
| **timestamp 12h** | Validates against the 12-hour clock.  `hh:mm:ss` |
| **timestamp 24h** | Validates against the 24-hour clock.  `hh:mm:ss` |
| **uuid** | Universally unique identifier. |










<!-- 
**Check for invalid values with custom error messages**

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

