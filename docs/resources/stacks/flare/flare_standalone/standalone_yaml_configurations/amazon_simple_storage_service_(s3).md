# Amazon Simple Storage Service (S3)


# Read Config

**Input Section Configuration for Reading from S3 Data Source**

```yaml
inputs:
  - name: city_connect
    inputType: file
    file:
      path: s3a://<bucket-name>/<dir>/<file>/<table> # e.g. s3a://sample/default/data/s3Table
      format: json
```

**Sample YAML for Reading from S3 Data Source**

```yaml
version: v1
name: s3-read-01
type: workflow
tags:
  - standalone
  - readJob
  - s3
description: The job ingests city data from s3 bucket to any file source

workflow:
  title: Connect City
  dag:
    - name: city-s3-write-01
      title: Sample Transaction Data Ingester
      description: The job ingests city data from dropzone into raw zone
      spec:
        tags:
          - standalone
          - readJob
          - s3
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from S3
              - name: city_connect
                inputType: file
                file:
                  path: s3a://<bucket-name>/<dir>/<file>/<table>
                  format: json

            outputs: # Write to Local File System
              - name: finalDf
                outputType: file
                file:
                  format: iceberg
                  warehousePath: /data/examples/dataout/localFileDataSourceOutput
                  schemaName: default
                  tableName: trans_oms_data3
                  options:
                    saveMode: append

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect

          sparkConf:
            - 'spark.hadoop.fs.s3a.bucket.<bucket-name>.access.key': '<access-key>'
            - 'spark.hadoop.fs.s3a.bucket.<bucket-name>.secret.key': '<secret-key>'
```

# Write Config

**Output Section Configuration for Writing to S3 Data Source**

```yaml
outputs:
  - name: finalDf
    outputType: file
    file:
      path: s3a://<bucket-name>/<dir>/<file>/<table> # e.g. s3a://sample/default/data/s3Table
      format: json
```

**Sample YAML for Writing to S3 Data Source**

```yaml
version: v1
name: s3-write-01
type: workflow
tags:
  - standalone
  - writeJob
  - s3
description: The job ingests city data from any file source to s3 table

workflow:
  title: Connect City
  dag:
    - name: standalone-s3-write
      title: Sample Transaction Data Ingester
      description: The job ingests city data from dropzone into raw zone
      spec:
        tags:
          - standalone
          - writeJob
          - s3
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from Local System
              - name: city_connect
                inputType: file
                file:
                  path: /data/examples/default/transactions
                  format: json
                  isStream: false

            outputs: # Write to S3
              - name: finalDf
                outputType: file
                file:
                  path: s3a://<bucket-name>/<dir>/<file>/<table>
                  format: json

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect
          sparkConf:
            - 'spark.hadoop.fs.s3a.bucket.<bucket-name>.access.key': '<access-key>'
            - 'spark.hadoop.fs.s3a.bucket.<bucket-name>.secret.key': '<secret-key>'
```

Table of Contents