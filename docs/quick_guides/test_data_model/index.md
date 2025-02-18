# Testing Data Model Locally

!!! info "Information"
    This guide offers a step-by-step approach to validating your SQL queries within the data model, enabling you to test them directly on your local machine. Testing your Lens model locally is a best practice, ensuring that the resulting tables and joins function as intended before deploying them in a production environment on DataOS.

## Key Steps

Follow the below steps:

<center>
<div style="text-align: center;">
<img src="/quick_guides/test_data_model/3_test_data_model.png" alt="Steps to test a data model" style="border: 1px solid black;">
</div>
</center>

<!-- ![3_test_data_model.png](/quick_guides/test_data_model/3_test_data_model.png) -->

## Pre-requisites

Before you begin, ensure the following tools are installed on your system:

1. **Docker**: Runs Lens 2.0 in an isolated environment.
2. **Docker-compose**: Configures multi-container Docker applications.
3. **Postman App** / **Postman VS Code Extension**: For querying and testing Lens.
4. **VS Code Plugin (Optional)**: Assists in creating Lens views and tables.

<!-- For installation instructions, refer to the [detailed guide here](https://www.notion.so/Installing-Pre-requisites-for-Lens2-0-Local-Dev-78c46ee164354c09955b5d817b82676b?pvs=21). -->

**Additionally, ensure your Lens project is set up with the required SQL and YAML files.** 

Refer to the [Quick Guide: Creating Data Model (Lens)](/quick_guides/create_data_model/) for more details.

---

## Step 1: Configuring  `docker-compose.yml` File

When you download the Lens Project Template, it includes `docker-compose.yml` and the necessary folder hierarchy. This file is essential for testing your Lens setup locally.

This template is pre-configured with most of the necessary settings, so you only need to update a few fields to suit your specific needs.

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
NODE_ENV: production

services:
  api:
    restart: always
    image: rubiklabs/lens2:0.35.18-50
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

Modify the `docker-compose.yml` file to include your environment's URL, Lens metadata, and source details, ensuring the setup is tailored to your specific needs.

1. **Environment URL:**
    
    ```yaml
    DATAOS_FQDN: your-env-url.dataos.app
    ```
    
2. **Lens Meta Info:**
    
    ```yaml
    LENS2_NAME: your_lens_name
    LENS2_DESCRIPTION: "Lens description"
    LENS2_TAGS: "tags for discoverability"
    LENS2_AUTHORS: "author_name"
    ```
    
3. **Source Details:** Add the environment variables for connecting to the data source.
    
    **Environment variable for connecting via Depot**
    
    ```yaml
      # Data Source
      # This defines env variables for connecting to the source via the depot
      LENS2_SOURCE_TYPE: depot
      LENS2_SOURCE_NAME: depot_name #add the name of the depot 
      DATAOS_RUN_AS_APIKEY: ****** # Add the user API Key for the env
    ```
    
    **Environment variable to connect via Minerva or Themis**
    
    ```yaml
      # Data Source
      # This defines env variables for connecting to the source via the Minerva cluster
      LENS2_SOURCE_TYPE: minerva #If you want to connect via Themis, change the source type to Themis 
      LENS2_SOURCE_NAME: cluster_name #add the cluster name
      LENS2_SOURCE_CATALOG_NAME: catalog_name #add the catalog name
      DATAOS_RUN_AS_APIKEY: ******
    ```  
    <!--     
    🗣 If connecting without a Depot, refer to the [environmental variables guide](https://www.notion.so/Supported-Sources-5d0da3eaf1b14eca82e4d7d1aafe6b86?pvs=21) for different sources, as each may require a specific set of settings.
     -->    
4. **Verify Service Configuration:**

    - Ensure that the image tag is up to date or is the same as the one you pulled in the prerequisite stage.

## Step 2: Starting Your Lens Locally

After completing the Lens setup and defining the Lens model, start Lens locally:

<aside class="callout">
🗣 Ensure your working directory is the Lens project directory.
</aside>

You can start Lens locally by running the following command in your terminal.

```bash
docker-compose up  #run docker-compose up command in terminal
```

**Output**

You should see an output similar to this, indicating the Lens server has started locally:

```bash
lens2-api-1  | Loaded  /app/scripts/config.js
lens2-api-1  | 🔥 Table Store (0.35.40) is assigned to 3030 port.
lens2-api-1  | 🔗 Lens2 SQL Service (PostgreSQL) is listening on 0.0.0.0:5432
lens2-api-1  | 🚀 Lens2 API server (0.35.41-05) is listening on 4000
```

Now that your Lens is up and running on your local machine, it's time to test the creation of tables and ensure the joins are functioning correctly.

## Step 3: Testing Your Lens Model

To ensure your Lens model functions as expected, start by running a series of validation tests. Begin with basic checks to verify that all SQL queries are correctly defined and executed. Next, review the results to confirm that your model accurately reflects the intended logic and performance requirements.

### **Validating Lens Model Using PostgreSQL Interface**

Lens exposes a PostgreSQL interface that allows you to query Lens Tables and Views in PostgreSQL dialect.

1. Now use PostgreSQL API to interact with your Lens. Make sure your queries align with the PostgreSQL dialect. Use the following connection details to interact with your Lens:
    
    ```yaml
    host - localhost
    port - 25432 # Always refer to 'ports' within the services section in docker-compose.yml for the exposed port 
    usernames- {dataos-username}
    password - {dataos-apikey} // use the API key of env you have defined in the docker-compose.yml
    database_name = db
    ```
    
2. **Connection Options:**
    - **PostgreSQL Client (psql)**: Execute queries from the command line.
    - **VS Code Extension (PostgreSQL Client)**: Connect and query Lens directly in VS Code.
    
    ![postgre_connection.png](/quick_guides/test_data_model/postgre_connection.png)
    
    Once the connection is a success you can start executing the queries in the terminal. This is to ensure that all the SQLs are correctly written and the resulting tables and joins are accurate.
    
    ```sql
    postgres=> \d
                    List of relations
    Schema |         Name         | Type  |  Owner   
    --------+----------------------+-------+----------
    public | customer             | table | postgres
    public | product_analysis     | table | postgres
    public | products             | table | postgres
    public | transaction_analysis | table | postgres
    public | transactions         | table | postgres
    (5 rows)
    ```
    
    You can see the tables and business views defined in your data model listed here in the output.
    
    To verify, run a query to check the output data.
    
    ```yaml
    postgres=> select customer_id, first_name, gender from customer limit 5; 
    customer_id | first_name | gender 
    -------------+------------+--------
    10111       | Clemente   | MALE
    10112       | Werner     | MALE
    10113       | Dominic    | MALE
    10114       | Kaleigh    | FEMALE
    10115       | Nenita     | OTHER
    (5 rows)
    ```
    

### **Validating Lens Model Using Postman**

Postman is a tool that allows you to query and test the Lens environment by sending API requests through an intuitive interface. It allows you to execute a query using JSON Payload.

Follow the [Postman Installation Guide](https://learning.postman.com/docs/getting-started/installation/installation-and-updates/) to install Postman on your local system.

**Verifying Installation**

To ensure that Postman is installed correctly and ready for use:

1. **Open Postman**:
    - Launch the application. You should see the main interface where you can create requests and organize them in collections.
        
        
2. **Create a Simple Request** (optional):
    - To test if Postman is functioning correctly, try sending a simple GET request to a public API endpoint like `https://api.publicapis.org/entries`. This action should return a list of public APIs as a response, indicating that Postman is set up properly.

<aside class="callout">
🗣 Alternatively, you can also use the Postman VS Code extension. This allows you to perform similar tasks within VS Code.

</aside>

**Using Postman in VS Code**

1. Install Postman VS Code Extension.
    
    Search for "Postman" in the VS Code Extensions Marketplace and install the Postman extension.
    
    ![postman_vscode_ext.png](/quick_guides/test_data_model/postman_vscode_ext.png)
    
2. Open the extension within VS Code to start creating and sending requests directly from the editor.
3. Upload Lens API Collection.
    
    To use **Lens API** endpoints, upload the **Lens2-APIs.postman_collection.json** file.
    
    [Lens2-APIs.postman_collection.json](/quick_guides/test_data_model/Lens2-apis.postman_collection.json)
    
4. Start a New HTTP Request. 
    
    In the Postman extension view, click on the "New HTTP Request" button.
    
    ![lens_postman.png](/quick_guides/test_data_model/lens_postman.png)
    
5. Fetch metadata and data.
    
    Provide the following information:
    
    - **Authorization**: Use your DataOS API key.
    - **Lens Name**: Include the Lens name in the URL.
6. Click on the **Send** button.
    
    In this example, we successfully fetched the metadata of the Lens model. A "200 OK" status confirms that the metadata retrieval was successful.
    
    ![postman_testing_get_metadata.png](/quick_guides/test_data_model/postman_testing_get_metadata.png)
    
    Next, let's retrieve data from the Lens model. In the request body, paste the following query.
    
    ```json
    {
        "query": {
            "measures": [
                "customer.total_customers"
            ],
            "dimensions": [
                "customer.customer_id"
            ],
            "segments": [],
            "limit": 1,
            "responseFormat": "compact"
        }
    }
    ```
    
    Since the Lens model is functioning correctly, we received the desired output with a success status.
    
    ![lens_testing_postman.png](/quick_guides/test_data_model/lens_testing_postman.png)

    ## Next Steps

    [Deploying Your Data Model on DataOS](/quick_guides/deploy_data_model/)