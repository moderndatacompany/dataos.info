# Creating a semantic model on Snowflake Depot

<aside class="callout">

When setting up a semantic model, it is crucial to understand that the semantic model is part of the Data Product. Therefore, no need to create a separate Git repository. Instead, semantic model will be in the <code>/build</code> folder of the the Data Product's existing repository. 
</aside>

## Pre-requisites for creating a semantic model

### **DataOS requirements**

Ensure you meet the following requirements specific to DataOS:

1. To create and access all DataOS resources and the Data Product, a user must possess the `roles:id:data-dev` tag, or any tag designated by the organization for such access. To obtain this tag, please contact your DataOS Administrator. You can view the available tags by executing the following command in the DataOS CLI terminal. For more information on tags, please refer to the following link.

    ```bash
    dataos-ctl user get
    ```

    Expected output:

    ```bash
    INFO[0000] 😃 user get...                                
    INFO[0001] 😃 user get...complete                        

          NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
    ───────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
        iam groot  │  iamgroot   │ person │   iamgroot@tmdc.io   │ roles:id:data-dev,                          
                   │             │        │                      │ roles:id:user,                  
                   │             │        │                      │ users:id:iamgroot 
    ```

2. Alternatively, instead of assigning the tag, a user can be assigned the particular use cases built for the specific purpose for Lens creation. Following are the use-cases for reading and creating Lens in DataOS. 

      - `Read Lens`
      - `Manage Lens`
      - `View Lens2 App`
      - `Manage Lens2 Backend`
      - `Read Lens2 Backend`

    Learn more about use cases by referring to this [link](/interfaces/bifrost/use_cases/).

3. DataOS CLI Version should be `dataos-cli 2.26.39` or greater. Check current CLI version using the below command:

    ```bash
    dataos-ctl version
    ```

    Expected output:

    ```bash
      _____            _              ____     _____  
    |  __ \          | |            / __ \   / ____| 
    | |  | |   __ _  | |_    __ _  | |  | | | (___   
    | |  | |  / _` | | __|  / _` | | |  | |  \___ \  
    | |__| | | (_| | | |_  | (_| | | |__| |  ____) | 
    |_____/   \__,_|  \__|  \__,_|  \____/  |_____/  
                                                      
    ctl-version     : dataos-cli 2.26.39 62d502dd7d957e7ed13ae5e750d4fa4fa5fca8d1
    product-version : DataOS® draco-1.22.12
    hub-fqdn        : dataos-training.dataos.app
    hub-tcp-fqdn    : tcp.dataos-training.dataos.app
    cloud-provider  : azure
    ```

    Please reach out to your Modern executive for assistance in updating the CLI.

4. It is recommended that the configuration files of the semantic model or Lens be stored in a Bitbucket/Github repository for better collaboration, as shown below, while building the Data Product. 

    ```
    data-product-deployment
    └──── data_product
            ├── depot
            │   └──depot.yaml
            ├── scanner
            │   ├── depot_scanner.yaml
            │   └── dp_scanner.yaml
            ├── semantic_model
            │   ├── model
            │   │   ├── sqls
            │   │   │   └── sales.sql  # SQL script for table dimensions
            │   │   ├── tables
            │   │   │   └── table1.yml  # Logical table definition (dimensions, measures)
            │   │   ├── views
            │   │   │   └── view1.yml  # Logical views referencing tables
            │   │   └── user_groups.yml  # User group policies for governance
            │   └── lens_deployment.yaml
            ├── bundle
            │   └── bundle.yaml   
            └── dp_deployment.yaml
    ```

    Notice that the semantic model directory, which is part of the Data Product, contains the Semantic Model (Lens) configuration. This includes SQL scripts for defining tables, logical views, user group policies, and Lens deployment manifest file needed for successful integration into the Data Product consumption layer. By storing these files in a version-controlled repository, teams can better manage, collaborate, and track changes to the Data Product’s components throughout its lifecycle.

### **Snowflake requirement**

Since Lens is created on Snowflake as the source, the data remains in the source, and queries are executed within the Snowflake system itself. Only the metadata is ingested into Data OS for the creation of the Data Product. This means Lens utilizes Snowflake’s native query engine to run queries directly on the Snowflake source.

To ensure smooth query execution, sufficient computing and storage permissions are required. Learn more about access control in Snowflake by referring to this link.
Sufficient computing and storage permissions are needed to run queries. Learn more about access control in Snowflake by referring to this [link](https://docs.snowflake.com/en/user-guide/security-access-control-privileges).


## Step 1: Create Instance Secret to securely store Snowflake credentials

To securely store Snowflake credentials, two Instance Secrets must be created for read-write access:

- Read-only Instance Secret

- Read-write Instance Secret

<aside class="callout">
Make sure to keep these Instance Secret manifest files stored locally and avoid pushing them to the code repository.
</aside>

1. The following manifest files are provided as templates. Simply update them with your credentials and use them to create the corresponding instance secrets.

  ```yaml title="instance-secret-r.yml"
  name: snowflake-r
  version: v1
  type: instance-secret
  description: "The purpose of secret to mount the snowflake"
  layer: user
  instance-secret:
    type: key-value-properties
    acl: r
    data:
      username: "<username>" # username of the snowflake account
      password: "<password>" # password of the snowflake account
  ```

  ```yaml title="instance-secret-rw.yml"
  name: snowflake-rw
  version: v1
  type: instance-secret
  description: "The purpose of secret to mount the snowflake"
  layer: user
  instance-secret:
    type: key-value-properties
    acl: rw
    data:
      username: "<username>" # username of the snowflake account
      password: "<password>" # password of the snowflake account
  ```

2. Apply the read-only Instance Secret manifest file by executing the command below.

  ```bash
  dataos-ctl apply -f <manifest-file-path>
  ```

  Expected output:

  ```bash
  INFO[0000] 🛠 apply...                                   
  INFO[0000] 🔧 applying snowflake-r:v1:instance-secret... 
  INFO[0002] 🔧 applying snowflake-r:v1:instance-secret...created
  INFO[0002] 🛠 apply...complete
  ```

  Similarly apply the read write Instance Secret manifest file for access.

  ```bash
  dataos-ctl apply -f <manifest-file-path>
  ```

  Expected output:

  ```bash
  INFO[0000] 🛠 apply...                                   
  INFO[0000] 🔧 applying snowflake-rw:v1:instance-secret... 
  INFO[0002] 🔧 applying snowflake-rw:v1:instance-secret...created
  INFO[0002] 🛠 apply...complete
  ```

## Step 2: Set up a connection with source

To set up a connection with the source, create Depot if the Depot has already been created and activated during the Design phase of the Data Product, skip this step. The semantic model will utilize the existing Depot and the associated Instance Secrets set up. Ensure the Depot is properly connected to the correct data source and that you have the necessary access credentials (Instance Secrets) configured for the Lens deployment.

The following information is required to connect the Snowflake with DataOS using Depot Resource:

| **Field**    | **Description**                                                                                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **warehouse**| The Snowflake warehouse that will be accessed.                                                                                                                  |
| **url**      | The URL to connect to the Snowflake instance, typically formatted as `https://<orgname>-<account_name>.snowflakecomputing.com`.                                  |
| **database** | The specific Snowflake database to be used.                                                                                                                     |
| **account**  | The Snowflake account identifier, which is related to the URL (e.g., the part of the URL before `snowflakecomputing.com`).                                      |

After configuring Depot with the above configurations the Depot manifest file look as follows:

```yaml title="snowflake-depot.yml" hl_lines="22-27"
name: snowflake
version: v2alpha
type: depot
tags:
  - Snowflake depot
  - user data
layer: user
depot:
  name: snowflake
  type: snowflake
  description: Depot to fetch data from Snowflake datasource
  secrets:
    - name: snowflake-r
      keys:
        - snowflake-r
      allKeys: true
    - name: snowflake-rw
      keys:
        - snowflake-rw
      allKeys: true
  external: true
  snowflake:
    database: TMDC_V1
    url: ABCD23-XYZ8932.snowflakecomputing.com  # dont use https:// 
    warehouse: COMPUTE_WH
    account: ABCD23-XYZ8932
  source: snowflake
```

## Step 3: Extract the metadata 

To access the metadata of the snowflake data on Metis UI, the user must create a Scanner Workflow that scans the metadata from the source (Depot) and stores it in Metis DB.

```yaml
version: v1
name: snowflake-depot-scanner
type: workflow
tags:
  - Scanner
title: Scan snowflake-depot
description: |
  The purpose of this workflow is to scan snowflake and see if scanner works fine with a snowflake of depot.
workflow:
  dag:
    - name: scan-snowflake-db
      title: Scan snowflake db
      description: |
        The purpose of this job is to scan gateway db and see if scanner works fine with a snowflake type of depot.
      tags:
        - Scanner
      spec:
        stack: scanner:2.0
        compute: runnable-default
        stackSpec:
          depot: snowflake # snowflake depot name
```

Apply the Scanner Workflow by executing the command below.

```bash
dataos-ctl resource apply -f /home/data_product/depot/scanner.yaml -w public
```


## Step 3: Prepare the semantic model folder inside the cloned Data Product repository

Organize the semantic model folder with the following structure to define tables, views, and governance policies:

```
semantic_model
└── model
│   └── sample.sql  # SQL script for table dimensions
├── tables
│   └── sample_table.yml  # Logical table definition (joins, dimensions, measures, segments)
├── views
│   └── sample_view.yml  # Logical views referencing tables
└── user_groups.yml  # User group policies for governance
```

### **Load data from the data source**

In the sqls folder, create a `.sql` file for each logical table. Each file should be responsible for loading or selecting the relevant data from the source, using Snowflake-compatible SQL synta such as table names are formatted as schema.table.

For example, a simple data load might look as follows:

```sql
SELECT
  *
FROM
  "retail".channel;
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
  "retail".customer;
```

### **Define the table in the model**

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
    sql: {{ load_sql('customer') }}
    description: Table containing sales records with order details.

    dimensions:
      - name: order_id
        type: number   #data type of dimension possible values - string, number, time, boolean
        description: Unique identifier for each order.
        column: order_id       # References the column defined in the table’s SQL.
        primary_key: true   #set the given dimension as primary key
        public: true # to control the visibility of the dimension. By default it is true.

    measures:
      - name: total_orders_count  
        type: count   # type of measure column : time, string, number, boolean, count, sum, count_distinct, count_distinct_approx, avg, min, max
        sql: id      #references the column used to calculate the measure
        description: Total number of orders.
```
Know more about [dimensions](/resources/lens/concepts/#dimensions) and [measures](/resources/lens/concepts/#measures).

#### **Add segments to filter**

Segments are filters that allow for the application of specific conditions to refine the data analysis. By defining segments, you can focus on particular subsets of data, ensuring that only the relevant records are included in your analysis. For example, to filter for records where the state is either Illinois or Ohio, you can define a segment as follows:

```yaml
segments:
  - name: state_filter
    sql: "{TABLE}.state IN ('Illinois', 'Ohio')"  #Here {TABLE} refers to the current table (jinja templating)
```

To know more about segments click [here](/resources/lens/segments/).


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

To know more about the views click [here](/resources/lens/views/).

### **Create user groups**

This YAML manifest file is used to manage access levels for the semantic model. It defines user groups that organize users based on their access privileges. In this file, you can create multiple groups and assign different users to each group, allowing you to control access to the model. By default, there is a 'default' user group in the YAML file that includes all users.

```yaml
user_groups:
  - name: default
    description: this is default user group
    includes: "*"  # refers all users. you can always give the list of users in the form of tag example users:id:iamgroot
```

To know more about the User groups click [here](/resources/lens/user_groups_and_data_policies/)

## Step 3: Deployment manifest file

After setting up the semantic model folder, the next step is to configure the deployment manifest. Below is the YAML template for configuring a Lens deployment.

```yaml
# RESOURCE META SECTION
version: v1alpha # Lens manifest version (mandatory)
name: "snowflake-lens" # Lens Resource name (mandatory)
layer: user # DataOS Layer (optional)
type: lens # Type of Resource (mandatory)
tags: # Tags (optional)
  - lens
description: snowflake depot lens deployment on lens2 # Lens Resource description (optional)

# LENS-SPECIFIC SECTION
lens:
  compute: runnable-default # Compute Resource that Lens should utilize (mandatory)
  secrets: # Referred Instance-secret configuration (**mandatory for private code repository, not required for public repository)
    - name: bitbucket-cred # Referred Instance Secret name (mandatory)
      allKeys: true # All keys within the secret are required or not (optional)

  source: # Data Source configuration
    type: depot # Source type is depot here
    name: snowflake-depot # Name of the snowflake depot

  repo: # Lens model code repository configuration (mandatory)
    url: https://bitbucket.org/tmdc/sample # URL of repository containing the Lens model (mandatory)
    lensBaseDir: sample/lens/source/depot/snowflake/model # Relative path of the Lens 'model' directory in the repository (mandatory)
    syncFlags: # Additional flags used during synchronization, such as specific branch.
      - --ref=lens # Repository Branch
```

Each section of the YAML template defines key aspects of the Lens deployment. Below is a detailed explanation of its components:

* **Defining the Source:**

      * **Source type:**  The `type` attribute in the `source` section must be explicitly set to `depot`.

      * **Source name:** The `name` attribute in the `source` section should specify the name of the Snowflake Depot created.


* **Setting Up Compute and Secrets:**

      * Define the compute settings, such as which engine (e.g., `runnable-default`) will process the data.

      * Include any necessary secrets (e.g., credentials for Bitbucket or AWS) for secure access to data and repositories.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the semantic model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the semantic model. Example: `sample/lens/source/depot/snowflake/model`.

      * **`secretId`:**  The `secretId` attribute is used to access private repositories (e.g., Bitbucket, GitHub) . It specifies the secret needed to securely authenticate and access the repository.

      * **`syncFlags`**:  Specifies additional flags to control repository synchronization. Example: `--ref=dev` specifies that the semantic model resides in the `dev` branch.

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

<aside class="callout">

Once the Lens Resource is applied and all configurations are correctly set up, the semantic model will be deployed. Upon deployment, a Lens Service is created in the backend, which may take some time to initialize.

To verify whether the Lens Service is running, execute the following command. The Service name follows the pattern: <strong><code>&lt;lens-name&gt;-api</code></strong>


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

