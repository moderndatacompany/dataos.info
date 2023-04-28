# **Azure Blob Storage (ABFSS)**

# **Read Config**

**Input Section Configuration for Reading from ABFSS Data Source**

```yaml
inputs:
  - name: city_connect
    inputType: file
    file:
      path: 'abfss://<container>@<account-name>.dfs.core.windows.net/<depot>/<collection>/<dataset>'
      schemaName: abfss01
      format: json
      isStream: false
```

**Sample YAML for Reading from ABFSS Data Source**

```yaml
version: v1 
name: standalone-read-abfss 
type: workflow 
tags: 
  - standalone
  - readJob
  - abfss
description: The job ingests city data from azure to file source 
workflow: 
  title: Connect City 
  dag: 
    - name: city-abfss-write-01 
      title: Sample Transaction Data Ingester 
      description: The job ingests city data from azure to local directory 
      spec: 
        tags: 
          - standalone
          - readJob
          - abfss
        stack: flare:3.0 
        compute: runnable-default 
        flare: 
          job: 
            explain: true

            inputs: # Read from Azure Blob File System
              - name: city_connect
                inputType: file 
                file: 
                  path: 'abfss://<container>@<account-name>.dfs.core.windows.net/<depot>/<collection>/<dataset>'
                  format: iceberg
                  isStream: false

            outputs: # Write to Local System
              - name: finalDf
                outputType: file
                file: 
                  format: iceberg
                  warehousePath: /data/examples/dataout/bigquerydata
                  schemaName: default
                  tableName: trans_oms_data3
                  options:
                    saveMode: append
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect

          sparkConf:
            - 'spark.hadoop.fs.azure.account.key.<account-name>.dfs.core.windows.net': 'account-key'
```

# **Write Config**

**Output Section Configuration for Writing to ABFSS Data Source**

```yaml
outputs:
  - name: city_connect
    outputType: file
    file:
      warehousePath: 'abfss://<container>@<account-name>.dfs.core.windows.net/<depot>'
      schemaName: abfss01
      tableName: abfssTable
      format: iceberg
```

**Sample YAML for Writing to ABFSS Data Source**

```yaml
---
version: v1
name: standalone-write-abfss
type: workflow
tags:
  - standalone
  - writeJob
  - abfss
description: The job ingests city data from file source to azure
workflow:
  title: Connect City
  dag:
    - name: standalone-abfss-write
      title: Sample Transaction Data Ingester
      description: The job ingests city data from dropzone into raw zone
      spec:
        tags:
          - standalone
          - writeJob
          - abfss
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true

            inputs: # Read from Local System
              - name: city_connect
                inputType: file
                file:
                  path: /data/examples/default/transactions
                  format: json
                  isStream: false

            outputs: # Write to Azure Blob File System
              - name: city_connect
                outputType: file
                file:
                  warehousePath: 'abfss://<container>@<account-name>.dfs.core.windows.net/<depot>'
                  schemaName: <collection> # e.g. abfss01
                  tableName: <dataset> # e.g. abfssTable
                  format: iceberg

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect

          sparkConf:
            - 'spark.hadoop.fs.azure.account.key.<account-name>.dfs.core.windows.net': '<account-key>'
```