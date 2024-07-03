# Quantile digest functions

## Data structures

A quantile digest is a data sketch which stores approximate percentile information. 

| Trino Type | Parameter Options            | Description                                                                                                      |
|------------|------------------------------|------------------------------------------------------------------------------------------------------------------|
| qdigest    | `bigint`, `double`, `real`  | Represents the set of numbers that may be ingested by the qdigest. They may be merged without losing precision. For storage and retrieval, they may be cast to/from `VARBINARY` seamlessly. |

## Functions

### **`merge()`**

| Function         | Description                                                                           | Return Value |
| ---------------- | ------------------------------------------------------------------------------------- | ------------ |
| `merge(qdigest)` | Merges all input `qdigests` into a single `qdigest`.                                  | qdigest      |

### **`value_at_quantile()`**

| Function                                    | Description                                                                                         | Return Value |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------ |
| `value_at_quantile(qdigest(T), quantile)`  | Returns the approximate percentile value from the quantile digest given the number `quantile`.    | Numeric           |

### **`quantile_at_value()`**

| Function                               | Description                                                                                       | Return Value |
| -------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------ |
| `quantile_at_value(qdigest(T), T)`    | Returns the approximate quantile number between 0 and 1 from the quantile digest given an input value. | Numeric     |

### **`values_at_quantiles(qdigest(T), quantiles)`**

| Function                                          | Description                                                                                                                                     | Return Value |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `values_at_quantiles(qdigest(T), quantiles)`      | Returns the approximate percentile values as an array given the input quantile digest and array of values between 0 and 1 representing quantiles. | Array(T)     |

### **`qdigest_agg()`**

| Function                          | Description                                                                                                     | Return Value      |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------- |
| `qdigest_agg(x) -> qdigest([same as x])` | Returns the qdigest composed of all input values of `x`.                                                       | qdigest([same as x]) |
| `qdigest_agg(x, w) -> qdigest([same as x])` | Returns the qdigest composed of all input values of `x` using the per-item weight `w`.                         | qdigest([same as x]) |
| `qdigest_agg(x, w, accuracy) -> qdigest([same as x])` | Returns the qdigest composed of all input values of `x` using the per-item weight `w` and maximum error of `accuracy`. | qdigest([same as x]) |


