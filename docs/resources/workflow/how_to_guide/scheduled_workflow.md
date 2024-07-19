# Scheduled or Cron Workflow

The code snippet below illustrates a sample schedule Workflow for profiling using the [Flare](/resources/stacks/flare/) Stack in output depots with [Iceberg file format with Hadoop Catalog type and REST Metastore.](/resources/depot/#limit-data-sources-file-format). To understand schedule related attribute in details click [here](/resources/workflow/configurations/#schedule).

The following code snippet defines a scheduling configuration for a workflow, setting specific rules for when and how the workflow should execute. Here is an extended description of each attribute in the schedule:

This setup ensures the workflow is triggered every 2 minutes, regardless of the hour, day, month, or weekday.

???tip "Click here to view the code snippet"

    ```yaml title="scheduled_workflow.yml" hl_lines="13-17"
    --8<-- "examples/resources/workflow/scheduled_workflow.yml"
    ```


This code snippet will run the workflow in every 2 minutes on the given date to read data from pulsar topic and write to icebase whose detailed explanation is  given below .

### **`cron: '*/2 * * * *'`**

This cron expression specifies the frequency of the workflow execution. In this case:

*/2 in the minute field means the workflow will run every 2 minutes.

The remaining fields (* * * *) mean that this schedule applies to every hour of the day, every day of the month, every month of the year, and every day of the week.

### **`concurrencyPolicy: Allow`**


- **Allow:** This permits multiple instances of the workflow to run concurrently. If a new instance of the workflow is triggered before the previous one finishes, both will run simultaneously. To know more about different configuration values of concurrencyPolicy attribute click [here](/resources/workflow/configurations/#concurrencyPolicy)

### **`endOn: 2024-11-01T23:40:45Z`**

The endOn attribute defines the expiration time for the schedule. The workflow will continue to execute according to the defined cron schedule until this date and time:

2024-11-01T23:40:45Z indicates that the workflow will stop being triggered after 23:40:45 UTC on November 1, 2024.The time is in Coordinated Universal Time (UTC).

###**`timezone: Asia/Kolkata`**

The timezone attribute specifies the time zone for the cron schedule. Here, Asia/Kolkata is used:

This means that the times specified in the cron expression will be interpreted in the Asia/Kolkata time zone. The Asia/Kolkata time zone is 5 hours and 30 minutes ahead of UTC. 

**Summary**

- The workflow runs every 2 minutes based on Indian Standard Time (IST).

- The workflow continues until 2024-11-02 05:10:45 IST.

- The end time corresponds to 2024-11-01T23:40:45Z in UTC.

- The last scheduled run before the end time will be at 2024-11-02 05:08:00 IST.