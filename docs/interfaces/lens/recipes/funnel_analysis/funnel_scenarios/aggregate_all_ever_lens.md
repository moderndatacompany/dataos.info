# Aggregate all Ever Lens

Regardless of when the primary activity took place, appends an aggregation of all append activities that happened ever.

```yaml
name: aggallever
contract: test01
owner: iamgroot
entities:
  - name: activitystream
    sql:
      query: SELECT * FROM icebase.entity_360.campaign_stream
      columns:
        - name: ts_
        - name: occurence
        - name: entity_id
      verified: true
      tables:
        - icebase.entity_360.campaign_stream
    fields:
      - name: uuid
        type: string
        primary: true
        sql_snippet: uuid
      - name: ts_
        type: date
        sql_snippet: ts
      - name: entity_id
        type: string
        sql_snippet: entity_id
      - name: activity
        type: string
        sql_snippet: activity
      - name: occurence
        type: number
        sql_snippet: occurence
      - name: next_occured_at
        type: date
        sql_snippet: next_occured_at
      - name: feature1
        type: string
        sql_snippet: feature1
      - name: feature2
        type: string
        sql_snippet: feature2
      - name: feature3
        type: string
        sql_snippet: feature3

  - name: visitedcampaign
    extend: activitystream
    sql:
      query: SELECT * FROM ${activitystream.sql()} where activity = 'visited_campaign'
      columns:
        - name: ts_
        - name: occurence
        - name: entity_id
      tables:
        - icebase.entity_360.campaign_stream
    fields:
      - name: uuid
        type: string
        sql_snippet: uuid
      - name: entity_id
        type: string
        sql_snippet: entity_id
        primary: true
      - name: occurence
        type: number
        sql_snippet: occurence
      - name: ts_
        type: date
        sql_snippet: ts
      - name: activity
        type: string
        sql_snippet: activity
      - name: next_occured_at
        type: date
        sql_snippet: next_occured_at
      - name: feature1
        type: string
        sql_snippet: feature1
      - name: feature2
        type: string
        sql_snippet: feature2
      - name: feature3
        type: string
        sql_snippet: feature3
      - name: count_of_product
        type: number
        sql_snippet: ${checkedout.count_of_feature2}
        sub_query: true
      - name: sum_of_revenue
        type: number
        sql_snippet: ${checkedout.sum_of_feature3}
        sub_query: true
    measures:
      - name: avg_of_count
        sql_snippet: ${ENTITY.count_of_product}
        type: avg
    relationships:
      - type: 1:N
        field: entity_id
        target:
          name: checkedout
          field: entity_id
        verified: true

  - name: checkedout
    extend: activitystream
    sql:
      query: SELECT * FROM ${activitystream.sql()} where activity = 'checked_out_product'
      columns:
        - name: ts_
        - name: occurence
        - name: entity_id
      tables:
        - icebase.entity_360.campaign_stream
    fields:
      - name: uuid
        type: string
        sql_snippet: uuid
      - name: entity_id
        type: string
        sql_snippet: entity_id
        primary: true
      - name: occurence
        type: number
        sql_snippet: occurence
      - name: ts_
        type: date
        sql_snippet: ts
      - name: activity
        type: string
        sql_snippet: activity
      - name: next_occured_at
        type: date
        sql_snippet: next_occured_at
      - name: feature1
        type: string
        sql_snippet: feature1
      - name: feature2
        type: string
        sql_snippet: feature2
      - name: feature3
        type: string
        sql_snippet: feature3
    measures:
      - name: count_of_feature2
        sql_snippet: ${ENTITY.feature2}
        type: count
      - name: sum_of_feature3
        sql_snippet: cast(${ENTITY.feature3} as integer)
        type: count
```

## Additional Use Case

- Add the SUM of the revenue from all purchased products to your dataset to make it richer (LTV)
- Include the COUNT of all paid invoices in your dataset (Total active months)
- Include the COUNT of all Tickets in your dataset (How many tickets did this customer submit)