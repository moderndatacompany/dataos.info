# Rewrite Manifest Files


When a table’s write pattern doesn’t align with the query pattern, metadata can be rewritten to re-group data files into manifests using Flare stack’s `rewrite_manifest` [action](/resources/stacks/flare/configurations/#rewrite_manifest)

## Code Snippet

The below case scenario depicts rewriting manifest files of dataset stored within the Icebase depot using the `rewrite_manifest` action. The `rewrite_manifest` action is supported in both Flare Stack Versions `flare:3.0` and `flare:4.0`, though the end result is the same in both cases, the action definition slightly differs in the two versions which are given separately in the YAMLs below.

### **Syntax for Flare Version `flare:4.0`**

```yaml
version: v1 # Version
name: manifest # Name of the Workflow
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
        stack: flare:4.0 # Stack is Flare (Here Flare Version is 4.0)
        compute: runnable-default # Compute
        flare: # Flare Stack specific Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Input Dataset Name
                dataset: dataos://icebase:actions/random_users_data?acl=rw # Input UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: rewrite_manifest # Action Name
                input: inputDf # Input Dataset Name
```

### **Syntax for Flare Version `flare:3.0`**

```yaml
version: v1 # Version
name: manifest # Name of the Workflow
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
        stack: flare:3.0 # Stack is Flare (Here Flare Version is 4.0)
        compute: runnable-default # Compute
        flare: # Flare Stack specific Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Input Dataset Name
                dataset: dataos://icebase:actions/random_users_data?acl=rw # Input UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: rewrite_manifest # Action Name
```
