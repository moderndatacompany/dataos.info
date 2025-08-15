---
search:
  exclude: true
---

# First Ever Lens

## First ever

All the users who have performed a ‘checked_out_product’, when was their first ever campaign visit?

Assuming we have a primary activity say “checked_out_product” and secondary activity say “visited_campaign” now we want to find out the first-ever information about the customer where the customer first-ever visited the campaign.

```yaml
name: firstever
contract: test01
owner: iamgroot
entities:
  - name: activitystream
    sql:
      query: SELECT * FROM icebase.entity_360.campaign_stream
      columns:
        - name: ts_
        - name: occurrence
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
        sql_snippet: and ${visitedcampaign.occurence} = 1
        verified: true

  - name: checkedout
    extend: activitystream
    sql:
      query: SELECT * FROM ${activitystream.sql()} where activity = 'checked_out_product'
      columns:
        - name: ts_
        - name: occurrence
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

## Other scenarios you can achieve

- Segment datasets based on the primary ad source (first-touch attribution)
- Segment your datasets according to what they ordered first (split by customer tenure)
- Segment your datasets according to the initial subscription's start date (think retention curves)
- Segment your datasets based on the customer's first-viewed page.