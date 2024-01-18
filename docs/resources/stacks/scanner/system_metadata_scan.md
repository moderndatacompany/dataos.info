# Scanner for Users Info
This scanner periodically scans the icebase and Fastbase and stores metadata related to tables and topics in Metis DB. 

## Scanner Workflow YAML 

The given YAML will scan the user-related information from Heimdall.

### **YAML Configuration**

```yaml
name: system-metadata-sync
version: v1
type: workflow
tags:
  - icebase
  - fastbase
  - profile
  - scanner
description: Icebase, fastbase metadata scanner workflow
owner: metis
workspace: system
workflow:
  title: Icebase and Fastbase Depot Scanner
  schedule:
    cron: '*/30 * * * *'
    timezone: UTC
    concurrencyPolicy: Forbid
  dag:
    - name: icebase-scanner
      description: The job scans and publishes all datasets from icebase to metis.
      spec:
        stack: scanner:2.0
        logLevel: INFO
        compute: runnable-default
        resources:
          requests:
            cpu: 250m
            memory: 512Mi
          limits: {}
        runAsApiKey: >-
          ****************************************************************************
        runAsUser: metis
        stackSpec:
          depot: icebase
          sourceConfig:
            config:
              markDeletedTables: true
    - name: fastbase-scanner
      description: The job scans and publishes all datasets from fastbase to metis.
      spec:
        stack: scanner:2.0
        logLevel: INFO
        compute: runnable-default
        resources:
          requests:
            cpu: 250m
            memory: 512Mi
          limits:
            cpu: 1100m
            memory: 2048Mi
        runAsApiKey: >-
          ****************************************************************************
        runAsUser: metis
        stackSpec:
          depot: fastbase
stamp: '-bkcu'
generation: 33
uid: a105c747-410c-4edc-9953-bda462e94efd
status: {}
```
## Metadata on Metis UI

On a successful run, you can view the scanned metadata on Metis UI under the "Assets" for tables and topics.