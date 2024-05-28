# Window functions

| Aspect                         | Description                                                                                                   |
|--------------------------------|---------------------------------------------------------------------------------------------------------------|
| Timing of execution            | Window functions run after the HAVING clause but before the ORDER BY clause.                                  |
| Syntax for invocation          | Invoking a window function requires special syntax using the OVER clause to specify the window.              |
| Two ways to specify the window | <ul><li>By referencing a named window specification defined in the WINDOW clause.</li><li>By using an in-line window specification, which allows defining window components and referring to them.</li></ul> |




Example:
```sql
SELECT orderkey, clerk, totalprice,
       rank() OVER (PARTITION BY clerk
                    ORDER BY totalprice DESC) AS rnk
FROM orders
ORDER BY clerk, rnk
```

## Aggregate functions

| Feature                                                     | Description                                                                                                                                                   |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Usage as window functions                                   | All aggregate functions can be used as window functions by adding the OVER clause.                                                                            |
| Computation scope                                           | The aggregate function is computed for each row over the rows within the current row’s window frame.                                                           |
| Ordering during aggregation                                | Ordering during aggregation is not supported.                                                                                                                |

Example:

```sql
SELECT clerk, orderdate, orderkey, totalprice,
       sum(totalprice) OVER (PARTITION BY clerk
                             ORDER BY orderdate) AS rolling_sum
FROM orders
ORDER BY clerk, orderdate, orderkey
```

## Ranking functions

### **`cume_dist()`**

| Function        | Description                                                       | Return Type |
| --------------- | ----------------------------------------------------------------- | ----------- |
| `cume_dist()`   | Returns the cumulative distribution of a value in a group of values. | `bigint`    |

### **`dense_rank()`**

| Function        | Description                                                                                     | Return Type |
| --------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| `dense_rank()`  | Returns the rank of a value in a group of values, with no gaps in the sequence for tie values. | `bigint`    |

### **`ntile()`**

| Function        | Description                                                                                     | Return Type |
| --------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| `ntile(n)`      | Divides the rows for each window partition into n buckets.                                      | `bigint`    |

### **`percent_rank()`**

| Function        | Description                                                                                     | Return Type |
| --------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| `percent_rank()`| Returns the percentage ranking of a value in a group of values.                                  | `double`    |

### **`rank()`**

| Function        | Description                                                       | Return Type |
| --------------- | ----------------------------------------------------------------- | ----------- |
| `rank()`        | Returns the rank of a value in a group of values, with gaps in the sequence for tie values.     | `bigint`    |

### **`row_number()`**

| Function        | Description                                                       | Return Type |
| --------------- | ----------------------------------------------------------------- | ----------- |
| `row_number()`  | Returns a unique, sequential number for each row within the window partition.                   | `bigint`    |

## Value functions

### **`first_value()`**

| Function          | Description                                                                                                     | Return Type    |
| ----------------- | --------------------------------------------------------------------------------------------------------------- | -------------- |
| `first_value(x)`  | Returns the first value of the window.                                                                          | `[same as input]` |

### **`last_value()`**
| Function        | Description                                                                                                | Return Type    |
| --------------- | ---------------------------------------------------------------------------------------------------------- | -------------- |
| `last_value(x)` | Returns the last value of the window.                                                                       | `[same as input]` |

### **`nth_value()`**
| Function              | Description                                                                                                      | Return Type    |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------- |
| `nth_value(x, offset)`| Returns the value at the specified offset from the beginning of the window.                                      | `[same as input]` |

### **`lead()`**
| Function                        | Description                                                                                             | Return Type    |
| ------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------- |
| `lead(x[, offset[, default_value]])` | Returns the value at offset rows after the current row in the window partition.                           | `[same as input]` |

### **`lag()`**

| Function                         | Description                                                                                                  | Return Type    |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------- |
| `lag(x[, offset[, default_value]])` | Returns the value at offset rows before the current row in the window partition.                               | `[same as input]` |
