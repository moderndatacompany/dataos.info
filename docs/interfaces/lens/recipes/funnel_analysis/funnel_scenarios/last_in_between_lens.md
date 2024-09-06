---
search:
  exclude: true
---

# Last in Between Lens

Appends the LAST append action that took place between the primary activity in question and the primary activity that follows it. In other words, add the last activity that occurred before the subsequent main activity.

```yaml
name: lastinbetween
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
      - name: secondary_ts
        type: date
        sql_snippet: ${checkedout.sec_ts}
        sub_query: true
      - name: secondary_act
        type: date
        sql_snippet: ${checkedout.sec_activity}
        sub_query: true
      - name: secondary_feature2
        type: date
        sql_snippet: ${checkedout.sec_feature2}
        sub_query: true
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
      - name: sec_ts
        sql_snippet: array_agg(${checkedout.ts_} order by ${checkedout.ts_} desc )[1]
        type: number        
      - name: sec_activity
        sql_snippet: array_agg(${checkedout.activity} order by ${checkedout.ts_} desc )[1]
        type: number
      - name: sec_feature2
        sql_snippet: array_agg(${checkedout.feature2} order by ${checkedout.ts_} desc )[1]
        type: number
```

## Additional Use Cases

- Determine the behavior that resulted in a consumer leaving or abandoning.
- Between each initiated session, find the most recent search word (what caused the customer to leave)
- Between each page view, look for the most recent advertisement.
- Discover the final FAQ page seen by a customer.