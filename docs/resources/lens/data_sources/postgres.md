# AWS Redshift

## Prerequisites

While migrating to Postgres the following aspects need to be considered:

- SQL dialect should be changed to the Postgres one
- The table naming should be of the following format `schema.table`


### **Docker Compose Manifest file**

The highlighted attributes are all the required attributes.

```yaml hl_lines="14-16"
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-donkey.dataos.app
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
Follow these steps to create the `docker-compose.yml`:

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

