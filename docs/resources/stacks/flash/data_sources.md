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
