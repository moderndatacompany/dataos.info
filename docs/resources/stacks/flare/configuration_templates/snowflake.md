# Snowflake Depots

To read/write data on the Snowflake data source, you first need to create a depot on top of it. In case you haven’t created a Snowflake Depot navigate to the below link

## Read Config

Once you have set up a Snowflake Depot, you can start reading data from it. 

```yaml
version: v1
name: connect-snowflake-read-write-02
type: workflow
tags:
  - Connect
  - read
  - write
description: Jobs writes data to snowflake and reads from it
workflow:
  title: Connect Snowflake
  dag:
    - name: read-snowflake-01
      title: Reading data and writing to snowflake
      description: This job writes data to wnowflake
      spec:
        tags:
          - Connect
          - write
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
             - name: city_connect
               dataset: dataos://snowflake01:public/CITY01
               format: snowflake
               options:
                sfWarehouse: WAREHOUSE
            logLevel: INFO
            outputs:
              - name: cities
                dataset: dataos://icebase:sample/city_from_snowflake_01?acl=rw
                format: Iceberg
                description: City data ingested from bigquery
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                tags:
                  - Connect
                title: City Source Data
            steps:
              - sequence:
                - name: cities
                  sql: SELECT * FROM city_connect
    - name: tool-city-snrksh
      spec:
      stack: toolbox
      compute: runnable-default
      toolbox:
        dataset: dataos://icebase:sample/city_snowflake?acl=rw
        action:
          name: set_version
          value: latest
```

## Write Config

```yaml
version: v1
name: connect-snowflake-read-write-02
type: workflow
tags:
  - Connect
  - read
  - write
description: Jobs writes data to snowflake and reads from it
workflow:
  title: Connect Snowflake
  dag:
    - name: write-snowflake-02
      title: Reading data and writing to snowflake
      description: This job writes data to wnowflake
      spec:
        tags:
          - Connect
          - write
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
              - name: city_connect
                dataset: dataos://snowflake01:public/city02?acl=rw
                format: Snowflake
                options:
                  extraOptions:
                    sfWarehouse: WAREHOUSE
                description: City data ingested from external csv
                title: City Source Data
```