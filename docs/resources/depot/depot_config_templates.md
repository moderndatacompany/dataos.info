# Depot Configuration Templates

To make the process of creating a Depot configuration easier, we provide a set of predefined templates for various data sources. These templates serve as a starting point for configuring your Depot based on the specific data source you are working with. Simply choose the template that corresponds to your organization's data source and follow the instructions provided to fill in the required information.

<aside class=callout>

🗣️ When using these templates, you will need to populate the key-value properties in the YAML config file with the appropriate values for your data source. This requires a basic understanding of your organization's data infrastructure and the necessary credentials or connection details.

</aside>

The available Depot configuration Templates are provided in the table below:

<center>

| **Data Source Template**                                              | **Category**           |
| --------------------------------------------------------- | ------------------ |
| [Amazon Redshift](./depot_config_templates/amazon_redshift.md)       | Data Warehouse     |
| [Google BigQuery](./depot_config_templates/google_bigquery.md)       | Data Warehouse     |
| [Snowflake](./depot_config_templates/snowflake.md)                 | Data Warehouse     |
| [Amazon Simple Storage Service (S3)](./depot_config_templates/amazon_s3.md)       | Data Lake          |
| [Azure Blob File System Storage (ABFSS)](./depot_config_templates/azure_abfss.md) | Data Lake          |
| [Windows Azure Storage Blob Service (WASBS)](./depot_config_templates/azure_wasbs.md) | Data Lake          |
| [Google Cloud Storage (GCS)](./depot_config_templates/google_gcs.md)           | Data Lake          |
| [Apache Pulsar](./depot_config_templates/apache_pulsar.md)              | Streaming Source   |
| [Eventhub](./depot_config_templates/eventhub.md)                       | Streaming Source   |
| [Apache Kafka](./depot_config_templates/kafka.md)                       | Streaming Source   |
| [Elasticsearch](./depot_config_templates/elasticsearch.md)          | NoSQL Database     |
| [MongoDB](./depot_config_templates/mongodb.md)                     | NoSQL Database     |
| [Opensearch](./depot_config_templates/opensearch.md)               | NoSQL Database     |
| [Oracle](./depot_config_templates/oracle.md)                     | Relational Database |
| [JDBC](./depot_config_templates/jdbc.md)                         | Relational Database |
| [MySQL](./depot_config_templates/mysql.md)                       | Relational Database |
| [Microsoft SQL Server](./depot_config_templates/microsoft_sql_server.md) | Relational Database |
| [PostgreSQL](./depot_config_templates/postgresql.md)             | Relational Database |

</center>

Apart from the above sources, any source that supports a JDBC connection, can be connected to DataOS. This includes MariaDB, IBM Db2, etc.

