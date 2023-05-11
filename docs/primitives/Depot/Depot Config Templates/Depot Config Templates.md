# Depot Config Templates

Instead of just staring at the overwhelmingly long list with blank eyes, why not be productive and try one out? You have already learned the details on the [Create Depot](./Create%20Depot.md) page, so pick one, anyone, and take it for a spin.

The data source you pick must be the one your organisation is using, how else will you fill-up the key-value properties in the YAML config file? A little common sense would not go amiss!

- [Amazon Redshift](./Depot%20Config%20Templates/Amazon%20Redshift.md)

- [Amazon S3](./Depot%20Config%20Templates/Amazon%20S3.md)

- [Apache Pulsar](./Depot%20Config%20Templates/Apache%20Pulsar.md)

- [Azure Blob Storage](./Depot%20Config%20Templates/Azure%20Blob%20Storage.md)

- [Azure Data Lake Storage Gen2](./Depot%20Config%20Templates/Azure%20Data%20Lake%20Storage%20Gen2.md)

- [BigQuery](./Depot%20Config%20Templates/BigQuery.md)

- [Elasticsearch](./Depot%20Config%20Templates/Elasticsearch.md)

- [File](./Depot%20Config%20Templates/File.md)

- [JDBC](./Depot%20Config%20Templates/JDBC.md)

- [Kafka](./Depot%20Config%20Templates/Kafka.md)

- [Oracle](./Depot%20Config%20Templates/Oracle.md)

- [Presto](./Depot%20Config%20Templates/Presto.md)

- [Redis](./Depot%20Config%20Templates/Redis.md)

- [Snowflake](./Depot%20Config%20Templates/Snowflake.md)

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

- [MySQL](./Depot%20Config%20Templates/MySQL.md)

- [Microsoft SQL Server](./Depot%20Config%20Templates/Microsoft%20SQL%20Server.md)

- [PostgreSQL](./Depot%20Config%20Templates/PostgreSQL.md)