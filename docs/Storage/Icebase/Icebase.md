# Icebase

Icebase depot type is backed by Apache Iceberg table format on underlying object storage (Azure Data Lake / GCS / S3 etc.). Icebase implements a Lakehouse pattern which means having an OLAP system on top of object storage that makes interaction with DataOS Data Lake as accessible as data warehouses. 

As it's a depot type, a whole collection of such depots can be created, and data within can be engineered and analyzed using R, Python, Scala, and Java, using tools like Spark and Flink. At the same time, interaction with the table can be done using SQL. 

Icebase depot 

> Apache Iceberg (or simply Iceberg) is a new, open-source, high-performance table format in a big data ecosystem designed for storing massive, analytic, or petabyte-scale datasets.
> 


> 🗣 `Iceberg` is a file format, `icebase` is a catalog, a type of depot within the DataOS.

# Commands in DataOS

In Icebase, we need a mechanism to manage and inspect datasets. The management APIs would help us deal with the client's Data Definition Language (schema) related asks.

We have implemented APIs to add/remove columns, manage dataset metadata, list snapshots, etc.

## Flags

The `-a` flag denotes addresses in datasets.

## Observing changes on the Workbench

To observe the metadata changes in the Workbench, you can execute the set-metadata command with the latest version. The changes implemented on the command line are not visible on the Workbench until the set-metadata command is executed.

The `set-metadata` command to update the version to the latest can be executed as follows -

```bash
dataos-ctl dataset -a dataos://icebase:retail/city set-metadata \
-v latest
```

# Creating and Getting Datasets

## Create Dataset

The command helps to create a dataset from a certain file stored in a folder with its respective YAML file.

```bash
dataos-ctl dataset -a dataos://icebase:retail/city create \
-f <manifest-file-path>
# Here '-f' flag denotes a file
```

The path of the payload or schema file in YAML is to be mentioned in which the schema type is AVRO while creating a dataset. The sample format for the YAML file is provided below.

YAML Example for Dataset Creation (Manifest File For Iceberg)

```yaml
schema: # <mandatory>
  type: "avro"
  avro: '{"type": "record", "name": "defaultName", "fields":[{"name": "__metadata", "type" :{" type": "map", "values": "string", "key-id":10, "value-id":11}, "field-id":1},{"name": "city_id", "type" :[ "null", "string"], "default":null, "field-id":2},{"name": "zip_code", "type" :[ "null", "int"], "default":null, "field-id":3},{"name": "city_name", "type" :[ "null", "string"], "default":null, "field-id":4},{"name": "county_name", "type" :[ "null", "string"], "default":null, "field-id":5},{"name": "state_code", "type" :[ "null", "string"], "default":null, "field-id":6},{"name": "state_name", "type" :[ "null", "string"], "default":null, "field-id":7},{"name": "version", "type": "string", "field-id":8},{"name": "ts_city", "type" :{" type": "long", "logicalType": "timestamp-micros", "adjust-to-utc":true}, "field-id":9}]}'
iceberg: # <optional>
  specs: # <optional>
    - index: 1
      type: "identity"
      column: "state_name"
			name: "state_name" # <optional>
		- index: 2
      type: year
      column: __ts
	    name: "year" # <optional>
  properties: # <optional>
    write.format.default: "parquet"
    prop1: "value1"
```

## Get Dataset

To get an existing dataset, the following command can be used.

```bash
dataos-ctl dataset -a dataos://icebase:retail/city get
```

For more details and use cases, refer to
[Case Scenario: Creating and Getting Dataset](Icebase/Case%20Scenario%20Creating%20and%20Getting%20Dataset.md).

# Table Properties

## List Properties

To obtain the list of all the properties and their value, execute the following command

```bash
dataos-ctl dataset properties -a dataos://icebase:retail/city
```

## Add Properties

To add a single property, the below code can be used. 

```bash
dataos-ctl dataset -a dataos://icebase:retail/city add-properties \
-p "<property-name>:<property-value>"
```

To add multiple properties at the same time, use

```bash
dataos-ctl dataset -a dataos://icebase:retail/city add-properties \
-p "<property-name>:<property-value>" \
-p "<property-name>:<property-value>"
```

## Remove Properties

To remove a property, the following command can be used.

```bash
dataos-ctl dataset -a dataos://icebase:retail/city remove-properties \
-p "<property-name>" \
-p "<property-name>"
```

For more details and use cases, refer to
[Case Scenario: Table Properties](Icebase/Case%20Scenario%20Table%20Properties.md).

# Schema Evolution

## Add Column

The following command can be used to add a column to the table or a nested struct by mentioning the name and datatype of the column to be added

```bash
dataos-ctl dataset -a dataos://icebase:retail/city add-field \
-n <column-name> \
-t <column-datatype>
```

## Drop Column

To remove an existing column from the table or a nested struct, the following command can be executed

```bash
dataos-ctl dataset -a dataos://icebase:retail/city drop-field \
-n <column-name>
```

## Rename Column

To rename an existing column or field in a nested struct, execute the below code

```bash
dataos-ctl dataset -a dataos://icebase:retail/city rename-field \
-n <column-name> \
-m <column-new-name>
```

## Update Column

To widen the type of a column, struct field, map key, map value, or list element, the below command can be executed

```bash
dataos-ctl dataset -a dataos://icebase:retail/city update-field \
-n <column-name> \
-t <column-datatype>
```

For more details and use, case refer to
[Case Scenario: Schema Evolution](Icebase/Case%20Scenario%20Schema%20Evolution.md).

# Partitioning

> 🗣 This procedure uses partitioning on the upcoming/future data, not the existing one. To make changes to the current data, please take a look at the partitioning in Flare Case Scenarios.


## Single Partitioning

The partitioning in any iceberg table is column based. Currently, Flare supports only these Partition Transforms: identity, year, month, day, and hour.

1. identity
    
    ```bash
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "identity:state_name"
    ```
    
2. year
    
    ```bash
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "year:ts_city:year_partition"
    ```
    
3. month
    
    ```bash
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "month:ts_city:month_partition"
    ```
    
4. day
    
    ```bash
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "day:ts_city:day_partition"
    ```
    
5. hour
    
    ```bash
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "hour:ts_city:hour_partition"
    ```
    

## Multiple Partitioning

Partitioning can be done on multiple levels. For example, a user wants to partition the city data into two partitions, the first based on `state_code` and the second based on the `month`. This can be done using the below command:

```bash
dataos-ctl dataset -a dataos://icebase:retail/city \
-p "identity:state_code" \
-p "month:ts_city:month_partition"
```


> 🗣 The order of partition given should be the hierarchy in which the user needs the data to be partitioned.


## Partition Updation

```bash
dataos-ctl dataset -a dataos://icebase:retail/city update-partition \
-p "<partition_type>:<column_name>:<partition_name>"
```

For more details and use cases, refer to
[Case Scenario: Partitioning](Icebase/Case%20Scenario%20Partitioning.md).

# Maintenance: Snapshot Modelling and Metadata Listing

# Snapshot

Whenever you write a dataset in Iceberg format, each time a snapshot is created, and you can list all the snapshots using the command. This will help determine how many dataset snapshots you have so you can set snapshots to travel back.

## List Snapshots

The list snapshot command is used to list all the snapshots of the dataset. This will help determine how many dataset snapshots you have. Execute the following command -

```bash
dataos-ctl dataset -a dataos://icebase:retail/city snapshots 
```

## Set Snapshot

This command helps in setting the snapshot of a dataset to a particular snapshot id. 

```bash
dataos-ctl dataset -a dataos://icebase:retail/city set-snapshot \
-i <snapshot-id>
```

# Metadata Listing

## List Metadata

This command lists the metadata files with their time of creation.

```bash
dataos-ctl dataset metadata -a dataos://icebase:retail/city
```

## Set Metadata

To set the metadata to the latest or some specific version, the following command can be used

```bash
dataos-ctl dataset -a dataos://icebase:retail/city set-metadata \
-v <latest|v2.gz.metadata.json>
```

For more details and use cases, refer to
[Case Scenario: Maintenance Snapshots and Meta Data Listing](Icebase/Case%20Scenario%20Maintenance%20(Snapshots%20and%20Meta%20Data).md).
