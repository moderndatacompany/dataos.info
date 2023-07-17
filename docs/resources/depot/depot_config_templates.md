# Depot Config Templates

To make the process of creating a Depot configuration easier, we provide a set of predefined templates for various data sources. These templates serve as a starting point for configuring your Depot based on the specific data source you are working with. Simply choose the template that corresponds to your organization's data source and follow the instructions provided to fill in the required information.

It's important to note that when using these templates, you will need to populate the key-value properties in the YAML config file with the appropriate values for your data source. This requires a basic understanding of your organization's data infrastructure and the necessary credentials or connection details.

Here are some of the available Depot config templates:

## Depots on Data Warehouse

[Amazon Redshift](./depot_config_templates/amazon_redshift.md)

[Google BigQuery](./depot_config_templates/google_bigquery.md)

[Snowflake](./depot_config_templates/snowflake.md)

## Depots on Data Lake

[Amazon Simple Storage Service (S3)](./depot_config_templates/amazon_s3.md)

[Azure Blob File System Storage (ABFSS)](./depot_config_templates/azure_abfss.md)

[Windows Azure Storage Blob Service (WASBS)](./depot_config_templates/azure_wasbs.md)

[Google Cloud Storage (GCS)](./depot_config_templates/google_gcs.md)

## Depots on Streaming Source

[Apache Pulsar](./depot_config_templates/apache_pulsar.md)

[Eventhub](./depot_config_templates/eventhub.md)

[Apache Kafka](./depot_config_templates/kafka.md)

## Depots on NoSQL Databases


[Elasticsearch](./depot_config_templates/elasticsearch.md)

[MongoDB](./depot_config_templates/mongodb.md)

[Opensearch](./depot_config_templates/opensearch.md)

## Depots on Relational Databases

[Oracle](./depot_config_templates/oracle.md)

[JDBC](./depot_config_templates/jdbc.md)

If you are connecting to relational databases using the JDBC API and encounter self-signed certificate (SSL/TLS) requirements, you can disable encryption by modifying the YAML configuration file. Simply provide the necessary details for the subprotocol, host, port, database, and use the params field to specify the appropriate parameters for your specific source system as shown below:

```yaml
spec:
    subprotocol:
    host: 
    port: 
    database:
    params:
#use params for JDBC type connections where self-signed certificates have been enabled
```

The particular specifications to be filled within *params* depend on the source system. We have listed these in the templates below:

[MySQL](./depot_config_templates/mysql.md)

[Microsoft SQL Server](./depot_config_templates/microsoft_sql_server.md)

[PostgreSQL](./depot_config_templates/postgresql.md)

Apart from the above sources, any source that supports a JDBC connection, can be connected to DataOS. This includes MariaDB, IBM Db2, etc.