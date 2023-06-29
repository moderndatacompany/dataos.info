# List of Flare Functions


### **`add_column`**

| Function | Description |
| --- | --- |
| `add_column` | The *add_column* function adds a new column. The supported types are string, boolean, byte, short, int, long, float, double, decimal, date, and timestamp. |

**Code Snippet**

```yaml
functions:
  - name: add_column 
    column: new_column_name 
    value: some_value 
    type: int
```

> **Note:** In the event that the specified data type is not among the supported options, the `add_column` function will return an **Invalid datatype found** error.
> 

### **`any_date`**

| Function | Description |
| --- | --- |
| `any_date` | The *any_date* function converts the string to date type while parsing the string based on the rule provided. Using the by default rule, it converts a date column given in any format like yyyy.mm.dd, dd.mm.yyyy, dd/MM/yy, yyyy/mm/dd, and other (total 18 different formats) into yyyy-mm-dd format.  The rule should be a regular expression. |

**Code Snippet:**

```yaml
functions:
  - name: any_date 
    column: date_string_column_name 
    asColumn: column_name 
#   rule: 
# - "【(?<year>\\d{4})\\W{1}(?<month>\\d{1,2})\\W{1}(?<day>\\d{1,2})[^\\d]? \\W*(?:at )?(?<hour>\\d{1,2}):(?<minute>\\d{1,2})(?::(?<second>\\d{1,2}))?(?:[.,](?<ns>\\d{1,9}))?(?<zero>z)?】"
```

> **Note:** You can provide explicit regex `rules` for the column passed in the **any_date** function. Without an explicit regex, the function will use the default rule.
> 

### **`any_timestamp`**

| Function | Description |
| --- | --- |
| `any_timestamp` | The *any_timestamp* function converts a string to timestamp type while parsing the string based on the rule provided. The timestamp format is as per the specified timezone. The rule should be a regular expression. |

**Code Snippet:**

```yaml
functions:
  - name: any_timestamp 
    column: datetime_string_column_name 
    asColumn: column_name 
    timezone: Asia/Kolkata 
#   rules:
#     - "【(?<year>\\d{4})\\W{1}(?<month>\\d{1,2})\\W{1}(?<day>\\d{1,2})[^\\d]? \\W*(?:at )?(?<hour>\\d{1,2}):(?<minute>\\d{1,2})(?::(?<second>\\d{1,2}))?(?:[.,](?<ns>\\d{1,9}))?(?<zero>z)?】"
```

> **Note:** You can provide explicit regex `rules` for the column passed in the **any_timestamp** function. Without an explicit regex, the function will use the default rule.
> 

### **`change_case`**

| Function | Description |
| --- | --- |
| `change_case` | The *change_case* function alters the columns case to Lowercase, Uppercase, or Titlecase depending upon the applied lower/upper/title case changes the column values . |

**Code Snippet:**

```yaml
functions:
  - name: change_case 
    case: lower 
    column: asin 
```

### **`change_column_case`**

| Function | Description |
| --- | --- |
| `change_column_case` | The *change_column_case* function changes column names(all columns) to either lowercase or uppercase based on value of case: lower/upper. |

**Code Snippet:**

```yaml
functions:
  - name: change_column_case 
    case: upper 
```

### **`cleanse_column_names`**

| Function | Description |
| --- | --- |
| `cleanse_column_names`  | The *cleanse_column_names* function sanatizes column names, following these rules: <br> • Trim leading and trailing spaces <br> • Lowercases the column name <br> • Replaces any character that are not one of [A-Z][a-z][0-9] or _ with an underscore (_) |

**Code Snippet:**

```yaml
functions:
  - name: cleanse_column_names
```

### **`columns_replace`**

| Function | Description |
| --- | --- |
| `columns_replace` | The *columns_replace* function alters column names in bulk. |

**Code Snippet:**

```yaml
functions:
  - name: columns_replace
    sedExpression: 's/^data_//g'
```

### **`copy`**

| Function | Description |
| --- | --- |
| `copy` | The *copy* function copies values from a source column into a destination column. |

**Code Snippet:**

```yaml
functions:
  - name: copy
    fromColumn: source_column_name
    toColumn: destination_column_name
```

### **`cut_character`**

| Function | Description |
| --- | --- |
| `cut_character` | The *cut_character* function selects parts of a string value, accepting standard cut options. |

**Code Snippet:**

```yaml
functions: 
  - name: cut_character 
    column: title 
    asColumn: title_prefix 
    startIndex: 1 
    endIndex: 5
```

### **`decode`**

| Function | Description |
| --- | --- |
| `decode` | The *decode* function decodes a column value as one of base32, base64, or hex following RFC-4648. |

**Code Snippet:**

```yaml
functions: 
  - name: decode 
    algo: base64 
    column: col1 
    asColumn: new_col1
```

### **`diff_date`**

| Function | Description |
| --- | --- |
| `diff_date` | The *diff_date* function calculates difference between two date columns. |

**Code Snippet:**

```yaml
functions: 
  - name: diff_date 
    columnA: col_a 
    columnB: col_b 
    asColumn: col_diff_date
```

### **`drop`**

| Function | Description |
| --- | --- |
| `drop` | The *drop* function is used to drop a list of columns. |

**Code Snippet:**

```yaml
functions:
  - name: drop
    columns:
      - column_1 
      - column_2
```

### **`drop_duplicates`**

| Function | Description |
| --- | --- |
| `drop_duplicates` | The *drop_duplicates* function removes all the duplicate elements from a list of columns. |

**Code Snippet:**

```yaml
functions:
  - name: drop_duplicates
    columns:
      - column_1 
      - column_2
```

### **`encode`**

| Function | Description |
| --- | --- |
| `encode` | The *encode* function encodes a column value as one of base32 , base64, or hex following RFC-4648. |

**Code Snippet:**

```yaml
functions:
  - name: encode
    algo: base64 
    column: col1 
    asColumn: new_col1
```

### **`epoch_to_timestamp`**

| Function | Description |
| --- | --- |
| `epoch_to_timestamp` | The *epoch_to_timestamp* function converts epoch string to timestamp format. |

**Code Snippet:**

```yaml
functions:
  - name: epoch_to_timestamp
    column: epoch_column
    asColumn: date_column
```

### **`fill_null_or_empty`**

| Function | Description |
| --- | --- |
| `fill_null_or_empty` | The *fill_null_or_empty* function fills column value with a fixed value if it is either null or empty (""). If the column does not exist, then the function will fail.The defaultValue can only be of type string. |

**Code Snippet:**

```yaml
functions:
  - name: fill_null_or_empty
    columns:
      column1: value1
      column2: value2
```

### **`find_and_replace`**

| Function | Description |
| --- | --- |
| `find_and_replace` | The *find_and_replace* function transforms string column values using a "sed"-like expression to find and replace text within the same column. |

**Code Snippet:**

```yaml
functions:
  - name: find_and_replace
    column: title
    sedExpression: "s/regex/replacement/g"
```

### **`flatten`**

| Function | Description |
| --- | --- |
| `flatten` | The *flatten* function separates the elements in a repeated field into individual records. This function is useful for the flexible exploration of repeated data. To maintain the association between each flattened value and the other fields in the record, the FLATTEN directive copies all of the other columns into each new record. <br> <b>Note</b> :- Use flatten_outer when array has null values and you want records of root with null in flattened columns.  |

**Code Snippet:**

```yaml
functions:
  - name: flatten
    column: array_holding_column
    asColumn: new_column_name
```

### **`format_date`**

| Function | Description |
| --- | --- |
| `format_date` | The *format_date* function allows custom patterns for date-time formatting. |

**Code Snippet:**

```yaml
functions:
  - name: format_date
    column: date_column
    format: "yyyy-MM-dd'T'HH:mm:ss"
```

### **`format_unix_date`**

| Function | Description |
| --- | --- |
| `format_unix_date` | The *format_unix_date* function allows custom patterns for date-time formatting. |

**Code Snippet:**

```yaml
functions:
  - name: format_unix_date
    column: unix_epoch_column
    format: "yyyy-MM-dd'T'HH:mm:ss"
```

### **`generate_uuid`**

| Function | Description |
| --- | --- |
| `generate_uuid` | The *generate_uuid* function generates a universally unique identifier (UUID) of the record. |

**Code Snippet:**

```yaml
functions:
  - name: generate_uuid
    asColumn: column_01
```

### **`hash`**

| Function | Description |
| --- | --- |
| `hash` | The *hash* function generates a message digest. The column is replaced with the digest created using the supplied algorithm. The type of column is a string. |

**Code Snippet:**

```yaml
functions:
  - name: hash
    column: column_to_hash
    algo: MD5 | SHA-1 | SHA-256 | SHA-384 | SHA-512
```

### **`increment_variable`**

| Function | Description |
| --- | --- |
| `increment_variable` | The *increment_variable* function increments the value of the variable that is local to the input record being processed. |

**Code Snippet:**

```yaml
functions:
  - name: increment_variable
    column: column_01
```

### **`mask_number`**

| Function | Description |
| --- | --- |
| `mask_number` | The *mask_number* function applies substitution masking on the column values.<br>The 'column' specifies the name of an existing column to be masked.<br>The 'pattern' is a substitution pattern to be used to mask the column values.<br>Substitution masking is generally used for masking credit card or social security numbers. The MASK_NUMBER applies substitution masking on the column values. This type of masking is fixed masking, where the pattern is applied on the fixed length string.<br>These rules are used for the pattern:<br>• Use of # will include the digit from the position.<br>• Use x or any other character to mask the digit at that position.<br>• E.g. For SSN '000-00-0000' and pattern: 'XXX-XX-####' output would be like: XXX-XX-0000 |

**Code Snippet:**

```yaml
functions:
  - name: mask_number
    column: ssn
    pattern: XXX-XX-####
```

### **`merge`**

| Function | Description |
| --- | --- |
| `merge` | The *merge* function merges two or more columns by inserting a third column specified as asColumn into a row. The values in the third column are merged values from the specified columns delimited by a specified separator. |

**Code Snippet:**

```yaml
functions:
  - name: merge
    separator: "__"
    columns:
      - first_name
      - last_name
    asColumn: full_name
```

### **`parse_as_json`**

| Function | Description |
| --- | --- |
| `parse_as_json` | The *parse_as_json* function is for parsing a JSON object. The function can operate on String or JSON Object types. It requires spark schema json to parse the json back into dataframe. |

**Code Snippet:**

```yaml
functions:
  - name: parse_as_json
    column: json_string_column_name
    asColumn: column_name
    sparkSchema: "<spark_schema_json>"
    avroSchema: "<avro_schema>"
```

### **`parse_html`**

| Function | Description |
| --- | --- |
| `parse_html` | The *parse_html* function is used to convert the HTML-coded string to a normal string without any html tags. Here, asColumn is an optional parameter incase you wish to create a separate column for the processed data. Else, the processed data will replace the original column on which the function is performed. The function works using the jsoup library. More details about this library can be found here: https://github.com/jhy/jsoup |

**Code Snippet:**

```yaml
functions:
  - name: parse_html
    column: questionText
    asColumn: parsedText
```

### **`pivot`**

| Function | Description |
| --- | --- |
| `pivot` | The *pivot* function is used to pivot/rotate the data from one DataFrame/Dataset column into multiple columns (transform row to columns). <br>Here, values and approach are optional parameters. Also, aggregate_expression requires an alias to be written the same as the column name used with aggregate functions like sum, count, avg, etc. <br>Values can be used to specify only those columns needed after pivot from column . <br>Approach can be set to “two-phase” for running an optimized version query on large datasets. |

**Code Snippet:**

```yaml
functions:
  - name: pivot
    groupBy:
      - "Product"
      - "Country"
    column: "Country"
    values:
      - "USA"
      - "Mexico"
      - "India"
    aggregateExpression: "sum(Amount) as Amount"
    approach: "two-phase"
```

### **`rename`**

| Function | Description |
| --- | --- |
| `rename` | The *rename* function will change the name of a supplied column to a new column name. |

**Code Snippet:**

```yaml
functions:
  - name: rename
    column: column_name
    asColumn: new_column_name
```

### **`rename_all`**

| Function | Description |
| --- | --- |
| `rename_all` | The *rename_all* function will change the names of a supplied in columns to values. |

**Code Snippet:**

```yaml
functions:
  - name: rename_all
    columns:
      column1: new_column1
      column2: new_column2
```

### **`select`**

| Function | Description |
| --- | --- |
| `select` | The *select* function is used to keep specified columns from the record. This is the opposite behaviour of the DROP function. |

**Code Snippet:**

```yaml
functions:
  - name: select
    columns:
      - column_01
      - column_02
      - column_03
      - column_04
      - column_05
      - column_06
```

### **`set_column`**

| Function | Description |
| --- | --- |
| `set_column` | The *set_column* function will change name of a supplied in column to value in asColumn. |

**Code Snippet:**

```yaml
functions:
  - name: set_column
    column: my_col_name
    value: "some value here"
```

### **`set_type`**

| Function | Description |
| --- | --- |
| `set_type` | The `set_type` function converts the data type of a column. Here type can be one of the Spark data types e.g. int, string, long, double, etc. |

**Code Snippet:**

```yaml
functions:
  - name: set_type
    columns:
      column1: type
      column2: type
```

### **`set_variable`**

| Function | Description |
| --- | --- |
| `set_variable` | The *set_variable* function evaluates the expression supplied and sets the value in the variable. |

**Code Snippet:**

```yaml
functions:
  - name: set_variable
    column: some_new_column
    expression: "ROUND(AVG(src_bytes), 2)"
```

### **`snake_case`**

| Function | Description |
| --- | --- |
| `snake_case` | The *snake_case* function converts column names from camel case to snake case and is only applicable for batch dataframe/ job. |

**Code Snippet:**

```yaml
functions:
  - name: snake_case
```

### **`split_email`**

| Function | Description |
| --- | --- |
| `split_email` | The *split_email* function splits/parses an email ID into its two constituent parts: account and domain. After splitting the email address stored in the column within the column property, the directive will create two new columns, appending to the original column, named: column_account, and column_domain. If the email address cannot be parsed correctly, the additional columns will still be generated, but they would be set to null depending on the parts that could not be parsed. |

**Code Snippet:**

```yaml
functions:
  - name: split_email
    column: email_column
```

### **`split_url`**

| Function | Description |
| --- | --- |
| `split_url` | The *split_url* function splits a URL into protocol, authority, host, port, path, filename, and query. The function will parse the URL into its constituents. Upon splitting the URL, the directive creates seven new columns by appending to the original<br>column name: column_protocol<br>column_authority<br>column_host<br>column_port<br>column_path<br>column_filename<br>column_query<br>If the URL cannot be parsed correctly, an exception is thrown. If the URL column does not exist, columns with a null value are added to the record. |

**Code Snippet:**

```yaml
functions:
  - name: split_url
    column: column_with_url_content
```

### **`swap`**

| Function | Description |
| --- | --- |
| `swap` | The *swap* function swaps the column names of two columns. |

**Code Snippet:**

```yaml
functions:
  - name: swap
    columnA: col_1
    columnB: col_2
```

### **`trim`**

| Function | Description |
| --- | --- |
| `trim` | The *trim* function trim whitespace from both sides, left side or right side of string values they are applied to. One can supply method as trim/ltrim/rtrim |

**Code Snippet:**

```yaml
functions:
  - name: trim
    column: col_001
    method: trim
```

### **`unfurl`**

| Function | Description |
| --- | --- |
| `unfurl` | The *unfurl* function uses the expression supplied to pull columns from within the nested JSON attribute out e.g. columnName.* |

**Code Snippet:**

```yaml

functions:
  - name: unfurl
    expression: col01.*
  - name: unfurl
    expression: explode(col01)
```

### **`unpivot`**

| Function | Description |
| --- | --- |
| `unpivot` | The *unpivot* function works as the reverse function for the pivot function in which you can achieve rotating column values into rows values.  |

<aside>
🗣️ Both `pivotColumns` and `columns` can not have `-`,`*` need to specify a list of columns in at least one.

</aside>

**Code Snippets:**

```yaml
functions:
  - name: unpivot
    columns: # Columns can have - "*" if need to select all remaining columns than pivot columns
      - USA
      - Mexico
      - China
      - Canada
    pivotColumns: # pivotColumns can have - "*" if need to select all remaining columns than columns
      - Col1
      - Col2
      - Col3
    keyColumnName: Country
    valueColumnName: Amount
```

```yaml
functions:
  - name: unpivot
    columns: # Columns can have - "*" if need to select all remaining columns than pivot columns
      - "*"
    pivotColumns: # pivotColumns can have - "*" if need to select all remaining columns than columns
      - Col1
      - Col2
      - Col3
    keyColumnName: Country  # this name will be assigned to stack column
    valueColumnName: Amount # thid name will be assigned to values column
```

> **Note:** Make sure provided list has the same datatype else it will throw an error. Do not forget to clean the column before passing `*` in columns if column names have hyphens and spaces.
> 