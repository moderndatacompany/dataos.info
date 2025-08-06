# Handling Row Multiplication in Relationships

In Lens, relationships are used to join entities and manage data model complexity. However, improper relationship definitions—especially in many-to-one relationship—can result in unintended row multiplication during query execution.

When a many-to-one (`N:1`) relationship is defined between a primary entity and a secondary entity, and the primary entity has multiple matching rows for a single row in the secondary entity, duplicate rows may appear in the query output.

## Example Scenario

Consider the following example where the `order` entity maintains an `N:1` relationship with the `clickstream` entity:

```yaml
name: retail
# ...
entities:
  - name: order
    sql:
    # ...
    fields:
      - name: order_id
        type: string
        column: order_id
        primary: true
    #   ...
    dimensions:
      - name: year
        type: number
        sql_snippet: year(${transaction.created_on})
      - name: month
        type: number
        sql_snippet: year(${transaction.created_on})
      - name: duration
        type: number
        sql_snippet: day(current_date - ${transaction.created_on})
      - name: received_any_campaign
        type: string
        sql_snippet: case when created_on not between current_date and current_date + interval '-2' month and campaign_id is null then true else false end
    measures:
      - name: avg_order_amount
        sql_snippet: ${transaction.saleprice} * ${transaction.quantity}
        type: avg
      - name: order_count
        sql_snippet: ${transaction.order_id}
        type: count_distinct
      - name: user_count
        sql_snippet: ${transaction.customer_index}
        type: count_distinct
      - name: last_purchase
        sql_snippet: (day(current_date - ${transaction.created_on}))
        type: min
    relationships:
      - type: N:1
        field: order_id
        target:
          name: clickstream
          field: order_id
        verified: true
```

Within the `clickstream` entity, a dimension `order_id_clickstream` is defined, referencing the `order_id` from the `order` entity:

```yaml
  - name: clickstream
    sql:
      query: >
        SELECT
          *,
          max(order_id) OVER (PARTITION BY session_id) AS order_id_session_wise,
          row_number() OVER (PARTITION BY session_id ORDER BY created_on) AS row_num,
          lag(created_on) OVER (PARTITION BY session_id ORDER BY created_on) AS last_act_time
        FROM icebase.campaign.click_stream
    columns:
    #   ...
    #   ...
    fields:
      - name: created_on
        type: date
        primary: true
        column: created_on
      - name: sku_id
        type: string
        column: sku_id
      - name: customer_index
        type: number
        column: customer_index
      - name: session_id
        type: string
        column: session_id
      - name: order_id
        type: string
        column: order_id
    dimensions:
      - name: order_id_clickstream
        sql_snippet: ${transaction.order_id}
        type: string
    measures:
      - name: abc
        sql_snippet: ${clickstream.order_id_clickstream}
        type: count
```

The following query demonstrates the issue:

```sql
select * from lens(select clickstream.abc from retail)
```

In this scenario, multiple rows may be returned for the `order_id_clickstream` dimension, even if a single row is expected. This occurs because the referenced `order_id` in the `clickstream` entity relates to multiple records in the `order` entity due to the `N:1` relationship configuration. This causes row multiplication.

## Solution: Use a 1:1 Relationship

To resolve the row multiplication issue, the relationship should be redefined as one-to-one (`1:1`). This instructs Lens to treat each matching row in the target entity as uniquely aligned with a single row in the referencing entity.

### Updated Relationship Configuration

```yaml
relationships:
  - type: 1:1
    field: order_id
    target:
      name: clickstream
      field: order_id
    verified: true
```

By redefining the relationship as `1:1`, the data model assumes a one-to-one mapping between `order_id` in the `order` and `clickstream` entities. This prevents unintended row expansion during aggregation or dimension reference resolution.

