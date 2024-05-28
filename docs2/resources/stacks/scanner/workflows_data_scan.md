# Scanner for DataOS Workflows

This Scanner workflow is designed to ingest metadata associated with Workflows into the metastore. It interacts with DataOS Poros, an orchestration engine for managing workflows, which are run for data transformation, movement, profiling, quality checking and metadata scanning. The Scanner job thoroughly scans information pertaining to workflows, their execution history, and current execution states. The scanner workflow is run at the time of installation and is scheduled to run periodically.

This workflow metadata is useful for tracking changes that occur to data in flight between source and target systems. Pairing this information with data lineage graphs aids impact analysis, so it can help to fully understand the repercussion of changes made from source to target systems or implications for quality issues in datasets due to failed executions.

## Scanner Workflow YAML for DataOS Workflows Metadata 
The YAML configuration will connect to DataOS Poros and scan the metadata related to various types of workflows in DataOS.

### YAML Configuration

```yaml
version: v1
name: poros-pipeline-scanner
type: workflow
tags:
  - scanner
  - poros
description: Scan and publish Workflow information from poros to metis.
workflow:
  dag:
    - name: poros-pipeline-scanner
      description: The job scans and publishes Workflow related information from poros to metis.
      spec:
        tags:
          - scanner
          - poros
        resources:
          requests:
            cpu: 2000m
            memory: 2048Mi
          limits:
            cpu: 8800m
            memory: 5024Mi
        stack: scanner:2.0
        compute: runnable-default
        scanner:
          type: poros                   # Scanner type
          source: poros
          sourceConnection:
            config:
              type: Poros
              supportsMetadataExtraction: True
          sourceConfig:
            config:
              type: PipelineMetadata.   # config type
```

## Metadata on Metis UI

You can view the captured information about workflows on Metis UI under `Workflows`.