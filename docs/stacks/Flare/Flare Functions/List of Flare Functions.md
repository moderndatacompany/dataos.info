# List of Flare Functions

## add_column

| Function | add_column |
| --- | --- |
| Description | The add_column function adds a new column. The supported types are `string`, `boolean`, `byte`, `short`, `int`, `long`, `float`, `double`, `decimal`, `date`, and `timestamp`. |

Code Snippet:

```yaml
functions: 
	- name: add_column # Name of the Function
		column: new_column_name # Name of the Column to be added
		value: some_value # Value could be of any format
		type: int # Supported types: string/boolean/byte/short/int/long/float/double/decimal/date/timestamp
```

> Note: In the event that the specified data type is not among the supported options, the `add_column` function will return an Invalid datatype found error.
> 

## any_date

| Function | any_date |
| --- | --- |
| Description | The any_date function converts the `string` to date type while parsing the string based on the rule provided. Using the by default rule, it converts a date column given in any format like `yyyy.mm.dd`, `dd.mm.yyyy`, `dd/MM/yy`, `yyyy/mm/dd`, and other (total 18 different formats) into `yyyy-mm-dd` format.  The `rule` should be a regular expression. |

Code Snippet:

```yaml
functions: 
	- name: any_date # Name of the function
		column: date_string_column_name # Name of the Column Initially
		asColumn: column_name # Name of the Column where the converted data is stored
#		rule: 
#			- "【(?<year>\\d{4})\\W{1}(?<month>\\d{1,2})\\W{1}(?<day>\\d{1,2})
# [^\\d]? \\W*(?:at )?(?<hour>\\d{1,2}):(?<minute>\\d{1,2})
# (?::(?<second>\\d{1,2}))?(?:[.,](?<ns>\\d{1,9}))?(?<zero>z)?】"
```

> Note: You can provide explicit regex `rules` for the column passed in the any_date function. Without an explicit regex, the function will use the default rule.
> 

## any_timestamp

| Function | any_timestamp |
| --- | --- |
| Description | The any_timestamp function converts a `string` to `timestamp` type while parsing the string based on the rule provided. The timestamp format is as per the specified `timezone`. The `rule` should be a regular expression. |

Code Snippet:

```yaml
functions: 
	- name: any_timestamp # Name of the function
		column: datetime_string_column_name # Name of the Column
		asColumn: column_name # Name of the Column after conversion
		timezone: Asia/Kolkata # Timezone
#   rules:
#     - "【(?<year>\\d{4})\\W{1}(?<month>\\d{1,2})\\W{1}(?<day>\\d{1,2})[^\\d]? \\W*(?:at )?(?<hour>\\d{1,2}):(?<minute>\\d{1,2})(?::(?<second>\\d{1,2}))?(?:[.,](?<ns>\\d{1,9}))?(?<zero>z)?】"
```

> Note: You can provide explicit regex `rules` for the column passed in the any_timestamp function. Without an explicit regex, the function will use the default rule.
> 

## change_case

| Function | change_case |
| --- | --- |
| Description | The change_case function alters the columns `case` to Lowercase, Uppercase, or Titlecase depending upon the applied lower/upper/title `case` changes the column values . |

Code Snippet:

```yaml
functions: 
	- name: change_case # Name of the function
		case: lower # Available Cases: lower/upper/title
		column: asin # Name of the column where function is applied
```

## change_column_case

| Function | change_column_case |
| --- | --- |
| Description | The CHANGE-COLUMN-CASE function changes column names(all columns) to either lowercase or uppercase based on value of <br>`case: lower/upper`. |

Code Snippet:

```yaml
functions: 
	- name: change_column_case 
		case: upper
```

## cleanse_column_names

| Function | cleanse_column_names |
| --- | --- |
| Description | The CLEANSE-COLUMN-NAMES function sanatizes column names, following these rules: <br> • Trim leading and trailing spaces <br> • Lowercases the column name <br> • Replaces any character that are not one of `[A-Z][a-z][0-9]` or _ with an underscore `(_)` |

Code Snippet:

```yaml
functions: 
	- name: cleanse_column_names
```

## columns_replace

| Function | columns_replace |
| --- | --- |
| Description | The COLUMNS_REPLACE function alters column names in bulk. |

Code Snippet:

```yaml
functions: 
	- name: columns_replace 
		sedExpression: 's/^data_//g'
```

## copy

| Function | copy |
| --- | --- |
| Description | The COPY function copies values from a source column into a destination column. |

Code Snippet:

```yaml
functions: 
	- name: copy 
		fromColumn: source_column_name 
		toColumn: destination_column_name
```

## cut_character

| Function | cut_character |
| --- | --- |
| Description | The CUT_CHARACTER function selects parts of a `string` value, accepting standard cut options. |

Code Snippet:

```yaml
functions: 
  - name: cut_character 
    column: title 
    asColumn: title_prefix 
    startIndex: 1 
    endIndex: 5
```

## decode

| Function | decode |
| --- | --- |
| Description | The DECODE function decodes a column value as one of base32, base64, or hex following RFC-4648 - `col1_decode_base32` |

Code Snippet:

```yaml
functions: 
  - name: decode 
    algo: base64 
    column: col1 
    asColumn: new_col1
```

## diff_date

Code Snippet:

```yaml
functions: 
  - name: diff_date 
    columnA: col_a 
    columnB: col_b 
    asColumn: col_diff_date
```

## drop

| Function | drop |
| --- | --- |
| Description | The DROP function is used to drop a column in a record. |

Code Snippet:

```yaml
functions: 
	- name: drop 
    columns: 
				- column_1 
				- column_2
```

## drop_duplicates

| Function | drop_duplicates |
| --- | --- |
| Description | The function removes all the duplicate elements from a list of columns. |

Code Snippet:

```yaml
functions: 
	- name: drop_duplicates 
		columns: 
				- column1 
				- column2
```

## encode

| Function | encode |
| --- | --- |
| Description | The ENCODE function encodes a column value as one of `base32` , `base64`, or `hex` following RFC-4648 - `col1_encode_base32`. |

Code Snippet:

```yaml
functions: 
	- name: encode 
		algo: base64 
		column: col1 
		asColumn: new_col1
```

## epoch_to_timestamp

| Function | epoch_to_timestamp |
| --- | --- |
| Description | The function converts `epoch string` to `timestamp format`. |

Code Snippet:

```yaml
functions: 
	- name: epoch_to_timestamp 
		column: epoch_column 
		asColumn: date_column
```

## fill_null_or_empty

| Function | fill_null_or_empty |
| --- | --- |
| Description | The FILL_NULL_OR_EMPTY function fills column value with a fixed value if it is either null or empty ("").<br> If the `column` does not exist, then the function will fail.<br> The `defaultValue` can only be of type `string`. |

Code Snippet:

```yaml
functions: 
	- name: fill_null_or_empty 
		columns: 
			column1: value1 
			column2: value2
```

## find_and_replace

| Function | find_and_replace |
| --- | --- |
| Description | The FIND_AND_REPLACE function transforms `string` column values using a "sed"-like expression to find and replace text within the same column. |

Code Snippet:

```yaml
functions: 
	- name: find_and_replace 
		column: title 
		sedExpression: "s/regex/replacement/g"
```

## flatten

| Function | flatten |
| --- | --- |
| Description | The FLATTEN function separates the elements in a repeated field into individual records.<br> The FLATTEN function is useful for the flexible exploration of repeated data. To maintain the association between each flattened value and the other fields in the record, the FLATTEN directive copies all of the other columns into each new record. <br> Note :- Use `flatten_outer` when array has null values and you want records of root with null in flattened columns.  |

Code Snippet:

```yaml
functions: 
	- name: flatten 
		column: array_holding_column 
		asColumn: new_column_name
```

## format_date

| Function | format_date |
| --- | --- |
| Description | The FORMAT_DATE function allows custom patterns for date-time formatting. |

Code Snippet:

```yaml
functions: 
	- name: format_date 
		column: date_column 
		format: "yyyy-MM-dd'T'HH:mm:ss"
```

## format_unix_date

| Function | format_unix_date |
| --- | --- |
| Description | The FORMAT_UNIX_DATE function allows custom patterns for date-time formatting. |

Code Snippet:

```yaml
functions: 
	- name: format_unix_date 
		column: unix_epoch_column 
		format: "yyyy-MM-dd'T'HH:mm:ss"
```

## generate_uuid

| Function | generate_uuid |
| --- | --- |
| Description | The GENERATE_UUID function generates a universally unique identifier (UUID) of the record. |

Code Snippet:

```yaml
functions: 
	- name: generate_uuid 
		asColumn: column_01
```

## hash

| Function | hash |
| --- | --- |
| Description | The HASH function generates a message digest. The column is replaced with the digest created using the supplied algorithm. The type of column is a string. |

Code Snippet:

```yaml
functions: 
	- name: hash 
		column: column_to_hash 
		algo: MD5 | SHA-1 | SHA-256 | SHA-384 | SHA-512
```

## increment_variable

| Function | increment_variable |
| --- | --- |
| Description | The INCREMENT_VARIABLE function increments the value of the variable that is local to the input record being processed. |

Code Snippet:

```yaml
functions: 
	- name: increment_variable 
		column: column_01
```

## mask_number

| Function | mask_number |
| --- | --- |
| Description | The MASK_NUMBER function applies substitution masking on the column values. <br><br> The 'column' specifies the name of an existing column to be masked. <br><br> The 'pattern' is a substitution pattern to be used to mask the column values. <br><br> Substitution masking is generally used for masking credit card or social security numbers. The MASK_NUMBER applies substitution masking on the column values. This type of masking is fixed masking, where the pattern is applied on the fixed length string.  <br><br> These rules are used for the pattern: <br> • Use of # will include the digit from the position. <br> • Use x or any other character to mask the digit at that position. <br> • E.g. For SSN '000-00-0000' and pattern: `'XXX-XX-####'` output would be like: `XXX-XX-0000` |

Code Snippet:

```yaml
functions: 
	- name: mask_number \
		column: ssn 
		pattern: XXX-XX-####
```

## merge

| Function | merge |
| --- | --- |
| Description | The MERGE function merges two or more columns by inserting a third column specified as `asColumn` into a row. The values in the third column are merged values from the specified `columns` delimited by a specified `separator`. |

Code Snippet:

```yaml
functions: 
	- name: merge 
		separator: "__" 
		columns: 
			- first_name 
			- last_name 
		asColumn: full_name
```

## parse_as_json

| Function | parse_as_json |
| --- | --- |
| Description | The PARSE_AS_JSON function is for parsing a JSON object. The function can operate on String or JSONObject types. It requires spark schema json to parse the json back into dataframe. |

Code Snippet:

```yaml
functions: 
	- name: parse_as_json 
		column: json_string_column_name 
		asColumn: column_name 
		sparkSchema: "<spark_schema_json>" 
		avroSchema: "<avro_schema>"
```

## parse_html

| Function | parse_html |
| --- | --- |
| Description | The parse-html function is used to convert the HTML-coded string to a normal string without any html tags. <br> Here, asColumn is an optional parameter incase you wish to create a separate column for the processed data. Else, the processed data will replace the original column on which the function is performed. <br> The function works using the jsoup library. More details about this library can be found `https://github.com/jhy/jsoup` |

Code Snippet:

```yaml
functions: 
	- name: parse_html 
		column: questionText 
		asColumn: parsedText
```

## pivot

| Function | pivot |
| --- | --- |
| Description | The pivot function is used to pivot/rotate the data from one DataFrame/Dataset column into multiple columns (transform row to columns). <br><br> Here, `values` and `approach` are optional parameters. Also, `aggregate_expression` requires an alias to be written the same as the column name used with aggregate functions like sum, count, avg, etc. <br><br> `values` can be used to specify only those columns needed after pivot from `column` . `approach` can be set to “two-phase” for running an optimized version query on large datasets. |

Code Snippet:

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

## rename

| Function | rename |
| --- | --- |
| Description | The RENAME function will change the name of a supplied column to a new column name. |

Code Snippet:

```yaml
functions: 
	- name: rename 
		column: column_name 
		asColumn: new_column_name
```

## rename_all

| Function | rename_all |
| --- | --- |
| Description | The RENAME ALL function will change the names of a supplied in columns to values. |

Code Snippet:

```yaml
functions: 
	- name: rename_all 
		columns: 
			column1: new_column1 
			column2: new_column2
```

## select

| Function | select |
| --- | --- |
| Description | The SELECT function is used to keep specified columns from the record. This is the opposite behaviour of the DROP function. |

Code Snippet:

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

## set_column

| Function | set_column |
| --- | --- |
| Description | The SET_COLUMN function will change name of a supplied in column to value in `asColumn`. |

Code Snippet:

```yaml
functions: 
	- name: set_column 
		column: my_col_name 
		value: "some value here"
```

## set_type

| Function | set_type |
| --- | --- |
| Description | Convert the data `type` of a column. Here type can be one of the spark data types e.g. `int`, `string`, `long`, `double`, etc. |

Code Snippet:

```yaml
functions: 
	- name: set_type 
		columns: 
			column1: type 
			column2: type
```

## set_variable

| Function | set_variable |
| --- | --- |
| Description | The SET_VARIABLE function evaluates the expression supplied and sets the value in the variable. |

Code Snippet:

```yaml
functions: 
	- name: set_variable 
		column: some_new_column 
		expression: "ROUND(AVG(src_bytes), 2)"
```

## snake_case

| Function | snake_case |
| --- | --- |
| Description | The snake_case function converts column names from camel case to snake case and is only applicable for batch dataframe/ job. |

Code Snippet:

```yaml
functions: 
	- name: snake_case
```

## split_email

| Function | split_email |
| --- | --- |
| Description | The split_email function splits/parses an email ID into its two constituent parts: account and domain. After splitting the email address stored in the column within the `column` property, the directive will create two new columns, appending to the original column, named: `column_account`, and `column_domain`. If the email address cannot be parsed correctly, the additional columns will still be generated, but they would be set to null depending on the parts that could not be parsed. |

Code Snippet:

```yaml
functions: 
	- name: split_email 
		column: email_column
```

## split_url

| Function | split_url |
| --- | --- |
| Description | The split_url function splits a URL into protocol, authority, host, port, path, filename, and query. The function will parse the URL into its constituents. Upon splitting the URL, the directive creates seven new columns by appending to the original column name: <br>`column_protocol`<br>` column_authority`<br> `column_host`<br> `column_port`<br> `column_path`<br> `column_filename`<br> `column_query`<br> If the URL cannot be parsed correctly, an exception is thrown. If the URL column does not exist, columns with a null value are added to the record. |

Code Snippet:

```yaml
functions: 
	- name: split_url 
		column: column_with_url_content
```

## swap

| Function | swap |
| --- | --- |
| Description | The swap function swaps the column names of two columns. |

Code Snippet:

```yaml
functions: 
	- name: swap 
		columnA: col_1 
		columnB: col_2
```

## trim

| Function | trim |
| --- | --- |
| Description | The trim function trim whitespace from both sides, left side or right side of string values they are applied to. One can supply `method` as `trim|ltrim|rtrim` |

Code Snippet:

```yaml
functions: 
	- name: trim 
		column: col_001 
		method: trim
```

## unfurl

| Function | unfurl |
| --- | --- |
| Description | The `unfurl` function uses the expression supplied to pull columns from within the nested JSON attribute out e.g. `columnName.*` |

Code Snippet:

```yaml
functions: 
	- name: unfurl 
		expression: col01.* 
	- name: unfurl 
		expression: explode(col01)
```

## unpivot

| Function | unpivot |
| --- | --- |
| Description | The unpivot function works as the reverse function for the pivot function in which you can achieve rotating column values into rows values.  |


> 🗣️ Both `pivotColumns` and `columns` can not have `-`,`*` need to specify a list of columns in at least one.

Code Snippets:

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

> Note: Make sure provided list has the same datatype else it will throw an error. Do not forget to clean the column before passing `*` in columns if column names have hyphens and spaces.
>