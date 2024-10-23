---
search:
  exclude: true
---

# Funnel Analysis

Funnel analysis helps businesses trace users’ journeys as they perform a series of activities that lead toward a defined goal. It helps investigate the activities performed by users, estimates the duration it takes for a user to perform an activity, tracks conversion time from one activity to another, and much more. It is essentially analyzing your core customer activities over time.

To enable funnel analysis, we will be using the Activity Schema. Activity schema makes it reasonably simple to perform funnel analysis, given the complexity of building more straightforward funnels through SQL.

> 🗣 Points to Consider

1. Base entity ‘activity stream’ is connected to Entity 1 and has a 1:N relationship with Entity 1
2. Base entity ‘activity stream’ is extended to create Entity 1 and Entity 2
</aside>

Let’s deep dive into different funnel analysis scenarios 

## Funnel Scenarios

|Theme |Lens YAML |Brief |Entity 1 |Entity 2 |Relationship|
|---|---|---|---|---|---|
|First Ever          |[First Ever Lens](/interfaces/lens/recipes/funnel_analysis/funnel_scenarios/first_ever_lens/) |Identifying the first ever ‘campaign visit’ of all the users who have performed ‘product checkout’                                     |visited_campaign|checked_out_product|1:N         |
|Last Ever           |[Last Ever Lens](/interfaces/lens/recipes/funnel_analysis/funnel_scenarios/last_ever_lens/) |Identifying the last ever ‘campaign visit’ of all the users who have performed ‘product checkout’                                      |visited_campaign|checked_out_product|1:N         |
|First Before        |[First Before Lens](/interfaces/lens/recipes/funnel_analysis/funnel_scenarios/first_before_lens/) |Identifies the first time ‘campaign visited’ occurred only if it happened before ‘checked_out_product’                                 |visited_campaign|checked_out_product|1:N         |
|Last Before         |[Last Before Lens](/interfaces/lens/recipes/funnel_analysis/funnel_scenarios/last_before_lens/) |Identifies the last time ‘campaign visited’ occurred given that it should have happened before ‘checked_out_product’                   |visited_campaign|checked_out_product|1:N         |
|First in Between    |[First in Between Lens](/interfaces/lens/recipes/funnel_analysis/funnel_scenarios/first_in_between_lens/) |Identifies the first time the ‘campaign visited’ activity happened before the next ’checked_out_product’ activity                      |visited_campaign|checked_out_product|1:N         |
|Last in Between     |[Last in Between Lens](/interfaces/lens/recipes/funnel_analysis/funnel_scenarios/last_in_between_lens/) |Identifies the last ‘campaign visit’ that happened before the next ‘checked_out_product’ activity                                      |visited_campaign|checked_out_product|1:N         |
|Aggregate in Between|[Aggregation in Between Lens](/interfaces/lens/recipes/funnel_analysis/funnel_scenarios/aggregation_in_between_lens/)|Calculates an aggregation of all the ‘campaign visit’ activity that happened in between consecutive ‘checked_out_product’ activities.  |visited_campaign|checked_out_product|1:N         |
|Aggregate all Ever  |[Aggregate all Ever Lens](/interfaces/lens/recipes/funnel_analysis/funnel_scenarios/aggregate_all_ever_lens/) |Calculates an aggregation of all the ‘campaign visit’ activity that occurred to date regardless of when ‘checked_out_product’ occurred.|visited_campaign|checked_out_product|1:N         |
|Aggregate Before    |[Aggregate Before Lens](/interfaces/lens/recipes/funnel_analysis/funnel_scenarios/aggregate_before_lens/) |Calculates an aggregation of all the  ‘campaign visits’ that occurred before the checked_out_product’ activity happened                |visited_campaign|checked_out_product|1:N         |
|Aggregate After     |[Aggregate After Lens](/interfaces/lens/recipes/funnel_analysis/funnel_scenarios/aggregate_after_lens/) |Calculates an aggregation of all the  ‘campaign visits’ that occurred after the checked_out_product’ activity happened                 |visited_campaign|checked_out_product|1:N         |