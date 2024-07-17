# Depot Configuration Templates

To make the process of creating a Depot configuration easier, we provide a set of predefined templates for various data sources. These templates serve as a starting point for configuring your Depot based on the specific data source you are working with. Simply choose the template that corresponds to your organization's data source and follow the instructions provided to fill in the required information.

<aside class=callout>

🗣️ When using these templates, you will need to populate the key-value properties in the YAML config file with the appropriate values for your data source. This requires a basic understanding of your organization's data infrastructure and the necessary credentials or connection details.

</aside>

The available Depot configuration Templates are provided in the table below:

<center>

| **Data Source Template**                                              | **Category**           |
| --------------------------------------------------------- | ------------------ |
| [Amazon Redshift](/resources/depot/depot_config_templates/amazon_redshift)       | Data Warehouse     |
| [Google BigQuery](/resources/depot/depot_config_templates/google_bigquery)       | Data Warehouse     |
| [Snowflake](/resources/depot/depot_config_templates/snowflake)                 | Data Warehouse     |
| [Amazon Simple Storage Service (S3)](/resources/depot/depot_config_templates/amazon_s3)       | Lakehouse or Data Lake          |
| [Azure Blob File System Storage (ABFSS)](/resources/depot/depot_config_templates/azure_abfss) | Lakehouse or Data Lake          |
| [Windows Azure Storage Blob Service (WASBS)](/resources/depot/depot_config_templates/azure_wasbs) | Lakehouse or Data Lake          |
| [Google Cloud Storage (GCS)](/resources/depot/depot_config_templates/google_gcs)           | Lakehouse or Data Lake          |
| [Icebase](/resources/depot/depot_config_templates/icebase_hadoop_s3)       | Lakehouse or Data Lake          |
| [Apache Pulsar](/resources/depot/depot_config_templates/apache_pulsar)              | Streaming Source   |
| [Eventhub](/resources/depot/depot_config_templates/eventhub)                       | Streaming Source   |
| [Apache Kafka](/resources/depot/depot_config_templates/kafka)                       | Streaming Source   |
| [Elasticsearch](/resources/depot/depot_config_templates/elasticsearch)          | NoSQL Database     |
| [MongoDB](/resources/depot/depot_config_templates/mongodb)                     | NoSQL Database     |
| [Opensearch](/resources/depot/depot_config_templates/opensearch)               | NoSQL Database     |
| [JDBC](/resources/depot/depot_config_templates/jdbc)                         | Relational Database |
| [MySQL](/resources/depot/depot_config_templates/mysql)                       | Relational Database |
| [Microsoft SQL Server](/resources/depot/depot_config_templates/microsoft_sql_server) | Relational Database |
| [Oracle](/resources/depot/depot_config_templates/oracle)                     | Relational Database |
| [PostgreSQL](/resources/depot/depot_config_templates/postgresql)             | Relational Database |

</center>

Apart from the above sources, any source that supports a JDBC connection, can be connected to DataOS. This includes MariaDB, IBM Db2, etc.

