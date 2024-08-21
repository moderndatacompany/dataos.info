# Flare Functions

Flare is a robust stack that provides users with an extensive set of pre-defined data manipulation functions. These functions can be executed at different processing stages, allowing for the execution of complex tasks without the need for extensive coding efforts. Additionally, Flare empowers users to create their own custom functions, known as User-Defined Flare Functions (UDFs), to address specific requirements or extend the functionality of the stack. 

The YAML syntax given below provides a sample of how Flare Functions are defined:

```yaml
functions: 
  - name: cleanse_column_names
  - name: unpivot 
    columns: 
      - "*" 
    pivotColumns:
      - week_year
    keyColumnName: week_year_column 
    valueColumnName: values_columns
```

<details>
<summary>Sample YAML showcasing application of Flare Function</summary>

```yaml
version: v1
name: wf-sample
type: workflow
workflow:
  dag:
    - name: sample
      spec:
        stack: flare:5.0
        stackSpec:
          driver:    
            coreLimit: 12000m
            cores: 2
            memory: 12000m
          executor:
            coreLimit: 12000m
            cores: 4
            instances: 3
            memory: 22000m        
          job:
            inputs:
              - name: input 
                dataset: dataos://thirdparty01:analytics/survey_unpivot/unpivot_data.csv
                format: csv

            logLevel: INFO
            outputs:
              - name: clustered_records
                dataset: dataos://icebase:sample/unpivot_data_02?acl=rw
                format: Iceberg
                description: unpivotdata
                options:
                  saveMode: overwrite
                  sort:
                    mode: global
                    columns:
                      - name: week_year_column
                        order: desc
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                    partitionSpec:
                      - type: bucket # hour, day, month, year, identity, bucket
                        column: week_year_column
                        numBuckets: 2
                title: unpivot data

            steps:
                - sequence:
                    - name: select_all_column
                      sql: Select * from input
# Flare Functions 
                      functions: 
                        - name: cleanse_column_names
                        - name: unpivot 
                          columns: 
                            - "*" 
                          pivotColumns:
                            - week_year
                          keyColumnName: week_year_column 
                          valueColumnName: values_columns
                    - name: clustered_records
                      sql: SELECT * FROM select_all_column CLUSTER BY week_year_column

          sparkConf:
            - spark.sql.extensions: org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```
</details>

In the succeeding list, we provide comprehensive information about these pre-defined functions and their usage.

[List of Flare Functions](/resources/stacks/flare/functions/list/)

# User-Defined Flare Functions

In addition to the pre-defined Flare Functions, Flare offers the ability to create custom User-Defined Flare Functions. These functions can be defined using YAML syntax, as demonstrated below.

```yaml
udfs:
  to_upper: "(value: String) => if (value.nonEmpty) { value.toUpperCase() } else { \"\" }"
  to_mask: "(value: String, pattern: String, mask: String) =>  { import io.dataos.flare.functions.utils.Utils \n val indexes = Utils.findCharIndex(pattern, mask) \n
    val ssnStr = new StringBuilder(value) \n
    indexes.stream().forEach(index => ssnStr.setCharAt(index, mask.charAt(0))) \n
    ssnStr.toString \n
    } "
```

<details><summary>Sample YAML showcasing User-defined Flare Function</summary>

```yaml
version: v1
name: cnt-city-udf-ingestion-001
type: workflow
tags:
- Connect
- City
description: The job ingests city data from dropzone into raw zone
workflow:
  title: Connect City
  dag:
  - name: city-ingestion-udf-01
    title: City Dimension Ingester
    description: The job ingests city data from dropzone into raw zone
    spec:
      tags:
      - Connect
      - City
      stack: flare:5.0
      compute: runnable-default
      stackSpec:
        job:
          explain: true
          inputs:
           - name: cities
             dataset: dataos://icebase:retail/city
             format: Iceberg
# User Defined Flare Functions
          udfs:
            to_upper: "(value: String) => if (value.nonEmpty) { value.toUpperCase() } else { \"\" }"
            to_mask: "(value: String, pattern: String, mask: String) =>  { import io.dataos.flare.functions.utils.Utils \n val indexes = Utils.findCharIndex(pattern, mask) \n
              val ssnStr = new StringBuilder(value) \n
              indexes.stream().forEach(index => ssnStr.setCharAt(index, mask.charAt(0))) \n
              ssnStr.toString \n
              } "

          logLevel: INFO
          outputs:
            - name: out001
              depot: dataos://icebase:retailsample?acl=rw
          steps:
          - sink:
              - sequenceName: finalDf
                datasetName: udf_cities_01
                outputName: out001
                outputType: Iceberg
                description: City data ingested from external csv
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
              - name: finalDf
                sql: SELECT *, to_upper(city_name) as city_name_upper, to_mask(city_id, 'xx###', 'X') as mask_city_id FROM cities
```
</details>