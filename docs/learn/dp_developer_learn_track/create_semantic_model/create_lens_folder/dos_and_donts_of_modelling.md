# Do's and Dont's 

This section outlines essential Do's and Don'ts for using Lens functionalities. Following these guidelines will help you avoid common mistakes, ensure proper usage, and create efficient, maintainable data models.

## Do's

### **Data modelling**

#### **Referencing One Measure to Create Another Measure Within the Same Table**

When referencing a measure in the same table, always enclose the reference in curly braces {}. This ensures the reference is correctly interpreted and used in calculations.

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

#### **Proxy Dimension: Referencing Dimensions from another Table**

To reference a dimension from one table while creating a measure in another, enclose the dimension name in curly braces {}. If the dimension is from a different table, use the format {table_name.column_name}. If it is from the same table, simply use {column_name}.

**Example:** In the example, {ext_net} is referenced directly since it exists within the same table, while {sales.ref_dimension} includes the table name (sales) because the dimension is from another table. This allows you to reference columns from different tables in a single measure.

```yaml
- name: ref_dimension_cust
  sql: "{account.state}"
  type: string

measures:
  - name: ref_measure
    sql: case when {sales.ref_dimension} like '%w%' then **{ext_net}** end
    type: sum
```

#### **Calling a Measure from another Table**

When referencing a measure from another table, set `sub_query` to `true` to indicate that the measure is sourced from another table, ensuring the correct retrieval of data.

```yaml
- name: subq_rev
  sql: "{sales.total_revenue}"
  sub_query: true
  type: number
```

#### **Transforming Dimension and calling it in a Measure**

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
### **Rolling window**

- Use rolling windows for running totals or moving averages.

- Apply rolling windows for ranking and percentile analysis (e.g., top performers).

- Leverage rolling windows for time series analysis (e.g., tracking month-over-month growth).

- Use rolling windows for comparative analysis (e.g., previous/next values or differences between rows).


### **Working with window function**

To correctly aggregate a measure within a window, use the `rolling_window` parameter when defining the measure. This ensures that any filters applied to the measure are correctly placed in the WHERE clause, which is essential for accurate results. Without `rolling_window`, filters might go into the HAVING clause, leading to incorrect calculations.

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


### **Views**

- Views are helpful for defining metrics, managing data governance, controlling access, and resolving ambiguous join paths. Create views to expose a subset of your data model to consumer layers like BI tools. 

- Use the `table` or `includes` attribute in views to pull measures and dimensions from other tables, as views don’t have members of their own.

- Implement a refresh key in your views if the underlying data is regularly updated.

- To join other tables in a view, use the `join_path` and `includes` attribute to specify how tables should be joined.

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

Declare macros before use to avoid errors in the model. This allows you to generate dynamic SQL or configuration snippets.
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
    description: Table containing information about account
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

Leverage macros for `sql` properties to generate complex SQL code, like handling edge cases (e.g., division by zero) across multiple measures. For example, to avoid division by zero errors when creating measures, define a macro and use it in multiple measures.

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

#### **Dynamic Segments with secure access**

Use Jinja macros for dynamic segments to apply dynamic SQL logic with secure access control, like restricting access based on user groups. This example sets up segments for different categories with user group restrictions.

**Example:**

```yaml
{%- set categories = ["Wine", "Beer", "Spirits", "NAB"] -%}

segments:
  {% for name in categories %}
    - name: {{ "segment_" ~ name }}
      public: true
      sql: {{ "{category_name} = '" ~ name ~ "'" }}
      meta:
        secure:
          user_groups:
            includes:
              - {{ name }}
            excludes:
              - default
  {% endfor %}
```

#### **User Group Configuration**

```yaml
user_groups:
  - name: Wine
    api_scopes:
      - meta
      - data
      - graphql
      # - jobs
      # - source
    includes:
      - users:id:***
      - users:id:***
      - users:id:***
  - name: Beer
    api_scopes:
      - meta
      - data
      - graphql
      # - jobs
      # - source
    includes:
      - users:id:***
      - users:id:***
  - name: Spirits
    api_scopes:
      - meta
      - data
      - graphql
      # - jobs
      # - source
    includes:
      - users:id:***
      - users:id:***
      - users:id:***
  - name: NAB
    api_scopes:
      - meta
      - data
      - graphql
      # - jobs
      # - source
    includes:
      - users:id:***
      - users:id:***
  - name: default
    includes: "*"
    api_scopes:
      - meta
      - data
      - graphql
      # - jobs
      # - source
```

By leveraging Jinja macros, you can create efficient, reusable, and dynamic configurations in your Lens data models.

## Don’t

When creating Lens, avoid the following practices to ensure functionality and maintainability:

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

### **Avoid using single quotes in Measures, Dimensions, and Segments**

Using single quotes can throw errors. Instead, use double quotes.

```yaml
tables:
  - name: order
    sql: {{ load_sql('order') }}
    description: Table containing information about product
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

### **Avoid filtering Measures and Dimensions from the same Table with OR operator**

Measures and dimensions from the same table cannot be filtered simultaneously using the 'OR' operator.

=== "Incorrect Example"

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
      "timeDimensions": [],
      "limit": 10,
      "offset": 0
    }
    ```

=== "Correct Example"

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