# Remove Orphans


The `remove_orphans` [action](/resources/stacks/flare/configurations/#remove_orphans) cleans up orphans files older than a specified time period. This action may take a long time to finish if you have lots of files in data and metadata directories. It is recommended to execute this periodically, but you may not need to execute this often. 

<aside class="callout">

🗣️ <b>Note:</b> It is dangerous to remove orphan files with a retention interval shorter than the time expected for any write to complete because it might corrupt the table if in-progress files are considered orphaned and are deleted. The default interval is 3 days.

</aside>

**Get the list of snapshots by writing the following command**

```bash
dataos-ctl dataset snapshots -a dataos://icebase:retail/cit
```

**Expected output**


```bash

      SNAPSHOTID      │   TIMESTAMP   │    DATE AND TIME (GMT)     
──────────────────────┼───────────────┼────────────────────────────
  7002479430618666161 │ 1740643647492 │ 2025-02-27T08:07:27+00:00  
  2926095925031493170 │ 1740737372219 │ 2025-02-28T10:09:32+00:00  

```

### **Syntax for Flare Version `flare:6.0`**

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
        stack: flare:6.0 
        compute: runnable-default 
        stackSpec: 
          job: 
            explain: true 
            logLevel: INFO 
            inputs: 
              - name: inputDf 
                dataset: dataos://icebase:retail/city 
                format: Iceberg 
            actions: # Flare Action
              - name: remove_orphans # Action Name
                input: inputDf # Input Dataset Name
                options: # Options
                  olderThan: "1739734172" # Timestamp in Unix Format
```
