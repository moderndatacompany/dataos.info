# SQL Query Optimization


# Avoid Expensive Operations

> **Beneficial Scenario:** Joins causing expensive shuffles resulting in low performance
> 

Joins cause shuffling hence should be looked at carefully and optimized. Try to avoid the following operations - 

- `Count`
- `Repartition`
- `DistinctCount`

**What to do?**

- Instead of `DistinctCount`, use `approxCountDistinct`.
- `dropDuplicates` BEFORE `join`
- `dropDuplicates` BEFORE `groupBy`

# Level of Parallelism

> **Beneficial Scenario:** Increase or decrease partitions
> 

There are two ways to maintain parallelism:

**Repartition:** Gives an equal number of partitions with high shuffling, so it's not advisable to go for Repartition when you want to lash all the data.

**Coalesce:** Generally reduces the number of partitions with less shuffling.

## Using `COALESCE` and `REPARTITION` on SQL

While working with Spark SQL query, you can use `COALESCE`, `REPARTITION`, and `REPARTITION_BY_RANGE` within the query to increase or decrease the partitions on your data size.

```sql
SELECT /*+ COALESCE(3) */ * FROM EMP_TABLE
SELECT /*+ REPARTITION(3) */ * FROM EMP_TABLE
SELECT /*+ REPARTITION(c) */ * FROM EMP_TABLE
SELECT /*+ REPARTITION(3, dept_col) */ * FROM EMP_TABLE
SELECT /*+ REPARTITION_BY_RANGE(dept_col) */ * FROM EMP_TABLE
SELECT /*+ REPARTITION_BY_RANGE(3, dept_col) */ * FROM EMP_TABLE
```

# Predicate Pushdown Optimization

> **Beneficial Scenario:** When you want to limit the number of files and partitions SparkSQL reads while querying, to reduce disk I/O
> 

Predicate Pushdown is a technique to process only the required data. Predicates can be applied to SparkSQL by defining filters in where conditions. 

When creating Spark SQL queries that use comparison operators, making sure that the predicates are pushed down to the database correctly is critical to retrieving the correct data with the best performance.

For example, instead of 

```sql
SELECT * FROM test.common WHERE birthday < '2001-1-1';
```

Use 

```sql
SELECT * FROM test.common WHERE birthday < cast('2001-1-1' as TIMESTAMP)
```

Querying on data in buckets with predicate pushdowns produces results faster with less shuffle.

# Windowing Function

> **Beneficial Scenario:** When you have to carry out processing tasks such as calculating a moving average, computing a cumulative statistic, or accessing the value of rows given the relative position of the current row
> 

A window function defines a frame through which we can calculate the input rows of a table. On individual row level. Each row can have a clear framework. Windowing allows us to define a window for data in the data frame. We can compare multiple rows in the same data frame.

![Diagrammatic Representation of Window Function](SQL%20Query%20Optimization%20c852ab1245ce4608b4b568baf8b995c5/Untitled.png)

Diagrammatic Representation of Window Function

******************************************************Syntax of a window function******************************************************

```sql
window_function [ nulls_option ] OVER
( [  { PARTITION | DISTRIBUTE } BY partition_col_name = partition_col_val ( [ , ... ] ) ]
  { ORDER | SORT } BY expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [ , ... ]
  [ window_frame ] )
```

# Persisting and Caching Data in Memory

> **Useful Scenario:** Dataset is accessed multiple times in a single job or task or when there is an iterative loop such as in Machine Learning algorithms or the cost to generate the partitions again is higher.
> 

Spark persisting/caching is one of the best techniques to improve the performance of Spark workloads. Spark provides an optimization mechanism to store the intermediate computation of a Spark DataFrame so it can be reused in subsequent actions.

**Persist** - some part stored in memory and some part stored in disks.

**Caching** - storing always in memory. It is the same as persisting in memory only.

<aside>
🗣️ Transformations in Spark are lazily evaluated. Cache the dataset only when you’re sure that the cached data will be used for further transformation down the line. **Do not cache just because the dataset is small, or it's a dimension table (rather broadcast it)**. Too much caching can create overhead for the LRU algorithm as it will keep evicting things being cached and bringing new ones in to replace them. And the cycle will continue. 
Caching needs to be seen from the perspective of the data lineage, the DAG of transformations. Observe the **amount of data cached** in Spark UI and then decide.

</aside>

To know more about caching and its implementation within Flare click on the below link

[Case Scenario: Caching](../../Case%20Scenario%20eeb9bafe12c243ae8703f7e01f41b55f/Caching%20e4755604c8844ae89cb8ded0dfd75584.md)

# Broadcasting (Broadcast Joins)

Broadcasting is a technique to load small data files or datasets into Blocks of memory so that they can be joined with more massive data sets with less overhead of shuffling data.

# Bucketing

An alternative to partitioning is Bucketing. Conceptually it tries to achieve the same performance benefit, but rather than creating a directory per partition, bucketing distributes data across a group of predefined buckets using a hash on the bucket value.

To know more about bucketing and its implementation within Flare click on the below link

[Case Scenario: Bucketing](../../Case%20Scenario%20eeb9bafe12c243ae8703f7e01f41b55f/Bucketing%20e005ac7285b04f31be27c28b0c6c981d.md)

Table of Contents