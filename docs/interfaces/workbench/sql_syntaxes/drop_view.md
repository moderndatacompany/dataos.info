# DROP VIEW

## Synopsis

```yaml
DROP VIEW [ IF EXISTS ] view_name
```

## Description

Drop an existing view.

The optional `IF EXISTS` clause causes the error to be suppressed if the view does not exist.

## Examples

Drop the view `orders_by_date`:

```yaml
DROP VIEW orders_by_date
```

Drop the view `orders_by_date` if it exists:

```yaml
DROP VIEW IF EXISTS orders_by_date
```

## See also

[CREATE VIEW](/interfaces/workbench/sql_syntaxes/create_view/)