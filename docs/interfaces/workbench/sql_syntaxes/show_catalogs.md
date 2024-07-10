# SHOW CATALOGS

## Synopsis

```yaml
SHOW CATALOGS [ LIKE pattern ]
```

## Description

List the available catalogs.

Specify a pattern in the optional `LIKE` clause to filter the results to the desired subset. For example, the following query allows you to find catalogs that begin with `t`:

```yaml
SHOW CATALOGS LIKE 't%'
```