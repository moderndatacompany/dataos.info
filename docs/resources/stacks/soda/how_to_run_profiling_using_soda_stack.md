# Running Data Profiling with Soda Stack

Data profiling helps you understand the quality, structure, and completeness of your datasets.
Using **Soda Stack**, you can automate profiling jobs that scan datasets, run data quality checks, and generate profiling summaries — all as part of a workflow.

The following example demonstrates how to configure and run a profiling workflow using **Soda Stack** within a DataOS environment.


## Sample Workflow Manifest

```yaml
name: profile-soda
version: v1
type: workflow
tags:
  - profile
description: This job profiles datasets using Soda checks and profiling features.

workflow:
  dag:
    - name: sample-profile-soda-01
      title: Sample Data Profiling with Soda
      spec:
        stack: soda+python:1.0
        soda:
          - dataset: dataos://lakehouse:retail/customer
            checks:
              - row_count between 10 and 1000:
                  attributes:
                    category: Accuracy
                    title: Validate dataset size between 10 and 1000 records

              - missing_count(birth_date) = 0:
                  attributes:
                    category: Completeness
                    title: Ensure birth_date field is not missing

              # Example for validity check (commented)
              # - invalid_percent(phone) < 1%:
              #     valid format: phone number
              #     attributes:
              #       category: Validity
              #       title: Validate phone number format

              - invalid_count(number_cars_owned) = 0:
                  valid min: 1
                  valid max: 6
                  attributes:
                    category: Validity
                    title: Ensure number of cars owned is between 1 and 6

              - duplicate_count(phone) = 0:
                  attributes:
                    category: Uniqueness
                    title: Ensure no duplicate phone numbers

            profile:
              columns:
                - "*"
            engine: minerva

          - dataset: dataos://lakehouse:retail/customer_360
            checks:
              - row_count between 10 and 1000:
                  attributes:
                    category: Accuracy
                    title: Validate record count range for customer_360
              - missing_count(birth_date) = 0:
                  attributes:
                    category: Completeness
                    title: Ensure birth_date is populated
              - invalid_percent(phone) < 1%:
                  valid format: phone number
                  attributes:
                    category: Validity
                    title: Check phone number format accuracy
              - invalid_count(number_cars_owned) = 0:
                  valid min: 1
                  valid max: 6
                  attributes:
                    category: Validity
                    title: Verify number_cars_owned value range
              - duplicate_count(phone) = 0:
                  attributes:
                    category: Uniqueness
                    title: Detect duplicate phone entries

            profile:
              columns:
                - "*"
```


## Attribute Details

| **Attribute** | **Description**                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------- |
| **name**    | Defines the workflow name for profiling.                                                                |
| **type**    | Specifies that this configuration represents a workflow.                                                |
| **tags**    | Helps categorize and filter profiling workflows.                                                        |
| **stack**   | Indicates the runtime stack — `soda+python:1.0` combines Soda for checks with Python for orchestration. |
| **dataset** | References the dataset to be profiled.                                                                  |
| **checks**  | Defines various data quality checks to be executed during the profiling run.                            |
| **profile** | Specifies which columns to include in the profiling process. `"*"` means all columns are profiled.      |
| **engine**  | Indicates the query execution engine (`minerva` in this example).                                       |


## Example Use Cases

* Validate completeness of key columns before loading data into analytics tables.
* Detect duplicate or invalid records in CRM or customer datasets.
* Monitor freshness and accuracy of operational data feeds.

