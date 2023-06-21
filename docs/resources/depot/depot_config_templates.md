# Depot Config Templates


Instead of just staring at the overwhelmingly long list with blank eyes, why not be productive and try one out? You have already learned the details on the [Create Depot](./create_depot.md) page, so pick one, anyone, and take it for a spin.

The data source you pick must be the one your organisation is using, how else will you fill-up the key-value properties in the YAML config file? A little common sense would not go amiss!

[Amazon Redshift](./depot_config_templates/amazon_redshift.md)

[Amazon S3](./depot_config_templates/amazon_s3.md)

[Apache Pulsar](./depot_config_templates/apache_pulsar.md)

[Azure Blob Storage](./depot_config_templates/azure_blob_storage.md)

[Azure Data Lake Storage Gen2](./depot_config_templates/azure_data_lake_storage_gen2.md)

[Google BigQuery](./depot_config_templates/google_bigquery.md)

[Elasticsearch](./depot_config_templates/elasticsearch.md)

[File](./depot_config_templates/file.md)

[JDBC](./depot_config_templates/jdbc.md)

[Kafka](./depot_config_templates/kafka.md)

[Oracle](./depot_config_templates/oracle.md)

[Presto](./depot_config_templates/presto.md)

[Redis](./depot_config_templates/redis.md)

[Snowflake](./depot_config_templates/snowflake.md)

When connecting to relational databases, such as postgreSQL, msSQL, mySQL, through JDBC API, you might find that the storage systems are using a self-signed certificate(SSL/TLS). In such cases, all you need to do is disable the requirement for encryption while creating the depot. In the YAML configuration file, you can achieve this as follows:

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
