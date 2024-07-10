# DROP SCHEMA

## Synopsis

```yaml
DROP SCHEMA [ IF EXISTS ] schema_name [ CASCADE | RESTRICT ]
```

## Description

Drop an existing schema. The schema must be empty.

The optional `IF EXISTS` clause causes the error to be suppressed if the schema does not exist.

## Examples

Drop the schema `web`:

```yaml
DROP SCHEMA web
```

Drop the schema `sales` if it exists:

```yaml
DROP SCHEMA IF EXISTS sales
```

Drop the schema `archive`, along with everything it contains:

```yaml
DROP SCHEMA archive CASCADE
```

## See also

[ALTER SCHEMA](./alter_schema.md) 

[CREATE SCHEMA](./create_schema.md)