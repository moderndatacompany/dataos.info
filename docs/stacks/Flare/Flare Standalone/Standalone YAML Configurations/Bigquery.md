# Bigquery

## Read Config

Input Section Configuration for Reading from Bigquery Data Source

```yaml
inputs:
  - name: transactions_connect 
    inputType: bigquery 
    bigquery:
      table: transactions_standalone_02 
      projectId: <project-id> # provided in the json file
      dataset: <dataset-name> 
```

> 🗣️ Make sure the `dataset` and `temporaryBucket` you mention while writing should exist in the Bigquery otherwise your job/query will fail

Sample YAML for Reading from Bigquery Data Source

```yaml
version: v1
name: standalone-read-bigquery
type: workflow
tags:
  - standalone
  - readJob
  - bigquery
description: Sample job
workflow:
  dag:
    - name: city-bigquery-read-01
      title: Sample Transaction Data Ingester
      description: The job ingests customer data from Bigquery to file source
      spec:
        tags:
          - standalone
          - readJob
          - bigquery
        stack: flare:3.0
        compute: runnable-default
        tier: connect
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from Bigquery
              - name: transactions_connect
                inputType: bigquery
                bigquery:
                  table: transactions_standalone_09_nov
                  projected: <project-id>
                  dataset: <dataset-name>

            outputs: # Write to Local System
              - name: finalDf
                outputType: file
                file:
                  schemaName: retail
                  tableName: transactions_standalone_readbq02
                  format: Iceberg
                  warehousePath: /data/examples/dataout/bigquerydata
                  options:
                    saveMode: append

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM transactions_connect LIMIT 1

          sparkConf:
            - "spark.hadoop.google.cloud.auth.service.account.json.keyfile": 'secret-file-path'
					# Keep the json key file at the base directory where you have kept 
					# the configuration file & sample data and prefix it with /data/examples 
```

## Write Config

Output Section Configuration for Writing to Bigquery Data Source

```yaml
outputs:
  - name: finalDf
    outputType: bigquery 
    bigquery:
      table: transactions_standalone_01 
      projectId: <project-id> # refer from the json key
      dataset: <dataset-as-per-bigquery> 
      options:
        bigquery:
          temporaryBucket: <bucket-name>
```

Sample YAML for Writing to Bigquery Data Source

```yaml
version: v1
name: standalone-write-bigquery
type: workflow
tags:
  - standalone
  - writeJob
  - bigquery
description: Sample job
workflow:
  dag:
    - name: standalone-bigquery-write
      title: Sample Transaction Data Ingester
      description: The job ingests data from file source into bigquery
      spec:
        tags:
          - standalone
          - writeJob
          - bigquery
        stack: flare:3.0
        compute: runnable-default
        tier: connect
        flare:
          job:
            explain: true
            logLevel: INFO
            inputs: # Read from Local
              - name: transactions_connect
                inputType: file
                file:
                  path: /data/examples/default/transactions
                  format: json
                  isStream: false

            outputs: # Write to Bigquery
              - name: finalDf
                outputType: bigquery
                bigquery:
                  table: transactions_standalone_09_nov
                  projectId: dataos-ck-res-yak-dev
                  dataset: dev
                  options:
                    bigquery:
                      temporaryBucket: tmdc-development-new

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM transactions_connect

          sparkConf:
            - "spark.hadoop.google.cloud.auth.service.account.json.keyfile": 'secret-file-path'
					# Keep the json key file at the base directory where you have kept 
					# the configuration file & sample data and prefix it with /data/examples
```