# Best Practices

## Naming Conventions

**Common Rules**

- Names must start with a letter.
- Names can include letters, numbers, and underscore (`_`) symbols only.

<aside class="callout">
💡 <b>Recommended:</b> Use <b>snake_case</b> for naming.

</aside>

**Examples**

- Tables: `orders`, `stripe_invoices`, `base_payments`
- Views: `opportunities`, `cloud_accounts`, `arr`
- Measures: `count`, `avg_price`, `total_amount_shipped`
- Dimensions: `name`, `is_shipped`, `created_at`
- Pre-aggregations: `main`, `orders_by_status`, `lambda_invoices`

---

## SQL Expressions

### **Data Source Dialect**

When defining tables, you often provide SQL snippets in the `sql` parameter. These SQL expressions should match your data-source SQL dialect.

**Examples**

- In Snowflake, use the [`LISTAGG` function](https://docs.snowflake.com/en/sql-reference/functions/listagg) to aggregate a list of strings.
- In BigQuery, use the [`STRING_AGG` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#string_agg).

Here’s an example for defining a table with SQL snippets:

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
        sql: "listagg({TABLE.status}) WITHIN GROUP (ORDER BY {TABLE.status})"
        type: string

    dimensions:
      - name: status
        sql: "UPPER(status)"
        type: string
```

### **Case Sensitivity**

If your database uses case-sensitive identifiers, ensure you properly quote table and column names.

For example, to reference a Postgres table with uppercase letters:

```sql
SELECT
  site_number,
  site_name,
  site_region
FROM
  'public."Site"'
```

---

## References

To create reusable data models, it is essential to reference members of tables and views, such as measures or dimensions, as well as columns. Lens supports the following syntax for references:

### **column**

Prefix table column references with the table name or use the `TABLE` constant when referring to the current table's column.

In most cases, use bare column names in the `sql` parameter of measures or dimensions. For example, the `name` references the respective column of the users table. 

```yaml
tables:
  - name: order
    sql: {{ load_sql('order') }}
    description: Table containing information about orders
    public: true
    meta:
      export_to_board: false

    dimensions:
      - name: status
        sql: status
        type: string
```

This works well for simple cases. However, if your tables have joins and the joined tables have columns with the same name, the generated SQL query might become ambiguous. Here’s how to avoid that:

**`{member}`**

When defining measures and dimensions, you can reference other members of the same table by wrapping their names in curly braces.

In the example below, the `full_name` dimension references the `name` and `surname` dimensions of the same table.

```yaml
tables:
  - name: customer
    sql: {{ load_sql('customer') }}
    description: Table containing information about customers
    public: true
    meta:
      export_to_board: false
    dimensions:
      - name: name
        sql: name
        type: string

      - name: surname
        sql: "UPPER(surname)"
        type: string

      - name: full_name
        sql: "CONCAT({name}, ' ', {surname})"
        type: string
```

For cases where you need to reference members of other tables, see the example below:

```yaml
tables:
  - name: customer
    sql: {{ load_sql('customer') }}
    description: Table containing information about customers
    public: true
    meta:
      export_to_board: false
  dimensions:
    - name: name
      sql: name
      type: string

    - name: subq_rev
      sql: "{sales.total_revenue}"
      sub_query: true
      type: number
```

**`{tablename}.column` and `{tablename.member}`**

Qualify column and member names with the table name to remove ambiguity when tables are joined and reference members of other tables.

```yaml
tables:
  - name: users
    sql: {{ load_sql('users') }}

    joins:
      - name: contacts
        sql: "{users}.contact_id = {contacts.id}"
        relationship: one_to_one

    dimensions:
      - name: id
        sql: "{users}.id"
        type: number
        primary_key: true

      - name: name
        sql: "COALESCE({users.name}, {contacts.name})"
        type: string
```

```yaml
tables:
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

<aside class="callout">
🗣 Using fully-qualified names is encouraged in production as it removes ambiguity and keeps the data model code maintainable.
</aside>

However, always referring to the current table by its name can lead to code repetition. Here’s how to solve that:

**`{TABLE}` Variable**

Use the `{TABLE}` variable to reference the current table, avoiding the need to repeat its name.

```yaml
tables:
  - name: users
    sql: {{ load_sql('users') }}

    joins:
      - name: contacts
        sql: "{TABLE}.contact_id = {contacts.id}"
        relationship: one_to_one

    dimensions:
      - name: id
        sql: "{TABLE}.id"
        type: number
        primary_key: true

      - name: name
        sql: "COALESCE({TABLE.name}, {contacts.name})"
        type: string
```

```yaml
tables:
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

Using the `{TABLE}` variable keeps the data model code DRY and easy to maintain.

<aside class="callout">
🗣 <b>Recommended:</b> Use the <b>`TABLE`</b> context variable to reference columns or members of the current table.

</aside>

For more examples, refer to [Do’s And Don’ts](/resources/lens/data_modelling/do's_and_dont's/).

### **Non-SQL References**

Outside the `sql` parameter, `column` is not recognized as a column name but as a member name. This means you can reference members directly by their names without using curly braces: `member`, `table_name.member`, or `TABLE.member`.

```yaml
tables:
  - name: users
    sql: {{ load_sql('users') }}

    dimensions:
      - name: status
        sql: status
        type: string

    measures:
      - name: count
        type: count

    pre_aggregations:
      - name: orders_by_status
        dimensions:
          - TABLE.status
        measures:
          - TABLE.count
```

<aside class="callout">
🗣 <b>Recommended:</b> Use the <b>`TABLE`</b> context variable to reference dimensions or measures of the current table, ensuring your data model code remains DRY and easy to maintain.

</aside>

## Partitioning

1. **Optimal Query Performance:** Partitions should be small so that the Lens workers can process them in less time. Start with a relatively large partition (e.g., yearly) and adjust as needed.
2. **Avoid Partition Queueing:** To minimize queueing, make refresh keys as infrequent as possible.


## Payload Edit

For more information on handling JSON payloads, refer to [Working with Payload](/resources/lens/data_modelling/working_with_payload/).

## Commenting in SQL Files

**Guideline:**

- Add comments on a new line within the query.
- For end-of-query comments, leave two blank lines before the comment.

```sql
SELECT
  customer_key,
  prefix,
  first_name,
  last_name,
  to_timestamp(birth_date) as birth_date,
  marital_status,
  gender,
  email_address,
  annual_income,
  total_children,
  education_level,
  occupation,
  home_owner
  -- ,'test' as test
FROM
  icebase.sports.sample_customer

-- where occupation in ('service','business')
```