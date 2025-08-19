---
title: Attributes of Docker Compose manifest
search:
  exclude: true
---



# Attributes of Docker Compose manifest

## Structure of docker-compose manifest

```yaml
 version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-donkey.dataos.app
  # Overview
  LENS2_NAME: lens-audit
  LENS2_DESCRIPTION: "Ecommerce use case on Lens2 audit data"
  LENS2_TAGS: "lens2"
  LENS2_AUTHORS: "iamgroot"
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"

  # Data Source
  LENS2_SOURCE_TYPE: minerva
  LENS2_SOURCE_NAME: system
  LENS2_SOURCE_CATALOG_NAME: icebase
  DATAOS_RUN_AS_APIKEY: bGVuc21lItYTVmYi05MjE4YWRiMDY2YmE=

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
    image: rubiklabs/lens2:0.35.55-06
    ports:
      - 4000:4000
      - 25432:5432
      - 13306:13306
    environment:
      <<: *lens2-environment   
    volumes:
      - ./model:/etc/dataos/work/model
```

# Configuration

### **`version`**

**Description:** The version of the Docker Compose file format.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | "2.2" |

**Example usage:**

```yaml
version: "2.2"
```

---

### **`x-lens2-environment`**

**Description:** Environment variables for the Lens.

**Example usage:**

```yaml
x-lens2-environment: &lens2-environment
  DATAOS_BASE_URL: <https://set-walleye.dataos.app/>
  LENS2_NAME: lens-testing
  LENS2_DESCRIPTION: "Ecommerce use case on Adventureworks sales data"
  LENS2_TAGS: "lens2, ecom, sales and customer insights"
  LENS2_AUTHORS: "iamgroot, ironman"
  LENS2_DB_HOST: tcp.set-walleye.dataos.app
  LENS2_DB_PORT: 7432
  LENS2_DB_USER: iamgroot
  LENS2_DB_PASS: "eyJ0b2tlbiI6IlpHVjJhV05sWDJWMlpXNTBjeTR3WkRjNE1USTNaQzFoTURKaUxUUmpZamt0WWpZek9DMDBZamMwTTJFME16WXlZekU9IiwgImNsdXN0ZXIiOiJzeXN0ZW0ifQo="
  LENS2_DB_PRESTO_CATALOG: icebase
  LENS2_DB_SSL: true
  LENS2_DB_TYPE: trino
  LENS2_LOG_LEVEL: error
  CACHE_LOG_LEVEL: "error"
  LENS2_DEV_MODE: true
  LENS2_REFRESH_WORKER: true
  LENS2_SCHEMA_PATH: model
  LENS2_PG_SQL_PORT: 5432
  CACHE_DATA_DIR: "/var/work/.store"

```

**Fields:**

- **DATAOS_BASE_URL:** Base URL for DataOS.
- **LENS2_NAME:** Name of the Lens instance.
- **LENS2_DESCRIPTION:** Description of the Lens use case.
- **LENS2_TAGS:** Tags related to the Lens instance.
- **LENS2_AUTHORS:** Authors of the Lens instance.
- **LENS2_DB_HOST:** Database host for Lens.
- **LENS2_DB_PORT:** Database port for Lens.
- **LENS2_DB_USER:** Database user for Lens.
- **LENS2_DB_PASS:** Database password for Lens (encoded).
- **LENS2_DB_PRESTO_CATALOG:** Presto catalog for Lens.
- **LENS2_DB_SSL:** SSL usage for Lens database connection.
- **LENS2_DB_TYPE:** Type of database for Lens.
- **LENS2_LOG_LEVEL:** Log level for Lens.
- **CACHE_LOG_LEVEL:** Log level for cache.
- **LENS2_DEV_MODE:** Development mode toggle for Lens.
- **LENS2_REFRESH_WORKER:** Refresh worker toggle for Lens.
- **LENS2_SCHEMA_PATH:** Schema path for Lens.
- **LENS2_PG_SQL_PORT:** PostgreSQL port for Lens.
- **CACHE_DATA_DIR:** Data directory for Lens.

---

# Services section configuration

### **`api`**

API service configuration for the Lens.

**Example usage:**

```yaml
services:
  api:
    restart: always
    image: rubiklabs/lens2:0.35.55-01 
    ports:
      - 4000:4000
      - 25432:5432
    environment:
      <<: *lens2-environment
    volumes:
      - ./model:/etc/dataos/work/model
```

**Fields:**

**restart** 

**Description:** Restart policy for the API service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**       |
| ------------- | --------------- | ----------------- | ------------------------- |
| string        | optional        | none              | always, on-failure, no    |

**Example Usage** 

```yaml
restart: always
```

**image** 

**Description:** Docker image for the API service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**       |
| ------------- | --------------- | ----------------- | ------------------------- |
| string        | optional        | none              | always, on-failure, no    |

**Example Usage:** 

```yaml
image: rubiklabs/lens2:0.35.55-01 
```

**ports**

**Description:**  Ports mapping for the API service.

| **Data Type**      | **Requirement** | **Default Value** | **Possible Values**     |
| ------------------ | --------------- | ----------------- | ----------------------- |
| list of strings    | optional        | none              | any valid port mapping  |

**Example Usage:**
      
```yaml
ports:
  - 4000:4000
  - 25432:5432
```
        
**environment**

**Description:** Environment variables for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                |
| ------------- | --------------- | ----------------- | ---------------------------------- |
| map            | optional        | none              | any valid environment variables    |

**Example Usage:**
        
```yaml
environment:
  <<: *lens2-environment
```
        
**volumes** Volume mappings for the API service.

**Description:** The volume mappings for the API service.

| **Data Type**     | **Requirement** | **Default Value** | **Possible Values**        |
| ----------------- | --------------- | ----------------- | --------------------------- |
| list of strings   | optional        | none              | any valid volume mapping    |

**Example Usage:**
        
```yaml
volumes:
  - ./model:/etc/dataos/work/model

```