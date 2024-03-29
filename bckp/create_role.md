# CREATE ROLE

## Synopsis

```yaml
CREATE ROLE role_name
[ WITH ADMIN ( user | USER user | ROLE role | CURRENT_USER | CURRENT_ROLE ) ]
[ IN catalog ]
```

## Description

`CREATE ROLE` creates the specified role.

The optional `WITH ADMIN` clause causes the role to be created with the specified user as a role admin. A role admin has permission to drop or grant a role. If the optional `WITH ADMIN` clause is not specified, the role is created with current user as admin.

The optional `IN catalog` clause creates the role in a catalog as opposed to a system role.

## Examples

Create role `admin`

```yaml
CREATE ROLE admin;
```

Create role `moderator` with admin `bob`:

```yaml
CREATE ROLE moderator WITH ADMIN USER bob;
```

## Limitations

Some connectors do not support role management. See connector documentation for more details.

## See also

[DROP ROLE](./drop_role.md) 

[SET ROLE](./set_role.md) 

<!--[GRANT ROLES](./grant_roles.md)  -->

<!--[REVOKE ROLES](./revoke_roles.md) -->