# Icebase

Icebase is a depot type within DataOS that leverages the power of the Apache Iceberg table format. It integrates with popular object storage systems like [Azure Data Lake](./depot_config_templates/azure_abfss.md), [Google Cloud Storage](./depot_config_templates/google_gcs.md), and [Amazon S3](./depot_config_templates/amazon_s3.md), following the Lakehouse pattern. By utilizing Iceberg, Icebase provides a robust OLAP (Online Analytical Processing) system that simplifies data lake access, making it as user-friendly and accessible as traditional data warehouses.


>Apache Iceberg, also known as Iceberg, is an open-source and high-performance table format specifically designed for storing large-scale analytic datasets, including petabyte-scale data. As a valuable addition to the big data ecosystem, Iceberg is optimized to handle vast amounts of data efficiently.

Data developers can create multiple Icebase depots to store and manage data, enabling processing and analysis using various programming languages such as R, Python, Scala, and Java. Additionally, tools like Spark and Flink can be utilized to work with Icebase datasets. For seamless integration into existing workflows, SQL can be used to interact with the tables stored in Icebase depots.

<aside class=callout>
🗣 Iceberg refers to the file format itself, while Icebase is the catalog or depot type within DataOS. Multiple depots of the Icebase type can be created to accommodate expanding data storage and management requirements. It is important to note that datasets stored in the Iceberg format may also exist in depots that are not specifically of the Icebase type. Icebase is a depot on top of data lake storage that mandates the Iceberg file type.
</aside>

---

## Commands in DataOS

A mechanism is required to effectively manage and inspect datasets stored in Icebase or any other depot utilizing the Iceberg format. The management APIs serve this purpose by providing support for various Data Definition Language (schema) related tasks.

A set of APIs have been implemented to facilitate these operations, allowing for adding and removing columns, managing dataset metadata, listing snapshots, and more. The `dataset` command comes into the picture here as it enables apply data toolbox commands.

**Observing changes on the Workbench**

To view metadata changes in the Workbench, executing the `set-metadata` command with the `latest` version is necessary. The changes made at the command line will not be reflected in the Workbench until the `set-metadata` command has been executed.

The execution of the `set-metadata` command to update to the latest version can be performed as follows:

```shell
dataos-ctl dataset -a ${{udl}} set-metadata -v ${{set-metadata}}

# '-a' flag denotes Dataset Address
# ${{udl}} is a placeholder for dataset UDL - dataos://icebase:retail/city is one such sample UDL
# '-v' flag denotes the Set Metadata of the Dataset
# ${{set-metadata}} is a placeholder for the current set metadata version of the dataset - latest OR v1.gz.metadata.json are sample set metadata versions.
```

---

## How to create and fetch datasets?

### **Create Dataset**

The `create` command is utilized to create a dataset using the specified address and schema definition found within a YAML file. 

```shell
dataos-ctl dataset -a ${{udl}} create -f ${{manifest-file-path}}

# '-a' flag denotes the Dataset Address
# ${{udl}} is a placeholder for dataset UDL - dataos://icebase:retail/city is one such sample UDL
# '-f' flag denotes a file
# ${{manifest-file-path}} is a placeholder for Manifest File Location - home/new.yaml is one such sample Manifest File Location
```

When creating a dataset, the path of the payload or schema in the YAML file must be specified (mandatory), and the schema type must be in `avro` format. A sample manifest YAML file for Iceberg format dataset creation is provided for reference below. 

```yaml
schema: # mandatory
  type: "avro"
  avro: '{"type": "record", "name": "defaultName", "fields":[{"name": "__metadata", "type" :{"type": "map", "values": "string", "key-id":10, "value-id":11}, "field-id":1},{"name": "city_id", "type" :[ "null", "string"], "default":null, "field-id":2},{"name": "zip_code", "type" :[ "null", "int"], "default":null, "field-id":3},{"name": "city_name", "type" :[ "null", "string"], "default":null, "field-id":4},{"name": "county_name", "type" :[ "null", "string"], "default":null, "field-id":5},{"name": "state_code", "type" :[ "null", "string"], "default":null, "field-id":6},{"name": "state_name", "type" :[ "null", "string"], "default":null, "field-id":7},{"name": "version", "type": "string", "field-id":8},{"name": "ts_city", "type" :{"type": "long", "logicalType": "timestamp-micros", "adjust-to-utc":true}, "field-id":9}]}'
iceberg: # optional
  specs: # optional
    - index: 1
      type: "identity"
      column: "state_name"
      name: "state_name" # optional
    - index: 2
      type: year
      column: ts_city
      name: "year" # optional
  properties: # optional
    write.format.default: "parquet"
    prop1: "value1"
```

Save it onto your system, and provide its path in the manifest file location.

### **Get Dataset**

The `get` command can be used to fetch the existing dataset. The command can be used as follows:

```shell
dataos-ctl dataset -a ${{udl}} get

# '-a' flag denotes the Dataset Address
# ${{udl}} is a placeholder for dataset UDL - dataos://icebase:retail/city is one such sample UDL
```

### **Drop Dataset**

To drop the dataset and delete the entry from metastore, use the below command.

```shell
dataos-ctl dataset -a ${{udl}} drop

# '-a' flag denotes the Dataset Address
# ${{udl}} is a placeholder for dataset UDL - dataos://icebase:retail/city is one such sample UDL
```

or you can also equivalently use 

```shell
dataos-ctl dataset -a ${{udl}} drop -p false
# OR
dataos-ctl dataset -a ${{udl}} drop --purge false

# '-a' flag denotes the Dataset Address
# ${{udl}} is a placeholder for dataset UDL - dataos://icebase:retail/city is one such sample UDL
# '-p' or '--purge' flags denote the purge value
```

If this `-p`/`--purge` (Purge Value) is set to `true` (by default, this is `false`), the dataset entry gets deleted from the store as well as all its files.

```shell
dataos-ctl dataset -a ${{udl}} drop -p true
# OR
dataos-ctl dataset -a ${{udl}} drop --purge true

# ${{udl}} is a placeholder for dataset UDL - dataos://icebase:retail/city is one such sample UDL
# '-p' or '--purge' flags denote the purge value
```

[Case Scenario: Create, Get, and Drop Dataset](./icebase/case_scenario_create_fetch_and_drop_dataset.md)

---

## How to configure table properties?

### **List Properties**

To obtain the list of all the properties and their value, execute the following command

```shell
dataos-ctl dataset properties -a ${{udl}}

# '-a' flag denotes the Dataset Address
# ${{udl}} is a placeholder for dataset UDL - dataos://icebase:retail/city is one such sample UDL
```

### **Add Properties**

To add a single property, the below code can be used. 

```shell
dataos-ctl dataset -a ${{udl}} add-properties \
-p "${{property-name}}:${{property-value}}"

# '-a' flag denotes the Dataset Address
# ${{udl}} is a placeholder for dataset UDL - dataos://icebase:retail/city is one such sample UDL
```

To add multiple properties at the same time, use

```shell
dataos-ctl dataset -a dataos://icebase:retail/city add-properties \
-p "${{property-name}}:${{property-value}}" \
-p "${{property-name}}:${{property-value}}"
```

### **Remove Properties**

To remove a property, the following command can be used.

```shell
dataos-ctl dataset -a dataos://icebase:retail/city remove-properties \
-p "${{property-name}}" \
-p "${{property-name}}"
```

For more details and use cases, refer to the following link

[Case Scenario: Table Properties](./icebase/case_scenario_table_properties.md)

---

## How to manage field/column? (Schema Evolution)

### **Add Field/Column**

The following command can be used to add a column to the table or a nested struct by mentioning the name and datatype of the column to be added

```shell
dataos-ctl dataset -a dataos://icebase:retail/city add-field \
-n ${{column-name}} \
-t ${{column-datatype}}
# Additional Flags for -t decimal
-p ${{precision: any-positive-number-less-than-38}} \ # Only for -t decimal
-s ${{scale: any-whole-number-less-than-precision}} # Only for -t decimal
```

In the case of all data types excluding `decimal`, we have two command-line flags:

- The `-n` flag to designate the column name.
- The `-t` flag allows the specification of the data type.

Distinctly for the `decimal` data type, we provide two supplementary flags to allow for more granular control over the data:

- The `-p` flag for specifying the precision of the decimal number. The precision is defined as the maximum total number of digits that can be contained in the number. This value may be any positive integer up to, but not including, 38.
- The `-s` flag allows for the adjustment of the scale of the decimal number. The scale denotes the number of digits following the decimal point. This value can be any non-negative integer less than the value set for precision.

**Example of Add-Field (String Data Type)**

```shell
dataos-ctl dataset -a dataos://icebase:retail/city add-field \
-n new1 \ # Column/Field Name
-t string # Column/Field Data Type
```

**Example of Add-Field (Decimal Data Type)**

```shell
dataos-ctl dataset -a dataos://depot:collection/dataset add-field \
-n price \ # Column/Field Name
-t decimal \ # Column/Field Data Type
-p 10 \ # Precision
-s 2  # Scale
```

### **Drop Field/Column**

To remove an existing column from the table or a nested struct, the following command can be executed

```shell
dataos-ctl dataset -a dataos://icebase:retail/city drop-field \
-n ${{column-name}}
```

### **Rename Field/Column**

To rename an existing column or field in a nested struct, execute the below code

```shell
dataos-ctl dataset -a dataos://icebase:retail/city rename-field \
-n ${{column-name}} \
-m ${{column-new-name}}
```

### **Update Field/Column**

To widen the type of a column, struct field, map key, map value, or list element, the below command can be executed

```shell
dataos-ctl dataset -a dataos://icebase:retail/city update-field \
-n ${{column-name}} \
-t ${{column-datatype}}
# Additional Flags for -t decimal
-p ${{precision: can-only-be-widened-not-narrowed}} \ # Only for -t decimal
-s ${{scale: is fixed}} # Only for -t decimal
```

When updating a field, precision can only be widened, not narrowed. In contrast, the scale is fixed and cannot be changed when updating a field.

**Example of Update-Field (Long Data Type)**

```shell
dataos-ctl dataset -a dataos://icebase:retail/city update-field \
-n zip_code \
-t long
```

**Example of Update-Field (Decimal Data Type)**

```shell
dataos-ctl dataset -a dataos://depot:collection/dataset update-field \
-n price \ # Column/Field Name
-t decimal \ # Column/Field Data Type
-p 15 \ # Precision
-s 2 # Scale
```

For more details and use, case refer to the following link  

[Case Scenario: Schema Evolution](./icebase/case_scenario_schema_evolution.md)

---

## How to perform partitioning?

<aside class="callout">
🗣 This procedure uses partitioning on the upcoming/future data, not the existing one. To make changes to the current data, please look at the partitioning in Flare Case Scenarios.

</aside>

### **Single Partitioning**

The partitioning in any iceberg table is column based. Currently, Flare supports only these Partition Transforms: identity, year, month, day, and hour.

- #### **identity**
    
    ```shell
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "identity:state_name"
    ```
    
- #### **year**
    
    ```shell
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "year:ts_city:year_partition"
    ```
    
- #### **month**
    
    ```shell
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "month:ts_city:month_partition"
    ```
    
- #### **day**
    
    ```shell
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "day:ts_city:day_partition"
    ```
    
5. **hour**
    
    ```shell
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "hour:ts_city:hour_partition"
    ```
    

### **Multiple Partitioning**

Partitioning can be done on multiple levels. For example, a user wants to partition the city data into two partitions, the first based on `state_code` and the second based on the `month`. This can be done using the below command:

```shell
dataos-ctl dataset -a dataos://icebase:retail/city \
-p "identity:state_code" \
-p "month:ts_city:month_partition"
```

<aside class=callout>
🗣 The order of partition given should be the hierarchy in which the user needs the data to be partitioned.

</aside>

### **Partition Updation**

```shell
dataos-ctl dataset -a dataos://icebase:retail/city update-partition \
-p "${{partition_type}}:${{column_name}}:${{partition_name}}"
```

For more details and use cases, refer to the below link

[Case Scenario: Partitioning](./icebase/case_scenario_partitioning.md)

---

## How to model snapshots and managed metadata versions?

### **Snapshot**

Each time you write a dataset in Iceberg format, a snapshot is created. These snapshots provide the ability to query different versions of the dataset. 

#### **List Snapshots**

The `snapshots` command is used to list all the snapshots of the dataset. This will help determine how many dataset snapshots you have. Execute the following command -

```shell
dataos-ctl dataset -a dataos://icebase:retail/city snapshots 
```

#### **Set Snapshot**

This command helps in setting the snapshot of a dataset to a particular snapshot id. 

```shell
dataos-ctl dataset -a dataos://icebase:retail/city set-snapshot \
-i ${{snapshot-id}}
```

### **Metadata Listing**

#### **Get Metadata**

This command lists the metadata files with their time of creation.

```shell
dataos-ctl dataset metadata -a dataos://icebase:retail/city
```

#### **Set Metadata**

To set the metadata to the latest or some specific version, the following command can be used

```shell
dataos-ctl dataset -a dataos://icebase:retail/city set-metadata \
-v ${{latest|v2.gz.metadata.json}}
```

For more details and use cases, refer to the following link

[Case Scenario: Maintenance (Snapshots and Meta Data Listing)](./icebase/case_scenario_maintenance.md)