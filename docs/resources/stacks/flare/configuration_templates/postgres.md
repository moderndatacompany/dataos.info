# Postgres

## Read Config

```yaml
version: v1
name: postgres-read-write
type: workflow
tags:
  - bq
  - dataset
description: This job read and write data from to postgres
title: Read Write Postgres
workflow:
  dag:
    - name: read-postgres
      title: Read Postgres
      description: This job read data from postgres
      spec:
        tags:
          - Connect
        stack: flare:3.0
        compute: runnable-default

        flare:
          job:
            explain: true
            inputs:
              - name: input
                dataset: dataos://sanitypostgresalok02:public/postgres_write
                options:
                  driver: org.postgresql.Driver

            logLevel: INFO
            outputs:
              - name: input
                dataset: dataos://icebase:sanity/sanity_postgres?acl=rw
                format: Iceberg
                options:
                  saveMode: overwrite
                description: Data set from blender
                tags:
                  - Connect
                title: Postgres Dataset
```

## Write Config

```yaml
# creds depends upon the env refer to default schema public
# it's an internal service of  dataos which is not exposed publicly so can not be connected with any gui applications
version: v1
name: postgres-read-write
type: workflow
tags:
  - bq
  - dataset
description: This job read and write data from to postgres
title: Read Write Postgres
workflow:
  dag:
    - name: write-postgres
      title: Write Postgres
      description: This job write data from postgres
      spec:
        tags:
          - Connect
        stack: flare:3.0
        compute: runnable-default

        flare:
          job:
            explain: true
            inputs:
              - name: input
                dataset: dataos://thirdparty01:none/city
                format: csv
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
            logLevel: INFO
            outputs:
              - name: input
                dataset: dataos://sanitypostgresalok02:public/postgres_write?acl=rw
                driver: org.postgresql.Driver
                format: jdbc
                options:
                  saveMode: overwrite
                description: Data set from Icebase
                tags:
                  - Connect
                title: Postgres Dataset
```