# Writing Data Profiling Jobs using Flare
Data Profiling Jobs evaluate dataset validity, structure, accuracy, and completeness. They offer insights into your data, highlighting patterns, inconsistencies, anomalies, and redundancies. These jobs use basic statistics to validate data and provide comprehensive overviews, including data distribution, types, missing values, and outliers.

Data profiling can be done on the entire dataset or on the sample /filtered data. You can filter the data by applying appropriate rules. Data profiling is quite computationally intensive in terms of resources, so it is recommended to run it for sample data in a dataset.

## Structure of the Profile Section
The following code snippet illustrates a Workflow that defines a Flare Job and properties, required to perform data profiling.
```yaml
...
...
workflow:
  title: {{workflow title}}
  dag:
  - name: {{job name}}
    title: {{job title}}
    description: {{Job description}}
    spec:
      envs:
        DISABLE_RAW_FILE_SYSTEM_PERMISSION_SET: "true"
      tags:
      - {{tags}}
      stack: flare:5.0
      compute: runnable-default

      persistentVolume: # Define Persistent Volume
        name: persistent-v
        directory: fides 
      stackSpec:
        job:
          inputs:
            - name: profile_city
              dataset: dataos://icebase:retail/city # Dataset Name
              format: iceberg

          profile:
            level: basic
            filters:
              - type: expression
                expression: "state_code='TX'" # Filter Expression

```
### **Properties**
The following properties need to be defined specifically for the profiling job.

1. **Persistent Volume:** This is mandatory to define the volume to store intermediate files generated in the process of profiling. The directory given here is predefined.
    
    ```yaml
    persistentVolume:
      name: persistent-v
      directory: fides
    ```
    
2. **Filters:** You may define the filter criterion to reduce the data on which you want to perform profiling. If removed, profiling will be performed on the entire dataset. The filter criterion is like a `where` clause of your SQL query.
    
    ```yaml
    profile:
      level: basic
      filters:
        - type: expression
          expression: "gender='MALE'"
    ```
    
3. **Input:** Dataset, on which we are performing profiling should be first in the input list.
    
    ```yaml
    inputs:
      - name: profile_input_df
        dataset: dataos://set01:default/orders_enriched_01?acl=r
        format: hudi
    ```
    

<aside class="callout">
🗣 Each profile job can be associated with only one dataset.

</aside>

## Example YAML

The provided YAML below demonstrates how profiling can be done.

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
      stack: flare:5.0
      compute: runnable-default
      title: City Profile

      persistentVolume: # Define Persistent Volume
        name: persistent-v
        directory: fides 
      stackSpec:
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
            level: basic
            filters:
              - type: expression
                expression: "state_code='TX'" # Filter Expression

        sparkConf:
        - spark.sql.shuffle.partitions: 10
        - spark.default.parallelism: 10
```