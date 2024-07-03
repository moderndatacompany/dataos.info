# Aggregate functions

Aggregate functions process a set of values to derive a singular outcome. 

However, `count()`, `count_if()`, `max_by()`, `min_by()`, and `approx_distinct()` differ in that they take null values into account. For all other aggregate functions, null values are disregarded, and when there are no input rows or all values are null, they return null. For instance, `sum()`yields null instead of zero, and `avg()` excludes null values from the count. To transform null into zero, the coalesce function can be applied.


## General aggregate functions

### **`count()`**

| Function        | Description                                              | Return Type |
| --------------- | -------------------------------------------------------- | ----------- |
| `count(*)`      | Returns the number of input rows.                         | `bigint`    |
| `count(x)`      | Returns the number of non-null input values.              | `bigint`    |
| `count_if(x)`   | Returns the number of TRUE input values. This function is equivalent to `count(CASE WHEN x THEN 1 END)`. | `bigint`    |

### **`avg()`**

| Function                            | Description                                                | Return Type  |
| ----------------------------------- | ---------------------------------------------------------- | ------------ |
| `avg(x)`                            | Computes the average (arithmetic mean) of all input values. | `same as input(numeric)`    |
| `avg(time interval type)`           | Calculates the average interval length of all input values. | `same as input(interval)`   |

*Example:*
```sql
SELECT avg(time_column) as average_interval
FROM your_table;
```

### **`bool()`**

| Function                       | Description                                                      | Return Type  |
| ------------------------------ | ---------------------------------------------------------------- | ------------ |
| `bool_and(boolean)`            | Yields TRUE only if every input value is TRUE; otherwise, FALSE. | `boolean`    |
| `bool_or(boolean)`             | Yields TRUE if at least one input value is TRUE; otherwise, FALSE. | `boolean`    |

### **`every()`**

| Function           | Description                      | Return Type  |
| ------------------ | -------------------------------- | ------------ |
| `every(boolean)`   | Acts as an alias for `bool_and()`. | `boolean`    |


### **`array_agg()`**

| Function                       | Description                                                      | Return Type  |
| ------------------------------ | ---------------------------------------------------------------- | ------------ |
| `array_agg(x)`                 | Generates an array containing the input `x` elements.              | `array<[same as input]>` |

### **`checksum()`**

| Function          | Description                                               | Return Type  |
| ------------------ | --------------------------------------------------------- | ------------ |
| `checksum(x)`      | Computes an order-insensitive checksum for the provided values. | `varbinary`     |


### **`geometric_mean()`**

| Function              | Description                                   | Return Type  |
| --------------------- | --------------------------------------------- | ------------ |
| `geometric_mean(x)`   | Computes the geometric mean of all input values. | `double`    |

### **`listagg()`**

| Function               | Description                                                      | Return Type  |
| ---------------------- | ---------------------------------------------------------------- | ------------ |
| `listagg(x, separator)` | Concatenates input values, separated by the specified separator string. | `varchar`     |


### **`max()`**

| Function             | Description                                                                                  | Return Type  |
| -------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| `max(x)`             | Computes the maximum value among all input values.                                           | `<same as input>` |
| `max(x, n)`          | Retrieves the n largest values from all input values of `x`.                                    | `array<[same as input]>` |

### **`max_by()`**

| Function           | Description                                              | Return Type          |
|--------------------|----------------------------------------------------------|----------------------|
| `max_by(x, y)`     | Obtains the value of `x` associated with the maximum value of `y`. | `<same as x>`        |
| `max_by(x, y, n)`  | Retrieves n values of `x` associated with the n largest values of `y`. | `array<[same as x]>` |


### **`min()`**

| Function             | Description                                                                                  | Return Type  |
| -------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| `min(x)`             | Computes the minimum value among all input values.                                           | `<same as input>` |
| `min(x, n)`          | Retrieves the n smallest values from all input values of x.                                   | `array<[same as input]>` |


### **`min_by`**

| Function           | Description                                              | Return Type          |
|--------------------|----------------------------------------------------------|----------------------|
| `min_by(x, y)`     | Obtains the value of `x` associated with the minimum value of `y`. | `<same as x>`        |
| `min_by(x, y, n)`  | Retrieves n values of `x` associated with the n smallest values of `y` in ascending order of `y`. | `array<[same as x]>` |


### **`sum()`**

| Function       | Description                        | Return Type  |
| -------------- | ---------------------------------- | ------------ |
| `sum(x)`       | Computes the sum of all input values.| `<same as input>` |


## Bitwise aggregate functions

| Function             | Description                                                           | Return Type  |
| -------------------- | --------------------------------------------------------------------- | ------------ |
| `bitwise_and_agg(x)` | Computes the bitwise AND of all input values in 2’s complement representation. | `<same as input>` |
| `bitwise_or_agg(x)`  | Calculates the bitwise OR of all input values in 2’s complement representation. | `<same as input>` |



## Map aggregate functions

### **`histogram()`**

| Function         | Description                                                                      | Return Type  |
| ---------------- | -------------------------------------------------------------------------------- | ------------ |
| `histogram(x)`   | Generates a map containing the count of occurrences for each input value.         | `map<K,bigint>` |

### **`map_agg()`**

| Function             | Description                                       | Return Type  |
| -------------------- | ------------------------------------------------- | ------------ |
| `map_agg(key, value)` | Generates a map created from the input key/value pairs. | `map<key, value>` |


### **`map_union()`**

| Function                 | Description                                                  | Return Type  |
| ------------------------ | ------------------------------------------------------------ | ------------ |
| `map_union(x(K, V))`     | Obtains the union of all input maps. If a key is present in multiple input maps, the value in the resulting map is selected arbitrarily from one of the input maps. | `map<K, V>` |

### **`multimap_agg()`**

| Function                       | Description                                                                                      | Return Type  |
| ------------------------------ | ------------------------------------------------------------------------------------------------ | ------------ |
| `multimap_agg(key, value)`     | Generates a multimap created from the input key/value pairs. Each key can be associated with multiple values. | `multimap<key, value>` |


## Approximate aggregate functions 


### **`approximate_distinct() `**

| Function                   | Description                                                                                                          | Return Type |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| `approx_distinct(x)`       | Returns the approximate count of distinct non-null values in the input set `x`. Zero is returned if all input values are null. The standard error is approximately 2.3%, providing an approximation of count(DISTINCT x). | `bigint`     |
| `approx_distinct(x, e)`    | Returns the approximate count of distinct non-null values in the input set `x`. Zero is returned if all input values are null. The standard error is no more than `e`, with `e` in the range of [0.0040625, 0.26000]. | `bigint`     |


### **`approx_most_frequent()`**

| Function               | Description                                                                                                      | Return Type  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------ |
| `approx_most_frequent(buckets, value, capacity)`   | Approximates the top frequent values up to a specified number, balancing memory efficiency and accuracy.        | `map<[same as value], bigint>` |



### **`approx_percentile()`**

| Function&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;              | Description                                                                                                         | Return Type  |
| ----------------------------------------------|---------------------------------------------------------------------------------------------------------------------| ------------ |
| `approx_percentile(x, percentage)`             | Computes the approximate percentile for all input values of `x` at the given `percentage`. `percentage` must be between 0 and 1, constant for all rows.               | `[same as x]`     |
| `approx_percentile(x, percentages)`            | Calculates the approximate percentile for all input values of `x` at each specified percentage in the array. Each element in `percentages` must be between 0 and 1, constant for all rows.               | `array<[same as x]>`  |
| `approx_percentile(x, w, percentage)`          | Computes the approximate weighted percentile for all input values of `x` using per-item weight `w` at the given `percentage`. Weights >= 1, `percentage` between 0 and 1, constant for all rows. | ` [same as x]`     |
| `approx_percentile(x, w, percentages)`         | Calculates the approximate weighted percentile for all input values of `x` using per-item weight `w` at each specified percentage in the array. Weights >= 1, each element in `percentages` between 0 and 1, constant for all rows. | `array<n [same as x]>` 

### **`approx_set()`**

| Function            | Description                                   | Return Type  |
|---------------------|-----------------------------------------------| ------------ |
| `approx_set(x)`     | Generates a HyperLogLog structure for the given input values `x`. | `hll`        |

### **`merge()`**

| Function                            | Description                                     | Return Type          |
|-------------------------------------|-------------------------------------------------|----------------------|
| `merge(x)`                         | Merges HyperLogLog structures.                  | `hll`                |
| `merge(qdigest(T))`                | Merges Quantile digest structures.              | `qdigest(T)`         |
| `merge(tdigest)`                    | Merges T-Digest structures.                      | `tdigest`            |   

### **`numeric_histogram()`**

| Function                                        | Description                                                                                                              | Return Type           |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------|
| `numeric_histogram(buckets, value)`              | Computes an approximate histogram with up to `buckets` number of buckets for all values.                               | `map<double, double>`  |
| `numeric_histogram(buckets, value, weight)`      | Computes an approximate histogram with up to `buckets` number of buckets for all values with a per-item weight of `weight`. | `map<double, double>`  |



### **`qdigest_agg()`**

A quantile digest is a data sketch that stores approximate percentile information. It takes a parameter which must be one of `bigint`, `double`, or `real` which represent the set of numbers that may be ingested by the `qdigest`. They may be merged without losing precision, and for storage and retrieval, they may be cast to/from `VARBINARY`.

| Function                                 | Description                                                                     | Return Type               |
| -----------------------------------------|---------------------------------------------------------------------------------|---------------------------|
| `qdigest_agg(x)`                         | Computes a quantile digest (qdigest) for values in `x`.                          | `qdigest([same as x])`    |
| `qdigest_agg(x, w)` | Computes a quantile digest (qdigest) for values in `x` with per-item weights `w`. | `qdigest([same as x])`    |
| `qdigest_agg(x, w, accuracy)`            | Computes a quantile digest (qdigest) for values in `x` with per-item weights `w` and specified accuracy. | `qdigest([same as x])`    |


### **`tdigest_agg()`**

A T-digest is a data sketch specifically crafted to store approximate percentile information.

| Function                             | Description                                   | Return Type     |
| --------------------------------------|-----------------------------------------------|-----------------|
| `tdigest_agg(x)`           | Computes a T-Digest for values in `x`.        | `tdigest`      |
| `tdigest_agg(x, w)`        | Computes a T-Digest for values in `x` with per-item weights `w`. | `tdigest`      |


## Statistical aggregate functions


**`corr()`**

| Function        | Description                                    | Return Type            |
|-----------------|------------------------------------------------|------------------------|
| `corr(y, x)`    | Returns the correlation coefficient of input values `y` and `x`. | `double`    |

### **`covar_pop()`**

| Function              | Description                                           | Return Type            |
|-----------------------|-------------------------------------------------------|------------------------|
| `covar_pop(y, x)`     | Returns the population covariance of input values `y` and `x`. | `double`    |


### **`covar_samp()`**

| Function               | Description                                           | Return Type            |
|------------------------|-------------------------------------------------------|------------------------|
| `covar_samp(y, x)`     | Returns the sample covariance of input values `y` and `x`. | `double`    |


### **`kurtosis()`**

| Function          | Description                                                                                                           | Return Type            |
|-------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------|
| `kurtosis(x)`     | Returns the excess kurtosis of all input values. It provides an unbiased estimate using a specific mathematical expression. | `double`    |

### **`regr_intercept()`**

| Function                | Description                                          | Return Type            |
|-------------------------|------------------------------------------------------|------------------------|
| `regr_intercept(y, x)`  | Returns the linear regression intercept of input values. `y` is the dependent value, and `x` is the independent value. | `double`    |


### **`regr_slope()`**

| Function            | Description                                          | Return Type            |
|---------------------|------------------------------------------------------|------------------------|
| `regr_slope(y, x)`  | Returns the linear regression slope of input values. `y` is the dependent value, and `x` is the independent value. | `double`    |


### **`skewness()`**

| Function       | Description                                          | Return Type            |
|----------------|------------------------------------------------------|------------------------|
| `skewness(x)`  | Returns Fisher’s moment coefficient of skewness for all input values. | `double`    |


### **`stddev()`**

| Function      | Description                           | Return Type            |
|---------------|---------------------------------------|------------------------|
| `stddev(x)`   | Alias for `stddev_samp()`.             | `double`    |


### **`stddev_pop()`**

| Function          | Description                                           | Return Type            |
|-------------------|-------------------------------------------------------|------------------------|
| `stddev_pop(x)`   | Returns the population standard deviation of all input values. | `double`    |

### **`stddev_samp()`**

| Function          | Description                                           | Return Type            |
|-------------------|-------------------------------------------------------|------------------------|
| `stddev_samp(x)`  | Returns the sample standard deviation of all input values. | `double`    |

### **`variance()`**

| Function       | Description                          | Return Type            |
|----------------|--------------------------------------|------------------------|
| `variance(x)`  | Alias for `var_samp()`.               | `double`    |


### **`var_pop()`**

| Function         | Description                                    | Return Type            |
|------------------|------------------------------------------------|------------------------|
| `var_pop(x)`     | Returns the population variance of all input values. | `double`    |

### **`var_samp()`**

| Function         | Description                                    | Return Type            |
|------------------|------------------------------------------------|------------------------|
| `var_samp(x)`    | Returns the sample variance of all input values. | `double`    |


## Lambda aggregate functions

| Function                                                                                                                | Description                                                                                                                | Return Type            |
|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------|
| `reduce_agg(inputValue T, initialState S, inputFunction(S, T, S), combineFunction(S, S, S)) `                      | Reduces all input values into a single value. `inputFunction` is invoked for each non-null input value, taking the input value and the current state (initially `initialState`), and returning the new state. `combineFunction` is invoked to combine two states into a new state. The final state is returned. The state type (`S`) must be boolean, integer, floating-point, or date/time/interval. | `<Same as initialState>`|


#### Example:
```sql
-- Creating a sample table
CREATE TABLE sales (
    product_id INT,
    quantity_sold INT
);

-- Inserting sample data
INSERT INTO sales VALUES
    (1, 10),
    (1, 15),
    (2, 5),
    (2, 8),
    (2, 7);

-- Using reduce_agg to calculate the total quantity sold for each product
SELECT product_id, reduce_agg(quantity_sold, 0, (a, b) -> a + b, (a, b) -> a + b) AS total_quantity_sold
FROM sales
GROUP BY product_id;
```

The output will show the total quantity sold for each product:


```sql
 product_id | total_quantity_sold |
|------------|----------------------|
| 1          | 25                   |
| 2          | 20                   |
```

## Ordering  during aggregation
Some aggregate functions such as `array_agg()` produce different results depending on the order of input values. This ordering can be specified by writing an ORDER BY clause within the aggregate function:


| Example                                                | Description                                                                |
|--------------------------------------------------------|----------------------------------------------------------------------------|
| `array_agg(x ORDER BY y DESC)`                          | Aggregates `x` values ordered by `y` in descending order.                   |
| `array_agg(x ORDER BY x, y, z)`                         | Aggregates `x` values ordered by `x`, `y`, and `z`.                          |

## Filtering during aggregation

The `FILTER` keyword allows you to apply a condition using a `WHERE` clause to remove specific rows from aggregation processing. This condition is evaluated for each row before it is used in the aggregation and can be used with any aggregate function.

| Example                                                         | Description                                                                                           |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `aggregate_function(...) FILTER (WHERE <condition>)`            | Applies a condition using `WHERE` clause to remove specific rows from aggregation processing.        |
| `SELECT array_agg(name) FILTER (WHERE name IS NOT NULL)`        | Removes null values from consideration in `array_agg`.                                                 |
| `SELECT count(*) FILTER (WHERE petal_length_cm > 4) AS count`   | Adds a condition on the count for Iris flowers while retaining all information.                      |


