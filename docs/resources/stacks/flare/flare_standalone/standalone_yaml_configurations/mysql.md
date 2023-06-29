# MySQL


## Read Config

**Input Section Configuration for Reading from MySQL Data Source**

```yaml
inputs:
  - name: transactions_connect
    inputType: jdbc
    jdbc:
      url: jdbc:mysql://<mysql-host-address>/<database>
      username: <username>
      password: <password>
      driver: com.mysql.cj.jdbc.Driver
      table: <table-name>
```

**Sample YAML for Reading from MySQL Data Source**

```yaml
version: v1
name: standalone-read-mysql
type: workflow
tags:
  - standalone
  - readJob
  - mysql
description: Sample job
workflow:
  dag:
    - name: customer
      title: Sample Transaction Data Ingester
      description: The job ingests customer data from mysql to iceberg
      spec:
        tags:
          - standalone
          - readJob
          - mysql
        stack: flare:3.0
        compute: runnable-default
        tier: connect
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from MySQL
              - name: transactions_connect
                inputType: jdbc
                jdbc:
                  url: jdbc:mysql://<ip>:<port>/<database>
                  username: <username>
                  password: <password>
                  table: cityTable
                  options:
                    driver: com.mysql.cj.jdbc.Driver

            outputs: # Write to Local
              - name: finalDf
                outputType: file
                file:
                  format: iceberg
                  warehousePath: /data/examples/dataout/localmysql/
                  schemaName: default
                  tableName: trans_oms_data3
                  options:
                    saveMode: append

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM transactions_connect
```

## Write Config

**Output Section Configuration for Writing to MySQL Data Source**

```yaml
outputs:
  - name: finalDf
    outputType: jdbc
    jdbc:
      url: jdbc:mysql://<mysql-host-address>/<database>
      username: <username>
      password: <password>
      driver: com.mysql.cj.jdbc.Driver
      table: cityTable
```

**Sample YAML for Writing to MySQL Data Source**

```yaml
version: v1
name: standalone-write-mysql
type: workflow
tags:
  - standalone
  - writeJob
  - mysql
title: Write to mysql in standalone mode
description: |
  The purpose of this workflow is to write to mysql
workflow:
  dag:
    - name: standalone-mysql-write
      title: Write to mysql in standalone mode
      description: |
        The purpose of this job is to write to mysql
      spec:
        tags:
          - standalone
          - writeJob
          - mysql
        stack: flare:3.0
        compute: runnable-default

        flare:
          job:
            explain: true
            logLevel: INFO
            inputs:
              - name: city
                inputType: file
                file:
                  path: /data/examples/default/city
                  format: csv

            outputs:
              - name: finalDf
                outputType: jdbc
                jdbc:
                  url: jdbc:mysql://<ip>:<port>/<database>
                  username: <username>
                  password: <password>
                  driver: com.mysql.cj.jdbc.Driver
                  table: <table-name>

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city LIMIT 10
```
