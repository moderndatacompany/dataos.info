# Depot Service [WIP]

A typical business entity deals with various data systems which include Data warehouses, Databases, Object stores, etc. Each one of these systems has different APIs, different ways to organize data, different drivers, SDKs, connectors, secrets/credentials, etc. This adds to a lot of boiler-plating for a data engineer to work with them.

Depot abstracts these source systems and presents a coherent set of APIs to work with.

## Depot Service

Depot service is a DataOS service that manages depot construct. 

<center>

![Depot](./Depot_Service__(3).png)

</center>

<figcaption align = "center">Workflow of Depot Service</figcaption>
<br>

## Source Systems

Typically, there are 2 categories of data sources, A) Managed - where there is a system in place to manage metadata, and B) Unmanaged - where people can throw whatever files have in whatever format in a haphazard way. 

As depicted in `Figure 1`, Depot can handle 4 broad types of data sources. 

1. `File systems` - Unmanaged object storage with CSV, Parquet, Avro files. 
2. `Data-lake systems` - Managed object storage with files in a specific arrangement with specified formats, managed by a Metadata System. Like, Delta Lake, Apache Hudi, Apache Hive, DataOS Icebase, etc. 
3. `Database systems` - Any database or data warehouses that can be accessed by JDBC APIs. They have an in-built Metadata System.
4. `Event systems` - Messaging queues. Like, Kafka, Confluent Kafka, Pulsar, Apache Kinesis, etc. Some of these have Metadata Systems in place. 

## Features

### Address

Depot creates a consistent address for every source system that it connects with. A typical address looks like - `dataos://[depot]:[collection]/[dataset]`

A `collection` is how typically a database arranges its tables. Postgres calls it `schema`, MySql calls it a `database`, Pulsar calls it a `tenant`, Mongo calls it a `collection`, and so on. 

We call it a `collection`.

### Connection

Depot works like an abstraction for connection details too. The system keeps all such information behind depots. The components communicate about depot connection details using dataos address only.

### Secrets & Credentials

Depot keeps sensitive information with the help of pluggable secret management systems like heimdall today and it could be kubernetes secret store or may be hashicorp vault tomorrow. It helps you store credentials behind Dataos address only. One can ask the stacks to use secrets with specific acls e.g. 

`dataos://[depot]:[collection]/[dataset]?acl=r`

or 

`dataos://[depot]:[collection]/[dataset]?acl=rw`

### Introspection

Depot service helps you answer basic details about a depot or the storage engine depot is pointing to e.g.

- What all datasets are present within the depot?
- Basic details around the dataset e.g. dictionary, partition info, indexes and constraints.

### Query

Depot service helps in querying data by providing a on demand, scalable api/ jdbc based based query interface backed by dataframe based sqls.

### DDL

DDL interfaces power creating and managing (add/remove columns, partitions) capabilities on top of depots. These capabilities/features might vary based on depot types e.g. we offer a wide variety of operations on top of managed depots like icebase, fastbase etc. and limited support on top of unmanaged depots.

### DML

DML interfaces help deal with dataset based tooling for example compacting datasets, metadata files, managing dataset snapshots etc. These apis are also supported for few managed depots.

## Feature Matrix

| Source System Type | Metadata Management | Connection, secrets & credentials | Introspection | Dataframe SQL Query | DDL | DML |
| --- | --- | --- | --- | --- | --- | --- |
| Files | NO | YES | NO | PARTIAL | NO | NO |
| Data-lake | YES | YES | YES | YES | YES | YES |
| Database | YES | YES | YES | YES | YES | YES |
| Event | YES | YES | YES | YES | YES | NO |
| Event | NO | YES | NO | NO | NO | NO |

> If the source doesn’t have a Metadata System in place, Depot can *only* manage connection, secrets, and credentials abstraction.
> 

## Popular Sources Matrix


| Source System Type | Name | Metadata Management |
| --- | --- | --- |
| Files | AWS S3 | NO |
| Files | Azure Blob, ADLS | NO |
| Files | GCS | NO |
| Data-lake | DataOS Icebase | YES |
| Data-lake | Databricks Delta Lake | YES |
| Data-lake | Apache Hudi | YES |
| Data-lake | Apache Hive | YES |
| Data-lake | Apache Iceberg | YES |
| Data-lake | AWS Glue | YES |
| Database | Snowflake DB | YES |
| Database | Redshift | YES |
| Database | Greenplum | YES |
| Database | Trino | YES |
| Database | Athena | YES |
| Database | Presto | YES |
| Database | Azure SQL Warehouse | YES |
| Database | Big Query | YES |
| Database | Clickhouse | YES |
| Database | Oracle | YES |
| Database | Postgres | YES |
| Database | Mysql | YES |
| Event | Kafka | NO |
| Event | Confluent Kafka | YES |
| Event | Pulsar | YES |
| Event | DataOS Fastbase | YES |
| Event | Azure EventHub | NO |
| Event | Amazon Kinesis | YES |

## Depot Consumers

### DataOS Stacks

*TBD*

### Minerva

*TBD*

### Lens

*TBD*

### UDL

*TBD*

### Data Apps

*TBD*

---