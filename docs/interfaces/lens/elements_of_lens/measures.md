# Measures

A measure is an aggregated column that helps define business-specific metrics.

## Properties

### `name`

For naming a measure, the following rules should be adopted.

- Measure’s name should start with a lowercase letter.
- It can contain a letter, number, or ‘_’
- It needs a minimum length of 2 characters and cannot exceed 128 characters.

### `description`

Adding descriptions about a measure helps bring consensus between teams around the measure definition. 

### `type`

You can work with different types when defining measures. The `sql_snippet` parameter is required for all measures. You can reference a column directly, specify the aggregate type, or specify SQL expression to calculate a measure.

Supported measure types:

| Type | Description |
| --- | --- |
| number | All numerical values returned after expression execution. |
| count | Count of all values. |
| count_distinct | Count all distinct values. |
| count_distinct_approx | Gives an approx count of values in a column. |
| sum | Calculate the sum across all values. |
| average | Calculate the average across all values. |
| min | Calculate minimum across all values. |
| max | Calculate maximum across all values. |
| running_total | Calculates cumulative sum. The granularity will return the value's sum if it is not defined. |

Let’s dive into different types that can be assigned to a measure

### `number`

A valid SQL expression that returns a number or an integer can be assigned a number type. You can use a ‘number’ type measure if your expression results in an aggregated value.

```yaml
measure:
 - name: add_to_cart_activity_frequency
   type: number
   sql_snippet: count_if (events_event_name = 'Add_to_Cart')
```

### `count`

Gives the count of values for a column. It’s similar to the SQL count function. It accepts a valid sql expression as long as it returns a column. The count type expects a column.

```yaml

	entity:
- name: product
  sql:
   - query: SELECT * FROM icebase.test.products
   ----
   ----
	fields:
	 - name: quantity
     type: number
     column: quantity
   ----
   ----
	measure:
	 - name: total_quantity
	   type: count
	   sql_snippet: ${product.quantity)
```

### `count_distinct`

Measure declared as type ‘count_distinct’ calculates the count of unique values within a column. Measure type ‘count_distinct’ expects a column from the sql_snippet.

### `count_distinct_approx`

Measure declared as type ‘count_distinct_approx’ returns the approximate number of unique non-null values. It provides responsiveness in cases where the dataset is large, and there are large no. of distinct values.

### `sum`

Measure declared as type ‘sum’ calculates the sum of values within a column. Measure type ‘sum’ expects a column from the sql_snippet.

```yaml
# measure to calculate total sales
measure:
 - name: total_sales
   sql_snippet: ${orders.amount)
   type: sum
```

### `avg`

Measure declared as type ‘avg’ returns an average of values within a column. Measure type ‘avg’ expects a column from the sql_snippet.

```yaml
# measure to calculate avg sales 
measure:
 - name: avg_sales
   sql_snippet: ${orders.amount)
   type: avg
```

### `min`

Measure declared as type ‘min’ returns a minimum of values given in the snippet. Measure type ‘min’ expects a column from the sql_snippet.

```yaml
entity:
 - name: orders
   sql:
    - query: select * from icebase.test.orders
   ----
   ----
# measure to identify the first purchase date
	 measure:
	  - name: first_purchase_date
      sql_snippet: ${orders.created_on} 
      type: min
```

### `max`

Measure declared as type ‘min’ returns a maximum of values in a column. Measure type ‘min’ expects a column from the sql_snippet.

### `running_total`

Typically measure having the type running_total calculates the cumulative sum of values. It does a summation of current values and previous values in a column. For instance, it’s helpful when you want to get revenue till a specific date or stock in inventory to date.

```yaml
# measure to calculate stock till a specific date
	 measure:
	  - name: stock_till_date
      sql_snippet: ${product.quantity} 
      type: running_total
```

### `sql_snippet`

Allows you to define complex sql expressions that column type measure is incapable of. It needs to be ensured that the measure type is correctly specified based on the value that sql_snippet is expected to return.

```yaml
measure:
 - name: month_since_signup
   sql_snippet: date_diff('month' , min(created_on) , current_date)
   type: number
```

### `rolling_window`

To calculate an aggregated measure within a defined window(day, week, month, etc.), you can use the rolling window property. 

The ‘Offset’ parameter value can be set as *start* or *end* depending on the date range you select. 

‘Leading’ and ‘Trailing’ parameters define the window size. The trailing parameter specifies the size of a window part before the offset point and the leading parameter specifies the size after the offset point. The window size can be defined using the combination of integer and time period → `(+/-Integer)(minute | hour | day | week | month | year)`. Use the keyword unbounded to define an infinite size for the window.

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
		- name: count_of_cust_rolling_window
      sql_snippet: ${entity_id}
      type: count
      rolling_window:
         trailing: 1 month
         offset: start
```

### `hidden`

If the value is set to true the measure will not be shown on the user interface.