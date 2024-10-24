---
search:
  boost: 2
tags:
  - Supported Connectors
  - DataOS Connectors
hide:
  - tags
---

# DataOS Supported Connectors

This document provides an overview of the data sources supported by DataOS. It is designed to help users understand which data sources are supported by each component, enabling effective planning of data integration and processing workflows.

## Integration with DataOS Components

The connector support table lists various data sources and their compatibility with key DataOS components. Use this table to understand the capabilities of each component in relation to specific data sources.

- :white_check_mark: **Supported:** The data source is compatible with the DataOS component.
- :white_large_square: **Not Supported:** The data source is not compatible with the component.

**Table Legend**

- **Data Source:** The name of the database, data warehouse, data lake, messaging system, or other data source.
- **Type:** The category of the data source (e.g., Database, Data Warehouse, Messaging System).
- **Depot:** Indicates whether DataOS can connect to this source using the [Depot Resource](/resources/depot/).
- **Minerva:** Specifies if this data source can be queried directly using [Minerva Cluster](/resources/cluster/#minerva). Minerva is DataOS' high-performance, static federation engine, designed for executing queries in specific scenarios that require fail-fast architecture and faster performance. Minerva can query data from sources via two mechanisms: through Depots (for sources connected via the Depot Interface) or via catalogs (for sources where Depots cannot be created but can still be queried). For exploring Depot support for a particular source, contact our teams to discuss potential solutions.
- **Predicate Pushdown Support (Minerva):** Indicates whether Minerva can optimize queries by pushing filters and predicates directly to the data source, reducing data transfer and improving performance.
- **Themis:** Indicates whether the source can be queried using [Themis](/resources/cluster/#themis), DataOS' dynamic federation engine that supports SparkSQL. Themis auto-scales per query, and user-based scaling boundaries can be defined. It is designed to complete queries reliably in failure-prone scenarios but is generally slower than Minerva, making it less suited for real-time analysis.
- **Flare:** Determines if ETL operations with this data source can be performed using [Flare Stack](/resources/stacks/flare/), which is built on Apache Spark for large-scale data processing.
- **Scanner:** Indicates whether [Scanner](/resources/stacks/scanner/) can extract metadata from this source. Scanner is a DataOS Stack designed for metadata extraction from various systems.


## Supported Connectors

| Data Source                                          | Type                             | Depot <br> (connect) | Minerva <br> (query) | Predicate Pushdown <br> Support (Minerva) | Themis <br> (query) | Flare <br> (extract, transform, load) | Scanner <br> (metadata scan) | 
|------------------------------------------------------|----------------------------------|----------------------|-----------------------|--------------------------------------------|----------------------|---------------------------------------|-------------------------------|
| **ElasticSearch**                                    | Database                         | :white_check_mark:   | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_large_square:          |
| **DataOS Lakehouse (Iceberg Format)**                         | Data Warehouse & Data Lake                         | :white_check_mark:   | :white_check_mark:    | :white_large_square:                       | :white_check_mark:   | :white_check_mark:                    | :white_check_mark:            |
| **MySQL**                                            | Database                         | :white_check_mark:   | :white_check_mark:    | :white_check_mark:                         | :white_check_mark:   | :white_check_mark:                    | :white_check_mark:            |
| **Microsoft SQL Server**                             | Database                         | :white_check_mark:   | :white_check_mark:    | :white_check_mark:                         | :white_large_square: | :white_check_mark:                    | :white_check_mark:            |
| **MongoDB**                                          | Database                         | :white_check_mark:   | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_large_square:          |
| **Oracle**                                           | Database                         | :white_check_mark:   | :white_check_mark:    | :white_check_mark:                         | :white_large_square: | :white_check_mark:                    | :white_check_mark:            |
| **PostgreSQL**                                       | Database                         | :white_check_mark:   | :white_check_mark:    | :white_large_square:                       | :white_check_mark:   | :white_check_mark:                    | :white_check_mark:            |
| **EventHub**                                         | Messaging & Streaming Datastore  | :white_check_mark:   | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_large_square:          |
| **Fastbase (Pulsar)**                                | Messaging & Streaming Datastore  | :white_check_mark:   | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_check_mark:            |
| **Kafka**                                            | Messaging & Streaming Datastore  | :white_check_mark:   | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_check_mark:            |
| **AWS Redshift**                                     | Data Warehouse & Data Lake       | :white_check_mark:   | :white_check_mark:    | :white_large_square:                       | :white_check_mark:   | :white_check_mark:                    | :white_check_mark:            |
| **AWS S3 Blob Storage**                              | Data Warehouse & Data Lake       | :white_check_mark:   | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_large_square:          |
| **Azure Data Lake Gen2 (ABFSS)**                     | Data Warehouse & Data Lake       | :white_check_mark:   | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_large_square:          |
| **Azure Blob Storage (WASBS)**                       | Data Warehouse & Data Lake       | :white_check_mark:   | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_large_square:          |
| **BigQuery**                                         | Data Warehouse & Data Lake       | :white_check_mark:   | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_check_mark:            |
| **Google Cloud Storage (GCS)**                       | Data Warehouse & Data Lake       | :white_check_mark:   | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_large_square:          |
| **Snowflake**                                        | Data Warehouse & Data Lake       | :white_check_mark:   | :white_large_square:  | :white_large_square:                       | :white_check_mark:   | :white_check_mark:                    | :white_check_mark:            |
| **JDBC Sources**<br>(e.g., SAP HANA, IBM Db2)        | Miscellaneous                    | :white_check_mark:   | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_check_mark:            |
| **OpenSearch**                                       | Miscellaneous                    | :white_check_mark:   | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_check_mark:                    | :white_large_square:          |
| **Accumulo**                                         | Database                         | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **Cassandra**                                        | Database                         | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **ClickHouse**                                       | Database                         | :white_large_square: | :white_check_mark:    | :white_check_mark:                         | :white_large_square: | :white_large_square:                 | :white_check_mark:            |
| **IBM Db2**                                          | Database                         | :white_large_square: | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_check_mark:            |
| **DOMO Database**                                    | Database                         | :white_large_square: | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_check_mark:            |
| **Apache Ignite**                                    | Database (In-Memory Computing)   | :white_large_square: | :white_check_mark:    | :white_check_mark:                         | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **Apache Kudu**                                      | Database                         | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **Apache Phoenix**                                   | Database                         | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **Apache Pinot**                                     | Database                         | :white_large_square: | :white_check_mark:    | :white_check_mark:                         | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **Prometheus**                                       | Time-Series Database             | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **SingleStore**                                      | Database                         | :white_large_square: | :white_check_mark:    | :white_check_mark:                         | :white_large_square: | :white_large_square:                 | :white_check_mark:            |
| **Azure Databricks**                                 | Data Warehouse & Data Lake       | :white_large_square: | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_check_mark:            |
| **Apache Hive**                                      | Data Warehouse & Data Lake       | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_check_mark:            |
| **Apache Hudi**                                      | Data Lake                        | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **MariaDB**                                          | Database                         | :white_large_square: | :white_check_mark:    | :white_check_mark:                         | :white_large_square: | :white_large_square:                 | :white_check_mark:            |
| **Delta Lake**                                       | Data Lakehouse                   | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **Atop**                                             | Performance Analysis Tool        | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **AWS Glue**                                         | Data Integration Service         | :white_large_square: | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_check_mark:            |
| **AWS Athena**                                       | Interactive Analytics Service    | :white_large_square: | :white_large_square:  | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_check_mark:            |
| **Apache Druid**                                     | Real-time Analytics Database     | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_check_mark:            |
| **Google Sheets**                                    | Spreadsheet                      | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **JMX**                                              | Monitoring Tool                  | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **Amazon Kinesis**                                   | Streaming Platform               | :white_large_square: | :white_check_mark:    | :white_large_square:                       | :white_large_square: | :white_large_square:                 | :white_large_square:          |
| **Redis**                                            | In-Memory Data Store             | :white_large_square: | :white_check_mark:    | :white_check_mark:                         | :white_large_square: | :white_large_square:                 | :white_large_square:          |


## Integration with Third-Party Tools

DataOS extends its connectivity through integration with third-party tools, broadening the range of supported data sources.

### **Airbyte Connectors**

DataOS integrates with Airbyte, allowing you to connect to over 300 additional data sources, including various SaaS applications and databases.

???info "Airbyte Supported Sources"

    <center>

    | Sno. | Connector Name               | Type                    | Sources | Destinations |
    |------|------------------------------|-------------------------|---------|--------------|
    | 1    | AlloyDB for Postgre SQL       | Databases               | Yes     |              |
    | 2    | Apache Doris                  | Databases               |         | Yes          |
    | 3    | Apache Iceberg                | Databases               |         | Yes          |
    | 4    | Apache Kafka                  | Databases               | Yes     |              |
    | 5    | Click House                   | Databases               | Yes     | Yes          |
    | 6    | CockroachDB                   | Databases               | Yes     |              |
    | 7    | Convex.dev                    | Databases               | Yes     |              |
    | 8    | DuckDB                        | Databases               |         | Yes          |
    | 9    | DynamoDB                      | Databases               | Yes     | Yes          |
    | 10   | Elasticsearch                 | Databases               | Yes     | Yes          |
    | 11   | Fauna                         | Databases               | Yes     |              |
    | 12   | Firebase                      | Databases               | Yes     |              |
    | 13   | Google Pubsub                 | Databases               |         | Yes          |
    | 14   | IBM Db2                       | Databases               | Yes     |              |
    | 15   | Kafka                         | Databases               |         | Yes          |
    | 16   | MSSQL SQL Server              | Databases               | Yes     | Yes          |
    | 17   | MySQL                         | Databases               | Yes     | Yes          |
    | 18   | MongoDB                       | Databases               | Yes     | Yes          |
    | 19   | Microsoft Dataverse           | Databases               | Yes     |              |
    | 20   | Oracle DB                     | Databases               | Yes     | Yes          |
    | 21   | Postgre SQL                   | Databases               | Yes     | Yes          |
    | 22   | Pulsar                        | Databases               | Yes     | Yes          |
    | 23   | TiDB                          | Databases               | Yes     |              |
    | 24   | Yugabytedb                    | Databases               |         | Yes          |
    | 25   | S3                             | Warehouses and Lakes    | Yes     | Yes          |
    | 26   | BigQuery                      | Warehouses and Lakes    | Yes     | Yes          |
    | 27   | MariaDB Columnstore           | Warehouses and Lakes    |         | Yes          |
    | 28   | Firebolt                      | Warehouses and Lakes    | Yes     |              |
    | 29   | Azure Blob Storage            | Warehouses and Lakes    |         | Yes          |
    | 30   | Azure Table Storage           | Warehouses and Lakes    | Yes     |              |
    | 31   | S3 Glue                       | Warehouses and Lakes    |         | Yes          |
    | 32   | Redshift                      | Warehouses and Lakes    | Yes     | Yes          |
    | 33   | Google Cloud Storage          | Warehouses and Lakes    |         | Yes          |
    | 34   | Snowflake Data Cloud          | Warehouses and Lakes    | Yes     | Yes          |
    | 35   | Teradata                      | Warehouses and Lakes    |         | Yes          |
    | 36   | Databricks Lakehouse          | Warehouses and Lakes    |         | Yes          |
    | 37   | AWS                           | Warehouses and Lakes    |         | Yes          |
    | 38   | AWS Cloud Trail               | Engineering Analytics   | Yes     |              |
    | 39   | Amazon SQS                    | Engineering Analytics   | Yes     |              |
    | 40   | Auth0                         | Engineering Analytics   | Yes     |              |
    | 41   | Ashby                         | Engineering Analytics   | Yes     |              |
    | 42   | Convex                        | Engineering Analytics   | Yes     |              |
    | 43   | Courier                       | Engineering Analytics   | Yes     |              |
    | 44   | Datadog                       | Engineering Analytics   | Yes     |              |
    | 45   | Dockerhub                     | Engineering Analytics   | Yes     |              |
    | 46   | E2E Testing                   | Engineering Analytics   | Yes     |              |
    | 47   | GitLab                        | Engineering Analytics   | Yes     |              |
    | 48   | Harness                       | Engineering Analytics   | Yes     |              |
    | 49   | Intruder                      | Engineering Analytics   | Yes     |              |
    | 50   | K6 Cloud                      | Engineering Analytics   | Yes     |              |
    | 51   | PagerDuty                     | Engineering Analytics   | Yes     |              |
    | 52   | Jira                          | Engineering Analytics   | Yes     |              |
    | 53   | Jenkins                       | Engineering Analytics   | Yes     |              |
    | 54   | MeiliSearch                   | Engineering Analytics   |         | Yes          |
    | 55   | PyPI                          | Engineering Analytics   | Yes     |              |
    | 56   | Rest Api                      | Engineering Analytics   | Yes     |              |
    | 57   | Sentry                        | Engineering Analytics   | Yes     |              |
    | 58   | SonarCloud                    | Engineering Analytics   | Yes     |              |
    | 59   | Statuspage                    | Engineering Analytics   | Yes     |              |
    | 60   | Statuspage.io                 | Engineering Analytics   | Yes     |              |
    | 61   | Streamr                       | Engineering Analytics   |         | Yes          |
    | 62   | Typesense                     | Engineering Analytics   |         | Yes          |
    | 63   | Vantage                       | Engineering Analytics   | Yes     |              |
    | 64   | VictorOps                     | Engineering Analytics   | Yes     |              |
    | 65   | App follow                    | Product Analytics       | Yes     |              |
    | 66   | Adjust                        | Product Analytics       | Yes     |              |
    | 67   | Aha                           | Product Analytics       | Yes     |              |
    | 68   | Amplitude                     | Product Analytics       | Yes     |              |
    | 69   | Chartmogul                    | Product Analytics       | Yes     |              |
    | 70   | Config Cat                    | Product Analytics       | Yes     |              |
    | 71   | Keen                          | Product Analytics       |         | Yes          |
    | 72   | Launch Darkly                 | Product Analytics       | Yes     |              |
    | 73   | Looker                        | Product Analytics       | Yes     |              |
    | 74   | Mixpanel                      | Product Analytics       | Yes     |              |
    | 75   | Metabase                      | Product Analytics       | Yes     |              |
    | 76   | Plausible                     | Product Analytics       | Yes     |              |
    | 77   | Posthog                       | Product Analytics       | Yes     |              |
    | 78   | Microsoft Dynamics NAV        | Product Analytics       | Yes     |              |
    | 79   | Facebook Marketing            | Marketing Analytics     | Yes     |              |
    | 80   | Facebook Pages                | Marketing Analytics     | Yes     |              |
    | 81   | Google Ads                    | Marketing Analytics     | Yes     |              |
    | 82   | Google Analytics              | Marketing Analytics     | Yes     |              |
    | 83   | Google Search Console         | Marketing Analytics     | Yes     |              |
    | 84   | Instagram                     | Marketing Analytics     | Yes     |              |
    | 85   | Webflow                       | Marketing Analytics     | Yes     |              |
    | 86   | Active Campaign               | Marketing Analytics     | Yes     |              |
    | 87   | Amazon Ads                    | Marketing Analytics     | Yes     |              |
    | 88   | Bing Ads                      | Marketing Analytics     | Yes     |              |
    | 89   | Braze                         | Marketing Analytics     | Yes     |              |
    | 90   | Cart                          | Marketing Analytics     | Yes     |              |
    | 91   | Emarsys                       | Marketing Analytics     | Yes     |              |
    | 92   | Formidable Forms              | Marketing Analytics     | Yes     |              |
    | 93   | Heap                          | Marketing Analytics     | Yes     |              |
    | 94   | HubSpot                       | Marketing Analytics     | Yes     |              |
    | 95   | HubSpot CRM                   | Marketing Analytics     | Yes     |              |
    | 96   | HubSpot Marketing             | Marketing Analytics     | Yes     |              |
    | 97   | Iterable                      | Marketing Analytics     | Yes     |              |
    | 98   | Klaviyo                       | Marketing Analytics     | Yes     |              |
    | 99   | LinkedIn Pages                | Marketing Analytics     | Yes     |              |
    | 100  | LinkedIn                      | Marketing Analytics     | Yes     |              |
    | 101  | Mailchimp                     | Marketing Analytics     | Yes     |              |
    | 102  | Marketo                       | Marketing Analytics     | Yes     |              |
    | 103  | Microsoft Advertising         | Marketing Analytics     | Yes     |              |
    | 104  | Microsoft Dynamics 365        | Marketing Analytics     | Yes     |              |
    | 105  | Twitter Ads                   | Marketing Analytics     | Yes     |              |
    | 106  | LinkedIn Ads                  | Marketing Analytics     | Yes     |              |
    | 107  | Lokalise                      | Marketing Analytics     | Yes     |              |
    | 108  | Mailchimp                     | Marketing Analytics     | Yes     |              |
    | 109  | Mailgun                       | Marketing Analytics     | Yes     |              |
    | 110  | Mailjet Email                 | Marketing Analytics     | Yes     |              |
    | 111  | Mailjet SMS                   | Marketing Analytics     | Yes     |              |
    | 112  | Marketo                       | Marketing Analytics     | Yes     |              |
    | 113  | N8n                           | Marketing Analytics     | Yes     |              |
    | 114  | Omnisend                      | Marketing Analytics     | Yes     |              |
    | 115  | OneSignal                     | Marketing Analytics     | Yes     |              |
    | 116  | Orbit.love                    | Marketing Analytics     | Yes     |              |
    | 117  | PartnerStack                  | Marketing Analytics     | Yes     |              |
    | 118  | Pinterest Ads                 | Marketing Analytics     | Yes     |              |
    | 119  | Postmark App                  | Marketing Analytics     | Yes     |              |
    | 120  | Qualaroo                     | Marketing Analytics      | Yes     |              |
    | 121  | RD Station Marketing          | Marketing Analytics      | Yes     |              |
    | 122  | SendGrid                      | Marketing Analytics      | Yes     |              |
    | 123  | Sendinblue                    | Marketing Analytics      | Yes     |              |
    | 124  | Short.io                      | Marketing Analytics      | Yes     |              |
    | 125  | Smaily                        | Marketing Analytics      | Yes     |              |
    | 126  | SmartEngage                   | Marketing Analytics      | Yes     |              |
    | 127  | Snapchat Marketing            | Marketing Analytics      | Yes     |              |
    | 128  | SurveyMonkey                  | Marketing Analytics      | Yes     |              |
    | 129  | SurveySparrow                 | Marketing Analytics      | Yes     |              |
    | 130  | TikTok for Business Marketing | Marketing Analytics      | Yes     |              |
    | 131  | Twilio                        | Marketing Analytics      | Yes     |              |
    | 132  | Twitter                       | Marketing Analytics      | Yes     |              |
    | 133  | Tyntec SMS                    | Marketing Analytics      | Yes     |              |
    | 134  | Typeform                      | Marketing Analytics      | Yes     |              |
    | 135  | Whisky Hunter                 | Marketing Analytics      | Yes     |              |
    | 136  | Wordpress                     | Marketing Analytics      | Yes     |              |
    | 137  | Yandex Metrica                | Marketing Analytics      | Yes     |              |
    | 138  | YouTube Analytics             | Marketing Analytics      | Yes     |              |
    | 139  | Zapier Supported Storage      | Marketing Analytics      | Yes     |              |
    | 140  | App Store                     | Finance & Ops Analytics  | Yes     |              |
    | 141  | Asana                         | Finance & Ops Analytics  | Yes     |              |
    | 142  | Alpha Vantage                 | Finance & Ops Analytics  | Yes     |              |
    | 143  | Airtable                      | Finance & Ops Analytics  | Yes     |              |
    | 144  | Amazon Seller Partner         | Finance & Ops Analytics  | Yes     |              |
    | 145  | BambooHR                      | Finance & Ops Analytics  | Yes     |              |
    | 146  | Big Commerce                  | Finance & Ops Analytics  | Yes     |              |
    | 147  | Braintree                     | Finance & Ops Analytics  | Yes     |              |
    | 148  | Chargebee                     | Finance & Ops Analytics  | Yes     |              |
    | 149  | Chargify                     | Finance & Ops Analytics   |         | Yes          |
    | 150  | ClickUp                      | Finance & Ops Analytics   | Yes     |              |
    | 151  | Clockify                     | Finance & Ops Analytics   | Yes     |              |
    | 152  | Coin API                     | Finance & Ops Analytics   | Yes     |              |
    | 153  | Coin Gecko Coins             | Finance & Ops Analytics   | Yes     |              |
    | 154  | CoinMarketCap                | Finance & Ops Analytics   | Yes     |              |
    | 155  | Exchange Rates API           | Finance & Ops Analytics   | Yes     |              |
    | 156  | Fastbill                     | Finance & Ops Analytics   | Yes     |              |
    | 157  | Confluence                   | Finance & Ops Analytics   | Yes     |              |
    | 158  | Commerce tools               | Finance & Ops Analytics   | Yes     |              |
    | 159  | Flexport                     | Finance & Ops Analytics   | Yes     |              |
    | 160  | GetLago                      | Finance & Ops Analytics   | Yes     |              |
    | 161  | Glassfrog                    | Finance & Ops Analytics   | Yes     |              |
    | 162  | GoCardless                   | Finance & Ops Analytics   | Yes     |              |
    | 163  | Greenhouse                   | Finance & Ops Analytics   | Yes     |              |
    | 164  | Gutendex                     | Finance & Ops Analytics   | Yes     |              |
    | 165  | Google Directory             | Finance & Ops Analytics   | Yes     |              |
    | 166  | Harvest                      | Finance & Ops Analytics   | Yes     |              |
    | 167  | Hubplanner                   | Finance & Ops Analytics   | Yes     |              |
    | 168  | Klarna                       | Finance & Ops Analytics   | Yes     |              |
    | 169  | Lever Hiring                 | Finance & Ops Analytics   | Yes     |              |
    | 170  | Kyriba                      | Finance & Ops Analytics    | Yes     |              |
    | 171  | Linnworks                   | Finance & Ops Analytics    | Yes     |              |
    | 172  | Notion                      | Finance & Ops Analytics    | Yes     |              |
    | 173  | Okta                        | Finance & Ops Analytics    | Yes     |              |
    | 174  | Google Workspace Admin Reports | Finance & Ops Analytics | Yes     |              |
    | 175  | Microsoft Dynamics AX        | Finance & Ops Analytics   | Yes     |              |
    | 176  | Microsoft Teams              | Finance & Ops Analytics   | Yes     |              |
    | 177  | Microsoft Dynamics GP        | Finance & Ops Analytics   | Yes     |              |
    | 178  | My Hours                    | Finance & Ops Analytics    | Yes     |              |
    | 179  | Netsuite                    | Finance & Ops Analytics    | Yes     |              |
    | 180  | Oracle PeopleSoft           | Finance & Ops Analytics    | Yes     |              |
    | 181  | Orb                         | Finance & Ops Analytics    | Yes     |              |
    | 182  | Pagar.me                    | Finance & Ops Analytics    | Yes     |              |
    | 183  | PayPal Transaction          | Finance & Ops Analytics    | Yes     |              |
    | 184  | Plaid                       | Finance & Ops Analytics    | Yes     |              |
    | 185  | PrestaShop                  | Finance & Ops Analytics    | Yes     |              |
    | 186  | Primetric                  | Finance & Ops Analytics     | Yes     |              |
    | 187  | QuickBooks                 | Finance & Ops Analytics     | Yes     |              |
    | 188  | Railz                      | Finance & Ops Analytics     | Yes     |              |
    | 189  | Recharge                   | Finance & Ops Analytics     | Yes     |              |
    | 190  | Recruitee                  | Finance & Ops Analytics     | Yes     |              |
    | 191  | Recurly                    | Finance & Ops Analytics     | Yes     |              |
    | 192  | Rocket.chat                | Finance & Ops Analytics     | Yes     |              |
    | 193  | SAP Business One           | Finance & Ops Analytics     | Yes     |              |
    | 194  | SAP Fieldglass             | Finance & Ops Analytics     | Yes     |              |
    | 195  | Shopify                    | Finance & Ops Analytics     | Yes     |              |
    | 196  | Slack                      | Finance & Ops Analytics     | Yes     |              |
    | 197  | Spree Commerce             | Finance & Ops Analytics     | Yes     |              |
    | 198  | Square                     | Finance & Ops Analytics     | Yes     |              |
    | 199  | Stripe                     | Finance & Ops Analytics     | Yes     |              |
    | 200  | Tempo                      | Finance & Ops Analytics     | Yes     |              |
    | 201  | Timely                     | Finance & Ops Analytics     | Yes     |              |
    | 202  | Toggl                      | Finance & Ops Analytics     | Yes     |              |
    | 203  | Trello                     | Finance & Ops Analytics     | Yes     |              |
    | 204  | Visma E-conomic            | Finance & Ops Analytics     | Yes     |              |
    | 205  | WooCommerce                | Finance & Ops Analytics     | Yes     |              |
    | 206  | Workramp                   | Finance & Ops Analytics     | Yes     |              |
    | 207  | Wrike                      | Finance & Ops Analytics     | Yes     |              |
    | 208  | Younium                    | Finance & Ops Analytics     | Yes     |              |
    | 209  | Zenefits                   | Finance & Ops Analytics     | Yes     |              |
    | 210  | Zencart                    | Finance & Ops Analytics     | Yes     |              |
    | 211  | Zoom                       | Finance & Ops Analytics     | Yes     |              |
    | 212  | Zuora                      | Finance & Ops Analytics     | Yes     |              |
    | 213  | Salesforce                 | Sales & Support Analytics   | Yes     |              |
    | 214  | Close.com                  | Sales & Support Analytics   | Yes     |              |
    | 215  | Coda                       | Sales & Support Analytics   | Yes     |              |
    | 216  | Delighted                  | Sales & Support Analytics   | Yes     |              |
    | 217  | Dixa                       | Sales & Support Analytics   | Yes     |              |
    | 218  | Drift                      | Sales & Support Analytics   | Yes     |              |
    | 219  | Freshcaller                | Sales & Support Analytics   | Yes     |              |
    | 220  | Freshdesk                  | Sales & Support Analytics   | Yes     |              |
    | 221  | Freshsales                | Sales & Support Analytics    | Yes     |              |
    | 222  | Intercom                  | Sales & Support Analytics    | Yes     |              |
    | 223  | Kustomer                  | Sales & Support Analytics    | Yes     |              |
    | 224  | Oracle Siebel CRM         | Sales & Support Analytics    | Yes     |              |
    | 225  | Outreach                 | Sales & Support Analytics     | Yes     |              |
    | 226  | PersistIq                | Sales & Support Analytics     | Yes     |              |
    | 227  | Pipedrive                | Sales & Support Analytics     | Yes     |              |
    | 228  | Reply.io                 | Sales & Support Analytics     | Yes     |              |
    | 229  | Retently                | Sales & Support Analytics      | Yes     |              |
    | 230  | SalesLoft               | Sales & Support Analytics      | Yes     |              |
    | 231  | Sugar CRM               | Sales & Support Analytics      | Yes     |              |
    | 232  | TalkDesk Explore        | Sales & Support Analytics      | Yes     |              |
    | 233  | Vitally                 | Sales & Support Analytics      | Yes     |              |
    | 234  | Zendesk Chat            | Sales & Support Analytics      | Yes     |              |
    | 235  | Zendesk Sell            | Sales & Support Analytics      | Yes     |              |
    | 236  | Zendesk Sunshine        | Sales & Support Analytics      | Yes     |              |
    | 237  | Zendesk Support         | Sales & Support Analytics      | Yes     |              |
    | 238  | Zendesk Talk            | Sales & Support Analytics      | Yes     |              |
    | 239  | Zenloop                | Sales & Support Analytics       | Yes     |              |
    | 240  | Zoho CRM               | Sales & Support Analytics       | Yes     |              |
    | 241  | Microsoft Dynamics Customer Engagement | Sales & Support Analytics | Yes  |              |
    | 242  | Google Sheets           | Files                     | Yes     | Yes          |
    | 243  | CSV                      | Files                     | Yes     | Yes          |
    | 244  | Excel                    | Files                     | Yes     |              |
    | 245  | Feather                  | Files                     | Yes     |              |
    | 246  | JSON File                | Files                     | Yes     | Yes          |
    | 247  | SFTP                     | Files                     | Yes     |              |
    | 248  | Parquet File             | Files                     | Yes     |              |
    | 249  | Smartsheets              | Files                     | Yes     |              |
    | 250  | Apify                    | Others                    | Yes     |              |
    | 251  | Breezometer              | Others                    | Yes     |              |
    | 252  | Faker                    | Others                    | Yes     |              |
    | 253  | NASA                     | Others                    | Yes     |              |
    | 254  | New York Times           | Others                    | Yes     |              |
    | 255  | News API                 | Others                    | Yes     |              |
    | 256  | IP2Whois                 | Others                    | Yes     |              |
    | 257  | Google Webfonts          | Others                    | Yes     |              |
    | 258  | Newsdata                 | Others                    | Yes     |              |
    | 259  | OpenWeather              | Others                    | Yes     |              |
    | 260  | Oura                     | Others                    | Yes     |              |
    | 261  | Pexels API               | Others                    | Yes     |              |
    | 262  | Pocket                   | Others                    | Yes     |              |
    | 263  | PokéAPI                  | Others                    | Yes     |              |
    | 264  | Polygon                  | Others                    | Yes     |              |
    | 265  | Public API               | Others                    | Yes     |              |
    | 266  | Punk API                 | Others                    | Yes     |              |
    | 267  | REST Countries           | Others                    | Yes     |              |
    | 268  | RKI Covid                | Others                    | Yes     |              |
    | 269  | RSS                      | Others                    | Yes     |              |
    | 270  | Recreation.gov           | Others                    | Yes     |              |
    | 271  | SFTP Bulk                | Others                    | Yes     |              |
    | 272  | SearchMetrics            | Others                    | Yes     |              |
    | 273  | Secoda                   | Others                    | Yes     |              |
    | 274  | Senseforce               | Others                    | Yes     |              |
    | 275  | SpaceX API               | Others                    | Yes     |              |
    | 276  | Strava                   | Others                    | Yes     |              |
    | 277  | TMDb                     | Others                    | Yes     |              |
    | 278  | TVMaze Schedule          | Others                    | Yes     |              |
    | 279  | The Guardian API         | Others                    | Yes     |              |
    | 280  | US Census                | Others                    | Yes     |              |
    | 281  | Waiteraid                | Others                    | Yes     |              |
    | 282  | Weatherstack             | Others                    | Yes     |              |
    | 283  | Wikipedia Pageviews      | Others                    | Yes     |              |
    | 284  | xkcd                     | Others                    | Yes     |              |

    </center>

### **Business Intelligence (BI) Tools**
DataOS supports seamless integration with popular BI tools:

- [Tableau Cloud](/interfaces/data_product_hub/activation/bi_sync/tableau_cloud/)
- [Tableau Desktop](/interfaces/data_product_hub/activation/bi_sync/tableau_desk/)
- [Power BI](/interfaces/data_product_hub/activation/bi_sync/powerbi/)
- [Apache Superset](/interfaces/data_product_hub/activation/bi_sync/superset/)


Connection with [Microsoft Excel](/interfaces/data_product_hub/activation/bi_sync/excel/) is feasible thorough the Power BI Connector.

This enables you to visualize and analyze data processed through DataOS using your preferred BI platforms.

### **HighTouch Connectors**

Integration with HighTouch enables reverse-ETL use cases, allowing data to be syndicated from DataOS to over 125 SaaS tools and business applications.

???info "HighTouch Supported Sources"

    <center>

    | S.No | Connector Name         | Type            |
    |------|------------------------|-----------------|
    | 1    | Airtable               | Data Storage    |
    | 2    | Athena                 | Query Service   |
    | 3    | Azure Blob Storage      | Data Storage    |
    | 4    | Azure Synapse           | Data Warehouse  |
    | 5    | Bigquery                | Data Warehouse  |
    | 6    | ClickHouse              | Database        |
    | 7    | Databricks              | Data Platform   |
    | 8    | Datawarehouse.io        | Data Platform   |
    | 9    | Elasticsearch           | Search Engine   |
    | 10   | Firebolt                | Database        |
    | 11   | Google Cloud Storage    | Data Storage    |
    | 12   | Google Sheets           | Spreadsheet     |
    | 13   | Greenplum Database      | Database        |
    | 14   | Materialize             | Database        |
    | 15   | Metabase                | BI Tool         |
    | 16   | Microsoft Excel         | Spreadsheet     |
    | 17   | Microsoft Fabric        | Data Platform   |
    | 18   | Mixpanel Cohorts        | Analytics       |
    | 19   | MongoDB                 | Database        |
    | 20   | MySQL                   | Database        |
    | 21   | OracleDB                | Database        |
    | 22   | Palantir Foundry        | Data Platform   |
    | 23   | PlanetScale             | Database        |
    | 24   | PostgreSQL              | Database        |
    | 25   | Redshift                | Data Warehouse  |
    | 26   | Rockset                 | Analytics DB    |
    | 27   | S3                      | Data Storage    |
    | 28   | SFTP                    | File Transfer   |
    | 29   | SingleStore             | Database        |
    | 30   | Snowflake               | Data Warehouse  |
    | 31   | SQL Server              | Database        |
    | 32   | Tableau                 | BI Tool         |
    | 33   | Teradata Vantage        | Data Warehouse  |
    | 34   | Trino                   | Query Service   |

    </center>

???info "HighTouch Supported Destinations"

    <center>

    | S.No | Connector Name                  | Type                 |
    |------|---------------------------------|----------------------|
    | 1    | Acoustic                        | Marketing Platform   |
    | 2    | ActiveCampaign                  | Marketing Automation |
    | 3    | Adikteev                        | Advertising Platform |
    | 4    | Adjust                          | Mobile Analytics     |
    | 5    | Adobe Campaign Classic          | Marketing Automation |
    | 6    | Adobe Target                    | Personalization Tool |
    | 7    | Airship                         | Mobile Marketing     |
    | 8    | Airtable                        | Data Storage         |
    | 9    | Algolia                         | Search Platform      |
    | 10   | AlloyDB                         | Database             |
    | 11   | Amazon Ads DSP and AMC          | Advertising Platform |
    | 12   | Amazon EventBridge              | Event Bus            |
    | 13   | Amazon Kinesis                  | Streaming Data       |
    | 14   | Amazon SQS                      | Queue Service        |
    | 15   | Amobee                          | Advertising Platform |
    | 16   | Amplitude                       | Analytics Platform   |
    | 17   | Anaplan                         | Planning Platform    |
    | 18   | Apache Kafka                    | Streaming Platform   |
    | 19   | Apollo.io                       | Sales Platform       |
    | 20   | Appcues                         | User Experience      |
    | 21   | AppsFlyer                       | Mobile Analytics     |
    | 22   | Asana                           | Project Management   |
    | 23   | Athena                          | Query Service        |
    | 24   | Attentive                       | SMS Marketing        |
    | 25   | Attio                           | CRM                  |
    | 26   | Auth0                           | Identity Management  |
    | 27   | AWS Lambda                      | Serverless Compute   |
    | 28   | Azure Blob Storage              | Data Storage         |
    | 29   | Azure Functions                 | Serverless Compute   |
    | 30   | Beeswax                         | Advertising Platform |
    | 31   | BigCommerce                     | E-Commerce Platform  |
    | 32   | BigQuery                        | Data Warehouse       |
    | 33   | Bloomreach                      | Commerce Experience  |
    | 34   | Box                             | Cloud Storage        |
    | 35   | Braze                           | Customer Engagement  |
    | 36   | Braze Cohorts                   | Customer Segmentation|
    | 37   | Brevo                           | Email Marketing      |
    | 38   | Calixa                          | Customer Data        |
    | 39   | Campaign Monitor                | Email Marketing      |
    | 40   | Campaigner                      | Email Marketing      |
    | 41   | Chameleon                       | Product Tours        |
    | 42   | Chargebee                       | Subscription Billing |
    | 43   | ChartMogul                      | Subscription Analytics|
    | 44   | ChurnZero                       | Customer Success     |
    | 45   | CitrusAd                        | Retail Media         |
    | 46   | CJ Affiliate                    | Affiliate Marketing  |
    | 47   | CleverTap                       | Mobile Marketing     |
    | 48   | ClickUp                         | Project Management   |
    | 49   | ClientSuccess                   | Customer Success     |
    | 50   | Close                           | CRM                  |
    | 51   | CockroachDB                     | Database             |
    | 52   | Common Room                     | Community Management |
    | 53   | Cordial                         | Email Marketing      |
    | 54   | Courier                         | Notification Service |
    | 55   | Criteo                          | Advertising Platform |
    | 56   | Customer.io                     | Email Marketing      |
    | 57   | Delighted                       | Customer Feedback    |
    | 58   | Drift                           | Conversational Marketing |
    | 59   | Dropbox                         | Cloud Storage        |
    | 60   | Dynamic Yield                   | Personalization      |
    | 61   | DynamoDB                        | NoSQL Database       |
    | 62   | Dynata                          | Data Platform        |
    | 63   | Elasticsearch                   | Search Engine        |
    | 64   | Eloqua                          | Marketing Automation |
    | 65   | Emarsys                         | Customer Engagement  |
    | 66   | Embedded Destination            | Data Integration     |
    | 67   | EnjoyHQ                         | User Research        |
    | 68   | Facebook Conversions            | Advertising Analytics|
    | 69   | Facebook Custom Audience        | Advertising Platform |
    | 70   | Facebook Offline Conversions    | Advertising Analytics|
    | 71   | Facebook Product Catalog        | Advertising Platform |
    | 72   | Firestore                       | NoSQL Database       |
    | 73   | Freshdesk                       | Customer Support     |
    | 74   | Freshsales                     | CRM                  |
    | 75   | Front                           | Customer Support     |
    | 76   | FullStory                       | Digital Experience   |
    | 77   | Gainsight                       | Customer Success     |
    | 78   | Gainsight PX                    | Product Experience   |
    | 79   | Genesys                         | Customer Experience  |
    | 80   | Gladly                          | Customer Service     |
    | 81   | Gong                            | Revenue Intelligence |
    | 82   | Google Ad Manager 360           | Advertising Platform |
    | 83   | Google ADH (BigQuery)           | Analytics Platform   |
    | 84   | Google Ads                      | Advertising Platform |
    | 85   | Google Analytics                | Web Analytics        |
    | 86   | Google Campaign Manager 360     | Advertising Platform |
    | 87   | Google Cloud Functions          | Serverless Compute   |
    | 88   | Google Cloud Pub/Sub            | Messaging Service    |
    | 89   | Google Cloud Storage            | Cloud Storage        |
    | 90   | Google Display & Video 360      | Advertising Platform |
    | 91   | Google Drive                    | Cloud Storage        |
    | 92   | Google Retail                   | Commerce Platform    |
    | 93   | Google Search Ads 360           | Advertising Platform |
    | 94   | Google Sheets                   | Spreadsheet          |
    | 95   | Google Sheets - Service Account | Spreadsheet          |
    | 96   | Google Sheets - User Account    | Spreadsheet          |
    | 97   | Heap                            | Analytics Platform   |
    | 98   | Help Scout                      | Customer Support     |
    | 99   | Hightouch Personalization API   | Personalization      |
    | 100  | HTTP Request                    | API                  |
    | 101  | HubDB                           | CMS Database         |
    | 102  | HubSpot                         | CRM                  |
    | 103  | Insider InOne                   | Customer Engagement  |
    | 104  | Intercom                        | Customer Messaging   |
    | 105  | iSpot.tv                        | Advertising Platform |
    | 106  | Iterable                        | Marketing Automation |
    | 107  | Jira                            | Project Management   |
    | 108  | Kameleon                        | Personalization      |
    | 109  | Klaviyo                         | Email Marketing      |
    | 110  | Kustomer                        | Customer Service     |
    | 111  | LaunchDarkly                    | Feature Management   |
    | 112  | LINE Ads                        | Advertising Platform |
    | 113  | LinkedIn Ads                    | Advertising Platform |
    | 114  | Mailchimp                       | Email Marketing      |
    | 115  | MariaDB                         | Database             |
    | 116  | Marigold Engage (Selligent)     | Email Marketing      |
    | 117  | Marigold Engage+                | Email Marketing      |
    | 118  | Marketo                         | Marketing Automation |
    | 119  | Mattermost                      | Collaboration Tool   |
    | 120  | Maxio                           | Subscription Billing |
    | 121  | Medallia                        | Customer Feedback    |
    | 122  | Microsoft Ads (Bing Ads)        | Advertising Platform |
    | 123  | Microsoft Dynamics 365          | CRM                  |
    | 124  | Microsoft Excel                 | Spreadsheet          |
    | 125  | Microsoft OneDrive              | Cloud Storage        |
    | 126  | Microsoft Teams                 | Collaboration Tool   |
    | 127  | MinIO                           | Object Storage       |
    | 128  | Mixpanel                        | Product Analytics    |
    | 129  | MoEngage                        | Customer Engagement  |
    | 130  | Monday                          | Project Management   |
    | 131  | MongoDB                         | NoSQL Database       |
    | 132  | mParticle                       | Customer Data Platform|
    | 133  | MySQL                           | Database             |
    | 134  | NCR Advanced Marketing Solution | Marketing Platform   |
    | 135  | NetSuite (REST)                 | ERP                  |
    | 136  | NetSuite (SOAP)                 | ERP                  |
    | 137  | Nextdoor                        | Advertising Platform |
    | 138  | Notion                          | Collaboration Tool   |
    | 139  | OfferFit                        | Personalization      |
    | 140  | OneSignal                       | Push Notifications   |
    | 141  | OpenSearch                      | Search Engine        |
    | 142  | Optimizely                      | A/B Testing          |
    | 143  | Oracle DB                       | Database             |
    | 144  | Orbit                           | Community Management |
    | 145  | Ortto                           | Marketing Automation |
    | 146  | Outreach                        | Sales Engagement     |
    | 147  | Partnerstack                    | Partner Management   |
    | 148  | Pendo                            | Product Analytics    |
    | 149  | Pinterest Ads                   | Advertising Platform |
    | 150  | Pipedrive                       | CRM                  |
    | 151  | PlanetScale                     | Database             |
    | 152  | Planhat                         | Customer Success     |
    | 153  | Poplar                          | Advertising Platform |
    | 154  | PostgreSQL                      | Database             |
    | 155  | PostHog                         | Product Analytics    |
    | 156  | Qualtrics                       | Customer Experience  |
    | 157  | QuickBooks                      | Accounting           |
    | 158  | RabbitMQ                        | Messaging Service    |
    | 159  | Reddit Ads                      | Advertising Platform |
    | 160  | Redis                           | NoSQL Database       |
    | 161  | Reply.io                        | Sales Engagement     |
    | 162  | Responsys                       | Marketing Automation |
    | 163  | Retention Science               | Marketing Automation |
    | 164  | Rockerbox                       | Marketing Analytics  |
    | 165  | Rockset                         | Analytics Database   |
    | 166  | Rokt                            | Marketing Platform   |
    | 167  | Rudderstack                     | Customer Data Platform|
    | 168  | S3                              | Cloud Storage        |
    | 169  | Sage Intacct                    | Accounting           |
    | 170  | Sailthru                        | Email Marketing      |
    | 171  | Salesforce                      | CRM                  |
    | 172  | Salesforce (Sandbox)            | CRM                  |
    | 173  | Salesforce Commerce Cloud       | E-Commerce Platform  |
    | 174  | Salesforce Marketing Cloud      | Marketing Automation |
    | 175  | Salesforce Pardot               | Marketing Automation |
    | 176  | Salesforce Pardot (Sandbox)     | Marketing Automation |
    | 177  | Salesloft                       | Sales Engagement     |
    | 178  | Samsung Ads                     | Advertising Platform |
    | 179  | SAP HANA                        | Database             |
    | 180  | SAP IBP                         | Supply Chain Planning|
    | 181  | Segment                         | Customer Data Platform|
    | 182  | ServiceNow                      | IT Service Management|
    | 183  | SFTP                            | File Transfer        |
    | 184  | Shopify                         | E-Commerce Platform  |
    | 185  | Singular                        | Marketing Analytics  |
    | 186  | Slack                           | Collaboration Tool   |
    | 187  | Smartsheet                      | Project Management   |
    | 188  | SMTP Email                      | Email Service        |
    | 189  | Snapchat                        | Advertising Platform |
    | 190  | Snowflake                       | Data Warehouse       |
    | 191  | Split                           | Feature Management   |
    | 192  | SQL Server                      | Database             |
    | 193  | StackAdapt                      | Advertising Platform |
    | 194  | Statsig                         | Feature Management   |
    | 195  | Stripe                          | Payment Platform     |
    | 196  | SugarCRM                        | CRM                  |
    | 197  | Tableau                         | BI Tool              |
    | 198  | Taboola                         | Advertising Platform |
    | 199  | The Trade Desk                  | Advertising Platform |
    | 200  | TikTok                          | Advertising Platform |
    | 201  | Totango                         | Customer Success     |
    | 202  | Twilio                          | Communication Platform|
    | 203  | Twilio SendGrid                 | Email Service        |
    | 204  | Upland Waterfall                | Advertising Platform |
    | 205  | User Interviews                 | User Research        |
    | 206  | Userflow                        | Onboarding Platform  |
    | 207  | Vero Cloud                      | Email Marketing      |
    | 208  | Vistar Media                    | Advertising Platform |
    | 209  | Vitally                         | Customer Success     |
    | 210  | Vizio Ads                       | Advertising Platform |
    | 211  | Webflow                         | Website Builder      |
    | 212  | WhatsApp                        | Communication Tool   |
    | 213  | Workday                         | ERP                  |
    | 214  | Workday Adaptive Planning       | Planning Platform    |
    | 215  | X Ads (formerly Twitter Ads)    | Advertising Platform |
    | 216  | Xandr                           | Advertising Platform |
    | 217  | Xero                            | Accounting           |
    | 218  | Yahoo                           | Advertising Platform |
    | 219  | Zapier                          | Automation Tool      |
    | 220  | Zendesk                         | Customer Support     |
    | 221  | Zoho CRM                        | CRM                  |
    | 222  | Zuora                           | Subscription Billing |

    </center>
