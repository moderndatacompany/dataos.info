# Expire Snapshots


<!-- > Supported in both Flare Stack Versions `flare:3.0` and `flare:4.0`.
>  -->

The `expire_snapshots` [action](/resources/stacks/flare/configurations/#expire_snapshots) expires amassed snapshots. Expiring old snapshots removes them from metadata, so they are no longer available for time travel queries. Data files are not deleted until they are no longer referenced by a snapshot that may be used for time travel or rollback. Regularly expiring snapshots deletes unused data files.

## Code Snippet

The below code snippet depicts a case scenario that expires old snapshots using the `expire_snapshots` action. 
### **Syntax for Flare Version `flare:4.0`**

```yaml
version: v1 # Version
name: wf-expire-snapshots # Name of the Workflow
type: workflow # Type of Resource (Here its workflow)
tags: # Tags
  - expire
workflow: # Workflow Section
  title: expire snapshots # Title of the DAG
  dag: # Directed Acyclic Graph (DAG)
    - name: expire # Name of the Job
      title: expire snapshots # Title of the Job
      spec: # Specs
        tags: # Tags
          - Expire
        stack: flare:6.0 # Stack is Flare (so its a Flare Job)
        compute: runnable-default # Compute
        stackSpec: # Flare Stack specific Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Input Dataset Name
                dataset: dataos://icebase:retail/pos_store_product_cust?acl=rw # Input UDL
                format: Iceberg # Format
            actions: # Action Section
              - name: expire_snapshots # Name of Flare Action
                input: inputDf # Input Dataset Name
                options: # Options
                  expireOlderThan: "1741987433222" # Timestamp in Unix Format (All snapshots older than the timestamp are expired)

```
