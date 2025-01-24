# Connecting to Bigquery Depot

## Prerequisites

While creating a Lens on bigquery depot, the following aspects need to be considered:

- SQL dialect should be changed to the Bigquery one.
- The table naming should be of the following format `project_id.dataset.table`.
- Do not use `VARCHAR` as a datatype.
- Use `Extract` date function of the Bigquery.

## Deployment manifest file

The below manifest is intended for source type depot named `bigquerydepot`, created on the bigquery source.

```yaml hl_lines="13-16"
version: v1alpha
name: "bigquery-lens"
layer: user
type: lens
tags:
  - lens
description: bigquery depot lens deployment on lens2
lens:
  compute: runnable-default
  secrets:
    - name: bitbucket-cred
      allKeys: true
  source:
    type: depot # source type is depot here
    name: bigquerydepot # name of the bigquery depot

  repo:
    url: https://bitbucket.org/tmdc/sample
    lensBaseDir: sample/lens/source/depot/bigquery/model 
    # secretId: lens2_bitbucket_r
    syncFlags:
      - --ref=lens

  api:   # optional
    replicas: 1 # optional
    logLevel: info  # optional
      
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

    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
  router: # optional
    logLevel: info  # optional
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

**Required Bigquery Depot Source Attributes**

```yaml 
# Data Source
LENS2_SOURCE_TYPE: ${depot}  #source type should be depot
LENS2_SOURCE_NAME: ${bigquerydepot} # name of the bigquery depot (it could be anything)
```

## Docker compose manifest file

Ensure that the necessary attributes are highlighted in the Docker Compose Manifest file for proper configuration during the connection setup process.


<details>

  <summary>Docker compose manifest file for local testing</summary>

```yaml hl_lines="13-15"
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-monkey.dataos.app
  # Overview
  LENS2_NAME: sales360
  LENS2_DESCRIPTION: "Ecommerce use case on Adventureworks sales data"
  LENS2_TAGS: "lens2, ecom, sales and customer insights"
  LENS2_AUTHORS: "rakeshvishvakarma, shubhanshu"
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  # Data Source
  LENS2_SOURCE_TYPE: ${depot} #source name - depot
  LENS2_SOURCE_NAME: ${bigquerydepot} #name of the bigquery depot
  DATAOS_RUN_AS_APIKEY: ${A1ZjMDliZTFhZWJhMQ==}
  # LogZjAtNDY4My05
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
      # - ./scripts/commons.js:/app/scripts/commons.js
      # - ./scripts/bootstrap.js:/app/scripts/bootstrap.js
      # - ./scripts/config.js:/app/scripts/config.js
```

</details>



<!-- 
## Connecting to Bigquery without Depot/Cluster

### **Prerequisites**

In order to connect Google BigQuery to Lens, you need to provide service account credentials. Lens2 requires the service account to have **BigQuery Data Viewer** and **BigQuery Job User** roles enabled. You can learn more about acquiring Google BigQuery credentials [here](https://cloud.google.com/docs/authentication/getting-started).


- The [Google Cloud Project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin) for the BigQuery project.
- A set of [Google Cloud service credentials](https://support.google.com/a/answer/7378726?hl=en) which [allow access](https://cloud.google.com/docs/authentication/getting-started) to the BigQuery project
- The [Google Cloud region](https://cloud.google.com/bigquery/docs/locations#regional-locations) for the BigQuery project

Syntax with example is written below:

=== "Syntax"

    ```yaml
    # Bigquery configuration
    LENS2_DB_TYPE=bigquery
    LENS2_DB_BQ_PROJECT_ID=${BIGQUERY_PROJECT_ID}
    LENS2_DB_BQ_KEY_FILE=${BIGQUERY_KEY_FILE_PATH}
    ```

=== "Sample"

    ```yaml
    # Bigquery configuration
    LENS2_DB_TYPE=bigquery
    LENS2_DB_BQ_PROJECT_ID=my-bigquery-project-123456
    LENS2_DB_BQ_KEY_FILE=/path/to/my/keyfile.json
    ```
**Sample manifest file**

```yaml
LENS2_VERSION=0.34.60-13
LENS2_CACHE_VERSION=0.34.60-amd64v8

LENS2_LOG_LEVEL=error
LENS2_LOADER_LOG_LEVEL=debug

LENS2_HEIMDALL_BASE_URL="https://alpha-omega.dataos.app/heimdall"

LENS2_SCHEDULED_REFRESH_DEFAULT="false"
LENS2_API_SECRET=28487985729875987397AHFUHUD

CACHE_TELEMETRY="false"
CACHE_LOG_LEVEL=error

# Bigquery configuration
LENS2_DB_TYPE=bigquery
LENS2_DB_BQ_PROJECT_ID=my-bigquery-project-123456
LENS2_DB_BQ_KEY_FILE=/path/to/my/keyfile.json

 #Lens Configs
LENS2_NAME=bq_lens
LENS2_DESCRIPTION=lens description
LENS2_TAGS='lens2 tags (comma separated)'
LENS2_AUTHORS='lens2 auther names (comma separated)'

LENS2_BASE_URL=http://localhost:4000/lens2
LENS2_META_PATH=/v2/meta
LENS2_DATAOS_USER_NAME=USERNAME
LENS2_DATAOS_USER_APIKEY=APIKEY
LENS2_RILL_PATH=rill
LENS2_CHECKS_PATH=checks
```

### Environment variables

| **Environment Variable** | **Description** | **Possible Values** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| `LENS2_DB_TYPE` | The type of database | bigquery | bigquery | ✅ |
| `LENS2_DB_BQ_PROJECT_ID` | The Google BigQuery project ID to connect to | A valid Google BigQuery Project ID | my-bigquery-project-123456 | ✅ |
| `LENS2_DB_BQ_KEY_FILE` | The path to a JSON key file for connecting to Google BigQuery | A valid Google BigQuery JSON key file | /path/to/my/keyfile.json | ✅ | -->