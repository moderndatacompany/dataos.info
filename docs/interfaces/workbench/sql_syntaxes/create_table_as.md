# CREATE TABLE AS

## Synopsis

```yaml
CREATE TABLE [ IF NOT EXISTS ] table_name [ ( column_alias, ... ) ]
[ COMMENT table_comment ]
[ WITH ( property_name = expression [, ...] ) ]
AS query
[ WITH [ NO ] DATA ]
```

## Description

Create a new table containing the result of a [SELECT](./select.md) query. Use [CREATE TABLE](./create_table.md) to create an empty table.

The optional `IF NOT EXISTS` clause causes the error to be suppressed if the table already exists.

The optional `WITH` clause can be used to set properties on the newly created table. To list all available table properties, run the following query:

```yaml
SELECT * FROM system.metadata.table_properties
```

## Examples

Create a new table `orders_column_aliased` with the results of a query and the given column names:

```yaml
CREATE TABLE orders_column_aliased (order_date, total_price)
AS
SELECT orderdate, totalprice
FROM orders
```

Create a new table `orders_by_date` that summarizes `orders`:

```yaml
CREATE TABLE orders_by_date
COMMENT 'Summary of orders by date'
WITH (format = 'ORC')
AS
SELECT orderdate, sum(totalprice) AS price
FROM orders
GROUP BY orderdate
```

Create the table `orders_by_date` if it does not already exist:

```yaml
CREATE TABLE IF NOT EXISTS orders_by_date AS
SELECT orderdate, sum(totalprice) AS price
FROM orders
GROUP BY orderdate
```

Create a new `empty_nation` table with the same schema as `nation` and no data:

```yaml
CREATE TABLE empty_nation AS
SELECT *
FROM nation
WITH NO DATA
```

## See also

[CREATE TABLE](./create_table.md) 

[SELECT](./select.md)