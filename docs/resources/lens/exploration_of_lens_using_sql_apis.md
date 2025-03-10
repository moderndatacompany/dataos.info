# Exploration of Lens using SQL APIs

Lens exposes a PostgreSQL-compatible interface, enabling interaction with the semantic model(Lens) using SQL API. The PostgreSQL client tool `psql` is required to query the semantic model.

## Prerequisites

- **Active Lens:** Ensure the Lens is active and properly set up if deployed on DataOS to interact with it.

- **DataOS API Key:** When prompted for a password, use the DataOS API Key as the password. To retrieve the API Key, run the following command in the terminal:

    ```bash
    dataos-ctl user apikey get

    #Expected Output

    TOKEN                                                   │  TYPE  │        EXPIRATION         │                   NAME                     
    ───────────────────────────────────────────────────────────────────────────────────────────────────────────┼────────┼───────────────────────────┼────────────────────────────────────────────
    dG9rZW5fdXJnZW50bHlfZ2VuZXJhbGx5X2J1cnN0aW5nX2dvYmJsZXIuOGU1Yjg5MDktZjk5My00ZDkyLTkzMGQtZTMxZDYxYTRhMjAz │ apikey │ 2024-12-06T05:30:00+05:30 │ token_urgently_generally_bursting_gobbler  
    ```

    If the API Key is not already available, create one using the following command:

    ```bash
    dataos-ctl user apikey create -n ${name-of-apikey} -i ${user-id} -d ${duration}
    ```

    For example, if the user name is iamgroot:

    ```bash
    dataos-ctl user apikey create -n test_api_key -i aayushisolanki -d 24h

    #Expected_Output
    INFO[0000] 🔑 user apikey...                             
    INFO[0003] 🔑 user apikey...complete                     

                                    TOKEN                                 │  TYPE  │        EXPIRATION         │     NAME      
    ───────────────────────────────────────────────────────────────────────┼────────┼───────────────────────────┼───────────────
    dGVzdF9hcGlfa2V5LjZjYmE2Nzg0LTIyNDktNDBjMy1hZmNhLTc1MmZlNjM3OWExZA== │ apikey │ 2024-11-29T12:30:00+05:30 │ test_api_key  
    ```

To interact with Lens, the following options are available:

- **Postgreql client (psql):** The `psql` command-line tool enables direct interaction with a PostgreSQL database. It is used to run queries, manage the database, and perform various administrative tasks. Ensure that postgresql-client-16 is installed. If it is not already installed, download and install postgresql-client-16 for your operating system using [this link](https://www.postgresql.org/download/).

- **VS Code extension:** Use the PostgreSQL Client extension for Visual Studio Code. This extension enables SQL query execution and database management within VS Code.

## Postgresql client (psql)

The `psql` command-line tool is required to interact with Lens through PostgreSQL. Specifically, `postgresql-client-16` must be installed, as this version includes the necessary tools to connect and query the semantic model. 

### **Retrieve Lens**

Before using SQL APIs to explore a Lens, the Lens needs to be retrieved from the workspace. This can be done in different ways depending on whether the Lens is running locally or is deployed on DataOS.

If a user has created a Lens, verify its name in the `deployment.yml` file or retrieve it by running the following command:

=== "Command"

    ```bash
    dataos-ctl resource get -t lens -w ${workspace} 
    ```
=== "Example"

    ```bash
    # For a workspace named "curriculum", the command and its expected output are as follows:
    dataos-ctl resource get -t lens -w curriculum
    # Expected Output
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             

                NAME             | VERSION |  TYPE   | WORKSPACE  | STATUS |   RUNTIME   |     OWNER        
    -------------------------------|---------|---------|------------|--------|-------------|-------------------
            productaffinity              | v1      | cluster | curriculum | active | running:1   |     ironman  
    ```

To explore the Lens created by someone else in a particular worksapce use the following command:

=== "Command"

    This command requires specifying the workspace name to filter the Lens accordingly.

    ```bash
    dataos-ctl resource get -t lens -w ${workspace} -a
    ```

=== "Example"

    ```bash
    # For a workspace named "curriculum", the command and its expected output are as follows:
    dataos-ctl resource get -t lens -w curriculum -a
    # Expected Output
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             

                NAME             | VERSION |  TYPE   | WORKSPACE  | STATUS |   RUNTIME   |     OWNER        
    -------------------------------|---------|---------|------------|--------|-------------|-------------------
            sales-analysis               | v1      | cluster | curriculum | active | running:1   |     ironman  
            productaffinity             | v1      | cluster | curriculum | active | running:2   |     thanos  
    ```


### **Connect to Lens using `psql`**

After retrieving the name of the Lens, the following steps describe how to connect to it using the `psql` command. Again, the host parameter depends on whether the Lens is running locally or deployed on DataOS.


1. Open the terminal.

2. Use the following command to connect to the Lens using `psql`:
    
    ```bash
    psql -h ${host_name} -p 6432 -U ${user-name} -d ${lens:<workspace-name>:<lens-name>} 
    ```
    
    For deployed environment, use the following connection string:
    
    ```bash
    psql -h tcp.liberal-monkey.dataos.app -p 6432 -U iamgroot -d lens:curriculum:product360
    ```
    Replace <context> with the appropriate context for the deployed Lens. For example, in `liberal-monkey.dataos.app`, the context is `liberal-monkey`. Additionally, replace the workspace name with the name of the actual workspace where Lens is deployed. For instance, `public`, `sandbox` etc.

3. When prompted, enter the DataOS API Key as the password.

4. The connection is successful. Verify the connection by listing the available relations using the `\dt` command:
    
    ```sql
    iamgroot=> \dt
    ```
    
    **Expected output**
    
    ```bash
    Password for user iamgroot: 
    psql (16.3 (Ubuntu 16.3-1.pgdg22.04+1), server 14.2 (Lens2/sales400 v0.35.41-01))
    Type "help" for help.
    
    iamgroot=> \dt
                    List of relations
     Schema |          Name           | Type  |     Owner      
     --------+-------------------------+-------+----------------
     public | customer                | table | aayushisolanki
     public | customer_lifetime_Value | table | aayushisolanki
     public | product                 | table | aayushisolanki
     public | repeat_purchase_rate    | table | aayushisolanki
     public | sales                   | table | aayushisolanki
     public | stock_status            | table | aayushisolanki
     public | warehouse_inventory     | table | aayushisolanki
     (7 rows)
    ```
    
5. To exit `psql`, type:
    
    ```sql
    iamgroot=> \q
    ```

## Postgresql VS Code extension

One can also use the PostgreSQL extension on VS Code. Use the following details to connect to the Postgresql interface:

1. Install the PostgreSQL Client extension.

2. Click the 'Create Connection' button on the left side panel.

3. Configure the connection with the following details and click '+connect':

    | **POSTGRES PROPERTY** | **DESCRIPTION** | **EXAMPLE** |
    | --- | --- | --- |
    | Host  | host name | `localhost` |
    | Port | port name | `25432` |
    | Database | database name | `postgres` |
    | Username | dataos-username | `postgres` or `iamgroot` |
    | Password | dataos-user-apikey | `dskhcknskhknsmdnalklquajzZr=` |

4. Once connected, hover over the postgres folder and click the terminal icon to open the terminal for querying.

5. Execute queries in the terminal as needed. For example:

```bash
postgres=> \dt #listing all the tables in the connected database.

#Expected_output
 Schema |         Name         | Type  |  Owner   
--------+----------------------+-------+----------
 public | channel              | table | postgres
 public | customer             | table | postgres
 public | product_analysis     | table | postgres
 public | products             | table | postgres
 public | transaction_analysis | table | postgres
 public | transactions         | table | postgres
(6 rows)
```

## Commands

One can also introspect the semantic model in a Postgres-native way by querying tables or using backslash commands.

Here are some more commands for reference.

| Command Description                              | Command Example                 |
|--------------------------------------------------|---------------------------------|
| List all databases in the PostgreSQL server      | `\l`                            |
| List all roles and users                         | `\du`                           |
| List all schemas in the database                 | `\dn`                           |
| List all views in the connected database         | `\dv`                           |
| Exit the PostgreSQL prompt                       | `\q`                            |

After connecting, one can run queries in the Postgres dialect, just like the following one:

```sql
SELECT 
	 customer.country,
	 purchase.purchase_date,
	 MEASURE(purchase.total_spend)
 FROM
	 customer
	 CROSS JOIN purchase
 WHERE
	 (purchase.purchase_date BETWEEN '2024-01-01T15:37:55' AND '2024-12-31T15:38:02' AND (customer.country = 'Australia'))
 GROUP BY 1,2
 LIMIT 
	 10
 OFFSET 
	 0
```

## Query format in the SQL API

The SQL API uses the Postgres dialect to run queries that can reference tables and columns in the semantic model.

**Semantic model mapping**

In this model, each table or view is represented as a table in the database, and the measures, dimensions, and segments of the semantic model are represented as columns within these tables. This allows for seamless querying of the semantic model as if working with a regular relational database, where you can directly access the semantic model through SQL queries.

### **Tables and views**

<aside class="callout">

Given a table or view named `customers`, it can be queried just like a regular table.

</aside>

```sql
SELECT * FROM customer;
```

### **Dimensions**

To query a table or view with a dimension called country, it can be referenced as a column in the `SELECT` clause.
 <!-- Additionally, it must be included in the GROUP BY clause to ensure correct aggregation. -->

```
SELECT country
FROM customer;
```

<!-- ```
SELECT country
FROM customer
GROUP BY 1;
``` -->

### **Measures**

When a table or view has a measure (e.g., count), it needs to be referenced using an aggregation function like `MEASURE` to ensure that the measure is properly calculated over the relevant data.

```
SELECT MEASURE(total_customers)
FROM customer;
```
The SQL API allows aggregate functions on measures as long as they match measure types.


<aside class="callout">

🗣️ When querying dimension and measure together add `GROUP BY` clause:

```sql
SELECT country, MEASURE(total_customers) FROM customer GROUP BY 1;
```
</aside>


### **Aggregate functions**

The special `MEASURE` function works with measures of any type. Measure columns can also be aggregated with the following aggregate functions that correspond to measure types:

| Measure Type            | Aggregate Function in an Aggregated Query   |
|-------------------------|---------------------------------------------|
| `avg`                   | MEASURE or AVG                             |
| `boolean`               | MEASURE                                    |
| `count`                 | MEASURE or COUNT                           |
| `count_distinct`        | MEASURE or COUNT(DISTINCT ...)             |
| `count_distinct_approx` | MEASURE or COUNT(DISTINCT ...)             |
| `max`                   | MEASURE or MAX                             |
| `min`                   | MEASURE or MIN                             |
| `number`                | MEASURE or any other function from this table |
| `string`                | MEASURE or STRING_AGG                      |
| `sum`                   | MEASURE or SUM                             |
| `time`                  | MEASURE or MAX or MIN                      |


<aside class="callout">

🗣️ If an aggregate function doesn't match the measure type, the following error will be thrown: Measure aggregation type doesn't match.


</aside>

### **Segments**

Segments are exposed as columns of the `boolean` type. For instance a table has a segment called `country_india`, then reference it as a column in the `WHERE` clause:

```sql
SELECT *
FROM customer
WHERE country_india IS TRUE;
```

The SQL API allows aggregate functions on measures as long as they match measure types.

### **Joins**

Please refer to this page for details on joins.

```sql
SELECT country, 
education, 
MEASURE(total_customers) FROM customer 
WHERE education='Basic' 
GROUP BY 1,2 limit 10;
```
For this query, the SQL API would transform SELECT query fragments into a regular query. It can be represented as follows in the REST API query format:

```rest
{
  "dimensions": [
    "customer.country"
  ],
  "measures": [
    "customer.amount"
  ],
  "filters": [
    {
      "member": "orders.status",
      "operator": "equals",
      "values": [
        "shipped"
      ]
    }
  ]
}
```

Because of this transformation, not all functions and expressions are supported in query fragments performing `SELECT` from semantic model tables. Please refer to the [SQL API reference](/resources/lens/sql_apis/query_format#sql-api-references) to see whether a specific expression or function is supported and whether it can be used in selection (e.g., WHERE) or projection (e.g., SELECT) parts of SQL queries.

For example, the following query won't work because the SQL API can't push down the `CASE` expression to Lens for processing. It is not possible to translate `CASE` expressions in measures.

```sql
SELECT
  city,
  MAX(CASE
    WHEN status = 'shipped'
    THEN '2-done'
    ELSE '1-in-progress'
  END) AS real_status,
  SUM(number)
FROM orders
CROSS JOIN users
GROUP BY 1;
```
Nested queries allow for advanced querying by wrapping one `SELECT` statement (inner query) within another `SELECT` statement (outer query). This structure enables the use of additional SQL functions, operators, and expressions, such as CASE, which may not be directly applicable in the inner query.

To achieve this, the original `SELECT` statement can be rewritten with an outer query that performs further calculations or transformations.

Rewrite the above query as follows, making sure to wrap the original `SELECT` statement:

## Querying views via SQL API

The recommended approach for querying joins using the SQL API is through views. This method is preferred as it gives control over the join process.

 <!-- especially in complex scenarios. Although BI tools treat the view as a table, no materialization occurs until the semantic model is actually queried. When a semantic model view is queried via the SQL API, semantic model optimizes member pushdown, ensuring that only the necessary parts of the view are materialized at query time. Additionally, semantic model handles fan and chasm traps based on the dimensions specified in the query. As long as the measure aggregation types are correctly configured, the results in BI tools will be accurate, even though semantic models and views are essentially viewed as tables. -->


```yaml
views:
  - name: purchase_frequency
    description: This metric calculates the average number of times a product is purchased by customers within a given time period
    #...

    tables:
      - join_path: purchase
        prefix: true
        includes:
          - purchase_date
          - customer_id
          - purchase_frequency
          - purchases

      - join_path: product
        prefix: true
        includes:
          - product_category
          - product_name
```

Now, it is possible to get purchase_frequency of each product with the following query.

When a view is created by joining multiple tables, the columns in the view are prefixed with the respective table names from which they originate. This practice ensures that there is no ambiguity, even when multiple tables contain columns with similar or identical names.

For instance, in a view that aggregates data from the purchase and product tables:

- The `purchase_frequency` column originates from the `purchase` table, so it is prefixed with `purchase_` in the view, becoming `purchase_purchase_frequency` column in the view.
- Similarly, the `product_name` column originates from the `product` table, and in the view, it is prefixed with `product_`, becoming `product_product_name` in the view.

<aside class="callout">
🗣️ Failure to prefix table names in column names when querying a view with multiple tables can lead to errors.
</aside>


**Example:**

```shell
lens:public:productaffinity=> SELECT purchase_purchase_frequency, product_product_name FROM purchase_frequency;
 purchase_purchase_frequency | product_product_name 
-----------------------------+----------------------
                       12802 | Steak Meat
                       12091 | Salmon Fish
                        8154 | Red Wine
                        6388 | Chocolate
                        1618 | Apple
```


<aside class="callout">
See <a href="/resources/lens/sql_apis/supported_functions_and_operators/">SQL API reference</a> for the list of supported SQL commands, functions, and operators.
</aside>
