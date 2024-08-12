# ALTER TABLE

## Synopsis

```yaml
ALTER TABLE [ IF EXISTS ] name RENAME TO new_name
ALTER TABLE [ IF EXISTS ] name ADD COLUMN [ IF NOT EXISTS ] column_name data_type
  [ NOT NULL ] [ COMMENT comment ]
  [ WITH ( property_name = expression [, ...] ) ]
ALTER TABLE [ IF EXISTS ] name DROP COLUMN [ IF EXISTS ] column_name
ALTER TABLE [ IF EXISTS ] name RENAME COLUMN [ IF EXISTS ] old_name TO new_name
ALTER TABLE [ IF EXISTS ] name ALTER COLUMN column_name SET DATA TYPE new_type
ALTER TABLE name SET AUTHORIZATION ( user | USER user | ROLE role )
ALTER TABLE name SET PROPERTIES property_name = expression [, ...]
ALTER TABLE name EXECUTE command [ ( parameter => expression [, ... ] ) ]
    [ WHERE expression ]
```

## Description

Change the definition of an existing table.

The optional `IF EXISTS` (when used before the table name) clause causes the error to be suppressed if the table does not exists.

The optional `IF EXISTS` (when used before the column name) clause causes the error to be suppressed if the column does not exists.

The optional `IF NOT EXISTS` clause causes the error to be suppressed if the column already exists.

### SET PROPERTIES

The `ALTER TABLE SET PROPERTIES` statement followed by some number of `property_name` and `expression` pairs applies the specified properties and values to a table. Ommitting an already-set property from this statement leaves that property unchanged in the table.

A property in a `SET PROPERTIES` statement can be set to `DEFAULT`, which reverts its value back to the default in that table.

Support for `ALTER TABLE SET PROPERTIES` varies between connectors, as not all connectors support modifying table properties.

### EXECUTE

The `ALTER TABLE EXECUTE` statement followed by a `command` and `parameters` modifies the table according to the specified command and parameters. `ALTER TABLE EXECUTE` supports different commands on a per-connector basis.

You can use the `=>` operator for passing named parameter values. The left side is the name of the parameter, the right side is the value being passed:

```yaml
ALTER TABLE hive.schema.test_table EXECUTE optimize(file_size_threshold => '10MB')
```

## Examples

Rename table `users` to `people`:

```yaml
ALTER TABLE users RENAME TO people;
```

Rename table `users` to `people` if table `users` exists:

```yaml
ALTER TABLE IF EXISTS users RENAME TO people;
```

Add column `zip` to the `users` table:

```yaml
ALTER TABLE users ADD COLUMN zip varchar;
```

Add column `zip` to the `users` table if table `users` exists and column `zip` not already exists:

```yaml
ALTER TABLE IF EXISTS users ADD COLUMN IF NOT EXISTS zip varchar;
```

Drop column `zip` from the `users` table:

```yaml
ALTER TABLE users DROP COLUMN zip;
```

Drop column `zip` from the `users` table if table `users` and column `zip` exists:

```yaml
ALTER TABLE IF EXISTS users DROP COLUMN IF EXISTS zip;
```

Rename column `id` to `user_id` in the `users` table:

```yaml
ALTER TABLE users RENAME COLUMN id TO user_id;
```

Rename column `id` to `user_id` in the `users` table if table `users` and column `id` exists:

```yaml
ALTER TABLE IF EXISTS users RENAME column IF EXISTS id to user_id;
```

Change type of column `id` to `bigint` in the `users` table:

```yaml
ALTER TABLE users ALTER COLUMN id SET DATA TYPE bigint;
```

Change owner of table `people` to user `alice`:

```yaml
ALTER TABLE people SET AUTHORIZATION alice
```

Allow everyone with role public to drop and alter table `people`:

```yaml
ALTER TABLE people SET AUTHORIZATION ROLE PUBLIC
```

Set table properties (`x = y`) in table `people`:

```yaml
ALTER TABLE people SET PROPERTIES x = 'y';
```

Set multiple table properties (`foo = 123` and `foo bar = 456`) in table `people`:

```yaml
ALTER TABLE people SET PROPERTIES foo = 123, "foo bar" = 456;
```

Set table property `x` to its default value in table``people``:

```yaml
ALTER TABLE people SET PROPERTIES x = DEFAULT;
```

Collapse files in a table that are over 10 megabytes in size, as supported by the Hive connector:

```yaml
ALTER TABLE hive.schema.test_table EXECUTE optimize(file_size_threshold => '10MB')
```

## See also

[CREATE TABLE](/interfaces/workbench/sql_syntaxes/create_table/)