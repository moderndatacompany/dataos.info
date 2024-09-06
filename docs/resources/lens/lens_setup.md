---
title: Setting Up Lens
---

# Setting Up Lens

Set up the Lens project folder to include the Dockerfile, model folder, and `user_groups.yml` file.

In the Model folder, the Lens model will be defined, encompassing SQL mappings, logical tables, logical views, and user groups. Each folder contains specific files related to the Lens model.

### **Prerequisites**

Before setting up Lens, ensure you have all its dependencies installed.

The following page will provide step-by-step instructions and additional resources to help you install and configure these dependencies, ensuring a smooth setup process for Lens.

[Prerequisites for Lens](/resources/lens/installing_prerequisites/)

### **Set Up Lens Project Folder**

Set up the Lens project folder or you can download the following template.

[lens template](/resources/lens/lens_setup/lens-project-template.zip)

- Open the Model folder in the preferred editor. The Model folder will have the following hierarchy:

``` bash
model
├── sqls 
│   └── sample.sql
├── tables 
│   └── sample_table.yml //A logical table definition includes joins, dimensions, measures, and segments.
├── views 
│   └── sample_view.yml //View reference dimensions, measures, and segments from tables.
└── user_groups.yml //User groups organize users for easier policy application.
docker-compose.yml // Orchestrates multi-container services (e.g., database, web server)
```

- **`sqls` Folder**
    - This directory will contain SQL scripts corresponding to the dimensions of your tables.  A dedicated SQL file needs to be maintained for each table. The SQL dialect used will be source-specific.

- **Create `tables` Folder**
    - This directory will store your logical tables, with each table defined in a separate YAML file.
    
- **Create `views` Folder**
    - This directory will store all your logical views.

-  **Add user_groups.yml**
    - User groups organize users for easier policy applications to control access.
    - Presently, we have a 'default' user group defined in the YAML that includes all users.

- **Add a docker-compose.yml**
    - Docker compose is used to test the Lens in the development enviroment before deployment.

    - Here add data source details and update Lens meta details.  


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
          
  >Ensure you have access to the compute of the source. This needs to be verified at source end.

  **Data Source attributes for connecting via depot**

  ```yaml
    # Data Source
    # This defines env variables for connecting to the source via the depot
    LENS2_SOURCE_TYPE: depot
    LENS2_SOURCE_NAME: depot_name #add the name of the depot 
    DATAOS_RUN_AS_APIKEY: ****** # Add the user API Key for the env
  ```

  **Data Source attributes to connect via Minerva or Themis Cluster**

  ```yaml
    # Data Source
    # This defines env variables for connecting to the source via the cluster
    LENS2_SOURCE_TYPE: minerva #If you want to connect via Themis, change the source type to Themis 
    LENS2_SOURCE_NAME: cluster_name #add the cluster name
    LENS2_SOURCE_CATALOG_NAME: catalog_name #add the catalog name
    DATAOS_RUN_AS_APIKEY: ******
  ```
          
      
  - When connecting with different sources, refer to the [data source guide](/resources/lens/data_sources/) for various sources, as each may need its own specific settings."

4. **Verify Service Configuration:**

    - make sure the image tag is up to date or is the same as the one you pulled in the prerequisite stage.

## Testing Lens in Development Environment

Once you've completed the Lens setup(adding source connection detail) and have defined the Lens model you can start Lens. It is considered a good practice to test your Lens and ensuring the data model is error free before deploying it. the docker-compose file will help us for the same.

> <b>Note:</b> Ensure your working directory is the Lens project directory and that the API Key is correctly passed as defined in your docker-compose.yml.

You can test Lens in the development environment by running:

=== "Code"

    ```bash
    docker-compose up  #run docker-compose up command in terminal
    ```

=== "Output"

   The following output indicates that the Lens server has successfully started locally.
  
    ```bash
    lens2-api-1  | Loaded  /app/scripts/config.js
    lens2-api-1  | 🔥 Table Store (0.35.55-01 ) is assigned to 3030 port.
    lens2-api-1  | 🔗 Lens2 SQL Service (PostgreSQL) is listening on 0.0.0.0:5432
    lens2-api-1  | 🚀 Lens2 API server (0.35.55-01 ) is listening on 4000
    ```

## Interacting with Lens in Development Environment

Now that Lens is successfully running without errors, you can begin interacting with it using SQL APIs, REST APIs, or GraphQL APIs. This setup allows you to thoroughly test Lens before proceeding to deployment, ensuring all functionalities are working as expected.

### **Interacting via SQL API**

Lens 2.0 exposes a PostgreSQL-compatible interface, enabling you to query Lens tables and views using standard PostgreSQL syntax.

To interact with Lens via PostgreSQL, you have the following options:

- **PostgreSQL Client (psql):** This command-line tool allows direct interaction with your PostgreSQL database. Use psql to run queries, manage your database, and perform various administrative tasks.

- **VS Code Extension:** Use the PostgreSQL Client extension for Visual Studio Code. This extension enables SQL query execution and database management within VS Code.

**PostgreSQL Client(psql)**

The following setup will allow access using `user` as the username, `password` as the password, and any valid string as the database name in format `lens:${workspace_name}:${lens_name}.

=== "Syntax"

    ```bash
    psql -h ${host_name} -p ${port_name} -d ${database_name}
    ```

=== "Example"

    ```bash
    psql -h localhost -p 25432 -d lens:public:sales_analysis
    ```

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

To interact with REST APIs. You can use tools like `curl`, [Postman](https://www.postman.com/).

For instance, to test Lens in your development environment using Postman, upload the following API collection to Postman.

[Lens2-API](/resources/lens/lens_setup/Lens2-APIs.postman_collection.json)


Now, to make a basic `GET` request using Postman, follow these steps:

1. **Create a New Request**:
    - Open Postman and click on the **New** button in the top left corner.
    - Select **Request** from the dropdown menu.
2. **Configure the Request**:
    - **Enter Request Name**: Provide a name for your request.
    - **Select Collection**: Choose the uploaded collection.
3. **Set the HTTPS Method**:
    - In the request tab, select `GET` from the dropdown menu next to the URL input field.
4. **Enter the Request URL**:
    - Enter the full URL for the API endpoint you want to access. For example:
        
        ```bash
        http://localhost:8080/lens2/api/${lens_name}/v2/meta
        ```
    **Command Paramter**

      - `localhost:8080` represents the local or development environment for Lens, used for building and testing configurations.
      - `/lens2/api/` is the api prefix
      - `${lens_name}` is the placeholder for lens, replace it to the actual lens undergoin testing.
          
5. **Ensure the following header is passed in Authorization when running the API**
      
      ```bash
      Type: Bearer Token
      Token: <Your API Key> #Use the API key of the env defined in docker-compose.yml
      ```
6. Click **Send**

**Example response:**

```json
{
  "name": 
  "description": [],
  "authors": [],
  "devMode": true,
  "source": {
      "type": "minerva",
      }
          },
  "timeZones": ["UTC"],
  "tables": [
      {
          "name": "product_analysis",
          "type": "view",
          "title": "Product Analysis",
          
               }     ]
                
            
```



>*You can now successfully test your lens in postman via REST APIS.*

To interact with the deployed lens read the detailed doc [here](/resources/lens/consumption_using_rest_apis/)


## Next Step

[Deploying Lens model on DataOS](/resources/lens/lens_deployment/)








