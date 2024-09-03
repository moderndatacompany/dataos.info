---
title: Working with Views
search:
  exclude: true
---

# Working with Views

## Views in Lens

- Views serve as a layer atop the data graph of tables, presenting an abstraction of the entire data model for consumers to interact.
- They serve as a layer for defining metrics, providing a simplified interface for end-users to interact objectively with key metrics instead of the entire data model
- View reference dimensions, measures, and segments from multiple logical tables. It doesn’t have any measure, dimension, or segment of its own.

## When to Define Views?

- **Defining Metrics**: Views allow you to define metrics by including measures and dimensions from different tables. This enables you to create denormalized tables that comprehensively address a specific use case. For instance, you can have a view that gives you all the dimensions and measures to understand ‘Weekly Spirits Sales in Florida’
- **Providing a Simplified Interface**: By exposing only the relevant measures and dimensions, views make it easier for users to understand and query the data, reducing the complexity of the underlying data model.

## How to Define Views?

<aside>
💡 You can also expose a view to create operational boards ‘Iris Board’ to monitor key metrics. Learn more about it [here](https://www.notion.so/Consuming-Lens-Views-via-Iris-board-92d1e436fe79476ab85a967112fe4ea8?pvs=21)

</aside>

**Syntax:**

```yaml
views:
  - name: # name of the view 
    description: # description of the view
    public: # set this property as 'true' or 'false' to control the visibility
    meta: # metadata properties to export views to Iris board
      export_to_board: true # set this property to true if you want to export the view 
      board:
        timeseries: sales.posting_date # define a time dimension to be used to create the time-series chart
        includes: # define the list of dimensions/measures to be included in the board
        excludes: # define the list of dimensions/measures to be excluded from the board
   

    # An array where you can refer to multiple tables. 
    # List the tables whose measure and dimensions need to be included in the view
    tables:
      - join_path: # the name of the table
        prefix: false
        includes: # dimension/measure from the table that should be part of the view
        excludes: # dimension/measure from the table that should be part of the view
        
```

**Example:**

```yaml
  - name: generated_sales_across_territory
    description: View containing total and average sales for different territories
    public: true
    meta:
      export_to_board: false 

    tables:
      - join_path: sales_order_header
        prefix: true
        includes:
          - total_sales_amount
          - average_order_value
          - total_orders_count
          - order_mode
          - online_sales

      - join_path: sales_person
        prefix: true
        includes: "*"
        excludes:
          - territory_id
```