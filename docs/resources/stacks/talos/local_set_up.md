# How to set up Talos Locally?
This section involves setp-by-step guide to set up Talos on your local enviroment. 

## Pre-requisite

- Make sure you have initialized the Docker.
- Extract the [zip](/resources/stacks/talos/talos.zip).
    

## Steps

1. Create a Depot of type BigQuery, below is the sample manifest file of BigQuery Depot.
    
    ```yaml
    name: crmbq
    version: v1
    type: depot
    tags:
      - dropzone
      - bigquery
      - dataos:type:resource
      - dataos:type:cluster-resource
      - dataos:resource:depot
      - dataos:layer:user
    owner: iamgroot
    layer: user
    depot:
      name: crmbq
      type: BIGQUERY
      owner: iamgroot
      description: Google Cloud BigQuery
      connectionSecret:
        - type: key-value-properties
          acl: rw
          data:
            crmbq: '**********************************'
            crmbq_gcp-demo-write-sa.json: '***************************************************'
        - type: key-value-properties
          acl: r
          data:
            crmbq: '********************************************************'
            crmbq_gcp-demo-write-sa.json: '************************************************'
      external: true
      resources:
        requests:
          cpu: 100m
          memory: 550Mi
        limits:
          cpu: 1000m
          memory: 1500Mi
      runAsUser: iamgroot
      spec:
        project: dataos-ck-trs-yak-dev
    ```
    
    To know more about the Depot, please refer to this.
    
2. Apply the Depot manifest file by executing the following command:
    
    ```bash
    dataos-ctl resource apply -f ${{path/manifest.yaml}}
    ```
    
    <aside class="callout">
    🗣 Before moving into the next steps make sure that your Depot is active.
    
    </aside>
    
3. Open the talos repository with a code editor (VS Code), navigate to `config.yaml` manifest file and update the name, description, version, dataos context, Depot name, and Depot type.
    
    ```yaml
    name: postgres_city
    description: A talos-depot-postgres app
    version: 0.1.6
    auth:
      heimdallUrl: https://<<dataos-context>>/heimdall
    logLevel: 'DEBUG'
    sources:
      - name: crmbq # depot name
        type: depot 
    ```
    
4. Navigate to `docker-compose.yaml` manifest file and update the `volumes` path `/home/Desktop/talos/depot-postgres` with the actual path of your repository, add your dataos username and dataos API key in `DATAOS_RUN_AS_USER` and `DATAOS_RUN_AS_APIKEY` respectively.
    
    ```yaml
    version: "2.2"
    services:
      talos:
        image: rubiklabs/talos:0.1.6
        ports:
          - "3000:3000"
        volumes:
          - /home/Desktop/talos-examples/depot/depot-bigquery:/etc/dataos/work
        environment:
          DATAOS_RUN_AS_USER: shraddhaade
          DATAOS_RUN_AS_APIKEY: dG9rZW5fYWRtaXR0ZWRseV9uYXR1cmFsbHlfZW5hYmxpbmdfb3J5eC5lODg2MjIyZC05NDMwLTQ4MWEtYjU3MC01YTJiZWY5MjI5OGE=
          DATAOS_FQDN: liberal-donkey.dataos.app
        tty: true
    ```
    
6. Navigate to `apis` folder create two files, one with `.sql` and one with `.yaml` extension for example create two file one can be `table1.sql` and another one can be `table1.yaml` as shown below.
    
    ```sql
    SELECT first_name, last_name FROM demo.customer_profiles LIMIT 10;
    ```
    
    ```yaml
    urlPath: /customer
    description: customer list
    source: crmbq
    ```
    
7. Now run `docker-compose up` on the terminal. The output should look like the following:
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
        
8. Now you are ready to fetch your data using your DataOS API key. On your browser copy the below link by updating the path and API key with your actual DataOS API key:
    
    ```
    http://localhost:3000/api/customer?apikey=dG9rZW5fYWRt9uYXR1cmFsbHlfZgfhgu567rgdffC5lODg2MjIyZC05NDMwLTQ4MWEtYjU3MC01YTJiZWY5MjI5OGE=
    ```
    
    Successful execution will look like the following:
    
    <div style="text-align: center;">
    <img src="/resources/stacks/talos/image3.png" style="border:1px solid black; width: 80%; height: auto;">
    </div>
