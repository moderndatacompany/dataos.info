# VALUES

## Synopsis

```yaml
VALUES row [, ...]
```

where `row` is a single expression or

```yaml
( column_expression [, ...] )
```

## Description

Defines a literal inline table.

`VALUES` can be used anywhere a query can be used (e.g., the `FROM` clause of a [**SELECT**](/interfaces/workbench/sql_syntaxes/select/), an **INSERT**, or even at the top level). `VALUES` creates an anonymous table without column names, but the table and columns can be named using an `AS` clause with column aliases.

## Examples

Return a table with one column and three rows:

```yaml
VALUES 1, 2, 3
```

Return a table with two columns and three rows:

```yaml
VALUES
    (1, 'a'),
    (2, 'b'),
    (3, 'c')
```

Return table with column `id` and `name`:

```yaml
SELECT * FROM (
    VALUES
        (1, 'a'),
        (2, 'b'),
        (3, 'c')
) AS t (id, name)
```

Create a new table with column `id` and `name`:

```yaml
CREATE TABLE example AS
SELECT * FROM (
    VALUES
        (1, 'a'),
        (2, 'b'),
        (3, 'c')
) AS t (id, name)
```

## See also

<!-- [INSERT](./insert.md)  -->

[SELECT](/interfaces/workbench/sql_syntaxes/select/)