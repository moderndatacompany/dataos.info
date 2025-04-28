# Rewrite Manifest Files


When a table’s write pattern doesn’t align with the query pattern, metadata can be rewritten to re-group data files into manifests using `rewrite_manifest` [action](/resources/stacks/flare/configurations/#rewrite_manifest)

## Configurations

| Attribute     | Type    | Description |
|---------------|---------|-------------|
| use_caching   | boolean | Use caching during the operation. Defaults to true. |


## Code Snippet

The below case scenario depicts rewriting manifest files of dataset stored within the Lakehouse Depot using the `rewrite_manifest` action. 

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
        stack: flare:5.0 # Stack is Flare (Here Flare Version is 4.0)
        compute: runnable-default # Compute
        stackSpec: # Flare Stack specific Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Input Dataset Name
                dataset: dataos://lakehouse:retail/pos_store_product_cust?acl=rw # Input UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: rewrite_manifest # Action Name
                input: inputDf # Input Dataset Name
```

## Example 2

The below case scenario depicts rewriting manifest files of dataset stored within the Lakehouse    using the `rewrite_manifest` action with `useCaching` as False. 

```yaml
# this works with flare:5.0
version: v1
name: rewritemanifests
type: workflow
tags:
  - rewritemanifests
  - iceberg
  - actions
description: This workflow rewrite manifests of an iceberg dataset
workflow:
  title: Rewrite Manifests
  dag:
    - name: rewrite_manifests
      title: Rewrite Manifests
      description: This job rewrite manifests of an iceberg dataset
      spec:
        stack: flare:5.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
              - name: input
                dataset: dataos://lakehouse:retail/city
            logLevel: INFO
            actions:
              - name: rewrite_manifest
                input: input
                options:
                  useCaching: false
```