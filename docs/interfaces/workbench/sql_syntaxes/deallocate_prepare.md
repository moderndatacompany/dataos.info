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

[PREPARE](/interfaces/workbench/sql_syntaxes/prepare/) 

[EXECUTE](/interfaces/workbench/sql_syntaxes/execute/) 

[EXECUTE IMMEDIATE](/interfaces/workbench/sql_syntaxes/execute_immediate/)