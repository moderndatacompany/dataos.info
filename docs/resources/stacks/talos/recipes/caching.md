# Caching Dataset

The caching layer feature in Talos allows you to leverage caching to improve the performance and efficiency of your API queries. With the `{% cache %}` tag, you can query results directly from the cache layer storage, reducing the need for repeated queries to the data source. Let's explore how to use this feature effectively.

## Caching with in-memory database

To provide efficient caching functionality, Talos utilizes in-memory databse as the underlying storage engine. This ensures high-performance caching and improves the overall query execution speed.

First, you need to add the following configuration to  `config.yaml`

```yaml
cachePath: mycachepath # by default talos use /tmp as a path but you can provide your own path
sources:
  - name: pg # source name
    type: pg # source type
```

In the configuration, `tmp` means there will be a new folder called `tmp` in the root directory of the project you created.

## Caching query results

To utilise the caching layer, you can enclose your SQL query inside the `{% cache %}` and `{% endcache %}` tags. For example:

`product.sql`

```sql
{% cache %}
SELECT
  product_name, item_no
FROM
  product_cache
{% endcache %}
```

This tag enables the query to fetch the result from the cache layer storage. You can define which queries are preloaded into the cache layer by specifying cache settings in the configuration file. Here's an example configuration:

`product.yaml`

```yaml
urlPath: /lens/sales/product
description: product from sales
source: pg
cache:
  - cacheTableName: 'product_cache'
    options: # this is only for Postgres source
      offset: 0
      limit: 50
```

`product_cache.sql` 

```sql
SELECT * FROM product LIMIT ${LIMIT} OFFSET ${OFFSET};
```

In this configuration, the `product_cache` table will be utilised within the `{% cache %}` tag.

Also, you can add the refresh interval configuration in the manifest file in the cache section using the `refreshTime` keyword.

```yaml
cache:
  - cacheTableName: 'cache_departments' # The name of the table in the cache layer storage
    ...
    refreshTime: 
		    every: '5m' # this is mandotry
```

```yaml
cache:
  - cacheTableName: 'cache_departments' # The name of the table in the cache layer storage
    ...
    refreshExpression: 
		    expression: '* * * * *' #this should be a valid cron expression and should be a string
		    timezone: Asia/Kolkata #Optional 
		    runImmediately : true # boolean value  
```

## Reusing cached results

Talos provides the ability to keep the query result from the cache layer in a variable, which can be reused in subsequent queries. For example:

```sql
-- The cached result is stored in the variable named "employee"
{% cache employee %}
SELECT * FROM cache_employees WHERE "id" = {{ context.params.id }};
{% endcache %}

-- The cached result can be reused in subsequent queries by referencing the variable name "employee"
SELECT * FROM departments WHERE "employee_id" = {{ employee.value()[0].id }};
```

By assigning the result of the `{% cache %}` tag to the `employee` variable, you can access its value in subsequent queries. This allows you to build complex queries by utilizing the cached results. Note that when the `{% cache %}` tag does not have a variable assigned, it retrieves the result directly from the cache builder.