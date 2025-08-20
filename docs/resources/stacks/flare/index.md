---
title: Flare Stack
search:
  boost: 2
---

# Flare Stack

Flare is a declarative [Stack](/resources/stacks/) for large-scale data processing within DataOS. It leverages a manifest file–based declarative programming paradigm, built as an abstraction over Apache Spark, to provide a comprehensive solution for data ingestion, transformation, enrichment, profiling, quality assessment, and syndication across both batch and streaming data.


!!! tip "Flare Stack in the Data Product Lifecycle"

      The Flare Stack plays a central role in the Data Product Lifecycle within DataOS. Its declarative, manifest-driven design abstracts Apache Spark to streamline high-volume data processing.

      **Key Functions in the Lifecycle:**

      •  **Ingestion and Transformation:** Enables seamless ingestion and transformation of data from diverse sources into the data lake.

      •  **Data Quality Assurance:** Supports validation of datasets against predefined assertions, ensuring data integrity and relevance.

      •  **Batch and Streaming Processing:** Accommodates both real-time data streams and historical datasets through flexible job configurations.

      •  **Operational Optimization:** Executes scheduled maintenance and performance tuning through action jobs.

      Integrating the Flare Stack into the data lifecycle allows DataOS to deliver structured, high-quality data products aligned with organizational requirements. This enables efficient transformation of raw data into actionable assets for business decision-making.


<figure>
  <img src="/resources/stacks/flare/flare_overview.png" alt="Flare Overview" style="width:31rem; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />
  <figcaption><i>Placement of Flare Stack within DataOS</i></figcaption>
</figure>


## Flare Manifest File Syntax

![Flare YAML Configuration Syntax](/resources/stacks/flare/flare_syntax.png)
<center><i>Flare manifest file Configuration Syntax</i></center>

## How to create jobs using Flare Stack

Flare supports both batch and streaming data processing through distinct job types designed to meet varying operational requirements. Detailed instructions for creating Flare Jobs are available in the [Create Flare Jobs](/resources/stacks/flare/creating_flare_jobs/) documentation.


## Types of Flare Jobs

Flare Stack offers varied configuration to execute different types of [Jobs](/resources/stacks/flare/case_scenario/). The details of each job are provided in the table below:


| **Job Type**       | **Description**                                                                                                                                     | **Best Use Case**                                                                 | **Latency**         | **Cost**               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|----------------------|------------------------|
| **Batch Job**      | Processes all data every run, ensuring consistent performance. High latency due to full reprocessing.                                               | Small datasets or full reprocessing needed.                                        | High                 | High (for large data)   |
| **Data Quality Job** | Validates data using user-defined assertions to ensure accuracy and fitness for purpose.                                                          | Business validation, compliance checks.                                            | Medium               | Medium                  |
| **Incremental Job**| Processes only new or changed data since the last run, reducing computation.                                                                       | Large, frequently changing datasets.                                               | Low                  | Low (scales efficiently) |
| **Stream Job**     | Continuously processes real-time data with very low latency requirements.                                                                          | Real-time use cases requiring <1-minute latency.                                   | Very Low             | Very High               |
| **Action Job**     | Executes maintenance actions on Depots using Iceberg format (e.g., compaction, cleanup).                                                           | Data maintenance tasks in Lakehouse or similar Depots.                              | Depends on action     | Depends on action type  |


<!--
### **Batch Job**

Batch Jobs involve recomputing all changed datasets during each run, ensuring consistent end-to-end performance over time. However, they suffer from high latency as all data must be processed, even if it hasn't changed since the last synchronization. When a large volume of new data is introduced, batch jobs can become excessively costly and time-consuming. For smaller data sizes, running batch jobs for various transformation tasks is recommended. However, as data size grows and changes, [incremental jobs](#incremental-job) are a better option. Simple batch jobs typically involve reading data from one Depot (Depot A), performing transformations, and writing the data to another Depot (Depot B). To explore case scenario for a Batch Job, refer to the link: [Case Scenarios: Batch Jobs](/resources/stacks/flare/case_scenario/#batch-jobs).

Apart from regular batch jobs, there are three specialized types of batch jobs designed for specific scenarios: [Data Profiling Jobs](#data-profiling-job), [Data Quality Jobs](#data-quality-job), and [Incremental Jobs](#incremental-job).

#### **Data Profiling Job**

Data Profiling Jobs assess the validity and structure of datasets. These jobs examine source data to determine accuracy, completeness, and validity, providing summaries and insights about the data. Accurate and complete data is essential for making informed decisions based on the available data. Data Profiling Jobs enable you to analyze the structure, content, and relationships within the data, uncovering inconsistencies, and anomalies to achieve higher data quality.
To learn more about creating Data Profiling Jobs, refer to the link: [Case Scenarios: Data Profiling Jobs](/resources/stacks/flare/case_scenario/#data-profiling-job). 

**Fingerprinting**

Initiating a data profiling job for a dataset automatically triggers the fingerprinting process.

Fingerprinting primarily addresses the data classification challenge, aiming to categorize the columns of a table into a predefined categories. Fingerprinting analyzes data columns to detect distinctive patterns or signatures within the data. By examining the data values in a column, it can identify what type of data is there and determine what business terms or labels can be attached to this data. These labels or tags are valuable for enhancing discoverability and enabling effective governance.

To learn more about classification process, refer to [Fingerprinting in DataOS](/resources/stacks/flare/case_scenario/fingerprinting/).

DataOS conducts fingerprinting and stores the classification information for the dataset in Metis DB, which can be accessed through the Metis UI. To learn more, refer to [Fingerprinting Information on Metis UI](/interfaces/metis/navigating_metis_ui_how_to_guide/#how-to-get-fingerprinting-information).

#### **Data Quality Job**

DataOS allows users to define their data quality expectations and discover data shortcomings for the success of data-driven operations. It uses the Flare stack that provides a set of tools and functions for data quality analysis and validation. Flare provides assertions, which are business-specific validation rules, to test and evaluate the quality of specific datasets if they are appropriate for the intended purpose.

Data Quality Jobs measure and ensure data quality based on these assertions. For more information on defining assertions and their properties, refer to [Performing Business Validation Checks with Assertions](/resources/stacks/flare/assertions_case_scenario/). 

#### **Incremental Job**

Incremental Jobs only compute the rows or files of data that have changed since the last build. They are suitable for processing event data and datasets with frequent changes. Incremental jobs reduce overall computation and significantly decrease end-to-end latency compared to batch jobs. Moreover, compute costs for incremental jobs can be lower than batch jobs when dealing with high-scale datasets, as the amount of actual computation is minimized. By processing only new data, incremental jobs eliminate the need to redo analysis on large datasets where most information remains unchanged. For case scenarios on Incremental Jobs, refer to the link: [Case Scenarios: Incremental Jobs](/resources/stacks/flare/case_scenario/#incremental-jobs).

### **Stream Job**

Stream Jobs continuously process incoming data in real-time. They offer low latency but have the highest computing costs, as resources must always be available to handle new input data. Creating stream jobs should be avoided in most cases unless there are strict latency requirements, typically less than a minute. To explore stream-specific properties for Stream Jobs, click here. For a case scenario illustrating how a streaming job is declared within DataOS, refer to the link:[Case Scenario: Stream Jobs](/resources/stacks/flare/case_scenario/#stream-jobs).

### **Action Job**

The DataOS platform provides comprehensive support for executing maintenance actions jobs within the Depots supporting the Iceberg table format such as Lakehouse. These are specified within the actions section. To explore action-specific properties for Action Jobs, click here. For a case scenario illustrating how a action job is declared within DataOS, refer to the link: [Case Scenario: Action Job](/resources/stacks/flare/case_scenario/#flare-actions).

 | Flare Job Type  | Description                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| [Batch Job](/resources/stacks/flare/job_types#batch-job)       | Recomputes all changed datasets on each run, providing consistent performance. Has high latency and is suitable for smaller data sizes.                                              |
| [Data Profiling Job](/resources/stacks/flare/job_types#data-profiling-job) | Assesses data quality and structure, examining source data for accuracy, completeness, and validity.                    |
| [Data Quality Job](/resources/stacks/flare/job_types#data-quality-job) | Evaluates data quality based on business-specific validation rules (assertions).                                                      |
| [Incremental Job](/resources/stacks/flare/job_types#incremental-job) | Computes only the changed rows or files of data since the last build, reducing overall computation and latency.        |
| [Stream Job](/resources/stacks/flare/job_types#stream-job)      | Processes new data continuously with low latency, but incurs high computing costs and requires constant resource availability. |
| [Action Job](/resources/stacks/flare/job_types#action-job)      | Performs maintenance actions on data stored in Iceberg format in any depot (including Lakehouse) | 



Further information regarding Flare Jobs can be accessed [here](/resources/stacks/flare/job_types) -->



## Attributes in Flare Stack manifest configuration

The Flare Stack manifest comprises a wide range of configuration parameters designed to support various use cases. These configurations control how data is read, written, and transformed across multiple source and destination systems. Refer to the [Flare Stack Manifest Configurations](/resources/stacks/flare/configurations/) for detailed documentation.


## Flare functions

Flare provides a comprehensive set of built-in data manipulation functions that can be applied at various stages of job execution. These functions enable the implementation of complex data operations without requiring custom code. For a complete list of supported functions, refer to the [Flare functions reference.Flare functions](/resources/stacks/flare/functions/list/) 

<!-- 
 ## How to test Flare Jobs

Before deploying your logic into production, thorough testing is crucial. Flare Standalone provides a powerful and reliable testing interface, allowing you to test your Flare Jobs locally on your system. It helps identify and address potential issues before deployment. Further information regarding Flare Standalone can be accessed by clicking the link below.

[Flare Standalone](/resources/stacks/flare/standalone/) -->

## Job Optimization in Flare

To ensure optimal performance under different workloads, each job executed on the Flare Stack requires specific tuning and optimization. Refer to [Flare Optimizations](/resources/stacks/flare/optimizations/) for detailed techniques.


## Pre-defined Flare manifest file configuration templates

For a complete list of available Depot connectors in Flare, along with the associated configuration details, see [Flare Configuration Templates](/resources/stacks/flare/configuration_templates/).


## Flare Job Use Cases

To review implementation examples that demonstrate the practical application of the Flare Stack in real-world data processing workflows, refer to the [Case Scenario](/resources/stacks/flare/case_scenario/).

<!-- 
## Troubleshooting in Flare
Flare provides detailed execution metadata and logging to support efficient troubleshooting of job failures and unexpected behavior. Issues can be identified through system-generated logs, job statuses, and validation messages.

For examples of valid configurations and job patterns, refer to the [Flare configuration templates.](/resources/stacks/flare/troubleshooting/)
 -->






