# Merging Small Files

## Overview
This use case describes Flare job to efficiently perform metadata and data compaction on Iceberg tables. To write values from streaming query to Iceberg table, these queries can create new table versions quickly, which creates lots of table metadata to track those versions. The amount of data written in a micro batch is typically small, which can cause the table metadata to track lots of small files. You can write a Flare job for compacting small files into larger files to reduce the metadata overhead and runtime file open cost. While running at petabyte scale, it is important to increase storage as well as compute efficiency. 


## Solution approach

Iceberg tracks each data file in a table. More data files leads to more metadata stored in manifest files, and small data files causes an unnecessary amount of metadata and less efficient queries.

This example Flare job will compact data/metadata files in Iceberg  with the *rewriteDataFiles* action. 

## Implementation details

The follwoing actions are implemented in the re-write scenario. A workflow is defined with a job that compacts NY taxi data.

You can configure YAML for the following actions. 

### Rewrite manifests

Iceberg may write the new snapshot with a “fast” append that does not automatically compact manifests which could lead to  lots of small manifest files. Manifests can be rewritten to optimize queries and to compact. 

```yaml
---
version: v1beta1
name: com-nytaxi-01
type: workflow
tags:
- Compression
- NyTaxi
description: The job Compress NyTaxi data
workflow:
  title: Compression NyTaxi
  dag:
  - name: com-nytaxi01
    title: Compression NyTaxi
    description: The job Compress NyTaxi data
    spec:
      tags:
      - Compression
      - NyTaxi
      stack: flare:1.0
      flare:
        job:
          explain: true
          inputs:
           - name: ny_taxi
             dataset: dataos://icebase:raw01/ny_taxi_01?acl=r
          logLevel: INFO
          actions:
              - name: rewrite_manifest
                options:
                   specId: ""           # optional
                   stagingLocation: ""  # optional
                   useCaching: false    # optional
          outputs:
            - name: output01
              depot: dataos://icebase:raw01?acl=rw
```

### Expire snapshots
In Iceberg, each micro-batch written to a table produces a new snapshot, which are tracked in table metadata. Snapshots accumulate quickly with frequent commits, so it is highly recommended that tables written by streaming queries are regularly maintained. This action will remove old snapshots and related data files that are no longer needed. 

```yaml
---
version: v1beta1
name: com-nytaxi-01
type: workflow
tags:
- Compression
- NyTaxi
description: The job Compress NyTaxi data
workflow:
  title: Compression NyTaxi
  dag:
  - name: com-nytaxi01
    title: Compression NyTaxi
    description: The job Compress NyTaxi data
    spec:
      tags:
      - Compression
      - NyTaxi
      stack: flare:1.0
      flare:
        job:
          explain: true
          inputs:
           - name: ny_taxi
             dataset: dataos://icebase:raw01/ny_taxi_01?acl=r
          logLevel: INFO
          actions:
             - name: expire_snapshots
               options:
                 expireOlderThan: "1627500040443"   # expire all snapshots older than this timestamp millis.
                 expireSnapshotId: 1343444444       # specific snapshot to expire.
                 retainLast: 3000                   # retail most recent 10 snapshts.
                 streamDeleteResults: false 
                 #By default, all files to delete are brought to the driver at once which may be an issue with very long file lists. Set this to true to use toLocalIterator if you are running into memory issues when collecting the list of files to be deleted.
          outputs:
            - name: output01
              depot: dataos://icebase:raw01?acl=rw
```

### Remove orphan files

This action will remove files which are not referenced in any metadata files of an Iceberg table and can thus be considered “orphaned”.

```yaml
---
version: v1beta1
name: com-nytaxi-01
type: workflow
tags:
- Compression
- NyTaxi
description: The job Compress NyTaxi data
workflow:
  title: Compression NyTaxi
  dag:
  - name: com-nytaxi01
    title: Compression NyTaxi
    description: The job Compress NyTaxi data
    spec:
      tags:
      - Compression
      - NyTaxi
      stack: flare:1.0
      flare:
        job:
          explain: true
          inputs:
           - name: ny_taxi
             dataset: dataos://icebase:raw01/ny_taxi_01?acl=r
          logLevel: INFO
          actions:
             - name: remove_orphans
               options:
                  olderThan: "1627500040443"      # older than this time.
                  location: ""                    # Removes orphan files in the given location.
          outputs:
            - name: output01
              depot: dataos://icebase:raw01?acl=rw
```

### Rewrite dataset
This action will rewrite and compact the generated small data files.

```yaml
---
version: v1beta1
name: com-nytaxi-01
type: workflow
tags:
- Compression
- NyTaxi
description: The job Compress NyTaxi data
workflow:
  title: Compression NyTaxi
  dag:
  - name: com-nytaxi01
    title: Compression NyTaxi
    description: The job Compress NyTaxi data
    spec:
      tags:
      - Compression
      - NyTaxi
      stack: flare:1.0
      flare:
        job:
          explain: true
          inputs:
           - name: ny_taxi
             dataset: dataos://icebase:raw01/ny_taxi_01?acl=r
          logLevel: INFO
          actions:
              - name: rewrite_dataset
                options:
                   filter: "fiter expression here"
                   splitOpenFileCost: 3434343   # Specify the minimum file size to count to pack into one "bin"
                   splitLookback: 3
                   targetSizeInBytes: 54545     # Specify the target rewrite data file size in bytes
                   outputSpecId: 3              
                   # Pass a PartitionSpec id to specify which PartitionSpec should be used in DataFile rewrite
                  caseSensitive: false          # Is it case sensitive
          outputs:
            - name: output01
              depot: dataos://icebase:raw01?acl=rw
```

## Outcomes

if there are  many files in some partition or non partitioned data,  it will merge all small files into a large one.



