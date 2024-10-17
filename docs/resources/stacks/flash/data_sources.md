# Supported Data Sources in Flash

This section provides guidance on configuring Flash Service for various types of [Depots](/resources/depot/) supported by Flash, including Iceberg, Redshift, Snowflake, and BigQuery formats.

## Iceberg format Depots

To configure Flash Service for Iceberg format Depots (e.g., DataOS Lakehouse, AWS S3, Azure ABFSS, Azure WASBS), add the following configuration in the Stack-specific section of the Flash Service manifest file. Replace the placeholders with actual values, customize the query, and adjust scheduling as needed.

```yaml
# Iceberg
datasets:
  - address: dataos://s3iceberg:iceberg_sink_s3/ice_groot
    name: customer

init:
  - create or replace table mycustomer as (select * from customer)

schedule:
  - expression: "*/2 * * * *"
    sql: INSERT INTO mycustomer BY NAME (select * from customer);
```

You can retrieve the dataset address from [Metis](/interfaces/metis/).

## Redshift Depot

For configuring Flash Service to work with Redshift Depots, use the following code. Ensure to replace the placeholders, modify the query as needed, and set the appropriate schedule.

```yaml
# Redshift Example
datasets:
  - name: f_sales
    depot: dataos://redshiftdepot
    sql: SELECT * FROM f_sales
    refresh:
      expression: "*/2 * * * *"
      sql: SELECT MAX(invoice_dt_sk) FROM f_sales
      where: invoice_dt_sk > CURRENT_SQL_RUN_VALUE
```

## Snowflake Depot

To configure Flash Service for Snowflake Depots, use the following configuration. Modify the placeholders and queries as necessary, and adjust the refresh schedule accordingly.

```yaml
# Snowflake Example
datasets:
  - name: f_sales_sf
    depot: dataos://stsnowflake
    sql: SELECT * FROM public.f_sales
    meta:
      schema: public
    refresh:
      expression: "*/2 * * * *"
      sql: SELECT MAX(invoice_dt_sk) FROM public.f_sales
      where: invoice_dt_sk > PREVIOUS_SQL_RUN_VALUE
```

## BigQuery Depot

For BigQuery Depots, configure the Flash Service using the following code. Update the dataset details, SQL query, and scheduling to fit your requirements.

```yaml
# BigQuery Example
datasets:
  - name: f_sales
    depot: dataos://bigquery
    sql: SELECT * FROM sales_360.f_sales
    meta:
      bucket: tmdcdemogcs
    refresh:
      expression: "*/2 * * * *"
      sql: SELECT MAX(invoice_dt_sk) FROM sales_360.f_sales
      where: invoice_dt_sk > PREVIOUS_SQL_RUN_VALUE
```

These configurations will allow Flash to cache datasets from various sources, ensuring efficient data access and query performance.