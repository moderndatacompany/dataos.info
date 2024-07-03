# SHOW SESSION

## Synopsis

```yaml
SHOW SESSION [ LIKE pattern ]
```

## Description

List the current [**session properties**](./set_session.md).

Specify a pattern in the optional `LIKE` clause to filter the results to the desired subset. For example, the following query allows you to find session properties that begin with `query`:

```yaml
SHOW SESSION LIKE 'query%'
```

## See also

[RESET SESSION](./reset_session.md) 

[SET SESSION](./set_session.md)