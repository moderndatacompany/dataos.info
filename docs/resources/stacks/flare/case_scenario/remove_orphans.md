# Remove Orphans


The `remove_orphans` [action](/resources/stacks/flare/configurations/#remove-orphans) cleans up orphans files older than a specified time period. This action may take a long time to finish if you have lots of files in data and metadata directories. It is recommended to execute this periodically, but you may not need to execute this often. 

<aside>

🗣️ **Note:** It is dangerous to remove orphan files with a retention interval shorter than the time expected for any write to complete because it might corrupt the table if in-progress files are considered orphaned and are deleted. The default interval is 3 days.

</aside>

### **Syntax for Flare Version `flare:4.0`**

```yaml
version: v1 
name: orphans 
type: workflow 
tags: 
  - orphans
workflow: 
  title: Remove orphan files 
  dag: 
    - name: orphans 
      title: Remove orphan files 
      spec: 
        tags: 
          - orphans
        stack: flare:4.0 
        compute: runnable-default 
        flare: 
          job: 
            explain: true 
            logLevel: INFO 
            inputs: 
              - name: inputDf 
                dataset: dataos://icebase:actions/random_users_data 
                format: Iceberg 
            actions: # Flare Action
              - name: remove_orphans # Action Name
                input: inputDf # Input Dataset Name
                options: # Options
                  olderThan: "1674201289720" # Timestamp in Unix Format
```
