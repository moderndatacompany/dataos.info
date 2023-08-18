# ANALYZE

## Synopsis

```yaml
ANALYZE table_name [ WITH ( property_name = expression [, ...] ) ]
```

## Description

Collects table and column statistics for a given table.

The optional `WITH` clause can be used to provide connector-specific properties. To list all available properties, run the following query:

```yaml
SELECT * FROM system.metadata.analyze_properties
```

## Examples

Analyze table `web` to collect table and column statistics:

```yaml
ANALYZE web;
```

Analyze table `stores` in catalog `hive` and schema `default`:

```yaml
ANALYZE hive.default.stores;
```

Analyze partitions `'1992-01-01', '1992-01-02'` from a Hive partitioned table `sales`:

```yaml
ANALYZE hive.default.sales WITH (partitions = ARRAY[ARRAY['1992-01-01'], ARRAY['1992-01-02']]);
```

Analyze partitions with complex partition key (`state` and `city` columns) from a Hive partitioned table `customers`:

```yaml
ANALYZE hive.default.customers WITH (partitions = ARRAY[ARRAY['CA', 'San Francisco'], ARRAY['NY', 'NY']]);
```

Analyze only columns `department` and `product_id` for partitions `'1992-01-01', '1992-01-02'` from a Hive partitioned table `sales`:

```yaml
ANALYZE hive.default.sales WITH (
    partitions = ARRAY[ARRAY['1992-01-01'], ARRAY['1992-01-02']],
    columns = ARRAY['department', 'product_id']);
```