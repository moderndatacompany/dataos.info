
# API Endpoints and Scopes

> **Each REST API endpoint belongs to an API scope**
> 

## Prerequisites

### **Authentication**

Lens uses API tokens to authorize requests and also for passing additional security context.The API Token is passed via the Authorization Header. The token itself is a `dataos-user-apikey`.
In the development environment, the token is not required for authorization, but
you can still use it to pass a security context.

The following `api_scopes` are currently supported:

| **API scope** | **REST API endpoints** |
| --- | --- |
| [**`meta`**](https://www.notion.so/API-Endpoints-and-their-scopes-a41a79334ce244979b1aeae72fc651a7?pvs=21) | **`/v2/meta`** |
| [**`data`**](https://www.notion.so/Lens-2-0-Local-Set-Up-eab16d644d2c4f668246cd84ab7d1684?pvs=21) | **- `/v2/load`, 

-  `/v2/sql`** |
| **`graphql`** | **`v2/graphql`** |
| [**`pre-aggregations`**](https://www.notion.so/API-Endpoints-and-their-scopes-a41a79334ce244979b1aeae72fc651a7?pvs=21) | 
**- `/v2/operate/pre-aggregations/timezones`, 

- `/v2/operate/pre-aggregations/security-contexts`,

- `/v2/operate/pre-aggregations/partitions`, 

- `/v2/operate/pre-aggregations/jobs`,

- `/v2/operate/pre-aggregations/jobs`

- `/v2/operate/pre-aggregations/preview`** |
| [**`source`**](https://www.notion.so/API-Endpoints-and-their-scopes-a41a79334ce244979b1aeae72fc651a7?pvs=21) | **- `/v2/default/schemas/`

- `/v2/default/schemas/sandbox/tables`

- `/v2/default/schemas/retail/tables/city`** |

                           *List of API Scopes and their Endpoints*

## **API Scopes and Their Corresponding Endpoints**

## meta scope:

Provides access to metadata-related endpoints. This scope allows users to view metadata, which typically includes information about sources, authors, timezones, security context, user groups, etc.

### **`\meta`**

**Syntax**                                                                                                                                                                                             **Example**

```bash
http://<host_name>:<port_name>/lens2/api/<data_model_name>/v2/meta
```

```bash
http://localhost:4000/lens2/api/sales_analysis/v2/meta
```

**Example response:**

```json
{
    "name": 
    "description": 

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
            },
```

<aside>
💡 Providing access to the `meta` API scope grants a user access to the Model and Explore Tab of the Lens 2.0 Studio Interface. But to fetch insights using the Explore interface, a user also requires the `data` API scope.

</aside>

## data scope:

### **`/load`** :

Executes queries to retrieve data based on the specified dimensions, measures, and filters. When you need to perform data analysis or retrieve specific data from the data model. 

Use `POST` request method along with `/load` endpoint to add or update the data.

**Syntax                                                                          Example**                                                                                    

```bash
http://<host_name>:<port_name>/lens2/api/<data_model_name>/v2/load?query=<query_parameters>

```

```bash
http://localhost:4000/lens2/api/sales_analysis/v2/load?query={"dimensions":["customer.customer_id","customer.annual_income"],"measures":["customer.total_customers", "customer.average_age"]}
```

**Syntax                                                                         Example**                                                                                                                                                   

```bash
http://<host_name>:<port_name>/lens2/api/<data_model_name>/v2/load
```

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

Example response:

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

### `/sql`

Alternatively, you can use `/sql` endpoint.

```bash
http://localhost:4000/lens2/api/sales_analysis/v2/sql
```

configure the body with the JSON Query Format similar to `/load`.

## graphql

Grants access to GraphQL endpoints. GraphQL is a query language for APIs that allows clients to request only the data they need. This scope enables users to perform GraphQL queries and mutations.

```sql

```

## pre-aggregations scope

 Provides access to job-related and pre-aggregation endpoints. 

**`/jobs` Endpoint:**

Jobs API grants access to build pre-aggregates. Without defining jobs api scope in api_scopes you won’t be able to preview the pre-aggregates.

| **Parameter** | **Description** | **Action** |
| --- | --- | --- |
| `list` | An array of lens names which contain pre-aggregations | `GET` |
| `security-contexts` | An array of objects, each containing a `securityContext` or `user groups`. | `GET` |
| `timezones` | Array of timezones | `GET` |
| `jobs` | Grants access to build pre-aggregates. | `POST` |
| `partitions` | An array of partitions in pre-aggregates. | `POST` |
| `preview` | Preview the pre-aggregations/lens | `POST` |

## source scope:

 Grants access to source-related endpoints. 

| **Parameter** | **Description** | **Action** |
| --- | --- | --- |
| `schemas` | An array of schemas name in the data source. | `GET` |
| `tables` | An array of schemas and tables name in the data source. | `GET` |
| `describe-table` | describes given source table | `GET` |
| `load-source` | load all datasets of source. | `POST` |

### `/schemas`

### `schemas/<catalogue_name>/tables`

### `/v2/default/schemas/retail/tables/city`