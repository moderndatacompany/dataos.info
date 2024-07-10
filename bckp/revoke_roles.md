# REVOKE ROLES

## Synopsis

```yaml
REVOKE
[ ADMIN OPTION FOR ]
role [, ...]
FROM ( user | USER user | ROLE role) [, ...]
[ GRANTED BY ( user | USER user | ROLE role | CURRENT_USER | CURRENT_ROLE ) ]
[ IN catalog ]
```

## Description

Revokes the specified role(s) from the specified principal(s).

If the `ADMIN OPTION FOR` clause is specified, the `GRANT` permission is revoked instead of the role.

For the `REVOKE` statement for roles to succeed, the user executing it either should be the role admin or should possess the `GRANT` option for the given role.

The optional `GRANTED BY` clause causes the role(s) to be revoked with the specified principal as a revoker. If the `GRANTED BY` clause is not specified, the roles are revoked by the current user as a revoker.

The optional `IN catalog` clause revokes the roles in a catalog as opposed to a system roles.

## Examples

Revoke role `bar` from user `foo`

```yaml
REVOKE bar FROM USER foo;
```

Revoke admin option for roles `bar` and `foo` from user `baz` and role `qux`

```yaml
REVOKE ADMIN OPTION FOR bar, foo FROM USER baz, ROLE qux;
```

## Limitations

Some connectors do not support role management. See connector documentation for more details.

## See also

[CREATE ROLE](./create_role.md) 

[DROP ROLE](./drop_role.md) 

[SET ROLE](./set_role.md) 

[GRANT ROLES](./grant_roles.md)