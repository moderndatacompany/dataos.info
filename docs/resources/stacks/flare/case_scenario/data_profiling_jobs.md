# Data profiling jobs

Data profiling jobs in DataOS are designed to analyze and summarize the characteristics of datasets. These jobs provide insights into the data distribution, completeness, uniqueness, and other key metrics. Profiling is crucial for understanding the structure and quality of the data before any transformation or processing steps are applied. The profiling results help teams make informed decisions on how to handle the data in subsequent workflows.

## Case scenario

In this case scenario, we perform data profiling on an entire dataset and filter it according to some appropriate rules. To learn more about Data Profiling, click [here](/resources/stacks/flare/#data-profiling-job).

## Key properties for profile job

Data profiling can be done on the entire dataset or on the sample /filtered data. You can filter the data by applying appropriate rules. Data profiling is quite computationally intensive in terms of resources, so it is recommended to run it for sample data in a dataset.

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

3. **Input:** Dataset, on which we are performing profiling should be first in the input list.

    ```yaml
    inputs:
      - name: profile_input_df
        dataset: dataos://set01:default/orders_enriched_01?acl=r
        format: hudi
    ```

> **Note**: One profile job can have only one dataset.
> 

## Code snippets

Below is a sample YAML to showcase how profiling can be done.

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
      stack: flare:6.0
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
            # basic | intermediate | advanced
            level: basic
            filters:
              - type: expression
                expression: "state_code='TX'" # Filter Expression

        sparkConf:
        - spark.sql.shuffle.partitions: 10
        - spark.default.parallelism: 10 
```

Once the profiling has been applied, you can view the results by following the below steps:

- Open the DataOS home page in your browser and  select Metis.
- In the Metis, navigate to the Assets section.
- On the left sidebar, filter the displayed assets by selecting the Icebase database.
- The list of tables within the Icebase database will be displayed.
- From the list of tables, choose the City table to view the profiling details.
- Navigate to the Profile tab of the city table to see the detailed profiling.

Here,the Table Profile allows you to monitor the overall structure of a dataset, including its row count. It provides a snapshot of the data's organization, helping users understand the size and completeness of their dataset. For example, the City table has 3,298 rows. The Column Profile provides detailed statistics on each column within a table. Key metrics include:

- **Null %:** Percentage of null values in the column.
- **Unique %:** Percentage of unique values.
- **Distinct %:** Percentage of distinct values.
- **Value count:**Total number of values in the column.
It also tracks the data type and the status of each column. For example, the city_id column has 100% unique values and 3,298 total values, while the county_name column has only 8% distinct values.

Further, When you click on the particular column say `zip_code`, detailed profiling information and graph is displayed, providing a deeper understanding of its structure and statistics. The following details are available:

**Column summary:**

- **Approx Distinct count:** Displays the number of unique values in the column (e.g., 2,473 distinct zip codes), indicating the diversity of values.
- **Null count:** Shows the total number of missing values in the column (e.g., 0, meaning no missing values).
- **Unique count:** Reflects the number of truly unique values, though in most cases this is included in the distinct count.
- **Values count:** Total number of entries or rows in the column (e.g., 3,298).

**Proportions:**

- **Distinct proportion:** The percentage of distinct values relative to the total (e.g., 75%).
- **Null proportion:** The percentage of null values (e.g., 0% if there are no missing values).
- **Unique proportion:** The percentage of unique values compared to the total (e.g., 53%).

**Statistical measures:**

- **Median:** The middle value of the column, providing a sense of central tendency.
- **Max:** The highest value in the column (e.g., 79,997).
- **Min:** The lowest value in the column (e.g., 73,301).
- **Mean:** The average of the column values (e.g., 77,363.35).
- **Standard Deviation:** A measure of the spread of values (e.g., 1,417.14), showing how much values deviate from the mean.
- **Variance:** Indicates how much the values spread from the mean (e.g., 2,008,278.54).
- **Coefficient of Variation:** A relative measure of variability (e.g., 1.83), indicating how spread out the values are in relation to the mean.

**Quartile information:**

- **First Quartile (Q1):** The 25th percentile value (e.g., 76,092).
- **Inter Quartile Range (IQR):**The range between the first and third quartiles, showing the spread of the middle 50% of the data (e.g., 2,500).
- **Third Quartile (Q3):** The 75th percentile value (e.g., 78,592).