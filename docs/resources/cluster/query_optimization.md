# SQL Query Optimization

SQL query optimization, also referred to as SQL query tuning, is an iterative process that aims to enhance the performance of a query in terms of execution time, the number of disk accesses, and other cost-measuring criteria.

## Purpose of SQL Query Optimization

The purpose of SQL query optimization is to achieve the following:

1. Reduce Response Time
2. Decrease CPU Execution Time
3. Improve Throughput

To accomplish these goals, developers can employ various optimization techniques. Here are some recommendations to make queries faster:

### **`SELECT` Specific Fields**

Instead of using `SELECT *` to retrieve all fields, it is advisable to specify the required fields explicitly. This approach can significantly improve query performance.

**Example:**

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

**Instead of**

```sql
SELECT
  *
FROM
  Customers
```

### **Avoid `SELECT DISTINCT`**

Using `SELECT DISTINCT` requires substantial processing power since it involves grouping all fields in the query to generate distinct results. Avoiding this operation can lead to performance gains.

**Example:**

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

**Instead of**

```sql
SELECT DISTINCT
  FirstName,
  LastName,
  State
FROM
  Customers
```

### **Use `INNER JOIN` for Joins**

When performing joins, utilize `INNER JOIN` instead of joining in the `WHERE` clause. Joining in the `WHERE` clause can result in a Cartesian Join, which generates all possible combinations of variables before filtering the desired records. `INNER JOIN` prevents this issue and improves query efficiency.

**Example:**

```sql
SELECT
  Customers.CustomerID,
  Customers.Name,
  Sales.LastSaleDate
FROM
  Customers
  INNER JOIN Sales ON Customers.CustomerID = Sales.CustomerID
```

### **Use `WHERE` instead of `HAVING` for Filters**

Prefer using the `WHERE` clause instead of `HAVING` to define filters. The `HAVING` clause should only be used when filtering on an aggregated field. By using `WHERE`, unnecessary records can be eliminated at an earlier stage, leading to better query performance.

**Example:**

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

### **Place Wildcards at the End of a Phrase**

When performing wildcard searches, such as searching for cities or names, it is more efficient to place wildcards at the end of the search phrase. This approach avoids unnecessarily broad searches and improves query performance.

**Example:**

```sql
SELECT
  City
FROM
  Customers
WHERE
  City LIKE 'Char%'
```

### **Use `LIMIT` to Sample Query Results**

Before executing a query for the first time, consider using the `LIMIT` statement to retrieve a limited number of results. This helps ensure that the query output is desirable and meaningful.

### **Prefer `EXISTS` over `IN`**

When dealing with subqueries that result in large datasets, using the `EXISTS` operator is generally more efficient than `IN`. The `IN` operator can be costly in terms of scans, while `EXISTS` provides a more optimized alternative.

**Example:**

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

**Instead of**

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

These optimization techniques should be considered based on the characteristics of the query. Queries involving large tables, Cartesian Joins, looping statements, DISTINCT selection, nested subqueries, wildcard searches in long text fields, and multiple schema queries are more likely to benefit from optimization. Consider running such queries during off-peak hours to further enhance performance.

In addition, Minerva offers the capability to push down query processing to the connected data source. This means that specific predicates, aggregation functions, or other operations can be passed through to the underlying database or storage system for processing. By leveraging this feature, query performance can be significantly improved.