# Creating a semantic model on Snowflake Depot

<aside class="callout">

When setting up a semantic model, it is crucial to understand that the semantic model is part of the Data Product. Therefore, no need to create a separate Git repository. Instead, semantic model will be in the <code>/build</code> folder of the the Data Product's existing repository. 
</aside>

## Prerequisite

CLI Version should be `dataos-cli 2.26.39-dev` or greater.

## Step 1: Set up a connection with source

To set up a connection with the source, create Depot if the Depot has already been created and activated during the Design phase of the Data Product, skip this step. The Lens model will utilize the existing Depot and the associated Instance Secrets set up. Ensure that the Depot is properly connected to the correct data source and that you have the necessary access credentials (Instance Secrets) available for the Lens deployment.

Before establishing a connection to the data source, an [Instance Secret](/resources/instance_secret/) must be created. This secret securely stores the credentials required for `read` (`r`) and `read write` (`rw`) access to the data source.

```yaml title="instance-secret-r.yml"
# RESOURCE META SECTION
name: <secret-name> # Secret Resource name (mandatory)
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

```yaml title="instance-secret-rw.yml"
# RESOURCE META SECTION
name: <secret-name> # Secret Resource name (mandatory)
version: v1 # Secret manifest version (mandatory)
type: instance-secret # Type of Resource (mandatory)
description: demo-secret read secrets for code repository # Secret Resource description (optional)
layer: user # DataOS Layer (optional)

# INSTANCE SECRET-SPECIFIC SECTION
instance-secret:
  type: key-value # Type of Instance-secret (mandatory)
  acl: rw # Access control list (mandatory)
  data: # Data (mandatory)
    GITSYNC_USERNAME: <code_repository_username>
    GITSYNC_PASSWORD: <code_repository_password>
```


```yaml title="snowflake-depot.yml"
name: snowflake-depot
version: v2alpha
type: depot
tags:
  - Snowflake depot
  - user data
layer: user
depot:
  name: sftest
  type: snowflake
  description: Depot to fetch data from Snowflake datasource
  secrets:
    - name: sftest-r
      keys:
        - sftest-r
      allKeys: true
    - name: sftest-rw
      keys:
        - sftest-rw
      allKeys: true
  external: true
  snowflake:
    database: TMDC_V1
    url: ABCD23-XYZ8932.snowflakecomputing.com
    warehouse: COMPUTE_WH
    account: ABCD23-XYZ8932
  source: sftest
```

## Step 2: Prepare the Lens model folder

After successfully setting up the connection with source, organize the semantic model folder with the following structure to define tables, views, and governance policies:

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

In the `sqls` folder, create `.sql` files for each logical table, where each file is responsible for loading or selecting the relevant data from the source. Ensure the SQL dialect matches snowflake syntax. Format table names as `schema.table`.

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
Know more about [dimensions](/resources/lens/concepts/#dimensions) and [measures](/resources/lens/concepts/#measures).

#### **Add segments to filter**

Segments are filters that allow for the application of specific conditions to refine the data analysis. By defining segments, you can focus on particular subsets of data, ensuring that only the relevant records are included in your analysis. For example, to filter for records where the state is either Illinois or Ohio, you can define a segment as follows:

```yaml
segments:
  - name: state_filter
    sql: "{TABLE}.state IN ('Illinois', 'Ohio')"
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

This YAML manifest file is used to manage access levels for the semantic model. It defines user groups that organize users based on their access privileges. In this file, you can create multiple groups and assign different users to each group, allowing you to control access to the model.By default, there is a 'default' user group in the YAML file that includes all users.

```yaml
user_groups:
  - name: default
    description: this is default user group
    includes: "*"
```

To know more about the User groups click [here](/resources/lens/user_groups_and_data_policies/)

## Step 3: Deployment manifest file

After setting up the Lens model folder, the next step is to configure the deployment manifest. Below is the YAML template for configuring a Lens deployment.

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

      * **Source name:** The `name` attribute in the `source` section should specify the name of the snowflake Depot created.

* **Setting Up Compute and Secrets:**

      * Define the compute settings, such as which engine (e.g., `runnable-default`) will process the data.

      * Include any necessary secrets (e.g., credentials for Bitbucket or AWS) for secure access to data and repositories.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/snowflake/model`.

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