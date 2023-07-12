# Elasticsearch

## Read Config

**Input Section Configuration for Reading from Elasticsearch Data Source**

```yaml
inputs:
  - name: finalDf
    inputType: elasticsearch
    elasticsearch:
      index: esTopic
      nodes: <ip>:<port> # e.g. localhost:6500
```

**Sample YAML for Reading from Elasticsearch Data Source**

```yaml
version: v1
name: standalone-read-elasticsearch
type: workflow
tags:
  - standalone
  - readJob
  - elasticsearch
title: Write to local in standalone mode
description: |
				The purpose of this workflow is to read from Elasticsearch and write to Local System
workflow:
  dag:
    - name: read-elasticsearch
      title: read from elasticsearch using standalone mode
      description: |
        The purpose of this job is to read from Elasticsearch and write to Local System
      spec:
        tags:
          - standalone
          - readJob
          - elasticsearch
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO
            inputs: # Read from Elasticsearch
              - name: oms_transactions_data
                inputType: elasticsearch
                elasticsearch:
                  index: estopic
                  nodes: <ip>:<port>
                  options:
                    es.nodes.wan.only: true
            outputs: # Write to Local System
              - name: finalDf
                outputType: file
                file:
                  format: iceberg
                  warehousePath: /data/examples/dataout/elasticdata/
                  schemaName: default
                  tableName: trans_oms_data3
                  options:
                    saveMode: append
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM oms_transactions_data
```

## Write Config

**Output Section Configuration for Writing to Elasticsearch Data Source**

```yaml
outputs:
  - name: finalDf
    outputType: elasticsearch
    elasticsearch:
      index: esTopic
      nodes: <ip>:<port>  # e.g. localhost:6500
```

**Sample YAML for Writing to Elasticsearch Data Source**

```yaml
version: v1
name: standalone-write-elasticsearch
type: workflow
tags:
  - standalone
  - writeJob
  - elasticsearch
title: Write to elasticsearch in standalone mode
description: |
  The purpose of this workflow is to read from Local system and write to Elasticsearch
workflow:
  dag:
    - name: standalone-elasticsearch-write
      title: Write to elasticsearch using standalone mode
      description: |
        The purpose of this job is to read from Elasticsearch and write to Local System
      spec:
        tags:
          - standalone
          - writeJob
          - elasticsearch
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO
            inputs: # Read from Local System
              - name: oms_transactions_data
                inputType: file
                file:
                  path: /data/examples/default/city
                  format: csv
            outputs: # Write to Elasticsearch
              - name: finalDf
                outputType: elasticsearch
                elasticsearch:
                  index: estopic
                  nodes: <ip>:<port>
                  options:
                    extraOptions:
                      es.nodes.wan.only: 'true'
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM oms_transactions_data LIMIT 10
```
