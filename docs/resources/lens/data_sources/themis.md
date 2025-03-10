# Themis


## Connecting to Themis using Depot/Cluster 

## Prerequisite

Ensure you have an active and running Minerva Cluster.

## Step 1: Prepare the Lens model folder

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

For example, a simple data load from `Postgres` source might look as follows:

```sql
SELECT
    customer_id as p_customer_id,
    cast(purchase_date as timestamp) as purchase_date,
    recency as recency_in_days,
    mntwines,
    mntmeatproducts,
    mntfishproducts,
    mntsweetproducts,
    mntgoldprods,
    mntfruits,
    numdealspurchases,
    numwebpurchases,
    numcatalogpurchases,
    numstorepurchases,
    numwebvisitsmonth,
    numwebpurchases + numcatalogpurchases + numstorepurchases + numstorepurchases as purchases,
    (mntwines+mntmeatproducts+mntfishproducts+mntsweetproducts+mntgoldprods+mntfruits) as spend
FROM
    postgres.public.purchase_data
```

Similarly, to load the data from another source `lakehouse` the sql looks as follows:

```sql
SELECT 
    customer_id, 
    birth_year, 
    education, 
    marital_status, 
    income, 
    country 
FROM 
    lakehouse.customer_relationship_management.customer_data
```
### **Define the table in the model**

Create a `tables` folder to store logical table definitions, with each table defined in a separate YAML file outlining its dimensions, measures, and segments. For example, to define a table for `cutomer `data:

```yaml
tables:
  - name: customer
    sql: {{ load_sql('customer') }}
    description: "This table stores key details about the customers, including their personal information, income, and classification into different risk segments. It serves as the central reference point for customer-related insights."
    public: true
```

### **Add dimensions and measures**

After defining the base table, add the necessary dimensions and measures. For example, to create a table for sales data with measures and dimensions, the YAML definition could look as follows:

```yaml
tables:
  - name: customer
    sql: {{ load_sql('customer') }}
    description: "This table stores key details about the customers, including their personal information, income, and classification into different risk segments. It serves as the central reference point for customer-related insights."
    public: true

    joins:
      - name: purchase
        relationship: one_to_many
        sql: "{TABLE.customer_id}= {purchase.p_customer_id}"
        
    dimensions:   
      - name: customer_id
        type: number
        column: customer_id
        description: "The unique identifier for each customer."
        primary_key: true
        public: true

      #...

    measures:
      - name: total_customers
        sql: "COUNT( Distinct {customer_id})"
        type: number
        description: "The total number of customers in the dataset, used as a basic measure of customer volume."
```

### **Add segments to filter**

Segments are filters that allow for the application of specific conditions to refine the data analysis. By defining segments, you can focus on particular subsets of data, ensuring that only the relevant records are included in your analysis. For example, to filter for records where the state is either Illinois or Ohio, you can define a segment as follows:

```yaml
#..
segments:
  - name: country_india
    sql: country = 'India'
```
To know more about segments click [here](o/resources/lens/working_with_segments/).

### **Create the views**

Create a `views` folder to store all logical views, with each view defined in a separate YAML file (e.g., `sample_view.yml`). Each view references dimensions, measures, and segments from multiple logical tables. For instance the following`total_spend` view is created.

```yaml
views:
  - name: total_spending
    description: This metric measures how many marketing campaigns a customer has engaged with. 
    public: true
    meta:
      title: Customer Spending by Product Category
      tags:   
        - DPDomain.Marketing
        - DPUsecase.Customer Segmentation
        - DPUsecase.Product Recommendation
        - DPTier.Consumer Aligned
      metric:
        expression: "*/45  * * * *"
        timezone: "UTC"
        window: "day"
        excludes: 
         - spend
    tables:
      - join_path: purchase
        prefix: true
        includes:
          - purchase_date
          - customer_id
          - total_spend
          - spend

      - join_path: product
        prefix: true
        includes:
          - product_category
          - product_name
```

To know more about the views click [here](/resources/lens/working_with_views/).

### **Create user groups**

This YAML manifest file is used to manage access levels for the semantic model. It defines user groups that organize users based on their access privileges. In this file, you can create multiple groups and assign different users to each group, allowing you to control access to the model.By default, there is a 'default' user group in the YAML file that includes all users.

```yaml
user_groups:
  - name: default
    description: this is default user group
    includes: "*"
```

Multiple user groups can be created in the `user_groups.yml` . To know more about the user groups click [here](/resources/lens/working_with_user_groups_and_data_policies/).

<aside class="callout">
🗣️ Push the semantic model folder and all other artifacts in a code repository. Secure the code repository by putting the code repository credentials into an Instance Secret. 
</aside>

## Create Lens manifest file

After preparing the Lens semantic model create a `lens_deployemnt.yml` parallel to the `model` folder.

```yaml
version: v1alpha
name: "themis-lens"
layer: user
type: lens
tags:
  - lens
description: themis lens deployment on lens2
lens:
  compute: runnable-default
  secrets:
    - name: bitbucket-cred
      allKeys: true
  source:
    type: themis #minerva/themis/depot
    name: lenstestingthemis
    catalog: icebase
  repo:
    url: https://bitbucket.org/tmdc/sample
    lensBaseDir: sample/lens/source/themis/model 
    # secretId: lens2_bitbucket_r
    syncFlags:
      - --ref=main #repo-name
```

The YAML manifest provided is designed for a cluster named `themiscluster`, created on the `Themis` source, with a data catalog named `icebase`. To utilize this manifest, duplicate the file and update the source details as needed.

Each section of the YAML template outlines essential elements of the Lens deployment. Below is a detailed breakdown of its components:

* **Defining the Source:**

      * **`type`:**  The `type` attribute in the `source` section must be explicitly set to `themis`.

      * **`name`:** The `name` attribute in the `source` section should specify the name of the Themis Cluster. For example, if the name of your Themis Cluster is `clthemis` the Source name would be `clthemis`.

      * **`catalog`:** The `catalog` attribute must define the specific catalog name within the Themis Cluster that you intend to use. For instance, if the catalog is named `lakehouse_retail`, ensure this is accurately reflected in the catalog field.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/awsredshift/model`.

      * **`secretId`:**  The `secretId` attribute is used to access private repositories (e.g., Bitbucket, GitHub). It specifies the secret needed to authenticate and access the repository securely.

      * **`syncFlags`**:  Specifies additional flags to control repository synchronization. Example: `--ref=dev` specifies that the Lens model resides in the `dev` branch.

* **Configure API, Worker, and Metric Settings (Optional):** Set up replicas, logging levels, and resource allocations for APIs, workers, routers, and other components.


The above manifest is intended for a cluster named `lenstestingthemis`, created on the themis source, with the Depot or data catalog named `icebase`. To use this manifest, copy the file and update the source details accordingly.

<aside class="callout">
🗣️ Within the Themis and Minerva cluster, all depots (such as Icebase, Redshift, Snowflake, etc.) are integrated. When configuring Lens, you only need to specify one Depot in the `catalog` field, as Lens can connect to and utilize depots from all sources available in the Themis cluster.
</aside>



<!-- ## Docker compose manifest file

<details>

  <summary>Docker compose manifest file for local testing</summary>

```yaml hl_lines="15-18"
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-donkey.dataos.app

  # Overview
  LENS2_NAME: themislens
  LENS2_DESCRIPTION: Description 
  LENS2_TAGS: Provide tags
  LENS2_AUTHORS: creator of lens
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  
  # Data Source
  LENS2_SOURCE_TYPE: themis  #minerva, depot
  LENS2_SOURCE_NAME: lenstestingthemis  #cluster name
  LENS2_SOURCE_CATALOG_NAME: icebase   #depot name, specify any catalog
  DATAOS_RUN_AS_APIKEY: ***** #dataos apikey
  
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
    image: rubiklabs/lens2:0.35.60-20 
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

<!-- While deploying Lens, adjust the configuration using the environment variables below according to the load.


| **Environment Variable** | **Description** | **Possible Values** | **Required** | **When should these env variables be used** |
|--------------------------|-----------------|---------------------|--------------|---------------------------------------------|
| `LENS2_DB_SSL`            | If `true`, enables SSL encryption for database connections from Cube. | `true`, `false` | ❌ | When SSL encryption for database connections is required to ensure security. |
| `LENS2_CONCURRENCY`       | The number of concurrent connections each queue has to the database. Default is `4`. | A valid number | ❌ | When adjusting the number of parallel operations or queries to the database is needed to optimize performance based on workload and database capabilities. Increasing the value can enhance throughput, while decreasing it can reduce load. |
| `LENS2_DB_MAX_POOL`       | The maximum number of concurrent database connections to pool. Default is `16`. | A valid number | ❌ | When managing the maximum number of concurrent database connections to ensure efficient resource utilization and prevent overloading the database server. Adjust according to the application’s connection needs and the database server’s capacity. | -->


<!-- 
## Connecting to Themis without Depot/Cluster 

<aside class="callout">
🗣️ When deploying Lens in DataOS, you need to connect to the source via the depot/cluster. The below configs are best suited for testing Locally. Otherwise, it is recommended that you connect via depot/cluster.
</aside>

### **Prerequisites**

- The host for the Themis database server.
- The username for the DataOS User.
- The name of the database to use with the Themis query engine database server.

### **`.env` configuration** 

Add the following environment variables to your Lens (.env) file

=== "Syntax"

    ```yaml
    # Themis query engine configuration
    LENS2_DB_TYPE=themis
    LENS2_DB_HOST=tcp.${DATAOS_FQDN}
    LENS2_DB_PORT=${PORT_NUMBER}
    LENS2_DB_USER=${DATAOS_USER_NAME}
    LENS2_DB_PASS=${DATAOS_WRAP_TOKEN}
    LENS2_DB_PRESTO_CATALOG=${CATALOG_NAME}
    LENS2_DB_SSL=${ENABLE_SSL}

    ```

=== "Sample"

    ```yaml
    # Themis query engine configuration
    LENS2_DB_TYPE=themis
    LENS2_DB_HOST=tcp.alpha-omega.dataos.app
    LENS2_DB_PORT=7432
    LENS2_DB_USER=iamgroot
    LENS2_DB_PASS="abcdefghijklmopqrstuvwyzabcdefghijklmopqrstuvwxyz"
    LENS2_DB_PRESTO_CATALOG=icebase
    LENS2_DB_SSL=true
    ```

**Sample environment variable file configuration**
    
```yaml
LENS2_VERSION=0.34.60-10-scratch2
LENS2_CACHE_VERSION=0.34.60-amd64v8

# source
LENS2_DB_HOST=tcp.alpha-omega.dataos.app
LENS2_DB_PORT=7432
LENS2_DB_USER=iamgroot
LENS2_DB_PASS=mypassword
LENS2_DB_PRESTO_CATALOG=adventureworks
LENS2_DB_SSL=true
LENS2_DB_TYPE=themis

LENS2_NAME=themislens
LENS2_DESCRIPTION="Ecommerce use case on sales data"
LENS2_TAGS="lens2, ecom, sales and customer insights"
LENS2_AUTHORS="iamgroot, thor"
LENS2_LOG_LEVEL=trace
LENS2_LOADER_LOG_LEVEL=debug

LENS2_HEIMDALL_BASE_URL="https://alpha-omega.dataos.app/heimdall"

LENS2_SCHEDULED_REFRESH_DEFAULT="false"
LENS2_API_SECRET=1245ABDJSJDIR56

CACHE_TELEMETRY=false
CACHE_LOG_LEVEL=error
LENS2_BOARD_PATH=boards
LENS2_BASE_URL="http://localhost:4000/lens2/api"
LENS2_META_PATH="/v2/meta"
LENS2_RILL_PATH=boards
LENS2_CHECKS_PATH=checks

DATAOS_USER_APIKEY="abcdefghijklmnopqrstuvwxyz"
DATAOS_USER_NAME="iamgroot"

LENS2_LOCAL_PG_DB_NAME=db
LENS2_LOCAL_PG_HOST=localhost
LENS2_LOCAL_PG_PORT=15432
LENS2_LOCAL_PG_PASSWORD="abcdefghijklmnopqrstuvwxyz"
LENS2_LOCAL_PG_USER=iamgroot
```
    
### **Environment variables attributes**

| **Environment Variable** | **Description** | **Possible Values** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| `LENS2_DB_TYPE` | The type of database to connect to | themis | themis | ✅ |
| `LENS2_DB_HOST` | The host URL for the database | A valid database host URL of the form `tcp.${DATAOS-FQDN}` where `${DATAOS-FQDN}` is the placeholder for DataOS’ fully qualified domain name. Replace the placeholder with your respective domain name. | `tcp.alpha-omega.dataos.app` | ✅ |
| `LENS2_DB_PORT` | The port for the database connection | A valid port number | `7432` | ❌ |
| `LENS2_DB_USER` | The DataOS user-id used to connect to the database. It can be retrieved from the second column of the output by running the `dataos-ctl user get` command from the DataOS CLI | A valid DataOS user-id | `iamgroot` | ✅ |
| `LENS2_DB_PASS` | The DataOS Wrap Token that serves as a password used to connect to the database | A valid Cluster Wrap Token.| `abcdefghijklmnopqrstuvwxyz` | ✅ |
| `LENS2_DB_PRESTO_CATALOG` | The catalog within Themis to connect to | A valid catalog name  | `icebase` | ✅ |
| `LENS2_DB_SSL` | If `true`, enable SSL encryption for database connections from Lens2. | `true`, `false` | `true` | ❌ |
| `LENS2_CONCURRENCY` | The number of concurrent connections each queue has to the database. Default is `2` | 3,4 | `2` |  |
| `LENS2_DB_MAX_POOL` | The maximum number of concurrent database connections to pool. Default is `8` | 9,10 |   `8` |  | -->
<!-- 
## Check Query Stats for Themis

<aside class="callout">
💡 Please ensure you have the required permission to access the Operations.
</aside>

To check the query statistics, please follow the steps below:

1. **Access the Themis Cluster**

      Navigate to the Themis cluster. You should see a screen similar to the image below:

    <div style="text-align: center;">
      <img src="/resources/lens/data_sources/Themis/Untitled(7).png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
    </div>

2. **Select the Running Driver**
    
    Choose the running driver. **This driver will always be the same, regardless of the user, as queries will be directed to the creator of the Themis cluster**. The running driver remains consistent for all users.
    
    <div style="text-align: center;">
        <img src="/resources/lens/data_sources/Themis/Untitled(9).png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
    </div>


3. **View the Spark UI**
    
    Go to terminal and use the following command to view the spark UI :
      

```yaml
dataos-ctl -t cluster -w public -n themislens --node themis-themislens-iamgroot-default-a650032d-ad6b-4668-b2d2-cd372579020a-driver view sparkui

**dataos-ctl -t cluster -w public -n themis_cluster_name --node  driver_name view sparkui**
```

You should see the following interface:

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/Themis/Untitled(9).png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>
 -->
