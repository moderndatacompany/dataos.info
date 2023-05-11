# Basic concepts of Flare Workflow

## Flare Workflow

DataOS uses Flare workflows to carry out large-scale data transformation, ingestion, profiling, syndication, and even a combination of these tasks.
 
<center>

![Picture](./diagram_03.jpg)

</center>

Flare is a declarative stack that can process large-scale data processing workflows using sequential YAML. On the other hand, a workflow is a Primitive/Resource within DataOS that runs a sequence of jobs in a specific order. A workflow is a DAG (Directed Acyclic Graph) of jobs.

> 🗣️ In this section and every subsequent one, when we say Flare workflow, we essentially imply a workflow containing a DAG with a job (or multiple jobs) that uses Flare stack. To submit a job that uses Flare stack (Flare Job), you need to write a Workflow.

## Deep Diving into a Flare Job

A job is a generalized way of defining a transformation task, based on the scenario and use case. Achieving the desired outcome requires the assistance of stacks. Any job is fully reliant on the completion of the job before it. E.g. A Flare Job represents a data processing workload which could be ingestion, transformation, profiling, syndication, etc., running on Flare stack, while in scenarios when the output dataset is to be stored in the Icebase depot, you also need the Toolbox stack along with the Flare Stack. If you would like to learn more about the Toolbox stack, refer to [Toolbox](../../Toolbox.md).

When declaring a Flare Job within a DAG using the YAML structure, it comprises of three sections.: The Input (read data from), the Output (write data to), and the Steps (transformation of data during transit). 
 
<center>

![Picture](./Build.svg)

</center>

## Types of Flare Job

Based on the type of workload, Flare Jobs can be classified into two broad categories:- Batch Jobs and Stream Jobs.

### Batch Job

Batch Job fully recomputes every dataset that has changed on each run, resulting in a consistent end-to-end performance over time. However, they have high latency, as all data must be processed whenever it lands, even if it has not changed since the last sync. If large amounts of new data flow into a Batch Job, they will become expensive and take too long to run. In most cases, running a Batch Job for various transformation tasks is recommended if your data size is small, but as the data size increases and changes, it is best to opt for an incremental job. A simple Batch Job is essentially used to read data from Depot A, perform some transformations, and write data to Depot B. To explore the various case scenarios for a Batch Job, refer to [Batch Job (Ingestion)](../Case%20Scenario/Batch%20Job%20(Ingestion).md).

Based on the purpose of the application, DataOS offers two types of batch jobs used in specific scenarios. They are Data Profiling Jobs and Data Quality Jobs.

### Data Profiling Job

A Data Profiling Job is a process of assessing the quality and structure of the data in the dataset. It examines source data to determine the accuracy, completeness, and validity and summarizes information about that data. It is crucial to know the completeness and correctness of the data to take full advantage of the value and usefulness of the source data available. Inaccurate and incomplete data used for the analysis can lead to incorrect data-driven decisions for any organization.

You can assess your source data quality before using it in critical business scenarios. This will verify the data columns in your dataset are populated with the correct data. Data Profiling Jobs can be used to analyze the structure, content, and relationships within data to uncover patterns, rules, inconsistencies, anomalies, and redundancies to achieve higher data quality. In addition, it uses basic statistics to know about the validity of the data. Click here to learn more about [Data Profiling Jobs](../Case%20Scenario/Data%20Profiling%20Jobs.md).

### Data Quality Job

Data Quality is essential and subjective as different consumers have different notions of it. Within DataOS, we define assertions, which are business-specific validation rules to test and evaluate the quality of specific datasets if they are appropriate for the intended purpose. On top of that, one can measure the data quality. If you want to look at which properties are required for defining the assertions, refer to the page [Assertions](../Building%20Blocks%20of%20Flare%20Workflow/Assertions.md). If you want to check out a case scenario related to Data Quality Jobs, refer to the page [Data Quality Jobs (Assertions)](../Case%20Scenario/Data%20Quality%20Jobs%20(Assertions).md).

### Stream Job

Streaming Jobs run continuously and process new data as it arrives. Therefore, in a streaming job, the latency is very low. Still, it incurs the highest computing costs, requiring resources always to be available to process new input data. Therefore, it is best to avoid creating a streaming job in most cases unless your use case has low latency requirements, like less than a minute. To check out streaming-specific properties for a Stream Job, refer to the page [Streaming](../Building%20Blocks%20of%20Flare%20Workflow/Streaming.md). If you want to see a case scenario, of how a streaming job is declared within DataOS refer to the page [Stream Job](../Case%20Scenario/Stream%20Job.md).

### Incremental Job

In an incremental job, only the rows or files of data that have changed since the last build are computed. This is suitable for processing event data and other datasets with large amounts of data changing over time. In addition to reducing the overall amount of computation, the end-to-end latency of the job can be reduced significantly compared to batch jobs. Compute costs for the incremental jobs can be lower than a batch job on high-scale datasets, as the amount of actual computation occurring can be minimized. Because only new data is processed, incremental jobs avoid needing to redo analysis on large datasets where most information is not changing. To learn more about case scenarios for Incremental Jobs, refer to the page [Incremental Job](../Case%20Scenario/Incremental%20Job.md).