# SET SESSION

## Synopsis

```yaml
SET SESSION name = expression
SET SESSION catalog.name = expression
```

## Description

Set a session property value or a catalog session property.

## Session properties

A session property is a configuration property that can be temporarily modified by a user for the duration of the current connection session to the Trino cluster. Many configuration properties have a corresponding session property that accepts the same values as the config property.

There are two types of session properties:

- **System session properties** apply to the whole cluster. Most session properties are system session properties unless specified otherwise.
- **Catalog session properties** are connector-defined session properties that can be set on a per-catalog basis. These properties must be set separately for each catalog by including the catalog name as a prefix, such as `catalogname.property_name`.

Session properties are tied to the current session, so a user can have multiple connections to a cluster that each have different values for the same session properties. Once a session ends, either by disconnecting or creating a new session, any changes made to session properties during the previous session are lost.

## Examples

The following example sets a system session property to enable optimized hash generation:

`SET SESSION optimize_hash_generation = true;`

The following example sets the `optimize_locality_enabled` catalog session property for an Accumulo catalog named `acc01`:

`SET SESSION acc01.optimize_locality_enabled = false;`

The example `acc01.optimize_locality_enabled` catalog session property does not apply to any other catalog, even if another catalog also uses the Accumulo connector.

## See also

[RESET SESSION](/interfaces/workbench/sql_syntaxes/reset_session/) 

[SHOW SESSION](/interfaces/workbench/sql_syntaxes/show_session/)