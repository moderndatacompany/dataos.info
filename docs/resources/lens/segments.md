# Working with Segments

!!! abstract "Quick Guide"
    To quickly get started with segments, follow the [quick guide on working with segments](/quick_guides/working_with_segments/). This quick guide walks you through defining and applying segments in Lens that can be used during analysis. With segments, you can save time and make your complex filtering logic reusable.


## When to use Segments?

Use segments when you notice the same filter conditions—especially those involving specific values or complex logic—being applied repeatedly across multiple queries or dashboards.

## How to define Segments?

Segments are reusable filters defined in the `segment` section within the table manifest of the semantic model. They allow stakeholders to apply common filtering logic consistently across multiple queries, just like how a `WHERE` clause works in SQL. Use the `sql` parameter to specify the filter expression.

An example segment declaration to create the `Illinois` segment filters the dataset to include only rows where the state column has the value 'Illinois'.

```yaml
segments:
  - name: common_state
    sql: "{TABLE}.state = 'Illinois'"
```

Use ‘OR’ to define a filter involving multiple columns.

```yaml
segments:
  - name: common_state
    sql: "{TABLE}.state = 'Illinois' or {TABLE}.state = 'Ohio'"
```

Leverage filtering keywords such as `LIKE` to define filtering criteria.
  
```yaml
segments:
  - name: common_state
    sql: "{TABLE}.state = 'Illinois' or {TABLE}.state like '%Ohio%'"
```

Use `AND` to create dynamic criteria for segments. 

```yaml
# The common_state_and_salary segment filters the dataset to include only rows where the state is 'Illinois' and the sales value is '1000'.
segments:
- name: common_state_and_salary
  sql: "{TABLE}.state = 'Illinois' and {TABLE}.sales = '1000'"
``` 

<!-- - Use `In` operator to filter multiple values for a column. It is a short hand for multiple `OR` conditions.

    An example segment declaration to filter for records where the state is either Illinois or Ohio:

    ```yaml
    segments:
    - name: common_multiple_state
      sql: "{TABLE}.state = 'Illinois' and {TABLE}.sales = '1000'"
    ```  -->


## Defining row filter policy on Segment

Data policies can be defined directly on segments to enforce data governance and compliance. This ensures that access and interaction with different subsets of data are managed effectively. It applies a row filter data policy to filter specific data based on user groups.

Let's demonstrate an example by adding the filter policy to the `segments` section of a table definition:

**Example:** Filtering rows to show online sales data to '`type-analyst` user groups and hide  `reader` user groups.

  ```yaml
  table: 

    #...

    segments:
      - name: online_sales
        sql: "{TABLE}.order_mode = 'online'"
        meta:
          secure:
            user_groups:
              includes:
                - reader
              excludes:
                - type-analyst
  ```
