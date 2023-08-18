# ALTER VIEW

## Synopsis

```yaml
ALTER VIEW name RENAME TO new_name
ALTER VIEW name SET AUTHORIZATION ( user | USER user | ROLE role )
```

## Description

Change the definition of an existing view.

## Examples

Rename view `people` to `users`:

```yaml
ALTER VIEW people RENAME TO users
```

Change owner of VIEW `people` to user `alice`:

```yaml
ALTER VIEW people SET AUTHORIZATION alice
```

## See also

[CREATE VIEW](./create_view.md)