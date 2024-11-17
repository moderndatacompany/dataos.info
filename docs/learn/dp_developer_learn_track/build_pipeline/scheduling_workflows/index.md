# Sheduling Workflows

You understand the importance of efficient and reliable data workflows. When your team faces the challenge of frequent manual updates to keep data pipelines current, it leads to inefficiencies. To streamline this process, you’ll learn how to automate scheduling of data pipelines in DataOS, minimizing manual intervention.

In this topic, you will explore how to set up and manage automated workflows, ensuring data is consistently updated and aligned with business needs. By the end, you’ll be equipped to configure scheduling attributes, use cron expressions, and implement best practices for creating reliable automated workflows in DataOS.

## Prerequisites
Before starting this topic, ensure you have:

- Access to DataOS and the DataOS CLI.

- Permissions to create and manage Workflows and Stacks in your organization’s DataOS instance. Refer here for more details.

## Steps to follow to schedule the Workflow

### **Step 1: Define the Workflow**

Begin by defining your workflow setup:

1. **Choose Workflow Logic**: Identify the specific data tasks like ingestion, transformation, or profiling.
2. **Select Output Format**: Specify the desired output format (e.g., Iceberg).
3. **Identify Source and Destination**: Ensure proper configuration of data sources (e.g., Pulsar topics) and output depots.

### **Step 2: Configure Scheduling Attributes**

Next, configure key scheduling attributes, starting with a cron expression to set execution intervals.

<aside class="callout"> 🗣️ Use a cron expression generator to simplify testing and minimize errors. </aside>
Key attributes include:

1. **cron**: A cron expression defines the timing of workflow executions.
   - **Example**: `/2 * * * *` runs the workflow every 2 minutes.
   - **Common cron fields**:
     - `Minute` (0-59): Use `/2` to specify every 2 minutes.
     - `Hour` (0-23): `*` means any hour.
     - `Day of Month` (1-31), `Month` (1-12), `Day of Week` (0-7): `*` applies to any value.
     
   > **Tip**: Use tools like Cron Expression Generator to test cron expressions.

2. **concurrencyPolicy**: Determines how instances of the workflow behave when overlapping.
   - **Allow**: Multiple workflow instances can run concurrently.
   - **Forbid**: Prevents a new instance from running if a previous instance is still active.
   - **Replace**: Stops the active instance to allow a new instance to start.

3. **endOn**: Specifies when the schedule expires.
   - **Format**: `YYYY-MM-DDTHH:MM:SSZ` (e.g., `2024-11-01T23:40:45Z`).
   - After this date and time, no further instances of the workflow will run.

4. **timezone**: Defines the time zone for the schedule.
   - **Example**: `Asia/Kolkata` schedules executions based on Indian Standard Time (IST).


### **Example Configuration**
To set up a profiling task every 2 minutes, configure your Workflow manifest as follows:

```yaml

# Workflow Scheduling Configuration
cron: '*/2 * * * *' # Executes every 2 minutes
concurrencyPolicy: Allow
endOn: 2024-11-01T23:40:45Z
timezone: Asia/Kolkata
```
#### **Complete Workflow Manifest**

```yaml

# Resource Section
name: scheduled-job-workflow
version: v1
type: workflow
tags:
  - eventhub
  - write
description: Reads data from third party and writes to eventhub
owner: iamgroot
# Workflow-specific Section
workflow:
  title: scheduled 
  schedule: 
    cron: '*/2 * * * *' 
    concurrencyPolicy: Allow 
    endOn: 2024-11-01T23:40:45Z
    timezone: Asia/Kolkata
  dag: 
   - name: write-snowflake-02
     title: Reading data and writing to snowflake
     description: Writes data to snowflake
     spec:
       tags:
         - Connect
         - write
       stack: flare:6.0
       compute: runnable-default
       stackSpec:
         job:
           explain: true
           inputs:
             - name: poros_workflows
               dataset: dataos://systemstreams:poros/workflows
               isStream: true
               options:
                 startingOffsets: earliest
           logLevel: INFO
           outputs:
             - name: poros_workflows
               dataset: dataos://icebase:sys09/poros_workflows_pulsar?acl=rw
               format: Iceberg
               options:
                 saveMode: overwrite
           options: 
               SSL: "true"
               driver: "io.trino.jdbc.TrinoDriver"
               cluster: "system"

```
### **Step 3: Apply the Configuration**
After finalizing the configuration, save it as workflow_schedule.yaml and apply it using the DataOS CLI:

```bash

dataos-ctl apply -f workflow_schedule.yaml -w sandbox
```
Verify the schedule is active by running:

```bash

dataos-ctl get -t workflow -w sandbox

```
## Best Practices
Here are some best practices for scheduling workflows:

1. Enable Retries: Set retries for transient issues to prevent failures.

```yaml

# Resource Section
name: retry-workflow
version: v1
type: workflow
tags:
  - Flare
description: Ingest data into Raw depot

# Workflow-specific Section
workflow:
  title: Demo Ingest Pipeline
  dag:

# Job 1 specific Section
    - name: connect-customer
      file: flare/connect-customer/config_v1.yaml
      retry: # Retry configuration
        count: 2
        strategy: "OnFailure"

# Job 2 specific Section
    - name: connect-customer-dt
      file: flare/connect-customer/dataos-tool_v1.yaml
      dependencies:
        - connect-customer
```
2. Minimize Overlap: Use concurrency policies like Forbid to prevent conflicts in workflows with shared resources.
By following these steps and best practices, you will be able to automate data pipelines effectively, reducing manual interventions and enhancing data reliability.