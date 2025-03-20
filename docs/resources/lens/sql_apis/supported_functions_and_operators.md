
## SQL API references

### **SQL commands**

#### **`SELECT`**


`SELECT` retrieves rows from a table. The `FROM` clause specifies one or more source tables for the `SELECT`. Qualification conditions can be added (via `WHERE`) to restrict the returned rows to a small subset of the original dataset.


```shell
SELECT select_expr [, ...]
  FROM from_item
    CROSS JOIN join_item
    ON join_criteria]*
  [ WHERE where_condition ]
  [ GROUP BY grouping_expression ]
  [ HAVING having_expression ]
  [ LIMIT number ] [ OFFSET number ];
```

#### **`EXPLAIN`** 

The `EXPLAIN` command displays the query execution plan that the Lens  planner will generate for the supplied statement.

**Example:**

```shell
lens:public:productaffinity=> EXPLAIN select total_customers, country from customer;
   plan_type   |                                           plan                                            
---------------+-------------------------------------------------------------------------------------------
 logical_plan  | Scan: request={                                                                          +
               |   "measures": [                                                                          +
               |     "customer.total_customers"                                                           +
               |   ],                                                                                     +
               |   "dimensions": [                                                                        +
               |     "customer.country"                                                                   +
               |   ],                                                                                     +
               |   "segments": []                                                                         +
               | }
 physical_plan | ScanExecutionPlan, Request:                                                              +
               | {"measures":["customer.total_customers"],"dimensions":["customer.country"],"segments":[]}+
               | 
(2 rows)
```

With `ANALYZE`:

```sql
lens:public:productaffinity=> EXPLAIN ANALYZE select total_customers, country from customer;
     plan_type     |                                                 plan                                                  
-------------------+-------------------------------------------------------------------------------------------------------
 Plan with Metrics | ScanExecutionPlan, Request:                                                                          +
                   | {"measures":["customer.total_customers"],"dimensions":["customer.country"],"segments":[]}, metrics=[]+
                   | 
(1 row)
```

#### **`SHOW`**

Returns the value of a runtime parameter using name, or all runtime parameters if ALL is specified.

```shell
SHOW timezone;

lens:public:productaffinity=> show timezone;
 setting 
---------
 GMT
(1 row)
```

Returns the value of a runtime parameter using name, or all runtime parameters if `ALL` is specified.


```shell
lens:public:productaffinity=> show all;
            name             |    setting     | description 
-----------------------------+----------------+-------------
 timezone                    | GMT            | 
 lc_collate                  | en_US.utf8     | 
 max_identifier_length       | 63             | 
 client_min_messages         | NOTICE         | 
 max_allowed_packet          | 67108864       | 
 standard_conforming_strings | on             | 
 application_name            | NULL           | 
 role                        | none           | 
 transaction_isolation       | read committed | 
 max_index_keys              | 32             | 
 extra_float_digits          | 1              | 
(11 rows)
```

### **SQL functions and operators**

#### **Comaprison operators**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-comparison.html#FUNCTIONS-COMPARISON-OP-TABLE" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>


| Function  | Description                                          | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-----------|------------------------------------------------------|-------|-----------------------------|------------------------------|
| `<`       | Returns TRUE if the first value is less than the second | ✅    |             ✅               |              ✅               |
| `>`       | Returns TRUE if the first value is greater than the second | ✅    |             ✅               |              ✅               |
| `<=`      | Returns TRUE if the first value is less than or equal to the second | ✅    |             ✅               |              ✅               |
| `>=`      | Returns TRUE if the first value is greater than or equal to the second | ✅    |             ✅               |              ✅               |
| `=`       | Returns TRUE if the first value is equal to the second | ✅    |             ✅               |              ✅               |
| `<>` or `!=` | Returns TRUE if the first value is not equal to the second | ✅    |             ✅               |              ✅               |


#### **Comparison predicates**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-comparison.html#FUNCTIONS-COMPARISON-PRED-TABLE" target="_blank">relevant section</a> of the PostgreSQL documentation.
</aside>

| Function        | Description                                    | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-----------------|------------------------------------------------|-------|-----------------------------|------------------------------|
| `BETWEEN`       | Returns TRUE if the first value is between the second and the third | ❌ | ✅ | ❌ |
| `IS NULL`       | Test whether value is NULL                     | ✅ | ✅ | ✅ |
| `IS NOT NULL`   | Test whether value is not NULL                 | ✅ | ✅ | ✅ |


#### **Mathematical functions**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-math.html#FUNCTIONS-MATH-FUNC-TABLE" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>


| Function        | Description                                    | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-----------------|------------------------------------------------|-------|-----------------------------|------------------------------|
| `ABS`           | Absolute value                                 | ✅ | ❌ | ✅ |
| `CEIL`          | Nearest integer greater than or equal to argument | ✅ | ❌ | ✅ |
| `DEGREES`       | Converts radians to degrees                    | ✅ | ❌ | ✅ |
| `EXP`           | Exponential (e raised to the given power)      | ✅ | ❌ | ✅ |
| `FLOOR`         | Nearest integer less than or equal to argument | ✅ | ❌ | ✅ |
| `LN`            | Natural logarithm                              | ✅ | ❌ | ✅ |
| `LOG`           | Base 10 logarithm                              | ✅ | ❌ | ✅ |
| `LOG10`         | Base 10 logarithm (same as LOG)                | ✅ | ❌ | ✅ |
| `PI`            | Approximate value of π                         | ✅ | ❌ | ✅ |
| `POWER`         | a raised to the power of b                     | ✅ | ❌ | ✅ |
| `RADIANS`       | Converts degrees to radians                    | ✅ | ❌ | ✅ |
| `ROUND`         | Rounds v to s decimal places                   | ✅ | ❌ | ✅ |
| `SIGN`          | Sign of the argument (-1, 0, or +1)            | ✅ | ❌ | ✅ |
| `SQRT`          | Square root                                    | ✅ | ❌ | ✅ |
| `TRUNC`         | Truncates to integer (towards zero)            | ✅ | ✅ | ❌ |


#### **Trigonometric functions**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-math.html#FUNCTIONS-MATH-TRIG-TABLE" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>

| Function        | Description                                    | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-----------------|------------------------------------------------|-------|-----------------------------|------------------------------|
| `ACOS`          | Inverse cosine, result in radians              | ✅ | ❌ | ✅ |
| `ASIN`          | Inverse sine, result in radians                | ✅ | ❌ | ✅ |
| `ATAN`          | Inverse tangent, result in radians             | ✅ | ❌ | ✅ |
| `ATAN2`         | Inverse tangent of y/x, result in radians      | ✅ | ❌ | ✅ |
| `COS`           | Cosine, argument in radians                    | ✅ | ❌ | ✅ |
| `COT`           | Cotangent, argument in radians                 | ✅ | ❌ | ✅ |
| `SIN`           | Sine, argument in radians                      | ✅ | ❌ | ✅ |
| `TAN`           | Tangent, argument in radians                   | ✅ | ❌ | ✅ |


#### **String functions and operators**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-string.html#FUNCTIONS-STRING-SQL" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>

| Function            | Description                                                                  | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|---------------------|------------------------------------------------------------------------------|-------|-----------------------------|------------------------------|
| `||`                | Concatenates two strings                                                      | ✅ | ✅ | ❌ |
| `BTRIM`             | Removes the longest string containing only characters in characters from the start and end of string | ✅ | ❌ | ✅ |
| `BIT_LENGTH`        | Returns number of bits in the string (8 times the OCTET_LENGTH)               | ✅ | ❌ | ❌ |
| `CHAR_LENGTH` or `CHARACTER_LENGTH` | Returns number of characters in the string                          | ✅ | ❌ | ❌ |
| `LOWER`             | Converts the string to all lower case                                         | ✅ | ✅ | ❌ |
| `LTRIM`             | Removes the longest string containing only characters in characters from the start of string | ✅ | ❌ | ✅ |
| `OCTET_LENGTH`      | Returns number of bytes in the string                                         | ✅ | ❌ | ❌ |
| `POSITION`          | Returns first starting index of the specified substring within string, or zero if it's not present | ✅ | ❌ | ✅ |
| `RTRIM`             | Removes the longest string containing only characters in characters from the end of string | ✅ | ❌ | ✅ |
| `SUBSTRING`         | Extracts the substring of string                                              | ✅ | ❌ | ✅ |
| `TRIM`              | Removes the longest string containing only characters in characters from the start, end, or both ends of string | ✅ | ❌ | ❌ |
| `UPPER`             | Converts the string to all upper case                                         | ✅ | ❌ | ❌ |


#### **Other string functions**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-comparison.html#FUNCTIONS-COMPARISON-OP-TABLE" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>

| Function        | Description                                                                  | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-----------------|------------------------------------------------------------------------------|-------|-----------------------------|------------------------------|
| `ASCII`         | Returns the numeric code of the first character of the argument               | ✅ | ❌ | ✅ |
| `CONCAT`        | Concatenates the text representations of all the arguments                    | ✅ | ❌ | ✅ |
| `LEFT`          | Returns first n characters in the string, or when n is negative, returns all but last ABS(n) characters | ✅ | ✅ | ✅ |
| `REPEAT`        | Repeats string the specified number of times                                  | ✅ | ❌ | ✅ |
| `REPLACE`       | Replaces all occurrences in string of substring from with substring to       | ✅ | ❌ | ✅ |
| `RIGHT`         | Returns last n characters in the string, or when n is negative, returns all but first ABS(n) characters | ✅ | ✅ | ✅ |
| `STARTS_WITH`   | Returns TRUE if string starts with prefix                                     | ✅ | ✅ | ❌ |


#### **Pattern matching**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-string.html#FUNCTIONS-STRING-OTHER" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>

| Function        | Description                                                   | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-----------------|---------------------------------------------------------------|-------|-----------------------------|------------------------------|
| `LIKE`          | Returns TRUE if the string matches the supplied pattern       | ✅ | ✅ | ✅ |
| `REGEXP_SUBSTR` | Returns the substring that matches a POSIX regular expression pattern | ✅ | ❌ | ✅ |


#### **Data type formatting functions**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-formatting.html" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>

| Function    | Description                                                   | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-------------|---------------------------------------------------------------|-------|-----------------------------|------------------------------|
| `TO_CHAR`   | Converts a timestamp to string according to the given format  | ✅ | ❌ | ✅ |


#### **Date/time functions**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-TABLE" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>

| Function        | Description                                                                  | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-----------------|------------------------------------------------------------------------------|-------|-----------------------------|------------------------------|
| `DATE_ADD`      | Add an interval to a timestamp with time zone                                 | ✅ | ❌ | ✅ |
| `DATE_TRUNC`    | Truncate a timestamp to specified precision                                  | ✅ | ✅ | ✅ |
| `DATEDIFF`      | From Redshift. Returns the difference between the date parts of two date or time expressions | ✅ | ❌ | ✅ |
| `EXTRACT`       | Retrieves subfields such as year or hour from date/time values               | ✅ | ❌ | ✅ |
| `LOCALTIMESTAMP`| Returns the current date and time without time zone                          | ✅ | ❌ | ✅ |
| `NOW`           | Returns the current date and time with time zone                             | ✅ | ❌ | ✅ |


#### **Conditional expressions**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-conditional.html" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>

| Expression      | Description                                                   | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-----------------|---------------------------------------------------------------|-------|-----------------------------|------------------------------|
| `CASE`          | Generic conditional expression                                | ✅ | ❌ | ✅ |
| `COALESCE`      | Returns the first of its arguments that is not NULL            | ✅ | ❌ | ✅ |
| `NULLIF`        | Returns NULL if both arguments are equal, otherwise returns the first argument | ✅ | ❌ | ✅ |
| `GREATEST`      | Select the largest value from a list of expressions            | ✅ | ❌ | ✅ |
| `LEAST`         | Select the smallest value from a list of expressions           | ✅ | ❌ | ✅ |

#### **General-purpose aggregate functions**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-aggregate.html#FUNCTIONS-AGGREGATE-TABLE" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>

| Function           | Description                                                   | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|--------------------|---------------------------------------------------------------|-------|-----------------------------|------------------------------|
| `AVG`              | Computes the average (arithmetic mean) of all the non-NULL input values | ✅ | ✅ | ✅ |
| `COUNT`            | Computes the number of input rows in which the input value is not NULL | ✅ | ✅ | ✅ |
| `COUNT(DISTINCT)`  | Computes the number of input rows containing unique input values | ✅ | ✅ | ✅ |
| `MAX`              | Computes the maximum of the non-NULL input values             | ✅ | ✅ | ✅ |
| `MIN`              | Computes the minimum of the non-NULL input values             | ✅ | ✅ | ✅ |
| `SUM`              | Computes the sum of the non-NULL input values                 | ✅ | ✅ | ✅ |
| `MEASURE`          | Works with measures of any type                               | ❌ | ✅ | ✅ |


In projections in inner parts of post-processing queries:

- AVG, COUNT, MAX, MIN, and SUM can only be used with measures of compatible types.
<!-- - If COUNT(*) is specified, Lens will query the first measure of type count of the relevant table. -->

#### **Aggregate functions for statistics**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-aggregate.html#FUNCTIONS-AGGREGATE-STATISTICS-TABLE" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>

| Function        | Description                                                        | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-----------------|--------------------------------------------------------------------|-------|-----------------------------|------------------------------|
| `COVAR_POP`     | Computes the population covariance                                 | ✅ | ✅ | ✅ |
| `COVAR_SAMP`    | Computes the sample covariance                                     | ✅ | ✅ | ✅ |
| `STDDEV_POP`    | Computes the population standard deviation of the input values      | ✅ | ✅ | ✅ |
| `STDDEV_SAMP`   | Computes the sample standard deviation of the input values          | ✅ | ✅ | ✅ |
| `VAR_POP`       | Computes the population variance of the input values               | ✅ | ✅ | ✅ |
| `VAR_SAMP`      | Computes the sample variance of the input values                   | ✅ | ✅ | ✅ |


#### **Row and array comparisons**

<aside class="callout">
  Learn more in the <a href="https://www.postgresql.org/docs/current/functions-comparisons.html" target="_blank">relevant section</a>  of the PostgreSQL documentation.
</aside>

| Function    | Description                                                      | Outer | Selections (`WHERE` Clause) | Projection (`SELECT` Clause) |
|-------------|------------------------------------------------------------------|-------|-----------------------------|------------------------------|
| `IN`        | Returns TRUE if a left-side value matches any of right-side values | ✅ | ✅ | ✅ |
| `NOT IN`    | Returns TRUE if a left-side value matches none of right-side values | ✅ | ✅ | ✅ |
