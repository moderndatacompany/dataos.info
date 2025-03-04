LakeSearch is designed to provide scalable, high-performance full-text search capabilities for Lakehouse tables.

The idea is to decouple storage and compute resources (in upcoming releases), LakeSearch would offer flexibility in scaling based on the specific demands of the workload. This approach enables businesses to optimize both performance and cost efficiency, making it ideal for environments where high-performance search is critical but current solutions are too costly and rigid.

Presently, LakeSearch is deployed as a Stack, similar to Flash. In the later stages, it will evolve into a fully scalable cluster architecture, allowing for fine-tuned control over Indexer and Searcher scaling. This flexibility will cater to both, small and large deployments, offering high availability and cost-efficiency at scale.

![LakeSearch Architecture](attachment:cb7ba211-c06f-4e36-bbd9-7b7da3fcefca:image.png)

LakeSearch Architecture

## Indexing a Table

A Lakesearch index is a logical namespace that holds a collection of documents, where each document is a collection of fields. These fields are key-value pairs that contain actual data. It acts as a collection or a structure that organizes the underlying data into a searchable format. The structure is optimized to handle large datasets, making full-text search and complex queries faster.

When you index a document, the system creates an inverted index, a specialized data structure that maps each term or keyword in your data to the documents containing those terms. This enables efficient searching by reducing the amount of data that must be scanned for a query.

An inverted index is a data structure that maps content, such as words or terms, to their locations within a dataset, such as documents. This is the opposite of a traditional forward index, which maps documents to the terms they contain.

### Creating an Index

An index is made up of multiple documents, similar to rows in a database, where each document consists of fields and values, representing different attributes. A mapping describes the structure of the documents and specifies data types (e.g., text, number, date, etc.) for each field.

The **columns** section defines how the documents and their fields are indexed and searched. Mapping allows users to control the structure of their data and specify how individual fields should behave during searching.

- Supported Data Types
    
    
    | Data Type | Description | Category |
    | --- | --- | --- |
    | `text` | The text data type forms the full-text part of the table. Text fields are indexed and can be searched for keywords. | full-text field |
    | `keyword` | Unlike full-text fields, string attributes are stored as they are received and cannot be used in full-text searches. Instead, they are returned in results, can be used to filter, sort and aggregate results. In general, it's not recommended to store large texts in string attributes, but use string attributes for metadata like names, titles, tags, keys, etc. | attribute |
    | `int` | Integer type allows storing 32 bit **unsigned** integer values. | attribute |
    | `bigint` | Big integers (bigint) are 64-bit wide **signed** integers. | attribute |
    | `bool` | Declares a boolean attribute. It's equivalent to an integer attribute with bit count of 1. | attribute |
    | `timestamp` | The timestamp type represents Unix timestamps, which are stored as 32-bit integers. The system expects a date/timestamp type object from the base_sql. | attribute |
    | `float` | Real numbers are stored as 32-bit IEEE 754 single precision floats. | attribute |
    | `vector` | Vector embedding generated as per the defined vector embedder logic. | full-text field |
- Example
    
    ```yaml
    columns:
      - name: row_num
        type: bigint
      - name: id
        description: "mapped to row_num"
        tags:
          - identifier
        type: bigint
      - name: device_id
        type: text
      - name: org_id
        type: keyword
      - name: device_name
        type: text
      - name: serial_number
        type: bigint
      - name: model_type
        type: text
      - name: family
        type: text
      - name: category
        type: keyword
      - name: model_name
        type: text
      - name: platform
        type: keyword
      - name: platform_vector
        type: vector
        knn:
          knn_dims: 384
          hnsw_similarity: l2
          hnsw_m: 16
      - name: manufacturer
        type: text
      - name: subscription_id
        type: text
      - name: created_at
        type: timestamp
      - name: updated_at
        type: timestamp
      - name: is_active
        type: bool
      - name: _deleted
        type: bool
    ```
    

**Defining Columns for Vector Indexing**

To enable vector-based search, specific columns must be indexed as vectors. The following configuration indexes the `platform_vector` column with vector-based search parameters:

```yaml
columns:
  - name: platform_vector
    type: vector
    knn:
      knn_dims: 384
      hnsw_similarity: l2
      hnsw_m: 16
```

Explanation of Parameters:

- **knn_dims**: Specifies the dimensionality of the vector embeddings (e.g., 384).
- **hnsw_similarity**: Determines the distance function for similarity search. Supported values:
    - `L2`: Squared L2 distance (Euclidean distance)
    - `IP`: Inner product
    - `COSINE`: Cosine similarity
- **hnsw_m**: Defines the maximum number of outgoing connections in the HNSW graph (default: 16).

### Defining batch

The indexing process is done in multiple batches. These batches are defined by the user using simple SQL queries and configuring the following parameters: 

- The `start` value specifies the starting point for batch processing.
- The `step` value defines the batch size.
- The `start` and `step` will be summed dynamically to calculate the `end` value, which can be used in the batch SQL logic.
- The system should ensure incremental updates to the `start` and `end` values during batch processing.

Furthermore, users can also throttle the system to control the batch execution:

- `min`: The minimum time(in ms) the system would wait before triggering a new batch.
- `max`: The maximum time(in ms) the system would wait before triggering a new batch.
- `factor`: This defines the factor by which the waiting time would increase (until it reached `max`).
- `jitter`: This is of type bool. It introduces randomness.
- Example
    
    ```yaml
    options:
    		start: 1735084800
    		step: 86400
    		batch_sql: |
    		  WITH base AS (
    		      {base_sql}
    		  ) SELECT 
    		    * 
    		  FROM 
    		    base 
    		  WHERE 
    		    epoch(updated_at) >= {start} AND epoch(updated_at) < {end}
    		throttle:
    		  min: 10000
    		  max: 60000
    		  factor: 1.2
    		  jitter: true
    ```
    

### API Endpoints

- To perform a search, users can send a POST request to the Lakesearch API: `{{base_url}}/api/v2/index/:index_name/search`
- To fetch the vector embedding created for a value, users can send a POST request to the Lakesearch API: `{{base_url}}/api/v2/embedding`

Where, 

- `{{base_url}}` is `<dataos_context_url>/lakesearch/<workplace>:<service_name>`
- `index_name` is the name of the index defined in the service config

Complete list of all API endpoints exposed can be found [here](https://www.notion.so/Lakesearch-v2-API-Endpoints-160c5c1d487680f19f91c0e21a9a2b7e?pvs=21).

### Searching an Index

- Simple Search
    
    A basic search request involves querying an index based on specific criteria to retrieve documents. Here is an outline of the key parameters:
    
    1. `query`: Specifies the search conditions for fetching documents from the index. For example, it might filter for documents with a particular job (e.g., *UX Designer*) and those where the address field includes the word *Sigrid*. This is a **mandatory** parameter.
    2. `limit`: Defines the maximum number of documents to return. This is an **optional** parameter. Alternatively, `size` can also be used for this purpose.
    3. `_source`: Specifies an array of fields to return in the search results, similar to the `select` clause in SQL. This is an **optional** parameter.
        1. If this is not defined, all the available attributes are fetched.
        2. You can also use `exclude` and `include` to define the attributes returned in the response payload.
    4. `sort`: An array of fields to define the sorting order of the results, similar to the `order by` clause in SQL. This is an **optional** parameter.
    - Example
        
        ```yaml
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
            },
            "limit": 10,
            "_source": {
                "excludes": [
                    "phone_number",
                    "customer_name"
                ]
            },
            "sort": [
                {
                    "@timestamp": "desc"
                },
                {
                    "birthdate": "asc"
                }
            ]
        }
        ```
        
- KNN Vector Search
    
    Once vectors are generated and indexed, users can leverage KNN search to perform similarity-based queries. We utilize an HNSW (Hierarchical Navigable Small World) index for efficient KNN searches, enabling fast and accurate retrieval of similar vectors.
    
    Each vector search request must include the following parameters:
    
    ```json
    {
      "field": "platform_vector",
      "k": 10,
      "query": "Windows"
    }
    ```
    
    Explanation of Query Parameters:
    
    - **field**: The name of the vector attribute being searched.
    - **k**: The number of nearest neighbors to retrieve. Note that the actual number of returned documents may vary due to filtering.
    - **query_vector**: The vector representation used as the search query; OR
    - **query:** You can also perform a vector search via the actual value of the column.
    - **ef** (optional): The dynamic list size used during the search. A higher `ef` leads to a more accurate but slower search.

More details can be found [here](https://www.notion.so/Searching-an-Index-15fc5c1d4876803cadfec2bc9790d2a6?pvs=21).