# Scanner for Query Usage 

DataOS Gateway service backed by Gateway DB keeps query usage data, and dataset usage analytics and harvests required insights such as (heavy datasets, popular datasets, datasets most associated together, etc.). The Scanner Worker is a continuous running service to extract query-related data and saves it to MetaStore. It scans information about queries, users, dates, and completion times. This query history/dataset usage data helps to rank the most used tables.

The following sample manifest Scanner Worker is for metadata extraction related to query usage data. It reactively reads the queries data published to pulsar topic and ingest it into Metis. It scans information about queries, users, dates, and completion times.

```yaml
name: query-usage-indexer
version: v1beta
type: worker
tags: 
  - Scanner
description: 
  This worker reactively reads the queries data published to pulsar topic and
  ingest it into metis.
owner: metis
workspace: system
worker: 
  title: Query Usage Indexer
  tags: 
    - Scanner
  replicas: 1
  autoScaling: 
    enabled: true
    minReplicas: 1
    maxReplicas: 2
    targetMemoryUtilizationPercentage: 120
    targetCPUUtilizationPercentage: 120
  stack: scanner:2.0
  stackSpec: 
    type: worker
    worker: query_indexer
  logLevel: INFO
  compute: runnable-default
  runAsUser: metis
  
```
The above sample manifest file is deployed using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Scanner YAML}}
```

The extracted metadata can be viewed on the Metis UI. 


**Updating the Scanner Workflow**:

If the Depot or Scanner configurations are updated, the Scanner must be redeployed after deleting the previous instance. Use the following command to delete the existing Scanner:

```bash 
  dataos-ctl delete -f ${{path-to-Scanner-YAML}}]
```

**OR**

```bash
  dataos-ctl delete -t workflow -n ${{name of Scanner}} -w ${{name of workspace}}
```


!!! info "**Best Practice**"

    As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.