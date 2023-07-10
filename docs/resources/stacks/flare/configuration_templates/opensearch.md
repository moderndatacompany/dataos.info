# Opensearch

## Read Config

```yaml
name: read-opensearch-01
version: v1
type: workflow
tags:
  - opensearch
  - read
description: this jobs reads data from opensearch and writes to icebase
workflow:
  dag:
    - name: opensearch-read-akshay-01
      title: read data from opensearch
      description: read data from opensearch
      spec:
        tags:
          - Connect
        stack: flare:4.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: input
                dataset: dataos://sanityopensearchalok01:default/opensearch_write
                options:
                  opensearch.nodes.wan.only: 'true'
                isStream: false
            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://icebase:sanity/sanity_opensearch?acl=rw
                format: iceberg
                options:
                  saveMode: append

            steps:
              - sequence:
                - name: finalDf
                  sql: SELECT * FROM input
```

## Write Config

```yaml
name: write-opensearch-01
version: v1
type: workflow
tags:
  - opensearch
  - write
description: this jobs reads data from thirdparty and writes to opensearch
workflow:
  dag:
    - name: opensearch-write
      title: write data to opensearch
      description: write data to opensearch
      spec:
        tags:
          - Connect
        stack: flare:4.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: input
                dataset: dataos://thirdparty01:none/city
                format: csv
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
                isStream: false
            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://sanityopensearchalok01:default/opensearch_write?acl=rw
                format: opensearch
                options:
                  extraOptions:
                    'opensearch.nodes.wan.only': 'true'
            steps:
              - sequence:
                - name: finalDf
                  sql: SELECT * FROM input
```