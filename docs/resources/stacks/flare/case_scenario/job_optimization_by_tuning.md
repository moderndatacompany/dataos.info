# Job Optimization by Tuning

The following document outlines the optimized Flare job configuration for enhanced performance. Various adjustments have been made to both the driver and executor settings, as well as key Spark configurations. These changes aim to improve resource allocation, optimize memory usage, and enhance the execution speed of Flare jobs.

## Code Snippet


```yaml
version: v1
name: wf-orders-enriched-data
type: workflow
tags:
  - customers
  - orders
description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
workflow:
  title: Customer Order Enriched Data
  dag:
    - name: orders-enriched-data
      title: Customer Order Enriched Data
      description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
      spec:
        tags:
          - customers
          - orders
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2200m
            cores: 3
            instances: 2
            memory: 4800m
          job:
            explain: true
            inputs:
              - name: region
                dataset: dataos://snowflake:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: last_5_tans_each_cust
                dataset: dataos://icebase:sandbox/last_5_tans_each_cust?acl=rw
                format: Iceberg
                description: This dataset has information of all event
                tags:
                  - clickstream
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: O_ORDERDATE
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: event_name
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: month
                      column: O_ORDERDATE
                      name: month
                    - type: identity
                      column: user_agent
                title: Customer Order Enriched Data
            steps:
              - sequence:
                  - name: nation_region
                    sql: select * from nation left join region on n_regionkey = r_regionkey

                  - name: cust_repart
                    sql: SELECT /*+ REPARTITION(c_nationkey) */ * FROM customer

                  - name: customer_nation_region # customer_final
                    sql: select /*+ MAPJOIN(nation_region) */ * from cust_repart left join nation_region on c_nationkey = n_nationkey

                  - name: repart_customer_nation_region
                    sql: select /*+ REPARTITION(100,c_custkey) */ * from customer_nation_region

                  - name: ps_repart
                    sql: select /*+ REPARTITION(ps_suppkey,ps_PARTKEY) */ * from partsupp

                  - name: partsupp_supp
                    sql: select * from ps_repart left join suppliers on ps_suppkey = s_suppkey

                  - name: partsupp_supp_part
                    sql: select * from partsupp_supp left join part on ps_partkey = p_partkey


                  # Order
                  - name: filtered_order
                    sql: select *, row_number() over (partition by o_custkey order by o_orderdate desc) as ranked from orders

                  - name: latest_order
                    sql: select /*+ REPARTITION_BY_RANGE(100,o_orderkey) */ * from filtered_order where ranked <= 2

                  - name: order_cust
                    sql: select * from latest_order left join repart_customer_nation_region on o_custkey = c_custkey

                  - name: repart_order_cust
                    sql: select /*+ REPARTITION(100,o_orderkey) */ * from order_cust

                  - name: line_repart
                    sql: select * from lineitem

                  - name: order_cust_line
                    sql: select * from repart_order_cust right join line_repart on o_orderkey = l_orderkey

                  - name: repart_order_cust_line
                    sql: select /*+ REPARTITION(100,l_suppkey,l_partkey)*/ * from order_cust_line

                  - name: last_5_tans_each_cust
                    sql: select * from repart_order_cust_line left join partsupp_supp_part on s_suppkey = l_suppkey and p_partkey = l_partkey

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 50
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 45
            - spark.sql.broadcastTimeout: 15
```

## Method: 1

```yaml
          driver:
            coreLimit: 3800m
            cores: 2
            memory: 4000m
          executor:
            coreLimit: 7500m
            cores: 3
            instances: 3
            memory: 8000m

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 20m
            - spark.sql.shuffle.partitions: 450
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 300
            - spark.sql.broadcastTimeout: 200
```

Total Duration: 8.13

```
		RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
 ------------|----------|---------------------------|----------------------------
   succeeded | 8/8      | 2022-08-10T22:36:43+05:30 | 2022-08-10T22:44:16+05:30
```


<details>

<summary> Click here to see the full manifest file </summary>

```yaml
version: v1
name: wf-orders-enriched-data
type: workflow
tags:
  - customers
  - orders
description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
workflow:
  title: Customer Order Enriched Data
  dag:
    - name: orders-enriched-data
      title: Customer Order Enriched Data
      description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
      spec:
        tags:
          - customers
          - orders
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 3800m
            cores: 2
            memory: 4000m
          executor:
            coreLimit: 7500m
            cores: 3
            instances: 3
            memory: 8000m
          job:
            explain: true
            inputs:
              - name: region
                dataset: dataos://snowflake:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: last_5_tans_each_cust
                dataset: dataos://icebase:sandbox/last_5_tans_each_cust?acl=rw
                format: Iceberg
                description: This dataset has information of all event
                tags:
                  - clickstream
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: O_ORDERDATE
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: event_name
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: month
                      column: O_ORDERDATE
                      name: month
                    - type: identity
                      column: user_agent
                title: Customer Order Enriched Data
            steps:
              - sequence:
                  - name: nation_region
                    sql: select * from nation left join region on n_regionkey = r_regionkey

                  - name: cust_repart
                    sql: SELECT /*+ REPARTITION(c_nationkey) */ * FROM customer

                  - name: customer_nation_region # customer_final
                    sql: select /*+ MAPJOIN(nation_region) */ * from cust_repart left join nation_region on c_nationkey = n_nationkey

                  - name: repart_customer_nation_region
                    sql: select /*+ REPARTITION(100,c_custkey) */ * from customer_nation_region

                  - name: ps_repart
                    sql: select /*+ REPARTITION(ps_suppkey,ps_PARTKEY) */ * from partsupp

                  - name: partsupp_supp
                    sql: select * from ps_repart left join suppliers on ps_suppkey = s_suppkey

                  - name: partsupp_supp_part
                    sql: select * from partsupp_supp left join part on ps_partkey = p_partkey


                  # Order
                  - name: filtered_order
                    sql: select *, row_number() over (partition by o_custkey order by o_orderdate desc) as ranked from orders

                  - name: latest_order
                    sql: select /*+ REPARTITION_BY_RANGE(100,o_orderkey) */ * from filtered_order where ranked <= 2

                  - name: order_cust
                    sql: select * from latest_order left join repart_customer_nation_region on o_custkey = c_custkey

                  - name: repart_order_cust
                    sql: select /*+ REPARTITION(100,o_orderkey) */ * from order_cust

                  - name: line_repart
                    sql: select * from lineitem

                  - name: order_cust_line
                    sql: select * from repart_order_cust right join line_repart on o_orderkey = l_orderkey

                  - name: repart_order_cust_line
                    sql: select /*+ REPARTITION(100,l_suppkey,l_partkey)*/ * from order_cust_line

                  - name: last_5_tans_each_cust
                    sql: select * from repart_order_cust_line left join partsupp_supp_part on s_suppkey = l_suppkey and p_partkey = l_partkey

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 20m
            - spark.sql.shuffle.partitions: 450
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 300
            - spark.sql.broadcastTimeout: 200
```
</details>


## Method: 2

```yaml
					driver:
            coreLimit: 3800m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 3000m
            cores: 3
            instances: 3
            memory: 6000m

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 20m
            - spark.sql.shuffle.partitions: 450
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 300
            - spark.sql.broadcastTimeout: 200
```


Total Duration: 7.33

```yaml
   RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-10T22:50:41+05:30 | 2022-08-10T22:57:39+05:30
```


<details>

<summary> Click here to see the full manifest file </summary>

```yaml
version: v1
name: wf-orders-enriched-data
type: workflow
tags:
  - customers
  - orders
description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
workflow:
  title: Customer Order Enriched Data
  dag:
    - name: orders-enriched-data
      title: Customer Order Enriched Data
      description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
      spec:
        tags:
          - customers
          - orders
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
					driver:
            coreLimit: 3800m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 3000m
            cores: 3
            instances: 3
            memory: 6000m
          job:
            explain: true
            inputs:
              - name: region
                dataset: dataos://snowflake:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: last_5_tans_each_cust
                dataset: dataos://icebase:sandbox/last_5_tans_each_cust?acl=rw
                format: Iceberg
                description: This dataset has information of all event
                tags:
                  - clickstream
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: O_ORDERDATE
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: event_name
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: month
                      column: O_ORDERDATE
                      name: month
                    - type: identity
                      column: user_agent
                title: Customer Order Enriched Data
            steps:
              - sequence:
                  - name: nation_region
                    sql: select * from nation left join region on n_regionkey = r_regionkey

                  - name: cust_repart
                    sql: SELECT /*+ REPARTITION(c_nationkey) */ * FROM customer

                  - name: customer_nation_region # customer_final
                    sql: select /*+ MAPJOIN(nation_region) */ * from cust_repart left join nation_region on c_nationkey = n_nationkey

                  - name: repart_customer_nation_region
                    sql: select /*+ REPARTITION(100,c_custkey) */ * from customer_nation_region

                  - name: ps_repart
                    sql: select /*+ REPARTITION(ps_suppkey,ps_PARTKEY) */ * from partsupp

                  - name: partsupp_supp
                    sql: select * from ps_repart left join suppliers on ps_suppkey = s_suppkey

                  - name: partsupp_supp_part
                    sql: select * from partsupp_supp left join part on ps_partkey = p_partkey


                  # Order
                  - name: filtered_order
                    sql: select *, row_number() over (partition by o_custkey order by o_orderdate desc) as ranked from orders

                  - name: latest_order
                    sql: select /*+ REPARTITION_BY_RANGE(100,o_orderkey) */ * from filtered_order where ranked <= 2

                  - name: order_cust
                    sql: select * from latest_order left join repart_customer_nation_region on o_custkey = c_custkey

                  - name: repart_order_cust
                    sql: select /*+ REPARTITION(100,o_orderkey) */ * from order_cust

                  - name: line_repart
                    sql: select * from lineitem

                  - name: order_cust_line
                    sql: select * from repart_order_cust right join line_repart on o_orderkey = l_orderkey

                  - name: repart_order_cust_line
                    sql: select /*+ REPARTITION(100,l_suppkey,l_partkey)*/ * from order_cust_line

                  - name: last_5_tans_each_cust
                    sql: select * from repart_order_cust_line left join partsupp_supp_part on s_suppkey = l_suppkey and p_partkey = l_partkey

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 20m
            - spark.sql.shuffle.partitions: 450
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 300
            - spark.sql.broadcastTimeout: 200
```
</details>

## Method: 3

In this approach, the configuration settings are left at their default values, allowing Apache Spark to automatically manage the execution and optimization of tasks.

```yaml
					driver:
            coreLimit: 3800m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 3
            instances: 3
            memory: 6000m

            #spark configuration would be set as default
```


<details> 

<summary> Click here to see the full manifest file </summary>

```yaml
version: v1
name: wf-orders-enriched-data
type: workflow
tags:
  - customers
  - orders
description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
workflow:
  title: Customer Order Enriched Data
  dag:
    - name: orders-enriched-data
      title: Customer Order Enriched Data
      description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
      spec:
        tags:
          - customers
          - orders
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
					driver:
            coreLimit: 3800m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 3
            instances: 3
            memory: 6000m
          job:
            explain: true
            inputs:
              - name: region
                dataset: dataos://snowflake:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: last_5_tans_each_cust
                dataset: dataos://icebase:sandbox/last_5_tans_each_cust?acl=rw
                format: Iceberg
                description: This dataset has information of all event
                tags:
                  - clickstream
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: O_ORDERDATE
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: event_name
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: month
                      column: O_ORDERDATE
                      name: month
                    - type: identity
                      column: user_agent
                title: Customer Order Enriched Data
            steps:
              - sequence:
                  - name: nation_region
                    sql: select * from nation left join region on n_regionkey = r_regionkey

                  - name: cust_repart
                    sql: SELECT /*+ REPARTITION(c_nationkey) */ * FROM customer

                  - name: customer_nation_region # customer_final
                    sql: select /*+ MAPJOIN(nation_region) */ * from cust_repart left join nation_region on c_nationkey = n_nationkey

                  - name: repart_customer_nation_region
                    sql: select /*+ REPARTITION(100,c_custkey) */ * from customer_nation_region

                  - name: ps_repart
                    sql: select /*+ REPARTITION(ps_suppkey,ps_PARTKEY) */ * from partsupp

                  - name: partsupp_supp
                    sql: select * from ps_repart left join suppliers on ps_suppkey = s_suppkey

                  - name: partsupp_supp_part
                    sql: select * from partsupp_supp left join part on ps_partkey = p_partkey


                  # Order
                  - name: filtered_order
                    sql: select *, row_number() over (partition by o_custkey order by o_orderdate desc) as ranked from orders

                  - name: latest_order
                    sql: select /*+ REPARTITION_BY_RANGE(100,o_orderkey) */ * from filtered_order where ranked <= 2

                  - name: order_cust
                    sql: select * from latest_order left join repart_customer_nation_region on o_custkey = c_custkey

                  - name: repart_order_cust
                    sql: select /*+ REPARTITION(100,o_orderkey) */ * from order_cust

                  - name: line_repart
                    sql: select * from lineitem

                  - name: order_cust_line
                    sql: select * from repart_order_cust right join line_repart on o_orderkey = l_orderkey

                  - name: repart_order_cust_line
                    sql: select /*+ REPARTITION(100,l_suppkey,l_partkey)*/ * from order_cust_line

                  - name: last_5_tans_each_cust
                    sql: select * from repart_order_cust_line left join partsupp_supp_part on s_suppkey = l_suppkey and p_partkey = l_partkey
```
</details>

Total Duration: 6.25

```yaml
	 RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-10T23:24:06+05:30 | 2022-08-10T23:30:31+05:30
```

## Method: 4

```yaml
					driver:
            coreLimit: 3800m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 2
            instances: 4
            memory: 6000m

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 150
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 130
            - spark.sql.broadcastTimeout: 30
```


Total Duration: 6.04

```yaml
   RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-11T10:41:29+05:30 | 2022-08-11T10:47:33+05:30
```


<details>

```yaml
version: v1
name: wf-orders-enriched-data
type: workflow
tags:
  - customers
  - orders
description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
workflow:
  title: Customer Order Enriched Data
  dag:
    - name: orders-enriched-data
      title: Customer Order Enriched Data
      description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
      spec:
        tags:
          - customers
          - orders
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
					driver:
            coreLimit: 3800m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 2
            instances: 4
            memory: 6000m
          job:
            explain: true
            inputs:
              - name: region
                dataset: dataos://snowflake:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: last_5_tans_each_cust
                dataset: dataos://icebase:sandbox/last_5_tans_each_cust?acl=rw
                format: Iceberg
                description: This dataset has information of all event
                tags:
                  - clickstream
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: O_ORDERDATE
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: event_name
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: month
                      column: O_ORDERDATE
                      name: month
                    - type: identity
                      column: user_agent
                title: Customer Order Enriched Data
            steps:
              - sequence:
                  - name: nation_region
                    sql: select * from nation left join region on n_regionkey = r_regionkey

                  - name: cust_repart
                    sql: SELECT /*+ REPARTITION(c_nationkey) */ * FROM customer

                  - name: customer_nation_region # customer_final
                    sql: select /*+ MAPJOIN(nation_region) */ * from cust_repart left join nation_region on c_nationkey = n_nationkey

                  - name: repart_customer_nation_region
                    sql: select /*+ REPARTITION(100,c_custkey) */ * from customer_nation_region

                  - name: ps_repart
                    sql: select /*+ REPARTITION(ps_suppkey,ps_PARTKEY) */ * from partsupp

                  - name: partsupp_supp
                    sql: select * from ps_repart left join suppliers on ps_suppkey = s_suppkey

                  - name: partsupp_supp_part
                    sql: select * from partsupp_supp left join part on ps_partkey = p_partkey


                  # Order
                  - name: filtered_order
                    sql: select *, row_number() over (partition by o_custkey order by o_orderdate desc) as ranked from orders

                  - name: latest_order
                    sql: select /*+ REPARTITION_BY_RANGE(100,o_orderkey) */ * from filtered_order where ranked <= 2

                  - name: order_cust
                    sql: select * from latest_order left join repart_customer_nation_region on o_custkey = c_custkey

                  - name: repart_order_cust
                    sql: select /*+ REPARTITION(100,o_orderkey) */ * from order_cust

                  - name: line_repart
                    sql: select * from lineitem

                  - name: order_cust_line
                    sql: select * from repart_order_cust right join line_repart on o_orderkey = l_orderkey

                  - name: repart_order_cust_line
                    sql: select /*+ REPARTITION(100,l_suppkey,l_partkey)*/ * from order_cust_line

                  - name: last_5_tans_each_cust
                    sql: select * from repart_order_cust_line left join partsupp_supp_part on s_suppkey = l_suppkey and p_partkey = l_partkey

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 150
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 130
            - spark.sql.broadcastTimeout: 30

```
</details>

## Method: 5


```yaml
          driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 2
            instances: 4
            memory: 6000m

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 150
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 130
            - spark.sql.broadcastTimeout: 30
```


Total Duration: 6.05

```yaml
   RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-11T22:38:39+05:30 | 2022-08-11T22:44:44+05:30
```


<details>

<summary> Click here to see the full manifest file </summary>

```yaml
version: v1
name: wf-orders-enriched-data
type: workflow
tags:
  - customers
  - orders
description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
workflow:
  title: Customer Order Enriched Data
  dag:
    - name: orders-enriched-data
      title: Customer Order Enriched Data
      description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
      spec:
        tags:
          - customers
          - orders
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 2
            instances: 4
            memory: 6000m
          job:
            explain: true
            inputs:
              - name: region
                dataset: dataos://snowflake:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: last_5_tans_each_cust
                dataset: dataos://icebase:sandbox/last_5_tans_each_cust?acl=rw
                format: Iceberg
                description: This dataset has information of all event
                tags:
                  - clickstream
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: O_ORDERDATE
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: event_name
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: month
                      column: O_ORDERDATE
                      name: month
                    - type: identity
                      column: user_agent
                title: Customer Order Enriched Data
            steps:
              - sequence:
                  - name: nation_region
                    sql: select * from nation left join region on n_regionkey = r_regionkey

                  - name: cust_repart
                    sql: SELECT /*+ REPARTITION(c_nationkey) */ * FROM customer

                  - name: customer_nation_region # customer_final
                    sql: select /*+ MAPJOIN(nation_region) */ * from cust_repart left join nation_region on c_nationkey = n_nationkey

                  - name: repart_customer_nation_region
                    sql: select /*+ REPARTITION(100,c_custkey) */ * from customer_nation_region

                  - name: ps_repart
                    sql: select /*+ REPARTITION(ps_suppkey,ps_PARTKEY) */ * from partsupp

                  - name: partsupp_supp
                    sql: select * from ps_repart left join suppliers on ps_suppkey = s_suppkey

                  - name: partsupp_supp_part
                    sql: select * from partsupp_supp left join part on ps_partkey = p_partkey


                  # Order
                  - name: filtered_order
                    sql: select *, row_number() over (partition by o_custkey order by o_orderdate desc) as ranked from orders

                  - name: latest_order
                    sql: select /*+ REPARTITION_BY_RANGE(100,o_orderkey) */ * from filtered_order where ranked <= 2

                  - name: order_cust
                    sql: select * from latest_order left join repart_customer_nation_region on o_custkey = c_custkey

                  - name: repart_order_cust
                    sql: select /*+ REPARTITION(100,o_orderkey) */ * from order_cust

                  - name: line_repart
                    sql: select * from lineitem

                  - name: order_cust_line
                    sql: select * from repart_order_cust right join line_repart on o_orderkey = l_orderkey

                  - name: repart_order_cust_line
                    sql: select /*+ REPARTITION(100,l_suppkey,l_partkey)*/ * from order_cust_line

                  - name: last_5_tans_each_cust
                    sql: select * from repart_order_cust_line left join partsupp_supp_part on s_suppkey = l_suppkey and p_partkey = l_partkey

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 150
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 130
            - spark.sql.broadcastTimeout: 30
```
</details>

## Method: 6

```yaml
					driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 2
            instances: 3
            memory: 5000m

        sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 100
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 80
            - spark.sql.broadcastTimeout: 30
```

Total Duration: 6.11

```yaml
	 RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-11T22:46:25+05:30 | 2022-08-11T22:52:36+05:30
```


<details>
<summary> Click here to see the full manifest file </summary>

```yaml
version: v1
name: wf-orders-enriched-data
type: workflow
tags:
  - customers
  - orders
description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
workflow:
  title: Customer Order Enriched Data
  dag:
    - name: orders-enriched-data
      title: Customer Order Enriched Data
      description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
      spec:
        tags:
          - customers
          - orders
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
					driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 2
            instances: 3
            memory: 5000m
          job:
            explain: true
            inputs:
              - name: region
                dataset: dataos://snowflake:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: last_5_tans_each_cust
                dataset: dataos://icebase:sandbox/last_5_tans_each_cust?acl=rw
                format: Iceberg
                description: This dataset has information of all event
                tags:
                  - clickstream
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: O_ORDERDATE
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: event_name
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: month
                      column: O_ORDERDATE
                      name: month
                    - type: identity
                      column: user_agent
                title: Customer Order Enriched Data
            steps:
              - sequence:
                  - name: nation_region
                    sql: select * from nation left join region on n_regionkey = r_regionkey

                  - name: cust_repart
                    sql: SELECT /*+ REPARTITION(c_nationkey) */ * FROM customer

                  - name: customer_nation_region # customer_final
                    sql: select /*+ MAPJOIN(nation_region) */ * from cust_repart left join nation_region on c_nationkey = n_nationkey

                  - name: repart_customer_nation_region
                    sql: select /*+ REPARTITION(100,c_custkey) */ * from customer_nation_region

                  - name: ps_repart
                    sql: select /*+ REPARTITION(ps_suppkey,ps_PARTKEY) */ * from partsupp

                  - name: partsupp_supp
                    sql: select * from ps_repart left join suppliers on ps_suppkey = s_suppkey

                  - name: partsupp_supp_part
                    sql: select * from partsupp_supp left join part on ps_partkey = p_partkey


                  # Order
                  - name: filtered_order
                    sql: select *, row_number() over (partition by o_custkey order by o_orderdate desc) as ranked from orders

                  - name: latest_order
                    sql: select /*+ REPARTITION_BY_RANGE(100,o_orderkey) */ * from filtered_order where ranked <= 2

                  - name: order_cust
                    sql: select * from latest_order left join repart_customer_nation_region on o_custkey = c_custkey

                  - name: repart_order_cust
                    sql: select /*+ REPARTITION(100,o_orderkey) */ * from order_cust

                  - name: line_repart
                    sql: select * from lineitem

                  - name: order_cust_line
                    sql: select * from repart_order_cust right join line_repart on o_orderkey = l_orderkey

                  - name: repart_order_cust_line
                    sql: select /*+ REPARTITION(100,l_suppkey,l_partkey)*/ * from order_cust_line

                  - name: last_5_tans_each_cust
                    sql: select * from repart_order_cust_line left join partsupp_supp_part on s_suppkey = l_suppkey and p_partkey = l_partkey

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 100
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 80
            - spark.sql.broadcastTimeout: 30
```
</details>

## Method: 7

```yaml
          driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2200m
            cores: 3
            instances: 2
            memory: 5000m

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 100
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 80
            - spark.sql.broadcastTimeout: 30
```

Total Duration: 6.38

```yaml
   RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-11T22:58:41+05:30 | 2022-08-11T23:04:39+05:30
```

<details> 
<summary> Click here to see the full manifest file </summary>

```yaml
version: v1
name: wf-orders-enriched-data
type: workflow
tags:
  - customers
  - orders
description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
workflow:
  title: Customer Order Enriched Data
  dag:
    - name: orders-enriched-data
      title: Customer Order Enriched Data
      description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
      spec:
        tags:
          - customers
          - orders
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2200m
            cores: 3
            instances: 2
            memory: 5000m

          job:
            explain: true
            inputs:
              - name: region
                dataset: dataos://snowflake:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: last_5_tans_each_cust
                dataset: dataos://icebase:sandbox/last_5_tans_each_cust?acl=rw
                format: Iceberg
                description: This dataset has information of all event
                tags:
                  - clickstream
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: O_ORDERDATE
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: event_name
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: month
                      column: O_ORDERDATE
                      name: month
                    - type: identity
                      column: user_agent
                title: Customer Order Enriched Data
            steps:
              - sequence:
                  - name: nation_region
                    sql: select * from nation left join region on n_regionkey = r_regionkey

                  - name: cust_repart
                    sql: SELECT /*+ REPARTITION(c_nationkey) */ * FROM customer

                  - name: customer_nation_region # customer_final
                    sql: select /*+ MAPJOIN(nation_region) */ * from cust_repart left join nation_region on c_nationkey = n_nationkey

                  - name: repart_customer_nation_region
                    sql: select /*+ REPARTITION(100,c_custkey) */ * from customer_nation_region

                  - name: ps_repart
                    sql: select /*+ REPARTITION(ps_suppkey,ps_PARTKEY) */ * from partsupp

                  - name: partsupp_supp
                    sql: select * from ps_repart left join suppliers on ps_suppkey = s_suppkey

                  - name: partsupp_supp_part
                    sql: select * from partsupp_supp left join part on ps_partkey = p_partkey


                  # Order
                  - name: filtered_order
                    sql: select *, row_number() over (partition by o_custkey order by o_orderdate desc) as ranked from orders

                  - name: latest_order
                    sql: select /*+ REPARTITION_BY_RANGE(100,o_orderkey) */ * from filtered_order where ranked <= 2

                  - name: order_cust
                    sql: select * from latest_order left join repart_customer_nation_region on o_custkey = c_custkey

                  - name: repart_order_cust
                    sql: select /*+ REPARTITION(100,o_orderkey) */ * from order_cust

                  - name: line_repart
                    sql: select * from lineitem

                  - name: order_cust_line
                    sql: select * from repart_order_cust right join line_repart on o_orderkey = l_orderkey

                  - name: repart_order_cust_line
                    sql: select /*+ REPARTITION(100,l_suppkey,l_partkey)*/ * from order_cust_line

                  - name: last_5_tans_each_cust
                    sql: select * from repart_order_cust_line left join partsupp_supp_part on s_suppkey = l_suppkey and p_partkey = l_partkey


          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 100
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 80
            - spark.sql.broadcastTimeout: 30
```
</details>

## Method: 8

```yaml
          driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2200m
            cores: 3
            instances: 2
            memory: 4800m

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 75
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 60
            - spark.sql.broadcastTimeout: 15
```

Total Duration: 6

```yaml
   RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-11T23:07:17+05:30 | 2022-08-11T23:13:17+05:30
```

<details>
<summary> Click here to see the full manifest fil </summary>

```yaml
version: v1
name: wf-orders-enriched-data
type: workflow
tags:
  - customers
  - orders
description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
workflow:
  title: Customer Order Enriched Data
  dag:
    - name: orders-enriched-data
      title: Customer Order Enriched Data
      description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
      spec:
        tags:
          - customers
          - orders
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2200m
            cores: 3
            instances: 2
            memory: 4800m

          job:
            explain: true
            inputs:
              - name: region
                dataset: dataos://snowflake:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: last_5_tans_each_cust
                dataset: dataos://icebase:sandbox/last_5_tans_each_cust?acl=rw
                format: Iceberg
                description: This dataset has information of all event
                tags:
                  - clickstream
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: O_ORDERDATE
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: event_name
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: month
                      column: O_ORDERDATE
                      name: month
                    - type: identity
                      column: user_agent
                title: Customer Order Enriched Data
            steps:
              - sequence:
                  - name: nation_region
                    sql: select * from nation left join region on n_regionkey = r_regionkey

                  - name: cust_repart
                    sql: SELECT /*+ REPARTITION(c_nationkey) */ * FROM customer

                  - name: customer_nation_region # customer_final
                    sql: select /*+ MAPJOIN(nation_region) */ * from cust_repart left join nation_region on c_nationkey = n_nationkey

                  - name: repart_customer_nation_region
                    sql: select /*+ REPARTITION(100,c_custkey) */ * from customer_nation_region

                  - name: ps_repart
                    sql: select /*+ REPARTITION(ps_suppkey,ps_PARTKEY) */ * from partsupp

                  - name: partsupp_supp
                    sql: select * from ps_repart left join suppliers on ps_suppkey = s_suppkey

                  - name: partsupp_supp_part
                    sql: select * from partsupp_supp left join part on ps_partkey = p_partkey


                  # Order
                  - name: filtered_order
                    sql: select *, row_number() over (partition by o_custkey order by o_orderdate desc) as ranked from orders

                  - name: latest_order
                    sql: select /*+ REPARTITION_BY_RANGE(100,o_orderkey) */ * from filtered_order where ranked <= 2

                  - name: order_cust
                    sql: select * from latest_order left join repart_customer_nation_region on o_custkey = c_custkey

                  - name: repart_order_cust
                    sql: select /*+ REPARTITION(100,o_orderkey) */ * from order_cust

                  - name: line_repart
                    sql: select * from lineitem

                  - name: order_cust_line
                    sql: select * from repart_order_cust right join line_repart on o_orderkey = l_orderkey

                  - name: repart_order_cust_line
                    sql: select /*+ REPARTITION(100,l_suppkey,l_partkey)*/ * from order_cust_line

                  - name: last_5_tans_each_cust
                    sql: select * from repart_order_cust_line left join partsupp_supp_part on s_suppkey = l_suppkey and p_partkey = l_partkey

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 75
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 60
            - spark.sql.broadcastTimeout: 15
```
</details>



## Method: 9

```yaml
          driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2200m
            cores: 3
            instances: 2
            memory: 4800m

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 50
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 45
            - spark.sql.broadcastTimeout: 15
```

Total  Duration: 6.33

```yaml
   RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-11T23:51:59+05:30 | 2022-08-11T23:57:52+05:30
```

<details>
<summary> Click here to see the full manifest file </summary>

```yaml
version: v1
name: wf-orders-enriched-data
type: workflow
tags:
  - customers
  - orders
description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
workflow:
  title: Customer Order Enriched Data
  dag:
    - name: orders-enriched-data
      title: Customer Order Enriched Data
      description: The purpose of the workflow is to retrieve clickstream data from blobstorage to Icebase.
      spec:
        tags:
          - customers
          - orders
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 2000m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 2200m
            cores: 3
            instances: 2
            memory: 4800m

          job:
            explain: true
            inputs:
              - name: region
                dataset: dataos://snowflake:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: last_5_tans_each_cust
                dataset: dataos://icebase:sandbox/last_5_tans_each_cust?acl=rw
                format: Iceberg
                description: This dataset has information of all event
                tags:
                  - clickstream
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: O_ORDERDATE
                        order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: event_name
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: month
                      column: O_ORDERDATE
                      name: month
                    - type: identity
                      column: user_agent
                title: Customer Order Enriched Data
            steps:
              - sequence:
                  - name: nation_region
                    sql: select * from nation left join region on n_regionkey = r_regionkey

                  - name: cust_repart
                    sql: SELECT /*+ REPARTITION(c_nationkey) */ * FROM customer

                  - name: customer_nation_region # customer_final
                    sql: select /*+ MAPJOIN(nation_region) */ * from cust_repart left join nation_region on c_nationkey = n_nationkey

                  - name: repart_customer_nation_region
                    sql: select /*+ REPARTITION(100,c_custkey) */ * from customer_nation_region

                  - name: ps_repart
                    sql: select /*+ REPARTITION(ps_suppkey,ps_PARTKEY) */ * from partsupp

                  - name: partsupp_supp
                    sql: select * from ps_repart left join suppliers on ps_suppkey = s_suppkey

                  - name: partsupp_supp_part
                    sql: select * from partsupp_supp left join part on ps_partkey = p_partkey


                  # Order
                  - name: filtered_order
                    sql: select *, row_number() over (partition by o_custkey order by o_orderdate desc) as ranked from orders

                  - name: latest_order
                    sql: select /*+ REPARTITION_BY_RANGE(100,o_orderkey) */ * from filtered_order where ranked <= 2

                  - name: order_cust
                    sql: select * from latest_order left join repart_customer_nation_region on o_custkey = c_custkey

                  - name: repart_order_cust
                    sql: select /*+ REPARTITION(100,o_orderkey) */ * from order_cust

                  - name: line_repart
                    sql: select * from lineitem

                  - name: order_cust_line
                    sql: select * from repart_order_cust right join line_repart on o_orderkey = l_orderkey

                  - name: repart_order_cust_line
                    sql: select /*+ REPARTITION(100,l_suppkey,l_partkey)*/ * from order_cust_line

                  - name: last_5_tans_each_cust
                    sql: select * from repart_order_cust_line left join partsupp_supp_part on s_suppkey = l_suppkey and p_partkey = l_partkey

          sparkConf:
            - spark.sql.adaptive.autoBroadcastJoinThreshold: 10m
            - spark.sql.shuffle.partitions: 50
            - spark.sql.optimizer.dynamicPartitionPruning.enabled: true
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.default.parallelism: 45
            - spark.sql.broadcastTimeout: 15

```
</details>


