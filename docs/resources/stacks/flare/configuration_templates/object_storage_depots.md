# Object Storage Depots

To execute Flare Jobs on object storage depots such as Amazon S3, Azure ABFSS, Azure WASBS, Google Cloud Storage etc., a corresponding depot must first be created. If the required depot has not yet been created, refer to the following documentation links:

- [Amazon S3](/resources/depot/create_depot/s3/)

- [Azure ABFSS](/resources/depot/create_depot/abfss/)

- [Azure WASBS](/resources/depot/create_depot/wasbs/)

- [Google Cloud Storage](/resources/depot/create_depot/gcs/)

Depots created on top of supported object stores enable uniform interaction across platforms, including Azure Blob File System, Google Cloud Storage, and Amazon S3.

To run a Flare Job, the following information is required:

- The Uniform Data Locator (UDL) address of the input dataset (for read operations) or the output dataset (for write operations)

- The file format of the associated data

## Common Configurations

### **Read Config**

For reading the data, we need to configure the `name`, `dataset`, and `format` properties in the `inputs` section of the YAML. For instance, if your dataset name is `city_connect`, UDL address dataset stored in Azure Blob Storage is `dataos://thirdparty01:sampledata/avro`, and the file format is `avro`. Then the `inputs` section will be as follows-

```yaml
inputs:
  - name: city_connect                                # name of the dataset
    dataset: dataos://thirdparty01:sampledata/avro    # address of the input dataset
    format: avro                                      # file format: avro, csv, json, orc, parquet, txt, xlsx, xml
```

Your Flare Jobs can read from multiple data sources. In such a scenario, you have to provide an array of data source definitions as shown below.

```yaml
inputs:  
  - name: sample_csv                                                  # name of the dataset
    dataset: dataos://thirdparty01:none/sample_city.csv               # address of the input dataset
    format: csv                                                       # file format
    schemaPath: dataos://thirdparty01:default/schemas/avsc/city.avsc  # schema path
    schemaType:                                                       # schema type
    options:                                                          # additional options
      key1:value1                                                     # Data source-specific options
      key2:value2

  - name: sample_states                                               # name of the dataset
    dataset: dataos://thirdparty01:none/states                        # address of the input dataset
    format: csv                                                       # file format
    schema: "{\"type\":\"struct\",\"fields\":[{\"name\":\"country_code\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"country_id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}},{\"name\":\"id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}},{\"name\":\"latitude\",\"type\":\"double\",\"nullable\":true,\"metadata\":{}},{\"name\":\"longitude\",\"type\":\"double\",\"nullable\":true,\"metadata\":{}}]}" # schema

  - name: transaction_abfss                                           # name of the dataset
    dataset: dataos://abfss01:default/transactions_abfss_01           # address of the input dataset
    format: avro                                                      # file format
    options:                                                          # additional options
      key1:value1                                                     # Data source-specific options
      key2:value2

  - name: input_customers                                             # name of the dataset
    dataset: dataos://icebase:retail/customer                         # address of the input dataset
    format: iceberg                                                   # file format
```

**Sample Read configuration YAML**

Let’s take a case scenario where the dataset is stored in Azure Blob File System (ABFSS) and you have to read data from the source, perform some transformation steps and write it to the Icebase, which is a managed depot within the DataOS. The read config YAML will be as follows

```yaml title="object_storage_depots_read.yml"
--8<-- "examples/resources/stacks/flare/object_storage_depots_read.yml"
```

### **Write Config**

> **Note:** The `?acl=rw` suffix in the UDL indicates that the Access Control List (ACL) is configured with read-write permissions. The address of the output dataset can also be specified using the format `dataos://[depot]:[collection]?acl=rw`. The system will automatically append the name of the output dataset to this address.

For writing the data to a depot on an object store, we need to configure the `name`,  `dataset` and `format` properties in the `outputs` section of the YAML. For instance, if your dataset is to be stored at the UDL address  `dataos://thirdparty01:sampledata`  by the name `output01` and the file format is `avro`. Then the `outputs` section will be as follows

```yaml
outputs:
  - name: output01                                   # output name
    dataset: dataos://thirdparty01:sampledata?acl=rw # address where the output is to be stored
    format: avro                                     # file format: avro, csv, json, orc, parquet, txt, xlsx, xml
```

**Sample Write configuration YAML**

Let’s take a case scenario where the output dataset is to be stored in Azure Blob File System Depot (ABFSS), and you have to read data from the Icebase depot within the DataOS. The write config YAML will be as follows

```yaml title="object_storage_depots_write.yml"
--8<-- "examples/resources/stacks/flare/object_storage_depots_write.yml"
```




## Schema Configurations

This section describes schema configuration strategies used to manage and customize schemas for supported data sources within the Flare stack. For implementation guidance, refer to the [Schema Configurations documentation](/resources/stacks/flare/configuration_templates/object_storage_depots/schema_configurations/).





## Advanced Configurations

For detailed information for all supported formats, see [Source Configurations by Data Formats](/resources/stacks/flare/configuration_templates/object_storage_depots/source_configurations_by_data_formats/).
The following list provides format-specific configuration references for integrating various data sources with the Flare stack:

* **AVRO** – Describes how to configure [AVRO files](/resources/stacks/flare/configuration_templates/object_storage_depots/source_configurations_by_data_formats#avro) for source ingestion. 

* **CSV** – Covers options for parsing and validating CSV-formatted input. [View CSV configuration](/resources/stacks/flare/configuration_templates/object_storage_depots/source_configurations_by_data_formats#csv)
* **Iceberg** – Provides guidance on configuring [Apache Iceberg table formats](/resources/stacks/flare/configuration_templates/object_storage_depots/source_configurations_by_data_formats#iceberg). 
* **JSON** – Explains how to manage nested structures and data typing for [JSON input](/resources/stacks/flare/configuration_templates/object_storage_depots/source_configurations_by_data_formats#json).
* **ORC** – Details parameter settings for optimized ingestion of [ORC files](/resources/stacks/flare/configuration_templates/object_storage_depots/source_configurations_by_data_formats#orc).
* **Parquet** – Outlines best practices for reading schema-aware [Parquet data](/resources/stacks/flare/configuration_templates/object_storage_depots/source_configurations_by_data_formats#parquet).
* **Text** – Defines configuration options for [Plain text data sources](/resources/stacks/flare/configuration_templates/object_storage_depots/source_configurations_by_data_formats#text).
* **XLSX** – Specifies how to configure [Excel spreadsheet(XLSX) ingestion](/resources/stacks/flare/configuration_templates/object_storage_depots/source_configurations_by_data_formats#xlsx).
* **XML** – Provides details on parsing and validating structured [XML input](/resources/stacks/flare/configuration_templates/object_storage_depots/source_configurations_by_data_formats#xml).


