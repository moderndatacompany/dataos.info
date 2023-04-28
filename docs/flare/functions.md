# Functions

Flare allows the user to use various functions for data manipulations at different stages of processing. The following list gives the details about the functions and their usage.

## any_date
| Function | Description 
| --------- | ------- | 
| *any_date* | The any_date function converts a date column given in any format like yyyy.mm.dd, dd.mm.yyyy, dd/MM/yy, yyyy/mm/dd and other(total 18 different format) into (yyyy-mm-dd) format.|

Snippet:
``` yaml
functions:
  - name: any_date
    column: __inq_date
    asColumn: inquiry_date
    rules: 
      - "【(?<year>\\d{4})\\W{1}(?<month>\\d{1,2})\\W{1}(?<day>\\d{1,2})[^\\d]? \\W*(?:at )?(?<hour>\\d{1,2}):(?<minute>\\d{1,2})(?::(?<second>\\d{1,2}))?(?:[.,](?<ns>\\d{1,9}))?(?<zero>z)?】"
              
```
> :material-alert: **Note**: You can provide explicit regex rules for the column passed in the **any_date** function. Without an explicit regex, the function will use the default format.
---------------------------------------------

## any_timestamp
| Function | Description 
| --------- | ------- | 
| *any_timestamp* | The any_timestamp function converts a timestamp column into the timestamp format as per the specified timezone.| 

Snippet:
``` yaml
functions:
  - name: any_timestamp
    column: transaction_date
    asColumn: transaction_date
    timezone: Asia/Kolkata
    rules:
      - "【(?<year>\\d{4})\\W{1}(?<month>\\d{1,2})\\W{1}(?<day>\\d{1,2})[^\\d]? \\W*(?:at )?(?<hour>\\d{1,2}):(?<minute>\\d{1,2})(?::(?<second>\\d{1,2}))?(?:[.,](?<ns>\\d{1,9}))?(?<zero>z)?】"
              
``` 
> :material-alert: **Note**: You can provide explicit regex rules for the column passed in the **any_timestamp** function. Without an explicit regex, the function will use the default format.
---------------------------------------------

## change_case
| Function | Description 
| --------- | ------- | 
| *change_case* |The UPPERCASE, LOWERCASE, and TITLECASE functions change the case (`lower/upper/title`) of column values they are applied to. | 

Snippet:
``` yaml
 functions:
  - name: change_case
    case: lower
    column: asin
```
---------------------------------------------
## cleanse_column_names
| Function | Description |
| --------- | ------- |
| *cleanse_column_names* | The CLEANSE-COLUMN-NAMES function sanatizes column names, following these rules:
 | | 1. Trim leading and trailing spaces
 | | 2. Lowercases the column name
 | | 3. Replaces any character that are not one of [A-Z][a-z][0-9] or `_` with an underscore `(_)` |

 Snippet: 
``` yaml
 functions:
  - name: cleanse_column_names
```
---------------------------------------------
## cut_character
| Function | Description |
| --------- | ------- |
| *cut_character* | The CUT_CHARACTER function selects parts of a string value, accepting standard cut options. |

Snippet: 
``` yaml
functions:
  - name: cut_character
    column: title
    asColumn: title_prefix
    startIndex: 1
    endIndex: 5
```
---------------------------------------------
## decode
| Function | Description |
| --------- | ------- |
| *decode* | The DECODE function decodes a column value as one of `base32`, `base64`, or `hex` following RFC-4648 and adds one more column like `- col1_decode_base32` |

Snippet:
``` yaml
functions:
  - name: decode
    algo: base64
    column: id
    asColumn: id_1
```
---------------------------------------------
## drop
| Function | Description 
| --------- | ------- |
| *drop* | The DROP function is used to drop the specified columns in a record. |

Snippet:
``` yaml
functions:
  - name: drop
    columns:
        - column_1
        - column_2
```
---------------------------------------------
## encode
| Function | Description |
| --------- | ------- |
| *encode* | The ENCODE function encodes a column value as one of `base32`, `base64`, or `hex` following RFC-4648 and adds one more column like `- col1_encode_base32` |

Snippet: 
``` yaml
functions:
  - name: encode
    algo: base64
    column: id
    asColumn: id_2

```
---------------------------------------------
## diff_date
| Function | Description |
| --------- | ------- |
| *diff_date* | The DIFF_DATE function calculates the difference between two dates. |

Snippet: 
``` yaml
functions:
  - name: diff_date
    columnA: col_a
    columnB: col_b
    asColumn: col_diff_date
```
---------------------------------------------
## fill_null_or_empty
| Function | Description |
| --------- | ------- |
| *fill_null_or_empty* | The FILL_NULL_OR_EMPTY function fills column value with a fixed value if it is either null or empty (""). If the `column` does not exist, the function will fail. The `defaultValue` can only be of type string. |

Snippet:
``` yaml
functions:
  - name: fill_null_or_empty
    columns: 
      column1: value1
      column2: value2
```
---------------------------------------------

## find_and_replace
| Function | Description |
| --------- | ------- |
| *find_and_replace* | The FIND_AND_REPLACE function transforms string column values using a "sed"-like expression to find and replace text within the same column. |

Snippet: 
``` yaml
functions:
  - name: find_and_replace
    column: title
    sedExpression: "s/regex/replacement/g"
```
---------------------------------------------
## flatten
| Function | Description |
| --------- | ------- |
| *flatten* | The FLATTEN function separates the elements in a repeated field into individual records. It is useful for the flexible exploration of repeated data. To maintain the association between each flattened value and the other fields in the record, the FLATTEN directive copies all of the other columns into each new record. |

Snippet:
``` yaml
functions:
  - name: flatten
    column: array_holding_column
    asColumn: new_column_name
```
---------------------------------------------
## format_date
| Function | Description |
| --------- | ------- |
| *format_date* | The FORMAT_DATE function allows custom patterns for date-time formatting. It formats the date value according to the format string.

  |

Snippet:
``` yaml
functions:
  - name: format_date
    column: date_column
    format: "yyyy-MM-dd'T'HH:mm:ss"
```
---------------------------------------------
## format_unix_date
| Function | Description |
| --------- | ------- |
| *format_unix_date* | The FORMAT_UNIX_DATE function allows custom patterns for date-time formatting. |

Snippet:
``` yaml
functions:
  - name: format_unix_date
    column: unix_epoch_column
    format: "yyyy-MM-dd'T'HH:mm:ss"
```
---------------------------------------------
## generate_uuid
| Function | Description |
| --------- | ------- |
| *generate_uuid* | The GENERATE_UUID function generates a universally unique identifier (UUID) of the record. |

Snippet:
```  yaml
functions:
  - name: generate_uuid
    asColumn: column_01
```
---------------------------------------------
## hash
| Function | Description |
| --------- | ------- |
| *hash* | The HASH function generates a message digest. The column is replaced with the digest created using the supplied algorithm. The type of column is a string.|

Snippet:
``` yaml
functions:
  - name: hash
    column: column_to_hash
    algo: MD5 | SHA-1 | SHA-256 | SHA-384 | SHA-512
```
---------------------------------------------
## increment_variable
| Function | Description |
| --------- | ------- |
| *increment_variable* | The INCREMENT_VARIABLE function increments the value of the variable that is local to the input record being processed. |

Snippet:
``` yaml
functions:
  - name: increment_variable
    column: column_01
```
---------------------------------------------
## mask_number
| Function | Description |
| --------- | ------- |
| *mask_number* | The MASK_NUMBER function applies substitution masking on the column values. The 'column' specifies the name of an existing column to be masked. The 'pattern' is a substitution pattern to be used to mask the column values. Substitution masking is generally used for masking credit cards or social security numbers. The MASK_NUMBER applies substitution masking on the column values. This type of masking is fixed masking, where the pattern is applied on the fixed-length string. These rules are used for the pattern:
<ul><li>1. Use of # will include the digit from the position</li><li>2. Use x or any other character to mask the digit at that position e.g. For SSN '000-00-0000' and pattern: 'XXX-XX-####' output would be like: XXX-XX-0000</li></ul> |

Snippet:
``` yaml
functions:
  - name: mask_number
    column: ssn
    pattern: XXX-XX-####
```

---------------------------------------------
## merge
| Function | Description 
| --------- | ------- | 
| *merge* | The MERGE function merges two or more columns by inserting a third column specified as `asColumn` into a row. The values in the third column are merged values from the specified `columns` delimited by a specified `separator`.

Snippet:
``` yaml
functions:
  - name: merge
    separator: "__"
    columns:
      - first_name
      - last_name
    asColumn: full_name
```
---------------------------------------------
## parse_as_json
| Function | Description |
| --------- | ------- |
| *parse_as_json* | The PARSE_AS_JSON function is for parsing a JSON object. The function can operate on String or JSON object types. It requires spark schema json to parse the json back into dataframe. |

Snippet:
``` yaml
functions:
  - name: parse_as_json
    column: json_string_column_name
    asColumn: column_name
    sparkSchema: "<spark_schema_json>"
    avroSchema: "<avro_schema>"
```
---------------------------------------------
## parse_html
| Function | Description |
| --------- | ------- |
| *parse_html* | The parse-html function is used to create a new column asColumn by converting the HTML coded string in column. |

> :material-alert: **Note**: The function works using the jsoup library. You can find more details about this library here:

> <a href="https://github.com/jhy/jsoup" target="_blank">GitHub - jhy/jsoup: jsoup: the Java HTML parser, built for HTML editing, cleaning, scraping, and XSS safety </a>.


Snippet:
``` yaml
functions:
  - name: parse_html
    column: questionText
    asColumn: parsedText
```
---------------------------------------------
## pivot
| Function | Description |
| --------- | ------- |
| *pivot* | The Pivot function is used to reorganise data stored in a DataFrame/Dataset. It allows you to rotate unique values from one column in the expression into multiple columns in the output. It allows getting aggregated values based on specific column values. These values will appear as columns in the result. 

**Parameters:**

<ul><li>aggregate_expression: requires an aggregate function(sum, count, avg etc)along with alias.</li>

<li>values(optional): specifies only those values needed after pivot from column.</li>

<li>approach(optional): can be  set to “two-phase” for running an optimised version query on large datasets.</li></ul>

Snippet:
``` yaml
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
---------------------------------------------

## rename_all
| Function | Description |
| --------- | ------- |
| *rename* | The RENAME_ALL function will rename all supplied columns with the corresponding given column names.

Snippet:
``` yaml
functions:
  - name: rename_all
    columns:
      column1: new_column1
      column2: new_column2
    
    
```
---------------------------------------------
## select
| Function | Description |
| --------- | ------- |
| *select* | The SELECT function is used to keep specified columns from the record. This is the opposite behavior of the DROP function. |

Snippet:
``` yaml
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
---------------------------------------------
## set_column
| Function | Description |
| --------- | ------- |
| *set_column* | The SET_COLUMN  function will change name of a supplied in `column` to value in `asColumn`. |

Snippet:
``` yaml
functions:
  - name: set_column
    column: my_col_name
    value: "some value here"
```
---------------------------------------------
## set_type
| Function | Description |
| --------- | ------- |
| *set_type* | Convert data type of given columns. Here `type` can be one of spark data types e.g. int, string, long, double etc. |

Snippet:
``` yaml
functions:
  - name: set_type
    columns:
      column1: type
      column2: type
```
---------------------------------------------
## set_variable
| Function | Description |
| --------- | ------- |
| *set_variable* | The SET_VARIABLE  function evaluates the expression supplied and sets the value in the variable. |

Snippet:
``` yaml
functions:
  - name: set_variable
    column: some_new_column
    expression: "ROUND(AVG(src_bytes), 2)"
```
---------------------------------------------
## snake_case
| Function | Description |
| --------- | ------- |
| *snake_case* | The SNAKE_CASE function converts column names from camel case to snake case and is only applicable for batch dataframe/ job. |

Snippet:
``` yaml
functions:
  - name: snake_case
```
---------------------------------------------
## split_email
| Function | Description |
| --------- | ------- |
| *split_email* |The SPLIT_EMAIL function splits an email ID into an account and its domain. The `column` is a column containing an email address. The function will parse email address into its constituent parts: account and domain. After splitting the email address, the directive will create two new columns, appending to the original column name: <ul><li>column_account</li><li>column_domain</li></ul>If the email address cannot be parsed correctly, the additional columns will still be generated, but they would be set to null depending on the parts that could not be parsed.

Snippet:
``` yaml
functions:
   - name: split_email
     column: email_column
```
---------------------------------------------
## split_url
| Function | Description |
| --------- | ------- |
| *split_url* | The SPLIT_URL function splits a URL into protocol, authority, host, port, path, filename, and query. The SPLIT_URL function will parse the URL into its constituents. Upon splitting the URL, the directive creates seven new columns by appending to the original column name: <ul><li>column_authority</li><li>column_protocol</li><li>column_host</li><li>column_port</li><li>column_path</li><li>column_filename</li><li>column_query</li></ul> If the URL cannot be parsed correctly, an exception is throw. If the URL column does not exist, columns with a null value are added to the record.

Snippet:
``` yaml
functions:
  - name: split_url
    column: column_with_url_content
```
---------------------------------------------
## swap
| Function | Description |
| --------- | ------- |
| *swap* | The SWAP function swaps column names of two columns. |

Snippet:
``` yaml
functions:
  - name: swap
    columnA: col_1
    columnB: col_2
```
---------------------------------------------
## trim
| Function | Description |
| --------- | ------- |
| *trim* | The TRIM function trim whitespace from both sides, left side or right side of string values they are applied to. One can supply `method` as `trim|ltrim|rtrim` |

Snippet:
``` yaml
functions:
  - name: trim
    column: col_001
    method: trim
```
---------------------------------------------
## unfurl
| Function | Description |
| --------- | ------- |
| *unfurl* | The UNFURL function uses the expression supplied to pull columns from within the nested json attribute out e.g. `columnName.*` |

Snippet:
``` yaml
functions:
  - name: unfurl
    expression: "col01.*"
  - name: unfurl
    expression: explode("col01")
```
---------------------------------------------

