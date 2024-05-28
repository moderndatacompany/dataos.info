# Set Digest Functions

Minerva offers several functions for implementing the MinHash technique, which is commonly used to estimate the Jaccard similarity coefficient between two sets. This technique is particularly useful in data mining for efficiently detecting near-duplicate web pages at scale. By leveraging MinHash, search engines can effectively filter out nearly identical pages from their search results.

For instance, let's consider a scenario where we want to estimate the similarity between two texts. We can achieve this by splitting the texts into 4-shingles using the ngrams() function. These shingles serve as the input for creating a set digest for each original text. By comparing these set digests, we can approximate the similarity between the initial texts.

```sql
WITH text_input(id, text) AS (
         VALUES
             (1, 'The quick brown fox jumps over the lazy dog'),
             (2, 'The quick and the lazy'),
             (3, 'The quick brown fox jumps over the dog')
     ),
     text_ngrams(id, ngrams) AS (
         SELECT id,
                transform(
                  ngrams(
                    split(text, ' '),
                    4
                  ),
                  token -> array_join(token, ' ')
                )
         FROM text_input
     ),
     minhash_digest(id, digest) AS (
         SELECT id,
                (SELECT make_set_digest(v) FROM unnest(ngrams) u(v))
         FROM text_ngrams
     ),
     setdigest_side_by_side(id1, digest1, id2, digest2) AS (
         SELECT m1.id as id1,
                m1.digest as digest1,
                m2.id as id2,
                m2.digest as digest2
         FROM (SELECT id, digest FROM minhash_digest) m1
         JOIN (SELECT id, digest FROM minhash_digest) m2
           ON m1.id != m2.id AND m1.id < m2.id
     )
SELECT id1,
       id2,
       intersection_cardinality(digest1, digest2) AS intersection_cardinality,
       jaccard_index(digest1, digest2)            AS jaccard_index
FROM setdigest_side_by_side
ORDER BY id1, id2;
```  

```sql
| id1 | id2 | intersection_cardinality | jaccard_index |
|-----|-----|--------------------------|---------------|
|   1 |   2 |                        0 |           0.0 |
|   1 |   3 |                        4 |           0.6 |
|   2 |   3 |                        0 |           0.0 |
```


## Data structures
In Minerva, Set Digest data sketches are constructed by combining two key components:

* HyperLogLog: This component approximates the number of distinct elements within the original set. It's particularly useful for estimating cardinality with minimal memory usage.

* MinHash with a single hash function: The MinHash structure is employed to generate a compact signature of the original set, resulting in a low-memory footprint representation. This signature allows for efficient comparison of similarities between sets.

Minerva provides the setdigest type to encapsulate these data structures. Additionally, Trino enables the merging of multiple Set Digest data sketches, facilitating the aggregation and analysis of large datasets efficiently.

## Serialization
Data sketches can be serialized to and deserialized from varbinary. This allows them to be stored for later use.

## Functions

### **`make_set_digest()`**

| Function                  | Description                                            | Return Value |
| ------------------------- | ------------------------------------------------------ | ------------ |
| `make_set_digest(x)`      | Composes all input values of `x` into a setdigest.     | setdigest    |

Create a `setdigest` corresponding to a `bigint` array:

```sql
SELECT make_set_digest(value)
FROM (VALUES 1, 2, 3) T(value);
```
Create a `setdigest` corresponding to a `varchar` array:

```sql
SELECT make_set_digest(value)
FROM (VALUES 'Minerva', 'SQL', 'on', 'everything') T(value);
```
### **`merge_set_digest()`**

| Function                          | Description                                                               | Return Value |
| --------------------------------- | ------------------------------------------------------------------------- | ------------ |
| `merge_set_digest(setdigest)`     | Returns the setdigest of the aggregate union of the individual setdigest Set Digest structures. | setdigest    |

### **`cardinality()`**

| Function                        | Description                                                                   | Return Value |
| ------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| `cardinality(setdigest)`        | Returns the cardinality of the set digest from its internal HyperLogLog component. | long(or another large integer type)         |

Example:

```sql
SELECT cardinality(make_set_digest(value))
FROM (VALUES 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5) T(value);
-- 5
```

### **`intersection_cardinality()`**

| Function                           | Description                                                                                         | Return Value   |
| ---------------------------------- | --------------------------------------------------------------------------------------------------- | -------------- |
| `intersection_cardinality(x, y)`   | Returns the estimation for the cardinality of the intersection of the two set digests.             | long (or another large integer type) |

Example:

```sql
SELECT intersection_cardinality(make_set_digest(v1), make_set_digest(v2))
FROM (VALUES (1, 1), (NULL, 2), (2, 3), (3, 4)) T(v1, v2);
-- 3
```

### **`jaccard_index()`**

| Function                     | Description                                                                               | Return Type       |
| ---------------------------- | ----------------------------------------------------------------------------------------- | ----------------- |
| `jaccard_index(x, y) → double` | Returns the estimation of Jaccard index for the two set digests. `x` and `y` must be of type setdigest. | float (or double precision) |


Example:

```sql
SELECT jaccard_index(make_set_digest(v1), make_set_digest(v2))
FROM (VALUES (1, 1), (NULL,2), (2, 3), (NULL, 4)) T(v1, v2);
-- 0.5
```

### **`hash_counts()`**

| Function                   | Description                                                                                                       | Return Value         |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------- |
| `hash_counts(x)`           | Returns a map containing the Murmur3Hash128 hashed values and the count of their occurrences within the internal MinHash structure belonging to `x`. | Map (hashed value, count) |

Example:

```sql
SELECT hash_counts(make_set_digest(value))
FROM (VALUES 1, 1, 1, 2, 2) T(value);
-- {19144387141682250=3, -2447670524089286488=2}
```


