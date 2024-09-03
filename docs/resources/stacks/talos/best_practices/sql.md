# SQL Best Practices

Welcome to the SQL Best Practices guide for Talos. This document is designed to help you write efficient, readable, and maintainable SQL queries. Whether you're a beginner or an advanced user, following these best practices will ensure your queries perform well and are easy to understand.

## 1. Use Clear and Consistent Naming Conventions

**Example:**

```sql
SELECT customer_id, first_name, last_name
FROM customers;
```

- Use `snake_case` for column and table names.
- Be descriptive but concise.

## 2. Optimize Queries

**Example:**

Avoid `SELECT *`:

```sql
-- Bad Practice
SELECT * FROM orders;

-- Good Practice
SELECT order_id, order_date, total_amount FROM orders;
```

**Index Usage:**

```sql
CREATE INDEX idx_customer_id ON orders (customer_id);
```

- Use indexes on columns frequently used in `WHERE`, `JOIN`, and `ORDER BY` clauses.

## 3. Normalize Data

**Example:**

```sql
-- Normalized Tables
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);
```

- Normalize data to reduce redundancy and improve data integrity.

## 4. Write Readable Code

**Example:**

```sql
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.order_date
FROM
    customers c
JOIN
    orders o ON c.customer_id = o.customer_id
WHERE
    o.order_date >= '2024-01-01'
ORDER BY
    o.order_date DESC;
```

- Use indentation and line breaks.
- Comment on complex queries to explain logic.

## 5. Handle NULLs Properly

**Example:**

```sql
SELECT
    first_name,
    last_name,
    email
FROM
    customers
WHERE
    email IS NOT NULL;
```

- Use `IS NULL` and `IS NOT NULL` to handle `NULL` values correctly.

## 6. Use Transactions

**Example:**

```sql
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

COMMIT;
```

- Wrap related operations in transactions to ensure data consistency.

## 7. Avoid Subqueries in the SELECT Clause

**Example:**

```sql
-- Bad Practice
SELECT
    order_id,
    (SELECT first_name FROM customers WHERE customers.customer_id = orders.customer_id) AS customer_name
FROM
    orders;

-- Good Practice
SELECT
    o.order_id,
    c.first_name
FROM
    orders o
JOIN
    customers c ON o.customer_id = c.customer_id;
```

- Use `JOINs` instead of subqueries for better performance and readability.

## 8. Use Parameterized Queries

**Example:**

```sql
-- Example in a programming context, e.g., Python
cursor.execute("SELECT * FROM customers WHERE customer_id = %s", (customer_id,))
```

- Use parameterized queries to prevent SQL injection attacks.

## 9. Test and Validate

**Example:**

```sql
-- Test query to ensure expected results
SELECT
    order_id,
    order_date
FROM
    orders
WHERE
    order_date BETWEEN '2024-01-01' AND '2024-12-31';
```

- Test queries to ensure they return the expected results and perform well.

## 10. Monitor Performance

**Example:**

```sql
-- Use EXPLAIN to analyze query performance
EXPLAIN SELECT * FROM orders WHERE customer_id = 1;
```

- Use database tools to monitor and analyze query performance, and optimize as necessary.

## Advanced SQL Techniques

### Common Table Expressions (CTEs)

```sql
WITH RecentOrders AS (
    SELECT
        order_id,
        customer_id,
        order_date
    FROM
        orders
    WHERE
        order_date > '2024-01-01'
)
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    ro.order_id,
    ro.order_date
FROM
    customers c
JOIN
    RecentOrders ro ON c.customer_id = ro.customer_id;
```

- Use CTEs to simplify complex queries and improve readability.

### Window Functions

```sql
SELECT
    order_id,
    customer_id,
    order_date,
    SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS running_total
FROM
    orders;
```

- Use window functions for advanced calculations across a set of table rows.

By following these best practices, you'll ensure that your SQL code is efficient, maintainable, and scalable, helping you make the most out of your data with Talos.