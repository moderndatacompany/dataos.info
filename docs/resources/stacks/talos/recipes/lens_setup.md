# Setting up Talos for Lens

## Pre-requisites

- [Lens](/resources/lens/) set up
- Docker initialization

## Steps

1. Create a folder, open the folder with a code editor (VS Code), and create a `config.yaml` manifest file and copy the below code. Update the name, description, version, dataos context, Lens as type, and Lens name.
    
    ```yaml
    name: lens
    description: A talos-lens app
    version: 0.1.19-dev
    auth:
      heimdallUrl: https://${{liberal-donkey.dataos.app}}/heimdall
    logLevel: 'DEBUG'
    sources:
      - name: lens 
        type: lens
        lensName: 'public:sales360'
    ```
    

2. In the same folder, create `docker-compose.yaml` manifest file, copy the below-provided code, and update the `volumes` path `/home/iamgroot/Desktop/talos-examples/lens` with the actual path of your folder, add your dataos username and dataos API key in `DATAOS_RUN_AS_USER` and `DATAOS_RUN_AS_APIKEY` respectively.

  <aside class="callout">
  🗣 Ensure you’re using the latest version and image of Talos by confirming with the DataOS administrator.
  </aside>

    ```yaml
    version: "2.2"
    services:
      talos:
        image: rubiklabs/talos:0.1.6
        ports:
          - "3000:3000"
        volumes:
          - /home/iamgroot/Desktop/talos-examples/lens:/etc/dataos/work
        environment:
          DATAOS_RUN_AS_USER: ${{iamgroot}}
          DATAOS_RUN_AS_APIKEY: ${{AdtyuhJNKlsfdtMKGsopwhdgdtyjskshgJKHjdkdh86nney}}
          DATAOS_FQDN: ${{liberal-donkey.dataos.app}}
        tty: true
    ```
    
3. Create a file `Makefile` in the same folder, and copy the below code to be able test Talos locally.
    
    ```makefile
    start:
    	docker-compose -f docker-compose.yaml up -d
    
    stop:
    	docker-compose -f docker-compose.yaml down -v
    ```
    
4. Create a folder named `apis` inside the same parent folder, inside `apis` create the files `sales.sql` which will contain the SQL query, and `sales.yaml` to define the path to access sales data in your API as shown below. You can add as many `.sql` files as needed, but each one must have a corresponding `.yaml` manifest file with the same name.
    
    ```sql
    # sales.sql
    SELECT customer_no FROM sales LIMIT 20
    ```
    
    ```yaml
    # sales.yaml
    urlPath: /sales/customers
    description: list customer numbers from sales table
    source: lens
    ```
    
5. Run `docker-compose up` on the terminal to test locally, the output should look like the following. This step is optional; if you prefer, you can skip directly to the next step.
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
        depot-postgres-talos-1  | 2024-07-24 10:56:22.630  DEBUG [BUILD] Initializing data source:  
        depot-postgres-talos-1  | 2024-07-24 10:56:22.636  DEBUG
        depot-postgres-talos-1  | [CORE] Create connection for talos.cache
        depot-postgres-talos-1  | 2024-07-24 10:56:22.637  
        depot-postgres-talos-1  | DEBUG [CORE] Open database in automatic mode
        depot-postgres-talos-1  | 2024-07-24 10:56:22.650  
        depot-postgres-talos-1  | DEBUG
        depot-postgres-talos-1  | [CORE] Installed httpfs extension
        depot-postgres-talos-1  | 2024-07-24 10:56:22.653  
        depot-postgres-talos-1  | DEBUG [CORE]   config: access_mode = automatic
        depot-postgres-talos-1  | 2024-07-24 10:56:22.653  
        depot-postgres-talos-1  | DEBUG [CORE]   config: allow_persistent_secrets = true
        depot-postgres-talos-1  | 2024-07-24 10:56:22.654  
        depot-postgres-talos-1  | DEBUG [CORE]   config: checkpoint_threshold = 16.0 MiB
        depot-postgres-talos-1  | 2024-07-24 10:56:22.654  
        depot-postgres-talos-1  | DEBUG [CORE]   config: debug_checkpoint_abort = none
        depot-postgres-talos-1  | 2024-07-24 10:56:22.654  
        depot-postgres-talos-1  | DEBUG [CORE]   config: storage_compatibility_version = v0.10.2
        depot-postgres-talos-1  | 2024-07-24 10:56:22.654  
        depot-postgres-talos-1  | DEBUG [CORE]   config: debug_force_external = false
        depot-postgres-talos-1  | 2024-07-24 10:56:22.655  
        depot-postgres-talos-1  | DEBUG [CORE]   config: debug_force_no_cross_product = false
        depot-postgres-talos-1  | 2024-07-24 10:56:22.655  
        depot-postgres-talos-1  | DEBUG [CORE]   config: debug_asof_iejoin = false
        depot-postgres-talos-1  | 2024-07-24 10:56:22.655  
        depot-postgres-talos-1  | DEBUG [CORE]   config: prefer_range_joins = false
        depot-postgres-talos-1  | 2024-07-24 10:56:22.655  
        depot-postgres-talos-1  | DEBUG [CORE]   config: debug_window_mode = NULL
        depot-postgres-talos-1  | 2024-07-24 10:56:22.656  
        depot-postgres-talos-1  | DEBUG [CORE]   config: default_collation =
        depot-postgres-talos-1  | 2024-07-24 10:56:22.656  
        depot-postgres-talos-1  | DEBUG [CORE]   config: default_order = asc
        depot-postgres-talos-1  | 2024-07-24 10:56:22.656  
        depot-postgres-talos-1  | DEBUG [CORE]   config: default_null_order = nulls_last
        depot-postgres-talos-1  | 2024-07-24 10:56:22.656  
        depot-postgres-talos-1  | DEBUG [CORE]   config: disabled_filesystems =
        depot-postgres-talos-1  | 2024-07-24 10:56:22.656  
        depot-postgres-talos-1  | DEBUG [CORE]   config: disabled_optimizers =  
        depot-postgres-talos-1  | 2024-07-24 10:56:22.657  DEBUG [CORE]   config: enable_external_access = true
        depot-postgres-talos-1  | 
        
        ```
6. To deploy Talos as a Service within DataOS, initialize the repository and push the changes to the Bitbucket.

7. Create an Instance Secret to store your Bitbucket credentials. This step ensures that the necessary authentication details are securely stored and accessible for the Talos Service.

```yaml
name: ${{bitrepo}}-r
version: v1
type: instance-secret
description: ${{"Bitbucket credentials"}}
layer: ${{user}}
instance-secret:
  type: ${{key-value}}
  acl: ${{r}}
  data:
    GITSYNC_USERNAME: ${{"iamgroot7340"}}# Bitbucket username
    GITSYNC_PASSWORD: ${{"ATBBe2we5UPdGVthtEHnjkLDHL7443AC"}}# Bitbukcet app password
```

To create an app password in Bitbucket follow the below steps:

- Go to settings, then click on Personal Bitbucket settings.
- Go to App passwords create one and paste the password into your Instance Secret manifest file.
    
    <center>
      <img src="/resources/stacks/talos/app.png" alt="Talos" style="width:30rem; border: 1px solid black; padding: 5px;" />
    </center>

Apply the Instance Secret manifest file by executing the below command:

```bash
dataos-ctl resource apply -f /home/office/talos/secret.yaml 
```

To know more about Instance Secret, [please refer to this](https://dataos.info/resources/instance_secret/).

8. Now create a manifest file for the Talos Service as shown below.

  <aside class="callout">
  🗣 Ensure to map the repository path correctly.
  </aside>
    
    ```yaml
    name: ${{talos-test}} # service name
    version: ${{v1}} # version
    type: service # resource type
    tags: # tags
      - ${{service}}
      - ${{dataos:type:resource}}
      - ${{dataos:resource:service}}
      - ${{dataos:layer:user}}
    description: ${{Talos Service}}
    workspace: ${{public}}
    service: # service specific section
      servicePort: 3000
      ingress:
        enabled: true
        stripPath: true
        path: /talos/${{workspace}}:${{talos-test}} # service name
        noAuthentication: true
      replicas: ${{1}}
      logLevel: ${{DEBUG}}
      compute: runnable-default
      envs:
        TALOS_SCHEMA_PATH: ${{talos/setup}}
        TALOS_BASE_PATH: /talos/public:${{talos-test}}
      resources:
        requests:
          cpu: ${{100m}}
          memory: ${{128Mi}}
        limits:
          cpu: ${{500m}}
          memory: ${{512Mi}}
      stack: talos:2.0
      dataosSecrets:
        - name: ${{bitrepo-r}}
          allKeys: true
      stackSpec:
        repo:
          url: ${{https://bitbucket.org/mywork15/talos/}}
          projectDirectory: ${{talos/setup}}
          syncFlags:
            - '--ref=main'
    ```
    
To know more about each attribute, [please refer to this](/resources/stacks/talos/configurations/service/).
    
9. Apply the Service manifest by executing the below command:
    
    ```bash
    dataos-ctl resource apply -f /home/office/talos/service.yaml 
    ```
    
10. To check if the service is running successfully, execute the following command.
    
    ```bash
    dataos-ctl log -t service -n ${{service-name}} -w ${{workspace}}
    ```
    
    Successful execution will look like the following:
    
    ```bash
    EBUG [CORE]   config: TimeZone = Etc/UTC
    2024-07-31 08:51:12.566  
    DEBUG [SERVE] Data source initialized
    2024-07-31 08:51:12.567  DEBUG
    [SERVE] Initializing data source: pg
    2024-07-31 08:51:12.567  DEBUG
    [SERVE] Data source pg initialized
    2024-07-31 08:51:12.567  DEBUG
    [SERVE] Initializing data source: redshift
    2024-07-31 08:51:12.567  DEBUG
    [SERVE] Data source redshift initialized
    2024-07-31 08:51:12.568  
    DEBUG [SERVE] Initializing data source: snowflake
    2024-07-31 08:51:12.568  DEBUG
    [CORE] Initializing profile: snowflake using snowflake driver
    2024-07-31 08:51:12.681  DEBUG
    [CORE] Profile snowflake initialized
    2024-07-31 08:51:12.681  DEBUG [SERVE] Data source snowflake initialized
    2024-07-31 08:51:12.682  
    INFO  [SERVE] Start to load and schedule prefetched data results from data sources to cache layer...
    2024-07-31 08:51:12.689  DEBUG
    [SERVE] profile: snowflake, allow: *
    2024-07-31 08:51:12.690  
    DEBUG [SERVE] profile: talos.cache, allow: *
    2024-07-31 08:51:12.696  DEBUG
    [CORE] Authenticator: {
      "heimdallUrl": "https://liberal-donkey.dataos.app/heimdall",
      "userGroups": [
        {
          "name": "default",
          "description": "auto-generated default group to include everyone",
          "includes": "*"
        }
      ]
    }
    2024-07-31 08:51:12.702  
    INFO  [CLI] 🚀 Server is listening at port 3000.
    ```
    

### **Good to go!**

- Now you can access the data on the API endpoint using Postman, as shown below:
    
    <center>
      <img src="/resources/stacks/talos/image2.png" alt="Talos" style="width:40rem; border: 1px solid black; padding: 5px;" />
    </center>

    You can even hit the endpoint `/doc/postman?apikey='xxxxxxxxx'` to download the postman collection and import the `.json` collection into postman.
    
- Authenticate the API endpoints by passing the API Key on [DataOS CLI](/resources/stacks/cli_stack/), as query param as shown below.
    
    ```bash
    curl --location 'https://liberal-donkey.dataos.app/talos/pubic:talos-test/api/table?apikey=xxxx' 
    ```    

