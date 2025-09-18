# Merge Into Query

Merge Into functionality is used when you need to update values in the existing table using flare for a certain condition.

MERGE INTO allows you to perform an upsert operation (update or insert) between a target table and a source table. The operation works as follows:

  - **Update**: If the condition matches an existing row in the target table, the record is updated.

  - **Insert**: If the condition does not match, a new row is inserted into the target table.
  - 
It updates the target table using a source table using a set of conditions and updates records. This is a row-specific update where the row is found based on the **ON** clause.


## Case Scenario

Let’s say we have written a dataset of a city (i.e., `city_merge`) and it has all the information about the city and now the city data has changed.

In the city data (Source table) information about `zip_code = 36006` has changed.

| Column Name | Old Value | New Value |
| --- | --- | --- |
| city_name | Billingsley | abc |
| country_name | Autauga | abcd |
| state_code | AL | ab |
| state_name | Alabama | abcde |

> Now we want to update this on zip_code (i.e. 36006) records only.
> 

### **Existing city table.**

![Screen Shot 2022-06-02 at 1.08.49 AM.png](/resources/stacks/flare/case_scenario/merge_into_functionality/screen_shot_2022-06-02_at_1.08.49_am.png)

### **City table with updated records (Using merge into the function)**

![Screen Shot 2022-06-02 at 1.21.52 AM.png](/resources/stacks/flare/case_scenario/merge_into_functionality/screen_shot_2022-06-02_at_1.21.52_am.png)

## How to define merge in Flare.

**Syntax** 

```yaml
outputOptions:
  saveMode: overwrite
  iceberg:
    merge:
      onClause: "old.old_table_column_a = new.new_table_column_a"
      whenClause: "MATCHED THEN UPDATE SET old.old_table_column_b = new.old_table_column_b"
```

**`onClause`**: We can use multiple clauses for ON (the clauses should be separated using `AND` operator) We can’t use `OR` for multiple clauses.

**`whenClause`:**  This will be executed when `onClause` condition matches and **`whenClause`** conditions can be referred.

**`old`:** Refers to the existing dataset in Lakehouse.

**`new`:** Refers to the data frame by you are updating existing dataset.

!!! info
    Merge Into requires below sparkConf and this is mandatory for merge into function to work.

    ```yaml
    sparkConf:  # spark configuration 
        - spark.sql.extensions: org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions  # mandatory for merge into
    ```



<!-- 
> Merge option needs to be defined in **sink** for the dataset you are updating.
>  -->


!!! info
    
    Below flare `sequence` is only to create updated sample data (which will have new `city_name`, `country_name`, `state_code` and `state_name`) for `zip_code = 36006`.


```yaml
# **Update set using multiple column** 
- sequence:     # data transformation steps using Spark SQL 
    - name: main 
      sql: select * from input where zip_code = "36006"   # Selecting only zip code (36006) 
    - name: new_city  # Updating table value for zip code (36006)  
      sql: select  city_id, zip_code, 'abc' as city_name, 'abcd' as county_name, 'ab' as state_code , 'abcde' as state_name from main
```

```yaml
# **Update set using single column** 
merge:
  onClause: "old.city_id = new.city_id"
  whenClause: "MATCHED THEN UPDATE SET old.state_name = new.state_name"
```

## Flare workflow for merge into functionality



```yaml
version: v1
name: iceberg-merge-job-011 #workflow name
type: workflow
tags:
  - Connect
  - merge
  - iceberg
description: Merges city data into Iceberg table based on zip_code
workflow:
  title: Merge City Data into Iceberg
  dag:
    - name: merge-iceberg-city
      title: Merging city dataset
      description: Performs a MERGE INTO operation on Iceberg table using zip_code
      spec:
        tags:
          - merge
          - iceberg
        stack: flare:7.0
        compute: runnable-default
        envs:
          DISABLE_HADOOP_PATH_CHECKS: "true"
        stackSpec:
          job:
            explain: true
            logLevel: INFO
            inputs:
              - name: input01
                dataset: dataos://lakehouse:retail/city
                format: iceberg
                # schemaPath: dataos://lakehouse:default/schemas/city.avsc
                options:
                  saveMode: append
            outputs:
              - name: city_merge_output
                dataset: dataos://lakehouse:syndicate/city_merge
                format: iceberg
                options:
                  saveMode: overwrite
                  merge:
                    onClause: "old.zip_code = new.zip_code"
                    whenClause: >
                      MATCHED THEN UPDATE SET
                      old.city_name = new.city_name,
                      old.county_name = new.county_name,
                      old.state_code = new.state_code,
                      old.state_name = new.state_name
                  properties:
                    write.format.default: parquet
                    write.metadata.compression-codec: gzip
            steps:
              - sequence:
                  - name: city_source 
                    sql: select * from input01 where zip_code = "36006"   # Selecting only zip code (36006) 
                  - name: city_merge_output  # Updating table value for zip code (36006)  
                    sql: select city_id, zip_code, 'abc' as city_name, 'abcd' as county_name, 'ab' as state_code , 'abcde' as state_name from city_source 
      

```

!!! tip

    If you are using Flare 5.0 we recommend to use sparkConf in the flare manifest file.
    
    ??? note

        ```yaml
          version: v1
          name: iceberg-merge-job-011 #workflow name
          type: workflow
          tags:
            - Connect
            - merge
            - iceberg
          description: Merges city data into Iceberg table based on zip_code
          workflow:
            title: Merge City Data into Iceberg
            dag:
              - name: merge-iceberg-city
                title: Merging city dataset
                description: Performs a MERGE INTO operation on Iceberg table using zip_code
                spec:
                  tags:
                    - merge
                    - iceberg
                  stack: flare:5.0
                  compute: runnable-default
                  envs:
                    DISABLE_HADOOP_PATH_CHECKS: "true"
                  stackSpec:
                    job:
                      explain: true
                      logLevel: INFO
                      inputs:
                        - name: input01
                          dataset: dataos://lakehouse:retail/city
                          format: iceberg
                          # schemaPath: dataos://lakehouse:default/schemas/city.avsc
                          options:
                            saveMode: append
                      outputs:
                        - name: city_merge_output
                          dataset: dataos://lakehouse:syndicate/city_merge
                          format: iceberg
                          options:
                            saveMode: overwrite
                            merge:
                              onClause: "old.zip_code = new.zip_code"
                              whenClause: >
                                MATCHED THEN UPDATE SET
                                old.city_name = new.city_name,
                                old.county_name = new.county_name,
                                old.state_code = new.state_code,
                                old.state_name = new.state_name
                            properties:
                              write.format.default: parquet
                              write.metadata.compression-codec: gzip
                      steps:
                        - sequence:
                            - name: city_source 
                              sql: select * from input01 where zip_code = "36006"   # Selecting only zip code (36006) 
                            - name: city_merge_output  # Updating table value for zip code (36006)  
                              sql: select city_id, zip_code, 'abc' as city_name, 'abcd' as county_name, 'ab' as state_code , 'abcde' as state_name from city_source 
                
                    
                      sparkConf:  # spark configuration 
                        - spark.sql.extensions: org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions  # mandatory for merge into function to work  
        ```




