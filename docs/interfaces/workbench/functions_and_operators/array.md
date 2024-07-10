# Array Functions and Operators

### **`Subscript Operator []`**

| Operator | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| Subscript Operator `[]` | Used to access an element of an array, indexed starting from one. |

Example:

```sql
SELECT my_array[1] AS first_element;
```

### **`Concatenation Operator ||`**

| Operator         | Description                                                |
|--------------------------|------------------------------------------------------------|
| Concatenation Operator `[]` | Used to concatenate an array with another array or an element of the same type. |


 Examples:

```sql
-- Result: [1, 2]
SELECT ARRAY[1] || ARRAY[2] AS concatenated_array;

-- Result: [1, 2]
SELECT ARRAY[1] || 2 AS concatenated_array_with_element;

-- Result: [2, 1]
SELECT 2 || ARRAY[1] AS concatenated_element_with_array;
```

### **`all_match()`**

| Function                        | Description                                                                                                                                                  | Return Type |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| `all_match(array(T), function(T, boolean))` | Returns whether all elements of an array match the given predicate. Returns true if all the elements match the predicate (a special case is when the array is empty); false if one or more elements don’t match; `NULL` if the predicate function returns NULL for one or more elements and true for all other elements. | `boolean`     |

Example:

```sql
all_match(array(T), function(T, boolean)) → boolean
```

### **`any_match()`**

| Function | Description | Return Type |
| --- | --- | --- |
| \`any_match(array(T), function(T, boolean))\` | Returns whether any elements of an array match the given predicate. Returns true if one or more elements match the predicate; false if none of the elements matches (a special case is when the array is empty); \`NULL\` if the predicate function returns NULL for one or more elements and false for all other elements. | \`boolean\` |


### **`array distinct()`**

| Function              | Description                                | Return Type |
|-----------------------|--------------------------------------------|-------------|
| `array_distinct(x)`   | Remove duplicate values from the array `x`. | `array`     |


### **`array_intersect()`**


| Function       | Description                                               | Return Type |
|----------------------------------|-----------------------------------------------------------|-------------|
| `array_intersect(x, y)` | Returns an array of the elements in the intersection of `x` and `y`, without duplicates. | `array`       |

### **`array_union()`**


| Function        | Description                                                      | Return Type |
|-------------------------------|------------------------------------------------------------------|-------------|
| `array_except(x, y)`| Returns an array of elements in x but not in y, without duplicates. | `array`       |

### **`array_histogram()`**

| Function                | Description                                                                                                    | Return Type         |
|-------------------------|----------------------------------------------------------------------------------------------------------------|---------------------|
| `array_histogram(x)`| Returns a map where the keys are the unique elements in the input array x, and the values are the number of times that each element appears in x. Null values are ignored. | `map<K, bigint> `    |

Example:

```sql
SELECT array_histogram(ARRAY[42, 7, 42, NULL]);
-- {42=2, 7=1}
```
Returns an empty map if the input array has no non-null elements.


```sql
SELECT array_histogram(ARRAY[NULL, NULL]);
-- {}
```

### **`array_join()`**

| Function                                       | Description                                                                                                    | Return Type |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------|
| `array_join(x, delimiter)`                      | Concatenates the elements of the given array using the delimiter. Null elements are omitted in the result.     | `varchar`   |
| `array_join(x, delimiter, null_replacement)`   | Concatenates the elements of the given array using the delimiter and an optional string to replace nulls.     | `varchar`   |


### **`array_max()`**

| Function          | Description                                  | Return Type |
|-------------------|----------------------------------------------|-------------|
| `array_max(x)`    | Returns the maximum value of the input array. | `same as x`         |


### **`array_min()`**


| Function          | Description                                  | Return Type |
|-------------------|----------------------------------------------|-------------|
| `array_min(x)`    | Returns the minimum value of the input array. | `same as x`         |


### **`array_position`**

| Function                   | Description                                                          | Return Type |
|----------------------------|----------------------------------------------------------------------|-------------|
| `array_position(x, element)`| Returns the position of the first occurrence of the `element` in array `s` (or 0 if not found). | `bigint` |


### **`array_remove()`**


| Function                   | Description                                                          | Return Type |
|----------------------------|----------------------------------------------------------------------|-------------|
| `array_remove(x, element)` | Remove all elements that equal `element` from array `x`.                  | `array`     |


### **`array_sort()`**

| Function                                       | Description                                                                                                                          | Return Type |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------|
| `array_sort(x)`                                | Sorts and returns the array `x`. The elements of `x` must be orderable. Null elements will be placed at the end of the returned array.   | `array`     |
| `array_sort(array(T), function(T, T, int))`     | Sorts and returns the `array` based on the given comparator `function`. The comparator will take two nullable arguments representing two nullable elements of the `array`. It returns -1, 0, or 1 as the first nullable element is less than, equal to, or greater than the second nullable element. If the comparator function returns other values (including `NULL`), the query will fail and raise an error. | `array(T)`  |

Examples:
```sql
SELECT array_sort(ARRAY[3, 2, 5, 1, 2],
                  (x, y) -> IF(x < y, 1, IF(x = y, 0, -1)));
-- Result: [5, 3, 2, 2, 1]

SELECT array_sort(ARRAY['bc', 'ab', 'dc'],
```


### **`array_overlap()`**

| Function                    | Description                                                                                                       | Return Type |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------|-------------|
| `arrays_overlap(x, y)`      | Tests if arrays `x` and `y` have any non-null elements in common. Returns null if there are no non-null elements in common but either array contains null. | `boolean`   |


### **`cardinality`()**

| Function         | Description                                              | Return Type |
|------------------|----------------------------------------------------------|-------------|
| `cardinality(x)` | Returns the cardinality (size) of the array x.           | `bigint`    |


### **`concat()`**

| Function                            | Description                                                      | Return Type |
|-------------------------------------|------------------------------------------------------------------|-------------|
| `concat(array1, array2, ..., arrayN)` | Concatenates the arrays `array1, array2, ..., arrayN`. This function provides the same functionality as the SQL-standard concatenation operator ( &#124; &#124; )| `array`     |


### **`combinations()`**

| Function                                   | Description                                                      | Return Type        |
|--------------------------------------------|------------------------------------------------------------------|--------------------|
| `combinations(array(T), n) -> array(array(T))` | Returns n-element sub-groups of the input array. If the input array has no duplicates, the `combinations` function returns n-element subsets.  | `array(array(T))`  |

The order of sub-groups and elements within a sub-group is deterministic but unspecified. The value of n must not be greater than 5, and the total size of sub-groups generated must be smaller than 100,000.


### **`contains()`**

| Function                    | Description                                        | Return Type |
|-----------------------------|----------------------------------------------------|-------------|
| `contains(x, element)`      | Returns true if the array x contains the element. | `boolean`   |


### **`contains_sequence()`**

| Function                           | Description                                                               | Return Type |
|------------------------------------|---------------------------------------------------------------------------|-------------|
| `contains_sequence(x, seq)`        | Returns true if array `x` contains all of array seq as a subsequence (all values in the same consecutive order). | `boolean`   |


### **`element_at()`**

| Function                        | Description                                                                                                                       | Return Type |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------|
| `element_at(array(E), index)`   | Returns the element of the array at the given index. If index > 0, this function provides the same functionality as the SQL-standard subscript operator ([]), except that the function returns NULL when accessing an index larger than the array length, whereas the subscript operator would fail in such a case. If index < 0, `element_at` accesses elements from the last to the first. | `E`         |


### **`filter()`**

| Function                                    | Description                                                                         | Return Type |
|---------------------------------------------|-------------------------------------------------------------------------------------|-------------|
| `filter(array(T), function(T, boolean))`    | Constructs an array from those elements of the array for which the function returns true. | `array(T)`  |

```sql
SELECT filter(ARRAY[], x -> true);
-- []

SELECT filter(ARRAY[5, -6, NULL, 7], x -> x > 0);
-- [5, 7]

SELECT filter(ARRAY[5, NULL, 7, NULL], x -> x IS NOT NULL);
-- [5, 7]

```

### **`flatten()`**

| Function               | Description                                                    | Return Type |
|------------------------|----------------------------------------------------------------|-------------|
| `flatten(x)`           | Flattens an array(array(T)) to an array(T) by concatenating the contained arrays. | `array`     |


### **`ngrams()`**

| Function                    | Description                                                                        | Return Type        |
|-----------------------------|------------------------------------------------------------------------------------|--------------------|
| `ngrams(array(T), n)`       | Returns n-grams (sub-sequences of adjacent n elements) for the array. The order of the n-grams in the result is unspecified. | `array(array(T))`  |

```sql
SELECT ngrams(ARRAY['foo', 'bar', 'baz', 'foo'], 2);
-- [['foo', 'bar'], ['bar', 'baz'], ['baz', 'foo']]

SELECT ngrams(ARRAY['foo', 'bar', 'baz', 'foo'], 3);
-- [['foo', 'bar', 'baz'], ['bar', 'baz', 'foo']]

SELECT ngrams(ARRAY['foo', 'bar', 'baz', 'foo'], 4);
-- [['foo', 'bar', 'baz', 'foo']]

SELECT ngrams(ARRAY['foo', 'bar', 'baz', 'foo'], 5);
-- [['foo', 'bar', 'baz', 'foo']]

SELECT ngrams(ARRAY[1, 2, 3, 4], 2);
-- [[1, 2], [2, 3], [3, 4]]

```

### **`none_match()`**

| Function                                       | Description                                                                                                      | Return Type |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------|
| `none_match(array(T), function(T, boolean))`    | Returns whether no elements of an array match the given predicate. Returns `true` if none of the elements matches the predicate (a special case is when the array is empty); `false` if one or more elements match; `NULL` if the predicate function returns `NULL` for one or more elements and `false` for all other elements. | `boolean`   |


### **`reduce()`**

| Function                                       | Description                                                                                                                                                                       | Return Type |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| `reduce(array(T), initialState S, inputFunction(S, T, S), outputFunction(S, R))`    | Returns a single value reduced from the array. `inputFunction` will be invoked for each element in the array in order. In addition to taking the element, `inputFunction` takes the current state, initially `initialState`, and returns the new state. `outputFunction` will be invoked to turn the final state into the result value. It may be the identity function (i -> i). | `R`         |


```sql
SELECT reduce(ARRAY[], 0,
              (s, x) -> s + x,
              s -> s);
-- 0

SELECT reduce(ARRAY[5, 20, 50], 0,
              (s, x) -> s + x,
              s -> s);
-- 75

SELECT reduce(ARRAY[5, 20, NULL, 50], 0,
              (s, x) -> s + x,
              s -> s);
-- NULL

SELECT reduce(ARRAY[5, 20, NULL, 50], 0,
              (s, x) -> s + coalesce(x, 0),
              s -> s);
-- 75

SELECT reduce(ARRAY[5, 20, NULL, 50], 0,
              (s, x) -> IF(x IS NULL, s, s + x),
              s -> s);
-- 75

SELECT reduce(ARRAY[2147483647, 1], BIGINT '0',
              (s, x) -> s + x,
              s -> s);
-- 2147483648

-- calculates arithmetic average
SELECT reduce(ARRAY[5, 6, 10, 20],
              CAST(ROW(0.0, 0) AS ROW(sum DOUBLE, count INTEGER)),
              (s, x) -> CAST(ROW(x + s.sum, s.count + 1) AS
                             ROW(sum DOUBLE, count INTEGER)),
              s -> IF(s.count = 0, NULL, s.sum / s.count));
-- 10.25
```


### **`repeat()`**

| Function                     | Description                                                   | Return Type |
|------------------------------|---------------------------------------------------------------|-------------|
| `repeat(element, count)`     | Repeat the element for `count` times.                           | `array`     |


### **`sequence()`**

| Function                     | Description                                                                                                                        | Return Type |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------|
| `sequence(start, stop)`       | Generate a sequence of integers from `start` to `stop`, incrementing by 1 if `start` is less than or equal to `stop`, otherwise -1. | `array`     |
| `sequence(start, stop, step)` | Generate a sequence of integers from `start` to `stop`, incrementing by `step`.                                                  | `array`     |
| `sequence(start, stop)`       | Generate a sequence of dates from `start` date to `stop` date, incrementing by 1 day if `start` date is less than or equal to `stop` date, otherwise -1 day. | `array`     |
| `sequence(start, stop, step)` | Generate a sequence of dates from `start` to `stop`, incrementing by `step`. The type of step can be either INTERVAL DAY TO SECOND or INTERVAL YEAR TO MONTH. | `array`     |
| `sequence(start, stop, step)` | Generate a sequence of timestamps from `start` to `stop`, incrementing by `step`. The type of step can be either INTERVAL DAY TO SECOND or INTERVAL YEAR TO MONTH. | `array`     |



### **`shuffle()`**

| Function              | Description                                      | Return Type |
|-----------------------|--------------------------------------------------|-------------|
| `shuffle(x)`          | Generate a random permutation of the given array `x`. | `array`     |


### **`trim_array()`**

| Function                | Description                                   | Return Type |
|-------------------------|-----------------------------------------------|-------------|
| `trim_array(x, n)`      | Remove `n` elements from the end of the array. | `array`     |


```sql
SELECT trim_array(ARRAY[1, 2, 3, 4], 1);
-- [1, 2, 3]

SELECT trim_array(ARRAY[1, 2, 3, 4], 2);
-- [1, 2]
```

### **`transform()`**

| Function                           | Description                                                                   | Return Type |
|------------------------------------|-------------------------------------------------------------------------------|-------------|
| `transform(array(T), function(T, U))` | Returns an array that is the result of applying `function` to each element of the array. | `array(U)`  |

```sql
SELECT transform(ARRAY[], x -> x + 1);
-- []

SELECT transform(ARRAY[5, 6], x -> x + 1);
-- [6, 7]

SELECT transform(ARRAY[5, NULL, 6], x -> coalesce(x, 0) + 1);
-- [6, 1, 7]

SELECT transform(ARRAY['x', 'abc', 'z'], x -> x || '0');
-- ['x0', 'abc0', 'z0']

SELECT transform(ARRAY[ARRAY[1, NULL, 2], ARRAY[3, NULL]],
                 a -> filter(a, x -> x IS NOT NULL));
-- [[1, 2], [3]]
```

### **`zip()`**

| Function                           | Description                                                                                                     | Return Type |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------|
| `zip(array1, array2[, ...])`       | Merges the given arrays, element-wise, into a single array of rows. The M-th element of the N-th argument will be the N-th field of the M-th output element. If the arguments have an uneven length, missing values are filled with NULL. | `array(row)` |


```sql
SELECT zip(ARRAY[1, 2], ARRAY['1b', null, '3b']);
-- [ROW(1, '1b'), ROW(2, null), ROW(null, '3b')]

```
### **`zip_with()`**

| Function                                | Description                                                                                                                                     | Return Type |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| `zip_with(array(T), array(U), function(T, U, R))` | Merges the two given arrays, element-wise, into a single array using `function`. If one array is shorter, nulls are appended at the end to match the length of the longer array, before applying `function`. | `array(R)`  |


```sql
SELECT zip_with(ARRAY[1, 3, 5], ARRAY['a', 'b', 'c'],
                (x, y) -> (y, x));
-- [ROW('a', 1), ROW('b', 3), ROW('c', 5)]

SELECT zip_with(ARRAY[1, 2], ARRAY[3, 4],
                (x, y) -> x + y);
-- [4, 6]

SELECT zip_with(ARRAY['a', 'b', 'c'], ARRAY['d', 'e', 'f'],
                (x, y) -> concat(x, y));
-- ['ad', 'be', 'cf']

SELECT zip_with(ARRAY['a'], ARRAY['d', null, 'f'],
                (x, y) -> coalesce(x, y));
-- ['a', null, 'f']
```