# Opensearch

## Read Config

```yaml
name: standalone-read-opensearch
version: v1
type: workflow
tags:
  - standalone
  - readJob
  - opensearch
description: Sample job
workflow:
  dag:
    - name: customer
      title: Sample Transaction Data Ingester
      description: The job ingests data from opneSearch source into file
      spec:
        tags:
          - standalone
          - readJob
          - opensearch
        stack: flare:3.0
        compute: runnable-default
        tier: connect
        flare:
          job:
            explain: true
            inputs:
              - name: elasticsearch
                elasticsearch:
                  index: estopic
                  nodes: <https://<host>:<port>
                  username: <username>
                  password: <password>
                  options:
                    extraOptions:
                      'es.nodes.wan.only': 'true'

            logLevel: INFO
            outputs:
              - name: finalDf
                outputType: file
                file:
                  format: iceberg
                  warehousePath: /data/examples/dataout/opensearch/
                  schemaName: default
                  tableName: trans_oms_data3
                  options:
                    saveMode: append
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM transactions_connect LIMIT 1
```

## Write Config

```yaml
name: standalone-write-opensearch
version: v1
type: workflow
tags:
  - standalone
  - writeJob
  - opensearch
description: Sample job
workflow:
  dag:
    - name: standalone-opensearch-write
      title: Sample Transaction Data Ingester
      description: The job ingests data from file source into openSearch
      spec:
        tags:
          - standalone
          - writeJob
          - opensearch
        stack: flare:3.0
        compute: runnable-default
        tier: connect
        flare:
          job:
            explain: true
            inputs:
              - name: transactions_connect
                inputType: file
                file:
                  path: /data/examples/datadir/transactions
                  format: json
                  isStream: false

            logLevel: INFO
            outputs:
              - name: finalDf
                outputType: elasticsearch
                elasticsearch:
                  index: estopic
                  nodes: <nodes>
                  username: <username>
                  password: <password>
                  options:
                    extraOptions:
                      'es.nodes.wan.only': 'true'
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM transactions_connect LIMIT 1
```