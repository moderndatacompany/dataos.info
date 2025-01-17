# Getting started with data modelling

The data model is used to transform raw data into meaningful business definitions for optimal results. This data model is then exposed through a rich set of APIs that allows end-users to run a wide variety of analytical queries without modifying the data model itself.

Let's use a `sales` table with the following columns as an example:

**`sales`**

| order_id | product | amount | city          | customer_name |
|----------|---------|--------|---------------|---------------|
| 1        | Shoes   | 150    | New York      | John Doe      |
| 2        | Jacket  | 200    | San Francisco | Jane Smith    |
| 3        | Hat     | 50     | Los Angeles   | Michael Brown |
| 4        | Shoes   | 120    | New York      | Emily Davis   |
| 5        | Jacket  | 220    | Chicago       | Sarah Wilson  |

We can start with a set of simple questions about `sales` we want to answer:

- What is the total sales amount?
- What is the total order count?
- What is the average sales amount?
- How many sales came from different cities and customers?

Instead of writing individual SQL queries for each of these questions, the data model in Lens allows for creating well-organized and reusable SQL logic. By defining dimensions and measures in the data model, you can streamline these analyses and enhance the ability to extract meaningful insights from your data efficiently.


##  Creating a Lens

A Lens is used to model entities and their relationships. It organizes multiple related entities and defines how they interact with each other. For example, a Lens could include entities such as `sales`, `orders`, `products`, etc., with defined relationships between them.

In the table attribute of the Lens, define the base table. Here, it will be the sales table.


### **1. Loading data from the data source**

Begin by connecting to the data source. In the sql directory, create SQL scripts for each table you plan to use. These scripts will extract the required data from the data source.
Each SQL script corresponds to a table and uses the source-specific SQL dialect. For example:

```sql
SELECT
  *
FROM
  "icebase"."sales_360".channel;
```

This can be a simple extraction or include more complex transformations, such as:

```sql
SELECT
  cast(customer_id AS varchar) AS customer_id,
  first_name,
  cast(date_parse(birth_date,'%d-%m-%Y') as timestamp) as birth_date,
  age,
  cast(register_date as timestamp) as register_date,
  occupation,
  annual_income,
  city,
  state,
  country,
  zip_code
FROM
  "icebase"."sales_360".customer;
```


### 2. **Defining the Table in the Model**

In the tables directory, create a definition for real world entity. For example, to define a table for sales data:

```yaml
table:
  - name: sales
    sql: {{ load_sql('sales') }}
    description: Table containing information about sales transactions.
```

This links the SQL script loaded from the source to the Lens model.

### **3. Adding Measures and Dimensions**

After defining the base table, add measures and dimensions to provide meaningful analysis. 

> Dimensions are used for filtering and grouping data, while measures are the numerical values you want to analyze.

Let's go ahead and create our first measure and two dimensions:

```yaml
tables:
  - name: sales
    sql: {{ load_sql('sales') }}
    description: Table containing sales records with order details.

    dimensions:
      - name: order_id
        type: number
        description: Unique identifier for each order.
        sql: order_id
        primary_key: true
        public: true
        
      - name: city
        type: string
        description: City where the customer is located.
        sql: city

    measures:
      - name: total_orders_count
        type: count
        sql: id
        description: Total amount of orders.
    #....
```

Let's break down the above code snippet piece-by-piece. After defining the base table for the Lens (with the table attribute), we create a count measure in the measures block. The count type and sql means that when this measure will be requested via an API, Lens will generate and execute the following SQL:

```sql 
SELECT COUNT(order_id) AS total_orders_count
FROM sales;
```

When we apply a city dimension to the measure to see "Where are customers based?", Lens will generate SQL with a GROUP BY clause:

```sql
SELECT city, COUNT(id) AS count
FROM users
GROUP BY 2;
```

You can add as many dimensions as you want to your query when you perform grouping.


### **4. Adding Segments to Measures**

Now let's answer the next question – "What is the total sales amount for city New York?". To accomplish this, we will introduce measure filters called segments:

```yaml
segments:
  - name: total_sales_newyork
    sql: "{TABLE}.city = 'New York'"
```
Since the `segments` attribute type is an array, you can apply as many segments as required. 

```yaml
segments:
  - name: sanfrancisco_sales
    sql: "{TABLE}.city = 'San Francisco'"

  - name: losangeles_sales
    sql: "{TABLE}.city = 'Los Angeles'"

  - name: chicago_sales
    sql: "{TABLE}.city = 'Chicago'"

 #....
```


### **5. Using Calculated Measures**

To answer the question "What is the average sales amount per order?", you'll need to calculate the average amount for all orders. This can be done by defining a measure that calculates the average of the amount field. Here's how you can define this in YAML for your sales table:

```yaml
measures:
 - name: total_sales_amount
   sql: SUM(amount)
   type: number
   description: Total sales amount across all orders.

 - name: total_order_count
   sql: COUNT(order_id)
   type: count
   description: Total number of orders.

 - name: average_sales_amount_per_order
   sql: "{total_sales_amount} / NULLIF({total_order_count}, 0)"
   type: number
   format: currency
   description: The average sales amount per order.

# .....
```
Here we defined a calculated measure `average_sales_amount_per_order`, which divides the total sales amount by the total number of orders. The NULLIF function prevents division by zero in case there are no orders.

This example shows how you can reference measures inside other measure definitions. When you request the `average_sales_amount_per_order` measure via an API, the following SQL will be generated:

```sql
SELECT
  SUM(amount) / NULLIF(COUNT(order_id), 0) AS average_sales_amount_per_order
FROM
  sales
```
As with other measures, average_sales_amount_per_order can be used with dimensions.


<!-- ### **6.  **  -->