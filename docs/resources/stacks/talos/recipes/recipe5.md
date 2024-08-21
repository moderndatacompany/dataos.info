# Setting up Talos for Postgres

1. Create a repository, open the repository with a code editor (VS Code), and create a `config.yaml` manifest file and copy the below code. Update the name, description, version, dataos context, Depot name, and Depot type.
    
    ```yaml
    name: adventureworks
    description: A talos app
    version: 0.1.6
    logLevel: ERROR
    auth:
        heimdallUrl: https://liberal-donkey.dataos.app/heimdall
        userGroups:
        - name: reader
          description: This is a reader's group
          includes:
            - roles:id:data-dev
            - roles:id:data-guru
          excludes:
            - users:id:iamgroot
        - name: default
          description: Default group to accept everyone
          includes: "*"
    metrics:
      type: summary
      percentiles: [ 0.5, 0.75, 0.95, 0.98, 0.99, 0.999 ]
    rateLimit:
      enabled: true
      options:
        interval:
          min: 1
        max: 100
        delayAfter: 4
    cors:
      enabled: true
      options:
        origin: 'https://google.com'
        allowMethods: 'GET'  
    cachePath: tmp       
    sources:
        - name: pg 
          type: pg
          connection:
            host: pg-db
            port: 5432
            user: postgres
            password: '123456782934'
            database: Adventureworks
    
    ```
    
    Similarly, for other types of the Depot `config.yaml` will be the same, update the source name with your actual Depot name.
    
2. In the same repository, create `docker-compose.yaml` manifest file, copy the below-provided code, and update the `volumes` path `/home/Desktop/talos/depot-postgres` with the actual path of your repository, add your dataos username and dataos API key in `DATAOS_RUN_AS_USER` and `DATAOS_RUN_AS_APIKEY` respectively.
    
    ```yaml
    version: "2.2"
    services:
      pg-db:
        build: ./adventureworks-db
        container_name: adventureworks-db
        environment:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: 123456782934
        ports:
          - "54321:5432"
        networks:
          - app-network
        healthcheck:
          test: [ "CMD-SHELL", "pg_isready -U postgres" ]
          interval: 10s
          timeout: 5s
          retries: 5
    
      talos:
        image: rubiklabs/talos:0.1.6
        ports:
          - "3000:3000"
        volumes:
          - /home/iamgroot/Desktop/talos-examples/postgres:/etc/dataos/work
        environment:
          DATAOS_RUN_AS_USER: iamgroot
          DATAOS_RUN_AS_APIKEY: AQertfgcdcb8757698YUgytdYTUTGTTTFjhoij=
          DATAOS_FQDN: liberal-donkey.dataos.app
        tty: true
        depends_on:
          pg-db:
            condition: service_healthy
        networks:
          - app-network
    
    networks:
      app-network:
        driver: bridge
    ```
    
3. Create a new file `Makefile` in the same repository, and copy the below code.
    
    ```makefile
    start:
    	docker-compose -f docker-compose.yaml up -d
    
    stop:
    	docker-compose -f docker-compose.yaml down -v
    ```
    
4. Create a folder named `apis` inside the same repository create the files `customers.sql` which will contain the SQL query, and `customers.yaml` to define the path to access customer data in your API as shown below. Update your queries, urlPath, description, and source accordingly.
    
    ```sql
    with
      customer_person as (
        SELECT
          cust.customerid,
          cust.personid,
          cust.storeid,
          per.businessentityid,
          per.persontype,
          per.title,
          per.firstname,
          per.middlename,
          per.lastname,
          per.suffix
        FROM
          sales.customer cust
          LEFT JOIN person.person per ON cust.personID = per.businessEntityID
      ),
      customer_address AS (
        SELECT
          b.businessentityid,
          b.addressid,
          ad.name as address_type,
          a.addressline1,
          a.addressline2,
          a.city,
          a.stateprovinceid,
          a.postalcode,
          a.spatiallocation,
          a.stateprovincecode,
          a.countryregioncode,
          a.isonlystateprovinceflag,
          a.state_name,
          a.territoryid,
          a.territory_name,
          a.group
        FROM
          person.businessentityaddress b
          LEFT JOIN (
            SELECT
              a.addressid,
              a.addressline1,
              a.addressline2,
              a.city,
              a.stateprovinceid,
              a.postalcode,
              a.spatiallocation,
              s.stateprovincecode,
              s.countryregioncode,
              s.isonlystateprovinceflag,
              s.name AS state_name,
              s.territoryid,
              s.territory_name,
              s.group
            FROM
              person.address a
              LEFT JOIN (
                select
                  s.stateprovinceid,
                  s.stateprovincecode,
                  s.countryregioncode,
                  s.isonlystateprovinceflag,
                  s.name,
                  s.territoryid,
                  st.name as territory_name,
                  st.group
                from
                  person.stateprovince s
                  left join sales.salesterritory st on s.territoryid = st.territoryid
              ) s ON a.stateprovinceid = s.stateprovinceid
          ) AS a ON b.addressid = a.addressid
          LEFT JOIN person.addresstype ad ON b.addresstypeid = ad.addresstypeid
      ),
      cust_email as (
        select
          e.businessentityid,
          e.emailaddress
        from
          person.emailaddress e
      )
    select
      cp.customerid,
      cp.personid,
      cp.businessentityid,
      cp.persontype,
      cp.storeid,
      cp.title,
      cp.firstname,
      cp.middlename,
      cp.lastname,
      cp.suffix,
      ca.address_type,
      ca.addressline1,
      ca.addressline2,
      ca.city,
      ca.stateprovinceid,
      ca.postalcode,
      ca.spatiallocation,
      ca.stateprovincecode,
      ca.countryregioncode,
      ca.state_name,
      ca.territoryid,
      ca.territory_name,
      ca.group,
      ce.emailaddress
    from
      customer_person cp
      left join customer_address ca on cp.businessentityid = ca.businessentityid
      left join cust_email ce on cp.businessentityid = ce.businessentityid
      {% if context.params.id %}
        where cp.customerid = {{context.params.id}}
      {% endif %}
    
    ```
    
    ```yaml
    urlPath: /customers
    description: Get list of all the customers or one customer
    request : 
      - fieldName : id
        fieldIn: query
    source: pg
    ```
    
5. Run `docker-compose up` on the terminal. The output should look like the following:
    - output
        
        ```bash
        docker-compose up
        [+] Running 1/0
         ✔ Container snow-talos-1  Created                                                                                                0.0s 
        Attaching to snow-talos-1
        snow-talos-1  | 👉 /etc/dataos/work/config.yaml => {
        snow-talos-1  |   "name": "superstore",
        snow-talos-1  |   "description": "A talos snowflake app",
        snow-talos-1  |   "version": "0.1.6",
        snow-talos-1  |   "auth": {
        snow-talos-1  |     "heimdallUrl": "https://liberal-donkey.dataos.app/heimdall"
        snow-talos-1  |   },
        snow-talos-1  |   "logLevel": "DEBUG",
        snow-talos-1  |   "sources": [
        snow-talos-1  |     {
        snow-talos-1  |       "name": "snowflake",
        snow-talos-1  |       "type": "snowflake",
        snow-talos-1  |       "connection": {
        snow-talos-1  |         "account": "dz80249.central-india.azure",
        snow-talos-1  |         "username": "--REDACTED--",
        snow-talos-1  |         "password": "--REDACTED--",
        snow-talos-1  |         "warehouse": "mywarehouse",
        snow-talos-1  |         "database": "mydatabase"
        snow-talos-1  |       }
        snow-talos-1  |     }
        snow-talos-1  |   ],
        snow-talos-1  |   "schemaPath": "",
        snow-talos-1  |   "cachePath": "tmp"
        snow-talos-1  | }
        snow-talos-1  | 🧑‍🤝‍🧑 sources => [
        snow-talos-1  |   {
        snow-talos-1  |     "name": "snowflake",
        snow-talos-1  |     "type": "snowflake",
        snow-talos-1  |     "connection": {
        snow-talos-1  |       "account": "dz80249.central-india.azure",
        snow-talos-1  |       "username": "--REDACTED--",
        snow-talos-1  |       "password": "--REDACTED--",
        snow-talos-1  |       "warehouse": "mywarehouse",
        snow-talos-1  |       "database": "mydatabase"
        snow-talos-1  |     }
        snow-talos-1  |   }
        snow-talos-1  | ]
        snow-talos-1  | - Building project...
        snow-talos-1  | 2024-07-26 10:53:35.241  DEBUG
        snow-talos-1  | [BUILD] Initializing data source: mock
        snow-talos-1  | 2024-07-26 10:53:35.242  
        snow-talos-1  | DEBUG [BUILD] Data source mock initialized
        snow-talos-1  | 
        snow-talos-1  | 2024-07-26 10:53:35.242  DEBUG
        snow-talos-1  | [BUILD] Initializing data source: bq
        snow-talos-1  | 2024-07-26 10:53:35.243  
        snow-talos-1  | DEBUG [BUILD] Data source bq initialized
        snow-talos-1  | 2024-07-26 10:53:35.243  
        snow-talos-1  | DEBUG [BUILD] Initializing data source: clickhouse
        snow-talos-1  | 2024-07-26 10:53:35.243  DEBUG [BUILD] Data source clickhouse initialized
        snow-talos-1  | 
        snow-talos-1  | 2024-07-26 10:53:35.244  
        snow-talos-1  | DEBUG [BUILD] Initializing data source: duckdb
        snow-talos-1  | 2024-07-26 10:53:35.251  DEBUG [CORE] Create connection for talos.cache
        snow-talos-1  | 
        snow-talos-1  | 2024-07-26 10:53:35.252  DEBUG
        snow-talos-1  | [CORE] Open database in automatic mode
        snow-talos-1  | 2024-07-26 10:53:35.262  
        snow-talos-1  | DEBUG [CORE] Installed httpfs extension
        snow-talos-1  | 2024-07-26 10:53:35.265  
        snow-talos-1  | DEBUG [CORE] Duckdb config: access_mode = automatic
        snow-talos-1  | 2024-07-26 10:53:35.265  DEBUG
        snow-talos-1  | [CORE] Duckdb config: allow_persistent_secrets = true
        snow-talos-1  | 2024-07-26 10:53:35.266  DEBUG
        snow-talos-1  | [CORE] Duckdb config: checkpoint_threshold = 16.0 MiB
        snow-talos-1  | 2024-07-26 10:53:35.266  
        snow-talos-1  | DEBUG [CORE] Duckdb config: debug_checkpoint_abort = none
        snow-talos-1  | 2024-07-26 10:53:35.266  
        snow-talos-1  | DEBUG [CORE] Duckdb config: storage_compatibility_version = v0.10.2
        snow-talos-1  | 2024-07-26 10:53:35.267  DEBUG [CORE]
        snow-talos-1  | Duckdb config: debug_force_external = false
        snow-talos-1  | 2024-07-26 10:53:35.267  
        snow-talos-1  | DEBUG [CORE] Duckdb config: debug_force_no_cross_product = false
        snow-talos-1  | 2024-07-26 10:53:35.267  
        snow-talos-1  | DEBUG [CORE] Duckdb config: debug_asof_iejoin = false
        snow-talos-1  | 2024-07-26 10:53:35.267  
        snow-talos-1  | DEBUG [CORE] Duckdb config: prefer_range_joins = false
        snow-talos-1  | 2024-07-26 10:53:35.268  DEBUG [CORE]
        snow-talos-1  | Duckdb config: debug_window_mode = NULL
        snow-talos-1  | 2024-07-26 10:53:35.268  
        snow-talos-1  | DEBUG [CORE] Duckdb config: default_collation =
        snow-talos-1  | 2024-07-26 10:53:35.268  
        snow-talos-1  | DEBUG [CORE] Duckdb config: default_order = asc
        snow-talos-1  | 2024-07-26 10:53:35.268  
        snow-talos-1  | DEBUG [CORE] Duckdb config: default_null_order = nulls_last
        snow-talos-1  | 2024-07-26 10:53:35.269  
        snow-talos-1  | DEBUG [CORE] Duckdb config: disabled_filesystems =
        snow-talos-1  | 2024-07-26 10:53:35.269  
        snow-talos-1  | DEBUG [CORE] Duckdb config: disabled_optimizers =
        snow-talos-1  | 2024-07-26 10:53:35.269  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_external_access = true
        snow-talos-1  | 2024-07-26 10:53:35.269  DEBUG [CORE] Duckdb config: enable_fsst_vectors = false
        snow-talos-1  | 2024-07-26 10:53:35.270  DEBUG [CORE] Duckdb config: allow_unsigned_extensions = false
        snow-talos-1  | 2024-07-26 10:53:35.270  DEBUG [CORE] Duckdb config: allow_community_extensions = true
        snow-talos-1  | 2024-07-26 10:53:35.270  DEBUG [CORE] Duckdb config: allow_extensions_metadata_mismatch = false
        snow-talos-1  | 2024-07-26 10:53:35.271  DEBUG [CORE] Duckdb config: allow_unredacted_secrets = false
        snow-talos-1  | 2024-07-26 10:53:35.271  
        snow-talos-1  | DEBUG [CORE] Duckdb config: custom_extension_repository =
        snow-talos-1  | 2024-07-26 10:53:35.272  
        snow-talos-1  | DEBUG [CORE] Duckdb config: autoinstall_extension_repository =
        snow-talos-1  | 2024-07-26 10:53:35.272  
        snow-talos-1  | DEBUG
        snow-talos-1  | [CORE] Duckdb config: autoinstall_known_extensions = true
        snow-talos-1  | 2024-07-26 10:53:35.273  
        snow-talos-1  | DEBUG [CORE] Duckdb config: autoload_known_extensions = true
        snow-talos-1  | 2024-07-26 10:53:35.273  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_object_cache = false
        snow-talos-1  | 2024-07-26 10:53:35.274  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_http_metadata_cache = false
        snow-talos-1  | 2024-07-26 10:53:35.274  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_profiling = NULL
        snow-talos-1  | 2024-07-26 10:53:35.275  DEBUG [CORE]
        snow-talos-1  | Duckdb config: enable_progress_bar = false
        snow-talos-1  | 2024-07-26 10:53:35.275  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_progress_bar_print = true
        snow-talos-1  | 2024-07-26 10:53:35.276  
        snow-talos-1  | DEBUG [CORE] Duckdb config: errors_as_json = false
        snow-talos-1  | 2024-07-26 10:53:35.276  
        snow-talos-1  | DEBUG [CORE] Duckdb config: explain_output = physical_only
        snow-talos-1  | 2024-07-26 10:53:35.276  
        snow-talos-1  | DEBUG [CORE] Duckdb config: extension_directory =
        snow-talos-1  | 2024-07-26 10:53:35.277  
        snow-talos-1  | DEBUG [CORE] Duckdb config: external_threads = 1
        snow-talos-1  | 2024-07-26 10:53:35.277  
        snow-talos-1  | DEBUG [CORE] Duckdb config: file_search_path =
        snow-talos-1  | 2024-07-26 10:53:35.277  DEBUG [CORE]
        snow-talos-1  | Duckdb config: force_compression = Auto
        snow-talos-1  | 2024-07-26 10:53:35.277  
        snow-talos-1  | DEBUG [CORE] Duckdb config: force_bitpacking_mode = auto
        snow-talos-1  | 2024-07-26 10:53:35.278  
        snow-talos-1  | DEBUG [CORE] Duckdb config: home_directory =
        snow-talos-1  | 2024-07-26 10:53:35.278  
        snow-talos-1  | DEBUG [CORE] Duckdb config: log_query_path = NULL
        snow-talos-1  | 2024-07-26 10:53:35.278  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_macro_dependencies = false
        snow-talos-1  | 2024-07-26 10:53:35.278  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_view_dependencies = false
        snow-talos-1  | 2024-07-26 10:53:35.279  DEBUG [CORE] Duckdb config: lock_configuration = false 
        snow-talos-1  | 2024-07-26 10:53:35.279  DEBUG [CORE] Duckdb config: immediate_transaction_mode = false
        snow-talos-1  | 2024-07-26 10:53:35.279  DEBUG
        snow-talos-1  | [CORE] Duckdb config: integer_division = false
        snow-talos-1  | 2024-07-26 10:53:35.280  
        snow-talos-1  | DEBUG [CORE] Duckdb config: max_expression_depth = 1000
        snow-talos-1  | 2024-07-26 10:53:35.280  
        snow-talos-1  | DEBUG [CORE] Duckdb config: max_memory = 12.3 GiB
        snow-talos-1  | 2024-07-26 10:53:35.280  
        snow-talos-1  | DEBUG [CORE] Duckdb config: max_temp_directory_size = 0 bytes
        snow-talos-1  | 2024-07-26 10:53:35.281  DEBUG
        snow-talos-1  | [CORE] Duckdb config: old_implicit_casting = false 
        snow-talos-1  | 2024-07-26 10:53:35.281  DEBUG
        snow-talos-1  | [CORE] Duckdb config: memory_limit = 12.3 GiB
        snow-talos-1  | 
        snow-talos-1  | 2024-07-26 10:53:35.282  DEBUG [CORE] Duckdb config: null_order = nulls_last
        snow-talos-1  | 2024-07-26 10:53:35.282  
        snow-talos-1  | DEBUG [CORE] Duckdb config: ordered_aggregate_threshold = 262144
        snow-talos-1  | 2024-07-26 10:53:35.282  
        snow-talos-1  | DEBUG [CORE] Duckdb config: password = NULL
        snow-talos-1  | 2024-07-26 10:53:35.283  
        snow-talos-1  | DEBUG [CORE] Duckdb config: perfect_ht_threshold = 12
        snow-talos-1  | 2024-07-26 10:53:35.283  DEBUG
        snow-talos-1  | [CORE] Duckdb config: pivot_filter_threshold = 10
        snow-talos-1  | 2024-07-26 10:53:35.283  
        snow-talos-1  | DEBUG [CORE] Duckdb config: pivot_limit = 100000
        snow-talos-1  | 2024-07-26 10:53:35.283  DEBUG
        snow-talos-1  | [CORE] Duckdb config: preserve_identifier_case = true
        snow-talos-1  | 2024-07-26 10:53:35.284  
        snow-talos-1  | DEBUG [CORE] Duckdb config: preserve_insertion_order = true
        snow-talos-1  | 2024-07-26 10:53:35.284  DEBUG [CORE] Duckdb config: profile_output =
        snow-talos-1  | 
        snow-talos-1  | 2024-07-26 10:53:35.284  
        snow-talos-1  | DEBUG [CORE] Duckdb config: profiling_mode = NULL
        snow-talos-1  | 2024-07-26 10:53:35.284  
        snow-talos-1  | DEBUG [CORE] Duckdb config: profiling_output =
        snow-talos-1  | 2024-07-26 10:53:35.285  DEBUG
        snow-talos-1  | [CORE] Duckdb config: progress_bar_time = 2000
        snow-talos-1  | 2024-07-26 10:53:35.285  
        snow-talos-1  | DEBUG [CORE] Duckdb config: schema = main
        snow-talos-1  | 2024-07-26 10:53:35.285  
        snow-talos-1  | DEBUG [CORE] Duckdb config: search_path =
        snow-talos-1  | 2024-07-26 10:53:35.285  
        snow-talos-1  | DEBUG [CORE] Duckdb config: secret_directory = /root/.duckdb/stored_secrets
        snow-talos-1  | 2024-07-26 10:53:35.286  DEBUG [CORE] Duckdb config: default_secret_storage = local_file
        snow-talos-1  | 2024-07-26 10:53:35.286  DEBUG [CORE] Duckdb config: temp_directory = /etc/dataos/work/talos_cache.db.tmp
        snow-talos-1  | 2024-07-26 10:53:35.286  
        snow-talos-1  | DEBUG [CORE] Duckdb config: threads = 8
        snow-talos-1  | 2024-07-26 10:53:35.286  DEBUG
        snow-talos-1  | [CORE] Duckdb config: username = NULL
        snow-talos-1  | 2024-07-26 10:53:35.287  
        snow-talos-1  | DEBUG [CORE] Duckdb config: arrow_large_buffer_size = false
        snow-talos-1  | 2024-07-26 10:53:35.287  
        snow-talos-1  | DEBUG [CORE] Duckdb config: user = NULL
        snow-talos-1  | 2024-07-26 10:53:35.287  DEBUG [CORE] Duckdb config: wal_autocheckpoint = 16.0 MiB 
        snow-talos-1  | 2024-07-26 10:53:35.287  DEBUG [CORE] Duckdb config: worker_threads = 8 
        snow-talos-1  | 2024-07-26 10:53:35.287  DEBUG [CORE] Duckdb config: allocator_flush_threshold = 128.0 MiB
        snow-talos-1  | 2024-07-26 10:53:35.288  DEBUG [CORE] Duckdb config: duckdb_api = nodejs
        snow-talos-1  | 2024-07-26 10:53:35.288  
        snow-talos-1  | DEBUG [CORE] Duckdb config: custom_user_agent =
        snow-talos-1  | 2024-07-26 10:53:35.288  
        snow-talos-1  | DEBUG [CORE] Duckdb config: partitioned_write_flush_threshold = 524288
        snow-talos-1  | 2024-07-26 10:53:35.288  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_http_logging = false
        snow-talos-1  | 2024-07-26 10:53:35.289  
        snow-talos-1  | DEBUG [CORE] Duckdb config: http_logging_output =
        snow-talos-1  | 2024-07-26 10:53:35.289  DEBUG
        snow-talos-1  | [CORE] Duckdb config: binary_as_string =
        snow-talos-1  | 2024-07-26 10:53:35.289  DEBUG
        snow-talos-1  | [CORE] Duckdb config: Calendar = gregorian
        snow-talos-1  | 2024-07-26 10:53:35.290  DEBUG
        snow-talos-1  | [CORE] Duckdb config: TimeZone = Etc/UTC
        snow-talos-1  | 2024-07-26 10:53:35.291  
        snow-talos-1  | DEBUG [BUILD] Data source duckdb initialized
        snow-talos-1  | 2024-07-26 10:53:35.291  
        snow-talos-1  | DEBUG [BUILD] Initializing data source: pg
        snow-talos-1  | 2024-07-26 10:53:35.292  
        snow-talos-1  | DEBUG [BUILD] Data source pg initialized
        snow-talos-1  | 2024-07-26 10:53:35.293  DEBUG
        snow-talos-1  | [BUILD] Initializing data source: redshift
        snow-talos-1  | 2024-07-26 10:53:35.294  DEBUG
        snow-talos-1  | [BUILD] Data source redshift initialized
        snow-talos-1  | 2024-07-26 10:53:35.295  DEBUG [BUILD] Initializing data source: snowflake
        snow-talos-1  | 
        snow-talos-1  | 2024-07-26 10:53:35.299  DEBUG [CORE]
        snow-talos-1  | Initializing profile: snowflake using snowflake driver
        snow-talos-1  | {"level":"INFO","message":"[10:53:35.306 AM]: Trying to initialize Easy Logging"}
        snow-talos-1  | {"level":"INFO","message":"[10:53:35.320 AM]: No client config file found in default directories"}
        snow-talos-1  | {"level":"INFO","message":"[10:53:35.321 AM]: Easy Logging is disabled as no config has been found"}
        snow-talos-1  | 2024-07-26 10:53:35.942  DEBUG
        snow-talos-1  | [CORE] Profile snowflake initialized
        snow-talos-1  | 2024-07-26 10:53:35.942  DEBUG [BUILD]
        snow-talos-1  | Data source snowflake initialized
        snow-talos-1  | ✔ Built successfully.
        snow-talos-1  | 2024-07-26 10:53:36.385  
        snow-talos-1  | INFO  [CLI] Starting server...
        snow-talos-1  | 2024-07-26 10:53:36.394  DEBUG [SERVE] Initializing data source: mock
        snow-talos-1  | 2024-07-26 10:53:36.394  DEBUG
        snow-talos-1  | [SERVE] Data source mock initialized
        snow-talos-1  | 2024-07-26 10:53:36.394  
        snow-talos-1  | DEBUG [SERVE] Initializing data source: bq
        snow-talos-1  | 2024-07-26 10:53:36.395  
        snow-talos-1  | DEBUG [SERVE] Data source bq initialized
        snow-talos-1  | 2024-07-26 10:53:36.395  
        snow-talos-1  | DEBUG [SERVE] Initializing data source: clickhouse
        snow-talos-1  | 2024-07-26 10:53:36.395  
        snow-talos-1  | DEBUG [SERVE] Data source clickhouse initialized
        snow-talos-1  | 2024-07-26 10:53:36.395  
        snow-talos-1  | DEBUG [SERVE] Initializing data source: duckdb
        snow-talos-1  | 2024-07-26 10:53:36.396  
        snow-talos-1  | DEBUG [CORE] Create connection for talos.cache
        snow-talos-1  | 2024-07-26 10:53:36.396  
        snow-talos-1  | DEBUG [CORE] Open database in automatic mode
        snow-talos-1  | 2024-07-26 10:53:36.405  
        snow-talos-1  | DEBUG [CORE] Installed httpfs extension
        snow-talos-1  | 2024-07-26 10:53:36.407  
        snow-talos-1  | DEBUG [CORE] Duckdb config: access_mode = automatic
        snow-talos-1  | 2024-07-26 10:53:36.407  
        snow-talos-1  | DEBUG [CORE] Duckdb config: allow_persistent_secrets = true
        snow-talos-1  | 2024-07-26 10:53:36.407  
        snow-talos-1  | DEBUG [CORE] Duckdb config: checkpoint_threshold = 16.0 MiB
        snow-talos-1  | 2024-07-26 10:53:36.407  DEBUG
        snow-talos-1  | [CORE] Duckdb config: debug_checkpoint_abort = none
        snow-talos-1  | 2024-07-26 10:53:36.408  DEBUG [CORE]
        snow-talos-1  | Duckdb config: storage_compatibility_version = v0.10.2
        snow-talos-1  | 2024-07-26 10:53:36.408  
        snow-talos-1  | DEBUG [CORE] Duckdb config: debug_force_external = false
        snow-talos-1  | 2024-07-26 10:53:36.408  
        snow-talos-1  | DEBUG [CORE] Duckdb config: debug_force_no_cross_product = false
        snow-talos-1  | 2024-07-26 10:53:36.408  
        snow-talos-1  | DEBUG [CORE] Duckdb config: debug_asof_iejoin = false
        snow-talos-1  | 2024-07-26 10:53:36.409  
        snow-talos-1  | DEBUG [CORE] Duckdb config: prefer_range_joins = false
        snow-talos-1  | 2024-07-26 10:53:36.409  DEBUG
        snow-talos-1  | [CORE] Duckdb config: debug_window_mode = NULL
        snow-talos-1  | 2024-07-26 10:53:36.409  
        snow-talos-1  | DEBUG [CORE] Duckdb config: default_collation =
        snow-talos-1  | 2024-07-26 10:53:36.409  DEBUG [CORE] Duckdb config: default_order = asc
        snow-talos-1  | 2024-07-26 10:53:36.410  
        snow-talos-1  | DEBUG [CORE] Duckdb config: default_null_order = nulls_last
        snow-talos-1  | 2024-07-26 10:53:36.410  
        snow-talos-1  | DEBUG [CORE] Duckdb config: disabled_filesystems =
        snow-talos-1  | 2024-07-26 10:53:36.410  DEBUG [CORE] Duckdb config: disabled_optimizers =
        snow-talos-1  | 2024-07-26 10:53:36.410  DEBUG [CORE] Duckdb config: enable_external_access = true
        snow-talos-1  | 
        snow-talos-1  | 2024-07-26 10:53:36.411  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_fsst_vectors = false
        snow-talos-1  | 2024-07-26 10:53:36.411  DEBUG [CORE] Duckdb config: allow_unsigned_extensions = false
        snow-talos-1  | 2024-07-26 10:53:36.411  DEBUG
        snow-talos-1  | [CORE] Duckdb config: allow_community_extensions = true
        snow-talos-1  | 2024-07-26 10:53:36.412  DEBUG [CORE] Duckdb config: allow_extensions_metadata_mismatch = false
        snow-talos-1  | 2024-07-26 10:53:36.412  DEBUG [CORE] Duckdb config: allow_unredacted_secrets = false
        snow-talos-1  | 2024-07-26 10:53:36.413  DEBUG [CORE] Duckdb config: custom_extension_repository =
        snow-talos-1  | 2024-07-26 10:53:36.414  DEBUG [CORE] Duckdb config: autoinstall_extension_repository =
        snow-talos-1  | 2024-07-26 10:53:36.414  DEBUG [CORE]
        snow-talos-1  | Duckdb config: autoinstall_known_extensions = true
        snow-talos-1  | 2024-07-26 10:53:36.414  DEBUG [CORE] Duckdb config: autoload_known_extensions = true
        snow-talos-1  | 2024-07-26 10:53:36.415  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_object_cache = false 
        snow-talos-1  | 2024-07-26 10:53:36.415  DEBUG [CORE] Duckdb config: enable_http_metadata_cache = false 
        snow-talos-1  | 2024-07-26 10:53:36.415  DEBUG [CORE] Duckdb config: enable_profiling = NULL
        snow-talos-1  | 2024-07-26 10:53:36.415  DEBUG [CORE] Duckdb config: enable_progress_bar = false
        snow-talos-1  | 2024-07-26 10:53:36.416  DEBUG
        snow-talos-1  | [CORE] Duckdb config: enable_progress_bar_print = true
        snow-talos-1  | 2024-07-26 10:53:36.416  DEBUG [CORE]
        snow-talos-1  | Duckdb config: errors_as_json = false
        snow-talos-1  | 2024-07-26 10:53:36.416  DEBUG [CORE] Duckdb config: explain_output = physical_only
        snow-talos-1  | 
        snow-talos-1  | 2024-07-26 10:53:36.416  DEBUG [CORE] Duckdb config: extension_directory =
        snow-talos-1  | 2024-07-26 10:53:36.417  DEBUG
        snow-talos-1  | [CORE] Duckdb config: external_threads = 1
        snow-talos-1  | 2024-07-26 10:53:36.417  DEBUG [CORE]
        snow-talos-1  | Duckdb config: file_search_path =
        snow-talos-1  | 2024-07-26 10:53:36.417  
        snow-talos-1  | DEBUG [CORE] Duckdb config: force_compression = Auto
        snow-talos-1  | 2024-07-26 10:53:36.417  
        snow-talos-1  | DEBUG [CORE] Duckdb config: force_bitpacking_mode = auto
        snow-talos-1  | 2024-07-26 10:53:36.418  
        snow-talos-1  | DEBUG [CORE] Duckdb config: home_directory =
        snow-talos-1  | 2024-07-26 10:53:36.418  
        snow-talos-1  | DEBUG [CORE] Duckdb config: log_query_path = NULL
        snow-talos-1  | 2024-07-26 10:53:36.418  
        snow-talos-1  | 
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_macro_dependencies = false
        snow-talos-1  | 2024-07-26 10:53:36.419  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_view_dependencies = false
        snow-talos-1  | 2024-07-26 10:53:36.419  
        snow-talos-1  | DEBUG [CORE] Duckdb config: lock_configuration = false
        snow-talos-1  | 2024-07-26 10:53:36.419  
        snow-talos-1  | DEBUG [CORE] Duckdb config: immediate_transaction_mode = false
        snow-talos-1  | 2024-07-26 10:53:36.419  
        snow-talos-1  | DEBUG [CORE] Duckdb config: integer_division = false
        snow-talos-1  | 2024-07-26 10:53:36.420  DEBUG
        snow-talos-1  | [CORE] Duckdb config: max_expression_depth = 1000
        snow-talos-1  | 2024-07-26 10:53:36.420  
        snow-talos-1  | DEBUG [CORE] Duckdb config: max_memory = 12.3 GiB
        snow-talos-1  | 2024-07-26 10:53:36.420  
        snow-talos-1  | DEBUG [CORE] Duckdb config: max_temp_directory_size = 0 bytes
        snow-talos-1  | 2024-07-26 10:53:36.421  
        snow-talos-1  | DEBUG [CORE] Duckdb config: old_implicit_casting = false
        snow-talos-1  | 2024-07-26 10:53:36.421  DEBUG [CORE]
        snow-talos-1  | Duckdb config: memory_limit = 12.3 GiB
        snow-talos-1  | 2024-07-26 10:53:36.421  
        snow-talos-1  | DEBUG [CORE] Duckdb config: null_order = nulls_last
        snow-talos-1  | 2024-07-26 10:53:36.421  DEBUG
        snow-talos-1  | [CORE] Duckdb config: ordered_aggregate_threshold = 262144
        snow-talos-1  | 2024-07-26 10:53:36.422  DEBUG [CORE]
        snow-talos-1  | Duckdb config: password = NULL
        snow-talos-1  | 2024-07-26 10:53:36.422  DEBUG [CORE]
        snow-talos-1  | Duckdb config: perfect_ht_threshold = 12
        snow-talos-1  | 
        snow-talos-1  | 2024-07-26 10:53:36.423  
        snow-talos-1  | DEBUG [CORE] Duckdb config: pivot_filter_threshold = 10
        snow-talos-1  | 2024-07-26 10:53:36.423  
        snow-talos-1  | DEBUG [CORE] Duckdb config: pivot_limit = 100000
        snow-talos-1  | 2024-07-26 10:53:36.424  
        snow-talos-1  | DEBUG [CORE] Duckdb config: preserve_identifier_case = true
        snow-talos-1  | 2024-07-26 10:53:36.424  DEBUG [CORE] Duckdb config: preserve_insertion_order = true
        snow-talos-1  | 2024-07-26 10:53:36.425  
        snow-talos-1  | DEBUG [CORE] Duckdb config: profile_output =
        snow-talos-1  | 2024-07-26 10:53:36.426  DEBUG [CORE]
        snow-talos-1  | Duckdb config: profiling_mode = NULL
        snow-talos-1  | 2024-07-26 10:53:36.426  
        snow-talos-1  | DEBUG [CORE] Duckdb config: profiling_output =  
        snow-talos-1  | 2024-07-26 10:53:36.427  DEBUG [CORE] Duckdb config: progress_bar_time = 2000 
        snow-talos-1  | 2024-07-26 10:53:36.427  DEBUG [CORE] Duckdb config: schema = main
        snow-talos-1  | 2024-07-26 10:53:36.428  DEBUG [CORE] Duckdb config: search_path =
        snow-talos-1  | 2024-07-26 10:53:36.428  
        snow-talos-1  | DEBUG [CORE] Duckdb config: secret_directory = /root/.duckdb/stored_secrets
        snow-talos-1  | 2024-07-26 10:53:36.429  
        snow-talos-1  | DEBUG [CORE] Duckdb config: default_secret_storage = local_file
        snow-talos-1  | 2024-07-26 10:53:36.430  DEBUG [CORE] Duckdb config: temp_directory = /etc/dataos/work/talos_cache.db.tmp
        snow-talos-1  | 2024-07-26 10:53:36.430  DEBUG
        snow-talos-1  | [CORE] Duckdb config: threads = 8
        snow-talos-1  | 2024-07-26 10:53:36.431  
        snow-talos-1  | DEBUG [CORE] Duckdb config: username = NULL
        snow-talos-1  | 2024-07-26 10:53:36.431  
        snow-talos-1  | DEBUG [CORE] Duckdb config: arrow_large_buffer_size = false
        snow-talos-1  | 2024-07-26 10:53:36.431  
        snow-talos-1  | DEBUG [CORE] Duckdb config: user = NULL
        snow-talos-1  | 2024-07-26 10:53:36.432  DEBUG [CORE]
        snow-talos-1  | Duckdb config: wal_autocheckpoint = 16.0 MiB
        snow-talos-1  | 2024-07-26 10:53:36.432  DEBUG
        snow-talos-1  | [CORE] Duckdb config: worker_threads = 8
        snow-talos-1  | 2024-07-26 10:53:36.433  
        snow-talos-1  | DEBUG [CORE] Duckdb config: allocator_flush_threshold = 128.0 MiB
        snow-talos-1  | 2024-07-26 10:53:36.433  
        snow-talos-1  | DEBUG [CORE] Duckdb config: duckdb_api = nodejs
        snow-talos-1  | 2024-07-26 10:53:36.433  
        snow-talos-1  | DEBUG [CORE] Duckdb config: custom_user_agent =
        snow-talos-1  | 2024-07-26 10:53:36.434  DEBUG [CORE] Duckdb config: partitioned_write_flush_threshold = 524288
        snow-talos-1  | 2024-07-26 10:53:36.434  
        snow-talos-1  | DEBUG [CORE] Duckdb config: enable_http_logging = false
        snow-talos-1  | 2024-07-26 10:53:36.434  DEBUG
        snow-talos-1  | [CORE] Duckdb config: http_logging_output =
        snow-talos-1  | 2024-07-26 10:53:36.435  DEBUG
        snow-talos-1  | [CORE] Duckdb config: binary_as_string =
        snow-talos-1  | 2024-07-26 10:53:36.435  
        snow-talos-1  | DEBUG [CORE] Duckdb config: Calendar = gregorian
        snow-talos-1  | 2024-07-26 10:53:36.435  
        snow-talos-1  | DEBUG [CORE] Duckdb config: TimeZone = Etc/UTC
        snow-talos-1  | 2024-07-26 10:53:36.436  
        snow-talos-1  | DEBUG [SERVE] Data source duckdb initialized
        snow-talos-1  | 2024-07-26 10:53:36.436  
        snow-talos-1  | DEBUG [SERVE] Initializing data source: pg
        snow-talos-1  | 2024-07-26 10:53:36.437  
        snow-talos-1  | DEBUG [SERVE] Data source pg initialized
        snow-talos-1  | 2024-07-26 10:53:36.437  
        snow-talos-1  | DEBUG [SERVE] Initializing data source: redshift
        snow-talos-1  | 2024-07-26 10:53:36.438  
        snow-talos-1  | DEBUG [SERVE] Data source redshift initialized
        snow-talos-1  | 2024-07-26 10:53:36.438  
        snow-talos-1  | DEBUG [SERVE] Initializing data source: snowflake
        snow-talos-1  | 2024-07-26 10:53:36.438  
        snow-talos-1  | DEBUG [CORE] Initializing profile: snowflake using snowflake driver
        snow-talos-1  | 2024-07-26 10:53:36.605  DEBUG [CORE]
        snow-talos-1  | Profile snowflake initialized 
        snow-talos-1  | 2024-07-26 10:53:36.605  DEBUG
        snow-talos-1  | [SERVE] Data source snowflake initialized
        snow-talos-1  | 2024-07-26 10:53:36.606  
        snow-talos-1  | INFO  [SERVE] Start to load and schedule prefetched data results from data sources to cache layer...
        snow-talos-1  | 2024-07-26 10:53:36.617  DEBUG
        snow-talos-1  | [SERVE] profile: snowflake, allow: *
        snow-talos-1  | 2024-07-26 10:53:36.618  
        snow-talos-1  | DEBUG [SERVE] profile: talos.cache, allow: *
        snow-talos-1  | 2024-07-26 10:53:36.627  DEBUG
        snow-talos-1  | [CORE] Authenticator: {
        snow-talos-1  |   "heimdallUrl": "https://liberal-donkey.dataos.app/heimdall",
        snow-talos-1  |   "userGroups": [
        snow-talos-1  |     {
        snow-talos-1  |       "name": "default",
        snow-talos-1  |       "description": "auto-generated default group to include everyone",
        snow-talos-1  |       "includes": "*"
        snow-talos-1  |     }
        snow-talos-1  |   ]
        snow-talos-1  | }
        snow-talos-1  | 2024-07-26 10:53:36.633  
        snow-talos-1  | INFO  [CLI] 🚀 Server is listening at port 3000.
        ```
        
6. Now you are ready to fetch your data using your DataOS API key. On your browser copy the below link by updating the API key with your actual DataOS API key:
    
    ```
    http://localhost:3000/api/customers?apikey=dG9rZW5fZfyHJBDE98X3llYXJseV91c2VmdWxfYnVmZmFsby5lOWNiYmEyOS05YzdGFDYKKOTM3NC1mNDAzMjdhNTYwYWE=
    ```