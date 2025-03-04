# Architecture of Lakesearch

LakeSearch is a scalable search solution built on top of a Lakehouse (Object Store), providing efficient indexing and retrieval of structured and semi-structured data. The architecture consists of multiple Indexers, which process user-defined indices to enable fast search capabilities. Each indexer interacts with a Search API, which serves as the interface for querying the indexed data.

## Components

### **Search APIs**
The Search APIs provide a standardized interface for querying indexed data, allowing users to perform high-speed searches on structured information. By leveraging pre-built indexes, these APIs minimize query latency and optimize data retrieval. This enables seamless access to critical business insights while maintaining system efficiency.


### **Indexer**

The Indexer is responsible for reading data from the source table and loading it into an object storage location, such as an S3 bucket. This process involves an initial data load followed by ongoing synchronization based on a user-defined schedule. The Indexer monitors changes in the source table and ensures that these changes are replicated in the object storage. Each Indexer is dedicated to a single source table and can be vertically scaled to improve performance as needed.



## LakeSearch Query processing Flow

The query processing in LakeSearch follows a structured workflow, ensuring optimal query execution based on query type and available resources.

<div style="text-align: center;">
  <img src="/resources/stacks/lakesearch/images/qp.jpg" alt="Lakesearch flow" style="border:1px solid black; width: 70%; height: auto;">
</div>

### Query Execution Steps:

2. User Submits a Query: A search query is sent to the LakeSearchAPI (/search).

3. Query Rewriter Check: If a query rewriter is available, the query is rewritten and optimized.Otherwise, the original query is used.

4. Vector Search Processing (if applicable):If the query requires KNN vector search, vector embeddings are generated. If embeddings are already precomputed, this step is skipped.

5. Document Retrieval: The query is executed against the indexed data in the Lakehouse.

6. Response Handling: If an error occurs (e.g., authentication, syntax, timeout), an error response is returned. Otherwise, relevant documents are fetched and returned to the user. This structured approach ensures that search operations are optimized for speed and relevance.

## LakeSearch Index Creation Flow

Index creation in LakeSearch follows a batch-processing model, where indexing occurs in a loop until all batches are processed.

<div style="text-align: center;">
  <img src="/resources/stacks/lakesearch/images/ip.jpg" alt="Lakesearch flow" style="border:1px solid black; width: 70%; height: auto;">
</div>

### Indexing Process:

1. Defining Index Configuration: Users define index mappings in a YAML file, specifying indexing logic. The mapping is deployed via CLI.

2. Batch Processing: The LakeSearch Service allocates resources and starts indexing. The indexer retrieves batches of documents for processing.

3. Vector Embedding Handling: If a vector column is included, the system checks for an available vector embedder. If present, embeddings are generated and stored. If missing, an error is thrown.

4. Document Storage & Updates: Indexed documents are stored in the Lakehouse.Start and end values are updated until indexing is complete.

5. Completion: Once no new documents are found, the indexing process is finalized. This indexing workflow ensures that LakeSearch efficiently processes large datasets while handling structured and unstructured search requirements.



This architecture provides a scalable and cost-effective alternative to traditional full-text search implementations, making it well-suited for enterprise data lake environments.