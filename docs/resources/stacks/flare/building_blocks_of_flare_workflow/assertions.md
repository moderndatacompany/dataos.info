# Assertions

DataOS allows you to define your own `assertions` with a combination of `tests` to check the rules. These `tests` consist of boolean expressions that incorporate metric functions for aggregated data, such as determining whether the average sales price surpasses a specified limit. When creating assertions, DataOS automatically generates metrics based on the functions utilized. For more sophisticated use cases, SQL and regular expressions can also be used to define assertions. 

Additional information on Data Quality Jobs and the application of assertions can be found in this case scenario.

## **Structure of the Assertions Section**

```yaml
assertions: #(Mandatory)
	- column: order_amount #(Optional)
		filter: brand_name == 'Urbane' #(Optional)
		validFormat: #(Optional)
			regex: Awkward #(Optional)
		tests: #(Optional)
			- avg > 1000.00
			- max < 1000
			- max > 1000
	- sql: | 
			SELECT
				AVG(order_amount) AS avg_order_amount,
				MAX(order_amount) AS max_order_amount
			FROM source
				where brand_name = 'Awkward Styles' 
		tests: #(Optional)
	    - avg_order_amount > 1000
	    - max_order_amount < 1000
		
```

### Assertion Properties

| Property | Description | Example | Field (Mandatory/ Optional) |
| --- | --- | --- | --- |
| column | The column on which the rule is to be defined. | column: order_amount | Optional |
| filter | Criterion, to apply assertions on the resulting data based on the filter criterion. | filter: brand_name == 'Urbane’ | Optional |
| sql | The SQL statement for more complex custom logic that can be evaluated with computed columns | sql: |
SELECT
AVG(order_amount) AS avg_order_amount,
MAX(order_amount) AS max_order_amount
FROM source
where brand_name = 'Awkward Styles’ | Optional |
| validFormat | Validation Format | validFormat: 
    {} | Optional |
| regex | Regular Expressions | regex: Awkward  | Optional |
| tests | A boolean expression for each test. You can use quality metrics functions such as avg, max, min, etc. to define the rules with threshold values. These tests are expected to evaluate to true if the assertion should pass. | tests:
   - avg > 1000.00
   - max < 1000
   - max > 1000 | Optional |

### Quality metrics functions

| Function | Description | Example |
| --- | --- | --- |
| avg | The avg function returns the average of a column. | avg > 1000.00 |
| avg_length | The avg_length function returns the average length of the column value. | avg_length < 12 |
| distinct_count | The distinct_count function returns the count of the distinct values of a column. | distinct_count > 10 |
| duplicate_count | The duplicate_count function returns the count of duplicate values in the column. | duplicate_count < 11 |
| min | The min function returns the minimum value of a column. | min > 100 |
| max | The max function returns the maximum value of a column. | max < 1000 |
| max_length | The max_length function returns the maximum length of the column value. | max_length < 20 |
| min_length | The min_length function returns the minimum length of the column value. | min_length > 30 |
| missing_count | The missing_count function returns the count of missing values in the column. | missing_count < 5 |
| missing_percentage | The missing_percentage function returns the rate of missing values in the column. | missing_percentage < 0.1 |
| sum | The sum function returns the total sum of the column value. | sum > 500 |