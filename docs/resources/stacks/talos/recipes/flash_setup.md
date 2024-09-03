# Setting up Talos for Flash

## Pre-requisites

- Flash set up
- Docker initialization

## Steps

1. Create a repository, open the repository with a code editor (VS Code), and create a `config.yaml` manifest file and copy the below code. Update the name, description, version, dataos context, Flash as type, and Flash name.
    
    ```yaml
    name: flash
    description: A talos-flash app
    version: 0.1.6
    auth:
      heimdallUrl: https://liberal-donkey.dataos.app/heimdall
    logLevel: 'DEBUG'
    sources:
      - name: flash # profile name
        type: flash
        flashName: 'public:flash-service'
    ```
    
2. In the same repository, create `docker-compose.YAML` manifest file, copy the below-provided code, and update the `volumes` path `/home/iamgroot/Desktop/talos-examples/lens` with the actual path of your repository, add your dataos username and dataos API key in `DATAOS_RUN_AS_USER` and `DATAOS_RUN_AS_APIKEY` respectively.
    
    ```yaml
    version: "2.2"
    services:
      talos:
        image: rubiklabs/talos:0.1.6
        ports:
          - "3000:3000"
        volumes:
          - /home/iamgroot/Desktop/talos-examples/flash:/etc/dataos/work
        environment:
          DATAOS_RUN_AS_USER: 
          DATAOS_RUN_AS_APIKEY: 
          DATAOS_FQDN: liberal-donkey.dataos.app
        tty: true
    ```
    
3. Create a new file `Makefile` in the same repository, and copy the below code.
    
    ```makefile
    start:
    	docker-compose -f docker-compose.yaml up -d
    
    stop:
    	docker-compose -f docker-compose.yaml down -v
    ```
    
4. Create a folder named `apis` inside the same repository, inside `apis` create the files `customer.sql` which will contain the SQL query, and `customer.yaml` to define the path to access sales data in your API as shown below. 
    
    ```sql
    SELECT * FROM mycustomer LIMIT 20
    ```
    
    ```yaml
    urlPath: /flash/customers
    description: list customers from customer table
    source: flash
    ```
    
5. Run `docker-compose up` on the terminal. The output should look like the following:
    - output
        
        ```bash
        docker-compose up
        [+] Running 1/0
         ✔ Container depot-postgres-talos-1  Created                                                                                                                                                                  0.0s 
        Attaching to depot-postgres-talos-1
        depot-postgres-talos-1  | 👉 /etc/dataos/work/config.yaml => {
        depot-postgres-talos-1  |   "name": "postgres_domain",
        depot-postgres-talos-1  |   "description": "A talos-depot-postgres app",
        depot-postgres-talos-1  |   "version": "0.1.6",
        depot-postgres-talos-1  |   "auth": {
        depot-postgres-talos-1  |     "heimdallUrl": "https://liberal-donkey.dataos.app/heimdall"
        depot-postgres-talos-1  |   },
        depot-postgres-talos-1  |   "logLevel": "DEBUG",
        depot-postgres-talos-1  |   "sources": [
        depot-postgres-talos-1  |     {
        depot-postgres-talos-1  |       "name": "postgre01",
        depot-postgres-talos-1  |       "type": "depot"
        depot-postgres-talos-1  |     }
        depot-postgres-talos-1  |   ],
        depot-postgres-talos-1  |   "schemaPath": "",
        depot-postgres-talos-1  |   "cachePath": "tmp"
        depot-postgres-talos-1  | }
        depot-postgres-talos-1  | Get Depot Service Depot Fetch URL:  https://liberal-donkey.dataos.app/ds/api/v2/depots/postgre01
        depot-postgres-talos-1  | Get Depot Service Secrets Fetch URL:  https://liberal-donkey.dataos.app/ds/api/v2/secrets/postgre01_r
        depot-postgres-talos-1  | 🧑‍🤝‍🧑 sources => [
        depot-postgres-talos-1  |   {
        depot-postgres-talos-1  |     "name": "postgre01",
        depot-postgres-talos-1  |     "type": "pg",
        depot-postgres-talos-1  |     "connection": {
        depot-postgres-talos-1  |       "host": "usr-db-dataos-ck-vgji-liberaldo-dev.postgres.database.azure.com",
        depot-postgres-talos-1  |       "port": 5432,
        depot-postgres-talos-1  |       "database": "postgres",
        depot-postgres-talos-1  |       "user": "--REDACTED--",
        depot-postgres-talos-1  |       "password": "--REDACTED--"
        depot-postgres-talos-1  |     }
        depot-postgres-talos-1  |   }
        depot-postgres-talos-1  | ]
        depot-postgres-talos-1  | - Building project...
        depot-postgres-talos-1  | 2024-07-24 10:56:22.626  
        depot-postgres-talos-1  | DEBUG [BUILD]
        depot-postgres-talos-1  | Initializing data source: mock
        depot-postgres-talos-1  | 2024-07-24 10:56:22.627  
        depot-postgres-talos-1  | DEBUG [BUILD] Data source mock initialized
        depot-postgres-talos-1  | 2024-07-24 10:56:22.628  
        depot-postgres-talos-1  | DEBUG [BUILD] Initializing data source: bq
        depot-postgres-talos-1  | 2024-07-24 10:56:22.628  
        depot-postgres-talos-1  | DEBUG [BUILD] Data source bq initialized
        depot-postgres-talos-1  | 
        depot-postgres-talos-1  | 2024-07-24 10:56:22.629  DEBUG
        depot-postgres-talos-1  | [BUILD] Initializing data source: clickhouse
        depot-postgres-talos-1  | 2024-07-24 10:56:22.629  
        depot-postgres-talos-1  | DEBUG [BUILD] Data source clickhouse initialized
        depot-postgres-talos-1  | 
        depot-postgres-talos-1  | 2024-07-24 10:56:22.630  DEBUG [BUILD] Initializing data source: duckdb
        depot-postgres-talos-1  | 2024-07-24 10:56:22.636  DEBUG
        depot-postgres-talos-1  | [CORE] Create connection for talos.cache
        depot-postgres-talos-1  | 2024-07-24 10:56:22.637  
        depot-postgres-talos-1  | DEBUG [CORE] Open database in automatic mode
        depot-postgres-talos-1  | 2024-07-24 10:56:22.650  
        depot-postgres-talos-1  | DEBUG
        depot-postgres-talos-1  | [CORE] Installed httpfs extension
        depot-postgres-talos-1  | 2024-07-24 10:56:22.653  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: access_mode = automatic
        depot-postgres-talos-1  | 2024-07-24 10:56:22.653  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: allow_persistent_secrets = true
        depot-postgres-talos-1  | 2024-07-24 10:56:22.654  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: checkpoint_threshold = 16.0 MiB
        depot-postgres-talos-1  | 2024-07-24 10:56:22.654  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: debug_checkpoint_abort = none
        depot-postgres-talos-1  | 2024-07-24 10:56:22.654  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: storage_compatibility_version = v0.10.2
        depot-postgres-talos-1  | 2024-07-24 10:56:22.654  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: debug_force_external = false
        depot-postgres-talos-1  | 2024-07-24 10:56:22.655  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: debug_force_no_cross_product = false
        depot-postgres-talos-1  | 2024-07-24 10:56:22.655  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: debug_asof_iejoin = false
        depot-postgres-talos-1  | 2024-07-24 10:56:22.655  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: prefer_range_joins = false
        depot-postgres-talos-1  | 2024-07-24 10:56:22.655  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: debug_window_mode = NULL
        depot-postgres-talos-1  | 2024-07-24 10:56:22.656  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: default_collation =
        depot-postgres-talos-1  | 2024-07-24 10:56:22.656  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: default_order = asc
        depot-postgres-talos-1  | 2024-07-24 10:56:22.656  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: default_null_order = nulls_last
        depot-postgres-talos-1  | 2024-07-24 10:56:22.656  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: disabled_filesystems =
        depot-postgres-talos-1  | 2024-07-24 10:56:22.656  
        depot-postgres-talos-1  | DEBUG [CORE] Duckdb config: disabled_optimizers =  
        depot-postgres-talos-1  | 2024-07-24 10:56:22.657  DEBUG [CORE] Duckdb config: enable_external_access = true
        depot-postgres-talos-1  | 
        
        ```