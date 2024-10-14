# Bigquery

## Connecting to Bigquery with Depot/Cluster

### **Prerequisites**

While migrating to Bigquery the following aspects need to be considered:

- SQL dialect should be changed to the Bigquery one
- The table naming should be of the following format `project_id.dataset.table` 
- Do not use `VARCHAR` as a datatype
- Use `Extract` date function of the Bigquery

### **Docker Compose Manifest File**

Ensure that the necessary attributes are highlighted in the Docker Compose Manifest file for proper configuration during the connection setup process.

```yaml hl_lines="13-15"
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-donkey.dataos.app
  # Overview
  LENS2_NAME: sales360
  LENS2_DESCRIPTION: "Ecommerce use case on Adventureworks sales data"
  LENS2_TAGS: "lens2, ecom, sales and customer insights"
  LENS2_AUTHORS: "rakeshvishvakarma, shubhanshu"
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  # Data Source
  LENS2_SOURCE_TYPE: ${depot}
  LENS2_SOURCE_NAME: ${yakdevbq}
  DATAOS_RUN_AS_APIKEY: ${bGVuc3NzLmUzMDA1ZjMzLTZiZjAtNDY4My05ZjhhLWNhODliZTFhZWJhMQ==}
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
      # - ./scripts/commons.js:/app/scripts/commons.js
      # - ./scripts/bootstrap.js:/app/scripts/bootstrap.js
      # - ./scripts/config.js:/app/scripts/config.js
```
**Required Bigquery Depot Source Attributes**

```yaml 
# Data Source
LENS2_SOURCE_TYPE: ${depot}
LENS2_SOURCE_NAME: ${yakdevbq}
DATAOS_RUN_AS_APIKEY: ${bGVuc3NzLmUzMDA1ZjMzLTZiZjAtNDY4My05ZjhhLWNhODliZTFhZWJhMQ==}
```

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