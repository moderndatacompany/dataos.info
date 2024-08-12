# SELECT

## Synopsis

```yaml
[ WITH [ RECURSIVE ] with_query [, ...] ]
SELECT [ ALL | DISTINCT ] select_expression [, ...]
[ FROM from_item [, ...] ]
[ WHERE condition ]
[ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
[ HAVING condition]
[ WINDOW window_definition_list]
[ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
[ ORDER BY expression [ ASC | DESC ] [, ...] ]
[ OFFSET count [ ROW | ROWS ] ]
[ LIMIT { count | ALL } ]
[ FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES } ]
```

where `from_item` is one of

```yaml
table_name [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
```

```yaml
from_item join_type from_item
  [ ON join_condition | USING ( join_column [, ...] ) ]
```

```yaml
table_name [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
  MATCH_RECOGNIZE pattern_recognition_specification
    [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
```

For detailed description of `MATCH_RECOGNIZE` clause, see [**pattern recognition in FROM clause**](/interfaces/workbench/sql_syntaxes/match_recognize/).

```yaml
TABLE (table_function_invocation) [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
```

<!-- For description of table functions usage, see [table functions](https://trino.io/docs/current/functions/table.html). -->

and `join_type` is one of

```yaml
[ INNER ] JOIN
LEFT [ OUTER ] JOIN
RIGHT [ OUTER ] JOIN
FULL [ OUTER ] JOIN
CROSS JOIN
```

and `grouping_element` is one of

```yaml
()
expression
GROUPING SETS ( ( column [, ...] ) [, ...] )
CUBE ( column [, ...] )
ROLLUP ( column [, ...] )
```

## Description

Retrieve rows from zero or more tables.

## WITH clause

The `WITH` clause defines named relations for use within a query. It allows flattening nested queries or simplifying subqueries. For example, the following queries are equivalent:

```yaml
SELECT a, b
FROM (
  SELECT a, MAX(b) AS b FROM t GROUP BY a
) AS x;

WITH x AS (SELECT a, MAX(b) AS b FROM t GROUP BY a)
SELECT a, b FROM x;
```

This also works with multiple subqueries:

```yaml
WITH
  t1 AS (SELECT a, MAX(b) AS b FROM x GROUP BY a),
  t2 AS (SELECT a, AVG(d) AS d FROM y GROUP BY a)
SELECT t1.*, t2.*
FROM t1
JOIN t2 ON t1.a = t2.a;
```

Additionally, the relations within a `WITH` clause can chain:

```yaml
WITH
  x AS (SELECT a FROM t),
  y AS (SELECT a AS b FROM x),
  z AS (SELECT b AS c FROM y)
SELECT c FROM z;
```

>🗣 **Warning :**
Currently, the SQL for the `WITH` clause will be inlined anywhere the named relation is used. This means that if the relation is used more than once and the query is non-deterministic, the results may be different each time.
>

## WITH RECURSIVE clause

The `WITH RECURSIVE` clause is a variant of the `WITH` clause. It defines a list of queries to process, including recursive processing of suitable queries.

>🗣 **Warning :**
This feature is experimental only. Proceed to use it only if you understand potential query failures and the impact of the recursion processing on your workload.
>

A recursive `WITH`-query must be shaped as a `UNION` of two relations. The first relation is called the *recursion base*, and the second relation is called the *recursion step*. Trino supports recursive `WITH`-queries with a single recursive reference to a `WITH`-query from within the query. The name `T` of the query `T` can be mentioned once in the `FROM` clause of the recursion step relation.

The following listing shows a simple example, that displays a commonly used form of a single query in the list:

```yaml
WITH RECURSIVE t(n) AS (
    VALUES (1)
    UNION ALL
    SELECT n + 1 FROM t WHERE n < 4
)
SELECT sum(n) FROM t;
```

In the preceding query the simple assignment `VALUES (1)` defines the recursion base relation. `SELECT n + 1 FROM t WHERE n < 4` defines the recursion step relation. The recursion processing performs these steps:

- recursive base yields `1`
- first recursion yields `1 + 1 = 2`
- second recursion uses the result from the first and adds one: `2 + 1 = 3`
- third recursion uses the result from the second and adds one again: `3 + 1 = 4`
- fourth recursion aborts since `n = 4`
- this results in `t` having values `1`, `2`, `3` and `4`
- the final statement performs the sum operation of these elements with the final result value `10`

The types of the returned columns are those of the base relation. Therefore it is required that types in the step relation can be coerced to base relation types.

The `RECURSIVE` clause applies to all queries in the `WITH` list, but not all of them must be recursive. If a `WITH`-query is not shaped according to the rules mentioned above or it does not contain a recursive reference, it is processed like a regular `WITH`-query. Column aliases are mandatory for all the queries in the recursive `WITH` list.

The following limitations apply as a result of following the SQL standard and due to implementation choices, in addition to `WITH` clause limitations:

- only single-element recursive cycles are supported. Like in regular `WITH`queries, references to previous queries in the `WITH` list are allowed. References to following queries are forbidden.
- usage of outer joins, set operations, limit clause, and others is not always allowed in the step relation
- recursion depth is fixed, defaults to `10`, and doesn’t depend on the actual query results

You can adjust the recursion depth with the [**session property**](/interfaces/workbench/sql_syntaxes/set_session/) `max_recursion_depth`. When changing the value consider that the size of the query plan growth is quadratic with the recursion depth.

## SELECT clause

The `SELECT` clause specifies the output of the query. Each `select_expression` defines a column or columns to be included in the result.

```yaml
SELECT [ ALL | DISTINCT ] select_expression [, ...]
```

The `ALL` and `DISTINCT` quantifiers determine whether duplicate rows are included in the result set. If the argument `ALL` is specified, all rows are included. If the argument `DISTINCT` is specified, only unique rows are included in the result set. In this case, each output column must be of a type that allows comparison. If neither argument is specified, the behavior defaults to `ALL`.

### Select expressions

Each `select_expression` must be in one of the following forms:

```yaml
expression [ [ AS ] column_alias ]
```

```yaml
row_expression.* [ AS ( column_alias [, ...] ) ]
```

```yaml
relation.*
```

```yaml
*
```

In the case of `expression [ [ AS ] column_alias ]`, a single output column is defined.

In the case of `row_expression.* [ AS ( column_alias [, ...] ) ]`, the `row_expression` is an arbitrary expression of type `ROW`. All fields of the row define output columns to be included in the result set.

In the case of `relation.*`, all columns of `relation` are included in the result set. In this case column aliases are not allowed.

In the case of `*`, all columns of the relation defined by the query are included in the result set.

In the result set, the order of columns is the same as the order of their specification by the select expressions. If a select expression returns multiple columns, they are ordered the same way they were ordered in the source relation or row type expression.

If column aliases are specified, they override any preexisting column or row field names:

```yaml
SELECT (CAST(ROW(1, true) AS ROW(field1 bigint, field2 boolean))).* AS (alias1, alias2);
```

```yaml
 alias1 | alias2
--------+--------
      1 | true
(1 row)
```

Otherwise, the existing names are used:

```yaml
SELECT (CAST(ROW(1, true) AS ROW(field1 bigint, field2 boolean))).*;
```

```yaml
 field1 | field2
--------+--------
      1 | true
(1 row)
```

and in their absence, anonymous columns are produced:

```yaml
SELECT (ROW(1, true)).*;
```

```yaml
 _col0 | _col1
-------+-------
     1 | true
(1 row)
```

## GROUP BY clause

The `GROUP BY` clause divides the output of a `SELECT` statement into groups of rows containing matching values. A simple `GROUP BY` clause may contain any expression composed of input columns or it may be an ordinal number selecting an output column by position (starting at one).

The following queries are equivalent. They both group the output by the `nationkey` input column with the first query using the ordinal position of the output column and the second query using the input column name:

```yaml
SELECT count(*), nationkey FROM customer GROUP BY 2;

SELECT count(*), nationkey FROM customer GROUP BY nationkey;
```

`GROUP BY` clauses can group output by input column names not appearing in the output of a select statement. For example, the following query generates row counts for the `customer` table using the input column `mktsegment`:

`SELECT count(*) FROM customer GROUP BY mktsegment;`

```yaml
 _col0
-------
 29968
 30142
 30189
 29949
 29752
(5 rows)
```

When a `GROUP BY` clause is used in a `SELECT` statement all output expressions must be either aggregate functions or columns present in the `GROUP BY` clause.

### Complex grouping operations

Trino also supports complex aggregations using the `GROUPING SETS`, `CUBE` and `ROLLUP` syntax. This syntax allows users to perform analysis that requires aggregation on multiple sets of columns in a single query. Complex grouping operations do not support grouping on expressions composed of input columns. Only column names are allowed.

Complex grouping operations are often equivalent to a `UNION ALL` of simple `GROUP BY` expressions, as shown in the following examples. This equivalence does not apply, however, when the source of data for the aggregation is non-deterministic.

### GROUPING SETS

Grouping sets allow users to specify multiple lists of columns to group on. The columns not part of a given sublist of grouping columns are set to `NULL`.

```yaml
SELECT * FROM shipping;
```

```yaml
 origin_state | origin_zip | destination_state | destination_zip | package_weight
--------------+------------+-------------------+-----------------+----------------
 California   |      94131 | New Jersey        |            8648 |             13
 California   |      94131 | New Jersey        |            8540 |             42
 New Jersey   |       7081 | Connecticut       |            6708 |            225
 California   |      90210 | Connecticut       |            6927 |           1337
 California   |      94131 | Colorado          |           80302 |              5
 New York     |      10002 | New Jersey        |            8540 |              3
(6 rows)
```

`GROUPING SETS` semantics are demonstrated by this example query:

```yaml
SELECT origin_state, origin_zip, destination_state, sum(package_weight)
FROM shipping
GROUP BY GROUPING SETS (
    (origin_state),
    (origin_state, origin_zip),
    (destination_state));
```

```yaml
 origin_state | origin_zip | destination_state | _col0
--------------+------------+-------------------+-------
 New Jersey   | NULL       | NULL              |   225
 California   | NULL       | NULL              |  1397
 New York     | NULL       | NULL              |     3
 California   |      90210 | NULL              |  1337
 California   |      94131 | NULL              |    60
 New Jersey   |       7081 | NULL              |   225
 New York     |      10002 | NULL              |     3
 NULL         | NULL       | Colorado          |     5
 NULL         | NULL       | New Jersey        |    58
 NULL         | NULL       | Connecticut       |  1562
(10 rows)
```

The preceding query may be considered logically equivalent to a `UNION ALL` of multiple `GROUP BY` queries:

```yaml
SELECT origin_state, NULL, NULL, sum(package_weight)
FROM shipping GROUP BY origin_state

UNION ALL

SELECT origin_state, origin_zip, NULL, sum(package_weight)
FROM shipping GROUP BY origin_state, origin_zip

UNION ALL

SELECT NULL, NULL, destination_state, sum(package_weight)
FROM shipping GROUP BY destination_state;
```

However, the query with the complex grouping syntax (`GROUPING SETS`, `CUBE` or `ROLLUP`) will only read from the underlying data source once, while the query with the `UNION ALL` reads the underlying data three times. This is why queries with a `UNION ALL` may produce inconsistent results when the data source is not deterministic.

### CUBE

The `CUBE` operator generates all possible grouping sets (i.e. a power set) for a given set of columns. For example, the query:

```yaml
SELECT origin_state, destination_state, sum(package_weight)
FROM shipping
GROUP BY CUBE (origin_state, destination_state);
```

is equivalent to:

```yaml
SELECT origin_state, destination_state, sum(package_weight)
FROM shipping
GROUP BY GROUPING SETS (
    (origin_state, destination_state),
    (origin_state),
    (destination_state),
    ()
);
```

```yaml
 origin_state | destination_state | _col0
--------------+-------------------+-------
 California   | New Jersey        |    55
 California   | Colorado          |     5
 New York     | New Jersey        |     3
 New Jersey   | Connecticut       |   225
 California   | Connecticut       |  1337
 California   | NULL              |  1397
 New York     | NULL              |     3
 New Jersey   | NULL              |   225
 NULL         | New Jersey        |    58
 NULL         | Connecticut       |  1562
 NULL         | Colorado          |     5
 NULL         | NULL              |  1625
(12 rows)
```

### ROLLUP

The `ROLLUP` operator generates all possible subtotals for a given set of columns. For example, the query:

```yaml
SELECT origin_state, origin_zip, sum(package_weight)
FROM shipping
GROUP BY ROLLUP (origin_state, origin_zip);
```

```yaml
 origin_state | origin_zip | _col2
--------------+------------+-------
 California   |      94131 |    60
 California   |      90210 |  1337
 New Jersey   |       7081 |   225
 New York     |      10002 |     3
 California   | NULL       |  1397
 New York     | NULL       |     3
 New Jersey   | NULL       |   225
 NULL         | NULL       |  1625
(8 rows)
```

is equivalent to:

```yaml
SELECT origin_state, origin_zip, sum(package_weight)
FROM shipping
GROUP BY GROUPING SETS ((origin_state, origin_zip), (origin_state), ());
```

### Combining multiple grouping expressions

Multiple grouping expressions in the same query are interpreted as having cross-product semantics. For example, the following query:

```yaml
SELECT origin_state, destination_state, origin_zip, sum(package_weight)
FROM shipping
GROUP BY
    GROUPING SETS ((origin_state, destination_state)),
    ROLLUP (origin_zip);
```

which can be rewritten as:

```yaml
SELECT origin_state, destination_state, origin_zip, sum(package_weight)
FROM shipping
GROUP BY
    GROUPING SETS ((origin_state, destination_state)),
    GROUPING SETS ((origin_zip), ());
```

is logically equivalent to:

```yaml
SELECT origin_state, destination_state, origin_zip, sum(package_weight)
FROM shipping
GROUP BY GROUPING SETS (
    (origin_state, destination_state, origin_zip),
    (origin_state, destination_state)
);
```

```yaml
 origin_state | destination_state | origin_zip | _col3
--------------+-------------------+------------+-------
 New York     | New Jersey        |      10002 |     3
 California   | New Jersey        |      94131 |    55
 New Jersey   | Connecticut       |       7081 |   225
 California   | Connecticut       |      90210 |  1337
 California   | Colorado          |      94131 |     5
 New York     | New Jersey        | NULL       |     3
 New Jersey   | Connecticut       | NULL       |   225
 California   | Colorado          | NULL       |     5
 California   | Connecticut       | NULL       |  1337
 California   | New Jersey        | NULL       |    55
(10 rows)
```

The `ALL` and `DISTINCT` quantifiers determine whether duplicate grouping sets each produce distinct output rows. This is particularly useful when multiple complex grouping sets are combined in the same query. For example, the following query:

```yaml
SELECT origin_state, destination_state, origin_zip, sum(package_weight)
FROM shipping
GROUP BY ALL
    CUBE (origin_state, destination_state),
    ROLLUP (origin_state, origin_zip);
```

is equivalent to:

```yaml
SELECT origin_state, destination_state, origin_zip, sum(package_weight)
FROM shipping
GROUP BY GROUPING SETS (
    (origin_state, destination_state, origin_zip),
    (origin_state, origin_zip),
    (origin_state, destination_state, origin_zip),
    (origin_state, origin_zip),
    (origin_state, destination_state),
    (origin_state),
    (origin_state, destination_state),
    (origin_state),
    (origin_state, destination_state),
    (origin_state),
    (destination_state),
    ()
);
```

However, if the query uses the `DISTINCT` quantifier for the `GROUP BY`:

```yaml
SELECT origin_state, destination_state, origin_zip, sum(package_weight)
FROM shipping
GROUP BY DISTINCT
    CUBE (origin_state, destination_state),
    ROLLUP (origin_state, origin_zip);
```

only unique grouping sets are generated:

```yaml
SELECT origin_state, destination_state, origin_zip, sum(package_weight)
FROM shipping
GROUP BY GROUPING SETS (
    (origin_state, destination_state, origin_zip),
    (origin_state, origin_zip),
    (origin_state, destination_state),
    (origin_state),
    (destination_state),
    ()
);
```

The default set quantifier is `ALL`.

### GROUPING operation

`grouping(col1, ..., colN) -> bigint`

The grouping operation returns a bit set converted to decimal, indicating which columns are present in a grouping. It must be used in conjunction with `GROUPING SETS`, `ROLLUP`, `CUBE` or `GROUP BY` and its arguments must match exactly the columns referenced in the corresponding `GROUPING SETS`, `ROLLUP`, `CUBE` or `GROUP BY` clause.

To compute the resulting bit set for a particular row, bits are assigned to the argument columns with the rightmost column being the least significant bit. For a given grouping, a bit is set to 0 if the corresponding column is included in the grouping and to 1 otherwise. For example, consider the query below:

```yaml
SELECT origin_state, origin_zip, destination_state, sum(package_weight),
       grouping(origin_state, origin_zip, destination_state)
FROM shipping
GROUP BY GROUPING SETS (
    (origin_state),
    (origin_state, origin_zip),
    (destination_state)
);
```

```yaml
origin_state | origin_zip | destination_state | _col3 | _col4
--------------+------------+-------------------+-------+-------
California   | NULL       | NULL              |  1397 |     3
New Jersey   | NULL       | NULL              |   225 |     3
New York     | NULL       | NULL              |     3 |     3
California   |      94131 | NULL              |    60 |     1
New Jersey   |       7081 | NULL              |   225 |     1
California   |      90210 | NULL              |  1337 |     1
New York     |      10002 | NULL              |     3 |     1
NULL         | NULL       | New Jersey        |    58 |     6
NULL         | NULL       | Connecticut       |  1562 |     6
NULL         | NULL       | Colorado          |     5 |     6
(10 rows)
```

The first grouping in the above result only includes the `origin_state` column and excludes the `origin_zip` and `destination_state` columns. The bit set constructed for that grouping is `011` where the most significant bit represents `origin_state`.

## HAVING clause

The `HAVING` clause is used in conjunction with aggregate functions and the `GROUP BY` clause to control which groups are selected. A `HAVING` clause eliminates groups that do not satisfy the given conditions. `HAVING` filters groups after groups and aggregates are computed.

The following example queries the `customer` table and selects groups with an account balance greater than the specified value:

```yaml
SELECT count(*), mktsegment, nationkey,
       CAST(sum(acctbal) AS bigint) AS totalbal
FROM customer
GROUP BY mktsegment, nationkey
HAVING sum(acctbal) > 5700000
ORDER BY totalbal DESC;
```

```yaml
 _col0 | mktsegment | nationkey | totalbal
-------+------------+-----------+----------
  1272 | AUTOMOBILE |        19 |  5856939
  1253 | FURNITURE  |        14 |  5794887
  1248 | FURNITURE  |         9 |  5784628
  1243 | FURNITURE  |        12 |  5757371
  1231 | HOUSEHOLD  |         3 |  5753216
  1251 | MACHINERY  |         2 |  5719140
  1247 | FURNITURE  |         8 |  5701952
(7 rows)
```

## WINDOW clause

The `WINDOW` clause is used to define named window specifications. The defined named window specifications can be referred to in the `SELECT` and `ORDER BY` clauses of the enclosing query:

```yaml
SELECT orderkey, clerk, totalprice,
      rank() OVER w AS rnk
FROM orders
WINDOW w AS (PARTITION BY clerk ORDER BY totalprice DESC)
ORDER BY count() OVER w, clerk, rnk
```

The window definition list of `WINDOW` clause can contain one or multiple named window specifications of the form

`window_name AS (window_specification)`

A window specification has the following components:

- The existing window name, which refers to a named window specification in the `WINDOW` clause. The window specification associated with the referenced name is the basis of the current specification.
- The partition specification, which separates the input rows into different partitions. This is analogous to how the `GROUP BY` clause separates rows into different groups for aggregate functions.
- The ordering specification, which determines the order in which input rows will be processed by the window function.
- The window frame, which specifies a sliding window of rows to be processed by the function for a given row. If the frame is not specified, it defaults to `RANGE UNBOUNDED PRECEDING`, which is the same as `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. This frame contains all rows from the start of the partition up to the last peer of the current row. In the absence of `ORDER BY`, all rows are considered peers, so `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` is equivalent to `BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`. The window frame syntax supports additional clauses for row pattern recognition. If the row pattern recognition clauses are specified, the window frame for a particular row consists of the rows matched by a pattern starting from that row. Additionally, if the frame specifies row pattern measures, they can be called over the window, similarly to window functions. For more details, see [**Row pattern recognition in window structures**](/interfaces/workbench/sql_syntaxes/row_pattern_recognition_in_window_structures/).

Each window component is optional. If a window specification does not specify window partitioning, ordering or frame, those components are obtained from the window specification referenced by the `existing window name`, or from another window specification in the reference chain. In case when there is no `existing window name` specified, or none of the referenced window specifications contains the component, the default value is used.

## Set operations

`UNION` `INTERSECT` and `EXCEPT` are all set operations. These clauses are used to combine the results of more than one select statement into a single result set:

```yaml
query UNION [ALL | DISTINCT] query
```

```yaml
query INTERSECT [ALL | DISTINCT] query
```

```yaml
query EXCEPT [ALL | DISTINCT] query
```

The argument `ALL` or `DISTINCT` controls which rows are included in the final result set. If the argument `ALL` is specified all rows are included even if the rows are identical. If the argument `DISTINCT` is specified only unique rows are included in the combined result set. If neither is specified, the behavior defaults to `DISTINCT`.

Multiple set operations are processed left to right, unless the order is explicitly specified via parentheses. Additionally, `INTERSECT` binds more tightly than `EXCEPT` and `UNION`. That means `A UNION B INTERSECT C EXCEPT D` is the same as `A UNION (B INTERSECT C) EXCEPT D`.

### UNION clause

`UNION` combines all the rows that are in the result set from the first query with those that are in the result set for the second query. The following is an example of one of the simplest possible `UNION` clauses. It selects the value `13` and combines this result set with a second query that selects the value `42`:

```yaml
SELECT 13
UNION
SELECT 42;
```

```yaml
 _col0
-------
    13
    42
(2 rows)
```

The following query demonstrates the difference between `UNION` and `UNION ALL`. It selects the value `13` and combines this result set with a second query that selects the values `42` and `13`:

```yaml
SELECT 13
UNION
SELECT * FROM (VALUES 42, 13);
```

```yaml
 _col0
-------
    13
    42
(2 rows)
```

```yaml
SELECT 13
UNION ALL
SELECT * FROM (VALUES 42, 13);
```

```yaml
 _col0
-------
    13
    42
    13
(2 rows)
```

### INTERSECT clause

`INTERSECT` returns only the rows that are in the result sets of both the first and the second queries. The following is an example of one of the simplest possible `INTERSECT` clauses. It selects the values `13` and `42` and combines this result set with a second query that selects the value `13`. Since `42` is only in the result set of the first query, it is not included in the final results.:

```yaml
SELECT * FROM (VALUES 13, 42)
INTERSECT
SELECT 13;
```

```yaml
 _col0
-------
    13
(2 rows)
```

### EXCEPT clause

`EXCEPT` returns the rows that are in the result set of the first query, but not the second. The following is an example of one of the simplest possible `EXCEPT` clauses. It selects the values `13` and `42` and combines this result set with a second query that selects the value `13`. Since `13` is also in the result set of the second query, it is not included in the final result.:

```yaml
SELECT * FROM (VALUES 13, 42)
EXCEPT
SELECT 13;
```

```yaml
 _col0
-------
   42
(2 rows)
```

## ORDER BY clause

The `ORDER BY` clause is used to sort a result set by one or more output expressions:

```yaml
ORDER BY expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...]
```

Each expression may be composed of output columns, or it may be an ordinal number selecting an output column by position, starting at one. The `ORDER BY` clause is evaluated after any `GROUP BY` or `HAVING` clause, and before any `OFFSET`, `LIMIT` or `FETCH FIRST` clause. The default null ordering is `NULLS LAST`, regardless of the ordering direction.

Note that, following the SQL specification, an `ORDER BY` clause only affects the order of rows for queries that immediately contain the clause. Trino follows that specification, and drops redundant usage of the clause to avoid negative performance impacts.

In the following example, the clause only applies to the select statement.

```yaml
INSERT INTO some_table
SELECT * FROM another_table
ORDER BY field;
```

Since tables in SQL are inherently unordered, and the `ORDER BY` clause in this case does not result in any difference, but negatively impacts performance of running the overall insert statement, Trino skips the sort operation.

Another example where the `ORDER BY` clause is redundant, and does not affect the outcome of the overall statement, is a nested query:

```yaml
SELECT *
FROM some_table
    JOIN (SELECT * FROM another_table ORDER BY field) u
    ON some_table.key = u.key;
```

<!-- More background information and details can be found in a blog post about this optimization.-->

## OFFSET clause

The `OFFSET` clause is used to discard a number of leading rows from the result set:

```yaml
OFFSET count [ ROW | ROWS ]
```

If the `ORDER BY` clause is present, the `OFFSET` clause is evaluated over a sorted result set, and the set remains sorted after the leading rows are discarded:

```yaml
SELECT name FROM nation ORDER BY name OFFSET 22;
```

```yaml
      name
----------------
 UNITED KINGDOM
 UNITED STATES
 VIETNAM
(3 rows)
```

Otherwise, it is arbitrary which rows are discarded. If the count specified in the `OFFSET` clause equals or exceeds the size of the result set, the final result is empty.

## LIMIT or FETCH FIRST clause

The `LIMIT` or `FETCH FIRST` clause restricts the number of rows in the result set.

```yaml
LIMIT { count | ALL }
```

```yaml
FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES }
```

The following example queries a large table, but the `LIMIT` clause restricts the output to only have five rows (because the query lacks an `ORDER BY`, exactly which rows are returned is arbitrary):

```yaml
SELECT orderdate FROM orders LIMIT 5;
```

```yaml
 orderdate
------------
 1994-07-25
 1993-11-12
 1992-10-06
 1994-01-04
 1997-12-28
(5 rows)
```

`LIMIT ALL` is the same as omitting the `LIMIT` clause.

The `FETCH FIRST` clause supports either the `FIRST` or `NEXT` keywords and the `ROW` or `ROWS` keywords. These keywords are equivalent and the choice of keyword has no effect on query execution.

If the count is not specified in the `FETCH FIRST` clause, it defaults to `1`:

```yaml
SELECT orderdate FROM orders FETCH FIRST ROW ONLY;
```

```yaml
 orderdate
------------
 1994-02-12
(1 row)
```

If the `OFFSET` clause is present, the `LIMIT` or `FETCH FIRST` clause is evaluated after the `OFFSET` clause:

```yaml
SELECT * FROM (VALUES 5, 2, 4, 1, 3) t(x) ORDER BY x OFFSET 2 LIMIT 2;
```

```yaml
 x
---
 3
 4
(2 rows)
```

For the `FETCH FIRST` clause, the argument `ONLY` or `WITH TIES` controls which rows are included in the result set.

If the argument `ONLY` is specified, the result set is limited to the exact number of leading rows determined by the count.

If the argument `WITH TIES` is specified, it is required that the `ORDER BY` clause be present. The result set consists of the same set of leading rows and all of the rows in the same peer group as the last of them (‘ties’) as established by the ordering in the `ORDER BY` clause. The result set is sorted:

```yaml
SELECT name, regionkey
FROM nation
ORDER BY regionkey FETCH FIRST ROW WITH TIES;
```

```yaml
    name    | regionkey
------------+-----------
 ETHIOPIA   |         0
 MOROCCO    |         0
 KENYA      |         0
 ALGERIA    |         0
 MOZAMBIQUE |         0
(5 rows)
```

## TABLESAMPLE

There are multiple sample methods:

`BERNOULLI` Each row is selected to be in the table sample with a probability of the sample percentage. When a table is sampled using the Bernoulli method, all physical blocks of the table are scanned and certain rows are skipped (based on a comparison between the sample percentage and a random value calculated at runtime).
The probability of a row being included in the result is independent from any other row. This does not reduce the time required to read the sampled table from disk. It may have an impact on the total query time if the sampled output is processed further.`SYSTEM`This sampling method divides the table into logical segments of data and samples the table at this granularity. This sampling method either selects all the rows from a particular segment of data or skips it (based on a comparison between the sample percentage and a random value calculated at runtime).
The rows selected in a system sampling will be dependent on which connector is used. For example, when used with Hive, it is dependent on how the data is laid out on HDFS. This method does not guarantee independent sampling probabilities.

>📌 **Note :**
Neither of the two methods allow deterministic bounds on the number of rows returned.
>

Examples:

```yaml
SELECT *
FROM users TABLESAMPLE BERNOULLI (50);

SELECT *
FROM users TABLESAMPLE SYSTEM (75);
```

Using sampling with joins:

```yaml
SELECT o.*, i.*
FROM orders o TABLESAMPLE SYSTEM (10)
JOIN lineitem i TABLESAMPLE BERNOULLI (40)
  ON o.orderkey = i.orderkey;
```

## UNNEST

`UNNEST` can be used to expand an ARRAY or MAP into a relation. Arrays are expanded into a single column:

```yaml
SELECT * FROM UNNEST(ARRAY[1,2]) AS t(number);
```

```yaml
 number
--------
      1
      2
(2 rows)
```

Maps are expanded into two columns (key, value):

```yaml
SELECT * FROM UNNEST(
        map_from_entries(
            ARRAY[
                ('SQL',1974),
                ('Java', 1995)
            ]
        )
) AS t(language, first_appeared_year);
```

```yaml
 language | first_appeared_year
----------+---------------------
 SQL      |                1974
 Java     |                1995
(2 rows)
```

`UNNEST` can be used in combination with an `ARRAY` of ROW structures for expanding each field of the `ROW` into a corresponding column:

```yaml
SELECT *
FROM UNNEST(
        ARRAY[
            ROW('Java',  1995),
            ROW('SQL' , 1974)],
        ARRAY[
            ROW(false),
            ROW(true)]
) as t(language,first_appeared_year,declarative);
```

```yaml
 language | first_appeared_year | declarative
----------+---------------------+-------------
 Java     |                1995 | false
 SQL      |                1974 | true
(2 rows)
```

`UNNEST` can optionally have a `WITH ORDINALITY` clause, in which case an additional ordinality column is added to the end:

```yaml
SELECT a, b, rownumber
FROM UNNEST (
    ARRAY[2, 5],
    ARRAY[7, 8, 9]
     ) WITH ORDINALITY AS t(a, b, rownumber);
```

```yaml
  a   | b | rownumber
------+---+-----------
    2 | 7 |         1
    5 | 8 |         2
 NULL | 9 |         3
(3 rows)
```

`UNNEST` returns zero entries when the array/map is empty:

```yaml
SELECT * FROM UNNEST (ARRAY[]) AS t(value);
```

```yaml
 value
-------
(0 rows)
```

`UNNEST` returns zero entries when the array/map is null:

```yaml
SELECT * FROM UNNEST (CAST(null AS ARRAY(integer))) AS t(number);
```

```yaml
 number
--------
(0 rows)
```

`UNNEST` is normally used with a `JOIN`, and can reference columns from relations on the left side of the join:

```yaml
SELECT student, score
FROM (
   VALUES
      ('John', ARRAY[7, 10, 9]),
      ('Mary', ARRAY[4, 8, 9])
) AS tests (student, scores)
CROSS JOIN UNNEST(scores) AS t(score);
```

```yaml
 student | score
---------+-------
 John    |     7
 John    |    10
 John    |     9
 Mary    |     4
 Mary    |     8
 Mary    |     9
(6 rows)
```

`UNNEST` can also be used with multiple arguments, in which case they are expanded into multiple columns, with as many rows as the highest cardinality argument (the other columns are padded with nulls):

```yaml
SELECT numbers, animals, n, a
FROM (
  VALUES
    (ARRAY[2, 5], ARRAY['dog', 'cat', 'bird']),
    (ARRAY[7, 8, 9], ARRAY['cow', 'pig'])
) AS x (numbers, animals)
CROSS JOIN UNNEST(numbers, animals) AS t (n, a);
```

```yaml
  numbers  |     animals      |  n   |  a
-----------+------------------+------+------
 [2, 5]    | [dog, cat, bird] |    2 | dog
 [2, 5]    | [dog, cat, bird] |    5 | cat
 [2, 5]    | [dog, cat, bird] | NULL | bird
 [7, 8, 9] | [cow, pig]       |    7 | cow
 [7, 8, 9] | [cow, pig]       |    8 | pig
 [7, 8, 9] | [cow, pig]       |    9 | NULL
(6 rows)
```

`LEFT JOIN` is preferable in order to avoid losing the the row containing the array/map field in question when referenced columns from relations on the left side of the join can be empty or have `NULL` values:

```yaml
SELECT runner, checkpoint
FROM (
   VALUES
      ('Joe', ARRAY[10, 20, 30, 42]),
      ('Roger', ARRAY[10]),
      ('Dave', ARRAY[]),
      ('Levi', NULL)
) AS marathon (runner, checkpoints)
LEFT JOIN UNNEST(checkpoints) AS t(checkpoint) ON TRUE;
```

```yaml
 runner | checkpoint
--------+------------
 Joe    |         10
 Joe    |         20
 Joe    |         30
 Joe    |         42
 Roger  |         10
 Dave   |       NULL
 Levi   |       NULL
(7 rows)
```

Note that in case of using `LEFT JOIN` the only condition supported by the current implementation is `ON TRUE`.

## Joins

Joins allow you to combine data from multiple relations.

### CROSS JOIN

A cross join returns the Cartesian product (all combinations) of two relations. Cross joins can either be specified using the explit `CROSS JOIN` syntax or by specifying multiple relations in the `FROM` clause.

Both of the following queries are equivalent:

```yaml
SELECT *
FROM nation
CROSS JOIN region;

SELECT *
FROM nation, region;
```

The `nation` table contains 25 rows and the `region` table contains 5 rows, so a cross join between the two tables produces 125 rows:

```yaml
SELECT n.name AS nation, r.name AS region
FROM nation AS n
CROSS JOIN region AS r
ORDER BY 1, 2;
```

```yaml
     nation     |   region
----------------+-------------
 ALGERIA        | AFRICA
 ALGERIA        | AMERICA
 ALGERIA        | ASIA
 ALGERIA        | EUROPE
 ALGERIA        | MIDDLE EAST
 ARGENTINA      | AFRICA
 ARGENTINA      | AMERICA
...
(125 rows)
```

### LATERAL

Subqueries appearing in the `FROM` clause can be preceded by the keyword `LATERAL`. This allows them to reference columns provided by preceding `FROM` items.

A `LATERAL` join can appear at the top level in the `FROM` list, or anywhere within a parenthesized join tree. In the latter case, it can also refer to any items that are on the left-hand side of a `JOIN` for which it is on the right-hand side.

When a `FROM` item contains `LATERAL` cross-references, evaluation proceeds as follows: for each row of the `FROM` item providing the cross-referenced columns, the `LATERAL` item is evaluated using that row set’s values of the columns. The resulting rows are joined as usual with the rows they were computed from. This is repeated for set of rows from the column source tables.

`LATERAL` is primarily useful when the cross-referenced column is necessary for computing the rows to be joined:

```yaml
SELECT name, x, y
FROM nation
CROSS JOIN LATERAL (SELECT name || ' :-' AS x)
CROSS JOIN LATERAL (SELECT x || ')' AS y);
```

### Qualifying column names

When two relations in a join have columns with the same name, the column references must be qualified using the relation alias (if the relation has an alias), or with the relation name:

```yaml
SELECT nation.name, region.name
FROM nation
CROSS JOIN region;

SELECT n.name, r.name
FROM nation AS n
CROSS JOIN region AS r;

SELECT n.name, r.name
FROM nation n
CROSS JOIN region r;
```

The following query will fail with the error `Column 'name' is ambiguous`:

```yaml
SELECT name
FROM nation
CROSS JOIN region;
```

## Subqueries

A subquery is an expression which is composed of a query. The subquery is correlated when it refers to columns outside of the subquery. Logically, the subquery will be evaluated for each row in the surrounding query. The referenced columns will thus be constant during any single evaluation of the subquery.

>📌 **Note :**
Support for correlated subqueries is limited. Not every standard form is supported.
>

### EXISTS

The `EXISTS` predicate determines if a subquery returns any rows:

```yaml
SELECT name
FROM nation
WHERE EXISTS (
     SELECT *
     FROM region
     WHERE region.regionkey = nation.regionkey
);
```

### IN

The `IN` predicate determines if any values produced by the subquery are equal to the provided expression. The result of `IN` follows the standard rules for nulls. The subquery must produce exactly one column:

```yaml
SELECT name
FROM nation
WHERE regionkey IN (
     SELECT regionkey
     FROM region
     WHERE name = 'AMERICA' OR name = 'AFRICA'
);
```

### Scalar subquery

A scalar subquery is a non-correlated subquery that returns zero or one row. It is an error for the subquery to produce more than one row. The returned value is `NULL` if the subquery produces no rows:

```yaml
SELECT name
FROM nation
WHERE regionkey = (SELECT max(regionkey) FROM region);
```

>📌 **Note :**
Currently only single column can be returned from the scalar subquery.
>