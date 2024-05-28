# Dimensions

Dimensions are categorical or qualitative data describing measures at different granularity levels. You can drill down into the dataset using dimensions to filter your query results further. Dimensions can be used when defining a custom column.

Other than stating the description and type for a dimension, you can use properties like subquery to reference measures from other entities inside a dimension. It behaves like your typical correlated subqueries. Subquery dimensions can be referenced as a usual dimension in measures.

## Properties

### `name`

Similar to naming entities and fields, following rules can be adopted when naming dimensions.

- The dimension name should start with a lowercase letter.
- It can contain a letter, number, or ‘_’
- It needs a minimum length of 2 characters and cannot exceed 128 characters.

### `description`

To better understand the defined dimension, descriptions can be added. They also add clarity around its purpose and usage.

### `type`

You can assign various types to a dimension. Dimension’s expected value type includes -

`string`, `number`, `date`, `bool`

| Type | Description |
| --- | --- |
| string | Typically used when the dimension contains letters or special characters.  |
| number | Dimension containing an integer or number can be assigned the type number. |
| date | Use a date type for the dimension if the SQL expression expects to return a value of the type date. |
| bool | Used when a dimension contains boolean values |

### `sql_snippet`

You can add any valid SQL expression to define a dimension. A field, dimension, or measure must already be defined if referenced while defining a dimension.

```yaml
entity:
 - name: product
   sql:
     - query: SELECT * FROM icebase.test.products
     ---
     ---
   ---
   dimensions:
     - name: duration
       type: number
       sql_snippet: day(current_date - created_on)
```

### `sub_query`

Within the dimension, you can use the subquery feature to reference measures from other entities. 

> 🗣 Note: sub_query can only be used to refer to a measure.

In this example, we are referencing the measure sum_amount in dimension total.

```yaml
name: sample
contract: test01
owner: xxx
entities:
  - name: order
    sql:
      query: SELECT * FROM icebase.retail.orders
    fields:
			------
			------
    dimensions:
			------
		measures:
		 - name: sum_amount
		   type: sum
			 sql_snippet: order_amount
		
			
	- name: customer
		sql:
			query: SELECT * FROM icebase.retail.customers
		fields:
			------
			------
		dimensions:
	    - name: total
        type: number
				sql_snippet: $(order.sum_amount)
				sub_query: true
```

A correlated subquery in SQL will look like this -

```sql
SELECT 
    customer_name,
    city,
    (SELECT SUM(order_amount) , customer_id
     FROM orders
     JOIN customers ON orders.customer_id = customers.id) as total
FROM
    customers group by customer_id
ORDER BY total DESC
LIMIT 5;
```

### `hidden`

Hidden can be used to hide a dimension from the User Interface. Dimensions mainly used for deriving another dimension or measure and not needed for exploration can be hidden.