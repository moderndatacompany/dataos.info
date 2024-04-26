# Fastbase Depot_Scan

DataOS allows you to create a Depot of type 'FASTBASE' to read the topics/messages stored in Pulsar. The created Depot enables you to read the published topics and process incoming stream of messages. You can scan metadata from FASTBASE-type depot with Scanner workflows.

## Requirements

To scan the FASTBASE depot, you need the following:

- Ensure that the depot is created and you have `read` access for the depot.

## Scanner Workflow YAML

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

Create and apply the Scanner YAML. You can run the Scanner workflow with or without a filter pattern. 

```yaml
version: v1
name: fastbase-scanner2
type: workflow
tags:
  - fastbase-scanner2.0
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: scanner2-fastbase
      description: The job scans schema from fastbase depot tables and register metadata to metis2
      spec:
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        scanner:
          depot: fastbase
```

> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI for all topics.
