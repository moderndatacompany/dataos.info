# RESET SESSION

## Synopsis

```yaml
RESET SESSION name
RESET SESSION catalog.name
```

## Description

Reset a [**session property**](./set_session.md) value to the default value.

## Examples

```yaml
RESET SESSION optimize_hash_generation;
RESET SESSION hive.optimized_reader_enabled;
```

## See also

[SET SESSION](./set_session.md) 

[SHOW SESSION](./show_session.md)