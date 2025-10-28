
# Running Soda Checks on a Specific Branch of an Iceberg Dataset

Soda Stack in DataOS allows you to validate data changes via running data quality checks on a **specific branch**. Soda seamlessly integrates with Iceberg to run checks on any branch by specifying the `branchName` parameter in the dataset configuration.

This approach is particularly useful for:

* Validating data during development or staging phases.
* Ensuring schema compatibility across branches.
* Detecting anomalies before committing data to the main branch.


## Sample Workflow Manifest

The following example demonstrates how to configure and run **Soda checks** on a specific Iceberg branch (`b1`) using the **Soda Stack** within DataOS.

```yaml
name: soda-city-01
version: v1
type: workflow
tags:
  - workflow
  - soda-checks
description: Run Soda checks on a specific Iceberg branch
workspace: public

workflow:
  dag:
    - name: soda-job-v2
      title: Soda Sample Test Job
      description: Sample job to run Soda checks using the DataOS SDK
      spec:
        stack: soda+python:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 250m
            memory: 250Mi
          limits:
            cpu: 1000m
            memory: 250Mi
        logLevel: DEBUG # Options: WARNING, ERROR, DEBUG

        stackSpec:
          inputs:
            - dataset: dataos://lakehouse:retail/city?acl=rw
              options:
                branchName: b1  # Specify the Iceberg branch name
                engine: minerva
                clusterName: miniature

              profile:
                columns:
                  - "*"

              checks:
                - row_count between 10 and 1000:
                    attributes:
                      category: Accuracy
                      title: Validate total number of city records

                - missing_count(zip_code) = 0:
                    attributes:
                      category: Completeness
                      title: Ensure all records contain zip_code values

                - invalid_count(zip_code) < 1:
                    valid min: 500
                    valid max: 99403
                    filter: state_code = 'AL'
                    attributes:
                      category: Validity
                      title: Validate zip_code range for state 'AL'

                - duplicate_count(zip_code) = 0:
                    attributes:
                      category: Uniqueness
                      title: Ensure no duplicate zip_code values

                - duplicate_count(zip_code) > 10:
                    attributes:
                      category: Uniqueness
                      title: Identify high duplicate zip_code occurrences

                - duplicate_percent(zip_code) < 0.10:
                    attributes:
                      category: Uniqueness
                      title: Ensure less than 10% duplicate zip_codes

                - failed rows:
                    samples limit: 70
                    fail condition: zip_code < 18 AND zip_code >= 50
                    attributes:
                      category: Validity
                      title: Identify invalid zip_code entries

                - freshness(ts_city) < 1d:
                    attributes:
                      category: Freshness
                      title: Ensure data is updated within the last day

                - schema:
                    name: Confirm that required columns are present
                    warn:
                      when required column missing: [city_name, city_name]
                    fail:
                      when required column missing:
                        - city_id
                        - no_phone
                    attributes:
                      category: Schema validation
                      title: Validate presence of required schema columns

                - schema:
                    fail:
                      when forbidden column present: [Pii*]
                      when wrong column type:
                        state_code: DOUBLE
                    attributes:
                      category: Schema validation
                      title: Validate schema consistency and prevent PII columns
```


## Attribute Details

| **Attribute**      | **Description**                                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **branchName** | Specifies the Iceberg branch on which to execute Soda checks. This allows validation of data changes in isolated environments. |
| **engine**     | Defines the query execution engine — `minerva` in this example.                                                                |
| **profile**    | Generates column-level profiling for the dataset. `"*"` means all columns are included.                                        |
| **checks**     | Defines the Soda checks for accuracy, completeness, validity, uniqueness, freshness, and schema validation.                    |
| **resources**  | Allocates CPU and memory resources for the job.                                                                                |
| **logLevel**   | Controls verbosity for debugging and monitoring (options: `WARNING`, `ERROR`, `DEBUG`).                                        |

