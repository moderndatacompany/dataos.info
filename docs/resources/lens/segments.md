# Working with Segments

!!! abstract "Quick Guide"
    To quickly get started with segments, follow the [quick guide on working with segments](/quick_guides/segments/). This quick guide walks you through defining and applying segments in Lens that can be used during analysis. With segments, you can save time and make your complex filtering logic reusable.


## When to use Segments?

- **Complex Filtering Logic**: Segments are ideal for defining complex filtering logic in SQL that can be reused across multiple queries.

- **Reusability**: When you observe the reuse of common filters across various queries. Where the value of the filter doesn’t vary much.

## How to define Segments?

Segments are pre-defined groups of filters. It provides the ability to define Segments (filters) as code within the Lens YAML. They can be used to define repetitively used groups of filters by the stakeholders. Segments are defined within a Lens table’s schema. Utilize the **`sql`** parameter to define how a segment filters out a subset of data, ensuring the SQL expression is valid within a **`WHERE`** statement.

- Use ‘OR’ to define a filter involving multiple columns

    An example segment declaration to create a group of commonly used state filters:

    ```yaml
    segments:
      - name: common_state
        sql: "{TABLE}.state = 'Illinois'"
    ```

- You can leverage filtering keywords such as `LIKE` to define filtering criteria
  
    Below  example Segment filters for records where the state is Illinois or Ohio.

    ```yaml
    segments:
      - name: common_state
        sql: "{TABLE}.state = 'Illinois' or {TABLE}.state like '%Ohio%'"
    ```

- You can include logical operators like `OR` and `AND` to create dynamic criteria for segments. This is useful when you need to apply filters to more than one column.

    Below example Segment filters records where the state is "Illinois" or the sales is equal to 1000.

    ```yaml
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

Data policies can be defined directly on segments to enforce data governance and compliance. This ensures that access and interaction with different subsets of data are managed effectively. It applies a row filter data policy to show specific data based on user groups.

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
