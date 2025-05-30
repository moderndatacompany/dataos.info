---
search:
  exclude: true
---

# Data quality jobs (assertions)

Data quality jobs are designed to ensure that data meets specified quality standards by applying various assertions. Assertions are checks that validate data against predefined rules, such as value ranges, missing values, uniqueness, and other conditions. These jobs are essential for monitoring and maintaining data integrity throughout your workflows.

## Case Scenario

In this scenario, we define assertions to evaluate the quality of data. To learn more about Data Quality Jobs, click [here](/resources/stacks/flare/#data-quality-job)

## Different ways to define assertions

Assertions can be classified into two categories, namely, sinked or standalone assertions and pre-sink assertions. 

### **Standalone assertions**

In Flare Workflow, assertions on pre-existing datasets can be specified by declaring  `assertions` section distinct from the `inputs` section in the YAML definition. The following YAML of the Flare Workflow.

#### **Code snippets**

**Flare Workflow**

```yaml
version: v1 # Version
name: mtrx-chks-odr-enr-01 # Name of the Workflow
type: workflow
tags:
  - Metrics
  - Checks
description: The job performs metrics calculations and checks on order enriched data
workflow:
  title: Metrics and checks
  dag:
    - name: metrics-chks-order-enrich
      title: Metrics and checks
      description: The job performs metrics calculations and checks on order enriched data
      spec:
        stack: flare:5.0
        compute: runnable-default
        tags:
          - Metrics
        title: Metrics and checks
        description: The job performs metrics calculations and checks on order enriched data
        stackSpec:
          driver:
            coreLimit: 3000m
            cores: 2
            memory: 4000m
          executor:
            coreLimit: 6000m
            cores: 2
            instances: 1
            memory: 10000m
          job:
            explain: true
            logLevel: INFO
            #validate single input
            inputs:
              - name: source
                dataset: dataos://lakehouse:retail/orders_enriched
                format: iceberg
            #override outputs, steps with specific template
            assertions:
              - column: order_amount
                tests:
                  - avg > 1000.00
                  - max < 1000
                  - max > 1000
                  - distinct_count > 100
                  - missing_count < 100
                  - missing_percentage < 0.5

              - column: order_amount
                filter: brand_name == 'Urbane'
                tests:
                  - avg > 500
                  - distinct_count > 100
                  - missing_count < 100

              - column: brand_name
                validFormat:
                  regex: Awkward
                tests:
                  - invalid_count < 5
                  - invalid_percentage < 0.1

              - sql: |
                  SELECT
                    AVG(order_amount) AS avg_order_amount,
                    MAX(order_amount) AS max_order_amount
                  FROM source
                   where brand_name = 'Awkward Styles'
                tests:
                  - avg_order_amount > 1000
                  - max_order_amount < 1000

          sparkConf:
            - spark.serializer: org.apache.spark.serializer.KryoSerializer
            - spark.sql.shuffle.partitions: "10"
            - spark.memory.storageFraction: "0.1"
            - spark.memory.fraction: "0.1"
            - spark.shuffle.memoryFraction: "0.2"
```


### **Pre-Sink Assertions**

Starting from Flare version 4.0, users have the capability to integrate assertions directly into their data transformation processes within the `outputs` section, eliminating the requirement for standalone data quality jobs. This introduces pre-sink checks for datasets generated by Flare, enabling users to perform row-level checks on columns within the `outputs` section to avoid writing erroneous data to the target. 

#### **Code Snippet**

To utilize this functionality, pre-assertions can be established using the following YAML syntax:

```yaml
version: v1 # Version
name: pre-sink-assertion-workflow # Name of the Workflow
type: workflow # Resource Type (Here its workflow)
tags: # Tags
  - Assertion
title: Pre-Sink Assertions # Title of the workflow
description: |
  The purpose of this workflow is to define pre-sink assertions.
workflow: # Workflow Section
  dag: # Directed Acyclic Graph (DAG)
    - name: pre-sink-assertion-job # Name of the Job
      title: Pre-Sink Job # Title of the Job
      description: |
        The purpose of this job is to define pre-sink assertions.
      spec: # Specs
        tags: # Tags
          - Assertions
          - Quality
        stack: flare:6.0 # Flare Stack Version (Here its 4.0)
        compute: runnable-default # Compute
        stackSpec: # Flare Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            showPreviewLines: 2 
            inputs: # Inputs Section
              - name: sanity_city_input # Name of the Input Dataset
                dataset: dataos://thirdparty01:none/city # Input Dataset UDL
                format: csv # Input Dataset Format 
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc # Schema Path

            steps: # Steps Section
              - sequence: # Sequence
                  - name: cities # Transformation Step Name
                    doc: Pick all columns from cities and add version as yyyyMMddHHmm formatted timestamp. # Documentation
                    sql: |
                      SELECT
                        *,
                        date_format (now(), 'yyyyMMddHHmm') AS version,
                        now() AS ts_city
                      FROM
                        sanity_city_input

            outputs: # Outputs Section
              - name: cities # Output Dataset Name
                dataset: dataos://sanityazurealok01:retail/city_csv?acl=rw # Output Dataset UDL
                format: csv # Output Dataset Format 
                options: # Options
                  saveMode: overwrite
                  partitionBy:
                    - version
                tags: # Tags
                  - CSV
                title: Azure csv # Title
                description: Azure csv # Description
              - name: cities # Name of Output Dataset
                dataset: dataos://sanityazurealok01:retail/city_json?acl=rw # Output Datset UDL
                format: json # Format
                options: # Options
                  saveMode: overwrite
                  partitionBy:
                    - version
                tags: # Tags
                  - JSON
                title: Azure json # Title
                description: Azure json # Description
              - name: cities # Output Dataset Name
                dataset: dataos://sanityazurealok01:retail/city_parquet?acl=rw # Output Dataset UDL
                format: parquet # Output Datset Format
                options: # Options
                  saveMode: overwrite
                  partitionBy:
                    - version
                tags: # Tags
                  - Parquet
                title: Azure parquet
                description: Azure parquet
# Pre-sink Assertions
                assertions: # Assertions Section
                  - column: zip_code # Column Name
                    tests: # Tests
                      - avg < 100
                      - max < 1000
                      - max > 100
                      - distinct_count > 10
                      - missing_count < 100
                      - missing_percentage < 0.5
                  - column: zip_code # Column Name
                    filter: state_code == 'AL' # Filter Condition
                    tests: # Tests
                      - avg > 500
                  - column: city_name # Column Name
                    validFormat: 
                      regex: Prattville
                    tests: # Tests
                      - invalid_count < 5
                      - invalid_percentage < 0.1
                  - sql: |
                      SELECT
                        AVG(zip_code) AS avg_zip_code,
                        MAX(zip_code) AS max_zip_code
                      FROM products
                      WHERE state_code == 'AL'
                    tests: # Tests
                      - avg_zip_code > 3600
                      - max_zip_code < 36006
```