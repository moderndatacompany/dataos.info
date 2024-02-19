# Lambda Expressions
Lambda expressions are anonymous functions which are passed as arguments to higher-order SQL functions.

Lambda expressions are written with -> :
``` sql
x -> x + 1
(x, y) -> x + y
x -> regexp_like(x, 'a+')
x -> x[1] / x[2]
x -> IF(x > 0, x, -x)
x -> COALESCE(x, 0)
x -> CAST(x AS JSON)
x -> x + TRY(1 / 0)
```
## Limitations

| Limitations                    | Examples                       |
|--------------------------------|--------------------------------|
| Subqueries are not supported   | `x -> 2 + (SELECT 3)`          |
| Aggregations are not supported | `x -> max(y)`                  |

## Examples

### **`transform()`**

| Function  | Description                                                                                         | Return Type |
|-----------|-----------------------------------------------------------------------------------------------------|-------------|
| transform() | Applies a transformation function to each element of an array column.                              | Array       |


```sql
SELECT numbers,
       transform(numbers, n -> n * n) as squared_numbers
FROM (
    VALUES
        (ARRAY[1, 2]),
        (ARRAY[3, 4]),
        (ARRAY[5, 6, 7])
) AS t(numbers);

  numbers  | squared_numbers
-----------+-----------------
 [1, 2]    | [1, 4]
 [3, 4]    | [9, 16]
 [5, 6, 7] | [25, 36, 49]
(3 rows)
```


### **`any_match()`**

| Function  | Description                                                                                         | Return Type |
|-----------|-----------------------------------------------------------------------------------------------------|-------------|
| any_match() | Checks if any element in an array column matches a specified condition.                             | Boolean     |


```sql 
SELECT numbers
FROM (
    VALUES
        (ARRAY[1,NULL,3]),
        (ARRAY[10,20,30]),
        (ARRAY[100,200,300])
) AS t(numbers)
WHERE any_match(numbers, n ->  COALESCE(n, 0) > 100);
-- [100, 200, 300]
```

### **`regexp_replace()`**


| Function        | Description                                                                                            | Return Type |
|-----------------|--------------------------------------------------------------------------------------------------------|-------------|
| regexp_replace() | Performs a regular expression search and replace on a string column.                                   | String      |

```sql
SELECT regexp_replace('once upon a time ...', '^(\w)(\w*)(\s+.*)$',x -> upper(x[1]) || x[2] || x[3]);
-- Once upon a time ...
```

### **`reduce_agg()`**

| Function  | Description                                                                                         | Return Type |
|-----------|-----------------------------------------------------------------------------------------------------|-------------|
| reduce_agg() | Aggregates values in a column using a provided binary operation and an optional combination function for distributed processing. | Depends     |

```sql
SELECT reduce_agg(value, 0, (a, b) -> a + b, (a, b) -> a + b) sum_values
FROM (
    VALUES (1), (2), (3), (4), (5)
) AS t(value);
-- 15
```