
## Local development environment

Before deploying models to the development environment, it is important to ensure proper verification and validation. A recommended practice is to configure a Docker Compose manifest file (docker-compose.yml). While configuring this file is optional, it is widely considered a best practice to run and test models in the local environment to catch and resolve potential errors early. This proactive approach helps streamline the development process, ensuring smoother deployments and reducing the risk of issues arising in later stages.

## Add a `docker-compose.yml` manifest file

To do a local testing, add a **`docker-compose.yml`** manifest file. This file allows you to simulate the full development environment locally, ensuring that all necessary components are properly configured. The `docker-compose.yml` file defines how to set up and run Docker containers for Lens. 

> Always create the docker-compose.yml file in parallel to the model directory. 

<details><summary>Click here to see the docker-compose.yml file</summary>

```yaml
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
</details>

## Configure the docker-compose manifest file

Configure the `docker-compose.yml` manifest file to tailor it to include environment-URL, lens meta info, and, source details as per requirement: 

1. **Adjust the environment URL according to preferences.**
    
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

    - If connecting via the depot, refer to the provided environmental   variables in the syntax below. Currently, supported depot types include JDBC, PostgreSQL, MySQL, MS SQL, Snowflake, Bigquery, and Redshift.
            
        >Ensure access to the compute of the source. This needs to be verified at source end.

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
    - When connecting with different sources, refer to the [data source guide](/resources/lens/data_sources/) for various sources, as each may need its own specific settings.

4. **Verify Service Configuration:**

    - In the service configuration, the image attribute specifies the container image to be used. Ensure that the image tag is up to date or matches the version pulled during the prerequisite setup.

## Testing Lens in development environment

Run the `docker-compose.yml` manifest file by running `docker-compose up` command. Ensure that the working directory is the Lens project directory and that the API key is correctly configured as specified in the docker-compose.yml file.

Lens can be tested in the development environment by running:

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
## Exploring Lens in development environment

!!! abstract "Quick Guide"
    To quickly get started with testing Lens locally, follow the [quick guide on testing your Lens model locally](/resources/lens/testing_locally/). This guide provides a step-by-step approach to validating your SQL queries within the data model and ensures that tables and joins work as expected before deploying them to DataOS.

Now that Lens model is successfully running without errors using docker-compose, one can begin exploring it using SQL APIs, REST APIs, or GraphQL APIs. This setup allows to thoroughly test Lens before proceeding to deployment, ensuring all functionalities are working as expected.

### **Exploring Lens via SQL API**

Lens exposes a PostgreSQL-compatible interface, enabling to query Lens tables and views using standard PostgreSQL syntax.

To interact with Lens through PostgreSQL, the following options are available:

- **PostgreSQL Client (psql):** This command-line tool allows direct interaction with PostgreSQL database. Use psql to run queries, manage database, and perform various administrative tasks.

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

- Click the **Create Connection** button on the left side panel.

- Configure the connection with the following details and click **+connect**:

| **POSTGRES PROPERTY** | **DESCRIPTION** | **EXAMPLE** |
| --- | --- | --- |
| Host  | host name | `localhost` |
| Port | port name | `25432` |
| Database | database name | `postgres` |
| Username | dataos-username | `postgres` |
| Password | dataos-user-apikey | `dskhcknskhknsmdnalklquajzZr=` |

- Once connected, hover over the postgres folder and click the terminal icon to open the terminal for querying.

- Execute queries in the terminal as needed. For example:

```bash
postgres=> \dt #listing all the tables in the connected database.

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
**Here are some more commands for reference**

- Show the schema and details of a specific table.

    ```bash 
    \d [table_name]
    ```
    for example:

    ```bash
    \d customers
    ```

- List all databases in the PostgreSQL server.

    ```bash
    \l
    ```

- List all roles and users.

    ```bash
    \du
    ```

- List all schemas in the database.

    ```bash
    \dn
    ```

- List all views in the connected database.

    ```bash
    \dv
    ```

- Exit the PostgreSQL prompt.

    ```bash
    \q
    ```

### **Exploring Lens via REST API**

To interact with REST APIs use tools like `curl`, [Postman](https://www.postman.com/).

For instance, to test Lens in development environment using Postman, upload the following API collection to Postman.

[Lens2-API](/resources/lens/lens_setup/Lens2-APIs.postman_collection.json)


Now, to make a basic `GET` request using Postman, follow these steps:

1. **Create a New Request**:
    - Open Postman and click on the **New** button in the top left corner.
    - Select **Request** from the dropdown menu.
2. **Configure the Request**:
    - **Enter Request Name**: Provide a name for request.
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
      - `${lens_name}` is the placeholder for lens, replace it to the actual lens undergoing testing. For example, sales360, retail360.
          
5. **Ensure the following header is passed in Authorization when running the API**
      
      ```bash
      Type: Bearer Token
      Token: <DATAOS API Key> #Use the API key of the env defined in docker-compose.yml
      ```

6. Click **Send**

**Example response:**

```json
{
  "name": "",
  "description": [],
  "authors": [],
  "devMode": true,
  "source": {
    "type": "minerva"
  },
  "timeZones": ["UTC"],
  "tables": [
    {
      "name": "product_analysis",
      "type": "view",
      "title": "Product Analysis"
    }
  ]
}            
            
```



*You can now successfully test your lens in  development environment using postman via REST APIS.*

To interact with the deployed lens using REST APIs read the detailed doc [here](/resources/lens/exploration_of_deployed_lens_using_rest_apis/)


## Next Step

[Deploying Lens model on DataOS](/resources/lens/lens_deployment/)
