---
search:
  exclude: true
---

# First in Between Lens

Adds the FIRST append activity that took place BETWEEN that primary activity and its subsequent occurrence. Or, to put it another way, add the initial activity that took place before the next main activity.

```yaml
name: firstinbetween
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
        sql_snippet: array_agg(${checkedout.ts_} order by ${checkedout.ts_} asc )[1]
        type: number
      - name: sec_activity
        sql_snippet: array_agg(${checkedout.activity} order by ${checkedout.ts_} asc )[1]
        type: number
      - name: sec_feature2
        sql_snippet: array_agg(${checkedout.feature2} order by ${checkedout.ts_} asc )[1]
        type: number
```