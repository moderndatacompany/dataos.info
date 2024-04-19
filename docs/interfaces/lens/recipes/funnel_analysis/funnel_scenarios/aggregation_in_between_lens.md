# Aggregation in Between Lens

Adds a GROUPING of all the append actions that took place between the primary activity in question and the primary activity that follows it.

```yaml
name: agginbetween
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
        sql_snippet: uuid
      - name: ts_
        type: date
        sql_snippet: ts
        primary: true
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
      - name: occurence
        type: number
        sql_snippet: occurence
      - name: ts_
        type: date
        sql_snippet: ts
        primary: true
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
    relationships:
      - type: 1:N
        field: entity_id
        target:
          name: checkedout
          field: entity_id
        sql_snippet: (${checkedout.ts_} BETWEEN ${visitedcampaign.ts_} AND ${visitedcampaign.next_occured_at}) OR (${checkedout.ts_} > ${visitedcampaign.ts_} AND ${visitedcampaign.next_occured_at} IS NULL))
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
      - name: occurence
        type: number
        sql_snippet: occurence
      - name: ts_
        type: date
        sql_snippet: ts
        primary: true
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
        sql_snippet: ${checkedout.entity_id}
        type: count
```

## Additional Use Cases

- Add the COUNT of all pages that were seen between began sessions to your dataset (total page views per session)
- Include the SUM of the revenue from all active subscriptions in your dataset (subscription revenue).
- Add the COUNT of all events that were present between each received an invoice to your dataset (How many events did they attend per active month)
- The COUNT DISTINCT of all Viewed Product Kinds between each Session will enrich your dataset (How many unique product kinds did the user view )