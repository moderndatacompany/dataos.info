# Google Cloud Storage (GCS)

## Read Config

Input Section Configuration for Reading from GCS Data Source

```yaml
inputs:
  - name: city_connect
    inputType: file
    file:
      warehousePath: 'gs://<bucket-name>/<file-path>' #e.g. gs://sample/data
      schemaName: gcs01
      tableName: gcsTable
      format: iceberg
```

Sample YAML for Reading from GCS Data Source

```yaml
version: v1
name: standalone-read-gcs
type: workflow
tags:
  - standalone
  - readJob
  - gcs
description: The job ingests city data from gcs to iceberg
workflow:
  title: Connect City
  dag:
    - name: city-gcs-write-01
      title: Sample Transaction Data Ingester
      description: The job ingests city data from gcs to iceberg
      spec:
        tags:
          - standalone
          - readJob
          - gcs
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
						loglevel: INFO
            inputs: # Read from Google Storage
              - name: city_connect
                inputType: file
                file:
                  warehousePath: 'gs://<bucket-name>/<file-path>' #e.g. gs://tmdc-dataos/sampledata
                  schemaName: gcs01
                  tableName: gcsTable
                  format: iceberg

            outputs: # Write to Local System
              - name: finalDf
                outputType: file
                file:
                  format: iceberg
                  warehousePath: /data/examples/dataout/gcsdata/
                  schemaName: default
                  tableName: trans_oms_data3
                  options:
                    saveMode: append

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect

          sparkConf:
            - 'spark.hadoop.google.cloud.auth.service.account.json.keyfile': 'gcp-demo-sa.json'
					# Keep the JSON key file at the base directory where you have kept the configuration file & sample data.
```

## Write Config

Output Section Configuration for Writing to GCS Data Source

```yaml
outputs:
  - name: city_connect
    outputType: file
    file:
      warehousePath: 'gs://<bucket-name>/<file-path>' #e.g. gs://sample/data
      schemaName: gcs01
      tableName: gcsTable
      format: iceberg
```

Sample YAML for Writing to GCS Data Source

```yaml
version: v1
name: standalone-write-gcs
type: workflow
tags:
  - standalone
  - writeJob
  - gcs
description: The job ingests city data from file source to gcs
workflow:
  title: Connect City
  dag:
    - name: standalone-gcs-write
      title: Sample Transaction Data Ingester
      description: The job ingests city data from file to gcs
      spec:
        tags:
          - standalone
          - writeJob
          - gcs
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs: # Read from Local System
              - name: city_connect
                inputType: file
                file:
                  path: /transactions/oms_transactions.json
                  format: json
                  isStream: false
            outputs: # Write to Google Storage
              - name: city_connect
                outputType: file
                file:
                  warehousePath: 'gs://<bucket-name>/<file-path>' 
                  schemaName: gcs01
                  tableName: gcsTable
                  format: iceberg
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect
          sparkConf:
            - 'spark.hadoop.google.cloud.auth.service.account.json.keyfile': 'gcp-demo-sa.json'
					# Keep the JSON key file at the base directory where you have kept the configuration file & sample data.
```