# RESET SESSION

## Synopsis

```yaml
RESET SESSION name
RESET SESSION catalog.name
```

## Description

Reset a [**session property**](/interfaces/workbench/sql_syntaxes/set_session/) value to the default value.

## Examples

```yaml
RESET SESSION optimize_hash_generation;
RESET SESSION hive.optimized_reader_enabled;
```

## See also

[SET SESSION](/interfaces/workbench/sql_syntaxes/set_session/) 

[SHOW SESSION](/interfaces/workbench/sql_syntaxes/show_session/)