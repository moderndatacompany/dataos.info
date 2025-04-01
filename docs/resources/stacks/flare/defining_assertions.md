# Performing Business Validation Checks
DataOS allows you to define your own assertions with a combination of tests to check the rules. These tests are boolean expressions containing metric functions for aggregated data, such as the average sales price does not exceed some limit. DataOS automatically creates the metrics as per the function used while defining the assertions. You can also define assertions using SQL and regular expressions for more advanced use cases.

## **Defining Assertions**

The quality job YAML contains an assertions section to define tests for data quality validation. Each assertion specifies a set of criteria and tests to evaluate specific data attributes. 

Broadly, there are three ways to apply checks to a column:

1. **Using built-in functions that directly operate on a column's values**, such as average, minimum, maximum, and more.
    <br>**column:** It specifies the data column being examined and on which on which rule is to be defined
    <br>**filter:** It specifies the condition to narrow down the data.
    <br>**tests:** This section contains a series of tests that the data must pass, For example, if the average 'order_amount' is greater than 1000.00. You can use other aggregate functions as well.
    - avg > 1000.00
    - max < 1000: This test verifies that the maximum 'order_amount' is less than 1000.
        
    <aside class="callout">
        🗣 To get the list of various quality metrics functions that can be used in defining boolean expressions for the tests, refer to [**`tests`**](/resources/stacks/flare/assertion_configuration/#quality-metrics-functions).
        
    </aside>
        
2. **Employing built-in functions that work on the results of** **regular expressions** applied to a column's values, like checking for invalid percentages or counts.
    <br>**column:** It specifies the data column being examined and on which on which rule is to be defined
    <br>**validFormat:** This section has one attribute:
    <br>**regex:** It defines a regular expression ('regex'), which the column values should conform to.
    <br>**tests:** It contains tests that the data must pass.
    - invalid_count < 5
    - invalid_percentage < 0.1
    - regex_match > 10
3. **Creating custom quality rules using SQL-based assertions when you have complex testing criteria** that need custom logic and computed columns for evaluation. You can use SQL expressions to define your assertions.
    <br>**sql:** This attribute contains a SQL query that calculates the values to be compared.
    For example:
    ``` 
            SELECT
              AVG(order_amount) AS avg_order_amount,
              MAX(order_amount) AS max_order_amount
              FROM source
              WHERE brand_name = 'Awkward Styles'
    ```
        
    <br>**tests:**  This section lists tests based on the SQL query results. For example,
        - avg_order_amount > 1000: It checks if the calculated average 'order_amount' is greater than 1000.
        - max_order_amount < 1000: This test ensures that the calculated maximum 'order_amount' is less than 1000.

### **Example of Assertion YAML**

In the snippet below, you'll find examples of all the available assertions.

```yaml
assertions:
	- column: <name>
	  filter: <expression>
		tests:
		    - avg > 100
	      - max < 1000
	      - max > 100
	      - sum > 10000
	      - distinct_count > 10
	      - missing_count < 100
	      - missing_percentage < 0.5
	      - kurtosis > 1.0
	      - variance > 2.0
	      - skewness > 1.5
	      - stddev > 2.5
	      - null_percentage > 1
	      - null_count == 0
	      - avg_length < 10
				- min_length < 10
				- max_length < 10
	      - duplicate_count < 0
	- column: <name>
	  validFormat:
	    regex: <regex>
	  tests:
	    - invalid_count < 5
	    - invalid_percentage < 0.1
	    - regex_match > 10
	      
	 - sql: |
       SELECT
        AVG(price) AS avg_price,
        MAX(price) AS max_price,
        SUM(price) AS sum_price
      FROM finalDf
      WHERE city = 'RIO LINDA'
      tests:
        - avg_price > 100
        - max_price < 1000
        - sum_price > 100000
```
<aside class="callout">
🗣 While you can apply multiple checks to a column, it's important to note that you cannot simultaneously apply assertions from more than one of the mentioned categories.

</aside>

### **Structure of the Assertions Section**

```yaml
assertions: 
  - column: order_amount 
    filter: {{filter condition}} # Example: brand_name == 'Urbane' 
    tests: 
      - {{boolean expression with aggregate functions}}
  - column: 
    validFormat: 
      regex: <regex>
	  tests:
	    - {{boolean expression with in-built functions}}
  - sql: | 
      {{SQL statement}} 
    tests: 
      - {{boolean expressions with computed values}}
```

### **Attributes of Assertions Section**

The below table summarizes various properties within an assertions section in Quality job YAML.

| Attribute | Data Type | Requirement |
| --- | --- | --- |
| [`assertions`](/resources/stacks/flare/assertion_configuration/#assertions) | mapping | Mandatory |
| [`column`](/resources/stacks/flare/assertion_configuration/#column)| string | Mandatory |
| [`filter`](/resources/stacks/flare/assertion_configuration/#filter) | string | Optional |
| [`sql`](/resources/stacks/flare/assertion_configuration/#sql) | string | Optional |
| [`validFormat`](/resources/stacks/flare/assertion_configuration/#validformat) | mapping | Optional |
| [`regex`](/resources/stacks/flare/assertion_configuration/#regex) | string | Optional |
| [`tests`](/resources/stacks/flare/assertion_configuration/#tests) | boolean  | Mandatory |

To learn more about these attributes, their possible values, example usage, refer to [Assertions: Configuration Fields](assertion_configuration/).


## Different Ways to Define Assertions

Assertions can be classified into two categories, namely, sinked or standalone assertions and pre-sink assertions.

### **Standalone Assertions**

In Flare Workflow, assertions on pre-existing datasets can be specified by declaring `assertions` section distinct from the `inputs` section in the YAML definition.<br>
**Syntax for Standalone Assertions**

```yaml
workflow:
  title: {{workflow_title}}
  dag:
    - name: {{job-name}}
      title: {{job-title}}
      description: {{job-description}}
      spec:
        stack: flare:5.0
        compute: runnable-default
        tags:
          - {{tag1}}
        stackSpec:
          job:
            #validate single input
            inputs:
              - name: {{input-dataset-name}}
                dataset: {{input dataset udl address}}
                format: {{format}}
            assertions:
              - column: {{column-name}}
                tests:
                  - {{boolean expression}}
              - sql: |
                  {{SQL statement}}
                tests:
                  - {{boolean expression}}
```

<details><summary>Example YAML for Standalone Assertions</summary>
    
    The following YAML of the Flare Workflow demonstrates the definition of stand alone assertions. 
    
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
          description: The job performs metrics calculations and checks on order-enriched data
          spec:
            stack: flare:5.0
            compute: runnable-default
            tags:
              - Metrics
            title: Metrics and checks
            description: The job performs quality checks on order-enriched data
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
                    dataset: dataos://icebase:retail/orders_enriched
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
</details>



### **Pre-Sink Assertions**

Starting from Flare version 4.0, users can integrate assertions directly into their data transformation processes within the `outputs` section. Flare offers the capability to perform pre-sink checks or assertions on datasets enabling users to perform row-level checks before writing them to the destination. In this process, it initially verifies the assertion, and only if all the checks pass successfully, the data will be ingested.

This empowers users to validate their data to avoid writing erroneous data to the target and also eliminates the requirement for standalone data quality jobs.<br> <br>
**Syntax for Pre-sink Assertions**

```yaml
workflow:
  dag:
    - name: {{job-name}}
      title: {{job-title}}
      description: {{job description}}
      spec:
        tags:
          - {{tag1}}
        stack: flare:5.0
        compute: runnable-default
        stackSpec:
          job:
            inputs:
              - name: {{input-dataset-name}}
                dataset: {{input dataset udl address}}
                format: {{format}}
            steps:
              sequence:
            ...
            ...
            outputs:
              - name: {{output-dataset-name}}
                dataset: {{output dataset udl address}}
                format: {{output format}}
              assertions:
                - column: {{column name}}
                  tests:
                    - {{boolean expression}}
                - sql: |
                  {{SQL statement}}
                  tests:
                  - {{boolean expression}}
     ...
     ...
     ...

```

<details><summary>Example YAML for Pre-Sink Assertions</summary>
    
    To utilize this functionality, pre-assertions can be established as shown in the following YAML syntax:
    
    ```yaml
    version: v1
    name: sanity-write-azure
    type: workflow
    tags:
      - Sanity
      - quality
    title: Quality assertions
    description: This job is to validate data before writing to the destination
    workflow:
      dag:
        - name: sanity-write-az-job
          title: Quality check for data before ingestion
          description: quality job.
          spec:
            tags:
              - Sanity
              - Azure
            stack: flare:5.0
            compute: runnable-default
            stackSpec:
              job:
                explain: true
                logLevel: INFO
                showPreviewLines: 2
                inputs:
                  - name: sanity_city_input
                    dataset: dataos://thirdparty01:none/city
                    format: csv
                    schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
    
                steps:
                  - sequence:
                      - name: cities
                        doc: Pick all columns from cities and add version as yyyyMMddHHmm formatted
                          timestamp.
                        sql: |
                          SELECT
                            *,
                            date_format (now(), 'yyyyMMddHHmm') AS version,
                            now() AS ts_city
                          FROM
                            sanity_city_input
    
                outputs:
                  - name: cities
                    dataset: dataos://sanityazurealok01:retail/city_csv?acl=rw
                    format: csv
                    options:
                      saveMode: overwrite
                      partitionBy:
                        - version
                    tags:
                      - Sanity
                      - Azure
                      - CSV
                    title: Azure csv sanity
                    description: Azure csv sanity
    
                  - name: cities
                    dataset: dataos://sanityazurealok01:retail/city_json?acl=rw
                    format: json
                    options:
                      saveMode: overwrite
                      partitionBy:
                        - version
                    tags:
                      - Sanity
                      - Azure
                      - JSON
                    title: Azure json sanity
                    description: Azure json sanity
                    
                  - name: cities
                    dataset: dataos://sanityazurealok01:retail/city_parquet?acl=rw
                    format: parquet
                    options:
                      saveMode: overwrite
                      partitionBy:
                        - version
                    tags:
                      - Sanity
                      - Azure
                      - Parquet
                    title: Azure parquet sanity
                    description: Azure parquet sanity
                    assertions:
                      - column: zip_code
                        tests:
                          - avg < 100
                          - max < 1000
                          - max > 100
                          - distinct_count > 10
                          - missing_count < 100
                          - missing_percentage < 0.5
    
                      - column: zip_code
                        filter: state_code == 'AL'
                        tests:
                          - avg > 500
    
                      - column: city_name
                        validFormat:
                          regex: Prattville
                        tests:
                          - invalid_count < 5
                          - invalid_percentage < 0.1
    
                      - sql: |
                          SELECT
                            AVG(zip_code) AS avg_zip_code,
                            MAX(zip_code) AS max_zip_code
                          FROM products
                          WHERE state_code == 'AL'
                        tests:
                          - avg_zip_code > 3600
                          - max_zip_code < 36006
    ```

</details>

### **Alert Mechanism for Handling Assertion Failures**
When assertions fail, it results in the failure of the entire workflow, preventing data ingestion. DataOS features an alert system designed for this scenario. DataOS enables you to set up [**Workflow Alerts**](/dataos_alerts/#workflow-alerts), to notify stakeholders in case of workflow or job failures, significantly improving the Developer Experience (DevX). Each alert provides comprehensive information about workflow and job runs, including access to logs. This streamlined process greatly assists in the prompt identification and resolution of issues.

### **Case Scenario**

To understand how assertions are used in different scenarios, refer to [Enhancing Data Integrity with Assertion Jobs](/resources/stacks/flare/assertions_case_scenario/).