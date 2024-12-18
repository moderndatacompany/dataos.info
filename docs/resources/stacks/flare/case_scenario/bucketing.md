# Bucketing


Bucketing is an optimization technique that helps to prevent the shuffling and sorting of data during compute-heavy operations such as joins. Based on the bucketing columns we specify, data is collected in a number of bins.

![diagram 01.jpg](/resources/stacks/flare/case_scenario/bucketing/diagram_01.jpg)

## Bucketing vs Partitioning

Bucketing is similar to partitioning, but in the case of partitioning, we create directories for each partition. In bucketing, we create equal-sized buckets, and data is distributed across these buckets by a hash on the value of the bucket.

## When to use bucketing?

Bucketing is helpful in the following scenarios:

- When joins are performed between dimension tables that contain primary keys for joining.
- When join operations are being performed between small and large tables.
- Where the data is heavily skewed, or for executing faster joins on a cluster we can also use the bucketing technique to improve performance.

## Configurations

```yaml
partitionSpec:
	- type: bucket # select type bucket
		column: week_year_column # bucketing column
		numBuckets: 2 # number of buckets
```

## Code Snippets

### **Simple Bucketing**

**Flare Workflow**

```yaml
version: v1
name: wf-sample
type: workflow
workflow:
  dag:
    - name: sample
      spec:
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:    
            coreLimit: 12000m
            cores: 2
            memory: 12000m
          executor:
            coreLimit: 12000m
            cores: 4
            instances: 3
            memory: 22000m        
          job:
            inputs:
              - name: input 
                dataset: dataos://thirdparty01:analytics/survey_unpivot/unpivot_data.csv
                format: csv
            logLevel: INFO
            outputs:
              - name: clustered_records
                dataset: dataos://icebase:sample/unpivot_data_02?acl=rw
                format: Iceberg
                description: unpivotdata
                options:
                  saveMode: overwrite
                  sort:
                    mode: global
                    columns:
                      - name: week_year_column
                        order: desc
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
										# Bucketing
                    partitionSpec:
                      - type: bucket # bucket
                        column: week_year_column # bucketing column
                        numBuckets: 2 # number of buckets
                title: unpivot data
            steps:
                - sequence:
                    - name: select_all_column
                      sql: Select * from input 
                      functions: 
                        - name: cleanse_column_names
                        - name: unpivot 
                          columns: 
                            - "*" 
                          pivotColumns:
                            - week_year
                          keyColumnName: week_year_column 
                          valueColumnName: values_columns
                    - name: clustered_records
                      sql: SELECT * FROM select_all_column CLUSTER BY week_year_column
          sparkConf:
            - spark.sql.extensions: org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

**Toolbox Workflow**

This additional workflow is only required if your current icebase depot is based on Hadoop catalogue and Hive metastore. However, in the case where the catalog is based on Hadoop and REST Metastore, the additional metadata setting operation is not required.

```yaml
version: v1
name: datatool-wf-sample
type: workflow
workflow:
  dag:
  - name: dataos-tool-simple-bucket
    spec:
      stack: toolbox
      compute: runnable-default
      stackSpec:
        dataset: dataos://icebase:sample/unpivot_data_02
        action:
          name: set_version
          value: latest
```

### **Big Data-Nested Bucket**

**Flare Workflow**

```yaml
version: v1
name: wf-sample-02
type: workflow
workflow:
  dag:
    - name: sample
      spec:
        stack: flare:5.0
        compute: runnable-default
        stackSpec:
          driver:    
            coreLimit: 2200m
            cores: 2
            memory: 2000m
          executor:
            coreLimit: 3300m
            cores: 3
            instances: 1
            memory: 6000m  
          job:
            inputs:
              - name: input 
                dataset: dataos://icebase:retail/city
                format: iceberg
            logLevel: INFO
            outputs:
              - name: random_data
                dataset: dataos://icebase:sample/bucket_large_data_02?acl=rw
                format: Iceberg
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                    partitionSpec:
                      - type: identity
                        column: category
                      - type: bucket # bucket
                        column: seg_id # bucketing column
                        numBuckets: 20 # number of buckets
                      - type: day
                        column: ts
                        name: day_partitioned
                title: unpivot data
            steps:
                - sequence:
                  - name: random_data
                    sql: |
                      SELECT
                        uuid,
                        seg_id,
                        ts,
                        CASE WHEN cat > 0.67 THEN
                          'A'
                        WHEN cat > 0.33 THEN
                          'B'
                        ELSE
                          'C'
                        END AS category
                      FROM (
                        SELECT
                          explode (rand_value) uuid,
                          cast(random() * 100 AS int) seg_id,
                          add_months (CURRENT_TIMESTAMP, cast(random() * 100 AS int)) ts,
                          random() AS cat
                        FROM (
                          SELECT
                            SEQUENCE (1,
                              10000000) AS rand_value))

          sparkConf:
            - spark.sql.extensions: org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

If one attempts to  set metadata on the icebase depot based on REST metastore the following error will encounter:

```bash
➜  ~ dataos-ctl dataset set-metadata -a dataos://icebase:retail/city -v latest
INFO[0000] 📂 set metadata...                            
ERRO[0001] 📂 set metadata...error                       
ERRO[0001] set metadata operation is restricted to Hadoop Catalog and HIVE Metastore based depot, for given depot: icebase, icebergCatalogType: HADOOP and metastoreType: REST
```