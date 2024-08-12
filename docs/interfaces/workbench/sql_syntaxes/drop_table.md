# DROP TABLE

## Synopsis

```yaml
DROP TABLE  [ IF EXISTS ] table_name
```

## Description

Drops an existing table.

The optional `IF EXISTS` clause causes the error to be suppressed if the table does not exist.

## Examples

Drop the table `orders_by_date`:

```yaml
DROP TABLE orders_by_date
```

Drop the table `orders_by_date` if it exists:

```yaml
DROP TABLE IF EXISTS orders_by_date
```

## See also

[ALTER TABLE](/interfaces/workbench/sql_syntaxes/alter_table/) 

[CREATE TABLE](./create_table.md)