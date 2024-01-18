# Scanner for Data Products

Data product Scanner workflows is for collecting metadata related to Data products such as inputs, outputs, SLOs, policies, lineage and associated DataOS Resources.

This Scanner workflow reads the metadata and stores it in Metis DB. This metadata helps you understand data product's life cycle along with the data access permissions, infrastructure resources used for creating it.

## Scanner Workflow YAML 

The given YAML will scan the data product-related information.

**YAML Configuration**

```yaml
version: v1
name: scanner2-data-product
type: workflow
tags:
  - scanner
  - data-quality
description: The job scans schema tables and register data
workflow:
  # schedule:
  #   cron: '*/20 * * * *'
  #   concurrencyPolicy: Forbid
  dag:
    - name: scanner2-data-product-job
      description: The job scans schema from data-product and register data to metis
      spec:
        tags:
          - scanner2
        stack: scanner:2.0
        compute: runnable-default
        stackSpec:
          type: data-product
          sourceConfig:
            config:
              type: DataProduct
              markDeletedDataProducts: true
              # dataProductFilterPattern:
              #   includes:
              #     - customer-360-all$
```

## Metadata on Metis UI

On a successful run, you can view the Data Product information on Metis UI.