# Creating your first data pipeline

In this topic, you navigate through the process of building a batch data pipeline using DataOS Resources. By the end of this topic, you'll be able to create and manage efficient batch data pipelines in your own DataOS environment.

## Scenario

As a skilled Data Engineer/data Product Developer, you are presented with a new challenge: your team needs a data pipeline to transfer data from one data source to another. This task involves orchestrating data ingestion, processing, and writing tasks into a seamless pipeline.

## Steps to follow

1. **Identify data sources:** Determine the specific input and output data sources for the pipeline.
2. **Select the right DataOS Resource:** Maps the pipeline requirements to the most appropriate DataOS Resource.
3. **Choose the right Stack:** Select the ideal Stack to handle the pipeline’s data processing needs.
4. **Create a manifest file:** Configure the pipeline using a YAML manifest file.
5. **Apply the manifest file:** Finally, activate the pipeline using the DataOS CLI.


### **Step 1: Identifying the data source**

Begin by identifying the input (Data Source A) and output (Data Source B) for the pipeline. Within DataOS, this involves understanding the characteristics of each data source:

- **Data source A:** An Azure BLOB storage containing raw customer data.
- **Data source B:** A Lakehouse instance for storing processed data in Parquet format.


### **Step 2: Creating Depots**

In DataOS, pipelines can only be created for data sources connected using Depots. You need to ensure that Depots are built on top of the specific data sources. If they are not, please refer to the [Data Source Connectivity Module](/learn/dp_developer_learn_track/data_source_connectivity/), to establish Depots on the specific source system.

### **Step 3: Identifying the right DataOS Resource**

Review the three primary DataOS Resources used for building pipelines in DataOS— Workflow, Service, and Worker — to determine which fits your use case.

| **Characteristic** | **Workflow** | **Service** | **Worker** |
| --- | --- | --- | --- |
| *Overview* | Orchestrates sequences of tasks that terminate upon completion. | A continuous process that serves API requests. | Executes specific tasks indefinitely. |
| *Execution Model* | Batch processing using DAGs. | API-driven execution. | Continuous task execution. |
| *Ideal Use Case* | Batch data processing pipelines and scheduled jobs. | Real-time data retrieval or user interaction. | Event-driven or real-time analytics. |

Given the requirements for a batch pipeline, you can select the Workflow Resource, as it is designed for orchestrating multi-step data processing tasks.

### **Step 4: Identifying the right Stack**

DataOS provides several pre-defined stacks to handle various processing needs. Based on the requirement, you need to select the appropriate processing Stack.

| **Stack** | **Purpose** |
| --- | --- |
| **Scanner** | Extracting metadata from source system |
| **Flare** | Batch data processing. ETL. |
| **Benthos** | Stream processing. |
| **Soda** | Data quality checks. |
| **CLI Stack** | For automated CLI command execution |
|  |  |

here for the given scenario, you can choose the Flare Stack for its robust capabilities in batch data processing. The Flare Stack enables you to efficiently read, process, and write data.


### **Step 4: Creating the manifest file**

After deciding upon the suitable processing Stack, you need to draft the manifest file to configure the pipeline. Specify the Workflow Resource, define the input and output data sources, and integrate the Flare Stack.

```yaml
version: v1  # v1
name: wf-customer-data
type: workflow
tags:
  - crm
description: Ingesting customer data in lakehouse
workflow:
  # schedule:
  #   cron: '00 20 * * *'
  #  # endOn: '2023-12-12T22:00:00Z'
  #   concurrencyPolicy: Forbid
  dag:
    - name: dg-customer-data
      # title: flatten  Data Ingester
      # description: The job ingests Adobe flatten  data from S3 into icebase zone
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
            inputs:
              - name: customer_data
                dataset: dataos://thirdparty:onboarding/customer.csv
                format: csv
                options:
                  inferSchema: true
            logLevel: INFO
            outputs:
              - name: final
                dataset: dataos://lakehouse:customer_relationship_management/customer_data?acl=rw
                format: Iceberg
                options:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                    # partitionSpec:
                    #   - type: day
                    #     column: date_time
                    #     name: day
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
                    


```

### **Step 5: Applying the manifest file**

With the manifest file complete, use the DataOS CLI to deploy the pipeline:

```bash
dataos-ctl apply -f batch-data-pipeline.yaml
```

Verify the pipeline’s activation by checking the status of the Workflow Resource:

```bash
dataos-ctl get -t workflow -w public
```

By the end of this process, you have successfully created a batch data pipeline that automated the transfer of data from PostgreSQL to S3. Ready to take on your next data pipeline challenge? Follow the next steps and start building your own workflows in DataOS!

## Next steps

You are now equipped to handle batch data pipelines efficiently. As you move forward, you can explore additional features and capabilities in DataOS to enhance pipeline robustness and scalability:

- [Pipeline observability](/learn/dp_developer_learn_track/build_pipeline/pipeline_observability/)
- [Scheduling Workflows](/learn/dp_developer_learn_track/build_pipeline/scheduling_workflows/)
- [Data quality checks](/learn/dp_developer_learn_track/build_pipeline/dq_check/)