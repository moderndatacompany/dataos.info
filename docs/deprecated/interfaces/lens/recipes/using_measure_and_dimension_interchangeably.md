---
search:
  exclude: true
---

# Using Measure and Dimension Interchangeably

You can interchangeably call and use a measure or a dimension within a lens. There can be different scenarios where you would refer to measures or dimensions conversely within or between entities. Let's look at a few scenarios

## Referencing measures to build a new measure within the same entity.

> If you want to define a measure, instead of writing a SQL snippet you can use pre-defined measures to calculate the new measure.


"What's the average purchase value of a user?", such questions require calculating the ratio of total revenue to total orders. Referencing predefined measure definitions makes such computations manageable. The below example illustrates how a reference to a measure can be made within the definition of another measure.

```yaml
	 # Calling a measure inside another measure within the same entity.
   
   measures:
	 		- name: total_revenue
        sql_snippet: sum(${order.order_net_amt})
        type: number
			- name: total_orders
        sql_snippet: ${order.order_no}
        type: count_distinct
        description: Count of Orders

	 # referencing measures total_revenue and total_orders to calculate avg_order_value
     
		  - name: avg_order_value 
        sql_snippet: round(${order.total_revenue}/nullif(cast(${order.total_orders} as double),0),2)
        type: number
        description: Average order value = total revenue/total no. of orders
```

## Referencing a measure to create a dimension within another entity

> A measure can be referred to as a dimension in Lens. You can refer to one or more measures to define a dimension.

When referencing measures from other entities inside a dimension, you need to use subquery dimensions, i.e. make subquery = true in those dimensions. It leverages joins to build a correlated subquery in the resultant SQL.

In order to define a subquery dimension, it is imperative to first define measures in their respective entities. Once a measure is defined, it can then be referenced from a subquery dimension over a join.

```yaml
entities:
  - name: customer
    sql:
     -----
        
    fields:
     -----
    # measure recency is used to define the dimension days_since_last_order
    dimensions:     
			- name: days_since_last_order
				sql_snippet:  ${order_placed.recency}
        type: number
        sub_query: true
    ----
    relationship:
    ----

  - name: order_placed
    sql:
      ----
    fields:
      ----
    dimensions:
      ----
    measures:
      - name: recency
        sql_snippet: day(current_date - ${order_placed.activity_ts})
        type: min
        description: days since last order was placed
```

## Referencing a measure in another entity to define a new measure

> You cannot directly reference a measure in another entity to create a new measure. The measure can be indirectly referenced through subquery dimensions within another entity to define a new measure. This gives you the flexibility to reference a measure over a join from another entity.

> 🗣 Subquery dimensions can be further used to define another measure within the same entity.

For defining a measure, you need to create a subquery dimension, which can then be referenced to create a new measure.

```yaml
entities:
  - name: customer
    sql:
      ----
    fields:
      ----
    # defining a subquery dimension using a measure defined in another entity

    dimensions:     
    # referencing 'recency' measure defined in order_placed entity 
      - name: days_since_last_order
        sql_snippet:  ${order_placed.recency}
        type: number
        sub_query: true

    # referencing subquery dimension to define measure 'revenue' within customer entity
    measures:
      - name: revenue
        sql_snippet: ${customer.total_value}
        type: sum

    relationships:
      - type: 1:N
        field: customer_id
        target:
          name: order_placed
          field: entity_id
        verified: true

  - name: order_placed
    sql:
      ----
    fields:
      ----
    dimensions:
      ----
    measures:
      - name: recency
        sql_snippet: day(current_date - ${order_placed.activity_ts})
        type: min
        description: days since last order was placed
```