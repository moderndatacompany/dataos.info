# MS-SQL

## Read Config

```yaml
version: v1
name: cnt-city-demo-mssql-read-01
type: workflow
tags:
  - Connect
  - read
description: Jobs writes data to mssql and reads from it
workflow:
  title: Read MSSQL
  dag:
    - name: city-mysql-read
      title: Reading data and writing to dataos
      description: This job writes data to dataos
      spec:
        tags:
          - Connect
          - read
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: city_connect
                dataset: dataos://sanitymssqlalok01:dbo/city01
                format: jdbc
                options:
                  driver: com.microsoft.sqlserver.jdbc.SQLServerDriver
            logLevel: INFO
            outputs:
              - name: cities
                dataset: dataos://icebase:sanity/sanity_mysql?acl=rw
                format: iceberg
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadatacompression-codec: gzip
                description: City data ingested from external csv
                title: City Source Data

            steps:
              - sequence:
                - name: cities
                  sql: SELECT * FROM city_connect

```

## Write Config

```yaml
---
version: v1
name: cnt-city-demo-mssql-01
type: workflow
tags:
  - Connect
  - City
description: The job ingests city data from dropzone into raw zone
workflow:
  title: Connect City
  dag:
    - name: city-mssql-01
      title: City Dimension Ingester
      description: The job ingests city data from dropzone into raw zone
      spec:
        tags:
          - Connect
          - City
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: city_connect
                dataset: dataos://thirdparty01:none/city
                format: csv
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
            logLevel: INFO
            outputs:
              - name: cities
                dataset: dataos://sanitymssqlalok01:dbo/city01?acl=rw
                driver: com.microsoft.sqlserver.jdbc.SQLServerDriver
                format: jdbc
                description: City data ingested from external csv
                options:
                  saveMode: overwrite
                tags:
                  - Connect
                  - City
                title: City Source Data
            steps:
              - sequence:
                  - name: cities
                    doc: Pick all columns from cities and add version as yyyyMMddHHmm formatted
                      timestamp.
                    sql: SELECT * FROM city_connect
```