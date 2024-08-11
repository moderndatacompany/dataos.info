# DESCRIBE OUTPUT

## Synopsis

```yaml
DESCRIBE OUTPUT statement_name
```

## Description

List the output columns of a prepared statement, including the column name (or alias), catalog, schema, table, type, type size in bytes, and a boolean indicating if the column is aliased.

## Examples

Prepare and describe a query with four output columns:

```yaml
PREPARE my_select1 FROM
SELECT * FROM nation;
```

```yaml
DESCRIBE OUTPUT my_select1;
```

```yaml
 Column Name | Catalog | Schema | Table  |  Type   | Type Size | Aliased
-------------+---------+--------+--------+---------+-----------+---------
 nationkey   | tpch    | sf1    | nation | bigint  |         8 | false
 name        | tpch    | sf1    | nation | varchar |         0 | false
 regionkey   | tpch    | sf1    | nation | bigint  |         8 | false
 comment     | tpch    | sf1    | nation | varchar |         0 | false
(4 rows)
```

Prepare and describe a query whose output columns are expressions:

```yaml
PREPARE my_select2 FROM
SELECT count(*) as my_count, 1+2 FROM nation;
```

```yaml
DESCRIBE OUTPUT my_select2;
```

```yaml
 Column Name | Catalog | Schema | Table |  Type  | Type Size | Aliased
-------------+---------+--------+-------+--------+-----------+---------
 my_count    |         |        |       | bigint |         8 | true
 _col1       |         |        |       | bigint |         8 | false
(2 rows)
```

Prepare and describe a row count query:

```yaml
PREPARE my_create FROM
CREATE TABLE foo AS SELECT * FROM nation;
```

```yaml
DESCRIBE OUTPUT my_create;
```

```yaml
 Column Name | Catalog | Schema | Table |  Type  | Type Size | Aliased
-------------+---------+--------+-------+--------+-----------+---------
 rows        |         |        |       | bigint |         8 | false
(1 row)
```

## See also

[PREPARE](/interfaces/workbench/sql_syntaxes/prepare/)