# MongoDB

## Read Config

```yaml
version: v1
name: mongodb-read-02
type: workflow
workflow:
  dag:
    - name: mongodb-read-02
      spec:
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO
            inputs:
              - name: input
                dataset: dataos://mongodb02:tmdc/city_01
                format: mongodb
                connectionProps:
                  ssl: "true"
                  retryReads: "true"

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM input

            outputs:
              - name: finalDf
                dataset: dataos://icebase:mongodb/city_02?acl=rw
                format: Iceberg
                options:
                  saveMode: append
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: none
```

## Write Config

```yaml
version: v1
name: mongodb-write-02
type: workflow
workflow:
  dag:
    - name: mongodb-write-02
      spec:
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO
            inputs:
              - name: input
                dataset: dataos://thirdparty01:none/city
                format: csv
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc

            steps:
              - sequence:
                - name: finalDf
                  sql: SELECT *, date_format (now(), 'yyyyMMddHHmm') AS version, current_timestamp() AS ts_city FROM input

            outputs:
              - name: finalDf
                dataset: dataos://mongodb02:tmdc/city_03?acl=rw
                format: mongodb
                options:
                  saveMode: append
                  connectionProps:
                    ssl: "true"
                    retryWrites: "true"
                    w: "majority"

```