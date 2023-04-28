# **Snowflake**

# **Read Config**

**Input Section Configuration for Reading from Snowflake Data Source**

```yaml
inputs:
  - name: city_connect
    inputType: snowflake
    snowflake:
      url: <snowflake-host-address>
      database: <database> # make sure database exist
      table: <table/dataset>
      schema: <schema/collection> # make sure schema exist
      snowflakeWarehouse: <warehousename> # make sure warehouse is running
				# in Snowflake otherwise your job will fail to submit the query
      user: <username>
      password: <password>
```


> 🗣️ You can provide either `token`, `pemPrivateKey`, or `password` to access data from snowflake.


**Sample YAML for Reading from Snowflake Data Source**

```yaml
version: v1
name: standalone-read-snowflake
type: workflow
tags:
  - standalone
  - readJob
  - snowflake
description: The job ingests city data from any snowflake to file
workflow:
  title: Connect City
  dag:
    - name: city-s3-write-01
      title: Sample Transaction Data Ingester
      description: The job ingests city data from snowflake to file
      spec:
        tags:
          - standalone
          - readJob
          - snowflake
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from Snowflake
              - name: city_connect
                inputType: snowflake
                snowflake:
                  url: <snowflake-host-address>
                  database: <database>
                  table: <table/dataset>
                  schema: <schema/collection>
                  snowflakeWarehouse: <warehousename> 
                  user: <username>
                  password: <password>

            outputs: # Write to Snowflake
              - name: finalDf
                outputType: file
                file:
                  path: /data/examples/dataout/citydata
                  format: json

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect
```

# **Write Config**

**Output Section Configuration for Writing to Snowflake Data Source**

```yaml
outputs:
  - name: finalDf
    outputType: snowflake
    snowflake:
      url: <snowflake-host-address>
      database: <database> # make sure database exist
      table: <table/dataset> 
      schema: <schema/collection> # make sure schema exist
      warehouse: <warehouse> # make sure warehouse is running
			# in Snowflake otherwise your job will fail to submit the query
      user: <username>
      password: <password
```

> 🗣️ You can provide either `token`, `pemPrivateKey`, or `password` to access data from snowflake.


**Sample YAML for Writing to Snowflake Data Source**

```yaml
version: v1
name: standalone-write-snowflake
type: workflow
tags:
  - standalone
  - writeJob
  - snowflake
description: The job ingests city data from file to snowflake
workflow:
  title: Connect City
  dag:
    - name: standalone-snowflake-write
      title: Sample Transaction Data Ingester
      description: The job ingests city data from file to snowflake
      spec:
        tags:
          - standalone
          - writeJob
          - snowflake
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from Local
              - name: city_connect
                inputType: file
                file:
                  path: /data/examples/default/city
                  format: csv

            outputs: # Write to Snowflake
              - name: finalDf
                outputType: snowflake
                snowflake:
                  url: <snowflake-host-address>
                  database: <database>
                  table: <table/dataset>
                  schema: <schema/collection>
                  warehouse: <warehouse> 
                  user: <username>
                  password: <password>

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect
```