# HyperLogLog functions

Minerva implements the [approx_distinct()](./aggregate.md#approximate_distinct) function using the [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog) data structure.


## Data Structures

Minerva utilizes HyperLogLog data sketches, representing them as a collection of 32-bit buckets that store a maximum hash. These sketches can be stored either sparsely, functioning as a map from bucket ID to bucket, or densely, as a continuous memory block. Initially, the HyperLogLog data structure adopts the sparse representation and transitions to the dense format when deemed more efficient. In contrast, the P4HyperLogLog structure is initialized in a dense state and maintains this denseness throughout its lifetime.

[HyperLogLog](./hyperloglog.md#hyperloglog) implicitly casts to [P4HyperLogLog](./hyperloglog.md#p4hyperloglog), while one can explicitly cast `HyperLogLog` to `P4HyperLogLog`:


```sql
cast(hll AS P4HyperLogLog)
```


## Serialization

Serialization to and deserialization from varbinary empowers data sketches to be stored for subsequent use. When combined with the ability to merge multiple sketches, this facilitates the efficient computation of [approx_distinct()](./aggregate.md#approximate_distinct) for elements within a query partition. Consequently, the overall distinct count for an entire query can be determined with minimal computational cost.

For instance, computing the HyperLogLog for daily unique users enables the incremental calculation of weekly or monthly unique users by aggregating the daily results. This approach is analogous to computing weekly revenue by summing daily revenue. HyperLogLog seamlessly replaces [approx_distinct()](./aggregate.md#approximate_distinct) with GROUPING SETS in various scenarios. Examples include:

```sql
CREATE TABLE visit_summaries (
  visit_date date,
  hll varbinary
);

INSERT INTO visit_summaries
SELECT visit_date, cast(approx_set(user_id) AS varbinary)
FROM user_visits
GROUP BY visit_date;

SELECT cardinality(merge(cast(hll AS HyperLogLog))) AS weekly_unique_users
FROM visit_summaries
WHERE visit_date >= current_date - interval '7' day;
```

## Functions

### **`approx_set(x)`**

| Function         | Description                                                                                                          | Return Type   |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- | ------------- |
| `approx_set(x)`  | Returns the HyperLogLog sketch of the input data set `x`. This data sketch underlies `approx_distinct()` and can be stored and used later by calling `cardinality()`. | `HyperLogLog` |

### **`cardinality()`**

| Function         | Description                                           | Return Type   |
| ---------------- | ----------------------------------------------------- | ------------- |
| `cardinality(hll)` | Performs `approx_distinct()` on the data summarized by the `hll` HyperLogLog data sketch. | `bigint`      |

### **`empty_approx_set()`**

| Function             | Description                  | Return Type   |
| -------------------- | ---------------------------- | ------------- |
| `empty_approx_set()` | Returns an empty HyperLogLog. | `HyperLogLog` |

### **`merge(HyperLogLog)`**

| Function              | Description                                               | Return Type   |
| --------------------- | --------------------------------------------------------- | ------------- |
| `merge(HyperLogLog)`  | Returns the HyperLogLog of the aggregate union of the individual `hll` HyperLogLog structures. | `HyperLogLog` |


### Data types

HyperLogLog

A HyperLogLog sketch allows efficient computation of [approx_distinct()](./aggregate.md#approximate_distinct). It starts as a sparse representation, switching to a dense representation when it becomes more efficient


P4HyperLogLog

A P4HyperLogLog sketch is similar to [HyperLogLog](./hyperloglog.md#hyperloglog), but it starts (and remains) in the dense representation.