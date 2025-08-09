# Lakesearch API 

!!! info "Overview"
    LakeSearch is a powerful DataOS Stack that makes it easy to add fast, scalable search across Lakehouse tables. It allows app developers to add powerful search functionality, with indexing and query performance that can scale to meet business needs.

The LakeSearch API lets users search, filter and aggregate data from indexed tables using simple, flexible queries. A search consists of one or more queries that are combined and sent to Lakesearch. The system processes these queries and returns matching documents as hits or search results in the response. Additionally, a search may include parameters to refine query processing. For instance, it can be restricted to a specific index or configured to return a limited number of results. 

## Core Capabilities of LakeSearch

- **Full-Text Search**
    
    Find the exact information you need—like product names or customer details—quickly and accurately using advanced text matching.
    
- **Smart (Semantic) Search**
    
    Understands the meaning behind your search, not just the keywords—so you get more relevant results.
    
- **Search Built Into Your Apps**
    
    Easily add search features to your apps, dashboards, or internal tools—so your teams can explore data without needing technical help.
    

We have implemented the LakeSearch service that retrieves data from the source and indexes each column from one or multiple tables, making it searchable.

<details><summary>LakeSearch API YAML</summary>

```yaml
name: pals
version: v1
type: service
tags:
  - service
  - dataos:type:resource
  - dataos:resource:service
  - dataos:layer:user
description: Lakesearch Service Simple Index Config
workspace: public
service:
  servicePort: 4080
  ingress:
    enabled: true
    stripPath: false
    path: /lakesearch/public:pals
    noAuthentication: true
  replicas: 1
  logLevel: 'INFO'
  compute: runnable-default
  envs:
    LAKESEARCH_SERVER_NAME: "public:pals"
    DATA_DIR: public/productaffinity/test02
    USER_MODULES_DIR: /etc/dataos/config
  persistentVolume:
    name: pap-volume
    directory: public/productaffinity/test02
  resources:
    requests:
      cpu: 250m
      memory: 256Mi
  stack: lakesearch:1.0
  stackSpec:
    lakesearch:
      source:
        datasets:
          - name: customer
            dataset: dataos://lakehouse:customer_relationship_management/customer_data

          - name: cross_sell
            dataset: dataos://lakehouse:customer_relationship_management/cross_sell_recommendations
            
      index_tables:
        - name: customer
          description: "index for cross sell recommendations"
          tags:
            - customer
          properties:
            morphology: stem_en
          columns:
            - name: education
              type: keyword
            - name: birth_year
              type: bigint
            - name: income
              type: float
            - name: customer_id
              type: bigint
            - name: country
              type: text
            - name: id
              description: "mapped to row_num"
              tags:
                - identifier
              type: bigint
        - name: cross_sell
          description: "index for cross sell recommendations"
          tags:
            - cross_sell
          properties:
            morphology: stem_en
          columns:
            - name: customer_id
              type: bigint
            - name: customer_segments
              type: text
            - name: customer_segments_key
              type: keyword
            - name: cross_sell_recommendations
              type: text
            - name: id
              description: "mapped to row_num"
              tags:
                - identifier
              type: bigint
      indexers:
        - index_table: customer
          base_sql: |
            SELECT 
              customer_id as id,
              customer_id,
              birth_year,
              education,
              country,
              income
            FROM 
              customer
          options:
            start: 1
            step: 100
            batch_sql: |
              WITH base AS (
                  {base_sql}
              ) start: 1
            step: 1000
            batch_sql: |
              WITH base AS (
                  {base_sql}
              ) SELECT 
                * 
              FROM 
                base 
              WHERE 
                customer_id >= {start} AND customer_id < {end}
            throttle:
              min: 1000
              max: 6000
              factor: 1.2
              jitter: true

        - index_table: cross_sell
          base_sql: |
            SELECT 
              cast(customer_id as bigint) as id,
              cast(customer_id as bigint) as customer_id,
              customer_segments,
              customer_segments as customer_segments_key,
              cross_sell_recommendations
            FROM 
              cross_sell
          options:
            start: 1
            step: 100
            batch_sql: |
              WITH base AS (
                  {base_sql}
              ) start: 1
            step: 1000
            batch_sql: |
              WITH base AS (
                  {base_sql}
              ) SELECT 
                * 
              FROM 
                base 
              WHERE 
                customer_id >= {start} AND customer_id < {end}
            throttle:
              min: 1000
              max: 6000
              factor: 1.2
              jitter: true
```
</details>

## API Endpoint Details

API endpoints are exposed on the `path` defined under the `ingress` section of a Lakesearch Service.

```yaml
{{base_url}}: ${{dataos_context_url}}/lakesearch/${{workspace}}:${{service_name}}
```

## Basic Search Request

A basic search request is a structured query used to retrieve documents from an index based on specific criteria. A user can start searching for the index, keywords, or similar words by accessing the LakeSearch Service API endpoint.

### **GET requests**

GET APIs is generally used to retrive the information without the body. All LakeSearch GET APIs that require a body can be submitted as POST requests.

```yaml
GET https://dataos-training.dataos.app/lakesearch/public:pals/api/v2/index/customer/keywords?word=master
```

Here is the result.

```yaml
{
    "keywords": [
        {
            "docs": "370",
            "hits": "370",
            "keyword": "master"
        }
    ]
}
```

### **POST requests**

A search request is made using an HTTP `POST` request because it contains a body with search parameters. The query must be included in the request body in JSON format.

This table provides a quick reference to the various query types available in LakeSearch API, helping you choose the appropriate query for your data retrieval needs.

| **Query Type**     | **Purpose**                                           | **Key Features**                                                                                                                                   |
|--------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Match**          | Performs full-text search on a specific field.        | - Analyzes input text.<br>- Supports single or multiple fields.<br>- Default operator is OR; can be set to AND.                                   |
| **Match Phrase**   | Searches for exact phrases in a field.                | - Matches terms in the same order.<br>- Supports slop for proximity searches.                                                                      |
| **Query String**   | Allows complex queries with boolean operators and wildcards. | - Supports AND, OR, NOT operators.<br>- Allows wildcards (*, ?, %).<br>- Can specify fields and boost terms.                                       |
| **Filter (Bool Query)** | Combines multiple query clauses using boolean logic.   | - Uses must, must_not, should, and filter clauses.<br>- Filters are cached and do not affect scoring.                                              |
| **Must**           | Ensures all specified conditions are met.             | - Equivalent to logical AND.<br>- Used within bool queries.                                                                                        |
| **Must Not**       | Excludes documents matching specified conditions.     | - Equivalent to logical NOT.<br>- Used within bool queries.                                                                                        |
| **Should**         | At least one of the conditions should match.          | - Equivalent to logical OR.<br>- Influences relevance scoring.                                                                                     |
| **Nested Bool**    | Combines multiple bool queries for complex logic.     | - Allows nesting of bool clauses.<br>- Enables intricate query structures.                                                                         |
| **Range**          | Filters documents within a specified range.           | - Supports numeric, date, and string ranges.<br>- Uses gte, lte, gt, lt operators.                                                                 |
| **Aggregations**   | Groups and analyzes data based on specific attributes.| - Supports terms, range, and statistical aggregations.<br>- Can be used with size=0 to fetch only aggregation results.                             |
| **Buckets**        | Groups data into predefined ranges.                   | - Useful for histograms and range-based analyses.<br>- Each bucket includes a from and to value.                                                   |
| **Highlight**      | Highlights matching terms in the search results.      | - Supports pre_tags and post_tags for customization.<br>- Can specify fields to highlight.                                                         |
| **Expressions**    | Creates dynamic columns via search queries.           | - Columns hold custom logic defined by the user.<br>- These columns can be used to filter data.                                                    |


## Example Scenarios

Explore how the LakeSearch API on DataOS empowers users to perform powerful and intuitive searches across large datasets. Each scenario below demonstrates a practical use case, showcasing how different query types can be executed via the API endpoint.

### **1. Retrieve all records**

A data analyst wants to browse the entire dataset of customer-product affinity to get a sense of the data distribution before applying any filters.

Query:

```json
{
  "query": {
    "match_all": {}
  }
}

```

![match_all.png](/learn/dp_consumer_learn_track/integrate_lakesearch/match_all.png)

### **2. Filter by specific value**

    List customers tagged as "High Risk" to target them for risk-based intervention.

    **Query:**

```json
{
  "query": {
    "match": {
      "customer_segments": "High Risk"
    }
  }
}
```

![high_risk.png](/learn/dp_consumer_learn_track/integrate_lakesearch/high_risk.png)

### **3. Exact phrase match**
    
Find entries where the recommendation is exactly “Pair Wine with Meat”.
    
**Query:**
    
```json
json
CopyEdit
{
    "query": {
    "match_phrase": {
        "cross_sell_recommendations": "Pair Wine with Meat"
    }
    }
}

```
    
![match_phrase.png](/learn/dp_consumer_learn_track/integrate_lakesearch/match_phrase.png)
    

### **4. Highlight matched text (e.g., "Spain")**
    
A marketing analyst needs to identify all customers located in **Spain** to assess regional preferences and engagement.
    
**Query:**
    
```json
{
    "query": {
    "match": {
        "country": "Spain"
    }
    },
    "highlight": {
    "fields": {
        "country": {}
    },
    "pre_tags": ["<mark>"],
    "post_tags": ["</mark>"]
    }
}
```
    
![highlight_pretag.png](/learn/dp_consumer_learn_track/integrate_lakesearch/highlight_pretag.png)
    
### **5. Apply range filter**
    
A marketing analyst wants to analyze customer preferences for those born between **a specific range**, assuming that demographic may behave differently in terms of affinity.
    
**Query:**
    
```json
{
    "query": {
    "range": {
        "birth_year": {
        "gte": 1980,
        "lte": 1990
        }
    }
    }
}
```
    
![range.png](/learn/dp_consumer_learn_track/integrate_lakesearch/range.png)
    
### **6. Add new derived field using expression**
    
The product team wants to estimate the **projected income** by applying a business rule that multiplies a customer's current income by 10. 
    
**Query:**
    
```json
{
    "script_fields": {
    "projected_income": {
        "script": {
        "source": "doc['income'].value * 10"
        }
    }
    },
    "query": {
    "match_all": {}
    }
}
```
    
![add_income.png](/learn/dp_consumer_learn_track/integrate_lakesearch/add_income.png)
    
### **7. Combine filters, derived field and sorting**
    
A marketing analyst wants to analyze data for the customers from a specific country and age group with projected incomes.
    
Query:

```json
{
    "query": {
    "bool": {
        "must": [
        { "match": { "country": "Spain" }},
        { "range": { "age": { "gte": 30, "lte": 40 }}}
        ]
    }
    },
    "sort": [
    { "projected_income": { "order": "desc" }}
    ],
    "script_fields": {
    "projected_income": {
        "script": {
        "source": "doc['income'].value * 10"
        }
    }
    }
}

```
    
![condition_expr_sort.png](/learn/dp_consumer_learn_track/integrate_lakesearch/condition_expr_sort.png)
    

### **8. Multi-Condition filtering**
    
Segment + Recommendation: Get customers who are “Moderate Risk” and have a recommendation involving "Fish".
    
**Query:**
    
```json
{
    "query": {
    "bool": {
        "must": [
        { "match": { "customer_segments": "Moderate Risk" }},
        { "match": { "cross_sell_recommendations": "Fish" }}
        ]
    }
    }
}

```
    
![moderate_risk_fish.png](/learn/dp_consumer_learn_track/integrate_lakesearch/moderate_risk_fish.png)
    
### **9. Show Only Specific Fields**
    
Minimize API response by returning only essential fields. Only return `customer_id` and `cross_sell_recommendations` .
    
**Query:**
    
```json
{
    "_source": ["customer_id", "cross_sell_recommendations"],
    "query": {
    "match_all": {}
    }
}
```

![match_all.png](/learn/dp_consumer_learn_track/integrate_lakesearch/match_all%201.png)

### **10. Perform aggregation**

Get the count per segment: breakdown of how many customers exist in each customer segment.

**Query:**

```json
{
    "size": 0,
    "aggs": {
    "segment_count": {
        "terms": {
        "field": "customer_segments_key",
        "size": 10
        }
    }
    }
}
```
![image](/learn/dp_consumer_learn_track/integrate_lakesearch/agg.png)

### **11. Arrange data for analysis**
    
List all Low Risk customers sorted by `customer_id`.
    
**Query:**
    
```json
{
    "query": {
    "match": {
        "customer_segments": "Low Risk"
    }
    },
    "sort": [
    {
        "customer_id": {
        "order": "asc"
        }
    }
    ]
}
```

![image](/learn/dp_consumer_learn_track/integrate_lakesearch/sort.png)
    

