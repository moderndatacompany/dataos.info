# Minerva

To create a semantic model across multiple data sources using the Minerva Cluster, several prerequisite steps must be completed. These steps ensure proper setup and secure connections between the data sources and the Minerva Cluster.

## Prerequisites

The following prerequisites are required:

- [Instance Secret](/resources/lens/data_sources/minerva/#create-instance-secret-for-data-source-connection)
- [Active Depot](/resources/lens/data_sources/minerva/#create-postgres-depot-manifes-file)
- [Scanner](/resources/lens/data_sources/minerva/#create-the-scanner-manifest-file)
- [Cluster](/resources/lens/data_sources/minerva/#create-minerva-cluster-manifest-file)

### **Create Instance-Secret for data source connection**

Before establishing a connection to the data source, an [Instance Secret](/resources/instance_secret/) must be created. This secret securely stores the credentials required for `read` (`r`) and `read write` (`rw`) access to the data source.

For instance, to create the Depot for the source Postgres, create the Instance Secret as following:

```yaml title="instance-secret-r.yml"
name: postgres-r 
version: v1 
type: instance-secret 
description: read and write ds appysecret for User postgres db
layer: user 
instance-secret:
  type: key-value-properties 
  acl: r 
  data:
    username: 
    password: 
```

```yaml title="instance-secret-rw.yml"
name: postgres-rw 
version: v1
type: instance-secret 
description: read and write ds appysecret for User postgres db
layer: user 
instance-secret:
  type: key-value-properties 
  acl: rw 
  data:
    username: 
    password: 
```

### **Create Postgres Depot manifest file** 

Create Postgres Depot to set up the connection with the Postgres data source.

```yaml
name: postgres
version: v2alpha
type: depot
layer: user
depot:
  type: jdbc                 
  description: default postgres depot
  external: true
  secrets:
    - name: postgres-rw
      keys: 
        - postgres-rw
      allkeys: true

    - name: postgres-r
      keys: 
        - postgres-r
      allkeys: true
    
  jdbc:
    subprotocol: postgresql
    host: <host_address>  #replace host address with actual host address
    port: 5432
    database: postgres
```


### **Create the Scanner manifest file**

Create a scanner to scan the available dataset in the Postgres Depot and register it in the Metis.

```yaml
version: v1
name: wf-postgres-depot
type: workflow
tags:
  - postgres-depot-scan
description: The job scans schema tables and register data to metis
workflow:
  dag:
    - name: postgres-depot
      description: The job scans schema from postgres depot tables and register data to metis
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        compute: runnable-default
        stackSpec:
          depot: dataos://postgres
```

<aside class="callout">
Similarly, create the Instance Secret, Depot and Scanner for all the sources to be incldued in the semantic model.
</aside>

### **Create Minerva Cluster manifest file**

```yaml
name: minervacluster
version: v1
type: cluster
tags:
  - dataos:type:resource
  - dataos:resource:cluster
  - dataos:layer:user
  - dataos:workspace:public
owner: iamgroot
workspace: public
cluster:
  compute: query-default
  type: minerva
  minerva:
    replicas: 1
    resources:
      requests:
        cpu: 500m
        memory: 1Gi
      limits:
        cpu: 500m
        memory: 1Gi
    depots:
      - address: dataos://postgres?acl=r  #postgres depot created
      - address: dataos://lakehouse?acl=r #another depot
    debug:
      logLevel: INFO
      trinoLogLevel: ERROR
```
## Prepare the semantic model folder

Organize the semantic model folder with the following structure to define tables, views, and governance policies:

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
To know more about segments click [here](/resources/lens/segments/).

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

To know more about the views click [here](/resources/lens/views/).

### **Create user groups**

This YAML manifest file is used to manage access levels for the semantic model. It defines user groups that organize users based on their access privileges. In this file, you can create multiple groups and assign different users to each group, allowing you to control access to the model.By default, there is a 'default' user group in the YAML file that includes all users.

```yaml
user_groups:
  - name: default
    description: this is default user group
    includes: "*"
```

Multiple user groups can be created in the `user_groups.yml` . To know more about the user groups click [here](/resources/lens/user_groups_and_data_policies/).

<aside class="callout">
🗣️ Push the semantic model folder and all other artifacts in a code repository. Secure the code repository by putting the code repository credentials into an Instance Secret. 
</aside>

## Create an Instance Secret manifest file

```yaml
# RESOURCE META SECTION
name: bitbucket-cred # Secret Resource name (mandatory)
version: v1 # Secret manifest version (mandatory)
type: instance-secret # Type of Resource (mandatory)
description: demo-secret read secrets for code repository # Secret Resource description (optional)
layer: user # DataOS Layer (optional)

# INSTANCE SECRET-SPECIFIC SECTION
instance-secret:
  type: key-value # Type of Instance-secret (mandatory)
  acl: r # Access control list (mandatory)
  data: # Data (mandatory)
    GITSYNC_USERNAME: <code_repository_username>
    GITSYNC_PASSWORD: <code_repository_password>
```

## Create a Lens deployment manifest file

After preparing the Lens semantic model create a `lens_deployemnt.yml` parallel to the `model` folder.

```yaml
version: v1alpha
name: "minervalens"
layer: user
type: lens
tags:
  - lens
description: minerva deployment on lens2
lens:
  compute: runnable-default
  secrets:
    - name: bitbucket-cred #repo-cred
      allKeys: true
  source:
    type: minerva #minerva/themis/depot
    name: minervacluster  #name of minerva cluster
    catalog: lakehouse
  repo:
    url: https://bitbucket.org/tmdc/sample
    lensBaseDir: sample/lens/source/minerva/model 
    # secretId: lens2_bitbucket_r
    syncFlags:
      - --ref=lens
```

The manifest file provided is designed for a Cluster named `minervacluster`, created on the `Minerva` source, with a data catalog named `lakehouse`. To utilize this manifest, duplicate the file and update the source details as needed.

Each section of the YAML template outlines essential elements of the Lens deployment. Below is a detailed breakdown of its components:

* **Defining the source:**

      * **`type`:**  The `type` attribute in the `source` section must be explicitly set to `minerva`.

      * **`name`:** The `name` attribute in the `source` section should specify the name of the Minerva Cluster. For example, if the name of your Minerva Cluster is `minervacluster` the Source name would be `minervacluster`.

      * **`catalog`:** The `catalog` attribute must define the specific catalog name within the Minerva Cluster that you intend to use. For instance, if the catalog is named `lakehouse`, ensure this is accurately reflected in the catalog field.

* **Defining repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/cluster/minerva/model`.

      * **`secretId`:**  The `secretId` attribute is used to access private repositories (e.g., Bitbucket, GitHub). It specifies the secret needed to authenticate and access the repository securely.

      * **`syncFlags`**:  Specifies additional flags to control repository synchronization. Example: `--ref=dev` specifies that the Lens model resides in the `dev` branch.

* **Configure API, Worker, and Metric Settings (Optional):** Set up replicas, logging levels, and resource allocations for APIs, workers, routers, and other components.

The above YAML manifest is intended for a Cluster named `minervacluster`, created on the minerva source, with the data catalog named `lakehouse`. To use this manifest file, copy the file and update the source details accordingly.

<aside class="callout">
🗣️ Within the Themis and Minerva cluster, all depots (such as Lakehouse, Redshift, Snowflake, etc.) are integrated. When configuring Lens, specify one Depot in the `catalog` field, as Lens can connect to and utilize depots from all sources available in the Themis cluster.
</aside>



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


<aside class="callout">

Once the Lens Resource is applied and all configurations are correctly set up, the Lens model will be deployed. Upon deployment, a Lens Service is created in the backend, which may take some time to initialize.

To verify whether the Lens Service is running, execute the following command. The Service name follows the pattern: **`<lens-name>-api`**

Ensure Service is active and running before proceeding to the next steps.

```bash
dataos-ctl get -t service -n sales-insights-lens-api -w public
# Expected output:
INFO[0000] 🔍 get...                                     
INFO[0002] 🔍 get...complete                             

           NAME           | VERSION |  TYPE   | WORKSPACE | STATUS |  RUNTIME  |    OWNER     
--------------------------|---------|---------|-----------|--------|-----------|--------------
  sales360-lens-api | v1      | service | public    | active | running:1 | iamgroot
```

</aside>



<!--  ## Docker compose manifest file

<details>

  <summary>Docker compose manifest file for local testing</summary>

```yaml
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-monkey.dataos.app

  # Overview
  LENS2_NAME: minervalens
  LENS2_DESCRIPTION: Description 
  LENS2_TAGS: Provide tags
  LENS2_AUTHORS: creator of lens
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  
  # Data Source
  LENS2_SOURCE_TYPE: minerva  #themis, depot
  LENS2_SOURCE_NAME: minervacluster  #cluster name
  LENS2_SOURCE_CATALOG_NAME: icebase   #depot name, specify any catalog
  DATAOS_RUN_AS_APIKEY: *****
  
  #LENS2_DB_SSL: true
  #MINERVA_TCP_HOST: tcp.liberal-donkey.dataos.app
  
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
``` -->
<!-- 
</details>

Follow these steps to create the `docker-compose.yml`:

- Step 1: Create a `docker-compose.yml` manifest file.
- Step 2: Copy the template from above and paste it in a code.
- Step 3: Fill the values for the atttributes/fields declared in the manifest file as per the Minerva source.

**Required Minerva Depot source attributes**

```yaml
LENS2_SOURCE_TYPE: minerva  #themis, depot
LENS2_SOURCE_NAME: minervacluster  #cluster name
LENS2_SOURCE_CATALOG_NAME: icebase   #depot name, specify any catalog
DATAOS_RUN_AS_APIKEY: *****
``` -->
<!-- 
## Connecting to Minerva without Depot/Cluster 

<aside class="callout">
🗣️ When deploying Lens in DataOS, you need to connect to the source via the depot/cluster. The below configs are best suited for testing Locally. Otherwise, it is recommended that you connect via depot/cluster.
</aside>

### **Prerequisites**

- The hostname for the Trino database server.
- The username for the DataOS User.
- The name of the database to use with the Minerva query engine database server.

### **`.env` Configuration**

Add the following environment variables to your Lens (.env) file

=== "Syntax"

    ```yaml
    # Trino configuration
    LENS2_DB_TYPE=trino
    LENS2_DB_HOST=tcp.${DATAOS_FQDN}
    LENS2_DB_USER=${DATAOS_USER_NAME}
    LENS2_DB_PASS=${DATAOS_WRAP_TOKEN}
    LENS2_DB_PRESTO_CATALOG=${CATALOG_NAME}
    LENS2_DB_PORT=${PORT_NUMBER}
    ```
=== "Sample"

    ```yaml
    # Trino configuration
    LENS2_DB_TYPE=trino
    LENS2_DB_HOST="tcp.alpha-omega.dataos.app"
    LENS2_DB_USER="iamgroot"
    LENS2_DB_PASS="abcdefghijklmnopqrstuvwxyz"
    LENS2_DB_PRESTO_CATALOG="icebase"
    LENS2_DB_PORT=7432
    ```
**Sample environment variable file configuration**
    
```yaml
LENS2_VERSION=0.35.55-01 

# Minerva configuration
LENS2_DB_HOST=tcp.alpha-omega.dataos.app
LENS2_DB_PORT=7432
LENS2_DB_USER=iamgroot
LENS2_DB_PASS="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwzyz"
LENS2_DB_PRESTO_CATALOG=icebase
LENS2_DB_SSL=true
LENS2_DB_TYPE=trino

# Meta information
LENS2_NAME=trinolens # fetch from CLI
LENS2_DESCRIPTION="Trino lens generated"
LENS2_TAGS="lens2, sales, customer insights"
LENS2_AUTHORS="iamgroot"

LENS2_DEV_MODE="true"
LENS2_SCHEMA_PATH=model

LENS2_LOG_LEVEL="error"
LENS2_LOADER_LOG_LEVEL="error"
CACHE_LOG_LEVEL="error" # not there in Kishan's

DATAOS_FQDN=alpha-omega.dataos.app
DATAOS_USER_NAME=iamgroot
DATAOS_USER_APIKEY=abcdeghijklmopqrstuvwxyz

LENS2_DEPOT_SERVICE_URL="https://alpha-omega.dataos.app/ds" 
LENS2_HEIMDALL_BASE_URL="https://alpa-omega.dataos.app/heimdall" 

LENS2_SOURCE_TYPE=trino
LENS2_SOURCE_NAME=system
LENS2_SOURCE_CATALOG_NAME=icebase 

LENS2_BASE_URL="http://localhost:4000/lens2/api"
LENS2_META_PATH="/v2/meta"
LENS2_RILL_PATH=boards
LENS2_CHECKS_PATH=checks
LENS2_BOARD_PATH=boards
```

### **Environment variables Attributes**

| **Environment Variable** | **Description** | **Possible Values** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| `LENS2_DB_TYPE` | The type of database | trino | trino | ✅ |
| `LENS2_DB_HOST` | The host URL for the database | A valid database host URL of the form `tcp.${DATAOS-FQDN}` where `${DATAOS-FQDN}` is the placeholder for DataOS’ fully qualified domain name. Replace the placeholder with your respective domain name. | `tcp.alpha-omega.dataos.app` | ✅ |
| `LENS2_DB_PORT` | The port for the database connection | A valid port number | `7432` | ❌ |
| `LENS2_DB_USER` | The DataOS user-id used to connect to the database. It can be retrieved from the second column of the output by running the `dataos-ctl user get` command from the DataOS CLI | A valid DataOS user-id | `iamgroot` | ✅ |
| `LENS2_DB_PASS` | The DataOS Wrap Token that serves as a password used to connect to the database | A valid Cluster Wrap Token. Learn more about how to create a Cluster Wrap Token [**here.**](/interfaces/atlas/bi_tools/tableau/#generate-dataos-api-token) | `abcdefghijklmnopqrstuvwxyz` | ✅ |
| `LENS2_DB_PRESTO_CATALOG` | The catalog within Trino/Presto to connect to | A valid catalog name within the Trino/Presto database | `icebase` | ✅ |
| `LENS2_DB_SSL` | If `true`, enables SSL encryption for database connections from Lens2. | `true`, `false` | `true` | ❌ | -->
<!-- 
### **Example**

[trino.zip](/resources/lens/data_sources/trino/trino.zip)

## Check Query Stats for Minerva

<aside class="callout">
💡 Please ensure you have the required permission to access the Operations.
</aside>

To check the query statistics, please follow the steps below:

1. **Access Minerva Queries**
    
  Navigate to the operation section, then go to Minerva queries. Set the filters as follows:
    
    - Source: `lens2`
    - Dialect: `trino_sql`
    - You can also filter by cluster, username, and other criteria as per your choice.

    <div style="text-align: center;">
        <img src="/resources/lens/data_sources/minerva/Untitled1.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
    </div>

2. **Select the Query ID**
      
    Choose the query ID you are interested in. You will then be able to check the statistics, as shown in the example below:
      
    <div style="text-align: center;">
        <img src="/resources/lens/data_sources/minerva/Untitled1.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
    </div> -->
