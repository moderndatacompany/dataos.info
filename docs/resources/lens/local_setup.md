# Lens Local Setup

Set up the Lens project folder containing the Dockerfile and the model folder and user_groups.yml. 

In the Model folder, you'll define your Lens model, including SQL mapping, logical tables, logical views, and user groups. Each folder has a specific file related to your Lens model


## Step 1: Set Up Lens 2 Project

Set up the Lens2 project folder or you can download this template for 

[lens template](/resources/lens/local_setup/lens-project-template.zip)

- Open the Model folder in the editor of your choice. Your Model folder will have the following hierarchy:

``` bash
model
├── sqls 
│   └── sample.sql
├── tables 
│   └── sample_table.yml //A logical table definition includes joins, dimensions, measures, and segments. 
├── views 
│   └── sample_view.yml //View reference dimensions, measures, and segments from tables.
└── user_groups.yml //User groups organize users for easier policy application.
```

- **`sqls` Folder**
    - This directory will contain SQL scripts corresponding to the dimensions of your tables.  A dedicated SQL file needs to be maintained for each table. The SQL dialect used will be source-specific.
- **Create `tables` Folder**
    - This directory will store your logical tables, with each table defined in a separate YAML file.
- **Create `views` Folder**
    - This directory will store all your logical views.
1. **Add user_groups.yml**
    - User groups organize users for easier policy applications to control access.
    - Presently, we have a 'default' user group defined in the YAML that includes all users.

2.  Configure the docker-compose.yml file to add data source details and update Lens meta details.  




## Configure the docker-compose manifest file

The `docker-compose.yml` file defines how to set up and run your Docker containers for Lens 2.0. Customize this file to fit your specific environment and requirements.


```bash
version: "2.2"

x-lens2-environment: &lens2-environment

# DataOS

DATAOS_FQDN: <dataos_fqdn>.dataos.app #add the URL for the environment. Ensure you are passing the API key for this env

# Overview

LENS2_NAME: lens_name
LENS2_DESCRIPTION: "Purpose of the lens"
LENS2_TAGS: "lens2, ecommerce, sales and customer insights" #add tags for better discoverability
LENS2_AUTHORS: "author_name" #add the owner name here
LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"

# Data Source

# This defines env variables for connecting to the source via the depot

LENS2_SOURCE_TYPE: ${depot}
LENS2_SOURCE_NAME: ${depot_name}
LENS2_SOURCE_CATALOG_NAME: ${catalog_name}
DATAOS_RUN_AS_APIKEY: ******   #USER APIKEY

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

services:
api:
restart: always
image: rubiklabs/lens2:0.35.55-01 
ports:
- 4000:4000
- 25432:5432
- 13306:13306
environment:
<<: *lens2-environment

volumes:
- ./model:/etc/dataos/work/model
```

Modify the docker-compose.yml file to tailor it to include environment-URL, lens meta info, and, source details as per your requirement - 

1. **Adjust the environment URL according to your preferences.**
    
```yaml
# edit this section in your docker-compose.yml file
# DataOS
  DATAOS_FQDN: emerging-hawk.dataos.app #add the URL for the environment you prefer to use. 
```
    
2. **Update Lens meta info, including name, description, tags, and author details.**
    
```yaml
# Overview
  LENS2_NAME: lens_name 
  LENS2_DESCRIPTION: "Purpose of the lens"
  LENS2_TAGS: "lens2, ecom, sales and customer insights" #add tags for better discoverability
  LENS2_AUTHORS: "author_name" #add the owner name here
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
```

3. **Customize the source details:**

- If connecting via the depot, refer to the provided environmental variables in the syntax below. Currently, supported depot types include - JDBC, PostgreSQL, MySQL, MS SQL, Snowflake, Bigquery, and Redshift.
        
**(Ensure you have access to the compute of the source. This needs to be verified at source end.)**

Environment variable for connecting via depot

```yaml
  # Data Source
  # This defines env variables for connecting to the source via the depot
  LENS2_SOURCE_TYPE: depot
  LENS2_SOURCE_NAME: depot_name #add the name of the depot 
  DATAOS_RUN_AS_APIKEY: ****** # Add the user API Key for the env
```

Environment variable to connect via Minerva or Themis

```yaml
  # Data Source
  # This defines env variables for connecting to the source via the cluster
  LENS2_SOURCE_TYPE: minerva #If you want to connect via Themis, change the source type to Themis 
  LENS2_SOURCE_NAME: cluster_name #add the cluster name
  LENS2_SOURCE_CATALOG_NAME: catalog_name #add the catalog name
  DATAOS_RUN_AS_APIKEY: ******
```
        
    
- If connecting without a depot, consult the [environmental variables guide](https://www.notion.so/Supported-Sources-5d0da3eaf1b14eca82e4d7d1aafe6b86?pvs=21) for different sources, as each may require a specific set of settings.

4. **Verify Service Configuration:**
    - make sure the image tag is up to date or is the same as the one you pulled in the prerequisite stage.

## Starting Lens Locally

Once you've completed the Lens 2.0 setup(adding source connection detail) and have defined the Lens model you can start Lens. 

> **Note:** Ensure your working directory is the Lens project directory
> 

You can start Lens locally by running:

=== "Code"

    ```bash
    docker-compose up  #run docker-compose up command in terminal
    ```

=== "Output"

    The output lo like following indicates that the lens server has started locally

    ```bash
    lens2-api-1  | Loaded  /app/scripts/config.js
    lens2-api-1  | 🔥 Table Store (0.35.55-01 ) is assigned to 3030 port.
    lens2-api-1  | 🔗 Lens2 SQL Service (PostgreSQL) is listening on 0.0.0.0:5432
    lens2-api-1  | 🚀 Lens2 API server (0.35.55-01 ) is listening on 4000
    ```

## Interacting with Lens in Local Environment

Now that Lens is successfully running locally without errors, you can begin interacting with it using SQL APIs, REST APIs, or GraphQL APIs. This local setup allows you to thoroughly test Lens before proceeding to deployment, ensuring all functionalities are working as expected.

>Note: Ensure that the API Key is correctly passed as defined in your docker-compose.yml.
>

### **Interacting via SQL API**

Lens 2.0 exposes a PostgreSQL-compatible interface, enabling you to query Lens tables and views using standard PostgreSQL syntax.

To interact with Lens via PostgreSQL, you have the following options:

- **PostgreSQL Client (psql):** This command-line tool allows direct interaction with your PostgreSQL database. Use psql to run queries, manage your database, and perform various administrative tasks.

- **VS Code Extension:** Use the PostgreSQL Client extension for Visual Studio Code. This extension enables SQL query execution and database management within VS Code.

**PostgreSQL Client(psql)**

The following setup will allow access using `user` as the username, `password` as the password, and any valid string as the database name in format `lens:<workspace_name>:<lens_name>.

=== "Syntax"

    psql -h <host_name> -p <port_name> -d <database_name>

=== "Example"

    psql -h localhost -p 25432 -d lens:public:sales_analysis

**Connection Details:**

Use the following details to connect to the Postgresql interface:

<aside class="callout">
💡 Always refer to 'ports' within the services section in `docker-compose.yml` for the exposed port.
</aside>

**Using VS Code Extension:**

- Install the PostgreSQL Client extension.

- Click the Create Connection button on the left side panel.

- Configure the connection with the following details and click +connect:

| **POSTGRES PROPERTY** | **DESCRIPTION** | **EXAMPLE** |
| --- | --- | --- |
| Host  | host name | `localhost` |
| Port | port name | `25432` |
| Database | database name | `postgres` |
| Username | dataos-username | `postgres` |
| Password | dataos-user-apikey | `dskhcknskhknsmdnalklquajzZr=` |

- Once connected, hover over the postgres folder and click the terminal icon to open the terminal for querying.

- Execute queries in the terminal as needed. For example:

```sql
postgres=> \d #listing all the tables and databases

#Expected_output
 Schema |         Name         | Type  |  Owner   
--------+----------------------+-------+----------
 public | channel              | table | postgres
 public | customer             | table | postgres
 public | product_analysis     | table | postgres
 public | products             | table | postgres
 public | transaction_analysis | table | postgres
 public | transactions         | table | postgres
(6 rows)
```

### **Interacting Via REST API**

The REST API is enabled by default and secured using API scopes. It consists of a base path and API scopes:

- **Base Path:** All REST API endpoints are prefixed with /lens2/api. For example, /v2/meta is available at /lens2/api/<data_model_name>/v2/meta.

- **API Scopes:** Endpoints are secured by API scopes, restricting access based on user permissions. Follow the principle of least privilege to grant only necessary access.

To explore various API endpoints and scopes, refer to the [API Endpoints and Scopes](/resources/lens/api_endpoints_and_scopes) page.

You can use [Postman](https://www.postman.com/) to interact with Lens REST APIs. Start by importing the following Postman collection:

[Lens2-API](/resources/lens/local_setup/Lens2-APIs.postman_collection.json)








