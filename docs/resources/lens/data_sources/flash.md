# Flash

[Flash](/resources/stacks/flash/) is designed to optimize query performance by leveraging in-memory execution. When used with DataOS Lakehouse and Iceberg-format depots, it enables efficient handling of large-scale queries by reducing latency and optimizing resource usage. The following explains how to configure Lens using Flash.


### **Prerequisites**

To create a Lens using Flash ensure following:

- **Persistence Volume attached with Flash Service:** Ensure Flash service is running and has a Persistent Volume attached. A Persistent Volume allows Flash to spill data to disk, enhancing performance by preventing memory constraints from impacting query execution.
Ensure to replace the placeholders and modify the configurations as needed wherever required.

## Create Persistent Volume manifest file

Copy the template below and replace <name> with your desired resource name and <size> with the appropriate volume size (e.g., `100Gi`, `20Gi`, etc.), according to your available storage capacity. Make sure the configuration is aligned with both your storage and performance requirements. For the accessMode, you can choose ReadWriteOnce (RWO) for exclusive read-write access by a single node, or ReadOnlyMany (ROX) if the volume needs to be mounted as read-only by multiple nodes.

```yaml
name: <name>  # Name of the volume
version: v1beta  # Manifest version of the Resource
type: volume  # Type of Resource
tags:  # Tags for categorizing the Resource
  - volume
description: Common attributes applicable to all DataOS Resources
layer: user
volume:
  size: <size>  # Example: 100Gi, 50Mi, 10Ti, 500Mi, 20Gi
  accessMode: <accessMode>  # Example: ReadWriteOnce, ReadOnlyMany
  type: temp
```

<aside class="callout">
💡The persistent volume size should be at least 2.5 times the total dataset size, rounded to the nearest multiple of 10.

To check the dataset size, use the following query:

```sql
SELECT sum(total_size) FROM "<catalog>"."<schema>"."<table>$partitions";
```
The resultant size will be in the bytes.
</aside>

## Apply the Volume manifest file

Apply the persistent volume manifest file, using the following command in terminal:

```shell
dataos-ctl resource apply -f <file path of persistent volume>
```
This will deploy the Persistent Volume Resource, making it available for use by Flash Service.


## Create Service manifest file

Ensure that the name of the Persistent Volume you created is referenced correctly in the name attribute of the persistentVolume section. The name used here should match exactly with the name you assigned to the Persistent Volume during its creation.

```yaml
name: flash-service-training
version: v1
type: service
tags:
  - service
description: flash service
workspace: curriculum
service:
  servicePort: 5433
  replicas: 1
  logLevel: info

  compute: runnable-default

  resources:
    requests:
      cpu: 1000m
      memory: 1024Mi
# replace the name of the persistence volume from the pv created
  persistentVolume:
    name: <persistent_volume_name>
    directory: p_volume

  stack: flash+python:2.0

  stackSpec:
# dataset section
    datasets:
      - address: dataos://lakehouse:sales_analysis/channel  #view
        name: f_customer
      - address: dataos://lakehouse:sales_analysis/transactions
        name: f_transactions
      - address: dataos://lakehouse:sales_analysis/products
        name: f_products
      - address: dataos://lakehouse:sales_analysis/customer
        name: f_channel
# init section 
    init:
      - create table if not exists channel as (select * from f_channel)  #table
      - create table if not exists transactions as (select * from f_transactions)
      - create table if not exists products as (select * from f_products)
      - create table if not exists table customer as (select * from f_customer)
```

### How does this process work?

The flow of Flash operates as follows:

**Data loading:** The `datasets` attribute specifies the Depot `address` of the source data to be loaded into Flash. A dataset `name` is also provided, which Flash uses to generate a view of the source data.

**View creation:** Flash creates a view based on the assigned name, allowing for interaction with the source data without directly querying it.

**Table creation:** Specific columns from the generated view can be selected to define tables for further operations using `init` attribute. The `if not exists` clause ensures that the tables are created only if they don't already exist. If they are already present, the process skips creation.

**Usage in semantic model(SQL):** The tables created through the `init` attribute are used in SQL queries within Lens semantic model.

For example, in the manifest referenced, the `channel` table is first loaded from the source, and a view named `f_channel` is created. A table called `channel` is then defined on `channel` view. This table is then referenced in SQL models within Lens.

## Apply the Flash manifest file

To apply the Flash Service configuration, use the following command:

```bash
dataos-ctl resource apply -f <file path of flash service>
```

## Create an Instance-secrets manifest file

<aside class="callout">
Before pushing the model to a code repository (e.g., Bitbucket or GitHub), create an Instance-secret to store the repository credentials.
</aside>


```yaml
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

## Apply the Instance-secret manifest file

To apply the Instance-secret configuration, use the following command:

```bash
dataos-ctl resource apply -f <file path of the instance-secret>
```

<aside class="callout">
Push the semantic model folder into the code repository.
</aside>

## Prepare the semantic model folder

In the Model folder, the semantic model will be defined, encompassing SQL mappings, logical tables, logical views, and user groups. Each subfolder contains specific files related to the Lens model. Download the Lens template to quickly get started.

[lens template](/resources/lens/lens_model_folder_setup/lens-project-template.zip)

### **Load data from the data source**

In the `sqls` folder, create `.sql` files for each logical table, where each file is responsible for loading or selecting the relevant data from the source. Ensure that only the necessary columns are extracted, and the SQL dialect is specific to the data source. For Flash, the table name given in the  `init` will be the source table name.

For example, a simple data load might look as follows:

```sql
SELECT
  *
FROM
  channel; --flash source table name
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
  customer;  -- flash source table name
```
### **Define the table in the Model**

Create a `tables` folder to store logical table definitions, with each table defined in a separate YAML file outlining its dimensions, measures, and segments. For example, to define a table for `channel `data:

```yaml
tables:
  - name: channel  
    sql: {{ load_sql('channel') }}
    description: Table containing information about channel records.
```

#### **Add dimensions and measures**

After defining the base table, add the necessary dimensions and measures. For example, to create a table for `channel` data with measures and dimensions, the YAML definition could look as follows:

```yaml
tables:
  - name: channel
    sql: {{ load_sql('channel') }}  #sql table name
    description: Table containing information about channel records.

    
    dimensions:       
      - name: store_id
        type: string
        description: Unique identifier for each store.
        sql: store_id
        primary_key : true
        public : true         
      
      - name: store_name
        type: string
        description: The name of the store.
        sql: store_name
```

#### **Add segments to filter**

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
    
### **Create user groups**

The `user_groups.yml` manifest file is used to manage access levels for the semantic model. It defines user groups that organize users based on their access privileges. In this file, you can create multiple groups and assign different users to each group, allowing you to control access to the model.By default, the 'default' user group in the manifest file includes all users.

```yaml
user_groups:
  - name: default
    description: this is a default user group
    includes: "*"
```

You can create multiple user groups in `user_groups.yml` . To know more about the User groups click [here](https://dataos.info/resources/lens/user_groups_and_data_policies/).


## Create Lens manifest file

### **1. Define Flash as the data source**

Configure the Flash service as the data source in the Lens deployment manifest file.

**`Source`**

- **`type`** The source section specifies that Flash is used as the data source (`type: flash`). This indicates that data for the semantic model will be loaded from the Flash service.

- **`name`**: The Flash service is identified by the `name` attribute, here it is flash-service-lens. This name should match the deployed Flash service used for data ingestion. Below is an example configuration.

```bash
source:
  type: flash  # Specifies the data source type as Flash
  name: flash-training  # Name of the Flash service
```

### **2. Add environment variables**

To enable Lens to interact with the Flash service, specify the following environment variables in the Worker, API, and Router sections of the Lens deployment manifest.

**`envs`**

The following environment variables are defined under multiple components, including api, worker, router.

- **`LENS2_SOURCE_WORKSPACE_NAME`**  It refers to the workspace where the Flash service is deployed. 

- **`LENS2_SOURCE_FLASH_PORT`** The port number `5433` is specified for the Flash service. This port is used by Lens to establish communication with the Flash service. It ensures that all components—API, worker, router — can access the Flash service consistently.

```bash
envs:
  LENS2_SOURCE_WORKSPACE_NAME: public
  LENS2_SOURCE_FLASH_PORT: 5433
```
Following is the Lens manifest file:

```yaml title="lens_deployment.yml" hl_lines="13-15 25-26"
version: v1alpha
name: "lens-flash-training"
layer: user
type: lens
tags:
  - lens
description: A sample lens that contains three entities, a view and a few measures for users to test
lens:
  compute: runnable-default
  secrets: # Referred Instance-secret configuration (**mandatory for private code repository, not required for public repository)
    - name: githubr # Referred Instance Secret name (mandatory)
      allKeys: true # All keys within the secret are required or not (optional)
  source:
    type: flash # minerva, themis and depot
    name: flash-service-training # flash service name
  repo:
    url: https://github.com/tmdc/sample    # repo address
    lensBaseDir: sample/source/flash/model     # location where lens models are kept in the repo
    syncFlags:
      - --ref=main
```

## Apply Lens manifest file

Apply the Lens manifest file by using the following command in terminal:

```bash
dataos-ctl resource apply -f <lens-file-path>
```