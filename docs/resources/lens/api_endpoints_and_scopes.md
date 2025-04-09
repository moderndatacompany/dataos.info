# API Endpoints and Scopes

Each REST API endpoint belongs to an API scope, e.g., the `/v2/load` endpoint belongs to the `data` scope. API scopes provide a way to secure access to API endpoints, allowing you to limit accessibility to specific users or roles, or disallow access entirely. By default, API endpoints in all scopes are accessible to everyone, allowing broad access unless specifically restricted. 

You can manage API access using the [user_groups](/resources/lens/user_groups_and_data_policies/). The default user group ensures that API endpoints in all scopes are accessible to everyone. You can create custom user groups by defining roles and associating specific users with these roles in the user_group.yml file. To know more about user groups click [here](/resources/lens/user_groups_and_data_policies/).


The following `api_scopes` are currently supported:
<div style="text-align: center;">
  <table style="margin: 0 auto; border-collapse: collapse; text-align: center;">
    <tr>
      <th><strong>API scope</strong></th>
      <th><strong>REST API endpoints</strong></th>
    </tr>
    <tr>
      <td><a href="/resources/lens/api_endpoints_and_scopes/#meta-scope"><strong>meta</strong></a></td>
      <td><strong>/v2/meta</strong></td>
    </tr>
    <tr>
      <td><a href="/resources/lens/api_endpoints_and_scopes/#load-scope"><strong>data</strong></a></td>
      <td><strong>- /v2/load<br>- /v2/sql</strong></td>
    </tr>
    <tr>
      <td><a href="/resources/lens/api_endpoints_and_scopes/#graphql"><strong>graphql</strong></a></td>
      <td><strong>/v2/graphql</strong></td>
    </tr>
    <!-- <tr>
      <td><a href="/resources/lens/api_endpoints_and_scopes/#source"><strong>source</strong></a></td>
      <td><strong>- /v2/default/schemas/<br>
      - /v2/default/schemas/sandbox/tables<br>
      - /v2/default/schemas/retail/tables/city</strong></td>
    </tr> -->
  </table>
  <figcaption style="margin-top: 10px;">List of API Scopes and their Endpoints</figcaption>
</div>


## Prerequisites

### **Authentication and Authorization**

To securely interact with the Lens APIs, you must authenticate your requests using a DataOS API key and ensure proper user group configurations. This section explains how to generate an API key and configure user groups for accessing the API.

#### **Steps to Generate an API Key:**

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


## meta scope

Provides access to metadata-related endpoints. This scope allows users to view metadata, which typically includes information about sources, authors, timezones, security context, user groups, etc.

### **/v2/meta**
 
Get meta-information such as entitites,measures,dimensions for Lens and views defined in the data model. Information about Lens with `public: false` will not be returned.
 
=== "Syntax"

    ```bash
    http://<DATAOS_FQDN>/lens2/api/<workspace_name>:<data_model_name>/v2/meta
    ```

=== "Example"

    ```bash
    http://liberal-monkey.dataos.app/lens2/api/public:sales_analysis/v2/meta
    ```
  
**Example response:**

```json
{
    "name": 
    "description": [

    ],
    "authors": [
    ],
    "devMode": true,
    "source": {
        "type": "minerva",
        }
           },
    "timeZones": [
        "UTC"
    ],
    "tables": [
        {
            "name": "product_analysis",
            "type": "view",
            "title": "Product Analysis",
           
                    ]
                }
            
```

<aside class="callout">
💡 Providing access to the `<b>meta</b>` API scope grants a user access to the Model and Explore Tab of the Data Product Hub Interface. But to fetch insights using the Explore interface, a user also requires the <b>`data`</b> API scope.
</aside>

## data scope

### **/v2/load**

Executes queries to retrieve data based on the specified dimensions, measures, and filters. When you need to perform data analysis or retrieve specific data from the data model. 

Use `POST` request method along with `/load` endpoint to add or update the data.

You can use either of the following methods:

=== "Method 1"

    === "Syntax"   

        ```bash
        http://<DATAOS_FQDN>/lens2/api/<workspace_name>:<data_model_name>/v2/load?query=<query_parameters>
        ```
    === "Example"

        ```bash
        http://liberal-monkey.dataos.app/lens2/api/public:sales_analysis/v2/load?query={"dimensions":["customer.customer_id","customer.annual_income"],"measures":["customer.total_customers", "customer.average_age"]}
        ```
=== "Method 2"

    === "Syntax"  

        ```bash
        http://<DATAOS_FQDN>/lens2/api/<workspace_name>:<data_model_name>/v2/load
        ```  

    === "Example"
                                                                                    
        ```bash
        http://liberal-monkey.dataos.app/lens2/api/public:sales_analysis/v2/load?query={"dimensions":["customer.customer_id","customer.annual_income"],"measures":["customer.total_customers", "customer.average_age"]}
        ```                                                         

    In the `POST` request body, include the query parameters in the JSON Query Format:

    **Example Query**

    ```bash
    {
        "query": {
            "dimensions": ["customer.customer_id", "customer.annual_income"],
            "measures": ["customer.total_customers", "customer.average_age"],
            "limit": 50
        }
    }
    ```

    **Example response:**

    ```bash
    {
      "query": [
        {
          "name": "Customers",
          "title": "Customers",
          "meta": {
              "someKey": "someValue",
              "nested": {
                "someKey": "someValue"
              }
          },
          "connectedComponent": 1,
          "measures": [
            {
              "name": "customers.count",
              "title": "Customers Count",
              "shortTitle": "Count",
              "aliasName": "customers.count",
              "type": "number",
              "aggType": "count",
              "drillMembers": ["customers.id", "customers.city", "customers.createdAt"]
            }
          ],
          "dimensions": [
            {
              "name": "customers.city",
              "title": "Customers City",
              "type": "string",
              "aliasName": "customers.city",
              "shortTitle": "City",
              "suggestFilterValues": true
            }
          ],
          "segments": []
        }
      ]
    }
    ```

### **/v2/sql**

Alternatively, you can use `/sql` endpoint.

```bash
http://liberal-monkey.dataos.app/lens2/api/public:sales_analysis/v2/sql
```

configure the body with the JSON Query Format similar to `/load`.

## graphql scope

GraphQL scope grants access to `/graphql` endpoint. GraphQL is a query language for APIs that allows clients to request only the data they need. This scope enables users to perform GraphQL queries and mutations. To know more about How to use GraphQL click [here](/resources/lens/exploration_of_lens_using_graphql/)

## Possible Responses

### **Continue wait**

If the request takes too long to be processed, Lens Backend responds with { "error": "Continue wait" } and 200 status code. This is how the long polling mechanism in Lens is implemented. Clients should continuously retry the same query in a loop until they get a successful result. Subsequent calls to the Lens endpoints are idempotent and don't lead to scheduling new database queries if not required by the refresh_key. Also, receiving Continue wait doesn't mean the database query has been canceled, and it's actually still being processed by the Lens. Database queries that weren't started and are no longer waited by the client's long polling loop will be marked as orphaned and removed from the querying queue.

Possible reasons of **Continue wait**:

- The query requested is heavy, and it takes some time for the database to process it. Clients should wait for its completion, continuously sending the same REST API request. continueWaitTimeout can be adjusted in order to change the time Lens waits before returning Continue wait message.
    
- There are many queries requested and Lens backend queues them to save database from overloading.

## Error Handling

Lens REST API has basic errors and HTTP Error codes for all requests.

<div style="display: flex; justify-content: center;">
  <table style="border-collapse: collapse; text-align: center;">
    <tr>
      <th><strong>Status</strong></th>
      <th><strong>Error response</strong></th>
      <th><strong>Description</strong></th>
    </tr>
    <tr>
      <td><strong>400</strong></td>
      <td>Error message</td>
      <td>General error. It may be a database error, timeout, or other issue. Check error message for details.</td>
    </tr>
    <tr>
      <td><strong>403</strong></td>
      <td>Authorization header isn't set</td>
      <td>You didn't provide an auth token. Provide a valid API Token or disable authorization.</td>
    </tr>
    <tr>
      <td><strong>403</strong></td>
      <td>Invalid token</td>
      <td>The auth token provided is not valid. It may be expired or have an invalid signature.</td>
    </tr>
    <tr>
      <td><strong>500</strong></td>
      <td>Error message</td>
      <td>Lens internal server error. Check error message for details.</td>
    </tr>
  </table>
</div>


