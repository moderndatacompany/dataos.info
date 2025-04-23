# Handling Empty Tables in Flash

## Issue

In Flash, attempting to create tables or views for datasets with no records can result in failures, as the absence of data prevents the retrieval of a schema. Without a schema, Flash cannot generate the required tables or views, leading to errors like the one shown below:

```
2024-10-08 09:13:52,822: flash - ERROR - flash_migrations.py:130 - could not create view - `operating_system` for dataset - `{'address': 'dataos://icebase:pminsights/os?acl=rw', 'name': 'operating_system'}`, error - IO Error: Iceberg metadata file not found for table version '2' using 'none' compression and format(s): 'v%s%s.metadata.json,%s%s.metadata.json'
```

## Workaround

To handle this issue, a dummy row can be inserted into the empty table. This allows the schema to be generated, enabling Flash to create the necessary views or tables. Once real data is added, the dummy row can be filtered out or removed without affecting actual data.

**Example:**

```sql
SELECT
    uuid,
    serial,
    product,
    in_warranty,
    purchased,
    shipped,
    country,
    upgrade_url,
    device_uuid,
    device_warranty_expiration
FROM warranty_input
UNION ALL
SELECT
    'dummy' AS uuid,
    'dummy' AS serial,
    'dummy' AS product,
    NULL AS in_warranty,
    NULL AS purchased,
    NULL AS shipped,
    'dummy' AS country,
    'dummy' AS upgrade_url,
    'dummy' AS device_uuid,
    NULL AS device_warranty_expiration
WHERE (SELECT COUNT(1) FROM warranty_input) = 0
```

## Rationale

Flash's error handling when encountering an empty table is correct, as it cannot infer a schema from nonexistent data. By using a dummy row, the schema can be generated, enabling table/view creation while ensuring data integrity. The dummy row can be safely removed or ignored once the table is populated with actual data. This workaround should only be used until the table contains real data, at which point the dummy row is no longer necessary.