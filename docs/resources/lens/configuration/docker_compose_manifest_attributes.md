# Structure of docker-compose manifest

```yaml
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_BASE_URL: https://glad-rattler.dataos.app/
  # Overview
  LENS2_NAME: sales360
  LENS2_DESCRIPTION: "Ecommerce use case on Adventureworks sales data"
  LENS2_TAGS: "lens2, ecom, sales and customer insights"
  LENS2_AUTHORS: "rakeshvishvakarma, shubhanshu"
  # Data Source
  LENS2_DB_HOST: tcp.glad-rattler.dataos.app
  LENS2_DB_PORT: 7432
  LENS2_DB_USER: shubhanshujain
  LENS2_DB_PASS: "eyJ0b2tlbiI6ImJHVnVjeTQwTjJGa1ptTmxZUzB5TVRobUxUUTNZamt0WWpWalppMWlNbVJpTVdZME1tVmhaVFk9IiwiY2x1c3RlciI6InN5c3RlbSJ9Cg=="
  LENS2_DB_PRESTO_CATALOG: icebase
  LENS2_DB_SSL: true
  LENS2_DB_TYPE: trino  
  # Log
  LENS2_LOG_LEVEL: error
  CACHE_LOG_LEVEL: "error"
  # Operation
  LENS2_DEV_MODE: true   
  LENS2_REFRESH_WORKER: true
  LENS2_SCHEMA_PATH: model
  LENS2_PG_SQL_PORT: 5432
  CUBESTORE_DATA_DIR: "/var/work/.store"

services:
  api:
    restart: always
    image: rubiklabs/lens2:0.35.18-4
    ports:
      - 4000:4000
      - 25432:5432
    environment:
      <<: *lens2-environment   
    volumes:
      - ./model:/etc/dataos/work/model
      # - ./config.js:/etc/dataos/work/config.js
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

**Description:** Environment variables for the Lens2 application.

**Example usage:**

```yaml
x-lens2-environment: &lens2-environment
  DATAOS_BASE_URL: <https://set-walleye.dataos.app/>
  LENS2_NAME: lenovo
  LENS2_DESCRIPTION: "Ecommerce use case on Adventureworks sales data"
  LENS2_TAGS: "lens2, ecom, sales and customer insights"
  LENS2_AUTHORS: "rakeshvishvakarma, shubhanshu"
  LENS2_DB_HOST: tcp.set-walleye.dataos.app
  LENS2_DB_PORT: 7432
  LENS2_DB_USER: mansisingh
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
  CUBESTORE_DATA_DIR: "/var/work/.store"

```

**Fields:**

- **DATAOS_BASE_URL:** Base URL for DataOS.
- **LENS2_NAME:** Name of the Lens2 application.
- **LENS2_DESCRIPTION:** Description of the Lens2 use case.
- **LENS2_TAGS:** Tags related to the Lens2 application.
- **LENS2_AUTHORS:** Authors of the Lens2 application.
- **LENS2_DB_HOST:** Database host for Lens2.
- **LENS2_DB_PORT:** Database port for Lens2.
- **LENS2_DB_USER:** Database user for Lens2.
- **LENS2_DB_PASS:** Database password for Lens2 (encoded).
- **LENS2_DB_PRESTO_CATALOG:** Presto catalog for Lens2.
- **LENS2_DB_SSL:** SSL usage for Lens2 database connection.
- **LENS2_DB_TYPE:** Type of database for Lens2.
- **LENS2_LOG_LEVEL:** Log level for Lens2.
- **CACHE_LOG_LEVEL:** Log level for cache.
- **LENS2_DEV_MODE:** Development mode toggle for Lens2.
- **LENS2_REFRESH_WORKER:** Refresh worker toggle for Lens2.
- **LENS2_SCHEMA_PATH:** Schema path for Lens2.
- **LENS2_PG_SQL_PORT:** PostgreSQL port for Lens2.
- **CUBESTORE_DATA_DIR:** Data directory for CubeStore.

---

# Services section configuration

### **`api`**

**Description:** API service configuration for the Lens2 application.

**Example usage:**

```yaml
services:
  api:
    restart: always
    image: rubiklabs/lens2:0.35.18-21
    ports:
      - 4000:4000
      - 25432:5432
    environment:
      <<: *lens2-environment
    volumes:
      - ./model:/etc/dataos/work/model
```

**Fields:**

- **restart:** Restart policy for the API service.

  **Description:** Restart policy for the API service.

  | **Data Type** | **Requirement** | **Default Value** | **Possible Values**       |
  | ------------- | --------------- | ----------------- | ------------------------- |
  | string        | optional        | none              | always, on-failure, no    |

   - **Example Usage:** 

   ```yaml
   restart: always
   ```

- **image:** 

  **Description:** Docker image for the API service.

  | **Data Type** | **Requirement** | **Default Value** | **Possible Values**       |
  | ------------- | --------------- | ----------------- | ------------------------- |
  | string        | optional        | none              | always, on-failure, no    |

  - **Example Usage:** `image: rubiklabs/lens2:0.35.18-21`

- **ports:**

  **Description:**  Ports mapping for the API service.

  | **Data Type**      | **Requirement** | **Default Value** | **Possible Values**     |
  | ------------------ | --------------- | ----------------- | ----------------------- |
  | list of strings    | optional        | none              | any valid port mapping  |

    - **Example Usage:**
        
        ```yaml
        ports:
          - 4000:4000
          - 25432:5432
        ```
        
- **environment:** Environment variables for the API service.

  **Description:** Environment variables for the service

  | **Data Type** | **Requirement** | **Default Value** | **Possible Values**                |
  | ------------- | --------------- | ----------------- | ---------------------------------- |
  | map            | optional        | none              | any valid environment variables    |

    - **Example Usage:**
        
        ```yaml
        environment:
          <<: *lens2-environment
        
        ```
        
- **volumes:** Volume mappings for the API service.

  **Description:** The volume mappings for the system

  | **Data Type**     | **Requirement** | **Default Value** | **Possible Values**        |
  | ----------------- | --------------- | ----------------- | --------------------------- |
  | list of strings   | optional        | none              | any valid volume mapping    |

   - **Example Usage:**
        
      ```yaml
      volumes:
        - ./model:/etc/dataos/work/model
      
      ```