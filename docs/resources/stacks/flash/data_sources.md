In this section, we will guide you to create Flash Service for different types of [Depots](/resources/depot/) supported by Flash.

## Iceberg format Depots

To configure Flash Service for Iceberg format Depots, copy the provided code in the Stack-specific section of the Flash Service manifest file. Replace the placeholders with your actual values, update the query as needed, and adjust the scheduling according to your requirements.

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

You can get the dataset address from [Metis](/interfaces/metis/).

## Redshift Depot

To configure Flash Service for Redshift Depots, copy the provided code in the Stack-specific section of the Flash Service manifest file. Replace the placeholders with your actual values, update the query as needed, and adjust the scheduling according to your requirements.

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

To configure Flash Service for Snowflake Depots, copy the provided code in the Stack-specific section of the Flash Service manifest file. Replace the placeholders with your actual values, update the query as needed, and adjust the scheduling according to your requirements.

```yaml
#Snowflake Example
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

To configure Flash Service for BigQuery Depots, copy the provided code in the Stack-specific section of the Flash Service manifest file. Replace the placeholders with your actual values, update the query as needed, and adjust the scheduling according to your requirements.

```yaml
# Bigquery Example
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