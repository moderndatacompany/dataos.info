# START TRANSACTION

## Synopsis

```yaml
START TRANSACTION [ mode [, ...] ]
```

where `mode` is one of

```yaml
ISOLATION LEVEL { READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SERIALIZABLE }
READ { ONLY | WRITE }
```

## Description

Start a new transaction for the current session.

## Examples

```yaml
START TRANSACTION;
START TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION READ WRITE;
START TRANSACTION ISOLATION LEVEL READ COMMITTED, READ ONLY;
START TRANSACTION READ WRITE, ISOLATION LEVEL SERIALIZABLE;
```

## See also

[COMMIT](/interfaces/workbench/sql_syntaxes/commit/) 

[ROLLBACK](/interfaces/workbench/sql_syntaxes/rollback/)