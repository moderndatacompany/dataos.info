# Query Optimization

SQL Query optimization is defined as the iterative process of enhancing the performance of a query in terms of execution time, the number of disk accesses, and many more cost-measuring criteria.

SQL optimization is also known as SQL query tuning.

Purpose of SQL Query Optimization:

1. Reduce Response Time

2. Reduced CPU execution time

3. Improved Throughput

Here are some of the tricks to make your queries faster.

1. SELECT fields instead of using SELECT \\:

<u>Example:</u>

```sql
SELECT
  FirstName,
  LastName,
  Address,
  City,
  State,
  Zip
FROM
  Customers
```

Instead of

```sql
SELECT
  *
FROM
  Customers
```

2. Avoid SELECT DISTINCT:

`SELECT DISTINCT` works by `GROUPING` all fields in the query to create distinct results. To accomplish this goal, however, a large amount of processing power is required.

<u>Example:</u>

```sql
SELECT
  FirstName,
  LastName,
  Address,
  City,
  State,
  Zip
FROM
  Customers
```

Instead of

```sql
SELECT DISTINCT
  FirstName,
  LastName,
  State
FROM
  Customers
```

3. Create joins with INNER JOIN (not WHERE):

<u>Example:</u>

```sql
SELECT
  Customers.CustomerID,
  Customers.Name,
  Sales.LastSaleDate
FROM
  Customers,
  Sales
WHERE
  Customers.CustomerID = Sales.CustomerID
```

- This type of join creates a Cartesian Join, also called a Cartesian Product or  `CROSS JOIN`.
- In a Cartesian Join, all possible combinations of the variables are created. In this example, if we had 1,000 customers with 1,000 total sales, the query would first generate 1,000,000 results, then filter for the 1,000 records where CustomerID is correctly joined.
- To prevent creating a Cartesian Join, use `INNER JOIN` instead:

```sql
SELECT
  Customers.CustomerID,
  Customers.Name,
  Sales.LastSaleDate
FROM
  Customers
  INNER JOIN Sales ON Customers.CustomerID = Sales.CustomerID
```

- The database would only generate the 1,000 desired records where CustomerID is equal.

4. Use WHERE instead of HAVING to define filters:

<u>Example:</u>

Let’s assume 200 sales have been made in the year 2016, and we want to query for the number of sales per customer in 2016.

```sql
SELECT
  Customers.CustomerID,
  Customers.Name,
  Count(Sales.SalesID)
FROM
  Customers
  INNER JOIN Sales ON Customers.CustomerID = Sales.CustomerID
GROUP BY
  Customers.CustomerID,
  Customers.Name
HAVING
  Sales.LastSaleDate BETWEEN # 1 / 1 / 2016 # AND # 12 / 31 / 2016 #
```

This query would pull 1,000 sales records from the Sales table, then filter for the 200 records generated in the year 2016, and finally count the records in the dataset.

In comparison, `WHERE` clauses limit the number of records pulled:

```sql
SELECT
  Customers.CustomerID,
  Customers.Name,
  Count(Sales.SalesID)
FROM
  Customers
  INNER JOIN Sales ON Customers.CustomerID = Sales.CustomerID
WHERE
  Sales.LastSaleDate BETWEEN # 1 / 1 / 2016 # AND # 12 / 31 / 2016 #
GROUP BY
  Customers.CustomerID,
  Customers.Name
```

This query would pull the 200 records from the year 2016, and then count the records in the dataset. The first step in the `HAVING` clause has been completely eliminated.

`HAVING` should only be used when filtering on an aggregated field. In the query above, we could additionally filter for customers with greater than 5 sales using a HAVING statement.

```sql
SELECT
  Customers.CustomerID,
  Customers.Name,
  Count(Sales.SalesID)
FROM
  Customers
  INNER JOIN Sales ON Customers.CustomerID = Sales.CustomerID
WHERE
  Sales.LastSaleDate BETWEEN # 1 / 1 / 2016 # AND # 12 / 31 / 2016 #
GROUP BY
  Customers.CustomerID,
  Customers.Name
HAVING
  Count(Sales.SalesID) > 5
```

5. Use wildcards at the end of a phrase only:

<u>Example:</u>

When searching plaintext data, such as cities or names, `wildcards` create the widest search possible. However, the widest search is also the most inefficient search.

Consider this query to pull cities beginning with ‘Char’:

```sql
SELECT
  City
FROM
  Customers
WHERE
  City LIKE ‘%Char%’
```

This query will pull the expected results of Charleston, Charlotte, and Charlton. However, it will also pull unexpected results, such as Cape Charles, Crab Orchard, and Richardson.

A more efficient query would be:

```sql
SELECT
  City
FROM
  Customers
WHERE
  City LIKE ‘Char%’
```

This query will pull only the expected results of Charleston, Charlotte, and Charlton.

6. Use LIMIT to sample query results:

Before running a query for the first time, ensure the results will be desirable and meaningful by using a `LIMIT` statement.

7. IN versus EXIST:

IN operator is more costly than `EXISTS` in terms of scans especially when the result of the subquery is a large dataset. So we should try to use `EXISTS` rather than using IN for fetching results with a subquery.

<u>Example:</u>

```sql
SELECT
  ProductNumber,
  Name,
  Color
FROM
  SalesLT.Product
WHERE
  EXISTS (
    SELECT
      ProductID
    FROM
      SalesLT.ProductDescription)
```

Instead of

```sql
SELECT
  ProductNumber,
  Name,
  Color
FROM
  SalesLT.Product
WHERE
  ProductID IN (
    SELECT
      ProductID
    FROM
      SalesLT.ProductDescription)
```

1. The more of the following criteria your query has

 

- The more likely a candidate should be to run at night or run your query during off-peak hours
- Selecting from large tables (>1,000,000 records)
- Cartesian Joins or CROSS JOINs
- Looping statements
- SELECT DISTINCT statements
- Nested subqueries
- Wildcard searches in long text or memo fields
- Multiple schema queries