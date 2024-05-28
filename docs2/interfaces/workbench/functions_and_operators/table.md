# Table funtions
When a function's returned table type can vary based on its invoked arguments, it's termed as a polymorphic table function. Such functions enable dynamic invocation of custom logic directly within SQL queries. They serve various purposes, including interfacing with external systems and extending Trino's capabilities beyond standard SQL functionalities.
## Built-in table functions

### **`exclude_columns()`**
| Function                            | Description                                                    | Return Type |
| ---------------------------------- | -------------------------------------------------------------- | ----------- |
| `exclude_columns(input, columns)`  | Excludes from the input table all columns listed in the descriptor. | `table`     |

Example:

```sql
SELECT *
FROM TABLE(exclude_columns(
                        input => TABLE(orders),
                        columns => DESCRIPTOR(clerk, comment)))
```

### **`sequence()`**

| Function                                        | Description                                                                                                     | Return Type               |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------- |
| `sequence(start, stop, step)`                   | Returns a single column `sequential_number` containing a sequence of bigint.                                    | `table(sequential_number bigint)` |

> **Note:** The result of the sequence table function might not be ordered.


## Table function invocation

You invoke a table function in the FROM clause of a query. Table function invocation syntax is similar to a scalar function call.

### Function resolution

Every table function is provided by a catalog, and it belongs to a schema in the catalog. You can qualify the function name with a schema name, or with catalog and schema names:
```sql
SELECT * FROM TABLE(schema_name.my_function(1, 100))
SELECT * FROM TABLE(catalog_name.schema_name.my_function(1, 100))
```
### Arguments

| Argument Type      | Example                                   |
|--------------------|-------------------------------------------|
| Scalar Arguments   | `factor => 42`                            |
| Descriptor Arguments | `schema => DESCRIPTOR(id BIGINT, name VARCHAR)` <br> `columns => DESCRIPTOR(date, status, comment)` <br> `schema => CAST(null AS DESCRIPTOR)` (to pass null for a descriptor)|
| Table Arguments    | `input => TABLE(orders)` <br> `data => TABLE(SELECT * FROM region, nation WHERE region.regionkey = nation.regionkey)` <br> `input => TABLE(orders) PARTITION BY orderstatus KEEP WHEN EMPTY ORDER BY orderdate` |

### Argument passing conventions

| Convention                | Description                                                                                                                   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Arguments passed by name  | Allows passing arguments in arbitrary order. <br> You can skip arguments with default values. <br> Argument names are case-sensitive and automatically uppercased if unquoted.|
| Arguments passed positionally | Requires following the order of argument declaration. <br> Allows skipping a suffix of the argument list if they have default values. |


Example:

```sql
PREPARE stmt FROM
SELECT * FROM TABLE(my_function(row_count => ? + 1, column_count => ?));

EXECUTE stmt USING 100, 1;
```