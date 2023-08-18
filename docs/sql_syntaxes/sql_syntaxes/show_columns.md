# SHOW COLUMNS

## Synopsis

```yaml
SHOW COLUMNS FROM table [ LIKE pattern ]
```

## Description

List the columns in a `table` along with their data type and other attributes:

```yaml
SHOW COLUMNS FROM nation;
```

```yaml
  Column   |     Type     | Extra | Comment
-----------+--------------+-------+---------
 nationkey | bigint       |       |
 name      | varchar(25)  |       |
 regionkey | bigint       |       |
 comment   | varchar(152) |       |
```

Specify a pattern in the optional `LIKE` clause to filter the results to the desired subset. For example, the following query allows you to find columns ending in `key`:

```yaml
SHOW COLUMNS FROM nation LIKE '%key';
```

```yaml
  Column   |     Type     | Extra | Comment
-----------+--------------+-------+---------
 nationkey | bigint       |       |
 regionkey | bigint       |       |
```