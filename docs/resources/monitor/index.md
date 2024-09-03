---
title: Monitor
search:
  boost: 4
---

# :resources-monitor: Monitor

The Monitor [Resource](/resources/) is an integral part of DataOS’ Observability system, designed to trigger incidents based on specific [events](/resources/) or metrics. By leveraging the Monitor Resource alongside the [Pager](/resources/pager/) Resource for sending alerts, DataOS users can achieve comprehensive observability and proactive incident management, ensuring high system reliability and performance. To understand the key concepts associated with a Monitor, refer to the following link: [Core Concepts](/resources/monitor/core_concepts/).

## Structure of Monitor manifest

=== "Code"

    ```yaml title="monitor_manifest_structure.yaml"
    # Resource meta section
    name: ${{runtime-monitor}}
    version: ${{v1alpha}}
    type: monitor
    tags:
      - ${{dataos:type:resource}}
      - ${{dataos:layer:user}}
    description: ${{Attention! workflow run is succeeded.}}
    layer: ${{user}}
    monitor:

    # Monitor-specific section
      schedule: ${{'*/3 * * * *'}}
      incident:
        name: ${{workflowrunning}}
        severity: ${{high}}
        incidentType: ${{workflowruntime}}
        
      type: {{report_monitor}}
    # Report Monitor specification
      report:
        source:
          dataOsInstance:
            path: ${{/collated/api/v1/reports/resources/runtime?id=workflow:v1:scan-data-product-test:public}}
        conditions:
          - valueComparison:
              observationType: ${{runtime}}
              valueJqFilter: ${{'.value'}
              operator: ${{equals}}
              value: ${{succeeded}}}
    ```

## First Steps

Monitor Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/monitor/first_steps/).

## Configuration

Monitors can be configured to autoscale and match varying workload demands, reference pre-defined Secrets and Volumes, and more. The specific configurations may vary depending on the use case. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Monitor manifest](/resources/monitor/configurations/).





