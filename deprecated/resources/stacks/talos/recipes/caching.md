# Caching Dataset

## Caching Datasets in Talos

Talos provides a caching layer to enhance API query performance and efficiency. By using the `{% cache %}` tag, query results can be retrieved directly from cache storage, minimizing repeated queries to the data source. This section outlines how to configure and utilize caching effectively in Talos.

!!!info
    When using Talos, avoid caching in flash storage, as flash memory inherently performs its own caching.
    

### **1. Caching with an In-Memory Database**

Talos uses an in-memory database as the caching engine, ensuring high-performance query execution. To enable caching, the following configuration must be added to `config.yaml`:

```yaml
cachePath: tmp # by default talos use /tmp as a path but user can provide its own path
sources:
	- name: mysqldepot # source name
	  type: depot # source type
	  options:
	    ssl:               #for mysql depots
	      rejectUnauthorized: true
```

In this configuration, a folder named `tmp` will be created in the root directory of the project to store cached data.

### **2. Caching Query Results**

To leverage caching, SQL queries should be enclosed within `{% cache %}` and `{% endcache %}` tags.

**Example: Using Caching in SQL Queries (`product.sql`)**

```sql
{% cache %}

SELECT DISTINCT prod_id FROM mysql_cache WHERE prod_id = {{ context.params.prod_id}}

{% endcache %}
```

This ensures that results are fetched from the cache layer instead of querying the database repeatedly.

### **3. Configuring Cache Preloading**

Queries can be preloaded into the cache layer by defining cache settings in the configuration file.

**Example: Preloading a Cached Table (`product.yaml`)**

```yaml
urlPath: /mysql/sales/product
description: product from sales
description: validating the functionalities
source: mysqldepot
request:
  - fieldName: prod_id
    fieldIn: query
cache:
  - cacheTableName: 'mysql_cache'   #table name from which cache data will be selected
    sql: select distinct prod_id from mysqldb.mysql_dataset limit 10
    source: mysqldepot

```

This configuration ensures that the `mysql_cache` table is available for cached queries.

### **4. Configuring Cache Refresh Interval**

To refresh cached data periodically, the `refreshTime` or `refreshExpression` setting must be specified in the manifest file.

**Example: Cache Refresh Interval Configuration using `refreshTime`.**

```yaml
cache:
  - cacheTableName: 'mysql_cache' # The name of the table in the cache layer storage
    ...   # remaining attributes like query, source etc
    refreshTime:     # if refreshTime is added then
            every: '5m' # this is mandotry
```

**Example: Cache Refresh Interval Configuration using `refreshExpression`.**

```yaml
cache:
  - cacheTableName: 'mysql_cache'    #The name of the table in the cache layer storage
    ...   # remaining attributes like query, source etc
    refreshExpression: 
            expression: '* * * * *'  #this should be a valid cron expression and should be a string
            timezone: Asia/Kolkata   #Optional 
            runImmediately : true    # boolean value
```

By implementing caching in Talos, query execution times are reduced, and API performance is optimized.