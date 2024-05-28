# DEALLOCATE PREPARE

## Synopsis

```yaml
DEALLOCATE PREPARE statement_name
```

## Description

Removes a statement with the name `statement_name` from the list of prepared statements in a session.

## Examples

Deallocate a statement with the name `my_query`:

```yaml
DEALLOCATE PREPARE my_query;
```

## See also

[PREPARE](./prepare.md) 

[EXECUTE](./execute.md) 

[EXECUTE IMMEDIATE](./execute_immediate.md)