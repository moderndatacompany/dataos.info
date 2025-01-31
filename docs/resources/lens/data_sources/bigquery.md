# Connecting to Bigquery Depot

## Step 1: Create the Bigquery Depot

If the Depot is not active, you need to create one using the provided template.

```yaml
name: ${{bigquerydepot}}
version: v2alpha
type: depot
tags:
  - ${{dropzone}}
  - ${{bigquery}}
owner: ${{owner-name}}
layer: user
depot:
  type: BIGQUERY                 
      description: ${{description}} # optional
  external: ${{true}}
  secrets:
    - name: ${{bq-instance-secret-name}}-r
      allkeys: true

    - name: ${{bq-instance-secret-name}}-rw
      allkeys: true
  bigquery:  # optional                         
    project: ${{project-name}} # optional
    params: # optional
      ${{"key1": "value1"}}
      ${{"key2": "value2"}}
```

## Step 2: Prepare the Lens model folder

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

1. **SQL Scripts (`model/sqls`)**

      * Add SQL files defining table structures and transformations.

      * Ensure the SQL dialect matches BigQuery syntax. Format table names as:
        `project_id.dataset.table`

      * Use `STRING` for text data types instead of `VARCHAR`.

      * Replace generic functions with BigQuery's `EXTRACT` function.

2. **Tables (`model/tables`):** Define logical tables in separate YAML files. Include dimensions, measures, segments, and joins.

3. **Views (`model/views`):** Define views in YAML files, referencing the logical tables.

4. **User Groups (`user_groups.yml`):** Define access control by creating user groups and assigning permissions.

## Step 3: Deployment manifest file

After setting up the Lens model folder, the next step is to configure the deployment manifest. Below is the YAML template for configuring a Lens deployment.

```yaml
# RESOURCE META SECTION
version: v1alpha # Lens manifest version (mandatory)
name: "bigquery-lens" # Lens Resource name (mandatory)
layer: user # DataOS Layer (optional)
type: lens # Type of Resource (mandatory)
tags: # Tags (optional)
  - lens
description: bigquery depot lens deployment on lens2 # Lens Resource description (optional)

# LENS-SPECIFIC SECTION
lens:
  compute: runnable-default # Compute Resource that Lens should utilize (mandatory)
  secrets: # Referred Instance-secret configuration (**mandatory for private code repository, not required for public repository)
    - name: bitbucket-cred # Referred Instance Secret name (mandatory)
      allKeys: true # All keys within the secret are required or not (optional)

  source: # Data Source configuration
    type: depot # Source type is depot here
    name: bigquerydepot # Name of the bigquery depot

  repo: # Lens model code repository configuration (mandatory)
    url: https://bitbucket.org/tmdc/sample # URL of repository containing the Lens model (mandatory)
    lensBaseDir: sample/lens/source/depot/bigquery/model # Relative path of the Lens 'model' directory in the repository (mandatory)
    syncFlags: # Additional flags used during synchronization, such as specific branch.
      - --ref=lens # Repository Branch

  api: # API Instances configuration (optional)
    replicas: 1 # Number of API instance replicas (optional)
    logLevel: info  # Logging granularity (optional)
    resources: # CPU and memory configurations for API Instances (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 2000m
        memory: 2048Mi

  worker: # Worker configuration (optional)
    replicas: 2 # Number of Worker replicas (optional)
    logLevel: debug # Logging level (optional)
    resources: # CPU and memory configurations for Worker (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi

  router: # Router configuration (optional)
    logLevel: info  # Level of log detail (optional)
    resources: # CPU and memory resource specifications for the router (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi

  iris:
    logLevel: info # Level of log detail (optional)
    resources: # CPU and memory resource specifications for the iris board (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi

  metric:    #optional
    logLevel: info
```

Each section of the YAML template defines key aspects of the Lens deployment. Below is a detailed explanation of its components:

* **Defining the Source:**

      * **Source type:**  The `type` attribute in the `source` section must be explicitly set to `depot`.

      * **Source name:** The `name` attribute in the `source` section should specify the name of the Bigquery Depot created.

* **Setting Up Compute and Secrets:**

      * Define the compute settings, such as which engine (e.g., `runnable-default`) will process the data.

      * Include any necessary secrets (e.g., credentials for Bitbucket or AWS) for secure access to data and repositories.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/bigquery/model`.

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

Ensure that the necessary attributes are highlighted in the Docker Compose Manifest file for proper configuration during the connection setup process.


<details>

  <summary>Docker compose manifest file for local testing</summary>

```yaml hl_lines="13-15"
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-monkey.dataos.app
  # Overview
  LENS2_NAME: sales360
  LENS2_DESCRIPTION: "Ecommerce use case on Adventureworks sales data"
  LENS2_TAGS: "lens2, ecom, sales and customer insights"
  LENS2_AUTHORS: "rakeshvishvakarma, shubhanshu"
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  # Data Source
  LENS2_SOURCE_TYPE: ${depot} #source name - depot
  LENS2_SOURCE_NAME: ${bigquerydepot} #name of the bigquery depot
  DATAOS_RUN_AS_APIKEY: ${A1ZjMDliZTFhZWJhMQ==}
  # LogZjAtNDY4My05
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
      # - ./scripts/commons.js:/app/scripts/commons.js
      # - ./scripts/bootstrap.js:/app/scripts/bootstrap.js
      # - ./scripts/config.js:/app/scripts/config.js
```

</details>



<!-- 
## Connecting to Bigquery without Depot/Cluster

### **Prerequisites**

In order to connect Google BigQuery to Lens, you need to provide service account credentials. Lens2 requires the service account to have **BigQuery Data Viewer** and **BigQuery Job User** roles enabled. You can learn more about acquiring Google BigQuery credentials [here](https://cloud.google.com/docs/authentication/getting-started).


- The [Google Cloud Project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin) for the BigQuery project.
- A set of [Google Cloud service credentials](https://support.google.com/a/answer/7378726?hl=en) which [allow access](https://cloud.google.com/docs/authentication/getting-started) to the BigQuery project
- The [Google Cloud region](https://cloud.google.com/bigquery/docs/locations#regional-locations) for the BigQuery project

Syntax with example is written below:

=== "Syntax"

    ```yaml
    # Bigquery configuration
    LENS2_DB_TYPE=bigquery
    LENS2_DB_BQ_PROJECT_ID=${BIGQUERY_PROJECT_ID}
    LENS2_DB_BQ_KEY_FILE=${BIGQUERY_KEY_FILE_PATH}
    ```

=== "Sample"

    ```yaml
    # Bigquery configuration
    LENS2_DB_TYPE=bigquery
    LENS2_DB_BQ_PROJECT_ID=my-bigquery-project-123456
    LENS2_DB_BQ_KEY_FILE=/path/to/my/keyfile.json
    ```
**Sample manifest file**

```yaml
LENS2_VERSION=0.34.60-13
LENS2_CACHE_VERSION=0.34.60-amd64v8

LENS2_LOG_LEVEL=error
LENS2_LOADER_LOG_LEVEL=debug

LENS2_HEIMDALL_BASE_URL="https://alpha-omega.dataos.app/heimdall"

LENS2_SCHEDULED_REFRESH_DEFAULT="false"
LENS2_API_SECRET=28487985729875987397AHFUHUD

CACHE_TELEMETRY="false"
CACHE_LOG_LEVEL=error

# Bigquery configuration
LENS2_DB_TYPE=bigquery
LENS2_DB_BQ_PROJECT_ID=my-bigquery-project-123456
LENS2_DB_BQ_KEY_FILE=/path/to/my/keyfile.json

 #Lens Configs
LENS2_NAME=bq_lens
LENS2_DESCRIPTION=lens description
LENS2_TAGS='lens2 tags (comma separated)'
LENS2_AUTHORS='lens2 auther names (comma separated)'

LENS2_BASE_URL=http://localhost:4000/lens2
LENS2_META_PATH=/v2/meta
LENS2_DATAOS_USER_NAME=USERNAME
LENS2_DATAOS_USER_APIKEY=APIKEY
LENS2_RILL_PATH=rill
LENS2_CHECKS_PATH=checks
```

### Environment variables

| **Environment Variable** | **Description** | **Possible Values** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| `LENS2_DB_TYPE` | The type of database | bigquery | bigquery | ✅ |
| `LENS2_DB_BQ_PROJECT_ID` | The Google BigQuery project ID to connect to | A valid Google BigQuery Project ID | my-bigquery-project-123456 | ✅ |
| `LENS2_DB_BQ_KEY_FILE` | The path to a JSON key file for connecting to Google BigQuery | A valid Google BigQuery JSON key file | /path/to/my/keyfile.json | ✅ | -->