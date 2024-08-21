# EXECUTE IMMEDIATE

## Synopsis

```yaml
EXECUTE IMMEDIATE `statement` [ USING parameter1 [ , parameter2, ... ] ]
```

## Description

Executes a statement without the need to prepare or deallocate the statement. Parameter values are defined in the `USING` clause.

## Examples

Execute a query with no parameters:

```yaml
EXECUTE IMMEDIATE
'SELECT name FROM nation';
```

Execute a query with two parameters:

```yaml
EXECUTE IMMEDIATE
'SELECT name FROM nation WHERE regionkey = ? and nationkey < ?'
USING 1, 3;
```

This is equivalent to:

```yaml
PREPARE statement_name FROM SELECT name FROM nation WHERE regionkey = ? and nationkey < ?
EXECUTE statement_name USING 1, 3
DEALLOCATE PREPARE statement_name
```

## See also

[EXECUTE](/interfaces/workbench/sql_syntaxes/execute/) 

[PREPARE](/interfaces/workbench/sql_syntaxes/prepare/) 

[DEALLOCATE PREPARE](/interfaces/workbench/sql_syntaxes/deallocate_prepare/)