# Scheduling Workflows

!!! info "Overview"
    In this topic, you will explore how to set up and manage automated workflows, ensuring data is consistently updated and aligned with business needs. By the end, you’ll be equipped to configure scheduling attributes, use cron expressions, and implement best practices for creating reliable automated workflows in DataOS.

## 📘 Scenario

You understand the importance of efficient and reliable data workflows. When your team faces the challenge of frequent manual updates to keep data pipelines current, it leads to inefficiencies. To streamline this process, you’ll learn how to automate scheduling of data pipelines in DataOS, minimizing manual intervention.

## Prerequisites
Before starting this topic, ensure you have:

- Access to DataOS and the DataOS CLI.

- Permissions to create and manage Workflows and Stacks in your organization’s DataOS instance. Refer here for more details.

## Steps to follow to schedule the Workflow

### **Step 1: Define the Workflow**

Begin by defining your workflow setup:

1. **Choose Workflow logic**: Identify the specific data tasks like ingestion, transformation, or profiling.
2. **Select output format**: Specify the desired output format (e.g., Iceberg).
3. **Identify source and destination**: Ensure proper configuration of data sources (e.g., Pulsar topics) and output depots.

### **Step 2: Configure scheduling attributes**

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


### **Example configuration**
To set up a ingestion workflow to run once daily at 8:00 PM in the specified timezone, configure your Workflow manifest as follows:

```yaml

# Workflow Scheduling Configuration
cron: '00 20 * * *' # Executes daily at 8 pm 
concurrencyPolicy: Forbid
endOn: '2023-12-12T22:00:00Z'
timezone: Asia/Kolkata
```
#### **Complete Workflow manifest**

```yaml

# Important: Replace 'abc' with your initials to personalize and distinguish the resource you’ve created.
version: v1
name: wf-customer-data-abc
type: workflow
tags:
  - crm
description: Ingesting customer data in postgres
workflow:
  schedule:
    cron: '00 20 * * *'
    endOn: '2023-12-12T22:00:00Z'
    concurrencyPolicy: Forbid
    timezone: Asia/Kolkata
  dag:
    - name: dg-customer-data
      spec:
        tags:
          - crm
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 2000m
            cores: 1
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 1
            instances: 1
            memory: 2000m
          job:
            explain: true
            logLevel: INFO
            inputs:
              - name: customer_data
                dataset: dataos://thirdparty:onboarding/customer.csv
                format: csv
                options:
                  inferSchema: true

            steps:
              - sequence:
                  - name: final
                    sql: >
                      SELECT 
                        CAST(customer_id AS LONG)  as customer_id,
                        CAST(birth_year AS LONG) as birth_year,
                        education, 
                        marital_status, 
                        CAST(income AS DOUBLE) as income,
                        country,
                        current_timestamp() as created_at
                      FROM customer_data
                    
            outputs:
              - name: final
                dataset: dataos://postgresabc:public/customer_data?acl=rw
                driver: org.postgresql.Driver
                format: jdbc
                options:
                  saveMode: overwrite
                  



```
### **Step 3: Apply the configuration**
After finalizing the configuration, save it as workflow_schedule.yaml and apply it using the DataOS CLI:

```bash

dataos-ctl apply -f <workflow name> -w sandbox
```
Verify the schedule is active by running:

```bash

dataos-ctl get -t workflow -w sandbox

```
