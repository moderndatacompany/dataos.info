# Comparsion functions and operators

## comaprsion operators

| Operator | Description                        |
|----------|------------------------------------|
| `<`      | Less than                          |
| `>`      | Greater than                       |
| `<=`     | Less than or equal to              |
| `>=`     | Greater than or equal to           |
| `=`      | Equal                              |
| `<>`     | Not equal                          |
| `!=`     | Not equal (non-standard but popular syntax) |


## Range operator: BETWEEN

The `BETWEEN` operator tests if a value is within a specified range.
It uses the syntax `value BETWEEN min AND max`:



| Description                                | Syntax                   |
|--------------------------------------------|--------------------------|
| Tests if a value is within a specified range| `value BETWEEN min AND max` |
| Equivalent statement for `BETWEEN`          | `SELECT value >= min AND value <= max;` |
| Tests if a value does not fall within the specified range | `value NOT BETWEEN min AND max` |
| Equivalent statement for `NOT BETWEEN`      | `SELECT value < min OR value > max;` |



A `NULL` in a `BETWEEN` or `NOT BETWEEN` statement is evaluated
using the standard `NULL` evaluation rules applied to the equivalent
expression above:

| Expression                  | Result |
|-----------------------------|--------|
| NULL BETWEEN 2 AND 4      | `null` |
| 2 BETWEEN NULL AND 6      | `null` |
| 2 BETWEEN 3 AND NULL      | `false`|
| 8 BETWEEN NULL AND 6      | `false`|


The `BETWEEN` and `NOT BETWEEN` operators can also be used to
evaluate any orderable type.  For example, a `VARCHAR`:

| Expression                         | Result |
|------------------------------------|--------|
| 'Paul' BETWEEN 'John' AND 'Ringo' | `true` |


Note that the value, min, and max parameters to `BETWEEN` and `NOT
BETWEEN` must be the same type.  For example, Minerva will produce an
error if you ask it if John is between 2.3 and 35.2.


## IS NULL and IS NOT NULL

The `IS NULL` and `IS NOT NULL` operators test whether a value
is null (undefined).  Both operators work for all data types.

| Expression                | Result |
|---------------------------|--------|
| NULL IS NULL      | `true` |
| SELECT 3.0 IS NULL      | `false` |



## IS DISTINCT FROM and IS NOT DISTINCT FROM

In SQL, a NULL value represents an unknown value, and any comparison involving NULL will result in NULL. However, the IS DISTINCT FROM and IS NOT DISTINCT FROM operators treat NULL as a known value. Both operators ensure a reliable true or false outcome even in the presence of NULL input:

| Expression                                   | Result  |
|----------------------------------------------|--------|
|SELECT NULL IS DISTINCT FROM NULL;            | `false` |
|SELECT NULL IS NOT DISTINCT FROM NULL         | `true`  |

In the example provided above, a NULL value is not treated as distinct from another NULL. When comparing values that may include NULL, these operators can ensure either a TRUE or FALSE result.

The following truth table illustrates the handling of NULL in IS DISTINCT FROM and IS NOT DISTINCT FROM:

| a      | b      | a = b   | a <> b  | a DISTINCT b | a NOT DISTINCT b |
| ------ | ------ | ------- | ------- | ------------ | ---------------- |
| `1`    | `1`    | `TRUE`  | `FALSE` | `FALSE`      | `TRUE`           |
| `1`    | `2`    | `FALSE` | `TRUE`  | `TRUE`       | `FALSE`          |
| `1`    | `NULL` | `NULL`  | `NULL`  | `TRUE`       | `FALSE`          |
| `NULL` | `NULL` | `NULL`  | `NULL`  | `FALSE`      | `TRUE`           |

## GREATEST and LEAST

These functions are not part of the SQL standard but are a common extension. Similar to most other functions in Minerva, they return null if any argument is null. It's worth noting that in some other databases, such as PostgreSQL, these functions only return null if all arguments are null.


The following types are supported:
`DOUBLE`,
`BIGINT`,
`VARCHAR`,
`TIMESTAMP`,
`TIMESTAMP WITH TIME ZONE`,
`DATE`


| Function                     | Description                               | Return Type   |
|------------------------------|-------------------------------------------|---------------|
| `greatest(value1, ..., valueN)` | Returns the largest of the provided values. | `[same as input]` |
| `least(value1, ..., valueN)`    | Returns the smallest of the provided values. | `[same as input]` |



## Quantified comparison predicates: ALL, ANY and SOME

The `ALL`, `ANY` and `SOME` quantifiers can be used together with comparison operators in the
following way:

```text
expression operator quantifier ( subquery )
```

For example:

| Expression                                           | Result |
| ----------------------------------------------------- | ------ |
| 'hello' = ANY (VALUES 'hello', 'world')               |` true `  |
| 21 < ALL (VALUES 19, 20, 21)                          | `false`  |
| 42 >= SOME (SELECT 41 UNION ALL SELECT 42 UNION ALL SELECT 43) | `true `  |


Here are the meanings of some quantifier and comparison operator combinations:


| Expression           | Meaning                                                |
|----------------------|--------------------------------------------------------|
| `A = ALL (...)`      | Evaluates to `true` when `A` is equal to all values.    |
| `A <> ALL (...)`     | Evaluates to `true` when `A` doesn't match any value.   |
| `A < ALL (...)`      | Evaluates to `true` when `A` is smaller than the smallest value. |
| `A = ANY (...)`      | Evaluates to `true` when `A` is equal to any of the values. This form is equivalent to `A IN (...)`. |
| `A <> ANY (...)`     | Evaluates to `true` when `A` doesn't match one or more values. |
| `A < ANY (...)`      | Evaluates to `true` when `A` is smaller than the biggest value. |

`ANY` and `SOME` have the same meaning and can be used interchangeably.


## Pattern comparison: LIKE

The `LIKE` operator can be used to compare values with a pattern:

```sql
... column [NOT] LIKE 'pattern' ESCAPE 'character';
```

Matching characters is case sensitive, and the pattern supports two symbols for
matching:

- **`_`** matches any single character
- **`%`** matches zero or more characters

Typically it is often used as a condition in `WHERE` statements. An example is
a query to find all continents starting with `E`, which returns `Europe`:

```sql
SELECT * FROM (VALUES 'America', 'Asia', 'Africa', 'Europe', 'Australia', 'Antarctica') AS t (continent)
WHERE continent LIKE 'E%';
```

You can negate the result by adding `NOT`, and get all other continents, all
not starting with `E`:

```sql
SELECT * FROM (VALUES 'America', 'Asia', 'Africa', 'Europe', 'Australia', 'Antarctica') AS t (continent)
WHERE continent NOT LIKE 'E%';
```

If you only have one specific character to match, you can use the **`_`** symbol
for each character. The following query uses two underscores and produces only
`Asia` as result:

```sql
SELECT * FROM (VALUES 'America', 'Asia', 'Africa', 'Europe', 'Australia', 'Antarctica') AS t (continent)
WHERE continent LIKE 'A__A';
```

The wildcard characters **`_`** and **`%`** must be escaped to allow you to match
them as literals. This can be achieved by specifying the `ESCAPE` character to
use:

```sql
SELECT 'South_America' LIKE 'South\_America' ESCAPE '\';
```

The above query returns `true` since the escaped underscore symbol matches. If
you need to match the used escape character as well, you can escape it.

If you want to match for the chosen escape character, you simply escape itself.
For example, you can use `\\` to match for `\`.

## Row comparison: IN

The `IN` operator can be used in a `WHERE` clause to compare column values with 
a list of values. The list of values can be supplied by a subquery or directly 
as static values in an array:

```sql
... WHERE column [NOT] IN ('value1','value2');
... WHERE column [NOT] IN ( subquery );
```

Use the optional `NOT` keyword to negate the condition.

The following example shows a simple usage with a static array:

```sql
SELECT * FROM region WHERE name IN ('AMERICA', 'EUROPE');
```

The values in the clause are used for multiple comparisons that are combined as
a logical `OR`. The preceding query is equivalent to the following query:

```sql
SELECT * FROM region WHERE name = 'AMERICA' OR name = 'EUROPE';
```

You can negate the comparisons by adding `NOT`, and get all other regions
except the values in list:

```sql
SELECT * FROM region WHERE name NOT IN ('AMERICA', 'EUROPE');
```

When using a subquery to determine the values to use in the comparison, the
subquery must return a single column and one or more rows.

```sql
SELECT name
FROM nation
WHERE regionkey IN (
    SELECT starts_with(regionkey,"A") AS regionkey
    FROM region
);
```

