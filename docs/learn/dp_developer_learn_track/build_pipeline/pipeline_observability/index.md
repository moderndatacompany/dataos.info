# Pipeline observability

In this topic, you will learn to configure a Report Monitor to generate an incident whenever a workflow succeeds.

## Scenario

Imagine you are a Data Product Developer, tasked with ensuring that workflows run smoothly and incidents are detected promptly. Recently, your team reported delays in identifying when workflows succeed, leading to inefficient responses. Determined to streamline observability, you want to use the **Monitor** **Resource** in DataOS.

## Quick concepts

The Monitor Resource of type Report (or simply Report Monitor) allows you to track specific string values, such as the runtime status of workflows. 

## Configuring Report Monitor

Let us consider that for the given scenario, you decide to configure a Report Monitor for a workflow named `scan-data-product-test`. Your goal is to receive an incident notification every time the workflow status changes to “succeeded.” Here’s how you can set it up:

### Step 1: Define Resource metadata

Begin by defining the metadata for the Monitor Resource. This metadata ensures the monitor is uniquely identifiable and properly tagged.

```yaml
# Resource meta section
name: runtime-monitor
version: v1alpha
type: monitor
tags:
  - dataos:type:resource
  - dataos:layer:user
description: Attention! workflow run is succeeded.
layer: user
```

### Step 2: Specify Monitor configuration

Next, Configure the Monitor-specific section. You can set a schedule to check the workflow status every 3 minutes and defines the incident details to be triggered upon detecting the desired condition.

```yaml
# Monitor-specific section
monitor:
  schedule: '*/3 * * * *'  # Check every 3 minutes
  incident:
    name: workflowrunning
    severity: high
    incidentType: workflowruntime
  type: report_monitor
```

### Step 3: Configure the Report Monitor specification

To track the workflow runtime status, set up the Report Monitor’s `report` specification. You need to use the DataOS API endpoint to fetch runtime details and define the condition to match the “succeeded” status.

```yaml
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

---

## Testing the configuration

Before finalizing the monitor, test the API endpoint using a tool like Postman. Replace placeholders such as resource name, version, and workspace with actual values to ensure the API returns the expected runtime status. Once satisfied, you can proceed to deploy the configuration.

### Deploying the Report Monitor

Now you can apply the YAML configuration using the DataOS CLI:

```bash
dataos-ctl resource apply -f /path/to/runtime-monitor.yaml
```

### Monitoring Workflow success

With the Report Monitor in place, you receive high-severity incident alerts whenever the `scan-data-product-test` workflow succeeds. This ensures that your team can respond promptly, optimizing their operational efficiency.