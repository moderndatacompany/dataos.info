# Flare Job Types

Flare Jobs are categorized into two primary types: Batch Jobs and Stream Jobs.

## Batch Job

Batch Jobs involve recomputing all changed datasets during each run, ensuring consistent end-to-end performance over time. However, they suffer from high latency as all data must be processed, even if it hasn't changed since the last synchronization. When a large volume of new data is introduced, batch jobs can become excessively costly and time-consuming. For smaller data sizes, running batch jobs for various transformation tasks is recommended. However, as data size grows and changes, incremental jobs are a better option. Simple batch jobs typically involve reading data from one depot (depot A), performing transformations, and writing the data to another depot (depot B). To explore different case scenarios for Batch Jobs, refer to the [here](./case_scenario.md#batch-jobs).

Apart from regular batch jobs, there are three specialized types of batch jobs designed for specific scenarios: Data Profiling Jobs, Data Quality Jobs, and Incremental Jobs.

### **Data Profiling Job**

Data Profiling Jobs assess the validity and structure of datasets. These jobs examine source data to determine accuracy, completeness, and validity, providing summaries and insights about the data. Accurate and complete data is essential for making informed decisions based on the available data. Data Profiling Jobs enable you to analyze the structure, content, and relationships within the data, uncovering inconsistencies, and anomalies to achieve higher data quality. <br>
To learn more about creating Data Profiling Jobs, refer to [here](creating_data_profiling_jobs.md).

#### **Fingerprinting**
When you initiate a data profiling job for your dataset, it automatically triggers the **fingerprinting** process.

Fingerprinting primarily addresses the data classification challenge, aiming to categorize the columns of a table into a predefined categories. Fingerprinting analyzes data columns to detect distinctive patterns or signatures within the data. By examining the data values in a column, it can identify what type of data is there and determine what business terms or labels can be attached to this data. These labels or tags are valuable for enhancing discoverability and enabling effective governance. 

To learn more about classification process, refer to [Fingerprinting in DataOS](./case_scenario/fingerprinting.md).

DataOS conducts fingerprinting and stores the classification information for your dataset in Metis DB, which can be accessed through the Metis UI. To learn more, refer to [Fingerprinting Information on Metis UI](/interfaces/metis/explore_metis_ui/#how-to-get-fingerprinting-information).

### **Data Quality Job**
DataOS allows users to define their data quality expectations and discover data shortcomings for the success of data-driven operations. It uses the Flare stack that provides a set of tools and functions for data quality analysis and validation. Flare provides assertions, which are business-specific validation rules, to test and evaluate the quality of specific datasets if they are appropriate for the intended purpose. 

Data Quality Jobs measure and ensure data quality based on these assertions. For more information on defining assertions and their properties, refer to [Performing Business Validation Checks with Assertions](defining_assertions.md)



### **Incremental Job**

Incremental Jobs only compute the rows or files of data that have changed since the last build. They are suitable for processing event data and datasets with frequent changes. Incremental jobs reduce overall computation and significantly decrease end-to-end latency compared to batch jobs. Moreover, compute costs for incremental jobs can be lower than batch jobs when dealing with high-scale datasets, as the amount of actual computation is minimized. By processing only new data, incremental jobs eliminate the need to redo analysis on large datasets where most information remains unchanged. For case scenarios on Incremental Jobs, refer to [here](./case_scenario/incremental_jobs.md).

## Stream Job

Stream Jobs continuously process incoming data in real-time. They offer low latency but have the highest computing costs, as resources must always be available to handle new input data. Creating stream jobs should be avoided in most cases unless there are strict latency requirements, typically less than a minute. To explore stream-specific properties for Stream Jobs, click [here](./configurations/streaming.md). For a case scenario illustrating how a streaming job is declared within DataOS, refer to [here.](./case_scenario.md#stream-jobs)

## Action Job

The DataOS platform provides comprehensive support for executing maintenance actions jobs within the depots supporting the Iceberg table format such as Icebase. These are specified within the `actions` section. To explore action-specific properties for Action Jobs, click [here](./configurations/actions.md). For a case scenario illustrating how a action job is declared within DataOS, refer to [here](./case_scenario.md#flare-actions).