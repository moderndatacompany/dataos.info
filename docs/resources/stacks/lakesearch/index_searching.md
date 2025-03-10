# Lakesearch API endpoint and index searching

## Endpoint details

API endpoints are exposed on the `path` defined under the `ingress` section of a Lakesearch Service as shown below.

```yaml
service:
  servicePort: 4080
  ingress:
    enabled: true
    stripPath: false
    path: /lakesearch/public:ls-dummy
    noAuthentication: true
```


An API endpoint can be accessed via an URL shown below by replacing the place holders.

<div class="grid" markdown>

=== "Base URL"

    `{{base_url}}: ${{dataos_context_url}}/lakesearch/${{workspace}}:${{service_name}}`

=== "Curl command"

    ```bash
    curl -X GET "${{dataos_context_url}}/lakesearch/${{workspace}}:${{service_name}}/api/v2/index" \                           
    -H "Authorization: ${{dataos-user-token}}"
    ```
=== "Example"

    ```bash
    curl -X GET "https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index" \                           
    -H "Authorization: Bearer dG9rZW5fZGlzdhlkg3RseV9tYWlubHlfdXBlkmF5LjU1ZmE1ZWQyLWUwNDgtNGI3Yi1hNGQ2LWNlNjA1YTAzZTE4YQ=="
    ```
</div>

<aside class="callout">
🗣️ A user can get DataOS profile token from the profile section of DataOS Interface

</aside>

The following table containd the different endpoints for different purposes.

| **Endpoint** | **Method** | **Description** |
|-------------|----------|---------------|
| `{{base_url}}/version` | GET | Returns the Lakesearch version that is being used by the running service. |
| `{{base_url}}/healthz` | GET | Returns the health status of the service. |
| `{{base_url}}/metrics` | GET | Returns all the Prometheus metrics exposed by the service. |
| `{{base_url}}/api/v2/index` | GET | Lists all the indices created by the service. |
| `{{base_url}}/api/v2/index/:index_name` | GET | Uses a path variable `index_name`; describes the defined index. |
| `{{base_url}}/api/v2/index/:index_name/search` | GET | Uses a path variable `index_name`, and a query parameter `size`; executes a match_all query and returns all the fetched documents. If `size` is not set, it would still return at least 1 document. There is no upper limit to defining `size`. |
| `{{base_url}}/api/v2/index/:index_name/suggestions` | GET | Uses a path variable `index_name` and a query parameter `word`. The API returns suggested keywords, Levenshtein distance between the suggested and original keywords, and document statistics of the suggested keyword. |
| `{{base_url}}/api/v2/index/:index_name/keywords` | GET | Uses a path variable `index_name` and two query parameters: <br> - `word`: Partial word with `*` suffix <br> - `limit`: Assists with autocomplete use cases. |
| `{{base_url}}/api/v2/index/:index_name/search` | POST | Uses a path variable `index_name`; accepts search queries as JSON payloads and returns results. |
| `{{base_url}}/api/v2/embedding` | POST | Accepts KNN search queries. |
| `{{base_url}}/api/v2/_bulk` | POST | Elasticsearch `_bulk` endpoint. [More Details](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html) |




LakeSearch allows a user to search for an index using various filters and search parameters. The below sections explains how to perform searches efficiently.

<!-- ## Search Types

You can search for an index in different ways:

- **By Index Name**: A user can search for an index by its name.

- **By Keyword**: Use partial names or relevant terms to find the index.

- **By Metadata Filters**: Filter results based on metadata like creation date, size, owner, etc.

- **By Custom Queries**: Use advanced query options to refine search results. -->

## Basic search request

A basic search request is a structured query used to retrieve documents from an index based on specific criteria. Below is a breakdown of the key parameters involved in a basic search request.

1. `query`: Specifies the search conditions for fetching documents from the index. For example, it might filter for documents with a particular job (e.g., *UX Designer*) and those where the address field includes the word *Sigrid*. This is a **mandatory** parameter.

2. `limit`: Defines the maximum number of documents to return. This is an **optional** parameter. Alternatively, `size` can also be used for this purpose.

3. `_source`: Specifies an array of fields to return in the search results, similar to the `select` clause in SQL. This is an **optional** parameter.

    1. If this is not defined, all the available attributes are fetched.

    2. You can also use `exclude` and `include` to define the attributes returned in the response payload.

4. `sort`: An array of fields to define the sorting order of the results, similar to the `order by` clause in SQL. This is an **optional** parameter.

### **How to perform a basic search request?**

A search request is made using an HTTP `POST` request because it contains a body with search parameters. The query must be included in the request body in JSON format.

**Example**
  
A search request can be designed to return documents where the address field contains the word "Sigrid" and the job field matches "UX Designer".
    
```bash
curl -X POST "https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/_search" \
-H "Authorization: Bearer dG9rZW5fZGlzdhlkg3RseV9tYWlubHl2jXBlkmF5LjU1ZmE1ZWQyLWUwNDgtNGI3Yi1hNGQ2LWNlNjA1YTAzZTE4YQ==" \
-H "Content-Type: application/json" \
-d '{
    "query": {
        "bool": {
            "must": [
                { "match": { "address": "Sigrid" } },
                { "term": { "job": "UX Designer" } }
            ]
        }
    },
    "size": 10,
    "_source": {
        "excludes": ["phone_number", "customer_name"]
    },
    "sort": [
        { "@timestamp": "desc" },
        { "birthdate": "asc" }
    ]
}'

```
    

## Search Types

When searching through large sets of data, different types of queries help retrieve relevant results efficiently. Each type of search works differently depending on how precise the results need to be.

### **Match**

Match search looks for documents that contain the specified keywords in a particular field. It performs a full-text search, meaning it breaks down the input text and matches it with the indexed content.

**Syntax**

```json
{
    "query": {
        "match": {
            "<field_name>": "<search_term>"
        }
    }
}
```

**Examples**

- **Searching a specific column**: If someone searches for "Sigrid" in the "address" field, it will return all documents where "Sigrid" appears in the address.
    
    ```json
    {
        "query": {
            "match": {
                "address": "Sigrid"
            }
        }
    }
    ```
    
- **Searching all the columns**
    
    ```json
    {
        "query": {
            "match": {
                "*": "Sigrid"
            }
        }
    }
    ------------ OR ------------
    {
        "query": {
            "match": {
                "_all": "Sigrid"
            }
        }
    }
    ```
    
- **Searching all the columns except one**
    
    ```json
    {
        "query": {
            "match": {
                "!address": "Sigrid"
            }
        }
    }
    ```
    
- **Searching only a few columns**
    - By default, keywords are combined using the OR operator.
    - However, you can change that behavior using the "operator" clause.
    - `operator` can be set to "or" or "and".
    
    ```json
    {
        "query": {
            "match": {
                "address,email": {
                    "query": "Sigrid .net",
                    "operator": "and"
                }
            }
        }
    }
    ```


        

### **Match Phrase**

This search finds an exact phrase instead of separate words. All words must appear together, in the same order, without gaps. E.g., searching for `"gaming laptop"` only returns documents where "gaming laptop" appears as a phrase, not where "gaming" and "laptop" are separate or in a different order. Best for finding names, addresses, or specific phrases in text-heavy documents. Useful when looking for a fixed combination of words.

**Syntax**

```json
{
    "query": {
        "match_phrase": {
            "field_name": "<search_phrase>"
        }
    }
}
```

**Examples**

- **Searching a specific column**: This will only fetch the document(s) where the exact phrase is matched in the *address* column.
    
    ```json
    {
        "query": {
            "match_phrase": {
                "address": "Sigrid Curve, MS 6413"
            }
        }
    }
    ```
    
- **Searching all the columns**
    
    ```json
    {
        "query": {
            "match_phrase": {
                "_all": "Sigrid Curve, MS 6413"
            }
        }
    }
    ------------ OR ------------
    {
        "query": {
            "match_phrase": {
                "*": "Sigrid Curve, MS 6413"
            }
        }
    }
    ```
    
- **Searching all the columns except one**
    
    ```json
    {
        "query": {
            "match_phrase": {
                "!address": "Sigrid Curve, MS 6413"
            }
        }
    }
    ```
        

### **Query String**

`query_string` accepts an input string as a full-text query. This allows for complex queries using boolean operators, wildcards, field-specific searches, and more. It provides a flexible query syntax.

**Syntax**

```json
{
    "query": {
        "query_string": "<search_query>"
    }
}
```

**Operators:**

- Field Start and End Identifiers
    
    ```json
    //This will fetch all documents where any column value starts with *Sigrid*.
    {
        "query": {
            "query_string": "^Sigrid"
        }
    }
    //This will fetch all documents where any column value ends with com.
    {
        "query": {
            "query_string": "com$"
        }
    }
    ```
    
- AND
    
    An implicit logical AND operator is always present, so *Sanders Inc* implies that both "*Sanders*" and "*Inc*" must be found in the matching document.
    
    ```json
    {
        "query": {
            "query_string": "Sanders Inc"
        }
    }
    ```
    
- OR
    
    The logical OR operator **`|`** has a higher precedence than AND.
    
    Eg. `Sanders Inc | Org | Gov` means `Sanders (Inc | Org | Gov)` and not `(Sanders Inc) | Org | Gov`.
    
    ```json
    {
        "query": {
            "query_string": "Sanders | Inc"
        }
    }
    ```
    
- NEAR
    
    ```json
    //This will fetch all documents where any column value has FALL word in 
    //promimity of defined distance(here 2, max 6) with SIGRID word.
    {
        "query": {
            "query_string": "Sigrid NEAR/2 Fall"
        }
    }
    ```
    
- NOTNEAR
    
    ```json
    // This will fetch all documents where any column value **does not** have FALL word in promimity of defined distance(here 2, max 6) with SIGRID word.
    {
        "query": {
            "query_string": "Sigrid NOTNEAR/2 Fall"
        }
    }
    ```
    
- Wildcard
    
    The search will attempt to find all expansions of the wildcarded tokens, and each expansion is recorded as a matched hit
    
    `*` - cam match n number of characters after or before the defined search term
    
    `?` - can match any single character: `t?st` will match `test`, but not `teast`
    
    `%` - can match zero or one character: `tes%` will match `tes` or `test`, but not `testing`
    
    ```json
    {
        "query": {
            "match": "Sigird*"
        }
    }
    
    -------------
    
    {
        "query": {
            "query_string": "@device_name mentio%"
        }
    }
    
    -------------
    
    {
        "query": {
            "query_string": "@device_name mentio?"
        }
    }
    ```
        


## Filter

Filters are added to a search query via the `bool` object. The `bool` query matches documents based on boolean combinations of other queries and/or filters. Queries and filters must be specified in `must`, `should`, or `must_not` sections and can be nested.

**Syntax**

```json
{
    "query": {
        "bool": {
            "<must/must_not/should>": [
                {
                    "match/equals/in/match_phrase": {
                        "<field_name>": "<search_value>"
                    }
                }
            ]
        }
    }
}
```

**Examples**

- MATCH + Filter
    
    ```json
    // This fetches all documents where address has a word SIGRID and 
    // JOB = UX Designer.
    {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "address": "Sigrid"
                        }
                    },
                    {
                        "equals": {
                            "job": "UX Designer"
                        }
                    }
                ]
            }
        }
    }
    ```
    
- MATCH_PHRASE + Filter
    
    ```json
    {
        "query": {
            "match_phrase": "example.net",
            "bool": {
                "must": {
                    "equals": {
                        "job": "Sales Executive"
                    }
                }
            }
        }
    }
    ```
    
- QUERY_STRING + Filter - IN
    
    ```json
    {
        "query": {
            "bool": {
                "must": [
                    {
                        "query_string": "Wyman"
                    },
                    {
                        "in": {
                            "country": ["Djibouti","Gabon"]
                        }
                    }
                ]
            }
        }
    }
    ```
    
- MATCH + Filter - IN
    
    ```json
    {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "address": "Sigrid"
                        }
                    },
                    {
                        "in": {
                            "age": [47,50]
                        }
                    }
                ]
            }
        }
    }
    ```
        

### **Must**

Documents must match all conditions within the must section (like AND in SQL). If multiple full-text queries or filters are specified, all of them must match.

**Example**
    
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "address": "Sigrid"
                    }
                },
                {
                    "equals": {
                        "job": "Software Engineer"
                    }
                }
            ]
        }
    }
}
```
    

### **Must Not**

Queries and filters specified in the `must_not` section must not match the documents. If several queries are specified under `must_not`, the fetched documents are the ones where none of them are matched.

**Example**
    
```json
{
    "query": {
        "bool": {
            "must_not": [
                {
                    "equals": {
                        "job": "Software Engineer"
                    }
                },
                {
                    "equals": {
                        "job": "Product Manager"
                    }
                }
            ]
        }
    }
}
```
    

### **Should**

Queries and filters specified in the `should` section should match the documents. If some queries are specified in `must` or `must_not`, then `should` queries are ignored.On the other hand, if there are no queries other than `should`, then at least one of these queries must match a document for it to match the bool query. This is the equivalent of `OR` queries.

**Example**
    
```json
{
    "query": {
        "bool": {
            "should": [
                {
                    "equals": {
                        "job": "Software Engineer"
                    }
                },
                {
                    "equals": {
                        "job": "Product Manager"
                    }
                }
            ]
        }
    }
}
```
    

### **Nested Bool**

A bool query can be nested inside another bool so you can make more complex queries. To make a nested boolean query just use another `bool` instead of `must`, `should` or `must_not`.

**Example**
    
```json
// Fetch all documents where address column have the Sigrid word and job is 
// either Product Manager OR UX Designer
// a = 2 and (b = 1 or b = 2)
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "address": "Sigrid"
                    }
                },
                {
                    "bool": {
                        "should": [
                            {
                                "equals": {
                                    "job": "Product Manager"
                                }
                            },
                            {
                                "equals": {
                                    "job": "UX Designer"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
}
```
    

### **Range**

- Range filters match documents that have attribute values within a specified range.
- Range filters support the following properties:
    1. `gte`: greater than or equal to
    2. `gt`: greater than
    3. `lte`: less than or equal to
    4. `lt`: less than

**Syntax**

```json
{
    "query": {
        "range": {
            "<field_name>": {
                "gte": <value>,
                "lte": <value>
            }
        }
    }
}
```

**Examples**

- Range Filter
    
    ```json
    {
        "query": {
            "range": {
                "age": {
                    "gte": 30,
                    "lte": 50
                }
            }
        }
    }
    ```
    
- MATCH + Range Filter
    
    ```json
    {
        "query": {
            "match_phrase": {
                "address": "Sigrid Curve, "
            },
            "range": {
                "age": {
                    "gte": 30,
                    "lte": 50
                }
            }
        }
    }
    ```
        


## Aggregations

Aggregations in LakeSearch allow you to group and analyze data based on specific attributes. The aggregation results can be customized using sorting, aliasing, and different calculation methods.

**Key points**

- The facet values can originate from an attribute.
- Facet values can also be aliased, but the **alias must be unique** across all result sets (main query result set and other facets result sets).
- **CALLOUT**: The sort definition defined in the `aggs` object does not sort the documents fetched. It only sorts the `aggs` object in the response payload. To sort all the fetched documents please define the `sort` object outside `query`.
- **CALLOUT**: To fetch only calculated aggregations, please keep `size=0` outside the `aggs` object. You must specify a maximum `size` inside the attribute object to include all the docs in the aggregate calculations. Refer examples.

**Syntax**

```json
{
    "size": 0,
    "aggs": {
        "group_name": {
            "terms": {
                "field": "attribute_name",
                "size": 1000
            }
		             "sort": [
                {
                    "attribute_name": {
                        "order": "asc"
                    }
                }
            ]
        }
    }
}
```

**Examples**

- Total Count
    
    ```json
    {
        "size": 0,
        "aggs": {
            "group_by_job": {
                "terms": {
                    "field": "job",
                    "size": 1000
                }
            }
        }
    }
    ```
    
- Min/Max/Avg/Rate/Sum
    
    ```json
    // Replace max by min/avg/rate/sum
    {
        "size": 0,
        "aggs": {
            "group_by_age": {
                "max": {
                    "field": "age",
                    "size": 1000
                }
            }
        }
    }
    ```
        

### **Buckets**

Bucket aggregations allow you to group data into predefined ranges. The values are checked against the bucket range, where each bucket includes the `from` value and excludes the `to` value from the range.

**Syntax**

```json
{
    "size": 0,
    "aggs": {
        "<agg_group_name>": {
            "range": {
                "field": "<field_name>",
                "ranges": [
                    {
                        "to": <value>
                    },
                    {
                        "from": <value>,
                        "to": <value>
                    }
                    }
                ]
            }
        }
    }
}
```

**Example**
    
```json
{
    "size": 0,
    "aggs": {
        "age_range": {
            "range": {
                "field": "age",
                "ranges": [
                    {
                        "to": 10
                    },
                    {
                        "from": 10,
                        "to": 30
                    },
                    {
                        "from": 30,
                        "to": 50
                    },
                    {
                        "from": 50,
                        "to": 80
                    },
                    {
                        "from": 50
                    }
                ]
            }
        }
    }
}
```
    

## Highlight

- Highlighting enables you to obtain highlighted text fragments (snippets) from documents containing matching keywords.
- Highlighting can only be enabled on text-type columns.
- Highlighted results are fetched in a separate `highlight` object in the response payload.
- `highlight` Parameters:
    1. `fields`: This object contains attribute names with options. It can also be an array of field names (without any options). Note that by default, highlighting attempts to highlight the results following the full-text query. In a general case, when you don't specify fields to highlight, the highlight is based on your full-text query. However, if you specify fields to highlight, it highlights only if the full-text query matches the selected fields. This is optional
    2. `highlight_query`: This option allows you to highlight against a query other than your search query. The syntax is the same as in the main `query`. This is optional.
    3. `pre_tags` and `post_tags`: These options set the opening and closing tags for highlighted text snippets. These are optional.

**Syntax**

```json
{
    "query": {},
    "highlight": {
        "fields": ["field1", "field2",...],
        "highlight_query": {
            "match": {
                "*": "example_search_term"
            }
        }
    }
}
```

- **Examples**
    - Simple Highlighting
        
        In this example, we are highlighting all text-type columns from all the documents.
        
        ```json
        {
            "query": {
                "match_all": {}
            },
            "highlight": {}
        }
        ```
        
    - Highlighting with `pre_tags` and `post_tags`
        
        In this example, we are searching the word “agreement” in all full-text enabled columns and enclosing it with the HTML bold tag `<b>`. 
        
        ```json
        {
            "query": {
                "match": {
                    "*": "agreement"
                }
            },
            "highlight": {
                "pre_tags": "<b>",
                "post_tags": "</b>"
            }
        }
        ```
        
    - Matching and Highlighting different words
        
        In this example, we are searching for the word “agreement" across all documents and highlighting the word "white" using the HTML `<b>` tag. Additionally, the response payload will only include the manufacturer column in the highlight object.
        
        ```json
        {
            "query": {
                "match": {
                    "*": "agreement"
                }
            },
            "highlight": {
                "fields": ["manufacturer"],
                "highlight_query": {
                    "match": {
                        "*": "white"
                    }
                },
                "no_match_size": 2,
                "pre_tags": "<b>",
                "post_tags": "</b>"
            }
        }
        ```
        

## Expressions

- Expressions are used to create dynamic columns via search queries.
- These columns hold the custom logic defined by the user in the query.
- These columns can be used to filter data.

**Syntax**

```json
{
    "query": {
        "match_all": {}
    },
    "expressions": {
        "<new_key_name>": "<expression>"
    }
}
```

### **Arithmetic Operators**

`+`, `-`, `*`, `/`, `%`, `DIV`, `MOD`

- Add (`+`)
    
    ```json
    {
        "size": 10,
        "query": {
            "match_all": {}
        },
        "expressions": {
            "add_row_num": "row_num + 10"
        }
    }
    ```
    
- Subtract (`-`)
    
    ```json
    {
        "size": 10,
        "query": {
            "match_all": {}
        },
        "expressions": {
            "add_row_num": "row_num - 10"
        }
    }
    ```
    
- Multiple (`*`)
    
    ```json
    {
        "size": 10,
        "query": {
            "match_all": {}
        },
        "expressions": {
            "add_row_num": "row_num * 10"
        }
    }
    ```
    
- Divide (`/`)
    
    ```json
    {
        "size": 10,
        "query": {
            "match_all": {}
        },
        "expressions": {
            "add_row_num": "row_num / 10"
        }
    }
    ```
    
- Divisor (`DIV`)
    
    ```json
    {
        "size": 10,
        "query": {
            "match_all": {}
        },
        "expressions": {
            "add_row_num": "row_num DIV 10"
        }
    }
    ```
    
- Remainder (`MOD`)
    
    ```json
    {
        "size": 10,
        "query": {
            "match_all": {}
        },
        "expressions": {
            "add_row_num": "row_num MOD 10"
        }
    }
    ```
    
- Filter
    
    ```json
    {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "status": "healthy"
                        }
                    },
                    {
                        "range": {
                            "warranty_expiry": {
                                "gte": 1678147200
                            }
                        }
                    }
                ]
            }
        },
        "expressions": {
            "days_offline": "(1702838400 - last_online) / 86400",
            "warranty_overlap": "(warranty_expiry - last_online) / 86400"
        },
        "sort": [
            {
                "warranty_expiry": "desc"
            }
        ]
    }
    ```
    

### **Comparison Operators**

The comparison operators `<`, `>`, `<=`, `>=`, `=`, and `<>` return `1` when the condition is true and `0` otherwise.

- Less than
    
    ```json
    {
        "size": 10,
        "query": {
            "bool": {
                "must": [
                    {
                        "equals": {
                            "row_num": 1
                        }
                    }
                ]
            }
        },
        "expressions": {
            "add_row_num": "row_num < 10"
        }
    }
    ```
    
- Greater than
    
    ```json
    {
        "size": 10,
        "query": {
            "bool": {
                "must": [
                    {
                        "equals": {
                            "row_num": 1
                        }
                    }
                ]
            }
        },
        "expressions": {
            "add_row_num": "row_num > 10"
        }
    }
    ```
    
- Less than or equal to
    
    ```json
    {
        "size": 10,
        "query": {
            "bool": {
                "must": [
                    {
                        "equals": {
                            "row_num": 1
                        }
                    }
                ]
            }
        },
        "expressions": {
            "add_row_num": "row_num <= 10"
        }
    }
    ```
    
- Greater than or equal to
    
    ```json
    {
        "size": 10,
        "query": {
            "bool": {
                "must": [
                    {
                        "equals": {
                            "row_num": 1
                        }
                    }
                ]
            }
        },
        "expressions": {
            "add_row_num": "row_num >= 10"
        }
    }
    ```
    
- Equal
    
    ```json
    {
        "size": 10,
        "query": {
            "bool": {
                "must": [
                    {
                        "equals": {
                            "row_num": 1
                        }
                    }
                ]
            }
        },
        "expressions": {
            "add_row_num": "row_num = 10"
        }
    }
    ```
    
- Not Equal
    
    ```json
    {
        "size": 10,
        "query": {
            "bool": {
                "must": [
                    {
                        "equals": {
                            "row_num": 1
                        }
                    }
                ]
            }
        },
        "expressions": {
            "add_row_num": "row_num <> 10"
        }
    }
    ```
    

### **Boolean Operators**

Boolean operators (`AND`, `OR`, `NOT`) behave as expected. They are left-associative and have the lowest priority compared to other operators. `NOT` has higher priority than `AND` and `OR` but still less than any other operator. `AND` and `OR` share the same priority, so using parentheses is recommended to avoid confusion in complex expressions.

- AND
    
    ```json
    {
        "size": 10,
        "query": {
            "match_all": {}
        },
        "expressions": {
            "check": "(created_at < updated_at) AND (created_at - updated_at <> 0)"
        }
    }
    ```
    
- OR
    
    ```json
    {
        "size": 10,
        "query": {
            "match_all": {}
        },
        "expressions": {
            "check": "(created_at < updated_at) OR (created_at - updated_at <> 0)"
        }
    }
    ```
    
- NOT
    
    ```json
    {
        "size": 10,
        "query": {
            "match_all": {}
        },
        "expressions": {
            "check": "NOT (created_at - updated_at = 0)"
        }
    }
    ```
    

### **Mathematical Functions**

**Syntax**

```json
// Example of SQRT() function
{
    "size": 1,
    "query": {
        "match_all": {}
    },
    "expressions": {
        "check": "SQRT(<field_name>)"
    }
}
```

1. `MAX()`
    
    Returns the larger of two arguments.
    
2. `MIN()`
    
    Returns the smaller of two arguments.
    
3. `SQRT()`
    
    Returns the square root of the argument.
    

### **Type Casting Functions**

**Syntax**

```json
// Example of SINT() function
{
    "size": 10,
    "query": {
        "query_string": "anyone"
    },
    "expressions": {
        "check": "SINT(1-2)"
    }
}
```

1. `TO_STRING()`
    
    This function forcefully converts its argument to a string type. This involves additional computations.
    
2. `BIGINT()`
    
    This function promotes an integer argument to a 64-bit type, leaving floating-point arguments untouched. 
    
    It's designed to ensure the evaluation of specific expressions (such as **`a*b`**) in 64-bit mode, even if all arguments are 32-bit.
    
3. `DOUBLE()`
    
    Promotes its argument to a floating-point type.
    
4. `INTEGER()`
    
    Promotes its argument to a 64-bit signed type.
    
5. `UNIT()`
    
    Promotes its argument to a 32-bit unsigned integer type.
    
6. `UNIT64()`
    
    Promotes its argument to a 64-bit unsigned integer type.
    
7. `SINT()`
    - Function forcefully reinterprets its 32-bit unsigned integer argument as signed and extends it to a 64-bit type (since the 32-bit type is unsigned).
    - For instance, 1-2 ordinarily evaluates to 4294967295, but `SINT(1-2)` evaluates to `-1`.

### **Condition Functions**

1. `IF()`
    - It takes 3 arguments, checks whether the 1st argument is equal to 0.0, returns the 2nd argument if it is not zero, or the 3rd one when it is.
    - If no threshold is passed, by default it will compare with 0.0
    - **Example**
        
        ```json
        {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "status": "healthy"
                            }
                        },
                        {
                            "range": {
                                "warranty_expiry": {
                                    "gte": 1678147200
                                }
                            }
                        },
                        {
                            "equals": {
                                "warranty_overlap": 1
                            } //only show documents where warranty overlap is 1
                        }
                    ]
                }
            },
            "expressions": {
                "warranty_overlap": "IF (warranty_expiry-1791331200 = 0, 1, 0 )"
            },
            "sort": [
                {
                    "warranty_expiry": "desc"
                }
            ]
        }
        ```
        
2. `IN()`
    
    Matches the values with the expression, if it evaluates to be true returns 0, else 1.
    
    - **Example**
        
        `"warranty_overlap": "IN (device_type, 'Notebook','Convertible')”`
        
        ```json
        {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "status": "healthy"
                            }
                        },
                        {
                            "range": {
                                "warranty_expiry": {
                                    "gte": 1678147200
                                }
                            }
                        }
                    ]
                }
            },
            "expressions": {
                "warranty_overlap": "IN (warranty_expiry, 1756339200, 1745452800, 1730937600)"
            },
            "sort": [
                {
                    "warranty_expiry": "desc"
                }
            ]
        }
        ```
        
3. NESTED `IF()` and `IN()`
    - **Example**
        
        ```json
        {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "status": "healthy"
                            }
                        },
                        {
                            "range": {
                                "warranty_expiry": {
                                    "gte": 1678147200
                                }
                            }
                        },
                        {
                            "equals": {
                                "device_filter": 2
                            }
                        }
                    ]
                }
            },
            "expressions": {
                "device_filter": "IF (IN (warranty_expiry,1786060800,1776470400),2, IF(IN(warranty_expiry,1756339200,1745452800),1,0))"
            },
            "sort": [
                {
                    "warranty_expiry": "desc"
                }
            ]
        }
        ```
        
4. `CONCAT()`
    - Concatenates two or more strings into one.
    - For concatenate to work, non-string arguments must be explicitly converted to string using the `TO_STRING()` function
    - **Example**
        
        ```json
        {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "status": "healthy"
                            }
                        },
                        {
                            "range": {
                                "warranty_expiry": {
                                    "gte": 1678147200
                                }
                            }
                        }
                    ]
                }
            },
            "expressions": {
                "warranty_overlap": "CONCAT(TO_STRING(DATE(warranty_expiry)), '-', device_type)"
            },
            "sort": [
                {
                    "warranty_expiry": "desc"
                }
            ]
        }
        ```
        
5. `HISTOGRAM()`
    - Categorize numerical data into discrete buckets or intervals.
    - `HISTOGRAM(expr, {hist_interval=size, hist_offset=value})` takes a bucket size and returns the bucket number for the value.
    - **Example**
        
        ```json
        {
            "query": {
                "bool": {
                    "must": [
                        {
                            "equals": {
                                "age_range": 40
                            }
                        }
                    ]
                }
            },
            "expressions": {
                "age_range": "HISTOGRAM(age, {hist_interval=20, hist_offset = 0})"
            },
            "sort": [
                {
                    "age_range": "desc"
                }
            ],
            "_source": {
                "excludes": [
                    "age",
                    "customer_name"
                ]
            }
        }
        ```
        
6. `INTERVAL()`
    - Another way to categorize numerical data into discreet ranges. Use this function in queries to filter results based on defined ranges.
    - The `INTERVAL` function takes two or more arguments and returns the index of the argument that is less than the first argument (`expr`)
    - The points must be in strictly increasing order (i.e., `point1 < point2 < ... < pointN`) for the function to work correctly.
        
        `INTERVAL(expr,point1,point2,point3,...)`
        
    - **Example**
        
        ```json
        // if age is 
        // < 20 : returns age_range = 0
        // 20 <= age < 40 : returns age_range = 1, etc..
        {
            "query": {
                "bool": {
                    "must": [
                        {
                            "equals": {
                                "age_range": 3
                            }
                        }
                    ]
                }
            },
            "expressions": {
                "age_range": "INTERVAL(age,20,40,60,80)"
            },
            "sort": [
                {
                    "age_range": "desc"
                }
            ],
            "_source": {
                "excludes": [
                    "customer_name"
                ]
            }
        }
        ```
        
7. `RANGE()`
    - To create buckets, aggregate, and sort by that bucket.
    - `RANGE(expr, {range_from=value,range_to=value})` takes a set of ranges and returns the bucket number for the value.
    - **Example**
        
        ```json
        {
            "query": {
                "match_all": {}
            },
            "expressions": {
                "age_range": "RANGE(age, {range_to=20},{range_from=20,range_to=40},{range_from=40})"
            },
            "aggs": {
                "age_group": {
                    "terms": {
                        "field": "age_range"
                    }
                }
            },
            "sort": [
                {
                    "age_range": {
                        "order": "desc"
                    }
                }
            ],
            "_source": {
                "excludes": [
                    "age",
                    "customer_name"
                ]
            }
        }
        ```
        

### **Date Functions**

**Syntax**

```json
// Example of MONTHNAME()
{
    "query": {
        "match_all": {},
        "bool": {}
    },
    "expressions": {
        "joining_month": "MONTHNAME(created_at)"
    },
    "sort": [
        {
            "joining_month": {
                "order": "asc"
            }
        }
    ],
    "_source": {
        "excludes": [
            "customer_name"
        ]
    }
}
```

1. `NOW()`
    
    Returns the current timestamp as an INTEGER.
    
2. `CURTIME()`
    
    Returns the current time in the local timezone in `hh:ii:ss` format.
    
3. `CURDATE()`
    
    Returns the current date in the local timezone in `YYYY-MM-DD` format.
    
4. `UTC_TIME()`
    
    Returns the current time in UTC timezone in `hh:ii:ss` format.
    
5. `UTC_TIMESTAMP()`
    
    Returns the current time in UTC timezone in `YYYY-MM-DD hh:ii:ss` format.
    
6. `SECOND()`
    
    Returns the integer second (in the 0-59 range) from a timestamp argument, according to the current timezone.
    
7. `MINUTE()`
    
    Returns the integer minute (in the 0-59 range) from a timestamp argument, according to the current timezone.
    
8. `HOUR()`
    
    Returns the integer hour (in the 0-23 range) from a timestamp argument, according to the current timezone.
    
9. `DAY()`
    
    Returns the integer day of the month (in the 1-31 range) from a timestamp argument, according to the current timezone.
    
10. `MONTH()`
    
    Returns the integer month (in the 1-12 range) from a timestamp argument, according to the current timezone.
    
11. `QUARTER()`
    
    Returns the integer quarter of the year (in the 1-4 range) from a timestamp argument, according to the current timezone.
    
12. `YEAR()` 
    
    Returns the integer year (in the 1969-2038 range) from a timestamp argument, according to the current timezone.
    
13. `DAYNAME()`
    
    Returns the weekday name for a given timestamp argument, according to the current timezone.
    
14. `MONTHNAME()`
    
    Returns the name of the month for a given timestamp argument, according to the current timezone.
    
15. `DAYOFWEEK()`
    
    Returns the integer weekday index (in the 1-7 range) for a given timestamp argument, according to the current timezone. Note that the week starts on Sunday.
    
16. `DAYOFYEAR()`
    
    Returns the integer day of the year (in 1..366 range) for a given timestamp argument, according to the current timezone.
    
17. `YEAROFWEEK()`
    
    Returns the integer year and the day code of the first day of the current week (in the 1969001-2038366 range) for a given timestamp argument, according to the current timezone.
    
18. `YEARMONTH()`
    
    Returns the integer year and month code (in the 196912-203801 range) from a timestamp argument, according to the current timezone.
    
19. `YEARMONTHDAY()`
    
    Returns the integer year, month, and date code (from 19691231 to 20380119) based on the current timezone.
    
20. `TIMEDIFF()`
    
    Calculates the difference between two timestamps in the format `hh:ii:ss`.
    
21. `DATEDIFF()`
    
    Calculates the number of days between two given timestamps.
    
    - **Example**
        
        ```json
        {
            "query": {
                "match_all": {},
                "bool": {}
            },
            "expressions": {
                "warranty_period": "DATEDIFF(warranty_expiry, purchase_date)"
            },
            "sort": [
                {
                    "warranty_period": {
                        "order": "desc"
                    }
                }
            ]
        }
        ```
        
22. `DATE()`
    
    Formats the date part from a timestamp argument as a string in `YYYY-MM-DD` format.
    
    - **Example**
        
        ```json
        {
            "query": {
                "match_all": {},
                "bool": {}
            },
            "expressions": {
                "check": "DATE(NOW())"
            }
        }
        ```
        
23. `TIME()`
    
    Formats the time part from a timestamp argument as a string in `HH:MM:SS` format.
    
    - **Example**
        
        ```json
        {
            "query": {
                "match_all": {},
                "bool": {}
            },
            "expressions": {
                "check": "TIME(NOW())"
            }
        }
        ```
        
24. `DATE_RANGE()`
    - It takes a range set and returns the value's bucket number.
    - The expression includes the `range_from` value and excludes the `range_to` value for each range.
    - The range can be open - having only the `range_from` or only the `range_to` value.
    - The difference between this and the RANGE() function is that the `range_from` and `range_to` values can be expressed in Date math expressions.
    - `DATE_RANGE(expr, {range_from='date_math', range_to='date_math'})`
    - **Example**
        
        ```json
        {
            "query": {
                "match_all": {},
                "bool": {}
            },
            "expressions": {
                "warranty_period": "DATE_RANGE(warranty_expiry, {range_to='2023||+2M/M'},{range_from='2023||+2M/M',range_to='2023||+5M/M'},{range_from='2024||+5M/M'})"
            },
            "sort": [
                {
                    "warranty_period": {
                        "order": "desc"
                    }
                }
            ]
        }
        ```