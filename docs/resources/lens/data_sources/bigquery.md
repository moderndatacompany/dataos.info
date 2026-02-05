# Creating a semantic model on BigQuery source

<aside class="callout">

When setting up a semantic model, it is crucial to understand that the semantic model is part of the Data Product. Therefore, you do not need to create a separate Git repository. Instead, semantic model will be in the <code>/build</code> folder of the the Data Product's existing repository. 
</aside>


## Prerequisites

Before proceeding, ensure a secure connection to the source is established and metadata is extracted using the required resources:

- [Instance Secret](/resources/lens/data_sources/bigquery/#instance-secret): To secure source connection credentials.
- [Depot](/resources/lens/data_sources/bigquery/#depot): To set up a connection with the source.
- [Scanner](/resources/lens/data_sources/bigquery/#scanner): To extract the metadata and view on Metis application.

## Step 1: Set up a secure connection with source using Instance secret

To set up a connection with the source, create Depot if the Depot has already been created and activated during the Design phase of the Data Product, skip this step. The Lens model will utilize the existing Depot and the associated Instance Secrets set up. Ensure that the Depot is properly connected to the correct data source and that you have the necessary access credentials (Instance Secrets) available for the Lens deployment.

Before establishing a connection to the data source, an [Instance Secret](/resources/instance_secret/) must be created. This secret securely stores the credentials required for `read` (`r`) and `read write` (`rw`) access to the data source.

### Instance secret

Secure source connection credentials.

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
    username: 
    password: 
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
    username: 
    password: 
```

### Depot

Connect with the source referring recently created Instance-secret.

```yaml title="bigquery-depot.yml"
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
      allKeys: true
    - name: ${{bq-instance-secret-name}}-rw
      allKeys: true
  bigquery:  # optional
    project: ${{project-name}} # optional
    params: # optional
      ${{"key1": "value1"}}
      ${{"key2": "value2"}}
```

### Scanner

To extract the metadata and view on Metis application.

```yaml
version: v1
name: bigquery-scanner
type: workflow
tags:
  - bigquery-depot-scan
description: The job scans schema tables and register data to metis
workflow:
  dag:
    - name: bigquery-depot
      description: The job scans schema from bigquery depot tables and register data to metis
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        compute: runnable-default
        stackSpec:
          depot: dataos://bigquery
```


## Step 2: Prepare the Lens model folder

In the `model` folder, the semantic model will be defined, encompassing SQL mappings, logical tables, logical views, and user groups. Each subfolder contains specific files related to the Lens model. You can download the Lens template to quickly get started.

[Lens template](/resources/lens/lens_model_folder_setup/lens-project-template.zip)


### **Step 2.1: Load data from the data source**

In the `sqls` folder, create `.sql` files for each logical table, where each file is responsible for loading or selecting the relevant data from the source. Ensure, only the necessary columns are extracted, and the SQL dialect is specific to the bigquery. For instance,

* Format table names as: `project_id.dataset.table`.

* Use `STRING` for text data types instead of `VARCHAR`.

* Replace generic functions with BigQuery’s `EXTRACT` function.

For instance, a simple data load might look as follows:

```sql
SELECT
  *
FROM
  "bigquery"."retail"."channel";
```

Alternatively, you can write more advanced queries that include transformations, such as:

```sql
SELECT
  CAST(customer_id AS VARCHAR) AS customer_id,
  first_name,
  CAST(PARSE_DATE('%d-%m-%Y', birth_date) AS TIMESTAMP) AS birth_date,
  age,
  CAST(register_date AS TIMESTAMP) AS register_date,
  occupation,
  annual_income,
  city,
  state,
  country,
  zip_code
FROM
  "bigquery"."retail"."customer";
```
  
### **Step 2.2: Define the table in the model**

Create a `tables` folder to store logical table definitions, with each table defined in a separate YAML file outlining its dimensions, measures, and segments. For instance, to define a table for `sales `data:

```yaml
tables:
  - name: customers
    sql: {{ load_sql('customers') }}
    description: Table containing information about sales transactions.
```

### **Step 2.3: Add dimensions and measures**

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

### **Step 2.4: Add segments to filter**

Segments are filters that allow for the application of specific conditions to refine the data analysis. By defining segments, you can focus on particular subsets of data, ensuring that only the relevant records are included in your analysis. For example, to filter for records where the state is either Illinois or Ohio, you can define a segment as follows:

```yaml
segments:
  - name: state_filter
    sql: "{TABLE.state} IN ('Illinois', 'Ohio')"
```

To know more about segments click [here](/resources/lens/segments/).


### **Step 2.5: Create views**

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

To know more about the views click [here](/resources/lens/views/).


### **Step 2.6: Create User groups**

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

      * **Source type:** The `type` attribute in the `source` section must be explicitly set to `depot`.

      * **Source name:** The `name` attribute in the `source` section should specify the name of the BigQuery Depot created.

* **Setting Up Compute and Secrets:**

      * Define the compute settings, such as which engine (e.g., `runnable-default`) will process the data.

      * Include any necessary secrets (e.g., credentials for Bitbucket or AWS CodeCommit) for secure access to data and repositories.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:** The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/bigquery/model`.

      * **`secretId`:** The `secretId` attribute is used to access private repositories (e.g., Bitbucket, GitHub). It specifies the secret needed to securely authenticate and access the repository.

      * **`syncFlags`**: Specifies additional flags to control repository synchronization. Example: `--ref=dev` specifies that the Lens model resides in the `dev` branch.

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
    INFO[0000] 🔧 applying(curriculum) bigquery-lens:v1alpha:lens... 
    INFO[0001] 🔧 applying(curriculum) bigquery-lens:v1alpha:lens...created 
    INFO[0001] 🛠 apply...complete
    ```


<aside class="callout">

Once the Lens Resource is applied and all configurations are correctly set up, the Lens model will be deployed. Upon deployment, a Lens Service is created in the backend, which may take some time to initialize.

To verify whether the Lens Service is running, execute the following command. The Service name follows the pattern: `<lens-name>-api`**

Ensure Service is active and running before proceeding to the next steps.

```bash
dataos-ctl get -t service -n bigquery-lens-api -w public
# Expected output:
INFO[0000] 🔍 get...                                     
INFO[0002] 🔍 get...complete                             

           NAME           | VERSION |  TYPE   | WORKSPACE | STATUS |  RUNTIME  |    OWNER     
--------------------------|---------|---------|-----------|--------|-----------|--------------
  bigquery-lens-api | v1      | service | public    | active | running:1 | iamgroot
```

</aside>


