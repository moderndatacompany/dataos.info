# Working with Segments

!!! info "Quick Guide"
    To quickly get started with segments, click [here](/quick_guides/working_with_segments/). This guide walks you through defining and applying segments in Lens, which can be used during analysis. Segments help save time and make your complex filtering logic reusable.
 


## When to use Segments?

- **Complex Filtering Logic**: Segments are ideal for defining complex filtering logic in SQL that can be reused across multiple queries.

- **Reusability**: When you observe the reuse of common filters across various queries. Where the value of the filter doesn’t vary much.

## How to define Segments?

Segments are pre-defined groups of filters. It provides the ability to define Segments (filters) as code within the Lens YAML. They can be used to define repetitively used groups of filters by the stakeholders. Segments are defined within a Lens table’s schema.

- Utilize the **`sql`** parameter to define how a segment filters out a subset of data, ensuring the SQL expression is valid within a **`WHERE`** statement.
- You can use ‘OR’ to define a filter involving multiple columns

An example segment declaration to create a group of commonly used state filters:

```yaml
    segments:
      - name: common_state
        sql: "{TABLE}.state = 'Illinois' or {TABLE}.state = 'Ohio'"
```

You can leverage filtering keywords such as ‘LIKE’ to define filtering criteria

```yaml
    segments:
      - name: common_state
        sql: "{TABLE}.state = 'Illinois' or {TABLE}.state like '%Ohio%'"
```

