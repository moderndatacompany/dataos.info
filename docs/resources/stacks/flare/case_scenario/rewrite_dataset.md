# Rewrite Dataset

DataOS managed depot, Icebase built on top of Iceberg format can compact data files in parallel using Flare’s `rewrite_dataset` [action](/resources/stacks/flare/configurations/#rewrite_dataset). This will combine small files into larger files to reduce metadata overhead and runtime file open costs.

## Code Snippet

The below code snippet depicts a case scenario where using the `rewrite_dataset` action, we have compacted the dataset to the target file size.
### **Syntax for Flare Version `flare:6.0`**

```yaml
version: v1 # Version
name: rewrite # Name of the Workflow
type: workflow # Type of Resource (Here its a workflow)
tags: # Tags
  - Rewrite
workflow: # Workflow Specific Section
  title: Compress iceberg data files # Title of the DAG
  dag: # DAG (Directed Acyclic Graph)
    - name: rewrite # Name of the Job
      title: Compress iceberg data files # Title of the Job
      spec: # Specs
        tags: # Tags
          - Rewrite
        stack: flare:6.0 # Stack Version (Here its Flare stack Version 6.0)
        compute: runnable-default # Compute 
        stackSpec: # Flare Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Name of Input Dataset
                dataset: dataos://icebase:retail/pos_store_product_cust?acl=rw # Dataset UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: rewrite_dataset # Name of the action
                input: inputDf # Input Dataset Name 
                options: # Options
                  properties: # Properties
                    "target-file-size-bytes": "2500048" # Target File Size in Bytes
```
