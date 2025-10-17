# User-defined checks

If the built-in set of metrics and checks that Soda provides do not fully meet your requirements, you can define your own metrics to customize checks according to your specific data needs.
User-defined checks allow you to create **Common Table Expressions (CTE)** or **SQL queries** that Soda executes during a scan.

These checks follow the same structure as standard Soda checks — consisting of a **metric**, a **comparison operator or phrase**, and a **threshold**.



**Example using a custom metric expression:**
This example uses a CTE expression to define a custom metric named `avg_order_span`, which calculates the average difference between the first and last order years. The check validates that the calculated average falls within a defined range.

```yaml
- avg_order_span between 5 and 10:
    avg_order_span expression: AVG(last_order_year - first_order_year)
    attributes:
      category: Accuracy
      title: Validate average order span falls between 5 and 10 years
```

| **Field**                       | **Value / Example**                       |
| ------------------------------- | ----------------------------------------- |
| **Custom metric**               | `avg_order_span`                          |
| **Comparison symbol or phrase** | `between`                                 |
| **Threshold**                   | `5 and 10`                                |
| **Expression key**              | `avg_order_span expression`               |
| **Expression value**            | `AVG(last_order_year - first_order_year)` |



**Example using a custom metric defined by SQL query:**
Instead of defining a CTE expression, you can use a SQL query to create the metric. The following example defines a custom metric named `product_stock`, which counts the difference between `safety_stock_level` and `days_to_manufacture`. The check ensures that the resulting metric is greater than or equal to 50.

```yaml
- product_stock >= 50:
    product_stock query: |
      SELECT COUNT(safety_stock_level - days_to_manufacture)
      FROM dim_product
    attributes:
      category: Completeness
      title: Validate minimum product stock availability threshold
```

| **Field**                       | **Value / Example**                                                       |
| ------------------------------- | ------------------------------------------------------------------------- |
| **Custom metric**               | `product_stock`                                                           |
| **Comparison symbol or phrase** | `>=`                                                                      |
| **Threshold**                   | `50`                                                                      |
| **Query key**                   | `product_stock query`                                                     |
| **Query value**                 | `SELECT COUNT(safety_stock_level - days_to_manufacture) FROM dim_product` |



**Example of a user-defined check for data validity:**
This example defines a custom metric that calculates the ratio of valid email addresses in a dataset. The check ensures that at least 95% of email entries match a standard email pattern, maintaining data validity.

```yaml
- valid_email_ratio >= 0.95:
    valid_email_ratio expression: |
      SUM(CASE WHEN email_address ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' THEN 1 ELSE 0 END) / COUNT(*)
    attributes:
      category: Validity
      title: Ensure at least 95% of email addresses are valid
```

| **Field**                       | **Value / Example**                                                                                               |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Custom metric**               | `valid_email_ratio`                                                                                               |
| **Comparison symbol or phrase** | `>=`                                                                                                              |
| **Threshold**                   | `0.95`                                                                                                            |
| **Expression key**              | `valid_email_ratio expression`                                                                                    |
| **Expression value**            | `SUM(CASE WHEN email_address ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' THEN 1 ELSE 0 END) / COUNT(*)` |



**Best practices:**

* Always use **descriptive metric names** without spaces (e.g., `avg_order_span`, `valid_email_ratio`).
* Assign an appropriate **category** under `attributes` for easier tracking and reporting.
* Keep SQL expressions optimized for performance, especially when scanning large datasets.
* Use **custom metrics** for scenarios not covered by built-in Soda checks, such as domain-specific calculations or complex data validation logic.

