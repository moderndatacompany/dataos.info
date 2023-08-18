# DROP MATERIALIZED VIEW

## Synopsis

```yaml
DROP MATERIALIZED VIEW [ IF EXISTS ] view_name
```

## Description

Drop an existing materialized view `view_name`.

The optional `IF EXISTS` clause causes the error to be suppressed if the materialized view does not exist.

## Examples

Drop the materialized view `orders_by_date`:

```yaml
DROP MATERIALIZED VIEW orders_by_date;
```

Drop the materialized view `orders_by_date` if it exists:

```yaml
DROP MATERIALIZED VIEW IF EXISTS orders_by_date;
```

## See also

[CREATE MATERIALIZED VIEW](./create_materialized_view.md) 

[SHOW CREATE MATERIALIZED VIEW](./show_create_materialized_view.md) 

[REFRESH MATERIALIZED VIEW](./refresh_materialized_view.md)