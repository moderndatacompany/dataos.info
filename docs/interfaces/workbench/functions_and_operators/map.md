# Map functions and operators

## Subscript operator

| Operator                | Description                                                         | Example                                              |
| ----------------------- | ------------------------------------------------------------------- | ---------------------------------------------------- |
| `[]`                    | Retrieves the value corresponding to a given key from a map.        | Depends on the value type in the map                 |

## Map functions

### **`cardinality()`**
| Function             | Description                               | Return Type |
| -------------------- | ----------------------------------------- | ----------- |
| `cardinality(x)`     | Returns the cardinality (size) of the map `x`. | `bigint`    |

### **`element_at()`**
| Function                    | Description                                                      | Return Type |
| --------------------------- | ---------------------------------------------------------------- | ----------- |
| `element_at(map(K, V), key)` | Returns value for given `key`, or NULL if the key is not contained in the map. | `V`         |


### **`map()`**

| Function                  | Description                                                    | Return Type        |
| ------------------------- | -------------------------------------------------------------- | ------------------ |
| `map()`                   | Returns an empty map.                                          | `map<unknown, unknown>` |
| `map(array(K), array(V))` | Returns a map created using the given key/value arrays.       | `map(K, V)`       |

Example:
```sql
SELECT map();
-- {}
SELECT map(ARRAY[1,3], ARRAY[2,4]);
-- {1 -> 2, 3 -> 4}
```

### **`map_from_entries()`**

| Function                                | Description                                                      | Return Type  |
| --------------------------------------- | ---------------------------------------------------------------- | ------------ |
| `map_from_entries(array(row(K, V)))`    | Returns a map created from the given array of entries.           | `map(K, V)`  |


### **`multimap_from_entries()`**

| Function                                       | Description                                                             | Return Type         |
| ---------------------------------------------- | ----------------------------------------------------------------------- | ------------------- |
| `multimap_from_entries(array(row(K, V)))`      | Returns a multimap created from the given array of entries.             | `map(K, array(V))` |

### **`map_entries()`**

| Function                                | Description                                                      | Return Type        |
| --------------------------------------- | ---------------------------------------------------------------- | ------------------ |
| `map_entries(map(K, V))`                | Returns an array of all entries in the given map.                | `array(row(K, V))` |

Example:
```sql
SELECT map_from_entries(ARRAY[(1, 'x'), (2, 'y')]);
-- {1 -> 'x', 2 -> 'y'}
```

### **`map_concat()`**

| Function                                                          | Description                                                                  | Return Type |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------- |
| `map_concat(map1(K, V), map2(K, V), ..., mapN(K, V))`             | Returns the union of all the given maps.                                    | `map(K, V)` |

### **`map_filter()`**

| Function                                                          | Description                                                                  | Return Type |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------- |
| `map_filter(map(K, V), function(K, V, boolean))`                  | Constructs a map from those entries of map for which function returns true. | `map(K, V)` |

Example:

```sql
SELECT map_filter(MAP(ARRAY['k1', 'k2', 'k3'], ARRAY[20, 3, 15]),
                  (k, v) -> v > 10);
-- {k1 -> 20, k3 -> 15}
```

### **`map_keys()`**

| Function                                       | Description                                                             | Return Type    |
| ---------------------------------------------- | ----------------------------------------------------------------------- | -------------- |
| `map_keys(x(K, V))`                            | Returns all the keys in the map x.                                      | `array(K)`     |

### **`map_values()`**

| Function                                       | Description                                                             | Return Type    |
| ---------------------------------------------- | ----------------------------------------------------------------------- | -------------- |
| `map_values(x(K, V))`                          | Returns all the values in the map x.                                    | `array(V)`     |

### **`map_zip_with()`**

| Function                                                         | Description                                                                 | Return Type    |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------- |
| `map_zip_with(map(K, V1), map(K, V2), function(K, V1, V2, V3))` | Merges the two given maps into a single map by applying function to the pair of values with the same key. | `map(K, V3)`  |

Example:

```sql
SELECT map_zip_with(MAP(ARRAY['a', 'b', 'c'], ARRAY[1, 8, 27]),
                    MAP(ARRAY['a', 'b', 'c'], ARRAY[1, 2, 3]),
                    (k, v1, v2) -> k || CAST(v1 / v2 AS VARCHAR));
-- {a -> a1, b -> b4, c -> c9}
```

### **`transform_keys()`**

| Function                                              | Description                                                             | Return Type      |
| ----------------------------------------------------- | ----------------------------------------------------------------------- | ---------------- |
| `transform_keys(map(K1, V), function(K1, V, K2))`    | Returns a map that applies function to each entry of map and transforms the keys. | `map(K2, V)`     |

### **`transform_values()`**

| Function                                              | Description                                                             | Return Type      |
| ----------------------------------------------------- | ----------------------------------------------------------------------- | ---------------- |
| `transform_values(map(K, V1), function(K, V1, V2))`  | Returns a map that applies function to each entry of map and transforms the values. | `map(K, V2)`     |

Example:
```sql
SELECT transform_values(MAP(ARRAY [1, 2, 3], ARRAY [10, 20, 30]),
                        (k, v) -> v + k);
-- {1 -> 11, 2 -> 22, 3 -> 33}
```