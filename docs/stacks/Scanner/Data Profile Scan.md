# Data Profile Scan

Data profiling tool analyzes the structure, content, and relationships within data to uncover patterns, inconsistencies, anomalies, and redundancies to achieve higher data quality. It uses basic statistics to know about the validity of the data. Flare workflows are run for data profiling on the entire dataset or sample /filtered data. This analysis is stored in Icebase. 

Data profile Scanner workflow reads about these statistics (metadata extraction related to data profiling) and stores it in Metastore. This data helps you find your data's completeness, uniqueness, and correctness for the given dataset.

> 🗣️ Before running the Scanner workflow for metadata, ensure that the profiling and datatool workflows are run successfully.


## Scanner Workflow for Data Profiling Metadata

The YAML configuration will connect to the Icebase depot and scan the data profile-related information.

## YAML Configuration

Here is the complete YAML for scanning the metadata related to data profiling. 

```yaml
version: v1
name: icebase-depot-profile
type: workflow
tags:
  - icebase-scanner2
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: profile-icebase-depot
      description: The job scans schema from icebase depot tables and register metadata to metis2
      spec:
        tags:
          - scanner2.0
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        scanner:
          depot: dataos://icebase
          type: profiler
          sourceConfig:
            config:
              schemaFilterPattern:
                includes:
                  - emr_healthcare
              tableFilterPattern:
                includes:
                  - upload
```

## Metadata on Metis UI

On a successful run, you are able to view the captured data profiling information about the dataset on Metis UI.