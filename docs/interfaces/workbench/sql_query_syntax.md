# Popular SQL Query Syntax

These are some popular SQL syntax queries that will help you explore Workbench and how it functions.

## Common Table Expression

 Common Table Expression(CTE) creates named subqueries that have a reference in the main query. You can define a CTE using WITH and AS clauses within a query. To understand it better, refer the below examples.

**Example 1:** We Need to Find the Highest Salary by Department, Now, let’s see how this data can be expressed into a SQL query using CTE.

```sql
--------- Common Table Expression(CTE)--------------
WITH highest_salary AS (
  SELECT
    first_name,
    last_name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank
  FROM
    employees
)
SELECT 
  first_name,
  last_name,
  salary,
  department
FROM
  highest_salary
WHERE
  salary_rank = 1;
```

**Example 2**: Suppose, if you want to calculate time difference of two timestamp columns in hour, you can calculate the same by running a query for it that requests the hours and calculate the difference hour.

```sql
with period as (
  select
    timestamp '2017-01-09 10:49:49' as period_start,
    timestamp '2017-02-01 07:02:32' as period_end
)

select date_diff('hour', period_start, period_end) as duration_hours
from period
```

## Window Function

A window function performs calculations across a set of table rows that are somehow related to the current row. For e.g., Find the Sum of the salary of employees for each department and order employees within a department by Order of their salary in descending order  You may choose to use LAG, LEAD, AVERAGE, and RANK based on your requirement.

```sql
---------WINDOW FUNCTION-----------
SELECT
    Name,
    Age,
    Department,
    Salary,
    SUM(Salary) OVER (PARTITION BY Department ORDER BY Salary desc) AS Avg_Salary
    FROM
      employee
```

## Extracting JSON

Evaluates the JSON Path-like expression json_path on json 
(a string containing JSON) and returns the result as a JSON string: In this query you will view the table author and contents within it as the result.

```sql
------Extracting a Json Path---------------
SELECT
    json_extract_scalar (json, '$.store.author')
  FROM
    json_table

SELECT json_extract_scalar(json, json_path);

```

## Joins

Suppose you have two tables. One contains the customer name and the other holds details of the products purchased. When you run a query with the join function, it will join both the tables giving a 3rd table containing the customer's name and the products purchased by him/her. Joins can be done in different ways like right, left, inner, and cross joins. DataOS Workbench allows you to join in the right, left, cross, and inner fashion.

```sql
-----------JOINS-------------------
SELECT
    orders.ord_no,
    customer.cust_name
  FROM
    orders
    JOIN customer ON orders.customer_id = customer.customer_id;

JOIN clause is used to combine rows from two or more tables, 
based on a related column between them.
```

## CASE

The CASE statement goes through conditions and returns a value when the first condition is met (like an if-then-else statement). So, once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the ELSE clause For Ex: We need to give each student a grade, and we can use the case statement to do it automatically.

```sql
------------ CASE STATEMENT-----------------------
SELECT *,
  (CASE
    WHEN score >= 94 THEN 'A'
    WHEN score >= 90 THEN 'A-'
    WHEN score >= 87 THEN 'B+'
    WHEN score >= 83 THEN 'B'
    WHEN score >= 80 THEN 'B-'
    WHEN score >= 77 THEN 'C+'
    WHEN score >= 73 THEN 'C'
    WHEN score >= 70 THEN 'C-'
    WHEN score >= 67 THEN 'D+'
    WHEN score >= 60 THEN 'D'
    ELSE 'F'
  END) AS grade
FROM students_grades;
```

## CONCAT

The CONCAT () function adds two or more strings together. For e.g., you have First name, middle name, and last name in 3 different columns. When you run CONCAT, it will generate a result that will hold data from the 3 columns.

```sql
----------CONCAT-----------
SELECT
  CONCAT(FirstName, ' ', MiddleName, ' ', Lastname) AS Full_Name
FROM
  Customers
```

Suppose, if you want to calculate time difference of two timestamp columns in hour, you can calculate the same by running a query for it that requests the hours and calculate the difference hour.

```sql
with period as (
  select
    timestamp '2017-01-09 10:49:49' as period_start,
    timestamp '2017-02-01 07:02:32' as period_end
)

select date_diff('hour', period_start, period_end) as duration_hours
from period
```

## LIKE

The LIKE operator is used in a WHERE clause to search for a specified pattern in a column. This will give results based on a similar pattern.  For Ex: In this Query, it will select the First Name of people starting with A

```sql

SELECT *
FROM Person
WHERE firstname LIKE 'A%';

SELECT * FROM table_name WHERE name LIKE 'x%';
OR
SELECT * FROM table_name WHERE name LIKE '%x';
OR
SELECT * FROM table_name WHERE name LIKE '%x%';
OR
SELECT * FROM table_name WHERE name LIKE 'x___x;
```

## SQL Query Syntaxes

```sql
SELECT * FROM tables [WHERE conditions]  
[GROUP BY fieldName(s)]  
[HAVING condition]   
[ORDER BY fieldName(s)]  
[LIMIT N];
```

```sql
SELECT *  
FROM table_name  
WHERE conditions;
```

```sql
SELECT DISTINCT expressions  
FROM tables
```

```sql
SELECT expressions  
FROM tables  
[WHERE conditions]  
ORDER BY expression [ ASC | DESC ];
```

```sql
SELECT expression1, expression2, ... expression_n,   
aggregate_function (expression)  
FROM tables  
[WHERE conditions]  
GROUP BY expression1, expression2, ... expression_n;
```

```sql
SELECT expression1, expression2, ... expression_n,   
aggregate_function (expression)  
FROM tables  
[WHERE conditions]  
GROUP BY expression1, expression2, ... expression_n  
HAVING condition;
```

```sql
SELECT columns  
FROM table1   
INNER JOIN table2  
ON table1.column = table2.column;
```

```sql
SELECT column_list  
FROM Table1  
RIGHT JOIN Table2   
ON join_condition;
```

```sql
SELECT column-lists  
FROM table1  
CROSS JOIN table2;
```

```sql
SELECT s1.col_name, s2.col_name...  
FROM table1 s1, table1 s2  
WHERE s1.common_col_name = s2.common_col_name;
```

```sql
SELECT COUNT (column_name)    
FROM table_name
```

```sql
SELECT SUM(column_name)    
FROM table_name
```

```sql
SELECT AVG(column_name)    
FROM table_name
```

```sql
SELECT MIN ( column_name)  
FROM table_name
```

```sql
SELECT MAX(column_name)    
FROM table_name
```

```sql
SELECT LENGTH('string');
```

```sql
SELECT date_add(unit, value, timestamp);
ex:-SELECT date_add('second', 86, TIMESTAMP '2020-03-01 00:00:00');
```

```sql
---------Date Functions------------------
SELECT current_date();
SELECT current_time();
SELECT current_timestamp();
SELECT date(x) ;
SELECT day(x);
SELECT day_of_month(x) ;
SELECT SELECT day_of_week(x);  // OR SELECT dow(x);
SELECT day_of_year(x);    //OR SELECT doy(x);
SELECT extract(field FROM x);
SELECT hour(x);
SELECT last_day_of_month(x) ;
SELECT localtimestamp();
SELECT localtime();
SELECT minute(x);
SELECT month(x);
SELECT now();
SELECT quarter(x);
SELECT second(x)
SELECT timestamp(expression);
SELECT week(x);
SELECT year(x) ;
```

## Example Queries

The following queries will help you get started.

```sql
-------------- Selecting All Columns We use * and LIMIT limits the number of Row--------------------------------------------
SELECT
  *
FROM
  "icebase"."sportsproducts".sports_products_data_with_ts
LIMIT 10;
----------------------- Using Filter by using WHERE Clause----------------------------------------------
SELECT
  *
FROM
  "icebase"."sportsproducts".sports_products_data_with_ts
WHERE
  modelname = 'Sport-100'
    --------------------Count to number of rows in a column--------------------------------------------
SELECT
  count(productkey) AS
  Count_Of_Key
FROM
  "icebase"."sportsproducts".sports_products_data_with_ts
      ---------------------DISTINCT returns only different or distinct values------------------
SELECT
  count(DISTINCT productkey) AS
  Distinct_key
FROM
  "icebase"."sportsproducts".sports_products_data_with_ts
        ---------------Using CASE WHEN Statements-------------------------
SELECT
gender,
CASE WHEN gender = 'M' THEN
  'MALE'
WHEN gender = 'F' THEN
  'FEMALE'
ELSE
  'NA'
END AS Gender
FROM
"icebase"."sportsproducts".sports_customers_data_with_ts
          --------------------- SUBQUERY ------------
SELECT
  modelname,
  SUM(
    COST) AS
    Total_price
FROM (
  SELECT
    *,
    cast(productcost AS double) AS
    COST
  FROM
    "icebase"."sportsproducts".sports_products_data_with_ts)
GROUP BY
modelname
```

## Trino SQL query syntax

With DataOS Workbench you can write queries with Trino query syntax. Refer here for [**Trino Statement Syntaxes.**](https://trino.io/docs/current/sql.html)