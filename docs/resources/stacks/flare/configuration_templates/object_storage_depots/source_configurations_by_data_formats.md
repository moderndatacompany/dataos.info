# Source Configurations by Data Formats

Within this page, you will find comprehensive instructions on implementing advanced configurations for your data reading and writing processes. Whether you are working with structured data formats such as AVRO, Parquet, or ORC or handling text files, XML, XLSX, or Iceberg files, we have got you covered.

## AVRO

The AVRO format is a highly efficient and flexible storage format designed for Hadoop. It serves as a serialization platform, enabling seamless data exchange between programs written in different languages. AVRO is particularly well-suited for handling big data and offers robust support for evolving schemas.

To read AVRO data in Flare, you can use the following YAML configuration:

```yaml
inputs:
  - name: sample_avro
    dataset: dataos://thirdparty01:sampledata/avro
    format: avro
    schemaPath: dataos://thirdparty01:sampledata/sample_avro.avsc
    options:
      avroSchema: none
      datetimeRebaseMode: EXCEPTION/CORRECTED/LEGACY 
      positionalFieldMatching: true/false
```

> **Note**: For a more comprehensive understanding of AVRO options and their usage, please refer to the refer to [Avro options](https://spark.apache.org/docs/latest/sql-data-sources-avro.html#data-source-option).
> 

## CSV

Flare supports reading/writing files or directories of files in CSV format. You have the flexibility to customize the behavior of the CSV reader by providing various options. These options allow you to control aspects such as header handling, delimiter character, character set, schema inference, and more.

Consider the following YAML configuration to define the options when reading from a CSV file:

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

> **Note**: For a detailed understanding of each option available for CSV files, please refer to the [CSV options](https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option) documentation.
> 

## Iceberg

Flare supports reading/writing files in the Iceberg format, which is a columnar data format designed for large-scale data processing. With Flare, you can leverage the power of Iceberg files and perform various operations on them.

To write an Iceberg file using Flare, you can use the following YAML configuration as an example:

```yaml
outputs:
  - name: ny_taxi_ts
    dataset: dataos://icebase:sample/ny_taxi_iceberg?acl=rw
    format: Iceberg
    options:
      saveMode: append         
      iceberg:
        partitionSpec:
        - type: identity
          column: trip_duration
```

> **Note:** For more information on the available options when working with Iceberg files, refer to the [Apache Iceberg](https://iceberg.apache.org/docs/latest/spark-configuration/) documentation.
> 

## JSON

Flare supports automatic schema inference for JSON files, allowing you to load them as DataOS datasets. Each line in the JSON file should contain a separate, self-contained valid JSON object. In the case of a multi-line JSON file, you can enable the `multiLine` option to handle it appropriately.

To read from a JSON file and specify various options, utilize the following YAML configuration:

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

> **Note**: For a comprehensive understanding of the available options for JSON files, please refer to the [JSON options](https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option) documentation.
> 

## ORC

Flare supports reading/writing ORC (Optimized Row Columnar) files, which is a column-oriented data storage format within the Apache Hadoop ecosystem. ORC is designed to optimize performance and compression for big data processing workloads. With Flare, you can seamlessly read data from ORC files into your data workflows.

To read an ORC file using Flare, you can use the following YAML configuration:

```yaml
inputs:
  - name: sample_orc
    dataset: /datadir/data/sample_orc.orc
    format: orc 
    options:
      mergeSchema: false/true # Sets whether we should merge schemas collected from all ORC part-files.
```

> **Note**: For more details on the available options when working with ORC files, refer to the [ORC options](https://spark.apache.org/docs/latest/sql-data-sources-orc.html) documentation.
> 

## Parquet

Flare offers support for reading and writing Parquet files, which is a widely adopted columnar storage format compatible with various data processing systems. When working with Parquet files, Flare automatically preserves the original data schema, ensuring data integrity throughout the processing pipeline.

Parquet also enables schema evolution, allowing users to progressively add columns to an existing schema as needed. This means that multiple Parquet files can have different but mutually compatible schemas. Flare's Parquet data source effortlessly detects and merges schemas from these files, simplifying schema management.

When writing to Parquet files, you can customize the behavior using the following configuration settings:

```yaml
inputs:
  - name: sample_parquet
    dataset: dataos://thirdparty01:sampledata/parquet
    format: parquet
    schemaPath: dataos://thirdparty01:sampledata/sample_avro.avsc
    options:
      mergeSchema: false/true 
      datetimeRebaseMode: EXCEPTION/CORRECTED/LEGACY
```

> **Note**: For detailed information on the available options for Parquet files, please refer to the [Parquet options](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#data-source-option) documentation.
> 

## Text

Flare supports reading text files or directories of text files into DataOS datasets. When reading a text file, each line is treated as a row with a default string "value" column. You can customize the reading behavior by specifying various options in YAML, including controlling the line separator behavior.

To read a text file using Flare, you can use the following YAML configuration:

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

> **Note**: For more details on the available options when working with text files, refer to the [Text options](https://spark.apache.org/docs/latest/sql-data-sources-text.html#data-source-option) documentation.
> 

## XLSX

Flare supports the creation of datasets by reading data files in XLSX format. You can customize the behavior of reading XLSX files by configuring various options such as file location, sheet names, cell range, workbook password, and more. Flare also enables the reading of multiple XLSX files stored in a folder.

To read an XLSX file using Flare, you can use the following YAML configuration:

```yaml
inputs:
  - name: sample_xlsx
    dataset: dataos://thirdparty01:sampledata/xlsx/returns.xlsx    # pass complete file path
    format: xlsx
		options:
	    sheetName: aa 
	    header: false/true  
	    workbookPassword: password 
	    inferSchema: true # If column types to be inferred when reading the file.

  - name: sample_xlsx_files
    dataset: dataos://thirdparty01:sampledata/xlsx    # pass complete path for the folder where files are kept
    format: xlsx
```

> **Note**: For a more detailed understanding of the available options when working with XLSX files, refer to the [Spark Excel options](https://github.com/crealytics/spark-excel) documentation. ****
> 

## XML

Flare provides support for reading/writing XML files, allowing you to leverage data stored in XML format. You have the flexibility to customize the reading behavior by specifying various options, such as handling corrupt records, validating XML against an XSD file, excluding attributes, and more.

To read an XML file using Flare, you can use the following YAML configuration as an example:

```yaml
inputs:
  - name: sample_xml
    dataset: dataos://thirdparty01:sampledata/xml/sample.xml
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

> **Note**: For a detailed understanding of the available options when working with XML files, refer to the [Spark XML options](https://github.com/databricks/spark-xml) documentation. 
>