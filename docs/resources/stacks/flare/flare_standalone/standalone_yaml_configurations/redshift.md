# Redshift


## Read Config

**Input Section Configuration for Reading from Redshift Data Source**

```yaml
inputs:
  - name: oms_transactions_data
    inputType: redshift
    redshift:
      jdbcUrl: jdbc:redshift://<red-shift-host-address>/<database>
      tempDir: s3a://<bucket>/<dir>
      username: <username>
      password: <password>
      dbTable: <table-name>
```

**Sample YAML for Reading from Redshift Data Source**

```yaml
version: v1
name: standalone-red-shift-write
type: workflow
tags:
  - standalone
  - readJob
  - redshift
title: Read from red-shift using standalone mode
description: |
  The purpose of this workflow is to read from Redshift and write to Local.
workflow:
  dag:
    - name: write-redshift-local
      title: Read from red-shift using standalone mode
      description: |
        The purpose of this job is to read from Redshift and write to Local
      spec:
        tags:
          - standalone
          - readJob
          - red-shift
        stack: flare:3.0

        envs: # Environment Variables 
          DISABLE_HADOOP_PATH_CHECKS: true
						# Without these environment variables, the job will fail to establish 
					  # a connection with the Redshift in standalone mode.
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from Redshift
              - name: oms_transactions_data
                inputType: redshift
                redshift:
                  jdbcUrl: jdbc:redshift://<redshift-host-address>/<database>
                  tempDir: s3a://<bucket>/<dir>
                  username: <username>
                  password: <password>
                  dbTable: <table>

            outputs: # Write to Local
              - name: finalDf
                outputType: file
                file:
                  format: iceberg
                  warehousePath: /data/examples/dataout/redshift
                  schemaName: default
                  tableName: trans_oms_data3
                  options:
                    saveMode: append

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM oms_transactions_data LIMIT 10

          sparkConf:
            - 'spark.hadoop.fs.s3a.bucket.<bucket-name>.access.key': '<access-key>'
            - 'spark.hadoop.fs.s3a.bucket.<bucket-name>.secret.key': '<secret-key>'
```

## Write Config

**Output Section Configuration for Writing to Redshift Data Source**

```yaml
outputs:
  - name: finalDf
    outputType: redshift
    redshift:
      jdbcUrl: jdbc:redshift://<redshift-host-address>/<database>
      tempDir: s3a://<bucket>/<dir>
      username: <username>
      password: <password>
      dbTable: <table>
```

**Sample YAML for Writing to Redshift Data Source**

```yaml
version: v1
name: standalone-write-red-shift
type: workflow
tags:
  - standalone
  - writeJob
  - redshift
title: Write to red-shift in standalone mode
description: |
  The purpose of this workflow is to read from local and write to Redshift
workflow:
  dag:
    - name: standalone-redshift-write
      title: Write to red-shift using standalone mode
      description: |
        The purpose of this job is to read from local and write to Redshift
      spec:
        tags:
          - standalone
          - writeJob
          - redshift
        stack: flare:3.0

        envs: # Environment Variables
          DISABLE_HADOOP_PATH_CHECKS: true
					# Without these environment variables, the job will fail to establish 
				  # a connection with the Redshift in standalone mode.

        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from Local
              - name: oms_transactions_data
                inputType: file
                file:
                  path: /data/examples/default/city
                  format: csv

            outputs: # Write to Redshift
              - name: finalDf
                outputType: redshift
                redshift:
                  jdbcUrl: jdbc:redshift://<redshfit-host-address>/<database>
                  tempDir: s3a://<bucket>/<dir>
                  username: <username>
                  password: <password>
                  dbTable: <table-name>

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM oms_transactions_data LIMIT 10

          sparkConf:
            - 'spark.hadoop.fs.s3a.bucket.<bucket-name>.access.key': '<access-key>'
            - 'spark.hadoop.fs.s3a.bucket.<bucket-name>.secret.key': '<secret-key>'
```
