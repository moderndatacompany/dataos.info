# Setting up Talos for Redshift

This section will guide you in setting up the Redshift Database and exposing the data through APIs.

## Setting Up Tickit Database on AWS Redshift

The `Tickit`, an online ticket sales company wants to generate comprehensive reports on event sales, user preferences, and venue performance to enhance business strategies and customer experiences.

### Prerequisites

- AWS Account
- AWS CLI installed and configured
- SQL client tool (e.g., SQL Workbench/J)

### Step-by-Step Guide

1. **Create a Redshift Cluster:**
    - Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
    - Navigate to **Amazon Redshift**.
    - Click **Create cluster** and configure the cluster settings:
        - **Cluster identifier:** `tickit-cluster`
        - **Node type:** `dc2.large` (or your choice)
        - **Number of nodes:** 2 (or your choice)
        - **Database name:** `tickit`
        - **Master username:** `your-username`
        - **Master user password:** `your-password`
    - Click **Create cluster** and wait for the cluster to become available.
2. **Configure Security Group:**
    - Navigate to **VPC** > **Security Groups**.
    - Select the security group associated with your Redshift cluster.
    - Add an inbound rule to allow traffic on port `5439` (default Redshift port) from your IP address.
3. **Connect to the Redshift Cluster:**
    - Use a SQL client tool to connect to the Redshift cluster:
        - **Host:** `<your-cluster-endpoint>`
        - **Port:** `5439`
        - **Database:** `tickit`
        - **Username:** `your-username`
        - **Password:** `your-password`
4. **Create Tickit Schema and Tables:**
    - Download the Tickit dataset from the AWS documentation [Tickit Database Script](https://docs.aws.amazon.com/redshift/latest/dg/c_sampledb.html).
    - Execute the downloaded SQL script to create the schema and tables in your Redshift database.
5. **Load Sample Data:**
    - Ensure your data files (e.g., `allevents_pipe.txt`) are stored in an S3 bucket.
    - Use the `COPY` command to load data into the tables:
        
        ```sql
        COPY public.event FROM 's3://your-bucket-name/allevents_pipe.txt'
        CREDENTIALS 'aws_access_key_id=YOUR_ACCESS_KEY;aws_secret_access_key=YOUR_SECRET_KEY'
        DELIMITER '|'
        TIMEFORMAT 'auto'
        REGION 'your-region';
        
        ```
        
6. **Verify Data Loading:**
    - Run SQL queries to verify the data has been loaded correctly:
        
        ```sql
        SELECT * FROM public.event LIMIT 10;
        
        ```
        

Following these steps, you will have the Tickit database set up on AWS Redshift, ready for querying and reporting through the Talos API framework.

## Setting Up Talos

In this section, we’ll set up Talos to expose category popularity data through the API. 

### Pre-requisites

- Redshift Database set up
- Docker initialization

### Step-by-Step Guide

1. Create a working repository for Talos, inside this repository, create a `config.yaml` file with the following code to define the base configuration for Talos by updating the name, description, version, DataOS context, and connection details :
    
    ```yaml
    name: tickit
    description: A talos-redshift app
    version: 0.1.6
    auth:
      heimdallUrl: https://liberal-donkey.dataos.app/heimdall
    logLevel: 'DEBUG'
    cache: tmp
    sources:
      - name: redshift # profile name
        type: redshift
        connection:
          host: "host"
          port: 5439
          user: "user"
          password: "password"
          database: "database"
          cache:
            s3BucketPath: "s3://bucket/path"
            accessKeyId: "keyid"
            secretAccessKey: "secretAccessKey"
            region: "region"
    
    ```
    

1.  Create a folder named `apis` inside the same repository, then create `categorypopularity.sql` and `categorypopularity.yaml` files as shown below:
    
    SQL Query (`categorypopularity.sql`)
    
    ```sql
    SELECT category.catname, SUM(qtysold) AS total_tickets
    FROM category
    JOIN event ON category.catid = event.catid
    JOIN sales ON event.eventid = sales.eventid
    GROUP BY category.catname;
    ```
    
    YAML Configuration (`categorypopularity.yaml`)
    
    ```yaml
    urlPath: /categories/popularity
    description: Retrieve popularity metrics for event categories including total tickets sold per category.
    source: redshift
    ```
    

1. In the same repository, create `docker-compose.yaml` manifest file, copy the below-provided code, and update the `volumes` path `/home/Desktop/talos/depot-postgres` with the actual path of your repository, add your dataos username and dataos API key in `DATAOS_RUN_AS_USER` and `DATAOS_RUN_AS_APIKEY` respectively.
    
    ```yaml
    version: "2.2"
    services:
      talos:
        image: rubiklabs/talos:0.1.6
        ports:
          - "3000:3000"
        volumes:
          - /home/iamgroot/Desktop/talos-examples/redshift/:/etc/dataos/work
        environment:
          DATAOS_RUN_AS_USER: iamgroot
          DATAOS_RUN_AS_APIKEY: dG9rZW5fYWRtaXR8ujkk98erdtR1cmFsbHlfZW5hYmxpbmdfb3J5eC5lODg2MjIyZC05NDMwLTQ4MWEtYjU3MC01YTJiZWY5MjI5OGE=
          DATAOS_FQDN: liberal-donkey.dataos.app
        tty: true
    ```
    
2. Create a new file `Makefile` in the same repository, and copy the below code.
    
    ```makefile
    start:
    	docker-compose -f docker-compose.yaml up -d
    
    stop:
    	docker-compose -f docker-compose.yaml down -v
    ```
    
3. Run `docker-compose up` on the terminal. The output should look similar to the following:
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
        
4. Now you are ready to fetch your data using your DataOS API key on Postman or your browser copy the below link by updating the API key with your actual DataOS API key:
    
    ```
    http://localhost:3000/api/customer?apikey=dG9rZW5fYWRt9uYXR1cmFsbHlfZgfhgu567rgdffC5lODg2MjIyZC05NDMwLTQ4MWEtYjU3MC01YTJiZWY5MjI5OGE=
    ```
    

Similarly, for different queries, you just need to make changes in `apis` folder.

- **Event Details API**
    
    YAML Configuration (`eventdetails.yaml`):
    
    ```yaml
    urlPath: /events/:id
    description: Retrieve detailed information for a specific event.
    request :
      - fieldName: id
        fieldIn: path
    source: redshift
    
    ```
    
    SQL Query (`eventdetails.sql`)
    
    ```sql
    
    SELECT * FROM event WHERE 
    eventid = {{context.params.id}} ;
    ```
    

- **Create All Events API**
    
    YAML Configuration (`events.yaml`)
    
    ```yaml
    urlPath: /events
    description: Retrieve details of all events including event ID, name, venue, category, and start time.
    source: redshift
    cache:
      - cacheTableName: 'event_cache'
        sql: 'SELECT * FROM event'
        source: redshift
    
    ```
    
    SQL Query (`events.sql`)
    
    ```sql
    {% cache %}
    SELECT eventid, eventname, venueid, catid, dateid, starttime FROM event_cache;
    {% endcache %}
    ```
    

- **Create Sales by Event API**
    
    YAML Configuration (`getsalesbyevent.yaml`)
    
    ```yaml
    urlPath: /events/:id/sales
    description: Retrieve sales details for a specific event including ticket quantity sold, price paid, and sale time.
    request :
      - fieldName: id
        fieldIn: path
    source: redshift
    ```
    
    SQL Query (`getsalesbyevent.sql`)
    
    ```sql
    
    SELECT * FROM sales WHERE eventid = {{ context.params.id }};
    ```
    

- **Create User Purchase History API**
    
    YAML Configuration (`getuserpurchasehistory.yaml`)
    
    ```yaml
    urlPath: /users/:bid/purchases
    description: Retrieve all purchases made by a specific user.
    request :
      - fieldName: bid
        fieldIn: path
    source: redshift
    cache:
      - cacheTableName: 'sales_cache'
        sql: 'SELECT * FROM sales'
        source: redshift
    ```
    
    SQL Query (`getuserpurchasehistory.sql`)
    
    ```sql
    {% cache %}
    SELECT * FROM sales_cache WHERE buyerid = {{context.params.bid}};
    {% endcache %}
    ```
    

- **Create Venue Performance API**
    
    YAML Configuration (`venueperformance.yaml`)
    
    ```yaml
    urlPath: /venues/:id/performance
    description: Retrieve performance metrics for a specific venue including number of events hosted and total tickets sold.
    request :
      - fieldName: id
        fieldIn: path
    source: redshift
    ```
    
    SQL Query (`venueperformance.sql`)
    
    ```sql
    SELECT event.venueid, COUNT(event.eventid) AS total_events, SUM(sales.qtysold) AS total_tickets
    FROM public.event
    JOIN public.sales ON event.eventid = sales.eventid
    WHERE event.venueid = {{context.params.id}}
    GROUP BY event.venueid;
    
    ```