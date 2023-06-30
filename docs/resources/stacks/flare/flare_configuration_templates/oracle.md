# Oracle

## Read Config

```yaml
version: v1
name: read-write-oracle-a02
type: workflow
tags:
  - Connect
  - City
description: The job ingests city data from dropzone into raw zone
workflow:
  title: Connect City
  dag:
    - name: read-oracle-a02
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
                dataset: dataos://sanityoraclealok01:dev/oracle_write
                options:
                  driver: oracle.jdbc.driver.OracleDriver
            logLevel: INFO
            outputs:
              - name: cities
                dataset: dataos://icebase:sanity/sanity_read_oracle?acl=rw
                format: iceberg
                options:
                  saveMode: append
            steps:
              - sequence:
                - name: cities
                  doc: Pick all columns from cities and add version as yyyyMMddHHmm formatted
                    timestamp.
                  sql: SELECT * FROM city_connect LIMIT 100
```

## Write Config

```yaml
version: v1
name: write-oracle-01
type: workflow
tags:
  - Connect
  - City
description: The job ingests city data from dropzone into raw zone
workflow:
  title: Connect City
  dag:
    - name: write-oracle-01
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
                dataset: dataos://sanityoraclealok01:dev/oracle_write?acl=rw
                driver: oracle.jdbc.driver.OracleDriver
                format: jdbc
                description: City data ingested from external csv
                options:
                  saveMode: overwrite
                isStream: false
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