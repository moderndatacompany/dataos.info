# Compression

This section explains how the Flare Workflow is used to compress both Cloud Events and NY Taxi Data.


## Code Snippets

Below is the code snippet demonstrating the compression process for Cloud Events Data.

### **Compressing cloud event data**

```yaml title="compressing_cloud_event_data.yml"
version: v1
name: comcloudevent-01
type: workflow
tags:
- Compression
- Cloudevent
description: The job Compress Cloudevent data
workflow:
  title: Compression Cloudevent
  dag:
  - name: compressioncloudevent01
    title: Compression Cloudevent
    description: The job Compress Cloudevent data
    spec:
      tags:
      - Compression
      - Cloudevent
      stack: flare:6.0
      compute: runnable-default
      stackSpec:
        driver:
          coreLimit: 1200m
          cores: 1
          memory: 1024m
        executor:
          coreLimit: 2400m
          cores: 1
          instances: 2
          memory: 2048
        job:
          explain: true
          inputs:
           - name: cloudevents
             dataset: dataos://icebase:sys01/cloudevents

          logLevel: INFO

          actions:
            - name: rewrite_dataset
```

### **Compressing NY Taxi data**

```yaml 
version: v1
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
      stack: flare:6.0
      compute: runnable-default
      stackSpec:
        driver:
          coreLimit: 1200m
          cores: 1
          memory: 1024m
        executor:
          coreLimit: 2400m
          cores: 1
          instances: 1
          memory: 2048
        job:
          explain: true
          inputs:
           - name: ny_taxi
             dataset: dataos://icebase:raw01/ny_taxi_01
          logLevel: INFO
          rewriteDataset:
            mode: full
```