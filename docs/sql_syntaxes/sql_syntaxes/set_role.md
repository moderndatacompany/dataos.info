# SET ROLE

## Synopsis

```yaml
SET ROLE ( role | ALL | NONE )
[ IN catalog ]
```

## Description

`SET ROLE` sets the enabled role for the current session.

`SET ROLE role` enables a single specified role for the current session. For the `SET ROLE role` statement to succeed, the user executing it should have a grant for the given role.

`SET ROLE ALL` enables all roles that the current user has been granted for the current session.

`SET ROLE NONE` disables all the roles granted to the current user for the current session.

The optional `IN catalog` clause sets the role in a catalog as opposed to a system role.

## Limitations

Some connectors do not support role management. See connector documentation for more details.

## See also

[CREATE ROLE](./create_role.md) 

[DROP ROLE](./drop_role.md) 

[GRANT ROLES](./grant_roles.md) 

[REVOKE ROLES](./revoke_roles.md)