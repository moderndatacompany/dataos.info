# Reading and Writing Data 

Flare can process data from various data management/storage systems such as file systems, relational databases, Icebase, stream data. It supports reading and writing from different data sources (structured, semi-structured and unstructured) available in Apache Spark.

- Unstructured:  TXT, CSV

- Semi structured: JSON, XML

- Structured: AVRO, PARQUET, ORC, XLSX

This article will give you a better understanding of how you perform read and write operations in your Flare workflows. You need to provide the configuration settings under **inputs** and **outputs** section in the YAML file. You can also use specific options available for the various data sources based on their capabilities.

## Inputs section  

While reading data from any data source, you need to define the following under **inputs** section. 

- name: Name to refer the dataset 
- dataset: Address of the dataset to be read
- format: [optional] Format of data to be read. If a dataset is registered and indexed with Metis then format will be automatically identified. 
- schema/schema path:  [optional] If a data source accepts a user-specific schema, apply them.
- options: [optional] Key-value configuration for a specific data source to parameterize how data has to be read. If no option is supplied, default values for the options will be used.

> :material-alert: **Note**: Your Flare workflow can read from multiple data sources. In such a scenario, you have to provide an array of data source definitions. 

### Inputs example
 
```yaml
inputs:  
  - name: sample_csv
    dataset: dataos://thirdparty01:none/sample_city.csv
    format: csv
    schemaPath: dataos://thirdparty01:default/schemas/avsc/city.avsc
    schemaType:
    options: 
      key1:value1                                            # Data source specific options
      key2:value2

  - name: sample_states
    dataset: dataos://thirdparty01:none/states
    format: csv
    schema: "{\"type\":\"struct\",\"fields\":[{\"name\":\"country_code\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"country_id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}},{\"name\":\"id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}},{\"name\":\"latitude\",\"type\":\"double\",\"nullable\":true,\"metadata\":{}},{\"name\":\"longitude\",\"type\":\"double\",\"nullable\":true,\"metadata\":{}}]}"

  - name: my_input_view
    dataset: dataos://kafka:default/cloudevents01
    options:
      key1:value1                                            # Data source specific options
      key2:value2

  - name: transaction_abfss
    dataset: dataos://abfss01:default/transactions_abfss_01
    format: avro
    options:
      key1:value1                                            # Data source specific options
      key2:value2

  - name: input_customers
    format: iceberg
    dataset: dataos://icebase:retail/customer
```

## Outputs section 

Currently, Flare supports two output formats- parquet and iceberg. For writing data, define the details where the dataset is to be stored, what is going to be its name etc.

> :material-alert: **Note**: It is possible to write the output of a Flare job to multiple locations. You need to write the output and dataset information multiple times.

1. In the **outputs** section, provide the reference and location information for the output.
      - name: Reference for the output 
      - depot: Depot provides a reference to the Data sink where you want to create dataset. Specify Depot you want to write data to.

2. In the **steps** section, describe the steps to generate the output. you also need to provide the details of the ouput dataset and the order in which multiple operations will be executed to create the desired dataset.

      - **sink**: Provide the details of the output dataset.
         - sequenceName: The name of the sequence relevant for the sink
         - datasetName: Name assigned to the new dataset
         - title: Title for the output dataset
         - description: Description for the output dataset
         - tags: Labels attached to the output dataset
         - outputName: Name defined in the outputs section above
         - outputType: New dataset's file format
         - outputOptions: Different options depending on different outputTypes supported in Spark
             - partitionBy: Column used for partitioning the data. 
             - sort: Scope and columns for the sorting, sort order.
         
      - **sequence**: Order of operations, further has two key-value pairs:
        - name: Sequence name to be used as a reference for the output of the SQL query it has
        - doc: Documentation for the purpose of the query
        - sql: SQL query of the operation in Spark SQL format 
        - sqlfile: Reference to the sql file which contains sql query
        - functions: Flare functions and their parameters

To learn more about functions, refer to [Flare functions](functions.md).

### File-based output example
The following YAML shows the 'outputs' section for the file-based output type. In **outputOptions**, you can provide additional data source-specific options to customize the behavior of writing.

```yaml
  outputs:
    - name: output01
      depot: dataos://filebase:raw01
  steps:
    - sink:
        - sequenceName: seq_01
          datasetName: retail_dataset
          title: Retail Data
          description: ingested retail data
          tags:
            - Connect
            - retail
          outputName:  output01
          outputType: Parquet
          outputOptions:
            saveMode: overwrite
            partitionBy:
              - cust_id
             
      sequence:
        - name: seq_00
          sql: select *, to_timestamp(pickup_datetime/1000) as date_col from retail_data

        - name: seq_01
          sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
            ts_retail_data FROM seq_00
          functions:
              - name: rename
                column: Id
                asColumn: new_id

        - name: seq02
          doc: Pick all columns from cities and add version as yyyyMMddHHmm formatted timestamp.
          sqlfile: flare/connect-city/city.sql
```

### Iceberg output example

In case of the Iceberg output type, provide some of the iceberg specific properties such as write format, compression method, partition specs under **iceberg** section. 

```yaml
  outputs:
    - name: output01
      depot: dataos://icebase:retail?acl=rw
  steps:
    - sink:
        - sequenceName: cities
          datasetName: city
          title: City Source Data
          description: City data ingested from external csv
          tags:
            - Connect
            - City
          
          outputName: output01
          outputType: Iceberg
          outputOptions:
            saveMode: append
            sort:
              mode: partition
              columns:
                - name: cityId
                  order: desc
              iceberg:                                       # Iceberg specific properties
              properties:
                write.format.default: parquet
                write.metadata.compression-codec: gzip
              partitionSpec:
                - type: identity
                  column: cityId
                - type: date
                  column: last_updated 
      
      sequence:
        - name: cities
          doc: Pick all columns from cities and add version as yyyyMMddHHmm formatted timestamp.
          sqlFile: flare/connect-city/city.sql
            

```
> :material-alert: **Note**: It is important to define partitionSpec under **iceberg** section to apply the partition strategy effectively.

## Supported data sources 
This section describes the Apache Spark data sources you can use in Flare for reading and writing data. 

Flare supports reading/writing from the following data sources. 

**Data Source** | **Scope** | **Properties** |  
-------- | -------- |-------- |
AVRO | Read | <a href="https://spark.apache.org/docs/latest/sql-data-sources-avro.html#data-source-option" target="_blank">Avro options </a>|
CSV | Read |<a href="https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option" target="_blank">CSV options</a>|
ICEBERG | Read/Write | <a href="https://iceberg.apache.org/#spark-configuration/" target="_blank">Iceberg Spark Configurations </a>| 
JSON | Read | <a href="https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option" target="_blank">JSON options </a>|
ORC | Read | <a href="https://spark.apache.org/docs/latest/sql-data-sources-orc.html" target="_blank">ORC options </a>|
PARQUET | Read/Write | <a href="https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#data-source-option" target="_blank">Parquet options</a>|
TEXT | Read | <a href="https://spark.apache.org/docs/latest/sql-data-sources-text.html#data-source-option" target="_blank">Text options </a>|
XLSX | Read | <a href="https://github.com/crealytics/spark-excel" target="_blank">Spark Excel options </a>|
XML | Read | <a href="https://github.com/databricks/spark-xml" target="_blank">Spark XML options</a>|


## Recipes
This section describes the data source-specific options you can use in Flare to read and write data. 

### Reading data

The following examples show how to read  data from supported data sources.

####  AVRO 

Avro format is a row-based storage format for Hadoop, which is widely used as a serialization platform. Avro facilitates the exchange of big data between programs written in any language. Avro supports evolutionary schemas, which supports compatibility checks and allows evolving your data over time. 

**Sample YAML file**
```yaml

inputs:
  - name: sample_avro
    dataset: dataos://thirdparty01:sampledata/avro
    format: avro
    schemaPath: /datadir/data/sample_avro.avsc
    options:
      avroSchema: none
      datetimeRebaseMode: EXCEPTION/CORRECTED/LEGACY 
      positionalFieldMatching: true/false 
                   
```
> :material-alert: **Note**: To understand more about each of the options for AVRO file, see the <a href="https://spark.apache.org/docs/latest/sql-data-sources-avro.html#data-source-option" target="_blank">Avro options </a>.

#### CSV 

Flare allows you to read a file or directory of files in CSV format. You can provide various options to customize the behavior of reading, such as controlling the behavior of the header, delimiter character, character set, and so on.

The following YAML file describes how you define various options when you want to read from a CSV file.

```yaml
inputs:  
  - name: sample_csv
    dataset: /datadir/data/sample_csv.csv         # complete file path   
    format: csv
    options:
      header: false/true  
      inferSchema: true 
      delimiter: "   " 
      enforceSchema: false   
      timestampFormat: yyyy-MM-dd'T'HH:mm:ss[.SSS][XXX] 
      mode: PERMISSIVE/DROPMALFORMED/FAILFAST 

  - name: multiple_csvdata
    dataset: /datadir/data                      # complete folder path
    format: csv
    options:
      header: false/true  
      inferSchema: true 
             
```
> :material-alert: **Note**: To understand more about each of the options for CSV file, see the <a href="https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option" target="_blank">CSV options</a>.

#### JSON

Flare can automatically infer the schema of a JSON file and load it as a DataOS dataset. Each line in JSON file must contain a separate, self-contained valid JSON object. For a regular multi-line JSON file, set the multiLine option to true.

The following YAML file describes how you define various options for reading from a JSON file.

**Sample YAML file**

```yaml
inputs:
  - name: sample_json
    dataset: dataos://thirdparty01:sampledata/json
    format: json
    options:
      primitivesAsString: true/false 
      prefersDecimal: true/false 
      allowComments: true/false 
      mode: PERMISSIVE/DROPMALFORMED/FAILFAST 
      timestampFormat: yyyy-MM-dd'T'HH:mm:ss[.SSS][XXX].
      dateFormat: yyyy-MM-dd.
      multiLine: true/false 				
```
> :material-alert: **Note**: To understand more, see the <a href="https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option" target="_blank">JSON options </a>.

#### PARQUET 

Parquet is a columnar format supported by many other data processing systems. Flare provides support for both reading and writing Parquet files that automatically preserve the original data schema. 

Parquet also supports schema evolution. Users can start with a simple schema and gradually add more columns to the schema as needed. In this way, users may have multiple Parquet files with different but mutually compatible schemas. The Parquet data source can now automatically detect this case and merge schemas of all these files.

While writing to the parquet file, you need to provide configuration settings for the 'Save' mode and 'Compression' method.

This example YAML file shows how you define various options for reading from a Parquet file.

**Sample YAML**

```yaml
inputs:
  - name: sample_parquet
    dataset: dataos://thirdparty01:sampledata/parquet
    format: parquet
    schemaPath: /datadir/data/sample_avro.avsc
    options:
      mergeSchema: false/true 
      datetimeRebaseMode: EXCEPTION/CORRECTED/LEGACY 
        
            
```
> :material-alert: **Note**: To understand more, see the <a href="https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#data-source-option" target="_blank">Parquet options</a>.

#### ORC 

Apache ORC (Optimized Row Columnar) is a free and open-source column-oriented data storage format of the Apache Hadoop ecosystem. Flare allows you to read a file in orc format. 

This example file shows how you define various options for reading from an ORC file.

```yaml
inputs:
  - name: sample_orc
    dataset: /datadir/data/sample_orc.orc
    format: orc 
    options:
      mergeSchema: false/true # Sets whether we should merge schemas collected from all ORC part-files.
 
```
> :material-alert: **Note**: To understand more, see the <a href="https://spark.apache.org/docs/latest/sql-data-sources-orc.html" target="_blank">ORC options </a>.

#### TEXT 

Flare allows you to read a text file or directory of text files into a DataOS dataset. When reading a text file, each line becomes each row with a string "value" column by default. In YAML, you can specify various options to customize reading behavior, such as controlling the behavior of the line separator.

```yaml

inputs:
  - name: sample_txt
    dataset: dataos://thirdparty01:sampledata/sample.txt
    format: text
    options:
      wholetext: true 
      lineSep: \r, \r\n, \n

  - name: sample_txt_files
      dataset: dataos://thirdparty01:sampledata/txt
      format: text
      options:
        wholetext: true
        lineSep: \r, \r\n, \n           
```
> :material-alert: **Note**: To understand more, see the <a href="https://spark.apache.org/docs/latest/sql-data-sources-text.html#data-source-option" target="_blank">Text options </a>.

#### XLSX 

Flare allows you to construct a dataset by reading a data file in XLSX format.  You can configure several options for XLSX file and customize the behavior of reading, such as location, sheet names, cell range, workbook password, etc. Flare supports reading multiple XLSX files kept in a folder. 

This example YAML file shows how you define various options for reading from an XLSX file.

```yaml

inputs:
  - name: sample_xlsx
    dataset: dataos://thirdparty01:sampledata/xlsx/returns.xlsx    # pass complete file path
    format: xlsx
    sheetName: aa 
    header: false/true  
    workbookPassword: password 
    inferSchema: true # If column types to be inferred when reading the file.

  - name: sample_xlsx_files
    dataset: dataos://thirdparty01:sampledata/xlsx    # pass complete path for the folder where files are kept
    format: xlsx            
```
> :material-alert: **Note**: To understand more about the XLSX options, see the <a href="https://github.com/crealytics/spark-excel" target="_blank">Spark Excel options </a>.

#### XML 
 
Flare allows you to read a file in XML format. You can provide various options to customize the behavior of reading, such as how you want to deal with corrupt records, specify the path to an XSD file that is used to validate the XML for each row individually, whether to exclude attributes, etc. 

This example YAML file shows how you define various options for reading from a XML file.

```yaml
inputs:
  - name: sample_xml
    dataset: dataos://thirdparty01:sampledata/xml
    format: xml
    schemaPath: dataos://thirdparty01:none/schemas/avsc/csv.avsc
    options:
      path: Location of files 
      excludeAttribute : false
      inferSchema: true
      columnNameOfCorruptRecord: _corrupt_record
      attributePrefix: _
      valueTag: _VALUE
      charset: 'UTF-8' 
      ignoreNamespace: false
      timestampFormat: UTC
      dateFormat: ISO_DATE  
```
> :material-alert: **Note**: To understand more about the options for XML file, see the <a href="https://github.com/databricks/spark-xml" target="_blank">Spark XML options</a>.


### Writing data

The following examples show how you can specify various options while writing data to the supported data sources in Flare. 

#### PARQUET

```yaml
outputs:
  - name: output01
    depot: dataos://filebase:raw01
steps:
  - sink:
    - sequenceName: ny_taxi_ts
      datasetName: ny_taxi_parquet_06
      outputName:  output01
      outputType: Parquet
      outputOptions:
        saveMode: overwrite
        partitionBy:
          - store_and_fwd_flag
      tags:
        - Connect
        - NY-Taxi
      title: NY-Taxi Data

    sequence:
      - name: ny_taxi_changed_dateformat
        sql: select *, to_timestamp(pickup_datetime/1000) as date_col from ny_taxi

      - name: ny_taxi_ts
        sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
          ts_ny_taxi FROM ny_taxi_changed_dateformat
   			
```
#### ICEBERG
```yaml
outputs:
  - name: output01
    depot: dataos://icebase:retail?acl=rw
steps:
    - sink:
        - sequenceName: cities
          datasetName: city
          outputName: output01
          outputType: Iceberg
          description: City data ingested from external csv
          tags:
            - Connect
            - City
          title: City Source Data
          outputOptions:
            saveMode: overwrite
            iceberg:
              properties:
                write.format.default: parquet
                write.metadata.compression-codec: gzip
            partitionSpec:
              - type: identity
                column: version             
      sequence:
        - name: cities
          doc: Pick all columns from cities and add version 
          as yyyyMMddHHmm formatted timestamp.
          sqlFile: flare/connect-city/city.sql

```
> :material-alert: **Note**: To understand more, see the <a href="https://iceberg.apache.org/#spark-configuration/" target="_blank">Iceberg Spark Configurations </a>.





   
