---
search:
  exclude: true
---

# Last Before Lens

The last append action that occurred prior to the primary activity was appended.

```yaml
name: lastbefore
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
    relationships:
      - type: 1:N
        field: entity_id
        target:
          name: checkedout
          field: entity_id
        sql_snippet: and ${visitedcampaign.next_occured_at} IS NULL and ${ checkedout.ts_} <= ${visitedcampaign.ts_}
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
        primary: true
      - name: entity_id
        type: string
        sql_snippet: entity_id
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
```

## Additional use case

- Add the most recent support ticket a user sent before quitting to your dataset.
- Add the most recent web page they visited before submitting a support issue to your dataset.
- Sort your data according to the last email they opened before making a purchase Sort your data according to the last session's ad source (last-touch attribution)