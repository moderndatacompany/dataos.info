# Remove Orphans

> Supported in both Flare Stack Version `flare:3.0` and `flare:4.0`.
> 

The `remove_orphans` [action](../Building%20Blocks%20of%20Flare%20Workflow/Actions.md) cleans up orphans files older than a specified time period. This action may take a long time to finish if you have lots of files in data and metadata directories. It is recommended to execute this periodically, but you may not need to execute this often. 

> 🗣️ Note: It is dangerous to remove orphan files with a retention interval shorter than the time expected for any write to complete because it might corrupt the table if in-progress files are considered orphaned and are deleted. The default interval is 3 days.

## Code Snippet

The below code snippet depicts a case scenario that removes orphan files using Flare’s `remove_orphans` action before the timestamp specified in the `olderThan` property. The `remove_orphans` action is supported by both Flare stack versions, i.e. `flare:3.0` and `flare:4.0`, though the two differ in their definitions for 3.0 and 4.0. Both of them are provided below separately.

### Syntax for Flare Version `flare:4.0`

```yaml
version: v1 # Version
name: orphans # Name of the Workflow
type: workflow # Type of Resource (Here its Workflow)
tags: # Tags
  - orphans
workflow: # Workflow Section
  title: Remove orphan files # Title of the DAG
  dag: # Directed Acyclic Graph (DAG)
    - name: orphans # Name of the Job
      title: Remove orphan files # Title of the Job
      spec: # Specs
        tags: # Tags
          - orphans
        stack: flare:4.0 # Stack is Flare (so it's a Flare Job)
        compute: runnable-default # Compute
        flare: # Flare Stack specific section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Input Dataset Name
                dataset: dataos://icebase:actions/random_users_data # Input UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: remove_orphans # Action Name
                input: inputDf # Input Dataset Name
                options: # Options
                  olderThan: "1674201289720" # Timestamp in Unix Format
```

### Syntax for Flare Version `flare:3.0`

```yaml
version: v1 # Version
name: orphans # Name of the Workflow
type: workflow # Type of Resource (Here its Workflow)
tags: # Tags
  - orphans
workflow: # Workflow Section
  title: Remove orphan files # Title of the DAG
  dag: # Directed Acyclic Graph (DAG)
    - name: orphans # Name of the Job
      title: Remove orphan files # Title of the Job
      spec: # Specs
        tags: # Tags
          - orphans
        stack: flare:3.0 # Stack is Flare (so it's a Flare Job)
        compute: runnable-default # Compute
        flare: # Flare Stack specific section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Input Dataset Name
                dataset: dataos://icebase:actions/random_users_data # Input UDL
                format: Iceberg # Dataset Format
            actions: # Flare Action
              - name: remove_orphans # Action Name
                options: # Options
                  olderThan: "1674201289720" # Timestamp in Unix Format
```