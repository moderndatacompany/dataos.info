# Report Monitor

Report Monitor is suitable when the value you want to match is a string value. E.g. status and run time status of dataOS resource. Report monitor utilizes dataOS API to get the runtime and status of the resources.

**Configuring Report Monitor**

This sample configuration demonstrates how to set up the Report Monitor to generate the incident when a workflow succeed. 

``` yaml
# Resource meta section
name: runtime-monitor
version: v1alpha
type: monitor
tags:
  - dataos:type:resource
  - dataos:layer:user
description: Attention! workflow run is succeeded.
layer: user
monitor:

# Monitor-specific section
  schedule: '*/3 * * * *'
  incident:
    name: workflowrunning
    severity: high
    incidentType: workflowruntime
    
  type: report_monitor
# Report Monitor specification
  report:
    source:
      dataOsInstance:
        path: /collated/api/v1/reports/resources/runtime?id=workflow:v1:scan-data-product-test:public
    conditions:
      - valueComparison:
          observationType: runtime
          valueJqFilter: '.value'
          operator: equals
          value: succeeded
```

To configure the Report Monitor you can test the API using postman by replacing the resource, version, resource name, and workspace, then configure the conditions accordingly. To know more about the specific attributes, [refer to this](/resources/monitor/configuration/).