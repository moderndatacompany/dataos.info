# List of Flare Functions


### **`add_column`**

| Function | Description |
| --- | --- |
| `add_column` | The *add_column* function adds a new column. The supported types are string, boolean, byte, short, int, long, float, double, decimal, date, and timestamp. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: add_column 
        column: {{new_column_name}} 
        value: {{some_value}} 
        type: {{int}}
    ```
=== "Example"

    ```yaml title="add_column.yaml" hl_lines="51-55"
    --8<--  "examples/resources/stacks/flare/functions/add_column.yaml"
    ```

    Output

    ```shell
    | order_amount |
    |--------------|
    |      8       |
    |      8       |
    ```

</div>

!!! note
    In the event that the specified data type is not among the supported options, the `add_column` function will return an **Invalid datatype found** error.


### **`any_date`**

| Function | Description |
| --- | --- |
| `any_date` | The *any_date* function converts the string to date type while parsing the string based on the rule provided. Using the by default rule, it converts a date column given in any format like yyyy.mm.dd, dd.mm.yyyy, dd/MM/yy, yyyy/mm/dd, and other (total 18 different formats) into yyyy-mm-dd format.  The rule should be a regular expression. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml 
    functions:
      - name: any_date 
        column: {{date_string_column_name}} 
        asColumn: {{column_name}} 
        rule: 
          - "【(?<year>\\d{4})\\W{1}(?<month>\\d{1,2})\\W{1}(?<day>\\d{1,2})[^\\d]? \\W*(?:at )?(?<hour>\\d{1,2}):(?<minute>\\d{1,2})(?::(?<second>\\d{1,2}))?(?:[.,](?<ns>\\d{1,9}))?(?<zero>z)?】"
    ```
=== "Example"

    ```yaml title="any_date.yaml" hl_lines="51-56"
      --8<--  "examples/resources/stacks/flare/functions/any_date.yaml"
    ```

    Output

    ```shell
    +--------------------+----------+
    |            END_YEAR|  year_end|
    +--------------------+----------+
    |2020-03-01T05:07:38Z|2020-03-01|
    |2021-03-07T05:07:38Z|2021-03-07|
    +--------------------+----------+
    ```
</div>

!!! note
    You can provide explicit regex `rules` for the column passed in the **any_date** function. Without an explicit regex, the function will use the default rule.


### **`any_timestamp`**

| Function | Description |
| --- | --- |
| `any_timestamp` | The *any_timestamp* function converts a string to timestamp type while parsing the string based on the rule provided. The timestamp format is as per the specified timezone. The rule should be a regular expression. |

<div  class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: any_timestamp 
        column: {{datetime_string_column_name}} 
        asColumn: {{column_name}} 
        timezone: {{Asia/Kolkata}}
        rules:
          - "【(?<year>\\d{4})\\W{1}(?<month>\\d{1,2})\\W{1}(?<day>\\d{1,2})[^\\d]? \\W*(?:at )?(?<hour>\\d{1,2}):(?<minute>\\d{1,2})(?::(?<second>\\d{1,2}))?(?:[.,](?<ns>\\d{1,9}))?(?<zero>z)?】"
    ```

=== "Example"

    ```yaml title="any_timestamp.yaml" hl_lines="51-60"
      --8<--  "examples/resources/stacks/flare/functions/any_timestamp.yaml"
    ```       
    Output

    ```shell
    +--------------------+-------------------+
    |            END_YEAR|      END_YEAR_ASIA|
    +--------------------+-------------------+
    |2020-03-01T05:07:38Z|2020-03-01 10:37:38|
    |2021-03-07T05:07:38Z|2021-03-07 10:37:38|
    +--------------------+-------------------+
    ```
    for 'timezone': America/New_York
     
    ```shell
    +--------------------+-------------------+
    |            END_YEAR|   END_YEAR_AMERICA|
    +--------------------+-------------------+
    |2020-03-01T05:07:38Z|2020-03-01 00:07:38|
    |2021-03-07T05:07:38Z|2021-03-07 00:07:38|
    +--------------------+-------------------+
    ```
</div>

!!! note 
    You can provide explicit regex `rules` for the column passed in the **any_timestamp** function. Without an explicit regex, the function will use the default rule.


### **`change_case`**

| Function | Description |
| --- | --- |
| `change_case` | The change_case function alters the values in the column to a specified case (Lowercase, Uppercase, or Titlecase), depending on the applied transformation. It does not affect the column name but modifies the data within the column. For example, if the value is 'John Doe' and the function is applied with Uppercase, the value will change to 'JOHN DOE'.
 |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
      functions:
        - name: change_case 
          case: {{lower/upper/title}} 
          column: {{asin}} 
    ```
=== "Example"

    ```yaml title="change_case.yaml" hl_lines="51-54"
      --8<--  "examples/resources/stacks/flare/functions/change_case.yaml"
    ```
    Output

    patient column in lower case will be displayed

    ```shell
    +--------------------+--------------------+
    |             patient|            MEMBERID|
    +--------------------+--------------------+
    |b9c610cd-28a6-463...|bca22051-b39b-759...|
    |b9c610cd-28a6-463...|bca22051-b39b-759...|
    +--------------------+--------------------+
    ```
</div>

### **`change_column_case`**

| Function | Description |
| --- | --- |
| `change_column_case` | The *change_column_case* function changes column names(all columns) to either lowercase or uppercase based on value of case: lower/upper. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
      functions:
        - name: change_column_case 
          case: {{upper}} 
    ```
=== "Example"

    ```yaml title="change_column_case.yaml" hl_lines="51-53"
      --8<--  "examples/resources/stacks/flare/functions/change_column_case.yaml"
    ```

    Output

    ```shell
    +--------------------+--------------------+
    |          PATIENT   |            MEMBERID|
    +--------------------+--------------------+
    |b9c610cd-28a6-463...|bca22051-b39b-759...|
    |b9c610cd-28a6-463...|bca22051-b39b-759...|
    +--------------------+--------------------+
    ```
</div>

### **`cleanse_column_names`**

| Function | Description |
| --- | --- |
| `cleanse_column_names`  | The *cleanse_column_names* function sanatizes column names, following these rules: <br> • Trim leading and trailing spaces <br> • Lowercases the column name <br> • Replaces any character that are not one of [A-Z][a-z][0-9] or _ with an underscore (_) |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
      functions:
        - name: cleanse_column_names
    ```
=== "Example"

    ```yaml title="cleanse_column_names" hl_lines="51-54"
    --8<--  "examples/resources/stacks/flare/functions/cleanse_column_names.yaml"
    ```

    Before

    ```shell
    +----------------------+----------------------+
    |          PATIENT     |       MEMBERID      |
    +----------------------+----------------------+
    |b9c610cd-28a6-463...  |bca22051-b39b-759...  |
    |b9c610cd-28a6-463...  |bca22051-b39b-759...  |
    +----------------------+----------------------+
    ```
    After
    
    ```shell
    +----------------------+----------------------+
    |patient               |memberid              |
    +----------------------+----------------------+
    |b9c610cd-28a6-463...  |bca22051-b39b-759...  |
    |b9c610cd-28a6-463...  |bca22051-b39b-759...  |
    +----------------------+----------------------+
    ```
</div>

### **`columns_replace`**

| Function | Description |
| --- | --- |
| `columns_replace` | The *columns_replace* function alters column names in bulk. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
        functions:
          - name: columns_replace
            sedExpression: 's/^string_/new_/g' #any column that starts with string_ will be replaced by new_
    ```

=== "Example"

    ```yaml title="columns_replace.yaml" hl_lines="52-54"
    --8<--  "examples/resources/stacks/flare/functions/columns_replace.yaml"
    ```
    Before

    ```shell
    +--------------------+---------------+---------+
    |             PATIENT|num_days_stay  |stay_days|
    +--------------------+---------------+---------+
    |b9c610cd-28a6-463...|            -23|     null|
    |b9c610cd-28a6-463...|              6|     null|
    +--------------------+---------------+---------+
    ```
    After

    ```shell
    +--------------------+---------------+----------+
    |     PATIENT        |num_days_stayed|stayed_days|
    +--------------------+---------------+-----------+
    |b9c610cd-28a6-463...|            -23|     null  |
    |b9c610cd-28a6-463...|              6|     null  |
    +--------------------+---------------+-----------+
    ```
</div>

### **`copy`**

| Function | Description |
| --- | --- |
| `copy` | The *copy* function copies values from a source column into a destination column. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
      functions:
        - name: copy
          fromColumn: {{source_column_name}}
          toColumn: {{destination_column_name}}
    ```
=== "Example"

    ```yaml title="copy.yaml" hl_lines="51-54"
    --8<--  "examples/resources/stacks/flare/functions/copy.yaml"
    ```
    Before

    ```shell
    +--------------------+---------------+
    |               PAYER|SECONDARY_PAYER|
    +--------------------+---------------+
    |7c4411ce-02f1-39b...|           null|
    |7c4411ce-02f1-39b...|           null|
    +--------------------+---------------+
    ```
    After

    ```shell
    +--------------------+--------------------+
    |               PAYER|SECONDARY_PAYER     |
    +--------------------+--------------------+
    |7c4411ce-02f1-39b...|7c4411ce-02f1-39b...|
    |7c4411ce-02f1-39b...|7c4411ce-02f1-39b...|
    +--------------------+--------------------+
    ```
</div> 

### **`cut_character`**

| Function | Description |
| --- | --- |
| `cut_character` | The *cut_character* function selects parts of a string value, accepting standard cut options. |


<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions: 
      - name: cut_character 
        column: {{title}} 
        asColumn: {{title_prefix}} 
        startIndex: {{1}} 
        endIndex: {{5}}
    ```
=== "Example"

    ```yaml title="cut_character.yaml" hl_lines="51-56"
      --8<--  "examples/resources/stacks/flare/functions/cut_character.yaml"
    ```

    Output

    ```shell
    +----------+----------+
    | BIRTHDATE|birth_year|
    +----------+----------+
    |2019-02-17|      2019|
    |2005-07-04|      2005|
    +----------+----------+
    ```
</div>

### **`decode`**

| Function | Description |
| --- | --- |
| `decode` | The *decode* function decodes a column value as one of base32, base64, or hex following RFC-4648. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions: 
      - name: decode 
        algo: base64 
        column: col1 
        asColumn: new_col1
    ```
=== "Example"

    ```yaml title="decode.yaml" hl_lines="51-55"
    --8<--  "examples/resources/stacks/flare/functions/decode.yaml"
    ```
    Before

    ```shell
    +-----------+
    |ZIP_ENCODED|
    +-----------+
    |   GIYTENBU|
    |   GIYTENBU|
    +-----------+
    ```
    After

    ```shell
    +-----+
    |  ZIP_DECODED|
    +-------------+
    |    21244    |
    |    21244    |
    +-------------+
    ```
</div>


### **`diff_date`**

| Function | Description |
| --- | --- |
| `diff_date` | The *diff_date* function calculates difference between two date columns. |

<div class="grid" markdown>
=== "Syntax"

    ```yaml
    functions: 
      - name: diff_date 
        columnA: col_a 
        columnB: col_b 
        asColumn: col_diff_date
    ```
===  "Example"

    ```yaml title="diff_date.yaml" hl_lines="51-55"
    --8<-- "examples/resources/stacks/flare/functions/diff_date.yaml"
    ```
    Output

    ```shell
    +--------------------+--------------------+-----------+
    |          START_YEAR|            END_YEAR|Days_Stayed|
    +--------------------+--------------------+-----------+
    |2019-02-24T05:07:38Z|2020-03-01T05:07:38Z|        371|
    |2020-03-01T05:07:38Z|2021-03-07T05:07:38Z|        371|
    +--------------------+--------------------+-----------+
    ```
</div>

### **`drop`**

| Function | Description |
| --- | --- |
| `drop` | The *drop* function is used to drop a list of columns. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: drop
        columns:
          - column_1 
          - column_2
    ```
=== "Example"

    ```yaml title="drop.yaml" hl_lines="51-55"
    --8<-- "examples/resources/stacks/flare/functions/drop.yaml"
    ```
    Before

    ```shell
    |-- Id: string (nullable = true)
    |-- NAME: string (nullable = true)
    |-- ADDRESS: string (nullable = true)
    |-- CITY: string (nullable = true)
    |-- STATE_HEADQUARTERED: string (nullable = true)
    |-- ZIP: string (nullable = true)
    |-- PHONE: string (nullable = true)
    ```
    After

    ```shell
    |-- Id: string (nullable = true)
    |-- NAME: string (nullable = true)
    |-- ADDRESS: string (nullable = true)
    |-- CITY: string (nullable = true)
    |-- PHONE: string (nullable = true)
    ```
</div>

### **`drop_duplicates`**

| Function | Description |
| --- | --- |
| `drop_duplicates` | The *drop_duplicates* function removes all the duplicate elements from a list of columns. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: drop_duplicates
        columns:
          - column_1 
          - column_2
    ```
=== "Exmaple"

    ```yaml title="drop_duplicates.yaml" hl_lines="51-55"
    --8<-- "examples/resources/stacks/flare/functions/drop_duplicates.yaml"
    ```
    Before

    ```shell
    +------------+
    |        CITY|
    +------------+
    |   Baltimore|
    |   Baltimore|
    |   Baltimore|
    |  Louisville|
    |     Chicago|
    |  Minnetonka|
    |    Hartford|
    |  Bloomfield|
    |Indianapolis|
    |        null|
    +------------+
    ```
    After

    ```shell
    +------------+
    |        CITY|
    +------------+
    |  Louisville|
    |Indianapolis|
    |        null|
    |     Chicago|
    |  Minnetonka|
    |  Bloomfield|
    |    Hartford|
    |   Baltimore|
    +------------+
    ```
</div>  

### **`encode`**

| Function | Description |
| --- | --- |
| `encode` | The *encode* function encodes a column value as one of base32 , base64, or hex following RFC-4648. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: encode
        algo: {{base64}} 
        column: {{col1}} 
        asColumn: {{new_col1}}
    ```

=== "Example"

    ```yaml title="encode.yaml" hl_lines="51-55"
    --8<-- "examples/resources/stacks/flare/functions/encode.yaml"
    ``` 
    Before

    ```shell
    +-----+
    |  ZIP_DECODED|
    +-------------+
    |    21244    |
    |    21244    |
    +-------------+
    ```
    After

    ```shell
    +-----------+
    |ZIP_ENCODED|
    +-----------+
    |   GIYTENBU|
    |   GIYTENBU|
    +-----------+
    ```
</div>

### **`epoch_to_timestamp`**

| Function | Description |
| --- | --- |
| `epoch_to_timestamp` | The *epoch_to_timestamp* function converts epoch string to timestamp format. |

<div class="grid" markdown>

=== "Syntax"

      ```yaml
      functions:
        - name: epoch_to_timestamp
          column: epoch_column
          asColumn: date_column
      ```
=== "Example"

    ```yaml
    --8<-- "examples/resources/stacks/flare/functions/epoch_to_timestamp.yaml"
    ```
    Output

    ```shell
    +----------+-------------------+
    |    epochs|          timestamp|
    +----------+-------------------+
    |1709541360|2024-03-04 08:36:00|
    |1709541360|2024-03-04 08:36:00|
    +----------+-------------------+
    ```
</div>

### **`fill_null_or_empty`**

| Function | Description |
| --- | --- |
| `fill_null_or_empty` | The *fill_null_or_empty* function fills column value with a fixed value if it is either null or empty (""). If the column does not exist, then the function will fail.The defaultValue can only be of type string. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: fill_null_or_empty
        columns:
          column1: {{value1}}
          column2: {{value2}}
    ```
=== "Example"

    ```yaml title="fill_null_or_empty.yaml" hl_lines="51-55"
    --8<-- "examples/resources/stacks/flare/functions/fill_null_or_empty.yaml"
    ```

    Before

    ```shell
    +---------+
    |   PREFIX|
    +---------+
    |   null  |
    |   Mr.   |
    +---------+
    ```

    After

    ```shell
    +---------+
    |   PREFIX|
    +---------+
    |not known|
    |    Mr.  |
    +---------+
    ```
</div>

### **`find_and_replace`**

| Function | Description |
| --- | --- |
| `find_and_replace` | The *find_and_replace* function transforms string column values using a "sed"-like expression to find and replace text within the same column. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: find_and_replace
        column: title
        sedExpression: "s/regex/replacement/g"
    ```
===  "Example" 

    ```yaml title="find_and_replace.yaml" hl_lines="51-54"
    --8<-- "examples/resources/stacks/flare/functions/find_and_replace.yaml"
    ```
    Before

    ```shell
    +--------------------+
    |           OWNERNAME|
    +--------------------+
    | Damon455 Langosh790|
    ||Adalberto916 Wuns..|
    |Adalberto916 Wuns...|
    |Adalberto916 Wuns...|
    | Larissa293 Jerde200|
    +--------------------+
    ```
    After

    ```shell
    +-------------------+
    |          OWNERNAME|
    +-------------------+
    |Damon455 Langosh790|
    |Albert916 Wunsch504|
    |Albert916 Wunsch504|
    |Larissa293 Jerde200|
    +-------------------+
    ```
</div>

### **`flatten`**

| Function | Description |
| --- | --- |
| `flatten` | The *flatten* function separates the elements in a repeated field into individual records. This function is useful for the flexible exploration of repeated data. To maintain the association between each flattened value and the other fields in the record, the FLATTEN directive copies all of the other columns into each new record. <br> <b>Note</b> :- Use flatten_outer when array has null values and you want records of root with null in flattened columns.  |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: flatten
        column: array_holding_column
        asColumn: new_column_name
    ```
=== "Example"

    ```yaml title="flatten.yaml" hl_lines="51-54"
    --8<-- "examples/resources/stacks/flare/functions/flatten.yaml"
    ```
    Output

    ```shell
    root
    |-- discount: array (nullable = true)
    |    |-- element: struct (containsNull = true)
    |    |    |-- discount_amount: long (nullable = true)
    |    |    |-- discount_percent: long (nullable = true)
    |    |    |-- discount_sequence_number: long (nullable = true)
    |    |    |-- discount_type: string (nullable = true)
    |-- discounts: struct (nullable = true)
    |    |-- discount_amount: long (nullable = true)
    |    |-- discount_percent: long (nullable = true)
    |    |-- discount_sequence_number: long (nullable = true)
    |    |-- discount_type: string (nullable = true)
    ```
</div>

### **`format_date`**

| Function | Description |
| --- | --- |
| `format_date` | The *format_date* function allows custom patterns for date-time formatting. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: format_date
        column: date_column
        format: "yyyy-MM-dd'T'HH:mm:ss"
    ```
=== "Example"

    ```yaml title="format_date.yaml" hl_lines="51-54"
    --8<-- "examples/resources/stacks/flare/functions/format_date.yaml"
    ```

    Before

    ```shell
    +--------------------+
    |          START_YEAR|
    +--------------------+
    |2019-02-24T05:07:38Z|
    |2020-03-01T05:07:38Z|
    +--------------------+
    ```
    After

    ```shell
    +--------------------+
    |          START_YEAR|
    +--------------------+
    |2019/02/24T 05: 0...|
    |2020/03/01T 05: 0...|
    +--------------------+
    ```
</div>

### **`format_unix_date`**

| Function | Description |
| --- | --- |
| `format_unix_date` | The *format_unix_date* function allows custom patterns for date-time formatting. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: format_unix_date
        column: {{unix_epoch_column}}
        format: {{"yyyy-MM-dd'T'HH:mm:ss"}}
    ```
=== "Example"

    ```yaml title="format_unix_date.yaml" hl_lines="51-54"
    --8<--  "examples/resources/stacks/flare/functions/format_unix_date.yaml"
    ```
    Before:

    ```shell
    +------------+
    |epoch_column|
    +------------+
    |   178976646|
    |   178976646|
    +------------+
    ```
    After:

    ```shell
    +-------------------+
    |       epoch_column|
    +-------------------+
    |1975-09-03T11:44:06|
    |1975-09-03T11:44:06|
    +-------------------+
    ```
</div>

### **`generate_uuid`**

| Function | Description |
| --- | --- |
| `generate_uuid` | The *generate_uuid* function generates a universally unique identifier (UUID) of the record. |

<div class=grid markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: generate_uuid
        asColumn: {{column_01}}
    ```
=== "Example"  

    ```yaml title="generate_uuid.yaml" hl_lines="51-53"
    --8<--  "examples/resources/stacks/flare/functions/generate_uuid.yaml"
    ```
    Output

    ```shell
    ----------------+
    |         UUID_COLUMN|
    +--------------------+
    |0b74fc7f-5043-477...|
    |bbe0c644-6361-441...|
    +--------------------+
    ```
</div>

### **`hash`**

| Function | Description |
| --- | --- |
| `hash` | The *hash* function generates a message digest. The column is replaced with the digest created using the supplied algorithm. The type of column is a string. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: hash
        column: column_to_hash
        algo: MD5 | SHA-1 | SHA-256 | SHA-384 | SHA-512
    ```
=== "Example"

    ```yaml title="hash.yaml" hl_lines="51-54"
    --8<--  "examples/resources/stacks/flare/functions/hash.yaml"
    ```
    Before:

    ```shell
    +--------------+
    |    PHONE     |
    +--------------+
    |1-877-267-2323|
    |1-800-633-4227|
    +--------------+
    ```
    After:

    ```shell
    +--------------------+
    |       PHONE        |
    +--------------------+
    |75cb2eeea30b8b577...|
    |d71c4d3eae0755df6...|
    +--------------------+
    ```
</div>

### **`increment_variable`**

| Function | Description |
| --- | --- |
| `increment_variable` | The *increment_variable* function increments the value of the variable that is local to the input record being processed. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: increment_variable
        column: column_01
    ```
</div>

### **`mask_number`**

| Function | Description |
| --- | --- |
| `mask_number` | The *mask_number* function applies substitution masking on the column values.<br>The 'column' specifies the name of an existing column to be masked.<br>The 'pattern' is a substitution pattern to be used to mask the column values.<br>Substitution masking is generally used for masking credit card or social security numbers. The MASK_NUMBER applies substitution masking on the column values. This type of masking is fixed masking, where the pattern is applied on the fixed length string.<br>These rules are used for the pattern:<br>• Use of # will include the digit from the position.<br>• Use x or any other character to mask the digit at that position.<br>• E.g. For SSN '000-00-0000' and pattern: 'XXX-XX-####' output would be like: XXX-XX-0000 |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: mask_number
        column: {{column01}}
        pattern: {{XXX-XX-####}}
    ```
=== "Example"

    ```yaml title="mask_number.yaml" hl_lines="51-54"
    --8<--  "examples/resources/stacks/flare/functions/mask_number.yaml"
    ```
    Before:

    ```shell
    +-----------+
    |    SSN    |
    +-----------+
    |999-65-3251|
    |999-49-3323|
    +-----------+
    ```
    After:

    ```shell
    +-----------+
    |    SSN    |
    +-----------+
    |XXX-XX-3251|
    |XXX-XX-3323|
    +-----------+
    ```
</div>

### **`merge`**

| Function | Description |
| --- | --- |
| `merge` | The *merge* function merges two or more columns by inserting a third column specified as asColumn into a row. The values in the third column are merged values from the specified columns delimited by a specified separator. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: merge
        separator: "__"
        columns:
          - first_name
          - last_name
        asColumn: full_name
    ```
=== "Example"

    ```yaml title="merge.yaml" hl_lines="51-57"
    --8<--  "examples/resources/stacks/flare/functions/merge.yaml"
    ```

    ```shell
    +--------+----------+-------------------+
    |   FIRST|      LAST|          full_name|
    +--------+----------+-------------------+
    |Damon   |Langosh   |  Damon  Langosh   |
    |  Thi   | Wunsch   |    Thi  Wunsch    |
    +--------+----------+-------------------+
    ```
</div>

### **`parse_as_json`**

| Function | Description |
| --- | --- |
| `parse_as_json` | The *parse_as_json* function is for parsing a JSON object. The function can operate on String or JSON Object types. It requires spark schema json to parse the json back into dataframe. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: parse_as_json
        column: json_string_column_name
        asColumn: column_name
        sparkSchema: "<spark_schema_json>"
        avroSchema: "<avro_schema>"
    ```
</div>

### **`parse_html`**

| Function | Description |
| --- | --- |
| `parse_html` | The *parse_html* function is used to convert the HTML-coded string to a normal string without any html tags. Here, asColumn is an optional parameter incase you wish to create a separate column for the processed data. Else, the processed data will replace the original column on which the function is performed. The function works using the jsoup library. More details about this library can be found here: https://github.com/jhy/jsoup |

<div class="merge" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: parse_html
        column: questionText
        asColumn: parsedText
    ```
</div>

### **`pivot`**

| Function | Description |
| --- | --- |
| `pivot` | The *pivot* function is used to pivot/rotate the data from one DataFrame/Dataset column into multiple columns (transform row to columns). <br>Here, values and approach are optional parameters. Also, aggregate_expression requires an alias to be written the same as the column name used with aggregate functions like sum, count, avg, etc. <br>Values can be used to specify only those columns needed after pivot from column . <br>Approach can be set to “two-phase” for running an optimized version query on large datasets. |

<div class="merge" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: pivot
        groupBy:
          - {{"Product"}}
          - "{{Country"}}
        column: {{"Country"}}
        values:
          - {{"USA"}}
          - {{"Mexico"}}
          - {{"India"}}
        aggregateExpression: {{"sum(Amount) as Amount"}}
        approach: {{"two-phase"}}
    ```
=== "Example"

    ```yaml title="pivot.yaml" hl_lines="51-62"
    --8<--  "examples/resources/stacks/flare/functions/pivot.yaml"
    ```
    Output

    ```shell
    | ADDRESS           | STATE_HEADQUARTERED | null | Baltimore  | Bloomfield | Chicago | Hartford  | Indianapolis | Louisville | Minnetonka  |
    |-------------------|---------------------|------|------------|------------|---------|-----------|--------------|------------|------------|
    | Security Blvd     | MD                  | null | 2.309825E7 | null       | null    | null      | null         | null       | null       |
    | Virginia Ave      | IN                  | null | null       | null       | null    | null      | 1.598388E8   | null       | null       |
    | Farmington Ave    | CT                  | null | null       | null       | null    | 1.51906E8 | null         | null       | null       |
    | Healthcare Lane   | MN                  | null | null       | null       | null    | null      | null         | null       | 1.441036E8 |

    ```

    Example 2: with values added, values is optional here 

    ```shell
    +--------------------+-------------------+------+-----+
    |             ADDRESS|STATE_HEADQUARTERED|Mexico|India|
    +--------------------+-------------------+------+-----+
    |       Security Blvd|                 MD|  null| null|
    |                null|               null|  null| null|
    |        Virginia Ave|                 IN|  null| null|
    |      Farmington Ave|                 CT|  null| null|
    |     Healthcare Lane|                 MN|  null| null|
    +--------------------+-------------------+------+-----+
    ```
</div>

### **`rename`**

| Function | Description |
| --- | --- |
| `rename` | The *rename* function will change the name of a supplied column to a new column name. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: rename
        column: column_name
        asColumn: new_column_name
    ```
</div>

### **`rename_all`**

| Function | Description |
| --- | --- |
| `rename_all` | The *rename_all* function will change the names of a supplied in columns to values. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: rename_all
        columns:
          column1: new_column1
          column2: new_column2
    ```
=== "Example"

    ```yaml title="rename_all.yaml" hl_lines="51-55"
    --8<--  "examples/resources/stacks/flare/functions/rename_all.yaml"
    ```
    Before

    ```shell
    +--------------------+----------+
    |                  Id|      CITY|
    +--------------------+----------+
    |d47b3510-2895-3b7...|Louisville|
    |6e2f1a2d-27bd-370...|   Chicago|
    +--------------------+----------+
    ```
    After

    ```shell
    +--------------------+-----------+
    |           payers_id|payers_city|
    +--------------------+-----------+
    |d47b3510-2895-3b7...| Louisville|
    |6e2f1a2d-27bd-370...|    Chicago|
    +--------------------+-----------+
    ```
 </div>   

### **`select`**

| Function | Description |
| --- | --- |
| `select` | The *select* function is used to keep specified columns from the record. This is the opposite behaviour of the DROP function. |

<div class="grid" markdown>

=== "Syntax"

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
=== "Example"

      ```yaml title="select.yaml" hl_lines="51-55"
      --8<--  "examples/resources/stacks/flare/functions/select.yaml"
      ```
      Output

      ```shell
      +--------------+--------------------+
      |customer_index|            discount|
      +--------------+--------------------+
      |          1971|[{null, null, 1, ...|
      |          1516|[{45, 15, 1, 15% ...|
      +--------------+--------------------+
      ```
  </div>

  ### **`set_column`**

  | Function | Description |
  | --- | --- |
  | `set_column` | The *set_column* function will change name of a supplied in column to value in asColumn. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: set_column
        column: my_col_name
        value: "some value here"
    ```
=== "Example" 

    ```yaml title="set_column.yaml" hl_lines="51-54"
    --8<--  "examples/resources/stacks/flare/functions/set_column.yaml"
    ```
</div>

### **`set_type`**

| Function | Description |
| --- | --- |
| `set_type` | The `set_type` function converts the data type of a column. Here type can be one of the Spark data types e.g. int, string, long, double, etc. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: set_type
        columns:
          column1: type
          column2: type
    ```
=== "Example"

    ```yaml title="set_type.yaml" hl_lines="51-55"
    --8<--  "examples/resources/stacks/flare/functions/set_type.yaml"
    ```
    Before

    ```shell
    |-- HEALTHCARE_EXPENSES: string (nullable = true)
    |-- HEALTHCARE_COVERAGE: string (nullable = true)
    ```
    After

    ```shell
    |-- HEALTHCARE_EXPENSES: float (nullable = true)
    |-- HEALTHCARE_COVERAGE: float (nullable = true)
    ```
</div>

### **`set_variable`**

| Function | Description |
| --- | --- |
| `set_variable` | The *set_variable* function evaluates the expression supplied and sets the value in the variable. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: set_variable
        column: some_new_column
        expression: "ROUND(AVG(src_bytes), 2)"
    ```
=== "Example"

    ```yaml title="set_variable.yaml" hl_lines="51-54"
    --8<--  "examples/resources/stacks/flare/functions/set_variable.yaml"
    ```
    Output

    ```shell
    +-------------------+---------------------------+
    |HEALTHCARE_EXPENSES|HEALTHCARE_EXPENSES_ROUNDED|
    +-------------------+---------------------------+
    |           9039.164|                     9039.0|
    |           402723.4|                   402723.0|
    +-------------------+---------------------------+
    ```
</div>

### **`snake_case`**

| Function | Description |
| --- | --- |
| `snake_case` | The *snake_case* function converts column names from camel case to snake case and is only applicable for batch dataframe/ job. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: snake_case
    ```
=== "Example"

    ```yaml title="snake_case.yaml" hl_lines="51-52"
    --8<--  "examples/resources/stacks/flare/functions/snake_case.yaml"
    ```
    
    Before

    ```shell
    |-- COVERED_ENCOUNTERS: string (nullable = true)
    |-- UNCOVERED_ENCOUNTERS: string (nullable = true)
    |-- COVERED_MEDICATIONS: string (nullable = true)
    |-- UNCOVERED_MEDICATIONS: string (nullable = true)
    |-- COVERED_PROCEDURES: string (nullable = true)
    ```
    After

    ```shell
    |-- covered_encounters: string (nullable = true)
    |-- uncovered_encounters: string (nullable = true)
    |-- covered_medications: string (nullable = true)
    |-- uncovered_medications: string (nullable = true)
    |-- covered_procedures: string (nullable = true)
    ```
</div>

### **`split_email`**

| Function | Description |
| --- | --- |
| `split_email` | The *split_email* function splits/parses an email ID into its two constituent parts: account and domain. After splitting the email address stored in the column within the column property, the directive will create two new columns, appending to the original column, named: column_account, and column_domain. If the email address cannot be parsed correctly, the additional columns will still be generated, but they would be set to null depending on the parts that could not be parsed. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: split_email
        column: email_column
    ```

=== "Example"

    ```yaml title="split_email.yaml" hl_lines="51-53"
    --8<--  "examples/resources/stacks/flare/functions/split_email.yaml"
    ```

    ```shell
    +------------------+-------------+------------+
    |             Email|Email_account|Email_domain|
    +------------------+-------------+------------+
    |iamgroot@gmail.com|     iamgroot|   gmail.com|
    |iamgroot@gmail.com|     iamgroot|   gmail.com|
    +------------------+-------------+------------+
    ```
</div>

### **`split_url`**

| Function | Description |
| --- | --- |
| `split_url` | The *split_url* function splits a URL into protocol, authority, host, port, path, filename, and query. The function will parse the URL into its constituents. Upon splitting the URL, the directive creates seven new columns by appending to the original<br>column name: column_protocol<br>column_authority<br>column_host<br>column_port<br>column_path<br>column_filename<br>column_query<br>If the URL cannot be parsed correctly, an exception is thrown. If the URL column does not exist, columns with a null value are added to the record. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: split_url
        column: column_with_url_content
    ```
=== "Example"

    ```yaml title="split_url.yaml" hl_lines="51-53"
    --8<--  "examples/resources/stacks/flare/functions/split_url.yaml"
    ```

    ```shell
    +-----------------+------------+-------------+--------+
    |              URL|URL_protocol|URL_authority|URL_port|
    +-----------------+------------+-------------+--------+
    |www.spiderman.com|        null|         null|    null|
    |www.spiderman.com|        null|         null|    null|
    +-----------------+------------+-------------+--------+
    ```
</div>

### **`swap`**

| Function | Description |
| --- | --- |
| `swap` | The *swap* function swaps the column names of two columns. |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: swap
        columnA: col_1
        columnB: col_2
    ```
=== "Example"

    ```yaml title="swap.yaml" hl_lines="51-54"
    --8<--  "examples/resources/stacks/flare/functions/swap.yaml"
    ```
    Before

    ```shell
    +--------------------+-----+
    |                  Id|  ZIP|
    +--------------------+-----+
    |b3221cfc-24fb-339...|21244|
    |7caa7254-5050-3b5...|21244|
    |7c4411ce-02f1-39b...|21244|
    |d47b3510-2895-3b7...|40018|
    +--------------------+-----+
    ```
    After

    ```shell
    +-----+--------------------+
    |   Id|                 ZIP|
    +-----+--------------------+
    |21244|b3221cfc-24fb-339...|
    |21244|7caa7254-5050-3b5...|
    |21244|7c4411ce-02f1-39b...|
    |40018|d47b3510-2895-3b7...|
    +-----+--------------------+
    ```
</div>

### **`trim`**

| Function | Description |
| --- | --- |
| `trim` | The *trim* function trim whitespace from both sides, left side or right side of string values they are applied to. One can supply method as trim/ltrim/rtrim |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: trim
        column: col_001
        method: trim
    ```

=== "Example"


</div>

### **`unfurl`**

| Function | Description |
| --- | --- |
| `unfurl` | The *unfurl* function uses the expression supplied to pull columns from within the nested JSON attribute out e.g. columnName.* |

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: unfurl
        expression: explode(col01)  #it deconstructs array
      - name: unfurl
        expression: col02.* #it deconstructs struct
    ```

=== "Example"

    ```yaml title="unfurl.yaml" hl_lines="51-54"
    --8<--  "examples/resources/stacks/flare/functions/unfurl.yaml"
    ```

    Before

    ```shell
    |-- discount: array (nullable = true)
    |    |-- element: struct (containsNull = true)
    |    |    |-- discount_amount: long (nullable = true)
    |    |    |-- discount_percent: long (nullable = true)
    |    |    |-- discount_sequence_number: long (nullable = true)
    |    |    |-- discount_type: string (nullable = true)
    ```
    After

    ```shell
    |-- discount01: struct (nullable = true)
    |    |-- discount_amount: long (nullable = true)
    |    |-- discount_percent: long (nullable = true)
    |    |-- discount_sequence_number: long (nullable = true)
    |    |-- discount_type: string (nullable = true)

    ```
</div>

### **`unpivot`**

| Function | Description |
| --- | --- |
| `unpivot` | The *unpivot* function works as the reverse function for the pivot function in which you can achieve rotating column values into rows values.  |

<aside class="callout">
🗣️ Both `pivotColumns` and `columns` can not have `-`,`*` need to specify a list of columns in at least one.
</aside>

<div class="grid" markdown>

=== "Syntax"

    ```yaml
    functions:
      - name: unpivot
        columns: # Columns can have - "*" if need to select all remaining columns than pivot columns
          - {{USA}} or "*"
        pivotColumns: # pivotColumns can have - "*" if need to select all remaining columns than columns
          - {{Col1}}
          - {{Col2}}
          - {{Col3}}
        keyColumnName: {{Country}}
        valueColumnName: {{Amount}}
    ```
=== "Example"

    ```yaml title="unpivot.yaml" hl_lines="51-59"
    --8<--  "examples/resources/stacks/flare/functions/unpivot.yaml"
    ```
    pivoted_column

    ```shell
    +--------------------+-------------------+------+-----+
    |             ADDRESS|STATE_HEADQUARTERED|Mexico|India|
    +--------------------+-------------------+------+-----+
    |  7500 Security Blvd|                 MD|  null| null|
    |                null|               null|  null| null|
    |    220 Virginia Ave|                 IN|  null| null|
    |  151 Farmington Ave|                 CT|  null| null|
    |9800 Healthcare Lane|                 MN|  null| null|
    +--------------------+-------------------+------+-----+
    ```
    unpivoted_column

    ```shell
    +------------------+-------------------+------+-------+
    |           ADDRESS|STATE_HEADQUARTERED|  CITY|Revenue|
    +------------------+-------------------+------+-------+
    |7500 Security Blvd|                 MD| India|   null|
    |7500 Security Blvd|                 MD|Mexico|   null|
    |              null|               null| India|   null|
    |              null|               null|Mexico|   null|
    |  220 Virginia Ave|                 IN| India|   null|
    +------------------+-------------------+------+-------+
    ```
</div>

!!! note
    Make sure provided list has the same datatype else it will throw an error. Do not forget to clean the column before passing `*` in columns if column names have hyphens and spaces.

