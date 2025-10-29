# Creating a semantic model on Databricks source

!!! warning "Databricks source known limitations"

    All core features of Lens are supported except SQL API, which means:

    - Users cannot query semantic models via SQL API.

    - BI tools relying on psql-based connections cannot access semantic models.

    - BI Sync is not supported.

    - **Databricks Depot:** Databricks Depots can only be used as a source for Lens, not for other Stacks or Resources.

    - **Metadata Scanning:** Metadata scanning for Databricks tables is not yet supported.

## Prerequisites

Before setting up the connection, ensure all necessary prerequisites are in place:

- Databricks workspace and active SQL Warehouse, required to connect and run queries.

- **Personal Access Token (PAT):** Used as credentials and securely stored in an Instance Secret.

- **Instance Secret:** Secures the source credentials (and repository credentials if the repo is private).

- **JDBC connection details:**Iincludes the `host`, `port`, `httpPath`, and `database` parameters from Databricks SQL Warehouse connection URL.

- **Depot:** references both the Instance Secret and the JDBC parameters to establish a secure connection between Lens and Databricks.

- **Repository for version control:** The semantic model should be version-controlled within a dedicated Lens repository and `model/` folder before deployment.

## Step 1: Set up a connection with source

To ensure a smooth setup, complete the following prerequisites:

1. **Secure repository credentials by creating Instance Secret:**

Create Instance Secret for your preferred hosted repository (Bitbucket, AWS Code Commit, Github) if repository is public you can skip this step. Lens service requires the Personal Access Token (PAT) to access private Github repositories. After creating PAT, the user must store it in DataOS as a secret so the Lens service can authenticate the token during repository synchronization and read the model file from the repository. 

```yaml title="bitbucket-r.yaml"
name: bitbucket-r
version: v1
type: instance-secret
description: bitbucket credentials
layer: user
instance-secret:
  type: key-value
  acl: r                                # read level access
  data:
    GITSYNC_USERNAME: ${{"iamgroot"}}   # replace the placeholder with the bitbucket (or preferred code repository) username
    GITSYNC_PASSWORD: ${{"0123Abcedefghij="}}   #replace the placeholder with the personal access token
```

2. **Secure source credentials by creating Instance Secret**

Before establishing a connection to the Databricks, an Instance Secret must be created. This secret securely stores the credentials(here, the Databricks Personal Access Token). Follow the official Databricks guide to generate a [Personal Access Token](https://docs.databricks.com/aws/en/dev-tools/auth/pat#create-personal-access-tokens-for-workspace-users).


```yaml title="databricks-r.yml"
name: databricks-r
version: v1
type: instance-secret
layer: user
instance-secret:
  type: key-value-properties
  acl: r
  data:
    token: "dapi0123"  # databricks's personal access token here
```
3. **Connect to source by creating a Depot**

To connect to Databricks through a Depot, you’ll need its JDBC connection details. Follow these steps to retrieve them:

  1. Go to Databricks workspace.

  2. Navigate to: SQL → SQL Warehouses → select warehouse  → Connection Details.

  3. Copy the JDBC URL, it will look like this:

  ```
  jdbc:spark://<databricks-host>:443/default;transportMode=http;ssl=1;AuthMech=3;httpPath=sql/protocolv1/o/<org-id>/<warehouse-id>
  ```

Extract the following values from the URL to fill in Depot YAML:

| **Field**       | **Description**                                                       | **Example Value**                        |
| --------------- | --------------------------------------------------------------------- | ---------------------------------------- |
| `subprotocol`   | Identifies the JDBC driver type used to connect to Databricks.        | `databricks-jdbc`                        |
| `database`      | Specifies the default database or schema to connect to. (optional)    | `main`                                   |
| `host`          | The Databricks workspace host (server hostname).                      | `dbc-123abc23-d0aa.cloud.databricks.com` |
| `port`          | The port used for the JDBC connection.                                | `443`                                    |
| `transportMode` | Specifies the transport protocol used for communication.              | `http`                                   |
| `ssl`           | Enables SSL encryption for the connection.                            | `1`                                      |
| `AuthMech`      | Defines the authentication mechanism used.                            | `3`                                      |
| `httpPath`      | The HTTP path to the Databricks SQL Warehouse.                        | `/sql/1.0/warehouses/99123`              |
| `accept_policy` | Confirms acceptance of Databricks JDBC driver usage terms (required). | `true`                                   |

Use the extracted values to populate the following Depot manifest file:

```yaml title="databricks-depot.yml"
name: databricks-a   #depot name
version: v2alpha
type: depot
description: databricks jdbc depot
owner: iamgroot
layer: user
depot:
  type: JDBC
  external: true
  secrets:
    - name: databricks-r  #instance-secret created
      allkeys: true
  jdbc:
    subprotocol: databricks-jdbc
    database: main                               #optional
    host: dbc-123abc23-d0aa.cloud.databricks.com
    port: 443
    params:
      transportMode: http
      ssl: 1
      AuthMech: 3
      httpPath: /sql/1.0/warehouses/99123
      accept_policy: true # This accepts the Databricks usage policy and must be set to `true` to use the Databricks JDBC driver
```


## Step 2: Prepare the Lens model folder

In the `model` folder, the semantic model will be defined, encompassing SQL mappings, logical tables, logical views, and user groups. Each subfolder contains specific files related to the Lens model. 

```
model/
├── sqls/                        # Contains SQL files that load or transform data from Databricks
│   └── customer.sql             # SQL query for extracting and preparing customer data
│
├── tables/                      # YAML definitions describing logical tables, dimensions, measures, and joins
│   └── customer.yaml            # Defines the customer table schema, joins, dimensions, and measures
│
├── views/                       # YAML views combining data from multiple tables
│   └── customer_churn.yaml      # Logical view combining customer and campaign data for churn insights
│
└── user_groups.yaml             # Defines access control and user groups for the Lens model
```

### **Step 2.1: Load data from the data source**

In the `sqls` folder, create `.sql` files for each logical table, where each file is responsible for loading or selecting the relevant data from the source. Ensure that only the necessary columns are extracted and the SQL dialect is specific to the databricks. For instance,

* Format table names as: `database.table`.

* Use `STRING` for text data types instead of `VARCHAR`.

For instance, a simple data load might look as follows:

```sql
SELECT
  *
FROM
  main.account;  --database_name.table_name
```

Alternatively, you can write more advanced queries that include transformations, such as:

```sql title="customer.yaml"
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
  main.customer;
```
  
### **Step 2.2: Define the table in the model**

Create a `tables` folder to store logical table definitions, with each table defined in a separate YAML file outlining its dimensions, measures, and segments. For instance, to define a table for `customer `data:

```yaml title="customer.yaml"
table:
  - name: customers
    sql: {{ load_sql('customer') }}
    description: Table containing information about sales transactions.
```

### **Step 2.3: Add dimensions and measures**

After defining the base table, add the necessary dimensions and measures. For instance, to create a table for sales data with measures and dimensions, the YAML definition could look as follows:

```yaml title
tables:
  - name: customer
    sql: {{ load_sql('customer') }}
    description: Table containing customer records with order details.

    dimensions:
      - name: customer_id
        type: number
        description: Unique identifier for each order.
        sql: order_id
        primary_key: true
        public: true

    measures:
      - name: total_customer_count
        type: count
        sql: id
        description: Total number of orders.
```

### **Step 2.4: Add segments to filter**

Segments are filters that allow for the application of specific conditions to refine the data analysis. By defining segments, you can focus on particular subsets of data, ensuring that only the relevant records are included in analysis. For example, to filter for records where the state is either Illinois or Ohio, you can define a segment as follows:

```yaml
segments:
  - name: state_filter
    sql: "{TABLE.state} IN ('Illinois', 'Ohio')"
```

To know more about segments click [here](/resources/lens/segments/).


### **Step 2.5: Create views**

Create a views folder to store all logical views, with each view defined in a separate YAML file (e.g., `sample_view.yml`). Each view references dimensions, measures, and segments from multiple logical tables. For instance, the following customer_churn view is created:


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
    description: default user group for all users.
    includes: "*"
```

To know more about the User groups click [here](/resources/lens/user_groups_and_data_policies/).

!!! info

    Once you have completely created model, push the model files to a version control repository before proceeding with deployment.


## Step 3: Deployment manifest file

After setting up the Lens model folder, the next step is to configure the deployment manifest. Below is the YAML template for configuring a Lens deployment.

```yaml
# RESOURCE META SECTION
version: v1alpha # Lens manifest version (mandatory)
name: "databricks-lens" # Lens Resource name (mandatory)
layer: user # DataOS Layer (optional)
type: lens # Type of Resource (mandatory)
tags: # Tags (optional)
  - lens
description: databricks depot lens deployment on lens2 # Lens Resource description (optional)

# LENS-SPECIFIC SECTION
lens:
  compute: runnable-default # Compute Resource that Lens should utilize (mandatory)
  secrets: # Referred Instance-secret configuration (**mandatory for private code repository, not required for public repository)
    - name: bitbucket-cred # Referred Instance Secret name (mandatory)
      allKeys: true # All keys within the secret are required or not (optional)

  source: # Data Source configuration
    type: depot # Source type is depot here
    name: databricks # Name of the databricks depot 

    #The name under source: should match the actual depot name (databricks-a here)

  repo: # Lens model code repository configuration (mandatory)
    url: https://bitbucket.org/tmdc/sample # URL of repository containing the Lens model (mandatory)
    lensBaseDir: sample/lens/source/depot/databricks/model # Relative path of the Lens 'model' directory in the repository (mandatory)
    syncFlags: # Additional flags used during synchronization, such as specific branch.
      - --ref=main # Repository Branch
```

Each section of the YAML template defines key aspects of the Lens deployment. Below is a detailed explanation of its components:

* **Defining the Source:**

      * **Source type:**  The `type` attribute in the `source` section must be explicitly set to `depot`.

      * **Source name:** The `name` attribute in the `source` section should specify the name of the Databricks Depot created.

* **Setting Up Compute and Secrets:**

      * Define the compute settings, such as which engine (e.g., `runnable-default`) will process the data.

      * Include any necessary secrets (e.g., credentials for Bitbucket or AWS CodeCommit) for secure access to data and repositories.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/databricks/model`.

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


<aside class="callout">

Once the Lens Resource is applied and all configurations are correctly set up, the Lens model will be deployed. Upon deployment, a Lens Service is created in the backend, which may take some time to initialize.

To verify whether the Lens Service is running, execute the following command. The Service name follows the pattern: `<lens-name>-api`

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

