# ALTER SCHEMA

## Synopsis

```yaml
ALTER SCHEMA name RENAME TO new_name
ALTER SCHEMA name SET AUTHORIZATION ( user | USER user | ROLE role )
```

## Description

Change the definition of an existing schema.

## Examples

Rename schema `web` to `traffic`:

```yaml
ALTER SCHEMA web RENAME TO traffic
```

Change owner of schema `web` to user `alice`:

```yaml
ALTER SCHEMA web SET AUTHORIZATION alice
```

Allow everyone to drop schema and create tables in schema `web`:

```yaml
ALTER SCHEMA web SET AUTHORIZATION ROLE PUBLIC
```

## See also

[CREATE SCHEMA](/interfaces/workbench/sql_syntaxes/create_schema/)