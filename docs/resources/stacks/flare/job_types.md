# Flare Job Types

Flare Jobs are categorized into two primary types: Batch Jobs and Stream Jobs.

## Batch Job

Batch Jobs involve recomputing all changed datasets during each run, ensuring consistent end-to-end performance over time. However, they suffer from high latency as all data must be processed, even if it hasn't changed since the last synchronization. When a large volume of new data is introduced, batch jobs can become excessively costly and time-consuming. For smaller data sizes, running batch jobs for various transformation tasks is recommended. However, as data size grows and changes, incremental jobs are a better option. Simple batch jobs typically involve reading data from one depot (depot A), performing transformations, and writing the data to another depot (depot B). To explore different case scenarios for Batch Jobs, refer to the [here](./case_scenario/batch_jobs.md).

Apart from regular batch jobs, there are three specialized types of batch jobs designed for specific scenarios: Data Profiling Jobs, Data Quality Jobs, and Incremental Jobs.

### **Data Profiling Job**

Data Profiling Jobs assess the quality and structure of datasets. These jobs examine source data to determine accuracy, completeness, and validity, providing summaries and insights about the data. Accurate and complete data is essential for making informed decisions based on the available data. Data Profiling Jobs enable you to analyze the structure, content, and relationships within the data, uncovering patterns, rules, inconsistencies, anomalies, and redundancies to achieve higher data quality. Basic statistics are used to assess data validity. To learn more about Data Profiling Jobs, refer to the [here](./case_scenario/data_profiling_jobs.md).

### **Data Quality Job**

Data Quality is a subjective concept, varying among different consumers. In DataOS, assertions are defined as business-specific validation rules to evaluate the quality of specific datasets for their intended purpose. Data Quality Jobs measure and ensure data quality based on these assertions. For more information on defining assertions and their properties, refer to [here](./configurations/assertions.md). To explore a case scenario related to Data Quality Jobs, click [here](./case_scenario/data_quality_jobs.md).

### **Incremental Job**

Incremental Jobs only compute the rows or files of data that have changed since the last build. They are suitable for processing event data and datasets with frequent changes. Incremental jobs reduce overall computation and significantly decrease end-to-end latency compared to batch jobs. Moreover, compute costs for incremental jobs can be lower than batch jobs when dealing with high-scale datasets, as the amount of actual computation is minimized. By processing only new data, incremental jobs eliminate the need to redo analysis on large datasets where most information remains unchanged. For case scenarios on Incremental Jobs, refer to [here](./case_scenario/incremental_jobs.md).

## Stream Job

Stream Jobs continuously process incoming data in real-time. They offer low latency but have the highest computing costs, as resources must always be available to handle new input data. Creating stream jobs should be avoided in most cases unless there are strict latency requirements, typically less than a minute. To explore stream-specific properties for Stream Jobs, click [here](./configurations/streaming.md). For a case scenario illustrating how a streaming job is declared within DataOS, refer to [here](./case_scenario/stream_jobs.md).

## Action Job

The DataOS platform provides comprehensive support for executing maintenance actions jobs within the depots supporting the Iceberg table format such as Icebase. These are specified within the `actions` section. To explore action-specific properties for Action Jobs, click [here](./configurations/actions.md). For a case scenario illustrating how a action job is declared within DataOS, refer to [here](./case_scenario.md#flare-actions).