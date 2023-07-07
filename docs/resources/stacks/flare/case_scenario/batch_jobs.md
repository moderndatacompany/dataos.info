# Batch Jobs

## Case Scenario

In this case scenario, we have a Flare Batch Job in which we read data from one depot, process it, and write it to another depot. To know more about Batch Jobs, click [here](../job_types.md#batch-job)

## Implementation Flow

1. Save the below YAML file to your system
2. Make sure that the read dataset exists in your depots, along with the write depot.
3. Once you have made the changes, simply apply the yaml file using the resource apply command.

## Outcome

The data will be read from `thirdparty01` depot to `icebase` depot, after processing on the Flare Stack. Once the file is written to the Icebase depot, its metadata version will be updated to the latest, with Toolbox Stack. Once the data is written to the depot you can view it on the Metis UI

## Code Snippet

```yaml
version: v1
name: wf-sample-002
type: workflow
tags:
- Connect 2342
- CONNECT
description: The job ingests city data from dropzone into raw zone
workflow:
  title: Connect City
  dag:
  - name: wf-sample-job-001
    title: City Dimension Ingester
    description: The job ingests city data from dropzone into raw zone
    spec:
      tags:
      - Connect
      - City
      stack: flare:3.0
      compute: runnable-default
      flare:
        job:
          explain: true
          logLevel: INFO

          inputs:
           - name: city_connect
             dataset: dataos://thirdparty01:none/city
             format: csv
             schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc

          outputs:
            - name: cities
              dataset: dataos://icebase:retail/city01?acl=rw
              format: Iceberg
              description: City data ingested from external csv
              options:
                saveMode: append
                sort:
                  mode: partition
                  columns:
                    - name: version
                      order: desc
                iceberg:
                  properties:
                    write.format.default: parquet
                    write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: identity
                      column: version
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
                      city_connect

  - name: data-tool-job-001
    spec:
      stack: toolbox
      compute: runnable-default
      toolbox:
        dataset: dataos://icebase:retail/city01
        action:
          name: set_version
          value: latest
    dependencies: wf-sample-job-001
```