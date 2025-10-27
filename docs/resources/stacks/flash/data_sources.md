# Supported Data Sources in Flash

Flash is designed to work exclusively with DataOS Lakehouse, which uses the Iceberg table format. This section provides guidance on configuring Flash Service for [Depots](/resources/depot/) with DataOS Lakehouse.

## DataOS Lakehouse (Iceberg format)

To configure Flash Service for DataOS Lakehouse with Iceberg format, add the following configuration in the Stack-specific section of the Flash Service manifest file. Replace the placeholders with actual values, customize the query, and adjust scheduling as needed.

**Example Configuration:**

```yaml
# DataOS Lakehouse with Iceberg format
datasets:
  - address: dataos://lakehouse:flash/records
    name: customer

init:
  - create or replace table mycustomer as (select * from customer)

schedule:
  - expression: "*/2 * * * *"
    sql: INSERT INTO mycustomer BY NAME (select * from customer);
```

**Additional Examples:**

```yaml
# Using S3 with Iceberg format
datasets:
  - address: dataos://s3iceberg:iceberg_sink_s3/ice_groot
    name: customer

init:
  - create or replace table mycustomer as (select * from customer)

schedule:
  - expression: "*/2 * * * *"
    sql: INSERT INTO mycustomer BY NAME (select * from customer);
```

<<<<<<< HEAD
```yaml
# Using Azure ABFSS with Iceberg format
datasets:
  - address: dataos://azureabfss:iceberg_data/customer_data
    name: customer

init:
  - create or replace table mycustomer as (select * from customer)

schedule:
  - expression: "*/2 * * * *"
    sql: INSERT INTO mycustomer BY NAME (select * from customer);
```

You can retrieve the dataset address from [Metis](/interfaces/metis/). This configuration allows Flash to cache datasets from DataOS Lakehouse, ensuring efficient data access and query performance.
=======
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
>>>>>>> 3ba9f674e59b9131c1339af994c35c9bdc8a12fc
