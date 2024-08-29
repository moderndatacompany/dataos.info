# Consumption of Lens using GraphQL

Lens provides a GraphQL API interface for querying your deployed model. This document will guide you through the process of accessing the GraphQL interface and executing queries against the Lens model. You can interact with the Lens GraphQLAPI either through:

1. [**Lens Studio**](/resources/lens/consumption_of_deployed_lens/consumption_using_graphql/#method-1:-accessing-graphql-via-lens-studio): DataOS interface that serves as an interactive in-browser tool for writing GraphQL queries on top of deployed Lens.

2. [**Postman**](/resources/lens/consumption_of_deployed_lens/consumption_using_graphql/#method-1:-accessing-graphql-via-postman): For more manual query execution and testing.

## How to access GraphQL?

## Method 1: Accessing GraphQL via Lens Studio

The GraphQL Tab in Lens Studio provides an interactive environment for writing and executing GraphQL queries.

### **Step 1: Navigate to the deployed Lens on Metis UI**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/66c3969c-8022-4269-a3c7-bff8859d8802/Untitled.png)

### **Step 2: Click on the ‘Explore in Studio’ Button**

![annotely_image (2).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/c208927f-586e-422f-bfd9-2929b92b7b1c/annotely_image_(2).png)

### **Step 3: Navigate to the ‘Explore’ tab on Studio**

![annotely_image (1).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/32885c63-c383-41de-9a25-06cdf09110fc/annotely_image_(1).png)

### **Step 4: Create the GraphQL Query**

1. In the left pane, enter your GraphQL query. You can press `Ctrl` + `Space` to bring up the autocomplete window. For example:

```graphql
query LensQuery {
    table {
      wallet_sales_view {
      revenue
    }
    }
  }
```

You can now press the ‘Execute’ button or press `Ctrl` + `Enter` to run the GraphQL Query. The output will be displayed on the right side as follows:

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


## Method 2: Accessing GraphQL via Postman

This section guides you through accessing Lens's GraphQL API using Postman or a web browser. This method is suitable for developers who prefer a more hands-on approach to testing and querying the API outside of Lens Studio.

### **Step 1: Setting Up Postman**

Ensure you have Postman installed either as an application or as a Visual Studio Code Extension. If not, you can refer to the following link.

### **Step 2: Create a New Request**

1. Open Postman and click on `New` to create a new request.
2. Select `HTTPS Request`.

### **Step 3: Configure the Request**

1. **URL**: Enter the URL of your deployed GraphQL endpoint. Sample URLs for localhost and DataOS environment are provided below:
**For locally hosted Lens**, the endpoint will be as follows**:**
    
    ```graphql
    https://localhost:4000/lens2/api/<name-of-lens>/v2/graphql
    ```
    
    For instance, if the `<name-of-lens>` is `mylens` the URL will be as follows:
    
    ```graphql
    https://localhost:4000/lens2/api/mylens/v2/graphql
    ```
    
    **For Lens deployed on DataOS Environment**, the endpoint will be as follows:
    
    ```graphql
    https://<dataos-fqdn>/lens2/api/<workspace>:<name-of-lens>/v2/graphql
    ```
    
    For example, if the `<dataos-fqdn>` is `alpha-omega.dataos.app`, `<workspace>` in which Lens is deployed is `sandbox`, and the `<name-of-lens>` is `mylens`, the URL will be following:
    
    ```graphql
    https://alpha-omega.dataos.app/lens2/api/sandbox:mylens/v2/graphql
    ```
    
2. **Request Method**: Select `POST` as the request method.

### **Step 4: Set Up Headers**

1. Click on the `Headers` tab.
2. Add the following headers:
    - Key: `apikey`
    - Value: `DATAOS_APIKEY_TOKEN` (replace `DATAOS_APIKEY_TOKEN` with the actual token by using the `dataos-ctl user apikey get` or `dataos-ctl user apikey create` command).

### **Step 5: Create the GraphQL Query**

1. Click on the `Body` tab.
2. Select `GraphQL` from the dropdown.
3. Enter your GraphQL query. For instance:
    
```graphql
query LensQuery {
  table {
    wallet_sales_view {
    revenue
  }
  }
}
```

**Expected Output**

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

## Query Examples

### **Querying a dimension**

A GraphQL query to retrieve the `city` dimension associated with an `account` table might look something like this:

```graphql
query LensQuery {
    table {
     account {
      city
    }
    }
  }
```

**Expected Output**

```json
{
"data": {
"table": [
{
  "account": {
    "city": "Amarillo"
  }
},
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
    "city": "Charleston"
  }
},
{
  "account": {
    "city": "Chicago"
  }
},
{
  "account": {
    "city": "Cincinnati"
  }
},
{
  "account": {
    "city": "Colorado Springs"
  }
},
{
  "account": {
    "city": "Columbus"
  }
},
{
  "account": {
    "city": "Denver"
  }
},
{
  "account": {
    "city": "Fort Lauderdale"
  }
},
{
  "account": {
    "city": "Fort Myers"
  }
},
{
  "account": {
    "city": "Fort Wayne"
  }
},
{
  "account": {
    "city": "Greenville"
  }
},
{
  "account": {
    "city": "Houston"
  }
},
{
  "account": {
    "city": "Jacksonville"
  }
},
{
  "account": {
    "city": "Kansas City"
  }
},
{
  "account": {
    "city": "King of Prussia"
  }
},
{
  "account": {
    "city": "Lafayette"
  }
},
{
  "account": {
    "city": "Longview"
  }
},
{
  "account": {
    "city": "Los Angeles"
  }
},
{
  "account": {
    "city": "Miami"
  }
},
{
  "account": {
    "city": "Minneapolis"
  }
},
{
  "account": {
    "city": "New York"
  }
},
{
  "account": {
    "city": "Omaha"
  }
},
{
  "account": {
    "city": "Philadelphia"
  }
},
{
  "account": {
    "city": "Portland"
  }
},
{
  "account": {
    "city": "Puyallup"
  }
},
{
  "account": {
    "city": "Rochester"
  }
},
{
  "account": {
    "city": "Sacramento"
  }
},
{
  "account": {
    "city": "San Antonio"
  }
},
{
  "account": {
    "city": "San Diego"
  }
},
{
  "account": {
    "city": "San Francisco"
  }
},
{
  "account": {
    "city": "San Jose"
  }
},
{
  "account": {
    "city": "Seattle"
  }
},
{
  "account": {
    "city": "Spokane"
  }
},
{
  "account": {
    "city": "Springfield"
  }
},
{
  "account": {
    "city": "Syracuse"
  }
},
{
  "account": {
    "city": "Tampa"
  }
},
{
  "account": {
    "city": "Tulsa"
  }
}
]
}
}
```
    

### **Querying Measure and Dimension**

A GraphQL query to retrieve the `city` and the `total_accounts` associated with each entry within the `account` table is given below:

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

**Expected Output**
    
```json
{
  "data": {
    "table": [
      {
        "account": {
          "city": "Los Angeles",
          "total_accounts": 59
        }
      },
      {
        "account": {
          "city": "Chicago",
          "total_accounts": 12
        }
      },
      {
        "account": {
          "city": "Kansas City",
          "total_accounts": 11
        }
      },
      {
        "account": {
          "city": "San Francisco",
          "total_accounts": 8
        }
      },
      {
        "account": {
          "city": "New York",
          "total_accounts": 6
        }
      },
      {
        "account": {
          "city": "Miami",
          "total_accounts": 5
        }
      },
      {
        "account": {
          "city": "Houston",
          "total_accounts": 5
        }
      },
      {
        "account": {
          "city": "Philadelphia",
          "total_accounts": 5
        }
      },
      {
        "account": {
          "city": "Greenville",
          "total_accounts": 5
        }
      },
      {
        "account": {
          "city": "Omaha",
          "total_accounts": 4
        }
      },
      {
        "account": {
          "city": "Sacramento",
          "total_accounts": 4
        }
      },
      {
        "account": {
          "city": "Cincinnati",
          "total_accounts": 3
        }
      },
      {
        "account": {
          "city": "Denver",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Baton Rouge",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Minneapolis",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Baltimore",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Fort Lauderdale",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Spokane",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Fort Wayne",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Portland",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Tampa",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Lafayette",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Colorado Springs",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Seattle",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Jacksonville",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "San Jose",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Fort Myers",
          "total_accounts": 2
        }
      },
      {
        "account": {
          "city": "Charleston",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "Springfield",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "Rochester",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "San Diego",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "Syracuse",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "Tulsa",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "San Antonio",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "Austin",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "Puyallup",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "King of Prussia",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "Longview",
          "total_accounts": 1
        }
      },
      {
        "account": {
          "city": "Amarillo",
          "total_accounts": 1
        }
      },
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

**Expected output**
    
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
          "total_accounts": 5,
          "city": "San Francisco",
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
          "city": "Houston",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 4,
          "city": "Miami",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 4,
          "city": "Philadelphia",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 2,
          "city": "Sacramento",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Spokane",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Rochester",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Charleston",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Jacksonville",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Austin",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "King of Prussia",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Longview",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "San Antonio",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "San Jose",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Springfield",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Tulsa",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Baltimore",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Lafayette",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Greenville",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Portland",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Fort Lauderdale",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Tampa",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Cincinnati",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Fort Myers",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Colorado Springs",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "San Diego",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Amarillo",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Syracuse",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Omaha",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Baton Rouge",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Fort Wayne",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Minneapolis",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Columbus",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Denver",
          "premise_code": "OFF"
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Puyallup",
          "premise_code": "OFF"
        }
      }
    ]
  }
}
```
    

### **Specifying order by condition and limiting the result**

A GraphQL query that specifies an order by condition and limits the number of results returned would look like this:

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

**Expected Output**
    
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
          "total_accounts": 11,
          "city": "Kansas City",
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
      {
        "account": {
          "total_accounts": 4,
          "city": "Philadelphia",
          "premise_code": "OFF"
        }
      }
    ]
  }
}
```
    

### **Querying multiple tables**

Using the same `account` table as before, let’s try and get the revenue for each. We can do this by adding the `sales` table to our query as follows:

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

**Expected Output**
    
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
          "total_accounts": 11,
          "city": "Kansas City",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 3423034
        }
      },
      {
        "account": {
          "total_accounts": 9,
          "city": "Chicago",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 3206423
        }
      },
      {
        "account": {
          "total_accounts": 7,
          "city": "Los Angeles",
          "premise_code": "BOTH"
        },
        "sales": {
          "revenue": 937897
        }
      },
      {
        "account": {
          "total_accounts": 5,
          "city": "New York",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 6716860
        }
      },
      {
        "account": {
          "total_accounts": 5,
          "city": "Houston",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 2687617
        }
      },
      {
        "account": {
          "total_accounts": 5,
          "city": "San Francisco",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 4070105
        }
      },
      {
        "account": {
          "total_accounts": 4,
          "city": "Greenville",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 477785
        }
      },
      {
        "account": {
          "total_accounts": 4,
          "city": "Philadelphia",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 1942174
        }
      },
      {
        "account": {
          "total_accounts": 4,
          "city": "Miami",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 668754
        }
      },
      {
        "account": {
          "total_accounts": 3,
          "city": "Omaha",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 405282
        }
      },
      {
        "account": {
          "total_accounts": 2,
          "city": "Sacramento",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 1404419
        }
      },
      {
        "account": {
          "total_accounts": 2,
          "city": "Cincinnati",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 164592
        }
      },
      {
        "account": {
          "total_accounts": 2,
          "city": "Sacramento",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 2528656
        }
      },
      {
        "account": {
          "total_accounts": 2,
          "city": "San Francisco",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 679107
        }
      },
      {
        "account": {
          "total_accounts": 2,
          "city": "Chicago",
          "premise_code": "BOTH"
        },
        "sales": {
          "revenue": 832273
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Springfield",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 777520
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Fort Lauderdale",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 221214
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "San Jose",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 181778
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Longview",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 946538
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "King of Prussia",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 766746
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Seattle",
          "premise_code": "BOTH"
        },
        "sales": {
          "revenue": 1063062
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Tulsa",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 850874
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Lafayette",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 115326
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Charleston",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 821340
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Colorado Springs",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 170232
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Puyallup",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 1035429
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Seattle",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 1177920
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "New York",
          "premise_code": "BOTH"
        },
        "sales": {
          "revenue": 781302
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Baltimore",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 869502
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Lafayette",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 744290
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Chicago",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 74490
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Portland",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 828035
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Spokane",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 990615
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Jacksonville",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 94176
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Greenville",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 1767816
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "San Francisco",
          "premise_code": "BOTH"
        },
        "sales": {
          "revenue": 700260
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Amarillo",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 99198
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Fort Myers",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 834013
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Tampa",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 145404
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Rochester",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 718650
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Colorado Springs",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 792634
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Fort Myers",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 119688
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Philadelphia",
          "premise_code": "BOTH"
        },
        "sales": {
          "revenue": 848815
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "San Jose",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 763857
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "San Diego",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 920196
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Portland",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 925375
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Fort Wayne",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 129940
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Tampa",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 880686
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Fort Wayne",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 852510
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "San Antonio",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 1211924
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Baltimore",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 486769
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Fort Lauderdale",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 896544
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Jacksonville",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 64960
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Denver",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 219864
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Columbus",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 617413
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Baton Rouge",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 173586
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Syracuse",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 850440
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Minneapolis",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 840108
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Baton Rouge",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 819126
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Minneapolis",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 458590
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Miami",
          "premise_code": "BOTH"
        },
        "sales": {
          "revenue": 142380
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Denver",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 798121
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Cincinnati",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 941096
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Omaha",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 629094
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Austin",
          "premise_code": "OFF"
        },
        "sales": {
          "revenue": 84138
        }
      },
      {
        "account": {
          "total_accounts": 1,
          "city": "Spokane",
          "premise_code": "ON"
        },
        "sales": {
          "revenue": 972030
        }
      }
    ]
  }
}
```