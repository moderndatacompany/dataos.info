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

`{{base_url}}: <dataos_context_url>/lakesearch/<workspace>:<service_name>`

**Example:** `https://proud-cobra.dataos.app/lakesearch/public:ls-dummy`

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


