# **Query Usage Data Scan**

DataOS Gateway service backed by Gateway DB  keeps query usage data, cluster usage statistics, and dataset usage analytics and harvests required insights such as (heavy datasets, popular datasets, datasets most associated together, etc.). The Scanner workflow connects with the Gateway service to extract query-related data and saves it to MetaStore via the REST API Server.  It also scans information about queries, users, dates, and completion times.

This query history/dataset usage data helps to rank the most used tables.

# **Scanner Workflow for Quality Checks**

The following Scanner workflow is for metadata extraction related to query usage data. It will connect to the gateway service to scan the data and save it to the Metis DB periodically.

# **YAML Configuration**

Here is the complete YAML for scanning the query usage data. 

```yaml
version: v1
name: icebase-depot-query-count
type: workflow
tags:
  - icebase-depot
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: query-count-icebase-depot
      description: The job scans schema from icebase depot tables and register metadata to metis2
      spec:
        tags:
          - scanner2.0
        stack: scanner:2.0
        compute: runnable-default
				runAsUser: metis
        scanner:
          depot: dataos://icebase
          type: usage
          fromPastNumberOfDays: 10
          sourceConfig:
            config:
              schemaFilterPattern:
                includes:
                  - emr_healthcare
              tableFilterPattern:
                includes:
                  - upload
```

## **Metadata on Metis UI**

On a successful run, you can view the query usage data on Metis UI.