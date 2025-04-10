---
title: Lakesearch
search:
  boost: 4
---

# LakeSearch Stack

LakeSearch is a [Stack](/resources/stacks/) within DataOS that provides the scalable [full-text search](/resources/stacks/lakesearch/key_concepts/#full-text-search) solution for the DataOS Lakehouse. It allows app developers to enable full-text search on top of [DataOS Lakehouse](/resources/lakehouse/) tables with an ability to scale the [indexing](/resources/stacks/lakesearch/key_concepts/#indexer) and searching capabilities to meet business requirements.


The examples below illustrate the search functionality of LakeSearch where a user can access the API endpoint.

**Scenario:**

A travel application integrates LakeSearch to enhance its location-based services. Users can search for cities, states, or ZIP codes to find relevant information, such as weather, attractions, or available accommodations. Below is how LakeSearch works in this scenario.

- Users can search for cities, states, or ZIP codes. When a user starts typing "Alab" in the search bar, the system suggests "Alabama" as a keyword, improving the search experience through autocomplete functionality.

    <details>
    <summary>Search with auto-suggest</summary>
    Endpoint: `https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/city/words?word=alab*&limit=3`

    ```json
    # Result
    {
    "keywords": [
        {
        "docs": "767",
        "hits": "767",
        "keyword": "alabama"
        }
    ]
    }
    ```
    </details>

- In cases where a user mistypes a search term, LakeSearch suggests similar words to help refine the query. For example, if the user types "auta" instead of "Autauga," the system provides suggestions like "Utah," "South," and "Dakota," ensuring accurate search results even with minor spelling errors.

    <details>
    <summary>Search by similar word</summary>

    Endpoint: `https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/city/suggestions?word=auta`

    ```json
    # Result
    {
        "suggestions": [
            {
                "distance": 2,
                "docs": 339,
                "suggestion": "utah"
            },
            {
                "distance": 3,
                "docs": 1806,
                "suggestion": "south"
            },
            {
                "distance": 3,
                "docs": 1566,
                "suggestion": "dakota"
            }
        ]
    }
    ```
        
    </details>

## Features of LakeSearch

Following are the features of Lakesearch:

- **[Full-text search](/resources/stacks/lakesearch/key_concepts/#full-text-search):** Build a fast, relevant full-text search solution using inverted indexes, tokenization, and text analysis.

- **Semantic search:** Understand the intent and contextual meaning behind search queries.

- **Build search experiences:** Add search capabilities to apps or websites, or build enterprise search engines over your organization’s internal data sources.



## LakeSearch Architecture

LakeSearch follows a Master-Slave architecture, a design pattern commonly used for scalability, load balancing, and high availability.

<div style="text-align: center;">
  <figure>
    <img src="/resources/stacks/lakesearch/images/lsarch.jpg" 
         alt="LakeSearch architecture" 
         style="border: 1px solid black; width: 60%; height: auto; display: block; margin: auto;">
    <figcaption style="margin-top: 8px; font-style: italic;">LakeSearch architecture</figcaption>
  </figure>
</div>

### **Master node**

The Master node is responsible for indexing data, processing queries, and managing search operations. It extracts and processes raw data from the DataOS Lakehouse, converting it into an indexed format for efficient searching. When a search request is received, the Master node processes it and distributes the workload to Slave nodes if needed. Additionally, it manages the overall cluster by synchronizing indexed data across Slave nodes, ensuring consistency. The Master node also plays a key role in storage, saving indexed documents in an object store for quick and reliable retrieval.

### **Slave node**

The Slave node supports the Master node by handling search queries, ensuring smooth performance through load balancing. In case of a failure in the Master node, the Slave node can take over search operations, acting as a failover mechanism to maintain system availability. By distributing query loads and ensuring data redundancy, the Slave node enhances the overall reliability and scalability of the system.

### **Object store**

Indexed Document Storage (Object store - e.g. S3) stores indexed data, ensuring quick and efficient retrieval. It provides persistence, meaning the data remains intact even if nodes restart or fail. By leveraging an object store (e.g. S3), the system guarantees durability and scalability, enabling seamless access to indexed documents whenever needed.


## LakeSearch query processing flow

The query processing in LakeSearch follows a structured workflow, ensuring optimal query execution based on query type and available resources.

<!-- <div style="text-align: center;">
  <img src="/resources/stacks/lakesearch/images/qp.jpg" alt="LakeSearch flow" style="border:1px solid black; width: 80%; height: auto;">
</div> -->

### **Query execution steps**

2. **User submits a query:** A search query is sent to the Lakesearch API (/search).

3. **Query rewriter check:** If a query rewriter is available, the query is rewritten and optimized. Otherwise, the original query is used.

5. **[Document](/resources/stacks/key_concepts/#documents) retrieval:** The query is executed against the indexed data in the Lakehouse.

6. **Response handling:** If an error occurs (e.g., authentication, syntax, timeout), an error response is returned. Otherwise, relevant documents are fetched and returned to the user. This structured approach ensures that search operations are optimized for speed and relevance.

## LakeSearch index creation flow

Index creation in LakeSearch follows a batch-processing model, where indexing occurs in a loop until all batches are processed.

<!-- <div style="text-align: center;">
  <img src="/resources/stacks/lakesearch/images/ip.jpg" alt="LakeSearch flow" style="border:1px solid black; width: 70%; height: auto;">
</div> -->

### **Indexing process**

1. **Defining index configuration:** Users define index mappings in a YAML file, specifying the indexing logic. These mappings determine how data records are structured and stored. The configuration is deployed via the CLI.

2. **Batch processing:** The LakeSearch Service allocates resources and initiates the indexing process. The indexer retrieves data records in batches, processes them into documents, and stores them in object storage (Persistent Volume Claim) in the form of inverted indices.

4. **Document storage & updates:** Once processed, the indexed documents are stored in object storage (PVC). The system tracks progress throughout the indexing process to ensure consistency and completeness.

5. **Completion:** The indexing process continues until all available data records have been processed. Once no new data records are detected, the process completes, ensuring that the indexed data is fully available for search operations.



This architecture provides a scalable and cost-effective alternative to traditional full-text search implementations, making it well-suited for enterprise data lake environments.


## Structure of LakeSearch Service manifest file

<div style="text-align: center;">
  <figure>
    <img src="/resources/stacks/lakesearch/images/ls.jpg" alt="LakeSearch Service structure" style="border:1px solid black; width: 100%; height: auto;">
    <figcaption style="margin-top: 8px; font-style: italic;">LakeSearch Service Structure</figcaption>
  </figure>
</div>


<!-- ## How to deploy LakeSearch Stack within DataOS?

The Stack is deployed by a DataOS operator. Before starting the deployment of LakeSearch Stack within DataOS, check if it already exists by executing the below command, which will list all the deployed Stacks within the DataOS environment along with their flavor, version, and image:

```bash
dataos-ctl develop stack versions 
```

<details>
    <summary>Expected output</summary>

    ```bash
        STACK      │ FLAVOR  │ VERSION │                       IMAGE                       │     IMAGE PULL SECRET      
    ──────────────────┼─────────┼─────────┼───────────────────────────────────────────────────┼────────────────────────────
    beacon          │ graphql │ 1.0     │ docker.io/rubiklabs/beacon:postgraphile-4.10.0.d1 │ dataos-container-registry  
    beacon          │ rest    │ 1.0     │ docker.io/postgrest/postgrest:v12.2.3             │ dataos-container-registry  
    bento           │         │ 3.0     │ docker.io/rubiklabs/bento4:0.0.49                 │ dataos-container-registry  
    bento           │         │ 4.0     │ docker.io/rubiklabs/bento4:0.0.49                 │ dataos-container-registry  
    bundlebento     │         │ 4.0     │ docker.io/rubiklabs/bento-ds:0.8.28               │ dataos-container-registry  
    container       │         │ 1.0     │                                                   │                            
    dataos-ctl      │         │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.39            │ dataos-container-registry  
    dataos-resource │ apply   │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.39            │ dataos-container-registry  
    dataos-resource │ delete  │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.39            │ dataos-container-registry  
    dataos-resource │ run     │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.39            │ dataos-container-registry  
    dlthub          │ python  │ 1.0     │ docker.io/rubiklabs/dataos-dlthub:0.0.8-dev       │ dataos-container-registry  
    dlthub          │ python  │ 1.0     │ docker.io/rubiklabs/dataos-dlthub:0.0.8-dev       │ dataos-container-registry  
    flare           │         │ 5.0     │ docker.io/rubiklabs/flare5:7.3.18                 │ dataos-container-registry  
    flare           │         │ 6.0     │ docker.io/rubiklabs/flare6:8.0.26                 │ dataos-container-registry  
    flash           │ python  │ 4.0     │ docker.io/rubiklabs/flash:0.0.37-dev              │ dataos-container-registry  
    flash           │ python  │ 1.0     │ docker.io/rubiklabs/flash:0.0.44-dev              │ dataos-container-registry  
    LakeSearch      │         │ 2.0     │ docker.io/rubiklabs/lakesearch:0.3.3-exp.01       │ dataos-container-registry  
    LakeSearch      │         │ 3.0     │ docker.io/rubiklabs/lakesearch:0.2.6-exp.05       │ dataos-container-registry  
    LakeSearch      │         │ 4.0     │ docker.io/rubiklabs/lakesearch:0.3.3-exp.02       │ dataos-container-registry  
    LakeSearch      │         │ 5.0     │ docker.io/rubiklabs/lakesearch:0.3.3              │ dataos-container-registry  
    LakeSearch      │         │ 6.0     │ docker.io/rubiklabs/lakesearch:0.3.4              │ dataos-container-registry  
    nilus-cdc       │         │ 1.0     │ docker.io/rubiklabs/nilus-cdc:0.0.0-exp.01        │ dataos-container-registry  
    scanner         │         │ 2.0     │ docker.io/rubiklabs/scanner:4.8.26                │ dataos-container-registry  
    scanner         │         │ 1.0     │ docker.io/rubiklabs/dataos-scanner:0.1.28         │ dataos-container-registry  
    soda            │ python  │ 1.0     │ docker.io/rubiklabs/dataos-soda:0.0.30            │ dataos-container-registry  
    soda            │ python  │ 2.0     │ docker.io/rubiklabs/dataos-soda:0.0.27-dev        │ dataos-container-registry  
    stream-monitor  │         │ 1.0     │ docker.io/rubiklabs/monitor-api:0.17.2            │ dataos-container-registry  
    ststack         │ python  │ 1.0     │ docker.io/library/python:3.10.12-slim             │                            
    talos           │         │ 1.0     │ docker.io/rubiklabs/talos:0.1.26                  │ dataos-container-registry  
    talos           │         │ 2.0     │ docker.io/rubiklabs/talos:0.1.25                  │ dataos-container-registry  
    ```

</details>

Remember that only the user with an ‘operator’ tag can execute the above command. If you do not find the LakeSearch in the result, it is time to deploy the Stack. Follow [this link](/resources/stacks/lakesearch/deployment/) for steps to deploy the Stack.  -->


## How to set up a LakeSearch Service?

Once the LakeSearch Stack is available, follow the steps given in the links below to create a LakeSearch Service . The LakeSearch Service retrieves data from the source and indexes each column from one or multiple tables, making it searchable.

- [LakeSearch Service](/resources/stacks/lakesearch/service/)
- [LakeSearch Service with query rewriter](/resources/stacks/lakesearch/rewriter/)
<!-- - [LakeSearch Service with vector embedding](/resources/stacks/lakesearch/vector_embedding/) -->

For a detailed breakdown of the configuration options and attributes of a LakeSearch Service, please refer to the documentation: [Attributes of LakeSearch Service manifest](/resources/stacks/lakesearch/configurations/).

## How to perform index-based searches?

A user can start searching for the index, keywords, or similar words by accessing the LakeSearch Service API endpoint. Some basic index searching is given below, to know in detail about index searching, please refer [to this link](/resources/stacks/lakesearch/index_searching/).

### **Searching for an index**

A user can access the endpoint either by curl command or using any API platform.

- To get the list of all the indices, a user can execute the following curl command in the terminal.
    
    ```bash
    curl -X GET "https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index" \                           
    -H "Authorization: Bearer dG9rZW5fZGlzdhlkg3RseV9tYWlubHlfdXBlkmF5LjU1ZmE1ZWQyLWUwNDgtNGI3Yi1hNGQ2LWNlNjA1YTAzZTE4YQ=="
    ```
    
    Expected output:
    
    ```json
    [
        "__indexer_state",
        "city"
    ]
    ```
    
- To get the details of an individual index by name execute the below curl command.
    
    ```bash
    curl -X GET "https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/city/search" \
    -H "Authorization: Bearer dG9rZW5fZGlzdGluY3Rhklf9tYWlubHlfdXBfklF5LjU1ZmE1ZWQyLWUwNDgtNGI3Yi1hNGQ2LWNlNjA1YTAzZTE4YQ=="
    ```
    
    Expected output:
    
    ```bash
    {
        "took": 0,
        "timed_out": false,
        "hits": {
            "total": 1,
            "total_relation": "gte",
            "hits": [
                {
                    "_id": 36003,
                    "_score": 1,
                    "_source": {
                        "state_name": "Alabama",
                        "version": "202501090702",
                        "@timestamp": 1739964871,
                        "city_id": "CITY6",
                        "zip_code": 36003,
                        "city_name": "Autaugaville",
                        "county_name": "Autauga County",
                        "state_code": "AL",
                        "ts_city": 1736406148
                    }
                }
            ]
        }
    }
    ```
    

### **Searching for a keyword**

To search by the exact keyword execute the following curl command.

```bash
curl -X GET "https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/city/keywords?word=alabama" \ 
-H "Authorization: Bearer dG9rZW5fZGlzdGluY3RseV9tYWlubHlfdXBfcmFU1Zlo1ZWQyLWUwNDgtNGI3Yi1hNGQ2LWNlNjA1YTAzZTE4YQ=="
```

Expected output:

```bash
{
    "keywords": [
        {
            "docs": "767",
            "hits": "767",
            "keyword": "alabama"
        }
    ]
}
```

### **Searching for a similar word**

To search by the similar word execute the following curl command.

```bash
curl -X GET "https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/city/suggestions?word=alaba&limit=2" \
-H "Authorization: Bearer dG9rZW5fZGlzluY3RseV9tYWlubHlfcmF5LjU1ZmE1ZWQyLWplNDgtNGI3Yi1hNGQ2LWNlNjA1YTAzZTE4YQ=="

```

Expected output:

```json
{
    "suggestions": [
        {
            "distance": 2,
            "docs": 767,
            "suggestion": "alabama"
        },
        {
            "distance": 4,
            "docs": 90,
            "suggestion": "island"
        }
    ]
}
```


## Managing deleted records in Lakesearch

When records that have already been indexed in LakeSearch are deleted from the source table, they remain accessible through the search API unless explicitly handled. To manage this, LakeSearch supports **soft deletes**, ensuring that deleted records are appropriately excluded from search results.

### **Soft delete mechanism**

LakeSearch relies on two additional columns in the Lakehouse table:

1. **`_delete` (Boolean)** – Tracks whether a record should be considered deleted. By default, all records have `_delete = false`.
2. **Timestamp column** (e.g., `updated_at` or `last_modified_date`) – Records the last modification time.

When a record needs to be removed from search results:

- It is marked as **`_delete = true`**.
- The `updated_at` timestamp is refreshed to reflect the change.

This ensures that LakeSearch recognizes the update and removes the record from indexed search results.

### **Handling hard deletes**

If a record is permanently deleted from the source table, a mechanism must be in place to update `_delete = true` in the corresponding Lakehouse table record. If this update is **not** performed, LakeSearch remains unaware of the deletion, and the record will still be retrievable via the search API.

By implementing this process, LakeSearch ensures data consistency while allowing controlled deletion without losing historical traceability.

## Best practices

This section involves recommends dos and don’ts while configuring a LakeSearch Service.

- For large datasets, always use the partition indexer when configuring the LakeSearch Service. It divides the indexes into two parts, significantly reducing the time required to index all tables.

- The persistent volume size should be at least 2.5 times the total dataset size, rounded to the nearest multiple of 10. To check the dataset size, use the following query:

    ```sql
    SELECT sum(total_size) FROM "<catalog>"."<schema>"."<table>$partitions";
    ```
    The resultant size will be in the bytes.

## Trobleshooting

In case of any issues while using LakeSearch, refer to the [troubleshooting section](/resources/stacks/lakesearch/troubleshooting/) for common errors, solutions, and debugging steps. This section covers potential failures related to indexing, query processing, and node synchronization, along with recommended fixes to ensure smooth operation.


## FAQs

This section contains the answers to common questions about LakeSearch.


<details>
    <summary>What is the difference between indexing in relational databases and indexing in full-text search solutions?</summary>

Indexing in Relational Databases (RDBMS) and Full-Text Search Solutions serve different purposes and work differently. Here's a comparison:

<table>
<tr>
<th>Feature</th>
<th>Relational Database Indexing</th>
<th>Full-Text Search Indexing</th>
</tr>
<tr>
<td><b>Purpose</b></td>
<td>Speeds up exact-match lookups and range queries in structured data.</td>
<td>Enables fast, efficient searching in large volumes of unstructured text data.</td>
</tr>
<tr>
<td><b>Data Type</b></td>
<td>Works best for structured, tabular data (numbers, dates, strings).</td>
<td>Optimized for text-based data with complex search requirements.</td>
</tr>
<tr>
<td><b>Index Structure</b></td>
<td>Uses B-Trees, Hash Indexes, or Bitmap Indexes.</td>
<td>Uses <b>Inverted Index</b>, where words are mapped to their locations in documents.</td>
</tr>
<tr>
<td><b>Query Type</b></td>
<td>Supports exact matches (<code>=</code>, <code>LIKE 'abc%'</code>, <code>BETWEEN</code>).</td>
<td>Supports full-text searches (<code>MATCH() AGAINST()</code>, tokenization, stemming).</td>
</tr>
<tr>
<td><b>Sorting & Ranking</b></td>
<td>Typically retrieves results in the order of insertion or by indexed columns.</td>
<td>Returns ranked results based on relevance scoring (e.g., TF-IDF, BM25).</td>
</tr>
<tr>
<td><b>Updates & Performance</b></td>
<td>Index updates are costly but required for integrity constraints.</td>
<td>Updates are optimized for incremental changes but can be computationally expensive.</td>
</tr>
<tr>
<td><b>Use Case</b></td>
<td>Searching for exact records, foreign key lookups, and range queries.</td>
<td>Searching for words, phrases, synonyms, and fuzzy matches in large text corpora.</td>
</tr>
</table>

<p><strong>Example:</strong></p>
<ul>
    <li><strong>RDBMS Indexing:</strong> A database indexing a <code>customer_id</code> for fast lookup in a table.</li>
    <li><strong>Full-Text Search Indexing:</strong> A search engine indexing millions of articles to find relevant ones based on a keyword search.</li>
</ul>

</details>


