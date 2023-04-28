# Incremental Data Workload

## Overview

This use case describes a scenario where your data source contains a large amount of data that are continuously updated. Reloading the entire data set can be time-consuming. So you want only to read new data from the data source. The incremental load method is more efficient as compared to full data load when working with a huge volume of data.

## Solution approach

Iceberg has snapshotId and timestamp:

- timestamp: It is explicitly specified by the user to specify the scope of consumption. As start_timestamp of reading. 

Iceberg provides the ability to read deltas between start/end commit timestamps on a table and resume reading from the last read end timestamp.

So there are scenarios where the timestamp is used for the incremental read.

## Implementation details

To configure your Flare job for the Incremental read, you need to identify what is new data in an evolving data coming from the data source in Iceberg. This new data needs to be captured and stored on a regular interval. 

Here, we are adding a workflow that reads data incrementally based on commit timestamp.
The ‘start_time’ and ‘end_time’ timestamps are defined and updated using sql query. 

## Outcomes

## Code files
```
workflow:
  dag:
    - name: incremental-read
      title: read cloudevent data into usage datasets
      description: This job transforms cloudevent data into usage datasets
      spec:
        tags:
          - Transformation
        stack: flare:1.0
        tier: connect
        flare:
          job:
            explain: true
            inputs:
              - name: querydata
                dataset: dataos://icebase:sys01/cloudevents?acl=r
                incremental:                                   # configuration for incremental read
                  context: incrinput                           # context name
                  sql: select * from incrinput where time > '$|start_time|' AND time <= '$|end_time|'
                  keys:
                    - name: start_time
                      default: "2021-08-17 00:00:00"
                      #sql: select to_timestamp("2021-08-17 00:00:00")
                      updateFromKey: end_time
                    - name: end_time
                      sql: select current_timestamp()                                                 
            output:                                           # change save mode to append
                sink:
                   outputOptions:
                     saveMode: append

```