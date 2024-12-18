# Postgres

## Prerequisites

While creating Lens on Postgres Depot the following aspects need to be considered:

- SQL dialect should be changed to the Postgres one.
- The table naming should be of the format: `schema.table`.

## Deployment manifest file

The below manifest is intended for source type depot named `postgresdepot`, created on the postgres source.


```yaml hl_lines="13-16"
version: v1alpha
name: "postgres-lens"
layer: user
type: lens
tags:
  - lens
description: postgres depot lens deployment on lens2
lens:
  compute: runnable-default
  secrets:
    - name: bitbucket-cred
      allKeys: true
  source:
    type: depot #minerva/themis/depot
    name: postgresdepot
    catalog: icebase
  repo:
    url: https://bitbucket.org/tmdc/sample
    lensBaseDir: sample/lens/source/depot/postgres/model 
    # secretId: lens2_bitbucket_r
    syncFlags:
      - --ref=main #repo-name

  api:   # optional
    replicas: 1 # optional
    logLevel: info  # optional
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_DEV_MODE: "true"
      LENS2_CONCURRENCY: 10
      LENS2_DB_MAX_POOL: 15
      LENS2_DB_TIMEOUT: 1500000
      
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 2000m
        memory: 2048Mi
  worker: # optional
    replicas: 2 # optional
    logLevel: debug  # optional
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_DEV_MODE: "true"


    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
  router: # optional
    logLevel: info  # optional
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_DEV_MODE: "true"
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
  iris:
    logLevel: info  
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
```

## Docker compose manifest file

<details>

  <summary>Docker compose manifest file for local testing</summary>

```yaml hl_lines="14-16"
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-monkey.dataos.app
  # Overview
  LENS2_NAME: sales360
  LENS2_DESCRIPTION: "Ecommerce use case on Adventureworks sales data"
  LENS2_TAGS: "lens2, ecom, sales and customer insights"
  LENS2_AUTHORS: "iamgroot, iamloki"
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  # Data Source
  LENS2_SOURCE_TYPE: depot
  LENS2_SOURCE_NAME: postgreslens2
  DATAOS_RUN_AS_APIKEY: bGVuc3NzLmUzMDA1ZjMzLTZiZjAtNDY4My05ZjhhLWNhODliZTFhZWJhMQ==
  LENS2_DB_SSL : "true"
  # Log
  LENS2_LOG_LEVEL: error
  CACHE_LOG_LEVEL: "trace"
  # Operation
  LENS2_DEV_MODE: true
  LENS2_DEV_MODE_PLAYGROUND: false
  LENS2_REFRESH_WORKER: true
  LENS2_SCHEMA_PATH: model
  LENS2_PG_SQL_PORT: 5432
  CACHE_DATA_DIR: "/var/work/.store"
  NODE_ENV: production
  LENS2_ALLOW_UNGROUPED_WITHOUT_PRIMARY_KEY: "true"
services:
  api:
    restart: always
    image: rubiklabs/lens2:0.35.41-05
    ports:
      - 4000:4000
      - 25432:5432
      - 13306:13306
    environment:
      <<: *lens2-environment   
    volumes:
      - ./model:/etc/dataos/work/model
```

</details>


<!-- Follow these steps to create the `docker-compose.yml`:

- Step 1: Create a `docker-compose.yml` manifest file.
- Step 2: Copy the template from above and paste it in a code.
- Step 3: Fill the values for the atttributes/fields declared in the manifest file as per the Postgres source.



**Required Postgres Depot Source Attributes**

```yaml
LENS2_SOURCE_TYPE: depot
LENS2_SOURCE_NAME: postgreslens2
DATAOS_RUN_AS_APIKEY: bGVuc3NzLmUzMDA1ZjMzLTZiZjAtNDY4My05ZjhhLWNhODliZTFhZWJhMQ==
LENS2_DB_SSL : "true"
```
 -->
