# Workflows Data Scan

This Scanner workflow is designed to propel data pipeline metadata into metastore. It communicates with DataOS Poros, an orchestration engine for managing workflows, run for data transformation and movement. This Scanner job scans workflow-related information, execution history, and execution states. The scanner workflow is run at the time of installation and is scheduled to run periodically.

The workflow metadata is useful for tracking changes that occur to data in flight between source and target systems. Pairing this information with data lineage graphs aids impact analysis so it can help to fully understand the repercussion of changes made from source to target systems via data pipelines or implications for quality issues in datasets due to failed executions.

## Scanner Workflow for Pipeline Metadata

The YAML configuration will connect to DataOS Poros and scan the data pipelines(workflows in DataOS).

## YAML Configuration

Here is the complete YAML for scanning the metadata related to workflows in DataOS. 

```yaml
version: v1
name: poros-pipeline-scanner
type: workflow
tags:
  - scanner
  - poros
description: Scan and publish all pipelines from poros to metis.
workflow:
  dag:
    - name: poros-pipeline-scanner
      description: The job scans and publishes all pipelines from poros to metis.
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

You can view the captured information about workflows on Metis UI under `sources`.


> 🗣 You can check Scanner system workflows on Collated app UI under the `workflow > system` section.
