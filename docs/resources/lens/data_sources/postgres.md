# Postgres

## Step 1: Create Postgres Depot

If the Depot is not active, you need to create one using the provided template.

```yaml
name: ${{postgresdb}}
version: v2alpha
type: depot
layer: user
depot:
  type: JDBC                  
  description: ${{To write data to postgresql database}}
  external: ${{true}}
  secrets:
    - name: ${{sf-instance-secret-name}}-r
      allkeys: true

    - name: ${{sf-instance-secret-name}}-rw
      allkeys: true
  postgresql:                        
    subprotocol: "postgresql"
    host: ${{host}}
    port: ${{port}}
    database: ${{postgres}}
    params: #Required 
      sslmode: ${{disable}}
```

While creating Lens on Postgres Depot the following aspects need to be considered:

* The SQL dialect used in the `model/sql` folder to load data from the Postgres source should be of the Postgres dialect.

* The table naming in the `model/table`  should be of the format: `schema.table`.

## Step 2: Set up Lens model folder

Organize the Lens model folder with the following structure to define tables, views, and governance policies:

```
model
├── sqls
│   └── sample.sql  # SQL script for table dimensions
├── tables
│   └── sample_table.yml  # Logical table definition (joins, dimensions, measures, segments)
├── views
│   └── sample_view.yml  # Logical views referencing tables
└── user_groups.yml  # User group policies for governance
```

1. **SQL Scripts (`model/sqls`):** Add SQL files defining table structures and transformations. Ensure the SQL dialect is compatible to the Postgres.

2. **Tables (`model/tables`):** Define logical tables in separate YAML files. Include dimensions, measures, segments, and joins.

3. **Views (`model/views`):** Define views in YAML files, referencing the logical tables.

4. **User Groups (`user_groups.yml`):** Define access control by creating user groups and assigning permissions.

## Step 3: Create the Lens deployment manifest file

After setting up the Lens model folder, the next step is to configure the deployment manifest. Below is the YAML template for configuring a Lens deployment. The below manifest is intended for source-type depot named `postgresdepot`, created on the Postgres source.

```yaml
version: v1alpha
name: "postgres-lens"
layer: user
type: lens
tags:
  - lens
description: postgres depot lens deployment on lens2
lens:
  compute: runnable-default
  secrets:
    - name: bitbucket-cred
      allKeys: true
  source:
    type: depot #minerva/themis/depot
    name: postgresdepot
  repo:
    url: https://bitbucket.org/tmdc/sample
    lensBaseDir: sample/lens/source/depot/postgres/model 
    # secretId: lens2_bitbucket_r
    syncFlags:
      - --ref=dev #repo-name

  api:   # optional
    replicas: 1 # optional
    logLevel: info  # optional
      
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

    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
  router: # optional
    logLevel: info  # optional
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

Each section of the YAML template defines key aspects of the Lens deployment. Below is a detailed explanation of its components:

* **Defining the Source:**

      * **Source type:**  The `type` attribute in the `source` section must be explicitly set to `depot`.

      * **Source name:** The `name` attribute in the `source` section should specify the name of the Postgres  Depot created.

* **Setting Up Compute and Secrets:**

      * Define the compute settings, such as which engine (e.g., `runnable-default`) will process the data.

      * Include any necessary secrets (e.g., credentials for Bitbucket or AWS) for secure access to data and repositories.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/postgres/model`.

      * **`secretId`:**  The `secretId` attribute is used to access private repositories (e.g., Bitbucket, GitHub) . It specifies the secret needed to securely authenticate and access the repository.

      * **`syncFlags`**:  Specifies additional flags to control repository synchronization. Example: `--ref=dev` specifies that the Lens model rsides in the dev branch.

* **Configuring API, Worker and Metric Settings (Optional):** Set up replicas, logging levels, and resource allocations for APIs, workers, routers, and other components.


## Step 4: Apply the Lens deployment manifest file

After configuring the deployment file with the necessary settings and specifications, apply the manifest using the following command:

=== "Command"

    ```bash 
    dataos-ctl resource apply -f ${manifest-file-path}
    ```
=== "Alternative command"

    ```bash 
    dataos-ctl apply -f ${manifest-file-path}
    ```
=== "Example usage"

    ```bash 
    dataos-ctl apply -f /lens/lens_deployment.yml -w curriculum
    # Expected output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying(curriculum) sales360:v1alpha:lens... 
    INFO[0001] 🔧 applying(curriculum) sales360:v1alpha:lens...created 
    INFO[0001] 🛠 apply...complete
    ```



## Docker compose manifest file

<details>

  <summary>Docker compose manifest file for local testing</summary>

```yaml hl_lines="14-16"
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-monkey.dataos.app
  # Overview
  LENS2_NAME: sales360
  LENS2_DESCRIPTION: "Ecommerce use case on Adventureworks sales data"
  LENS2_TAGS: "lens2, ecom, sales and customer insights"
  LENS2_AUTHORS: "iamgroot, iamloki"
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  # Data Source
  LENS2_SOURCE_TYPE: depot
  LENS2_SOURCE_NAME: postgreslens2
  DATAOS_RUN_AS_APIKEY: bGVuc3NzLmUzMDA1ZjMzLTZiZjAtNDY4My05ZjhhLWNhODliZTFhZWJhMQ==
  LENS2_DB_SSL : "true"
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
    image: rubiklabs/lens2:0.35.41-05
    ports:
      - 4000:4000
      - 25432:5432
      - 13306:13306
    environment:
      <<: *lens2-environment   
    volumes:
      - ./model:/etc/dataos/work/model
```

</details>


<!-- Follow these steps to create the `docker-compose.yml`:

- Step 1: Create a `docker-compose.yml` manifest file.
- Step 2: Copy the template from above and paste it in a code.
- Step 3: Fill the values for the atttributes/fields declared in the manifest file as per the Postgres source.



**Required Postgres Depot Source Attributes**

```yaml
LENS2_SOURCE_TYPE: depot
LENS2_SOURCE_NAME: postgreslens2
DATAOS_RUN_AS_APIKEY: bGVuc3NzLmUzMDA1ZjMzLTZiZjAtNDY4My05ZjhhLWNhODliZTFhZWJhMQ==
LENS2_DB_SSL : "true"
```
 -->
