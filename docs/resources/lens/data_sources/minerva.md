# Minerva

## Prerequisites

While migrating to Themis the following aspects need to be considered:

- Minerva cluster
- Depot name

### Docker Compose Yaml

```yaml
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-donkey.dataos.app

  # Overview
  LENS2_NAME: minervalens
  LENS2_DESCRIPTION: Description 
  LENS2_TAGS: Provide tags
  LENS2_AUTHORS: creator of lens
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  
  # Data Source
  LENS2_SOURCE_TYPE: minerva  #themis, depot
  LENS2_SOURCE_NAME: minervacluster  #cluster name
  LENS2_SOURCE_CATALOG_NAME: icebase   #depot name, specify any catalog
  DATAOS_RUN_AS_APIKEY: *****
  
  #LENS2_DB_SSL: true
  #MINERVA_TCP_HOST: tcp.liberal-donkey.dataos.app
  
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
    image: rubiklabs/lens2:0.35.41-02
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
- Step 3: Fill the values for the atttributes/fields declared in the manifest file as per the Minerva source.

**Required Minerva Depot Source Attributes**

```yaml
LENS2_SOURCE_TYPE: minerva  #themis, depot
LENS2_SOURCE_NAME: minervacluster  #cluster name
LENS2_SOURCE_CATALOG_NAME: icebase   #depot name, specify any catalog
DATAOS_RUN_AS_APIKEY: *****
```

<aside class="callout">
🗣 Within the Themis and Minerva cluster, all depots (such as Icebase, Redshift, Snowflake, etc.) are integrated. When configuring Lens, you only need to specify one depot in the `catalog` field, as Lens can connect to and utilize depots from all sources available in the Themis cluster.
</aside>

## Check Query Stats for Minerva

<aside class="callout">
💡  Please ensure you have the required permission to access the Operations.

</aside>

To check the query statistics, please follow the steps below:

1. **Access Minerva Queries**
    
  Navigate to the operation section, then go to Minerva queries. Set the filters as follows:
  
  - Source: `lens2`
  - Dialect: `trino_sql`
  - You can also filter by cluster, username, and other criteria as per your choice.

  <div style="text-align: center;">
      <img src="docs/resources/lens/data_sources/minerva/Untitled1.png" alt="Untitled" style="max-width: 100%; height: auto; border: 1px solid #000;">
  </div>

2. **Select the Query ID**
    
  Choose the query ID you are interested in. You will then be able to check the statistics, as shown in the example below:
    
  <div style="text-align: center;">
      <img src="docs/resources/lens/data_sources/minerva/Untitled1.png" alt="Untitled" style="max-width: 100%; height: auto; border: 1px solid #000;">
  </div>
