# Snowflake Flare Configuration Templates

To read/write data on the Snowflake data source, you first need to create a depot on top of it. In case you haven’t created a Snowflake Depot navigate to the below link: [Snowflake Depot](/resources/depot/depot_config_templates/snowflake/).

## Read Config

Once you have set up a Snowflake Depot, you can start reading data from it. 

```yaml title="snowflake_depot_read.yml"
--8<-- "examples/resources/stacks/flare/snowflake_depot_read.yml"
```

## Write Config

```yaml title="snowflake_depot_write.yml"
--8<-- "examples/resources/stacks/flare/snowflake_depot_write.yml"
```