# Connecting to AWS Redshift Depot

## Step 1: Create the Depot

If the Depot is not active, create one using the provided template.

```yaml
name: ${{redshift-depot-name}}
version: v2alpha
type: depot
tags:
  - ${{redshift}}
layer: user
description: ${{Redshift Sample data}}
depot:
  type: REDSHIFT
  redshift:
    host: ${{hostname}}
    subprotocol: ${{subprotocol}}
    port: ${{5439}}
    database: ${{sample-database}}
    bucket: ${{tmdc-dataos}}
    relativePath: ${{development/redshift/data_02/}}
  external: ${{true}}
  secrets:
    - name: ${{redshift-instance-secret-name}}-r
      allkeys: true

    - name: ${{redshift-instance-secret-name}}-rw
      allkeys: true
```

## Step 2: Prepare the Lens model folder

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
  "onelakehouse"."retail".customer;
```
### **Define the table in the model**

Create a `tables` folder to store logical table definitions, with each table defined in a separate YAML file outlining its dimensions, measures, and segments. For example, to define a table for `sales `data:

```yaml
table:
  - name: customers
    sql: {{ load_sql('customers') }}
    description: Table containing information about sales transactions.
```

### **Add dimensions and measures**

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

### **Add segments to filter**

Segments are filters that allow for the application of specific conditions to refine the data analysis. By defining segments, you can focus on particular subsets of data, ensuring that only the relevant records are included in your analysis. For example, to filter for records where the state is either Illinois or Ohio, you can define a segment as follows:

```yaml
segments:
  - name: state_filter
    sql: "{TABLE}.state IN ('Illinois', 'Ohio')"
```

To know more about segments click [here](https://dataos.info/resources/lens/segments/).

### **Create the views**

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

### **Create user groups**

This YAML manifest file is used to manage access levels for the semantic model. It defines user groups that organize users based on their access privileges. In this file, you can create multiple groups and assign different users to each group, allowing you to control access to the model.By default, there is a 'default' user group in the YAML file that includes all users.

```yaml
user_groups:
  - name: default
    description: this is default user group
    includes: "*"
```

To know more about the User groups click [here](https://dataos.info/resources/lens/user_groups_and_data_policies/)


## Step 3: Deployment manifest file

Once the Lens with semantic model is prepared, create a `lens_deployment.yml` file parallel to the model folder to configure the deployment using the YAML template below.

```yaml
version: v1alpha
name: "redshiftlens"
layer: user
type: lens
tags:
  - lens
description: redshiftlens deployment on lens2
lens:
  compute: runnable-default
  secrets:
    - name: bitbucket-cred
      allKeys: true
  source:
    type: depot # source type is depot here
    name: redshiftdepot # name of the redshift depot
  repo:
    url: https://bitbucket.org/tmdc/sample
    lensBaseDir: sample/lens/source/depot/redshift/model 
    # secretId: lens2_bitbucket_r
    syncFlags:
      - --ref=lens
```

Each section of the YAML template defines key aspects of the Lens deployment. Below is a detailed explanation of its components:

* **Defining the Source:**

      * **`type`:**  The `type` attribute in the `source` section must be explicitly set to `depot`.

      * **`name`:** The `name` attribute in the `source` section should specify the name of the AWS Redshift Depot created.

* **Setting Up Compute and Secrets:**

      * Define the compute settings, such as which engine (e.g., `runnable-default`) will process the data.

      * Include any necessary secrets (e.g., credentials for Bitbucket or AWS) for secure access to data and repositories.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/awsredshift/model`.

      * **`secretId`:**  The `secretId` attribute is used to access private repositories (e.g., Bitbucket, GitHub). It specifies the secret needed to authenticate and access the repository securely.

      * **`syncFlags`**:  Specifies additional flags to control repository synchronization. Example: `--ref=dev` specifies that the Lens model resides in the `dev` branch.

* **Configure API, Worker, and Metric Settings (Optional):** Set up replicas, logging levels, and resource allocations for APIs, workers, routers, and other components.

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



<!-- 
## Check query statistics for AWSRedshift


> Note: Ensure the user has AWS console access before proceeding.
> 

### **1. Log in to AWS Console and access Redshift**

  a. Login to the AWS Console.<br>
  b. Search for 'Redshift' in the AWS Console search bar.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled1.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

### **2. Select Redshift Cluster**

  a. Click on 'Amazon Redshift' from the search results.You will be directed to the Redshift dashboard.<br>
  b. Select the appropriate region and choose the desired cluster name from the list.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled2.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

### **3. Access Query Monitoring**

  a. Select the cluster you want to monitor.<br>
  b. Navigate to the 'Query monitoring' tab to view query statistics.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled3.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

### **4. View running and completed queries**

  a. In the 'Query monitoring' tab, you will see a list of running  and completed queries.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled4.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

### **5. Monitor specific query**

  a. Click on the query you want to monitor.
  b. View the query statistics, as shown in the example below.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled5.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled6.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div> -->
