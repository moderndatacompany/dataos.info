# Scanner for Data Product

Data product Scanner workflows is for collecting metadata related to Data products such as inputs, outputs, SLOs, policies, lineage and associated DataOS Resources.

This Scanner Workflow reads the metadata and stores it in Metis DB. This metadata helps the user to understand data product's life cycle along with the data access permissions, infrastructure resources used for creating it.

!!! info
    The Scanner collects metadata for all Data Products in DataOS. Therefore, it is essential to include a filter regex under `dataProductFilterPattern`.


```yaml
# Workflow metadata
version: v1
name: scanner2-data-product  # Name of the workflow
type: workflow  # Type of the workflow
tags:  # Tags associated with the workflow
  - scanner  # Scanner workflow
  - data-quality  # Data quality workflow
description: The job scans schema tables and register data  # Brief description of the workflow

# Workflow configuration
workflow:
  # Schedule configuration (optional)
  # schedule:
  #   cron: '*/20 * * * *'  # Cron expression for scheduling (e.g., every 20 minutes)
  #   concurrencyPolicy: Forbid  # Concurrency policy (e.g., forbid concurrent runs)

  # Workflow DAG (Directed Acyclic Graph)
  dag:
    - name: scanner2-data-product-job  # Name of the job
      description: The job scans schema from data-product and register data to metis  # Brief description of the job
      spec:
        # Tags associated with the job
        tags:
          - scanner2
        # Stack and compute configuration
        stack: scanner:2.0  # Scanner stack version
        compute: runnable-default  # Compute configuration (e.g., default runner)

        # Stack specification
        stackSpec:
          # Type of the stack
          type: data-product
          # Source configuration
          sourceConfig:
            config:
              # Type of the data product
              type: DataProduct
              # Mark deleted data products as true
              markDeletedDataProducts: true
              # Data product filter pattern (e.g., includes specific data products)
              dataProductFilterPattern:
                includes:
                  - ^customer-360-all$  # Include data products with the specified pattern
```

On a successful run, user can view the Data Product information on Metis UI. The above sample manifest file is deployed using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Scanner YAML}}
```


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