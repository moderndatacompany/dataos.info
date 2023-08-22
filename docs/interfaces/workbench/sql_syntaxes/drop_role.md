# DROP ROLE

## Synopsis

```yaml
DROP ROLE role_name
[ IN catalog ]
```

## Description

`DROP ROLE` drops the specified role.

For `DROP ROLE` statement to succeed, the user executing it should possess admin privileges for the given role.

The optional `IN catalog` clause drops the role in a catalog as opposed to a system role.

## Examples

Drop role `admin`

```yaml
DROP ROLE admin;
```

## Limitations

Some connectors do not support role management. See connector documentation for more details.

## See also

[CREATE ROLE](./create_role.md) 

[SET ROLE](./set_role.md) 

[GRANT ROLES](./grant_roles.md) 

[REVOKE ROLES](./revoke_roles.md)