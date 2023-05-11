# Expire Snapshots

> Supported in both Flare Stack Versions `flare:3.0` and `flare:4.0`.
> 

The `expire_snapshots` [action](../Building%20Blocks%20of%20Flare%20Workflow/Actions.md) expires amassed snapshots. Expiring old snapshots removes them from metadata, so they are no longer available for time travel queries. Data files are not deleted until they are no longer referenced by a snapshot that may be used for time travel or rollback. Regularly expiring snapshots deletes unused data files.

## Code Snippet

The below code snippet depicts a case scenario that expires old snapshots using the `expire_snapshots` action. The `expire_snapshots` action is supported in both Flare Stack Versions `flare:3.0` and `flare:4.0`, though the end result is the same in both cases, the action definition slightly differs in the two versions which are given separately in the YAMLs below.

### Syntax for Flare Version `flare:4.0`

```yaml
version: v1 # Version
name: expire # Name of the Workflow
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
        stack: flare:4.0 # Stack is Flare (so its a Flare Job)
        compute: runnable-default # Compute
        flare: # Flare Stack specific Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Input Dataset Name
                dataset: dataos://icebase:actions/random_users_data?acl=rw # Input UDL
                format: Iceberg # Format
            actions: # Action Section
              - name: expire_snapshots # Name of Flare Action
                input: inputDf # Input Dataset Name
                options: # Options
                  expireOlderThan: "1674201289720" # Timestamp in Unix Format (All snapshots older than the timestamp are expired)
```

### Syntax for Flare Version `flare:3.0`

```yaml
version: v1 # Version
name: expire # Name of the Workflow
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
        stack: flare:3.0 # Stack is Flare (so its a Flare Job)
        compute: runnable-default # Compute
        flare: # Flare Stack specific Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Input Dataset Name
                dataset: dataos://icebase:actions/random_users_data?acl=rw # Input UDL
                format: Iceberg # Format
            actions: # Action Section
              - name: expire_snapshots # Name of Flare Action
                options: # Options
                  expireOlderThan: "1674201289720" # Timestamp in Unix Format (All snapshots older than the timestamp are expired)
```