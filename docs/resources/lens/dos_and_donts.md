# Best practices of semantic model built using Lens 

This documentation outlines essential guidelines while creating a semantic model, highlighting key best practices, such as when to create views and how to avoid common errors. and do's and don't's.

## Do's

### **Naming conventions**

* Use only letters, numbers, and underscores (\_); avoid special characters. Adopt snake\_case for naming tables, views, measures, and dimensions.

**Example naming conventions:**

* Tables: `orders`, `stripe_invoices`, `base_payments`

* Views: `opportunities`, `cloud_accounts`,

* Measures: `count`, `avg_price`, `total_amount_shipped`

* Dimensions: `name`, `is_shipped`, `created_at`

### **Case sensitivity**

If your database uses case-sensitive identifiers, ensure you properly quote table and column names. For example, to reference a Postgres table with uppercase letters:

```yaml
SELECT * FROM'public."Site"'
```

### **Materialization**

**Materialized views for historical data:** When working with large volumes of historical data, create materialized views in the transformation layer (e.g., Flare) to improve performance and reduce runtime during querying.
   
**Materialize repeated tables:** Common tables used in multiple Data Products should be materialized to enhance performance, avoid redundant computations, and maintain consistency.

**On the fly vs Pre-materialized measures:** Whether to calculate measures on-the-fly or materialize them depends on their complexity. For complex or computationally expensive measures, it’s better to materialize them beforehand to optimize performance and reduce runtime processing. For simpler measures that don’t require heavy computation, calculating on-the-fly is more efficient.

### **Dimension References**

To build reusable data models, it’s important to reference various members of tables and views, such as measures, dimensions, and columns. Lens uses specific syntax for handling these references:

#### **Direct Column Reference**

In general, for simple cases, you can use column names directly without the need for curly braces, like this: `column_name`. However, if you’re dealing with joins or complex queries, you may need to qualify the references for clarity.

```yaml
tables:
  - name: order
    sql: {{ load_sql('order') }}
    description: table containing order information
    public: true
    meta:
      export_to_board: false
    dimensions:
      - name: status
        sql: status
        type: string
```

In this example, the column status from the order table is referenced directly in the `sql` attribute. This syntax works great for simple use cases. However, if your tables have joins and joined tables have columns with the same name, the generated SQL query might become ambiguous. See below how to work around that.

#### **Prefix with table name**

When referencing a column from a specific table, prefix the column with the table name `table_name.column_name` (e.g., `order.status`). This is especially important when working with joined tables that may have columns with the same name.

```yaml
tables:
  - name: users
    sql: {{ load_sql('users') }}
    joins:
      - name: contacts
        sql: "{users}.contact_id = {contacts}.id"
        relationship: one_to_one
    dimensions:
      - name: id
        sql: "{users}.id"
        type: number
        primary_key: true
      - name: name
        sql: "COALESCE({users}.name, {contacts}.name)"
        type: string

  - name: contacts
    sql: {{ load_sql('contacts') }}
    dimensions:
      - name: id
        sql: "{contacts}.id"
        type: number
        primary_key: true
      - name: name
        sql: "{contacts}.name"
        type: string
```

In this case, the name field is referenced from both the users and contacts tables. Using `"{users}.name"` and `"{contacts}.name"` ensures that there’s no ambiguity.

#### **Use the `TABLE` constant**

If you need to refer to a column in the current table, use the TABLE constant `"{TABLE}.column_name"` (e.g., `"{TABLE.status}"` to avoid repeating the table's name.

```yaml
tables:
  - name: users
    sql: {{ load_sql('users') }}
    joins:
      - name: contacts
        sql: "{TABLE}.contact_id = {contacts}.id"
        relationship: one_to_one
    dimensions:
      - name: id
        sql: "{TABLE}.id"
        type: number
        primary_key: true
      - name: name
        sql: "COALESCE({TABLE}.name, {contacts}.name)"
        type: string

  - name: contacts
    sql: {{ load_sql('contacts') }}
    dimensions:
      - name: id
        sql: "{TABLE}.id"
        type: number
        primary_key: true
      - name: name
        sql: "{TABLE}.name"
        type: string
```

In this example, the `{TABLE}` constant is used to refer to columns in the `users` table, reducing repetition and making the code more efficient.

### **Measure References**

#### **Creating a measure based on another measure within the same table**

When you need to create a new measure that depends on the value of an existing measure within the same table, you can reference the existing measure using curly braces `{}`. This allows you to reference and perform operations on already defined measures without repeating their logic.

```yaml
- name: current_month_sum
  sql: sellingprice
  type: sum
  filters:
    - sql: month({invoice_date}) = 5

- name: previous_month_sum
  sql: sellingprice
  type: sum
  filters:
    - sql: month({invoice_date}) = 4

- name: month_over_month_ratio
  sql: "{current_month_sum} / {previous_month_sum}"
  type: number
```

In the above example, the `month_over_month_ratio` measure references the two previously defined measures and divides the `current_month_sum` by the `previous_month_sum` to get the month-over-month ratio.

#### **Proxy dimension: Referencing dimensions from another table**

To reference a dimension from one  while creating a measure in another, use the curly braces `{}`. Specify the dimension using `{.column}` if it is from another table, or `{column name}` if it is within the same table.

```yaml

- name: ref_dimension_cust
  sql: "{account.state}"
  type: string

measures:
  - name: ref_measure
    sql: case when {sales.ref_dimension} like '%w%' then **{ext_net}** end
    type: sum
```

#### **Calling a measure from another table**

When referencing a measure from another table, set `sub_query` to `true`.

```yaml
- name: subq_rev
  sql: "{sales.total_revenue}"
  sub_query: true
  type: number
```

#### **Transforming dimension and calling it in a measure**

Use curly braces `{}` when calling a transformed dimension within measures.

```yaml
dimensions:
  - name: quarter
    sql: quarter(invoice_date)
    type: number

measures:
  - name: total_quantities
    type: sum
    sql: qty_dec_equ
    filters:
      - sql: year({quarter}) = 1
```

#### **Working with windows function**

To correctly aggregate a measure within a window, use the rolling\_window parameter when defining the measure. This ensures that any filters applied to the measure are correctly placed in the WHERE clause, which is essential for accurate results. Without rolling\_window, filters might go into the HAVING clause, leading to incorrect calculations.

```yaml
# This calculates the rolling sum of inventory sold for the previous 30 days
  - name: monthly_inventory_sold
    description: sum of total inventory sold up to the start of the month
    type: sum
    sql: "{TABLE.inventory}"
    rolling_window:
      trailing: 1 month
      offset: start
```

**Use Cases for rolling windows:**

* Running totals or moving averages.

* Ranking and percentile analysis (e.g., top performers).

* Time series analysis (e.g., tracking month-over-month growth).

* Comparative analysis (e.g., previous/next values or differences between rows).

<aside class="callout">
Always aim to roll down data as much as possible to minimize the amount of data processed in subsequent stages, enhancing query efficiency.
</aside>

### **Views**

1. **Purpose:** Create views to provide a limited part of your data model to the consumer layer, such as any BI tool. Views are useful for defining metrics, managing governance and data access, and controlling ambiguous join paths.

2. **Members:** Views do not have their members. Instead, use the `table` or `includes` parameters to incorporate measures and dimensions from other tables into the view.

3. **Refresh key:** Use a refresh key if the underlying data is refreshed on a regular cadence.

**Example: `revenue_view`**

In the following example, we create a view called `revenue_view`, which includes selected members from the `sales`, `product`, and `account` tables:

```yaml
views:
  - name: revenue_view
    description: View containing sales 360 degree information
    public: true
    meta:     
      export_to_iris: true
      iris:
        timeseries: sales.invoice_date
        excludes:
         - sales.source
         - sales.invoice_date
        refresh:
          every: 24h

    tables:
      - join_path: sales
        prefix: false
        includes:
          - revenue
          - invoice_date
          - ext_net
          - source

      - join_path: product
        prefix: true   # product_category
        includes:
          - category
          - brand
          - class

      - join_path: account
        prefix: false
        includes:
          - site_name
          - state
```

### **Jinja macros**

Lens data models support Jinja macros, allowing you to define reusable snippets of code. This feature helps in creating dynamic data models and SQL properties efficiently.

#### **Dynamic data models**

In the example below, we define a macro called `dimension()` which generates a dimension. This macro is then invoked multiple times to generate various dimensions.

**Example:**

```yaml
{# Declare the macro before using it, otherwise Jinja will throw an error. #}
{%- macro dimension(column_name, type='string', description=None, primary_key=false, public_key=false) -%}
  - name: {{ column_name }}
    sql: {{ column_name }}
    type: {{ type }}
    {% if description is not none %}
    description: {{ description }}
    {% endif %}
    {% if primary_key -%}
    primary_key: true
    {% endif %}
    {% if public_key -%}
    public_key: false
    {% endif -%}
{% endmacro -%}

tables:
  - name: account
    sql: {{ load_sql('account') }}
    description: table containing information about account
    public: true
    meta:
      export_to_board: true

    dimensions:
      {{ dimension('customer_id', type='string', description='Customer primary key.', primary_key=true) }}
      {{ dimension('site_number', type='number', description='The site number.') }}
      {{ dimension('customer_name', description='Name of the customer.') }}
      {{ dimension('address', description='Address of the customer.') }}
      {{ dimension('city', description='City of the customer.', public_key=true) }}
      {{ dimension('county_name', description='County name of the customer.') }}
```

#### **SQL property**

Macros can also be used to generate SQL snippets for use in the `sql` property. For example, to avoid division by zero errors when creating measures, define a macro and use it in multiple measures.

**Example:**

```yaml
{%- macro nullif_sum_cast(column_name) -%}
  cast(nullif(sum({{ column_name }}), 0) as decimal(20,5))
{%- endmacro -%}

measures:
  - name: wallet_share
    sql: >
      round((sum(ext_net) FILTER (WHERE lower({source}) = 'proof')) / {{ nullif_sum_cast('ext_net') }}, 2)
    type: number
```

#### **Dynamic segments with secure access**

You can create dynamic segments with secure access using Jinja macros. This example sets up segments for different categories with user group restrictions.

**Example:**

```yaml
{%- set personas = ["data_consumer", "data_developer", "data_analyst", "data_scientist"] -%}

segments:
  {% for persona in personas %}
    - name: {{ "segment_" ~ persona }}
      public: true
      sql: {{ "{user_role} = '" ~ persona ~ "'" }}
      meta:
        secure:
          user_groups:
            includes:
              - {{ persona }}
            excludes:
              - default
  {% endfor %}
```

#### **User group configuration**

```yaml
user_groups:
  - name: data_consumer
    api_scopes:
      - data
      - graphql
    includes:
      - users:id:iamgroot
      - users:id:harrypotter
  - name: data_developer
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
    includes:
      - users:id:tonystark
      - users:id:brucebanner
  - name: data_analyst
    api_scopes:
      - meta
      - data
      - graphql
    includes:
      - users:id:sherlockholmes
      - users:id:watson
  - name: data_scientist
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes:
      - users:id:drstrange
      - users:id:spiderman
  - name: default
    includes: "*"
    api_scopes:
      - data
      - graphql
```

By leveraging Jinja macros, you can create efficient, reusable, and dynamic configurations in your Lens data models.

### **Materialized views for historical data**

When working with large volumes of historical data, create materialized views in the transformation layer (e.g., Flare) to improve performance and reduce runtime during querying.

### **Roll down data**

Always aim to roll down data as much as possible to minimize the amount of data processed in subsequent stages, enhancing query efficiency.

### **Avoid references and sub-queries with large data**

Avoid using references and sub-queries when dealing with large datasets. These operations tend to create multiple joins behind the scenes, which can severely degrade performance. However, for queries with many joins, using references might still be necessary for clarity and efficiency.

### **Materialize repeated tables**

Common tables used in multiple Data Products should be materialized to enhance performance, avoid redundant computations, and maintain consistency.

## **Don’ts**

When creating a semantic model, avoid the following practices to ensure functionality and maintainability:

### **Avoid references and sub-queries with large data** 

Avoid using references and sub-queries when dealing with large datasets. These operations tend to create multiple joins behind the scenes, which can severely degrade performance. However, for queries with many joins, using references might still be necessary for clarity and efficiency.

### **Avoid using curly braces `{}` in descriptions**

Since Jinja is supported, using curly braces `{}` in descriptions can cause issues.

```yaml
dimensions:
  - name: sales_sk
    type: string
    column: sales_sk
    public: false
    primary_key: true
    description: It is the primary key of sales
```

### **Avoid using single quotes in measures, dimensions, and segments**

Using single quotes can cause errors. Instead, use double quotes.

```yaml
tables:
  - name: order
    sql: {{ load_sql('order') }}
    description: table containing information about product
    public: true
    meta:
      export_to_board: false

    measures:
      - name: statuses
        sql: "listagg({order.status}) WITHIN GROUP (ORDER BY {order.status})"
        type: string

    dimensions:
      - name: status
        sql: "UPPER(status)"
        type: string
```

### **Avoid filtering measures and dimensions from the same table with the OR operator**

Measures and dimensions from the same table cannot be filtered simultaneously using the 'OR' operator.

=== "Incorrect example"

    Avoid combining dimensions and measures in the same 'OR' condition.

    ```json
    {
      "measures": [
        "sales.total_revenue"
      ],
      "dimensions": [
        "sales.site_number"
      ],
      "segments": [],
      "filters": [
        {
          "or": [
            {
              "member": "sales.site_number",
              "operator": "equals",
              "values": [
                "1",
                "21"
              ]
            },
            {
              "member": "sales.total_revenue",
              "operator": "gt",
              "values": [
                "0"
              ]
            }
          ]
        }
      ],
      "timedimensions": [],
      "limit": 10,
      "offset": 0
    }
    ```

=== "Correct example"

    Avoid combining dimensions and measures in the same 'OR' condition. Use separate conditions for clarity.

    ```json
    {
      "or": [
        {
          "member": "sales.invoice_no",
          "operator": "equals",
          "values": [
            "448",
            "1265",
            "45",
            "517",
            "2874",
            "1",
            "837"
          ]
        },
        {
          "member": "sales.site_number",
          "operator": "equals",
          "values": [
            "1",
            "21",
            "6",
            "18"
          ]
        },
        {
          "member": "sales.posting_period",
          "operator": "inDateRange",
          "values": [
            "2022-01-01",
            "2024-06-01"
          ]
        },
        {
          "member": "sales.revenue",
          "operator": "gt",
          "values": [
            "30000"
          ]
        }
      ]
    }
    ```

By adhering to these guidelines, you can avoid common pitfalls and ensure your Lens functions correctly and efficiently.