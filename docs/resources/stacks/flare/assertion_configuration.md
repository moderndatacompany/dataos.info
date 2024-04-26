# Assertions: Configuration Fields
The following configuration fields are to be defined in the assertion YAML. Here are the details of the fields.

### **`assertions`**

**Description:** Assertions enable you to conduct validation checks on pre-existing datasets as well as on data during the ingestion process before it is written to the output. They are defined under the assertions section.

| Data Type         | Requirement | Default Value | Possible Value |
|-------------------|-------------|---------------|----------------|
| object            | optional    | none          | none           |


**Example Usage:**

```yaml
assertions:
  {}
```

---

### **`column`**

**Description:** the column on which the rule is to be defined.

| Data Type         | Requirement | Default Value | Possible Value      |
|-------------------|-------------|---------------|---------------------|
| string            | optional    | none          | valid column name   |


**Example Usage:**

```yaml
column: order_amount
```

---

### **`filter`**

**Description:** criterion, to apply assertions on the resulting data based on the filter criterion.

| Data Type         | Requirement | Default Value | Possible Value             |
|-------------------|-------------|---------------|----------------------------|
| string            | optional    | none          | valid filter criterion     |


**Example Usage:**

`filter: brand_name == 'Urbane’`

---

### **`sql`**

**Description:** the SQL statement for more complex custom logic that can be evaluated with computed columns

| Data Type         | Requirement | Default Value | Possible Value          |
|-------------------|-------------|---------------|-------------------------|
| string            | optional    | none          | valid SQL expression    |


**Example Usage:**

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

**Description:** validation format

| Data Type | Requirement | Default Value | Possible Value |
|-----------|-------------|---------------|----------------|
| object    | optional    | none          | none           |

**Example Usage:**

`validFormat: 
  regex: Awkward`

---

### **`regex`**

**Description:** regular expression declaration

| Data Type | Requirement | Default Value | Possible Value  |
|-----------|-------------|---------------|-----------------|
| string    | optional    | none          | valid regex     |


**Example Usage:**

`regex: Awkward`

---

### **`tests`**

**Description:** a boolean expression for each test. You can use quality metrics functions such as avg, max, min, etc. to define the rules with threshold values. These tests are expected to evaluate to true if the assertion should pass.

| Data Type         | Requirement | Default Value | Possible Value                                                                     |
|-------------------|-------------|---------------|------------------------------------------------------------------------------------|
| list of strings   | optional    | none          | The table below explains various quality metrics functions that can be used in defining boolean expressions for the tests. |


### **Quality Metrics Functions**

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

**Example Usage:**

```yaml
tests:
  - avg > 1000.00
  - max < 1000
  - max > 1000
```