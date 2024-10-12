---
title: dbt Stack
search:
  boost: 2
---

# DBT Stack

dbt (data build tool) is a declarative [Stack](/resources/stacks/) within DataOS, acting as the transformative force in ELT (Extract, Load, Transform), dbt focuses on optimizing and refining data already loaded into the database. It facilitates the centralization and modularization of analytics code, adopting a structured approach akin to software engineering practices. It enables collaborative work on data models, and versioning, before their deployment to production.  It establishes a connection with the data platform and executes SQL code within the warehouse to perform data transformations, fostering collaboration among you and your team by establishing a single source of truth for metrics, insights, and business terminology.

<aside class="callout">
🗣️ It's crucial to understand that although dbt is highly proficient in transformation tasks, it does not manage the Extract and Load processes.
</aside>

**Prerequisites**

   -  **Basic to intermediate SQL:** proficiency in utilizing the WHERE and GROUP BY clauses is essential.

   -  **Basics of data warehouses:** a foundational understanding of data engineering is highly beneficial. It doesn't need to be extensive, but grasping key concepts is important.

# How to create and use dbt workflow?

### **Create a Workflow manifest**

dbt operates as a Stack that can be orchestrated through a [Workflow](/resources/workflow/) Resource. A Workflow is a DataOS Resource that represents a Directed Acyclic Graph (DAG) of jobs, where each job is executed using a Stack. It acts as an orchestrator for a Stack. 

**A DBT workflow is composed of the following sections:** 

- [Workflow-specific section](#configure-the-dbt-workflow-specific-section)
- [Stack-specific section]()


### **Configure the DBT Workflow-specific section**

The Workflow-specific section contains configurations specific to the Workflow Resource. 

The code snippet provided below shows a sample Workflow manifest.


=== "Syntax"

    ```yaml title="syntax_resource_dbt_meta_section.yaml"
    name: ${dbt-workflowname}
    version: v1
    type: workflow
    tags:
      - ${tag1}
    description: ${DBT Sample Workflow}
    workspace: sandbox
    workflow:
      dag:
        - name: ${dbt-jobname}
          title: ${title}
          spec:
            stack: dbt+python:1.0
            compute: ${compute-name}
            resources:
              requests:
                cpu: 1000m
                memory: 250Mi
              limits:
                cpu: 1000m
                memory: 250Mi
            logLevel: ${log-level}
            stackSpec:
              #stack specific section
    ```

=== "Sample"  

    ```yaml title="syntax_resource_dbt_meta_section.yaml"
    name: dbt-workflow-v01
    version: v1
    type: workflow
    tags:
      - tag1
    description: DBT Sample Workflow
    workspace: sandbox
    workflow:
      dag:
        - name: dbt-workflow-job-v2
          title: dbt Sample Test Jobs
          spec:
            stack: dbt+python:1.0
            compute: 
            resources:
              requests:
                cpu: 1000m
                memory: 250Mi
              limits:
                cpu: 1000m
                memory: 250Mi
            logLevel: INFO
            stackSpec:
               #stack specific section
    ```


### **Declare the configuration for DBT `stackSpec` section**

The [Workflow](/resources/workflow/) Resource comprises of a `stackSpec` section (or a mapping) containing the attributes of the Stack to be orchestrated. Specifically within the dbt Stack context, the stackSpec includes diverse configuration file.

The manifest below shows a sample structure of the DBT `stackSpec` Section:

=== "Syntax"

    ```yaml title="syntax_dbt_stackspec_section.yaml"
    stackSpec:
      profiles:
        my_new_project:
          target: ${dev}
          outputs:
            dev:
              type: ${data platform type}
                #database- specific connection details

      dbt_project:
        name: ${project_name}
        version: '1.0.0'
        config-version: 2
        model-paths: ${path of the model}
        profile:  ${project_name}
        target-path: "target"  #directory which will store compiled SQL files
        clean-targets:         #directories to be removed by `dbt clean`
          - "target"
          - "dbt_packages"
        models:
          ${modelname}:
              +materialized: view

      dbt_packages:
        packages:
          - git: "https://github.com/dataos/dbt101.git"
    ```

=== "Sample"

    ```yaml title="sample_dbt_stackspec_section.yaml"
    stackSpec:
      profiles:
        dbtlearnnew:
          target: dev
          outputs:
            dev:
              type: snowflake
              account: wylos-aidb-aq8123
                #account_id
              user: iamgroot
              password: iamgroot@123
              database: SAMPLEDB
              warehouse: COMPUTE_WH
              schema: PUBLIC
              role: DBTADMIN
              threads: 4
      dbt_project:
        name: 'dbtlearnnew'
        version: '1.0.0'
        config-version: 2
        model-paths: ["models"]
        profile: 'dbtlearnnew'
        target-path: "target"  #directory which will store compiled SQL files
        clean-targets:         #directories to be removed by `dbt clean`
          - "target"
          - "dbt_packages"
        models:
          dbtlearnnew:
                +materialized: view
      dbt_packages:
        packages:
          - git: "https://github.com/dataos/dbt101.git"
    ```

### Stack spec section

The DBT `stackSpec` section comprises of following key attributes:

- [Profiles section](#profiles-section)
- [Projects section](#project-section)
- [Packages section](#packages)

Each of these sections is mapping and comprises several section-specific attributes. The subsequent parts provide details on the necessary configurations.

### **Profiles section**

The `profiles.yml` file is a configuration file that specifies connection details for target databases. It includes information to connect to the data warehouse/platform.

=== "Syntax"

    ```yaml
    profiles:
      <profile-name>:
        target: dev
        outputs:
          dev:
            type: <bigquery | postgres | redshift | snowflake >
            threads: 4
            #database-specific connection details
    ```

=== "Sample"

    ```yaml
    profiles:
      my_new_project:
        target: dev
        outputs:
          dev:
            type: snowflake 
            threads: 4
            #datawarehouse-specific connection details
    ```

The following table provides a comprehensive overview of the various attributes within the Profile-specific Section.
    
**Common Attributes**

| Attributes | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`profile`] | mapping | none |  my_project | mandatory |
| [`target`] | string | none | dev| mandatory |
| [`outputs`] | mapping | none | dev | mandatory |
| [`type`] | string | none | bigquery, postgres | mandatory |
| [`threads`] | string | none | [1-4] | mandatory |

<!-- Number of threads for dbt execution
The profile dbt uses to connect to data platform -->

### **Project section**

The `dbt_project.yml` serves as the primary configuration file which informs DBT about the context of your project and how to transform your data.

It is crucial for  DRY (Don't Repeat Yourself) analytics code. Essentially, it acts as the repository for project-wide default configurations, and all objects will inherit from it unless overridden at the model level.

<!-- To know about how to structure the project [Project structure](https://www.notion.so/Project-structure-8b04c17cbf684271ac8c916077d5f786?pvs=21) -->

=== "Syntax"

    ```yaml title="syntax_dbt_project_section.yaml" 
    #Project names should contain only lowercase characters and underscores.
    name: ${project_name}
    version: ${project_version}
    config-version: 2

    #This setting configures which "profile" dbt uses for this project.
    profile: ${profile_name}

    #These configurations specify where dbt should look for different types of files.
    #The `model-paths` config, for example, states that models in this project can be
    #found in the "models/" directory. You probably won't need to change these!
    model-paths: [${model_paths}]

    #Configuring models
    models:
      ${project_name}:
        ${model_group}:
        #Config indicated by + and applies to all files under models/example/
        +materialised: ${materialisation}
    ```

=== "Syntax"

    ```yaml title="sample_dbt_project_section.yaml" 
    name: training_dbt
    version: 1.0.0
    config-version: 2

    profile: training_dbt
      #These configurations specify where dbt should look for different types of files.
      #The model-paths config, for example, states that models in this project can be
      #found in the "models/" directory. You probably won't need to change these!
      model-paths: [models]

      #Configuring models
      models:
        training_dbt:
          example:
          #Config indicated by + and applies to all files under models/example/
          +materialised: view
    ```

   
**Attributes of project in stackSpec section**

| Attributes | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| `name` | string | none | Your project's name in snake case | mandatory |
| `version` | version | none | Version of your project | mandatory |
| `require-dbt-version` | version range | none | Restrict your project to only work with a range of dbt Core versions | optional |
| `profile` | string | none | The profile dbt uses to connect to your data platform | mandatory |
| `model-paths` | string | none | Directories to where your model and source files live | mandatory |
| `seed-paths` | list of strings | none | Directories to where your seed files live | optional |
| `test-paths` | list of strings  | none | Directories to where your test files live | optional |
| `analysis-paths` | list of strings  | none | Directories to where your analyses live | optional |
| `macro-paths` | list of strings  | none | Directories to where your macros live | optional |
| `snapshot-paths` | list of strings  | none | Directories to where your snapshots live | optional |
| `docs-paths` | list of strings  | none | Directories to where your docs blocks live | optional |
| `clean-targets` | list of strings  | none | List of clean targets for the project | optional |
| `models` | list of dictionaries | none | List of model configurations | mandatory |

<!-- [Attribute of dbt `stackSpec` section](https://www.notion.so/Attribute-of-dbt-stackSpec-section-6150f99201844a99a3c9e8a6f4aead5e?pvs=21) -->

### **dbt_packages section**

The `dbt_packages` section is designed to specify the dbt projects that you wish to incorporate as dependencies. These projects, referred to as dbt packages, can be seamlessly integrated into your own dbt project, fostering modularity and code sharing.

=== "Syntax"

    ```yaml
    dbt_packages:
      packages:
      - git: <GIT_REPO_URL>
    ```
=== "Sample"
    
    ```yaml
    dbt_packages:
      packages:
        - git: "https://github.com/iamgroot/dbt-101.git"
    ```
      
### **Apply the manifest using CLI**

Use the apply command to apply the workflow using CLI.

=== "Command"

    ```shell
    dataos-ctl resource apply -f ${yaml-file-path} -w ${workspace-name}
    #or
    dataos-ctl apply -f ${yaml-file-path} -w ${workspace-name}
    ```
=== "Example"

    ```shell
    dataos-ctl resource apply -f dbt.yaml -w sandbox # By default the workspace is public
    #or
    dataos-ctl apply -f dbt.yaml -w sandbox
    ```

**Get Status of the Workflow**

=== "Command"

    ```shell
    dataos-ctl resource get -t ${workspace-name} -w {sandbox} -n ${workflow-name}
    ```

=== "Example"

    ```shell
    dataos-ctl resource get -t workflow -w sandbox -n dbt-worfklow-v01
    #Expected Output
    INFO[0000] 🔍 get...
    INFO[0001] 🔍 get...complete

              NAME        | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |   OWNER
    ----------------------|---------|----------|-----------|--------|---------|-------------
      dbt-workflow-v01   |   v1    | workflow |   sandbox  | active | running |   tmdc
    ```

To check this information for all users in a specific Workspace, add the `-a` flag to the command as shown below.

=== "Command"

    ```shell
    dataos-ctl resource get -t workflow -w ${workspace-name} -a
    ```

=== "Example"

    ```shell
    dataos-ctl resource get -t workflow -w sandbox -a
    #Expected Output
    INFO[0000] 🔍 get...
    INFO[0001] 🔍 get...complete

              NAME           | VERSION |   TYPE   | WORKSPACE | STATUS |  RUNTIME  |       OWNER
    -------------------------|---------|----------|-----------|--------|-----------|--------------------
      dbt-workflow-v01       | v1      | workflow | sandbox    | active | succeeded | wonderwoman
      cnt-product-demo-01    | v1      | workflow | sandbox    | active | running   | tmdc
      cnt-product-demo-01-01 | v1      | workflow | sandbox    | active | failed    | otheruser
      cnt-city-demo-01001    | v1      | workflow | sandbox    | active | succeeded | iamgroot
    ```

**Get Runtime Information**

To refresh or see updates on the Workflow progress, add the `-r` flag to the `[get runtime](/interfaces/cli/command_reference/#get-runtime)` command:

```bash
dataos-ctl -i get runtime " cnt-product-demo-01 | v1 | workflow | sandbox" -r
```

Press `Ctrl + C` to exit.

For any additional flags, use help by appending `-h` with the respective command.

# Case study

<!-- [End to end Analytics use case](https://www.notion.so/End-to-end-Analytics-use-case-dd50822055e84167b8f90ca0c3076311?pvs=21) -->
<!-- Draft 3 -->
    
### **Summary**
    
This dbt project aims to transform and prepare data through various stages, starting with cleaning and renaming in the staging phase, moving to intermediate transformations, building a core data layer, creating non-volatile datasets for mapping, and finally performing detailed analytics. The use cases highlight the specific objectives of each transformation, contributing to a comprehensive and well-organized data analytics workflow.
    
### Staging Folder
    
```sql title="stg_jaffle_shop_customers.sql"
select
    id as customer_id,
    concat(first_name, ' ', last_name) as customer_name,
    current_timestamp() as dp_load_date
from {{ source('jaffle_shop', 'customers') }}

```

```sql title="stg_jaffle_shop_orders.sql"
#Renamming columns for deeper understanding

select
    id as order_id,
    user_id as customer_id,
    order_date,
    status,
    _etl_loaded_at
from {{ source('jaffle_shop', 'orders') }}
```

### Intermediate Folder
    
**Payment Type Analysis:**

- Analyze payment data to understand the distribution of cash and credit payments.

**Total Payment Amount Calculation:**

- Calculate the total amount paid for orders with a "success" payment status.

- **`in_payment_type_amount.sql`:**
- Create a CTE (`order_payments`) based on the `stg_stripe_payment`.
- Summarize payment amounts based on different payment types and order statuses.

```sql
-- int_payment_type_amount.sql
with order_payments as (
    select * from {{ ref('stg_stripe_payment') }}
)
select
    order_id,
    sum(
        case
        when payment_type = 'cash' and
            status = 'success'
        then amount
        else 0
        end
    ) as cash_amount,
    sum(
        case
        when payment_type = 'credit' and
            status = 'success'
        then amount
        else 0
        end
    ) as credit_amount,
    sum(case
        when status = 'success'
        then amount
        end
    ) as total_amount
from order_payments
group by 1

```
    
### Marts/Core Folder
    
1. **Customer Dimension Creation:**
    - Create a dimensional view of customers, incorporating information from the staged customer data.
2. **Customer Data Exploration:**
    - Use the `dim_customers` view for exploratory analysis and understanding customer attributes.
3. **`dim_customers.sql`:**
    - **Transformation Objective:**
        - Create a CTE (`customers`) based on the `stg_jaffle_shop_customers`.
        - Select all columns from the `customers` CTE.

```sql title="customers.sql"
with customers as (
    select * from {{ ref('stg_jaffle_shop_customers') }}
)
select * from customers
```

**Order Fact Creation:**

- Create a fact table (`fact_orders`) representing detailed order information, including payment types and amounts.
1. **Order Completion Flag:**
    - Introduce a flag (`is_order_completed`) indicating whether an order is completed or not based on its status.

```sql title="fact_orders.sql"
-- fact_table
with orders as (
    select * from {{ ref('stg_jaffle_shop_orders' )}}
),
payment_type_orders as (
    select * from {{ ref('in_payment_type_amount_per_order' )}}
)
select
    ord.order_id,
    ord.customer_id,
    ord.order_date,
    pto.cash_amount,
    pto.credit_amount,
    pto.total_amount,
    case
    when status = 'completed'
    then 1
    else 0
    end as is_order_completed
from orders as ord
left join payment_type_orders as pto ON ord.order_id = pto.order_id
```
    
1. **`fact_orders.sql`:**
    - **Transformation Objective:**
        - Create CTEs (`orders` and `payment_type_orders`) based on the `stg_jaffle_shop_orders` and `in_payment_type_amount_per_order`.
        - Perform final transformations, including joining relevant CTEs and calculating additional fields.

**Possible Business Use Cases:**

1. **Customer Paid Amount Aggregation:**
    - Aggregate the total paid amount for each customer based on completed orders.
2. **Customer Classification:**
    - Classify customers into different categories (Regular, Bronze, Silver, Gold) based on their total paid amounts.

```sql title="customer_range_based_on_total_paid_amount.sql"
with fact_orders as (
    select * from {{ ref('fact_orders')}}
),
dim_customers as (
    select * from {{ ref('dim_customers' )}}
),
total_amount_per_customer_on_orders_complete as (
    select
        cust.customer_id,
        cust.customer_name,
        SUM(total_amount) as global_paid_amount
    from fact_orders as ord
    left join dim_customers as cust ON ord.customer_id = cust.customer_id
    where ord.is_order_completed = 1
    group by cust.customer_id, customer_name
),
customer_range_per_paid_amount as (
    select * from {{ ref('seed_customer_range_per_paid_amount' )}}
)
select
    tac.customer_id,
    tac.customer_name,
    tac.global_paid_amount,
    crp.classification
from total_amount_per_customer_on_orders_complete as tac
left join customer_range_per_paid_amount as crp
on tac.global_paid_amount >= crp.min_range
and tac.global_paid_amount <= crp.max_range
```
### Seeds Folder
    
**Objective:**
Create non-volatile datasets for mapping and enriching data.
    
**Use Case:**
In the `seeds` folder, we store small datasets to map values.
    
1. **`seed_customer_range_per_paid_amount.csv`:**
   - **Transformation Objective:**
      - Define ranges for customer classifications based on total paid amounts.
      - Ranges include Regular, Bronze, Silver, and Gold classifications.

Example:
    
```sql title="seed_customer_range_per_paid_amount.csv"
#with ranges mapping
min_range,max_range,classification
0,9.999,Regular
10,29.999,Bronze
30,49.999,Silver
50,9999999,Gold
```
Run command to materialize CSV file into a table in data platform.
    
### Analyses Folder
    
**Objective:**
Perform detailed analytics and generate insights for reporting.

**Use Case:**
In the `analyses` folder, we create SQL queries to analyze and derive insights.

1. **`customer_range_based_on_total_paid_amount.sql`:**
    - **Transformation Objective:**
        - Create CTEs based on `fact_orders`, `dim_customers`, `total_amount_per_customer_on_orders_complete`, and `customer_range_per_paid_amount`.
        - Analyze and categorize customers based on their total paid amounts.
        
    
Example:
    
```sql title="customer_range_based_on_total_paid_amount.sql"
#based on the completed orders and the total amount paid, the customer classification range.

with fct_orders as (
select * from {{ ref('fct_orders')}}
),
dim_customers as (
select * from {{ ref('dim_customers' )}}
),
total_amount_per_customer_on_orders_complete as (
select
cust.customer_id,
cust.first_name,
SUM(total_amount) as global_paid_amount
from fct_orders as ord
left join dim_customers as cust ON ord.customer_id = cust.customer_id
where ord.is_order_completed = 1
group by cust.customer_id, first_name
),
customer_range_per_paid_amount as (
select * from {{ ref('seed_customer_range_per_paid_amount' )}}
)
select
tac.customer_id,
tac.first_name,
tac.global_paid_amount,
crp.classification
from total_amount_per_customer_on_orders_complete as tac
left join customer_range_per_paid_amount as crp
on tac.global_paid_amount >= crp.min_range
and tac.global_paid_amount <= crp.max_range
```
        
It will give each customer the total amount paid and its corresponding range.

       