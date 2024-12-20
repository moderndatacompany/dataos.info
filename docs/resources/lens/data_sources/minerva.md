# Minerva

## Connecting to Minerva using Depot/Cluster 

### **Prerequisites**

While migrating to Minerva the following aspects need to be considered:

- The source name should be Minerva.
- The name of the cluster created on Minerva source.
- The name of the Depot.


### **Deployment manifest file**

```yaml hl_lines="13-16"
version: v1alpha
name: "minervalens"
layer: user
type: lens
tags:
  - lens
description: minerva deployment on lens2
lens:
  compute: runnable-default
  secrets:
    - name: bitbucket-cred
      allKeys: true
  source:
    type: minerva #minerva/themis/depot
    name: minervacluster  #name of minerva cluster
    catalog: icebase
  repo:
    url: https://bitbucket.org/tmdc/sample
    lensBaseDir: sample/lens/source/minerva/model 
    # secretId: lens2_bitbucket_r
    syncFlags:
      - --ref=lens

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

The above YAML manifest is intended for a cluster named `minervacluster`, created on the minerva source, with the data catalog named `icebase`. To use this manifest file, copy the file and update the source details accordingly.

<aside class="callout">
🗣️ Within the Themis and Minerva cluster, all depots (such as Icebase, Redshift, Snowflake, etc.) are integrated. When configuring Lens, you only need to specify one depot in the `catalog` field, as Lens can connect to and utilize depots from all sources available in the Themis cluster.
</aside>


### **Docker compose manifest file**

<details>

  <summary>Docker compose manifest file for local testing</summary>

```yaml
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-monkey.dataos.app

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
    image: rubiklabs/lens2:0.35.60-20
    ports:
      - 4000:4000
      - 25432:5432
      - 13306:13306
    environment:
      <<: *lens2-environment   
    volumes:
      - ./model:/etc/dataos/work/model
```
<!-- 
</details>

Follow these steps to create the `docker-compose.yml`:

- Step 1: Create a `docker-compose.yml` manifest file.
- Step 2: Copy the template from above and paste it in a code.
- Step 3: Fill the values for the atttributes/fields declared in the manifest file as per the Minerva source.

**Required Minerva Depot source attributes**

```yaml
LENS2_SOURCE_TYPE: minerva  #themis, depot
LENS2_SOURCE_NAME: minervacluster  #cluster name
LENS2_SOURCE_CATALOG_NAME: icebase   #depot name, specify any catalog
DATAOS_RUN_AS_APIKEY: *****
``` -->

## Connecting to Minerva without Depot/Cluster 

<aside class="callout">
🗣️ When deploying Lens in DataOS, you need to connect to the source via the depot/cluster. The below configs are best suited for testing Locally. Otherwise, it is recommended that you connect via depot/cluster.
</aside>

### **Prerequisites**

- The hostname for the Trino database server.
- The username for the DataOS User.
- The name of the database to use with the Minerva query engine database server.

### **`.env` Configuration**

Add the following environment variables to your Lens (.env) file

=== "Syntax"

    ```yaml
    # Trino configuration
    LENS2_DB_TYPE=trino
    LENS2_DB_HOST=tcp.${DATAOS_FQDN}
    LENS2_DB_USER=${DATAOS_USER_NAME}
    LENS2_DB_PASS=${DATAOS_WRAP_TOKEN}
    LENS2_DB_PRESTO_CATALOG=${CATALOG_NAME}
    LENS2_DB_PORT=${PORT_NUMBER}
    ```
=== "Sample"

    ```yaml
    # Trino configuration
    LENS2_DB_TYPE=trino
    LENS2_DB_HOST="tcp.alpha-omega.dataos.app"
    LENS2_DB_USER="iamgroot"
    LENS2_DB_PASS="abcdefghijklmnopqrstuvwxyz"
    LENS2_DB_PRESTO_CATALOG="icebase"
    LENS2_DB_PORT=7432
    ```
**Sample environment variable file configuration**
    
```yaml
LENS2_VERSION=0.35.55-01 

# Minerva configuration
LENS2_DB_HOST=tcp.alpha-omega.dataos.app
LENS2_DB_PORT=7432
LENS2_DB_USER=iamgroot
LENS2_DB_PASS="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwzyz"
LENS2_DB_PRESTO_CATALOG=icebase
LENS2_DB_SSL=true
LENS2_DB_TYPE=trino

# Meta information
LENS2_NAME=trinolens # fetch from CLI
LENS2_DESCRIPTION="Trino lens generated"
LENS2_TAGS="lens2, sales, customer insights"
LENS2_AUTHORS="iamgroot"

LENS2_DEV_MODE="true"
LENS2_SCHEMA_PATH=model

LENS2_LOG_LEVEL="error"
LENS2_LOADER_LOG_LEVEL="error"
CACHE_LOG_LEVEL="error" # not there in Kishan's

DATAOS_FQDN=alpha-omega.dataos.app
DATAOS_USER_NAME=iamgroot
DATAOS_USER_APIKEY=abcdeghijklmopqrstuvwxyz

LENS2_DEPOT_SERVICE_URL="https://alpha-omega.dataos.app/ds" 
LENS2_HEIMDALL_BASE_URL="https://alpa-omega.dataos.app/heimdall" 

LENS2_SOURCE_TYPE=trino
LENS2_SOURCE_NAME=system
LENS2_SOURCE_CATALOG_NAME=icebase 

LENS2_BASE_URL="http://localhost:4000/lens2/api"
LENS2_META_PATH="/v2/meta"
LENS2_RILL_PATH=boards
LENS2_CHECKS_PATH=checks
LENS2_BOARD_PATH=boards
```

### **Environment variables Attributes**

| **Environment Variable** | **Description** | **Possible Values** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| `LENS2_DB_TYPE` | The type of database | trino | trino | ✅ |
| `LENS2_DB_HOST` | The host URL for the database | A valid database host URL of the form `tcp.${DATAOS-FQDN}` where `${DATAOS-FQDN}` is the placeholder for DataOS’ fully qualified domain name. Replace the placeholder with your respective domain name. | `tcp.alpha-omega.dataos.app` | ✅ |
| `LENS2_DB_PORT` | The port for the database connection | A valid port number | `7432` | ❌ |
| `LENS2_DB_USER` | The DataOS user-id used to connect to the database. It can be retrieved from the second column of the output by running the `dataos-ctl user get` command from the DataOS CLI | A valid DataOS user-id | `iamgroot` | ✅ |
| `LENS2_DB_PASS` | The DataOS Wrap Token that serves as a password used to connect to the database | A valid Cluster Wrap Token. Learn more about how to create a Cluster Wrap Token [**here.**](https://dataos.info/interfaces/atlas/bi_tools/tableau/#generate-dataos-api-token) | `abcdefghijklmnopqrstuvwxyz` | ✅ |
| `LENS2_DB_PRESTO_CATALOG` | The catalog within Trino/Presto to connect to | A valid catalog name within the Trino/Presto database | `icebase` | ✅ |
| `LENS2_DB_SSL` | If `true`, enables SSL encryption for database connections from Lens2. | `true`, `false` | `true` | ❌ |

### **Example**

[trino.zip](/resources/lens/data_sources/trino/trino.zip)

## Check Query Stats for Minerva

<aside class="callout">
💡 Please ensure you have the required permission to access the Operations.
</aside>

To check the query statistics, please follow the steps below:

1. **Access Minerva Queries**
    
  Navigate to the operation section, then go to Minerva queries. Set the filters as follows:
    
    - Source: `lens2`
    - Dialect: `trino_sql`
    - You can also filter by cluster, username, and other criteria as per your choice.

    <div style="text-align: center;">
        <img src="/resources/lens/data_sources/minerva/Untitled1.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
    </div>

2. **Select the Query ID**
      
    Choose the query ID you are interested in. You will then be able to check the statistics, as shown in the example below:
      
    <div style="text-align: center;">
        <img src="/resources/lens/data_sources/minerva/Untitled1.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
    </div>
