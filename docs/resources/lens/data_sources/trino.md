# Trino

## Connecting to Trino without Depot/Cluster 

### **Prerequisites**

- The hostname for the Trino database server.
- The username for the DataOS User
- The name of the database to use with the Minerva query engine database server

### **Setup**

### **`.env` Configuration Attributes**

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

# Check whether this is even required or not
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
| `LENS2_DB_PASS` | The DataOS Wrap Token that serves as a password used to connect to the database | A valid Cluster Wrap Token. Learn more about how to create a Cluster Wrap Token [**here.**](https://www.notion.so/ac6f155294244807bc2272083f082f60?pvs=21) | `abcdefghijklmnopqrstuvwxyz` | ✅ |
| `LENS2_DB_PRESTO_CATALOG` | The catalog within Trino/Presto to connect to | A valid catalog name within the Trino/Presto database | `icebase` | ✅ |
| `LENS2_DB_SSL` | If `true`, enables SSL encryption for database connections from Lens2. | `true`, `false` | `true` | ❌ |

### **Example**

[trino.zip](/resources/lens/data_sources/trino/trino.zip)