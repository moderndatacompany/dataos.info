# Postgres

## Step 1: Create Postgres Depot

If the Depot is not active, create one using the provided template.

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


### **Load data from the data source**

In the `sqls` folder, create `.sql` files for each logical table, where each file is responsible for loading or selecting the relevant data from the source. Ensure that only the necessary columns are extracted, and the SQL dialect is specific to the data source.

For example, a simple data load might look as follows:

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
  "onelakehouse"."retail".customer; #catalog_name
```

### **Define the table in the Model**

Create a `tables` folder to store logical table definitions, with each table defined in a separate YAML file outlining its dimensions, measures, and segments. For example, to define a table for `sales `data:

```yaml
table:
  - name: customers
    sql: {{ load_sql('customers') }}
    description: Table containing information about sales transactions.
```

#### **Add dimensions and measures**

After defining the base table, add the necessary dimensions and measures. For example, to create a table for sales data with measures and dimensions, the YAML definition could look as follows:

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

#### **Add segments to filter**

Segments are filters that allow for the application of specific conditions to refine the data analysis. By defining segments, you can focus on particular subsets of data, ensuring that only the relevant records are included in your analysis. For example, to filter for records where the state is either Illinois or Ohio, you can define a segment as follows:

```yaml
segments:
  - name: state_filter
    sql: "{TABLE}.state IN ('Illinois', 'Ohio')"
```

To know more about segments click [here](https://dataos.info/resources/lens/working_with_segments/).


### **Create views**

Create a `views` folder to store all logical views, with each view defined in a separate YAML file (e.g., `sample_view.yml`). Each view references dimensions, measures, and segments from multiple logical tables. For instance the following`customer_churn` view is created.

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

To know more about the views click [here](https://dataos.info/resources/lens/working_with_views/).


### **Create User groups**

This YAML manifest file is used to manage access levels for the semantic model. It defines user groups that organize users based on their access privileges. In this file, you can create multiple groups and assign different users to each group, allowing you to control access to the model.By default, there is a 'default' user group in the YAML file that includes all users.

```yaml
user_groups:
  - name: default
    description: this is default user group
    includes: "*"
```

To know more about the User groups click [here](https://dataos.info/resources/lens/working_with_user_groups_and_data_policies/)

<aside class="callout">
Push the semantic model folder into the code repository. Before pushing secure the repo credentials by using the Instance Secret and referencing it in the Lens manifest file for secure access.
</aside>

## Step 3: Create the Lens manifest file

After setting up the Lens model folder, the next step is to configure the deployment manifest. Below is the YAML template for configuring a Lens deployment. The below manifest is intended for source-type Depot named `postgresdepot`, created on the Postgres source.

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

</details> -->


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
