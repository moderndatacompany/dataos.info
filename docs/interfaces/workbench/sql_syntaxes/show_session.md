# SHOW SESSION

## Synopsis

```yaml
SHOW SESSION [ LIKE pattern ]
```

## Description

List the current [**session properties**](/interfaces/workbench/sql_syntaxes/set_session/).

Specify a pattern in the optional `LIKE` clause to filter the results to the desired subset. For example, the following query allows you to find session properties that begin with `query`:

```yaml
SHOW SESSION LIKE 'query%'
```

## See also

[RESET SESSION](/interfaces/workbench/sql_syntaxes/reset_session/) 

[SET SESSION](/interfaces/workbench/sql_syntaxes/set_session/)