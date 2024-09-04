# Consumption of Lens using REST APIs

REST API enables Lens to deliver data over the HTTP protocol. It is is enabled by default and secured using [API scopes](/resources/lens/consumption_usin_rest_apis/#api-endpoints-and-scopes). It consists of a base path and API scopes:

- **Base Path:** All REST API endpoints are prefixed with `/lens2/api`. For example, `/v2/meta` is available at `/lens2/api/<lens_name>/v2/meta`
.

- **API Scopes:** Endpoints are secured by API scopes, restricting access based on user permissions. Follows the principle of least privilege to grant only necessary access.

You can use [Postman](https://www.postman.com/) to interact with Lens via REST APIs. Start by importing the following Postman collection, 
testing each endpoint.

[Lens2-API](/resources/lens/lens_setup/Lens2-APIs.postman_collection.json) 

You can manage API access using the [user_groups](/resources/lens/user_groups/). The default user group ensures that API endpoints in all scopes are accessible to everyone. You can create custom user groups by defining roles and associating specific users with these roles in the user_group.yml file. To know more about user groups click [here](/resources/lens/user_groups/).


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
      <td><a href="/resources/lens/api_endpoints_and_scopes/#load"><strong>data</strong></a></td>
      <td><strong>- /v2/load<br>- /v2/sql</strong></td>
    </tr>
    <tr>
      <td><a href="/resources/lens/api_endpoints_and_scopes/#graphql"><strong>graphql</strong></a></td>
      <td><strong>/v2/graphql</strong></td>
    </tr>
    <tr>
      <td><a href="/resources/lens/api_endpoints_and_scopes/#source"><strong>source</strong></a></td>
      <td><strong>- /v2/default/schemas/<br>
      - /v2/default/schemas/sandbox/tables<br>
      - /v2/default/schemas/retail/tables/city</strong></td>
    </tr>
  </table>
  <figcaption style="margin-top: 10px;">List of API Scopes and their Endpoints</figcaption>
</div>


## Prerequisites

### **Authentication**

Lens uses API tokens to authorize requests and also for passing additional security context.

The API Token is passed via the Authorization Header. The token itself is a `dataos-user-apikey`.

**Ensure the following header is passed in Authorization when running the APIs-**
    
```bash
Type: Bearer Token
Token: ${Your DataOS API Key} #Use the API key of the env defined in docker-compose.yml
```
Replace the placeholder with the DataOS API Key.

## meta scope

Provides access to metadata-related endpoints. This scope allows users to view metadata, which typically includes information about sources, authors, timezones, security context, user groups, etc.

<h3><strong><code>\v2\meta</code> endpoint</strong></h3>

Get meta-information for lens and views defined in the data model. Information about lens and lens with "**public: false**" will not be returned.

=== "Syntax"

    ```bash
    http://<host_name>:<port_name>/lens2/api/<data_model_name>/v2/meta
    ```

=== "Example"

    ```bash
    http://localhost:4000/lens2/api/sales_analysis/v2/meta
    ```
  
**Example response:**

```json
{{
    "name": 
    "description": [],
    "authors": [],
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
💡 Providing access to the `<b>meta</b>` API scope grants a user access to the Model and Explore Tab of the Lens Studio Interface. But to fetch insights using the Explore interface, a user also requires the <b>`data`</b> API scope.
</aside>

## data scope

<h3><strong><code>/v2/load</code> endpoint</strong></h3>

Executes queries to retrieve data based on the specified dimensions, measures, and filters. When you need to perform data analysis or retrieve specific data from the data model. 

Use `POST` request method along with `/load` endpoint to add or update the data.

You can use either of the following methods:

=== "Syntax"   

    ```bash
    http://<host_name>:<port_name>/lens2/api/<data_model_name>/v2/load?query=<query_parameters>
    ```
=== "Example"

    ```bash
    http://localhost:4000/lens2/api/sales_analysis/v2/load?query={"dimensions":["customer.customer_id","customer.annual_income"],"measures":["customer.total_customers", "customer.average_age"]}
    ```

=== "Syntax"  

    ```bash
    http://<host_name>:<port_name>/lens2/api/<data_model_name>/v2/load
    ```  

=== "Example"
                                                                                
    ```bash
    http://localhost:4000/lens2/api/sales_analysis/v2/load?query={"dimensions":["customer.customer_id","customer.annual_income"],"measures":["customer.total_customers", "customer.average_age"]}
    ```                                                         

In the POST request body, include the query parameters in the JSON Query Format:

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

<h3><strong><code>/v2/sql</code> endpoint</strong></h3>

Alternatively, you can use `/sql` endpoint.

```bash
http://localhost:4000/lens2/api/sales_analysis/v2/sql
```

configure the body with the JSON Query Format similar to `/load`.

## graphql

Grants access to GraphQL endpoints. GraphQL is a query language for APIs that allows clients to request only the data they need. This scope enables users to perform GraphQL queries and mutations.

## source scope

Grants access to source-related endpoints. 

<div style="display: flex; justify-content: center;">
  <table style="border-collapse: collapse; text-align: center;">
    <tr>
      <th><strong>`Parameter`</strong></th>
      <th><strong>Description</strong></th>
      <th><strong>Action</strong></th>
    </tr>
    <tr>
      <td><strong>`schemas`</strong></td>
      <td>An array of schema names in the data source.</td>
      <td><strong>GET</strong></td>
    </tr>
    <tr>
      <td><strong>`tables`</strong></td>
      <td>An array of schemas and table names in the data source.</td>
      <td><strong>GET</strong></td>
    </tr>
    <tr>
      <td><strong>`describe-table`</strong></td>
      <td>Describes the given source table.</td>
      <td><strong>GET</strong></td>
    </tr>
    <tr>
      <td><strong>`load-source`</strong></td>
      <td>Loads all datasets of the source.</td>
      <td><strong>POST</strong></td>
    </tr>

  </table>
</div>

<h3><strong><code>/v2/default/schemas</code> endpoint</strong></h3>


This endpoint retrieves all the schemas available within the source depot. For example if source is icebase it will get the list of all the schemas present in icebase depot.

**Example Request**

```http
GET http://localhost:4000/lens2/api/v2/default/schemas
```

**Example Response**

<h3><strong><code>/v2/default/schemas/&lt;collection_name&gt;/tables</code> endpoint</strong></h3>


This endpoint fetches all tables within a specified schema (collection).

**Example Requests**

**Example Response**
 
<h3><strong><code>/v2/default/schemas/&lt;collection_name&gt;/tables/&lt;table_name&gt;</code> endpoint</strong></h3>

This endpoint retrieves detailed information about a specific table within a schema.

**Example Requests**

```http
GET http://localhost:4000/lens2/api/v2/default/schemas/sales360/tables/customers
```

**Example Response**

<h3><strong><code>/v2/default/load-source?responseType=default</code> endpoint</strong></h3>

This endpoint is used to load data from a specified source into Lens 2.0. The responseType parameter defines the type of response expected. In this case, it’s set to default.

## Possible Responses

**Continue wait**

If the request takes too long to be processed, Lens Backend responds with { "error": "Continue wait" } and 200 status code. This is how the long polling mechanism in Lens is implemented. Clients should continuously retry the same query in a loop until they get a successful result. Subsequent calls to the Lens endpoints are idempotent and don't lead to scheduling new database queries if not required by the refresh_key. Also, receiving Continue wait doesn't mean the database query has been canceled, and it's actually still being processed by the Lens. Database queries that weren't started and are no longer waited by the client's long polling loop will be marked as orphaned and removed from the querying queue.

Possible reasons of **Continue wait**:

- The query requested is heavy, and it takes some time for the database to process it. Clients should wait for its completion, continuously sending the same REST API request. continueWaitTimeout can be adjusted in order to change the time Lens waits before returning Continue wait message.
    
- There are many queries requested and Lens backend queues them to save database from overloading.

### **Error Handling**

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


