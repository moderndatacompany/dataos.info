# Batch Jobs

Batch jobs in DataOS are used to recompute all relevant datasets during each execution cycle. This approach guarantees full data refresh and consistency across the pipeline, regardless of the number or type of data changes. Batch processing is appropriate for use cases where complete data recomputation is required on a recurring schedule.

## Use Case

Batch jobs are suitable for:

* Periodic ETL pipelines where all source data must be reprocessed
* Scenarios requiring deterministic, end-to-end recomputation
* Workflows where incremental logic is either unavailable or not preferred

## Execution Pattern

Each batch job follows a consistent operational pattern:

1. **Read** data from one or more source depots
2. **Transform** the data using Flare Stack logic
3. **Write** the output to a target depot

This structure ensures full replacement of the target dataset during each execution.

## Workflow Example

The following example demonstrates a simple Flare batch job that:

* Reads a CSV-formatted dataset from the `thirdparty01` depot
* Applies a SQL transformation using Flare Stack v7.0
* Writes the result to a BigQuery table in the `bqdepot` depot

```yaml
name: bq-write-01
version: v1
type: workflow
tags:
  - bq
  - City
title: Write bq
workflow:
  dag:
    - name: city-write-bq-01
      title: City write bq
      description: This job reads data from Azure and writes to BigQuery
      spec:
        tags:
          - Connect
          - City
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
              - name: city_connect
                dataset: dataos://thirdparty01:none/city
                format: csv
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://bqdepot:dev/city?acl=rw
                format: bigquery
                options:
                  saveMode: overwrite
                  bigquery:
                    temporaryBucket: tmdc-development-new
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect LIMIT 10
```

In this configuration:

* The `city_connect` input references a CSV dataset and its associated schema
* A SQL transformation selects a sample of 10 rows
* The result is written to a BigQuery table using overwrite mode


!!! info "Supported Data Sources"
        
        For examples of different source configurations, refer to the Flare configuration templates.
