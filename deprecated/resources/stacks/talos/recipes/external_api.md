# How to use external API as a data source?

Developers can utilize external APIs as data sources by defining DuckDB in the `config.yaml` file and invoking the API within SQL queries. By specifying DuckDB as a source, developers can seamlessly integrate external API data into their workflows. This functionality allows for efficient data retrieval directly from APIs, which can then be manipulated using standard SQL, enabling the development of rich, data-driven applications.

Add the below configuration in `config.yaml` to use external API as a data source:

```yaml
sources:
  - name: duckdb
    type: duckdb
```

Developers can access APIs by using the `rest_api(url='')` function within an SQL query, passing the URL of the API endpoint as an argument as shown below. This allows the API response to be treated as a data source, facilitating integration with other data processing operations.

```sql
SELECT {{ {} | rest_api(url='https://dummyjson.com/products/1') }}
```
  