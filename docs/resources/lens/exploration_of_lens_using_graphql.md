# Exploration of Lens using GraphQL

<aside class="callout">
💡 For a more streamlined and interactive experience with GraphQL, use the GraphQL playground on Data Product Hub. This interface simplifies interactions and eliminates the need to manually work with tools like curl.
<a href= "/interfaces/data_product_hub/activation/app_development/">Access the GraphQL guide here</a>
</aside>

This guide provides comprehensive instructions for accessing and interacting with the Lens GraphQL API. You can interact with the Lens GraphQL API using:

1. [**Explorer Studio in Data Product Hub**](#using-explorer-studio-in-data-product-hub): An interactive in-browser tool for writing and executing GraphQL queries.
2. [**Curl**](#using-curl): A command-line tool for transferring data with URLs, useful for automated scripts.
3. [**Python**](#using-python): Use Python's `requests` library for more complex interactions with the API.
4. [**Postman**](#using-postman): Use Postman API platform to start using and testing REST APIs.

## Authentication and Authorization

To securely interact with the Lens GraphQL API, you must authenticate your requests using a **DataOS API key** and ensure proper user group configurations. This section explains how to generate an API key and configure user groups for accessing the API.

### **Generating a DataOS API Key**

To authenticate API requests, you need a DataOS API key. This key validates your identity and ensures only authorized users can access and query the data.

**Steps to Generate an API Key:**

1. Open your terminal and run the following command to create a new API key:
    ```bash
    dataos-ctl user apikey create
    ```
2. To view existing API keys, use:
    ```bash
    dataos-ctl user apikey get
    ```
3. Note down your API key and keep it secure. You will use this key to authenticate your API requests.

API key tokens can also be fetched from the DataOS GUI, for more details refer to the [documentation here](/interfaces/#create-tokens).

### **Configuring User Groups**

To access and query data via the GraphQL endpoint, users must be part of a user group with the required permissions. The necessary permissions are defined using the `api_scopes` attribute within the user group configuration located in the Lens directory.

**Example User Group Configuration**

The following YAML configuration demonstrates how to set up user groups with different levels of access:

```yaml
user_groups:
  # User group with full access to GraphQL API and data querying capabilities
  - name: engineer
    description: Data Analyst
    api_scopes:
      - meta      # For accessing metadata
      - graphql   # For accessing the GraphQL API
      - data      # For querying the data
    includes:
      - users:id:exampleuser

  # User group with access to GraphQL API but no data querying capabilities
  - name: analyst
    description: Data Engineer
    api_scopes:
      - meta
      - graphql
    includes:
      - users:id:testuser

  # User group without access to GraphQL API or data querying capabilities
  - name: testuser
    description: Data Engineer
    api_scopes:
      - meta
    includes:
      - users:id:testuser
```

**Explanation of the Configuration:**

- **`engineer` Group:** This group can access the GraphQL API and query data because it includes both the `graphql` and `data` `api_scopes`. 
- **`analyst` Group:** This group can access the GraphQL API but cannot query the data because the `data` scope is missing. 
- **`testuser` Group:** This group cannot access the GraphQL API or query data because both the `graphql` and `data` scopes are missing. 

!!!note
    The user groups configured above only manage access permissions at the consumption level within DataOS. However, source-level permissions defined by the source administrator (e.g., in Snowflake or BigQuery) remain applicable. For sources accessible through the DataOS Query Engine (Minerva/Themis), you can define source-level permissions using the [Bifrost](/interfaces/bifrost/) application in the DataOS GUI or using the [Policy](/resources/policy/) and [Grant](/resources/grant/) Resource using DataOS CLI.

## How to access the GraphQL API?

### **Using Explorer Studio in Data Product Hub**

The Explorer Studio of Data Product Hub provides an intuitive, in-browser interface to interact with the GraphQL API.

1. **Open Metis:** Go to the Metis application on the DataOS GUI and navigate to the Resource section here click on Lens choose the desired deployed Lens model.

    <div style="text-align: center;">
        <img src="/resources/lens/consumption_of_deployed_lens/graphql/graphql1.png" alt="graphql" style="max-width: 80%; height: auto; border: 1px solid #000;">
    </div>
    <figcaption><i><center>Deployed Lens Resource on Metis UI</center></i></figcaption>

2. **Access GraphQL Tab:** Click on the ‘Explore in Studio’ button, the Studio will appear from here navigate to the GraphQL tab.

    <div style="text-align: center;">
        <img src="/resources/lens/consumption_of_deployed_lens/graphql/graphql2.png" alt="graphql" style="max-width: 80%; height: auto; border: 1px solid #000;">
    </div>
    <figcaption><i><center>Lens Details Page and Explore in Studio Button</center></i></figcaption>

3. **Compose a Query:** Enter your GraphQL query in the left pane.  

    <div style="text-align: center;">
        <img src="/resources/lens/consumption_of_deployed_lens/graphql/graphql3.png" alt="graphql" style="max-width: 80%; height: auto; border: 1px solid #000;">
    </div>
    <figcaption><i><center>GraphQL Tab on Explorer Studio in Data Product Hub</center></i></figcaption>

      You can press `Ctrl + Space` to bring up the autocomplete window. For example:

      ```graphql
      query LensQuery {
          table {
            wallet_sales_view {
            revenue
          }
          }
        }
      ```

4. **Execute the Query:** Click the 'Execute' button or press `Ctrl + Enter` to run the query. The results will appear in the right pane.

    ```graphql
    {
        "data": {
            "table": [
                {
                    "wallet_sales_view": {
                        "revenue": 77835071
                    }
                }
            ]
        }
    }
    ```

### **Using Curl**

Curl is a command-line tool used for transferring data with URLs, making it a convenient choice for interacting with APIs directly from the terminal. Ensure that `curl` is installed on your system before proceeding.

1. **Prepare the Request:** To send a GraphQL query using Curl, construct your request with the following template:

    ```bash
    curl -X POST <URL> \
    -H "Content-Type: application/json" \
    -H "apikey: <DATAOS_API_KEY>" \
    -d '{"query": "<GRAPHQL_QUERY>"}'
    ```

    - **Replace `<URL>` with the appropriate endpoint based on your environment:**
        For a deployed Lens model, use:
        
            ```html
            https://<DATAOS_FQDN>/lens2/api/<WORKSPACE>:<NAME_OF_LENS>/v2/graphql
            ```

    - **Replace `<DATAOS_API_KEY>` with your actual DataOS API key.** Refer to the [Generating an API Key](#generating-an-api-key) section for more information on obtaining an API key.

    - **Replace `<DATAOS_FQDN>` with the fully qualified domain name of your DataOS instance.** For example: `alpha-omega.dataos.app` or `happy-kangaroo.dataos.app`.

    - **Replace `<WORKSPACE>` with the DataOS Workspace name** where the Lens is deployed.

    - **Replace `<NAME_OF_LENS>` with the name of your deployed Lens model.** This corresponds to the specific Lens model you want to query.

    - **Replace `<GRAPHQL_QUERY>` with your GraphQL query.** Make sure to format the query as a valid JSON string.

    **Sample Request:**

    ```bash
    curl -X POST https://alpha-omega.dataos.app/lens2/api/public:lakehouse-insights01/v2/graphql \
    -H "Content-Type: application/json" \
    -H "apikey: abcdefghijklmnopqrstuvwxyz" \
    -d '{"query": "query LensQuery { table { total_operations { lakehouse_insights_total_data_size_in_gb lakehouse_insights_table_name } } }"}'
    ```

2. **Execute the Command:** Run the command in your terminal to execute the query and view the response.

> Ensure you replace the placeholders with the actual values specific to your environment. Properly formatted queries and valid API keys are essential for successful API interactions.

### **Using Python**

Python provides a flexible and powerful way to interact with the Lens GraphQL API. It is especially useful for building automation scripts or for use in data analysis workflows. Ensure that Python and the `requests` library are installed on your system before proceeding.

1. **Install the `requests` Library:**

    If you haven’t already installed the `requests` library, you can do so by running the following command:

    ```bash
    pip install requests
    ```

2. **Prepare the Python script:**

    Use the following template to create a Python script for querying the Lens GraphQL API:

    ```python
    import requests

    # Define the URL of the Lens GraphQL endpoint
    url = "<URL>"

    # Define the headers including the API key
    headers = {
        "Content-Type": "application/json",
        "apikey": "<DATAOS_API_KEY>"
    }

    # Define your GraphQL query
    query = """
    <GRAPHQL_QUERY>
    """

    # Send the POST request
    response = requests.post(url, headers=headers, json={'query': query})

    # Print the response
    print(response.json())
    ```

    - **Replace `<URL>` with the appropriate endpoint based on your environment:**
        For a deployed Lens model, use:

        ```plaintext
        https://<DATAOS_FQDN>/lens2/api/<WORKSPACE>:<NAME_OF_LENS>/v2/graphql
        ```

    - **Replace `<DATAOS_API_KEY>` with your actual DataOS API key.** Refer to the [Generating an API Key](#generating-an-api-key) section for more information on obtaining an API key.

    - **Replace `<DATAOS_FQDN>` with the fully qualified domain name of your DataOS instance.** For example: `alpha-omega.dataos.app` or `happy-kangaroo.dataos.app`.

    - **Replace `<WORKSPACE>` with the workspace name associated with your Lens model.** This is typically the name of the DataOS Workspace where the Lens is deployed. For example: `public`, `sandbox`, etc.

    - **Replace `<NAME_OF_LENS>` with the name of your deployed Lens model.** This corresponds to the specific Lens model you want to query.

    - **Replace `<GRAPHQL_QUERY>` with the specific fields you want to query from your GraphQL schema.** Make sure to format the query string as valid JSON.

    **Sample script:**

    ```python
    import requests

    # Define the URL of the Lens GraphQL endpoint
    url = "https://alpha-omega.dataos.app/lens2/api/public:lakehouse-insights01/v2/graphql"

    # Define the headers including the API key
    headers = {
        "Content-Type": "application/json",
        "apikey": "abcdefghijklmnopqrstuvwxyz"
    }

    # Define your GraphQL query
    query = """
      query LensQuery {
        table {
          total_operations {
            lakehouse_insights_total_data_size_in_gb
            lakehouse_insights_table_name
          }
        }
      }
    """

    # Send the POST request
    response = requests.post(url, headers=headers, json={'query': query})

    # Print the response
    print(response.json())
    ```

    In the above sample:
    - `<URL>` is `https://alpha-omega.dataos.app/lens2/api/public:lakehouse-insights01/v2/graphql`
    - `<DATAOS_API_KEY>` is `abcdefghijklmnopqrstuvwxyz` (replace with your actual API key)
    - `<WORKSPACE>` is `public`
    - `<NAME_OF_LENS>` is `lakehouse-insights01`
    - The query fetches `lakehouse_insights_total_data_size_in_gb` and `lakehouse_insights_table_name` fields from the `total_operations` table.

3. **Run the script:**

    Save the script as a `.py` file and execute it using the following command in your terminal:

    ```bash
    python <your_script_name>.py
    ```

    This will send the GraphQL query to the Lens API and print the response to your terminal.

> **Note:** Ensure you replace the placeholders with the actual values specific to your environment. Properly formatted queries and valid API keys are essential for successful API interactions.

### **Using Postman**

When working with a Postman collection to test APIs, you typically need to configure authorization, set request methods, and provide the request body. Below are the steps to get started:

1. **Open Postman and import the Postman collection:**

    - Open Postman and click on the **Import** button located at the top-left corner.
    - Import the Postman Collection file you’ve been given. For example, if you import the Lens API collection from the provided link, you will see a collection of API requests neatly organized into folders. Refer to the below image for subsequent steps.

        <div style="text-align: center;">
        <img src="/resources/lens/exploring_deployed_lens_using_rest_apis/Untitled1.png" alt="postman" style="max-width: 40rem; height: auto; border: 1px solid #000;">
        </div>
        <figcaption><i><center>Postman</center></i></figcaption>

2. **Set up Authorization (bearer token):**

    - Once the collection is imported, click on the specific API request you want to test.
    - Go to the **Authorization** tab.
    - From the **Auth Type** dropdown, select **Bearer Token**.
    - In the Token field, paste your Bearer token, which you have received from your authentication process.
    - This token grants you access to the meta and data scopes.

3. **Set the Request type:**

    - Select the API request type as `POST` from the dropdown next to the API URL.

4. **Prepare the URL and Query the API:**

    - Prepare the URL according to what data you want to fetch.

    ```bash
    http://<URL>/lens2/api/<WORKSPACE_NAME>:<LENS_NAME>/v2/<ENDPOINT>
    ```

     - **Replace `<URL>` with the appropriate environment Lens is deployed in:**

          ```plaintext
          https://<DATAOS_FQDN>/lens2/api/<WORKSPACE>:<NAME_OF_LENS>/v2/graphql
          ```

    - **Replace `<DATAOS_API_KEY>` with your actual DataOS API key.** Refer to the [Generating an API Key](#generating-an-api-key) section for more information on obtaining an API key.

    - **Replace `<DATAOS_FQDN>` with the fully qualified domain name of your DataOS instance.** For example: `alpha-omega.dataos.app` or `happy-kangaroo.dataos.app`.

    - **Replace `<WORKSPACE>` with the workspace name associated with your Lens model.** This is typically the name of the DataOS Workspace where the Lens is deployed. For example: `public`, `sandbox`, etc.

    - **Replace `<NAME_OF_LENS>` with the name of your deployed Lens model.** This corresponds to the specific Lens model you want to query. For e.g. `sales360`.

    - **Replace `<QUERY>` with the specific fields you want to query from schema.** Make sure to format the query string as valid JSON.

5. **Set the Request Body in Postman (for POST Methods):**

    - for `POST` requests, you will need to configure the Body tab for graphql. Refer to the below image for subsequent steps.

        <div style="text-align: center;">
        <img src="/resources/lens/exploring_deployed_lens_using_rest_apis/graphql.png" alt="graphql" style="max-width: 80%; height: auto; border: 1px solid #000;">
        </div>
        <figcaption><i><center>Postman GraphQL request body tab</center></i></figcaption>

        - In the `Body` tab, select `GraphQL` from the format options.
        - Enter the GraphQL query in the provided field in the following format.

        ```graphql
        query LensQuery {
          table(limit: 10, offset: 0) {
            <TABLENAME> {
              <DIMENSION>
              <MEASURE_1>
              <MEAUSRE_2>
            }
          }
        }
        ```

        - Replace table name and choose requried dimensions and measures. 

        - **For Example:** If you want to  compare the average price and average margin of two major categories: Apparel and Footwear for the `products` table. The  request body will be:

            === "Query"

                ```graphql
                query LensQuery {
                  table(limit: 10, offset: 0) {
                    products {
                      productcategory
                      average_price
                      average_margin
                    }
                  }
                }
                ```
            === "Response"

                ```
                {
                  "data": {
                    "table": [
                      {
                        "products": {
                          "productcategory": "Apparel",
                          "average_price": 84.94859281437131,
                          "average_margin": 50.872714570858385
                        }
                      },
                      {
                        "products": {
                          "productcategory": "Footwear",
                          "average_price": 83.98569138276541,
                          "average_margin": 49.84462925851698
                        }
                      }
                    ]
                  }
                }
                ```

## GraphQL Query Examples

This section provides sample GraphQL queries that you can use directly in Explorer Studio of the Data Product Hub. You can also use these queries with the <GRAPHQL_QUERY> placeholder in the Curl and Python methods described earlier.

<aside class="callout">
Compared to the <a href="/resources/lens/exploration_of_lens_using_rest_apis/">REST API</a>, GraphQL API currently has no support for referencing <a href="/resources/lens/segments/">segments</a> in queries.
</aside>

### **Querying a dimension**

A GraphQL query to retrieve the `city` dimension associated with an `account` table might look something like this:

=== "Query"

    ```graphql
    query LensQuery {
        table {
        account {
          city
        }
        }
      }
    ```

=== "Expected Output"

    ```json
    {
    "data": {
    "table": [
    {
      "account": {
        "city": "Austin"
      }
    },
    {
      "account": {
        "city": "Baltimore"
      }
    },
    {
      "account": {
        "city": "Baton Rouge"
      }
    },
    {
      "account": {
        "city": "Chicago"
      }
      ...
    }
    ]
    }
    }
    ```
    

### **Querying Measure and Dimension**

A GraphQL query to retrieve the `city` and the `total_accounts` associated with each entry within the `account` table is given below:

=== "Query"

    ```graphql
    query LensQuery {
        table {
        account {
          city
          total_accounts
        }
        }
      }
    ```

=== "Expected Output"
    
    ```json
    {
      "data": {
        "table": [
          {
            "account": {
              "city": "Los Angeles",
              "total_accounts": 59
            }
          }
          ...
          {
            "account": {
              "city": "Columbus",
              "total_accounts": 1
            }
          }
        ]
      }
    }
    ```
    

### **Modifying time dimension granularity**

The granularity for a time dimension can easily be changed by specifying it in the query:

```graphql
query LensQuery {
  table {
    sales {
      invoice_date {
        month
      }
    }
  }
}
```

Any supported granularity can be used. If you prefer to not specify a granularity, then use `value`:

```graphql
query LensQuery {
  table {
    sales {
      invoice_date {
        value
      }
    }
  }
}
```

### **Specifying filters**

Filters can be set on the load query or on a specific table. Specifying the filter on the load query applies it to all tables in the query. Filters can be added to the query as follows:

=== "Query"

    ```graphql
    query LensQuery {
        table{
        account(
          where: { premise_code: { equals: "OFF" } }
        ) {
          total_accounts
          city
          premise_code
        }
      }
    }
    ```

=== "Expected output"
    
    ```json
    {
      "data": {
        "table": [
          {
            "account": {
              "total_accounts": 25,
              "city": "Los Angeles",
              "premise_code": "OFF"
            }
          },
          {
            "account": {
              "total_accounts": 11,
              "city": "Kansas City",
              "premise_code": "OFF"
            }
          }
        ]
      }
    }
    ```
    

### **Specifying order by condition and limiting the result**

A GraphQL query that specifies an order by condition and limits the number of results returned would look like this:

=== "Query"

    ```graphql
    query LensQuery {
        table(limit: 10) {
        account(
          orderBy: { total_accounts: desc}
        ) {
          total_accounts
          city
          premise_code
        }
      }
    }
    ```

=== "Expected Output"
    
    ```json
    {
      "data": {
        "table": [
          {
            "account": {
              "total_accounts": 27,
              "city": "Los Angeles",
              "premise_code": "ON"
            }
          },
          {
            "account": {
              "total_accounts": 25,
              "city": "Los Angeles",
              "premise_code": "OFF"
            }
          },
          {
            "account": {
              "total_accounts": 9,
              "city": "Chicago",
              "premise_code": "OFF"
            }
          },
          {
            "account": {
              "total_accounts": 7,
              "city": "Los Angeles",
              "premise_code": "BOTH"
            }
          },
          {
            "account": {
              "total_accounts": 5,
              "city": "Houston",
              "premise_code": "OFF"
            }
          },
          {
            "account": {
              "total_accounts": 5,
              "city": "New York",
              "premise_code": "OFF"
            }
          },
          {
            "account": {
              "total_accounts": 5,
              "city": "San Francisco",
              "premise_code": "OFF"
            }
          },
          {
            "account": {
              "total_accounts": 4,
              "city": "Greenville",
              "premise_code": "ON"
            }
          },

        ]
      }
    }
    ```
    

### **Querying multiple tables**

Using the same `account` table as before, let’s try and get the revenue for each. We can do this by adding the `sales` table to our query as follows:

=== "Query"

    ```graphql
    query LensQuery {
        table{
        account{
          total_accounts
          city
          premise_code
        }
        sales{
          revenue
        }
      }
    }
    ```

=== "Expected Output"
    
    ```json
    {
      "data": {
        "table": [
          {
            "account": {
              "total_accounts": 26,
              "city": "Los Angeles",
              "premise_code": "ON"
            },
            "sales": {
              "revenue": 3911966
            }
          },
          {
            "account": {
              "total_accounts": 25,
              "city": "Los Angeles",
              "premise_code": "OFF"
            },
            "sales": {
              "revenue": 10562513
            }
          },
          {
            "account": {
              "total_accounts": 7,
              "city": "New York",
              "premise_code": "BOTH"
            },
            "sales": {
              "revenue": 937897
            }
          },
          {
            "account": {
              "total_accounts": 5,
              "city": "Chicago",
              "premise_code": "OFF"
            },
            "sales": {
              "revenue": 3206423
            }
          }
        ]
      }
    }
    ```



<aside class="callout">
To explore more examples click <a href="/resources/lens/graphql_api/graphql_query_example/">here</a>.
</aside>
