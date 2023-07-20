# Assertions

DataOS allows you to define your own `assertions` with a combination of `tests` to check the rules. These `tests` consist of boolean expressions that incorporate metric functions for aggregated data, such as determining whether the average sales price surpasses a specified limit. When creating assertions, DataOS automatically generates metrics based on the functions utilized. For more sophisticated use cases, SQL and regular expressions can also be used to define assertions. 

## Structure of the Assertions Section

```yaml
assertions: 
  - column: order_amount 
  	filter: brand_name == 'Urbane' 
	validFormat: 
	  regex: Awkward 
	tests: 
	  - avg > 1000.00
	  - max < 1000
	  - max > 1000
  - sql: | 
  	  SELECT
	  	AVG(order_amount) AS avg_order_amount,
		MAX(order_amount) AS max_order_amount
	  FROM source
	  WHERE brand_name = 'Awkward Styles' 
	tests: 
	  - avg_order_amount > 1000
	  - max_order_amount < 1000
```

### Configuration Fields

### **`assertions`**
<b>Description:</b> assertions allow you to perform validation checks on top of pre-written datasets. They are defined under the assertions section.  <br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> none <br>
<b>Example Usage:</b>

```yaml
assertions:
  {} 
```

---
### **`column`**
<b>Description:</b> the column on which the rule is to be defined. <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> valid column name <br>
<b>Example Usage:</b>

```yaml
column: order_amount
```

---

### **`filter`**
<b>Description:</b> criterion, to apply assertions on the resulting data based on the filter criterion. <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> valid filter criterion <br>
<b>Example Usage:</b>

```yaml
filter: brand_name == 'Urbane’
```

---

### **`sql`**
<b>Description:</b> the SQL statement for more complex custom logic that can be evaluated with computed columns <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> valid sql expression <br>
<b>Example Usage:</b>

```yaml
sql: |
SELECT
AVG(order_amount) AS avg_order_amount,
MAX(order_amount) AS max_order_amount
FROM source
where brand_name = 'Awkward Styles’
```

---

### **`validFormat`**
<b>Description:</b> validation format <br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> none <br>
<b>Example Usage:</b>

```yaml
validFormat: 
  regex: Awkward 
```

---

### **`regex`**
<b>Description:</b> regular expression declaration <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> valid regex <br>
<b>Example Usage:</b>

```yaml
regex: Awkward
```

---

### **`tests`**
<b>Description:</b> a boolean expression for each test. You can use quality metrics functions such as avg, max, min, etc. to define the rules with threshold values. These tests are expected to evaluate to true if the assertion should pass. <br>
<b>Data Type:</b> list of strings <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> possible Quality Metrics functions have been elucidated in the table below. 

| Function | Description | Example |
| --- | --- | --- |
| `avg` | The avg function returns the average of a column. | `avg > 1000.00` |
| `avg_length` | The avg_length function returns the average length of the column value. | `avg_length < 12` |
| `distinct_count` | The distinct_count function returns the count of the distinct values of a column. | `distinct_count > 10` |
| `duplicate_count` | The duplicate_count function returns the count of duplicate values in the column. | `duplicate_count < 11` |
| `min` | The min function returns the minimum value of a column. | `min > 100` |
| `max` | The max function returns the maximum value of a column. | `max < 1000` |
| `max_length` | The max_length function returns the maximum length of the column value. | `max_length < 20` |
| `min_length` | The min_length function returns the minimum length of the column value. | `min_length > 30` |
| `missing_count` | The missing_count function returns the count of missing values in the column. | `missing_count < 5` |
| `missing_percentage` | The missing_percentage function returns the rate of missing values in the column. | `missing_percentage < 0.1` |
| `sum` | The sum function returns the total sum of the column value. | `sum > 500` |

<b>Example Usage:</b>

```yaml
tests:
  - avg > 1000.00
  - max < 1000
  - max > 1000
```
