# DENY

## Synopsis

```yaml
DENY ( privilege [, ...] | ( ALL PRIVILEGES ) )
ON ( table_name | TABLE table_name | SCHEMA schema_name)
TO ( user | USER user | ROLE role )
```

## Description

Denies the specified privileges to the specified grantee.

Deny on a table rejects the specified privilege on all current and future columns of the table.

Deny on a schema rejects the specified privilege on all current and future columns of all current and future tables of the schema.

## Examples

Deny `INSERT` and `SELECT` privileges on the table `orders` to user `alice`:

```yaml
DENY INSERT, SELECT ON orders TO alice;
```

Deny `DELETE` privilege on the schema `finance` to user `bob`:

```yaml
DENY DELETE ON SCHEMA finance TO bob;
```

Deny `SELECT` privilege on the table `orders` to everyone:

```yaml
DENY SELECT ON orders TO ROLE PUBLIC;
```

## Limitations

The system access controls as well as the connectors provided by default in Minerva have no support for `DENY`.

## See also

[GRANT](./grant.md) 

[REVOKE](./revoke.md) 

[SHOW GRANTS](./show_grants.md)