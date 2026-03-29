# Endpoint details

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


To get more information on index searching, please refer to [this link](resources/stacks/lakesearch/index_searching/).

<!-- ### **KNN Vector Search**

This is an AI-powered search that finds results based on meaning rather than exact words. It works with vector embeddings (numerical representations of text) to locate similar content.

- `knn` is a vector query that allows searching for vectors in indexed documents.
- It accepts regular values and uses the same vector embedding model (that was used to create vector embedding while indexing) to generate dynamic vectors and search the indexed documents against it.
- **Parameters:**
    1. `field`: This is the name of the float vector attribute containing vector data.
    2. `k`: This represents the number of documents to return and is a key parameter for Hierarchical Navigable Small World (HNSW) indexes. It specifies the quantity of documents that a single HNSW index should return. However, the actual number of documents included in the final results may vary.
    3. `query`: This is the search term.
    4. `ef`: Optional size of the dynamic list used during the search. A higher **`ef`** leads to more accurate but slower search.

**Syntax:**

```json
{
    "knn": {
        "field": "<name of the vectorized field>",
        "k": <positive integer>,
        "query": "<search_term>"
}
```

**Example:**
    
```json
{
    "knn": {
        "field": "platform_vec",
        "k": 10,
        "query": "Android"
}
```
     -->
