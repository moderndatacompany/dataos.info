# Do's and Dont's 

This documentation provides guidelines for using Lens functionalities, including when to create views and best practices to avoid errors.

## Do's

### **Data modelling**

#### **Calling a Measure to create another Measure in the same Table**

When creating a measure that references another measure within the same table, use curly braces `{}`.

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

#### **Calling a Measure from another Table**

When referencing a measure from another table, set `sub_query` to `true`.

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


#### **Working with window function**

To correctly aggregate a measure within a window, use the rolling_window parameter when defining the measure. This ensures that any filters applied to the measure are correctly placed in the WHERE clause, which is essential for accurate results. Without rolling_window, filters might go into the HAVING clause, leading to incorrect calculations.

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

- Running totals or moving averages.
- Ranking and percentile analysis (e.g., top performers).
- Time series analysis (e.g., tracking month-over-month growth).
- Comparative analysis (e.g., previous/next values or differences between rows).

### **Views**

1. **Purpose:** Create views to provide a limited part of your data model to the consumer layer, such as any BI tool. Views are useful for defining metrics, managing governance and data access, and controlling ambiguous join paths.
2. **Members:** Views do not have their own members. Instead, use the `table` or `includes` parameters to incorporate measures and dimensions from other tables into the view.
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

#### **Dynamic Segments with secure access**

You can create dynamic segments with secure access using Jinja macros. This example sets up segments for different categories with user group restrictions.

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