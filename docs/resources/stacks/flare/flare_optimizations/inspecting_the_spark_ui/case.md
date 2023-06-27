# Case Scenario: Optimizing using Spark UI


```yaml
---
version: v1beta1
name: wf-orders-enriched-01
type: workflow
tags:
  - customers
  - orders
description: Jobs ingest orders enriched data from snowflake
workflow:
  title: Read Snowflake regions
  dag:
    - name: orders-enriched-job-08
      title: Order Supplier And Customer Enriched Data
      description: This job writes snowflake data to dataos
      spec:
        tags:
          - customers
          - orders
        stack: flare:3.0
        compute: runnable-default
        envs:
          HERA_SSL: "false"
          HERA_BASE_URL: "https://fit-garfish.dataos.app/hera"
        tier: connect
        flare:
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
                dataset: dataos://snowflake02:TPCH_SF10/REGION

              - name: customer
                dataset: dataos://snowflake02:TPCH_SF10/CUSTOMER

              - name: lineitem
                dataset: dataos://snowflake02:TPCH_SF10/LINEITEM
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  l_commitdate between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-31'
                    - name: end_time
                      sql: select '1998-08-29'

              - name: nation
                dataset: dataos://snowflake02:TPCH_SF10/NATION

              - name: orders
                dataset: dataos://snowflake02:TPCH_SF10/ORDERS
                incremental:
                  context: incrinputs
                  sql: select * from incrinputs where  O_ORDERDATE between '$|start_time|' AND '$|end_time|'
                  keys:
                    - name: start_time
                      sql: select '1998-07-01'
                    - name: end_time
                      sql: select '1998-07-30'

              - name: part
                dataset: dataos://snowflake02:TPCH_SF10/PART

              - name: partsupp
                dataset: dataos://snowflake02:TPCH_SF10/PARTSUPP

              - name: suppliers
                dataset: dataos://snowflake02:TPCH_SF10/SUPPLIER

            logLevel: INFO
            outputs:
              - name: region_output
                depot: dataos://icebase:sample?acl=rw
            steps:
              - sink:
                  - sequenceName: last_5_tans_each_cust
                    datasetName: customer_trans_latest_five_03
                    outputName: region_output
                    outputType: Iceberg
                    outputOptions:
                      saveMode: overwrite
                      sort:
                        mode: partition
                        columns:
                          - name: O_ORDERDATE
                            order: desc
                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip
                      partitionSpec:
                        - type: month
                          column: O_ORDERDATE
                          name: month
                        - type: identity
                          column: user_agent

                sequence:
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

    - name: dt-orders-last-8
      spec:
        stack: toolbox
        toolbox:
          dataset: dataos://icebase:sample/customer_trans_latest_five_03?acl=rw
          action:
            name: set_version
            value: latest
      dependencies:
        - orders-enriched-job-08
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

## Method: 3

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

				Spark Configuration: Default
```

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

### Total Duration: 6.11

```yaml
	 RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-11T22:46:25+05:30 | 2022-08-11T22:52:36+05:30
```

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

### Total Duration: 6.38

```yaml
   RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-11T22:58:41+05:30 | 2022-08-11T23:04:39+05:30
```

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

### Total Duration: 6

```yaml
   RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-11T23:07:17+05:30 | 2022-08-11T23:13:17+05:30
```

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

### Total  Duration: 6.33

```yaml
   RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 8/8      | 2022-08-11T23:51:59+05:30 | 2022-08-11T23:57:52+05:30
```