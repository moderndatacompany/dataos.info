# **Data Profiling Jobs**

# **Case Scenario**

In this case scenario, we perform data profiling on an entire dataset and filter it according to some appropriate rules. To know more about Data Profiling, refer to [Basic concepts of Flare Workflow](../Basic%20concepts%20of%20Flare%20Workflow.md).

# **Key Properties for Profile Job**

Data profiling can be done on the entire dataset or on the sample /filtered data. You can filter the data by applying appropriate rules. Data profiling is quite computationally intensive in terms of resources so it is recommended to run it for sample data in a dataset.

There are some **additional properties** that you need to define specifically for the profiling job.

1. **Persistent Volume:** This is mandatory to define the volume to store intermediate files generated in the process of profiling. The directory given here is predefined.

    ```yaml
    persistentVolume:
      name: persistent-v
      directory: fides
    ```

2. **Filters:** You may define the filter criterion to reduce the data on which you want to perform profiling. If removed, profiling will be performed on the entire dataset. The filter criterion is like a `where` clause of your SQL query.

    ```yaml
    profile:
      # basic | intermediate | advanced
      level: basic
      filters:
        - type: expression
          expression: "gender='MALE'"
    ```

3. **Input:** Dataset, on which we are performing profiling, should be first in the input list.

    ```yaml
    inputs:
      - name: profile_input_df
        dataset: dataos://set01:default/orders_enriched_01?acl=r
        format: hudi
    ```

> **Note**: One profile job can have only one dataset.

# **Code Snippets**

Below is a sample YAML to showcase how profiling can be done

```yaml
version: v1
name: profiler-raw-city-01
type: workflow
tags:
- Fides
- City
- has_profile
description: The job performs profiling on top of city data
workflow:
  title: City Profiler
  dag:
  - name: p-r-city-01
    title: Profiler Raw City
    description: The job performs profiling on city data
    spec:
      envs:
        DISABLE_RAW_FILE_SYSTEM_PERMISSION_SET: "true"
      tags:
      - Fides
      - City
      - has_profile
      stack: flare:3.0
      compute: runnable-default
      title: City Profile

      persistentVolume: # Define Persistent Volume
        name: persistent-v
        directory: fides 

      envs:
        DISABLE_RAW_FILE_SYSTEM_PERMISSION_SET: "true"
      flare:
        driver:
          coreLimit: 2400m
          cores: 2
          memory: 3072m
        executor:
          coreLimit: 2400m
          cores: 2
          instances: 1
          memory: 4096m
        job:
          explain: true
          logLevel: WARN

          inputs:
            - name: profile_city
              dataset: dataos://icebase:retail/city # Dataset Name
              format: iceberg

          profile:
            # basic | intermediate | advanced
            level: basic
            filters:
              - type: expression
                expression: "state_code='TX'" # Filter Expression

        sparkConf:
        - spark.sql.shuffle.partitions: 10
        - spark.default.parallelism: 10 
```