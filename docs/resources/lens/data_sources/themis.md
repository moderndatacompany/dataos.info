# Creating semantic model on Themis cluster as source

## Prerequisite

Ensure you have an active and running Themis Cluster.

## Prepare the Lens model folder

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

Create a `tables` folder to store logical table definitions, with each table defined in a separate YAML file outlining its dimensions, measures, and segments. For example, to define a table for `customer `data:

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
    name: lenstestingthemis #name of the themis cluster
    catalog: lakehouse                 # optional: you can provide any of the sources used and it will take care of others by default 
  repo:
    url: https://bitbucket.org/tmdc/sample
    lensBaseDir: sample/lens/source/themis/model 
    # secretId: lens2_bitbucket_r
    syncFlags:
      - --ref=main #repo-name
```

The YAML manifest provided is designed for a cluster named `themiscluster`, created on the `Themis` source, with a data catalog named `lakehouse`. To utilize this manifest, duplicate the file and update the source details as needed.

Each section of the YAML template outlines essential elements of the Lens deployment. Below is a detailed breakdown of its components:

* **Defining the Source:**

      * **`type`:**  The `type` attribute in the `source` section must be explicitly set to `themis`.

      * **`name`:** The `name` attribute in the `source` section should specify the name of the Themis Cluster. For example, if the name of your Themis Cluster is `clthemis` the Source name would be `clthemis`.

      * **`catalog`:** The `catalog` attribute define the specific catalog name within the Themis Cluster that you intend to use. For instance, if the catalog is named `lakehouse_retail`, ensure this is accurately reflected in the catalog field. However, You don’t need to provide all catalogs from different sources used in the semantic model — specifying any one is sufficient, as the rest will be auto-detected. For instance, if your semantic model includes both `Lakehouse` and `Postgres` sources, you only need to provide any one catalog name.
* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/awsredshift/model`.

      * **`secretId`:**  The `secretId` attribute is used to access private repositories (e.g., Bitbucket, GitHub). It specifies the secret needed to authenticate and access the repository securely.

      * **`syncFlags`**:  Specifies additional flags to control repository synchronization. Example: `--ref=dev` specifies that the Lens model resides in the `dev` branch.

* **Configure API, Worker, and Metric Settings (Optional):** Set up replicas, logging levels, and resource allocations for APIs, workers, routers, and other components.


The above manifest is intended for a cluster named `lenstestingthemis`, created on the themis source, with the Depot or data catalog named `lakehouse`. To use this manifest, copy the file and update the source details accordingly.

<aside class="callout">
🗣️ Within the Themis and Minerva cluster, all depots (such as lakehouse, Redshift, Snowflake, etc.) are integrated. When configuring Lens, you only need to specify one Depot in the `catalog` field, as Lens can connect to and utilize depots from all sources available in the Themis cluster.
</aside>


## Apply the Lens manifest file

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
    INFO[0000] 🔧 applying(curriculum) themis-lens:v1alpha:lens... 
    INFO[0001] 🔧 applying(curriculum) themis-lens:v1alpha:lens...created 
    INFO[0001] 🛠 apply...complete
    ```


!!! info "Note"

    Once the Lens Resource is applied and all configurations are correctly set up, the Lens model will be deployed. Upon deployment, a Lens Service is created in the backend, which may take some time to initialize.

    To verify whether the Lens Service is running, execute the following command. The Service name follows the pattern: **`${{lens-name}}-api`**

    Ensure Service is active and running before proceeding to the next steps.

    ```bash
    dataos-ctl get -t service -n themis-lens-lens-api -w public
    # Expected output:
    INFO[0000] 🔍 get...                                     
    INFO[0002] 🔍 get...complete                             

              NAME           | VERSION |  TYPE   | WORKSPACE | STATUS |  RUNTIME  |    OWNER     
    --------------------------|---------|---------|-----------|--------|-----------|--------------
      themis-lens-lens-api | v1      | service | public    | active | running:1 | iamgroot
    ```



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
