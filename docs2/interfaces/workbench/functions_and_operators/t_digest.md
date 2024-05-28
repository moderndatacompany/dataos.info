# T-Digest functions

## Data structures

A T-digest is a data sketch which stores approximate percentile information. The Minerva type for this data structure is called tdigest.

## Functions

###  **`merge()`**

| Function                               | Description                                                                                       | Return Type |
| -------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------- |
| `merge(tdigest)`                       | Aggregates all inputs into a single tdigest.                                                      | `tdigest`   |

### **`value_at_quantile()`**

| Function                                    | Description                                                                                            | Return Type |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------- |
| `value_at_quantile(tdigest, quantile)`     | Returns the approximate percentile value from the T-digest, given the number quantile between 0 and 1. | `double`    |

### **`values_at_quantiles()`**

| Function                                      | Description                                                                                          | Return Type |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| `values_at_quantiles(tdigest, quantiles)`     | Returns the approximate percentile values as an array, given the input T-digest and an array of values between 0 and 1, which represent the quantiles to return. | `array`     |

### **`tdigest_agg()`**

| Function          | Description                                                                                              | Return Type |
| ----------------- | -------------------------------------------------------------------------------------------------------- | ----------- |
| `tdigest_agg(x)`  | Composes all input values of x into a tdigest. x can be of any numeric type.                            | `tdigest`   |
| `tdigest_agg(x, w)` | Composes all input values of x into a tdigest using the per-item weight w. w must be greater or equal than 1. x and w can be of any numeric type. | `tdigest`   |

