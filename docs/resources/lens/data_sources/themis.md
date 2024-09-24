# Themis

## Prerequisites

While migrating to Themis the following aspects need to be considered:

- Themis Cluster name
- Themis Depot name

### Docker Compose Yaml

```yaml hl_lines="15-18"
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-donkey.dataos.app

  # Overview
  LENS2_NAME: redshiftlens
  LENS2_DESCRIPTION: Description 
  LENS2_TAGS: Provide tags
  LENS2_AUTHORS: creator of lens
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  
  # Data Source
  LENS2_SOURCE_TYPE: themis  #minerva, depot
  LENS2_SOURCE_NAME: lenstestingthemis  #cluster name
  LENS2_SOURCE_CATALOG_NAME: icebase   #depot name, specify any catalog
  DATAOS_RUN_AS_APIKEY: ***** #dataos apikey
  
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
    image: rubiklabs/lens2:0.35.55-01 
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
- Step 3: Fill the values for the atttributes/fields declared in the manifest file as per the Themis source.

**Required Themis Depot Source Attributes**

```yaml
LENS2_SOURCE_TYPE: themis  #minerva, depot
LENS2_SOURCE_NAME: lenstestingthemis  #cluster name
LENS2_SOURCE_CATALOG_NAME: icebase   #depot name, specify any catalog
DATAOS_RUN_AS_APIKEY: ***** #dataos apikey
```
<aside class="callout">
🗣 Within the Themis and Minerva cluster, all depots (such as Icebase, Redshift, Snowflake, etc.) are integrated. When configuring Lens, you only need to specify one depot in the `catalog` field, as Lens can connect to and utilize depots from all sources available in the Themis cluster.
</aside>

## Connecting to Themis without Depot/Cluster 

### **Prerequisites**

- The host for the Themis database server.
- The username for the DataOS User
- The name of the database to use with the Themis query engine database server

## `.env` Configuration 

Add the following environment variables to your Lens (.env) file

=== "Syntax"

    ```yaml
    # Themis query engine configuration
    LENS2_DB_TYPE=themis
    LENS2_DB_HOST=tcp.${DATAOS_FQDN}
    LENS2_DB_PORT=${PORT_NUMBER}
    LENS2_DB_USER=${DATAOS_USER_NAME}
    LENS2_DB_PASS=${DATAOS_WRAP_TOKEN}
    LENS2_DB_PRESTO_CATALOG=${CATALOG_NAME}
    LENS2_DB_SSL=${ENABLE_SSL}

    ```

=== "Sample"

    ```yaml
    # Themis query engine configuration
    LENS2_DB_TYPE=themis
    LENS2_DB_HOST=tcp.alpha-omega.dataos.app
    LENS2_DB_PORT=7432
    LENS2_DB_USER=iamgroot
    LENS2_DB_PASS="abcdefghijklmopqrstuvwyzabcdefghijklmopqrstuvwxyz"
    LENS2_DB_PRESTO_CATALOG=icebase
    LENS2_DB_SSL=true
    ```

**Sample environment variable file configuration**
    
```yaml
LENS2_VERSION=0.34.60-10-scratch2
LENS2_CACHE_VERSION=0.34.60-amd64v8

# source
LENS2_DB_HOST=tcp.alpha-omega.dataos.app
LENS2_DB_PORT=7432
LENS2_DB_USER=iamgroot
LENS2_DB_PASS=mypassword
LENS2_DB_PRESTO_CATALOG=adventureworks
LENS2_DB_SSL=true
LENS2_DB_TYPE=themis

LENS2_NAME=themislens
LENS2_DESCRIPTION="Ecommerce use case on sales data"
LENS2_TAGS="lens2, ecom, sales and customer insights"
LENS2_AUTHORS="iamgroot, thor"
LENS2_LOG_LEVEL=trace
LENS2_LOADER_LOG_LEVEL=debug

LENS2_HEIMDALL_BASE_URL="https://alpha-omega.dataos.app/heimdall"

LENS2_SCHEDULED_REFRESH_DEFAULT="false"
LENS2_API_SECRET=1245ABDJSJDIR56

CACHE_TELEMETRY=false
CACHE_LOG_LEVEL=error
LENS2_BOARD_PATH=boards
LENS2_BASE_URL="http://localhost:4000/lens2/api"
LENS2_META_PATH="/v2/meta"
LENS2_RILL_PATH=boards
LENS2_CHECKS_PATH=checks

DATAOS_USER_APIKEY="abcdefghijklmnopqrstuvwxyz"
DATAOS_USER_NAME="iamgroot"

LENS2_LOCAL_PG_DB_NAME=db
LENS2_LOCAL_PG_HOST=localhost
LENS2_LOCAL_PG_PORT=15432
LENS2_LOCAL_PG_PASSWORD="abcdefghijklmnopqrstuvwxyz"
LENS2_LOCAL_PG_USER=iamgroot
```
    
### **Environment variables Attributes**

| **Environment Variable** | **Description** | **Possible Values** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| `LENS2_DB_TYPE` | The type of database to connect to | themis | themis | ✅ |
| `LENS2_DB_HOST` | The host URL for the database | A valid database host URL of the form `tcp.${DATAOS-FQDN}` where `${DATAOS-FQDN}` is the placeholder for DataOS’ fully qualified domain name. Replace the placeholder with your respective domain name. | `tcp.alpha-omega.dataos.app` | ✅ |
| `LENS2_DB_PORT` | The port for the database connection | A valid port number | `7432` | ❌ |
| `LENS2_DB_USER` | The DataOS user-id used to connect to the database. It can be retrieved from the second column of the output by running the `dataos-ctl user get` command from the DataOS CLI | A valid DataOS user-id | `iamgroot` | ✅ |
| `LENS2_DB_PASS` | The DataOS Wrap Token that serves as a password used to connect to the database | A valid Cluster Wrap Token. Learn more about how to create a Cluster Wrap Token [**here.**](/interfaces/atlas/bi_tools/tableau/#generate-dataos-api-token) | `abcdefghijklmnopqrstuvwxyz` | ✅ |
| `LENS2_DB_PRESTO_CATALOG` | The catalog within Themis to connect to | A valid catalog name  | `icebase` | ✅ |
| `LENS2_DB_SSL` | If `true`, enable SSL encryption for database connections from Lens2. | `true`, `false` | `true` | ❌ |
| `LENS2_CONCURRENCY` | The number of concurrent connections each queue has to the database. Default is `2` | 3,4 | `2` |  |
| `LENS2_DB_MAX_POOL` | The maximum number of concurrent database connections to pool. Default is `8` | 9,10 |   `8` |  |

## Check Query Stats for Themis

<aside class="callout">
💡 Please ensure you have the required permission to access the Operations.
</aside>

To check the query statistics, please follow the steps below:

1. **Access the Themis Cluster**

    Navigate to the Themis cluster. You should see a screen similar to the image below:

  <div style="text-align: center;">
    <img src="/resources/lens/data_sources/Themis/Untitled(7).png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
  </div>

2. **Select the Running Driver**
    
  Choose the running driver. **This driver will always be the same, regardless of the user, as queries will be directed to the creator of the Themis cluster**. The running driver remains consistent for all users.
  
  <div style="text-align: center;">
      <img src="/resources/lens/data_sources/Themis/Untitled(9).png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
  </div>


3. **View the Spark UI**
    
  Go to terminal and use the following command to view the spark UI :
    

```yaml
dataos-ctl -t cluster -w public -n themislens --node themis-themislens-iamgroot-default-a650032d-ad6b-4668-b2d2-cd372579020a-driver view sparkui

**dataos-ctl -t cluster -w public -n themis_cluster_name --node  driver_name view sparkui**
```

You should see the following interface:

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/Themis/Untitled(9).png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

