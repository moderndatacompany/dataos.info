# Postgres

## Read Config

**Input Section Configuration for Reading from Postgres Data Source**

```yaml
inputs:
  - name: transactions_connect
    inputType: jdbc
    jdbc:
      url: jdbc:postgresql://<postgres-host-address>/<database>
      username: <username>
      password: <password>
      driver: org.postgresql.Driver
      table: <table-name>
```

**Sample YAML for Reading from Postgres Data Source**

```yaml
version: v1
name: standalone-read-postgres
type: workflow
tags:
  - standalone
  - readJob
  - postgres
description: Sample job
workflow:
  dag:
    - name: customer
      title: Sample Transaction Data Ingester
      description: The job ingests customer data from postgres source to file
      spec:
        tags:
          - standalone
          - readJob
          - postgres
        stack: flare:3.0
        compute: runnable-default
        tier: connect
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from Postgres
              - name: transactions_connect
                inputType: jdbc
                jdbc:
                  url: jdbc:postgresql://<ip>:<port>/<database>
                  username: <username>
                  password: <password>
                  table: transactionTable1234
                  options:
                    driver: org.postgresql.Driver

            outputs: # Write to Local
              - name: finalDf
                outputType: file
                file:
                  format: iceberg
                  warehousePath: /data/examples/dataout/localPostgres/
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

**Output Section Configuration for Writing to Postgres Data Source**

```yaml
outputs:
  - name: finalDf
    outputType: jdbc
    jdbc:
      url: jdbc:postgresql://<postgres-host-address>/<database>
      username: <username>
      password: <password>
      driver: org.postgresql.Driver
      table: <table-name>
```

**Sample YAML for Writing to Postgres Data Source**

```yaml
version: v1
name: standalone-write-postgres
type: workflow
tags:
  - Pulsar
  - Iceberg
description: Sample job
workflow:
  dag:
    - name: standalone-postgres-write
      title: Sample Transaction Data Ingester
      description: The job ingests customer data from file source to postgres
      spec:
        tags:
          - Postgres
          - Standalone
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
                  path: /data/examples/default/city
                  format: csv
                  isStream: false

            outputs: # Write to Postgres
              - name: finalDf
                outputType: jdbc
                jdbc:
                  url: jdbc:postgresql://<ip>:<port>/<database>
                  username: <username>
                  password: <password>
                  driver: org.postgresql.Driver
                  table: <table-name>

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM transactions_connect limit 10
```