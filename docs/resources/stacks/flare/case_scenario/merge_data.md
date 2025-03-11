# Merge Data

## Case Scenario

This Flare Workflow enables you to merge city data tables from two different locations

## Code Snippets

```yaml
version: v1
name: cnt-city-merge-01
type: workflow
tags:
- Connect
- City
- Merge
description: The job merges new city data from dropzone into existing city data
owner: iamgroot
workflow:
  title: Connect City Merge
  dag:
  - name: city-merge-01
    title: City Dimension Ingester
    description: The job merges new city data from dropzone into existing data
    spec:
      tags:
      - Connect
      - City
      - Merge
      stack: flare:6.0
      compute: runnable-default
      stackSpec:
        job:
          explain: true
          inputs:
           - name: city_connect_merge
             dataset: dataos://thirdparty01:none/city
             format: csv
             schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc

          logLevel: INFO
          outputs:
            - name: merge_data
              dataset: dataos://icebase:retail/city_merge_01?acl=rw
              description: City data ingested from external csv and merged into existing data
              options:
                file:
                  saveMode: Overwrite
                  outputType: CSV
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: none
                    merge:
                      onClause: "old.city_id = new.city_id"
                      whenClause: "MATCHED THEN UPDATE SET old.state_name = new.state_name"
                tags:
                  - Connect
                  - City
                  - Merge
                title: City Source Data

          steps:
            - sequence:
                - name: merge_data
                  doc: Pick all columns from cities and add version as yyyyMMddHHmm formatted
                    timestamp.
                  sql: SELECT * FROM city_connect_merge
```
