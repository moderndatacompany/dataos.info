# Connecting to Bigquery Depot

## Step 1: Create the Bigquery Depot

If the Depot is not active, create one using the provided template.

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

In the `model` folder, the semantic model will be defined, encompassing SQL mappings, logical tables, logical views, and user groups. Each subfolder contains specific files related to the Lens model. You can download the Lens template to quickly get started.

[lens template](/resources/lens/lens_model_folder_setup/lens-project-template.zip)


### **Load data from the data source**

In the `sqls` folder, create `.sql` files for each logical table, where each file is responsible for loading or selecting the relevant data from the source. Ensure, only the necessary columns are extracted, and the SQL dialect is specific to the bigquery. For instance,

* Format table names as: `project_id.dataset.table`.

* Use `STRING` for text data types instead of `VARCHAR`.

* Replace generic functions with BigQuery’s `EXTRACT` function.

For instance, a simple data load might look as follows:

```sql
SELECT
  *
FROM
  "onelakehouse"."retail".channel;
```

Alternatively, you can write more advanced queries that include transformations, such as:

```sql
SELECT
  CAST(customer_id AS VARCHAR) AS customer_id,
  first_name,
  CAST(DATE_PARSE(birth_date, '%d-%m-%Y') AS TIMESTAMP) AS birth_date,
  age,
  CAST(register_date AS TIMESTAMP) AS register_date,
  occupation,
  annual_income,
  city,
  state,
  country,
  zip_code
FROM
  "onelakehouse"."retail".customer;
```
  
### **Define the table in the model**

Create a `tables` folder to store logical table definitions, with each table defined in a separate YAML file outlining its dimensions, measures, and segments. For instance, to define a table for `sales `data:

```yaml
table:
  - name: customers
    sql: {{ load_sql('customers') }}
    description: Table containing information about sales transactions.
```

### **Add dimensions and measures**

After defining the base table, add the necessary dimensions and measures. For instance, to create a table for sales data with measures and dimensions, the YAML definition could look as follows:

```yaml
tables:
  - name: sales
    sql: {{ load_sql('sales') }}
    description: Table containing sales records with order details.

    dimensions:
      - name: order_id
        type: number
        description: Unique identifier for each order.
        sql: order_id
        primary_key: true
        public: true

    measures:
      - name: total_orders_count
        type: count
        sql: id
        description: Total number of orders.
```

### **Add segments to filter**

Segments are filters that allow for the application of specific conditions to refine the data analysis. By defining segments, you can focus on particular subsets of data, ensuring that only the relevant records are included in your analysis. For example, to filter for records where the state is either Illinois or Ohio, you can define a segment as follows:

```yaml
segments:
  - name: state_filter
    sql: "{TABLE}.state IN ('Illinois', 'Ohio')"
```

To know more about segments click [here](https://dataos.info/resources/lens/segments/).


### **Create views**

Create a **views** folder to store all logical views, with each view defined in a separate YAML file (e.g., `sample_view.yml`). Each view references dimensions, measures, and segments from multiple logical tables. For instance the following`customer_churn` view is created.

```yaml
views:
  - name: customer_churn_prediction
    description: Contains customer churn information.
    tables:
      - join_path: marketing_campaign
        includes:
          - engagement_score
          - customer_id
      - join_path: customer
        includes:
          - country
          - customer_segments
```

To know more about the views click [here](https://dataos.info/resources/lens/views/).


### **Create User groups**

This YAML manifest file is used to manage access levels for the semantic model. It defines user groups that organize users based on their access privileges. In this file, you can create multiple groups and assign different users to each group, allowing you to control access to the model.By default, there is a 'default' user group in the YAML file that includes all users.

```yaml
user_groups:
  - name: default
    description: this is default user group
    includes: "*"
```

To know more about the User groups click [here](/resources/lens/user_groups_and_data_policies/).


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
```

Each section of the YAML template defines key aspects of the Lens deployment. Below is a detailed explanation of its components:

* **Defining the Source:**

      * **Source type:**  The `type` attribute in the `source` section must be explicitly set to `depot`.

      * **Source name:** The `name` attribute in the `source` section should specify the name of the Bigquery Depot created.

* **Setting Up Compute and Secrets:**

      * Define the compute settings, such as which engine (e.g., `runnable-default`) will process the data.

      * Include any necessary secrets (e.g., credentials for Bitbucket or AWS CodeCommit) for secure access to data and repositories.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/bigquery/model`.

      * **`secretId`:**  The `secretId` attribute is used to access private repositories (e.g., Bitbucket, GitHub). It specifies the secret needed to securely authenticate and access the repository.

      * **`syncFlags`**:  Specifies additional flags to control repository synchronization. Example: `--ref=dev` specifies that the Lens model resides in the `dev` branch.

* **Configuring API, Worker and Metric Settings (Optional):** Set up replicas, logging levels, and resource allocations for APIs, workers, routers, and other components.

## Step 4: Apply the Lens manifest file

After configuring the deployment file with the necessary settings and specifications, apply the manifest using the following command:

=== "Command"

    ```bash 
    dataos-ctl resource apply -f ${manifest-file-path}
    ```
=== "Example usage"

    ```bash 
    dataos-ctl resource apply -f /lens/lens_deployment.yml -w curriculum
    # Expected output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying(curriculum) sales360:v1alpha:lens... 
    INFO[0001] 🔧 applying(curriculum) sales360:v1alpha:lens...created 
    INFO[0001] 🛠 apply...complete
    ```

<!-- ## Docker compose manifest file

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

</details> -->



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