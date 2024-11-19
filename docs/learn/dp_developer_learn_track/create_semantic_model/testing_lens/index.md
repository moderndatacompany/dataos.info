# Test lens locally in development environment 

This guide walks you through steps to validate your SQL queries and Lens model configuration directly on your local machine to confirm that your tables, joins, and data relationships behave as intended before moving to the production environment on DataOS.

## Scenario

You're building a semantic model for a retail business to analyze purchase patterns and product affinity. The model needs to combine data from various sources—like customer purchase history, product catalogs, and sales data—into a unified view. You want to ensure that your Lens model effectively captures customer behavior and accurately reflects relationships between different products that customers tend to purchase together. 
Before deploying it to DataOS, test the model locally to ensure it performs accurately and provides valuable insights for business decisions.


## Prerequisites

Before moving to technicalities, ensure you have the following pre-requisites installed.

- Docker
- Docker compose
- Postman (optional)
- VS Code

### **Docker**

You use Docker to run Lens in an isolated environment on your local system. First, check if Docker is already installed by running `docker --version` in your terminal. If Docker is not installed, follow the appropriate installation guide for a particular operating system:

- **Linux:** Follow the installation guide for the Docker engine for Linux here: [Install Docker on Linux](https://docs.docker.com/desktop/install/linux-install/). It is recommended that you install the Docker Desktop version.
- **Windows:** Follow the installation guide of the Docker engine for Windows here: [Install Docker on Windows](https://docs.docker.com/desktop/install/windows-install/).
- **macOS:** Follow the installation guide of the Docker engine for Linux here: [Install Docker on macOS](https://docs.docker.com/desktop/install/mac-install/). 

### **Docker login**

Before pulling or pushing images from or to a private repository, you must log in to Docker Hub using the command line. 

```yaml
docker login --username=lensuser01
```

Replace with your username.

### **Docker pull**

After successfully logging in, pull the image from a registry, follow the below command:

```bash
docker pull tmdclabs/lens:0.35.60.
```

<aside class="callout">
🗣️ Tags identify specific versions of an image and can be updated over time. Ensure the latest image tag or the tag specified in the docker-compose YAML is pulled.
</aside>

### **Docker Compose**

Before installing Docker compose, it is advisable to check if it has already been installed on the system. Use the below command to check:

```bash
docker-compose --version
```
This command will return the installed version of Docker Compose if it is present. For example

```bash
docker-compose version 1.29.2, build 5becea4c
```

If Docker compose is not installed, refer to the following link to [install Docker compose](https://docs.docker.com/compose/install/).

### **Postman or Postman Extension for VS Code**

Postman is a tool that allows data developers to perform querying and testing within the Lens environment by sending API requests through an intuitive user interface. Follow the [Postman Installation Guide](https://learning.postman.com/docs/getting-started/installation/installation-and-updates/) to install Postman on your local system.

### **Python**

Python 3.7 or higher is required for managing directory structures and virtual environments. Check if Python is installed by running below command:

```bash
python3 --version
#Expected_Output
Python 3.8.14
```

The expected output should be **`Python 3.X`** or a version greater than 3.7. If the existing version is below 3.7, update Python by following the [Updating Python](https://ioflood.com/blog/update-python-step-by-step-guide/) guide.

If Python is not installed on the system, follow the steps below to download and install the appropriate version.

1. **Access the installation guide**: Visit the [Python Installation Guide](https://realpython.com/installing-python/#how-to-install-python-on-windows). This guide provides detailed instructions for installing Python on various operating systems, including Windows, macOS, and Linux.
2. **Download Python**: From the guide, select the link corresponding to the operating system and download the latest version of Python.
3. **Install Python**: Run the downloaded installer. Before clicking "Install Now," check the box that says "Add Python 3.x to PATH.” This step is crucial as it makes Python accessible from the command line.
4. **Verify Installation**: After installation, open a command line interface and run the following command to check the installed version of Python. The expected output should be **`Python 3.X`** or another version greater than 3.7.
    
    ```bash
    python3 -V
    #Expected_Output
    Python 3.8.14
    ```
    
5. **Update Python**: If the installed version of Python is older than 3.7, follow the guide on [Updating Python](https://ioflood.com/blog/update-python-step-by-step-guide/) to upgrade to a newer version that meets the Lens prerequisites.

## Visual Studio Code

Visual Studio Code (VS Code) must be installed on the local system to create a Lens model effectively. Below are the links for installing VS Code on various operating systems.

**Installation links by Operating System**

- **Linux**: Follow the detailed steps to install VS Code on your Linux system by accessing the [Install VS Code on Linux guide](https://code.visualstudio.com/docs/setup/linux).
- **Windows**: To install VS Code on a Windows machine, refer to the [Install VS Code on Windows guide](https://code.visualstudio.com/docs/setup/windows).
- **MacOS**: For MacOS users, installation instructions can be found in the [Install VS Code on macOS guide](https://code.visualstudio.com/docs/setup/mac).


<aside class="callout">
💡 Local testing is an optional step. However, we recommend always testing your semantic model locally before pushing it to the deploying stage.
</aside>

Now, you create a file `docker-compose.yml` in a folder parallel to your model folder (not within it).


```yaml
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: ${DATAOS-CONTEXT.dataos.app} 
  # Overview
  LENS2_NAME: ${Name of the Lens}
  LENS2_DESCRIPTION: "${Description of the Lens}"
  LENS2_TAGS: "${retail, sales and customer insights}"
  LENS2_AUTHORS: "${Author1, Author2}"
  LENS2_SOURCE_TYPE: ${minerva}
  LENS2_SOURCE_NAME: ${system}
  LENS2_SOURCE_CATALOG_NAME: ${icebase}
  DATAOS_RUN_AS_APIKEY: ${YOUR_DATAOS_APIKEY}
  # Log
  LENS2_LOG_LEVEL: error
  CACHE_LOG_LEVEL: "error"
  # Operation
  LENS2_DEV_MODE: true   
  LENS2_REFRESH_WORKER: true
  LENS2_SCHEMA_PATH: model
  LENS2_PG_SQL_PORT: 5432
  CUBESTORE_DATA_DIR: "/var/work/.store"

services:
  api:
    restart: always
    image: rubiklabs/lens2:0.35.60-8
    ports:
      - 4000:4000
      - 25432:5432
      - 13306:13306
    environment:
      <<: *lens2-environment   
    volumes:
      - ./model:/etc/dataos/work/model
```
    

You use the pre-configured template and update a few settings, such as your environment's URL, Lens metadata, and source details.

- **Environment URL:** Suppose you prefer to deploy your Lens in the glad-rattler environment, so you update the `DATAOS_FQDN` attribute with the FQDN (Fully Qualified Domain Name) `glad-rattler.dataos.app` where `glad-rattler` is the name of the context.

```yaml
DATAOS_FQDN: glad-rattler.dataos.app #add the URL for the environment you prefer to use.
```

- **Update Lens meta info, including name, description, tags, and author details:** You update all the general information of your Lens, such as its name and description, to make it useful when other people use your artifacts and to increase its discoverability.  

```yaml
# Overview
LENS2_NAME: product-affinity-cross-sell 
LENS2_DESCRIPTION: "product affinity cross sell is used to.. "
LENS2_TAGS: "lens2, retail, and customer insights" #add tags for better discoverability
LENS2_AUTHORS: ${"author_name"} #add the owner name here
LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
```

- **Customize the source details:** 

Add the environment variables to connect to the data source via Depot.

- **Environment variable for connecting via data source Depot**
    
    ```bash
      # Data Source env variables for connecting to the source via the depot
      LENS2_SOURCE_TYPE: depot
      LENS2_SOURCE_NAME: icebase #add the name of the depot (e.g., icebase)
      DATAOS_RUN_AS_APIKEY: ****** # Add the user API Key for the env
    ```
    
<!-- - **Environment variable to connect via Minerva or Themis Cluster**
    
    ```bash
      # Data Source env variables for connecting to the source via the Minerva cluster
      LENS2_SOURCE_TYPE: minerva #If you want to connect via Themis, change the source type to Themis 
      LENS2_SOURCE_NAME: ${system} #add the cluster name(e.g., system)
      LENS2_SOURCE_CATALOG_NAME: ${icebase} #add the catalog name (e.g., icebase)
      DATAOS_RUN_AS_APIKEY: abcdefgHh==
    ```
     -->

- **Verify Service Configuration:** Ensure that the image tag is up to date or is the same as the one you pulled in the prerequisite stage.

<aside class="callout">
🗣️ The Lens image may change over time; contact the DataOS Administrator for the latest tag.
</aside>

## **Testing Lens in development environment**

After successfully installing all the dependencies for your local environment, you navigate to your Lens project directory. There, you execute the `docker-compose up` command in your terminal to run the `docker-compose.yml` manifest file. Additionally, you ensure that the API key is correctly configured to facilitate a smooth setup.

After running, you receive an output like the one below confirming that the lens you have successfully run the lens locally.

```bash
lens2-api-1  | Loaded  /app/scripts/config.js
lens2-api-1  | 🔥 Table Store (0.35.55-01 ) is assigned to 3030 port.
lens2-api-1  | 🔗 Lens2 SQL Service (PostgreSQL) is listening on 0.0.0.0:5432
lens2-api-1  | 🚀 Lens2 API server (0.35.55-01 ) is listening on 4000
```

## Exploring Lens in development environment

Now that your Lens model runs successfully,  you begin interacting with Lens using SQL, REST, or GraphQL API to thoroughly test Lens before deploying, ensuring all functionalities work as expected.

### **Exploring Lens via SQL API**

To validate your Lens model using the PostgreSQL interface, you start to query Lens tables and views in the PostgreSQL dialect using the **PostgreSQL client (psql)** you utilize this command-line tool for direct interaction with the PostgreSQL database to run queries, manage the database, and perform various administrative tasks.

### **Using PostgreSQL Client (psql)**

To access the Lens, you utilize the following command to enter the username and password and the name of your lens as the database name in the format `lens:${workspace_name}:${lens_name}`.

```bash
psql -h localhost -p 25432 -d lens:curriculum:product360
```

### **Connection details**

<aside class="callout">
🗣️ Always refer to 'ports' within the services section in `docker-compose.yml` for the exposed port.
</aside>

You use the following details to connect to the PostgreSQL interface:

- **Host:** localhost
- **Port:** 25432 (you referred to 'ports' in the services section of your `docker-compose.yml` to look for exposed port)
- **Database:** postgres
- **Username:** You use the following command to get your username:
    
    ```bash
    #Command
    dataos-ctl user get
    
    #Output
        NAME   │    ID    │  TYPE  │      EMAIL       │              TAGS               
    ───────────┼──────────┼────────┼──────────────────┼─────────────────────────────────
      IamGroot │ iamgroot │ person │ iamgroot@tmdc.io │ roles:id:user,                  
               │          │        │                  │ users:id:iamgroot  
    ```
    
- **Password:** dataos-user-apikey (Your defined API key)
    
    You use the following command to get your API key:
    
    ```bash
    dataos-ctl user apikey get
    ```
**Commands to run**

You execute a command to list all the tables in the connected database, run:


```sql
postgres=> \dt
```

**Expected Output:**

```sql
| Schema | Name                             | Type  | Owner    |
|--------|----------------------------------|-------|----------|
| curriculum | purchase                         | table | postgres |
| curriculum | customer                         | table | postgres |
| curriculum | cross_sell_oppurtunity_score     | table | postgres |
| curriculum | product                          | table | postgres |
| curriculum | purchase_frequency               | table | postgres |
| curriculum | total_spend                      | table | postgres |
(6 rows)                                  

```

Here are additional Commands for your reference
    
| Command Description | Command |
| --- | --- |
| Show the schema and details of a specific table | `\d [table_name]` |
| List all databases in the PostgreSQL server | `\l` |
| List all roles and users | `\du` |
| List all schemas in the database | `\dn` |
| List all views in the connected database | `\dv` |
| Exit the PostgreSQL prompt | `\q` |

### **Exploring Lens via REST API**

To explore Lens via the REST API, you interact using tools like C**url** or **Postman**.

Let’s suppose your company has asked you to use Curl, the syntax for the Curl command is as follows:

```bash
curl -X POST 'http://${DATAOS_FQDN}lens2/api/${WORKSPACE_NAME}:${LENS_NAME}/v2/${API_ENDPOINT}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer abcdefghijklmnopqrstuvwxyZ==' \
--data '{
    "query": {
        "dimensions": [
            "${TABLE_NAME}.${DIMENSION_NAME}"
        ],
        "measures": [
            "${TABLE_NAME}.${MEASURE_NAME}"
        ]
    }
}'
```

You open your terminal and try to create a basic `POST` request as follows:

```bash
curl -X POST 'http://splendid-shrew.dataos.app/lens2/api/curriculum:cross-sell-affinity/v2/load' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer abcdefghijklmnopqrstuvwxyZ==' \
--data '{
    "query": {
        "dimensions": [
            "product.product_category"
        ],
        "measures": [
            "product.total_products"
        ],
        "limit": ${10},
    }
}'
```

```bash
#Example_response

{
  "query": {
    "dimensions": ["product.product_category"],
    "measures": ["product.total_products"],
    "limit": 10,
    "timezone": "UTC",
    "filters": [],
    "timeDimensions": [],
    "segments": [],
    "meta": {
      "secured": {
        "segments": [],
        "dimensions": []
      }
    },
    "rowLimit": 10
  },
  "data": [
    {
      "product.product_category": "Meats",
      "product.total_products": 720
    },
    {
      "product.product_category": "Fish",
      "product.total_products": 650
    },
    {
      "product.product_category": "Wines",
      "product.total_products": 446
    },
    {
      "product.product_category": "Sweet Products",
      "product.total_products": 327
    },
    {
      "product.product_category": "Fruits",
      "product.total_products": 97
    }
  ],
  "lastRefreshTime": "2024-11-12T05:57:41.438Z",
  "refreshKeyValues": [
    [
      {
        "refresh_key": "14428258"
      }
    ]
  ]
  ...
  ...
  ....
```

You can achieve the same result in **Postman** by following these steps:

1. **Create a New Request**: Open Postman, click the **New** button in the top left corner, and select **Request** from the drop-down menu.
2. **Configure the Request**: You provide a name for the request and select the recently uploaded collection.
3. **Set the HTTPS Method**: Select **GET** from the dropdown menu next to the URL input field in the request tab.
4. **Enter the Request URL**: You input the full URL WITH THE `load` API endpoint to get the results.
    
    ```bash
    http://localhost:8080/lens2/api/<WORKSPACE_NAME>:<LENS_NAME>/v2/load
    ```
    
    You replace `${lens_name}` with the lens you are testing, say cross-sell-affinity.
    
5. **Set the Authorization Header**: You ensure the following header is included in the **Authorization** section:
    - **Type**: Bearer Token
    - **Token**: `<DATAOS API Key>` (the API key defined in your `docker-compose.yml`).
6. **Send the Request**: After completing the setup, click **Send** to execute the request. Below is the given example request and its response.

    
    ![image.png](/learn/dp_developer_learn_track/create_semantic_model/testing_lens/restsql.png)
    

7. **Review the Response**: Upon receiving the response, you find details about the lens, including its configuration and available tables, confirming the successful interaction with the Lens API.

## Next step

After testing, you can deploy the model to production. This phase involves optimizing the model for performance, ensuring it integrates with existing business systems, and making it accessible to users.


[Deploying Lens on DataOS](/learn/dp_developer_learn_track/create_semantic_model/deploy_lens_on_dataos/)