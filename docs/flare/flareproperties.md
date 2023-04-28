Introduction to YAML

YAML is a simple but robust data serialization language. It has just two data structures: 
- sequences (a list) 
- mappings (key and value pairs).

**Sequence (lists)**
---
- Linux
- BSD
- Illumos

**Mapping (key value pairs)**
--- 
version: v1beta1
name: product-demo-01
type: workflow

**These structures can be combined and embedded.**
Sequence of mappings (list of pairs) 
---
-
 CPU: AMD
 RAM: ‘16 GB’
-
 CPU: Intel
 RAM: ‘16 GB’

**Mapping sequences (key with many values)**
---
tags:
  - Connect
  - City
functions:
  - name: rename
    column: id
    asColumn: country_id
  - name: rename
    column: name
    asColumn: country_name
  
**Sequence of sequences (a list of lists)** 
- 
  - pineapple
  - coconut
-
  - umbrella
  - raincoat

**Mapping of mappings**

Joey:
  age: 22
  sex: M
Laura:
  age: 24
  sex: F

job:
  explain: true
  logLevel: INFO

## YAML for Flare Workflow

Here is the skeleton of the YAML for the Flare workflow.
```yaml
version: v1beta1          # Holds the current version of the Flare.
name: cnt-city-demo-01
type: workflow            # The workflows can have one or more jobs,defined in a dag in a sequence   
tags:                     # Labels/keywords attached for access and search
  - tag1                  # Multiple tags defined as an array    
  - tag2
description:              # Description of the workflow
workflow:
  title: title of the workflow  # title of the workflow
  dag:
  - name: 
    title: 
    description: The job ingests customer data from bigquery into raw zone
    spec:
      tags:
      - tag1
      - tag2
      stack: flare:1.0
      flare:
        driver:
          coreLimit: 2400m
          cores: 2
          memory: 3072m
        executor:
          coreLimit: 2400m
          cores: 2
          instances: 2
          memory: 4096m
        job:
          explain: true
          inputs:
           - name: customer_connect
             dataset: dataos://crmbq:demo/customer_profiles
          logLevel: WARN
          outputs:
            - name: output01
              depot: dataos://icebase:retail?acl=rw
          steps:
          - sink:
              - sequenceName: customers
                datasetName: customer
                outputName: output01
                outputType: Iceberg
                description: Customer data ingested from bigquery
                outputOptions:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                    partitionSpec:
                    - type: identity
                      column: version
                tags:
                  - Connect
                  - Customer
                title: Customer Source Data

            sequence:
              - name: customers
                doc: Pick all columns from customers and add version as yyyyMMddHHmm formatted
                  timestamp.
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                  ts_customer FROM customer_connect
                functions:
                  - name: rename
                    column: Id
                    asColumn: id

```


Example:
version: v1beta1
name: cnt-city-demo-01
type: workflow 
