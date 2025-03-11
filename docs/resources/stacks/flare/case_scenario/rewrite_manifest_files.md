# Rewrite Manifest Files


When a table’s write pattern doesn’t align with the query pattern, metadata can be rewritten to re-group data files into manifests using Flare stack’s `rewrite_manifest` [action](/resources/stacks/flare/configurations/#rewrite_manifest)

## Code Snippet

The below case scenario depicts rewriting manifest files of dataset stored within the Icebase depot using the `rewrite_manifest` action. 

### **Syntax for Flare Version `flare:6.0`**

```yaml
version: v1 # Version
name: wf-rewrite-manifest # Name of the Workflow
type: workflow # Type of Resource (Here its workflow)
tags: # Tags 
  - manifests
workflow: # Workflow Section
  title: Compress iceberg manifests # Title of the DAG
  dag: # Directed Acyclic Graph (DAG)
    - name: manifest # Name of the Job
      title: Compress iceberg manifests # Title of the Job
      spec: # Specs
        tags: # Tags
          - manifests
        stack: flare:6.0 # Stack is Flare (Here Flare Version is 4.0)
        compute: runnable-default # Compute
        stackSpec: # Flare Stack specific Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Input Dataset Name
                dataset: dataos://icebase:retail/pos_store_product_cust?acl=rw # Input UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: rewrite_manifest # Action Name
                input: inputDf # Input Dataset Name
```
