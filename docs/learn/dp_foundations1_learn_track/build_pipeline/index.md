# Building and Maintaining Data Pipelines

!!! info "Overview"
    In this topic, you’ll learn how to build and maintain data pipelines to deliver reliable data for your Data Products. Your focus will be on maintaining seamless data flow, ensuring data accuracy, and applying the necessary transformations when needed.


DataOS enables you to explore your data without the need to move it. However, there are scenarios where data transformations are necessary to prepare it for use—for example, converting string fields to integers or doubles. In such cases, we ingest the data and apply the required transformations before it can be effectively utilized.

---

## 📘 Scenario

You’re a Data Engineer responsible for transforming raw data into structured datasets for analytics. In this scenario, you're working with CSV files stored in Azure Blob Storage. Your goal is to ingest this raw data into DataOS, apply type conversions (e.g., string to numeric), and prepare it for downstream Data Products.

<aside class="callout">
🗣 
Some steps in this module require permissions typically granted to DataOS Operators. Hence, before diving into building data pipelines, you need to ensure you have the `Operator` tag. Contact the training team for assistance.
</aside>

---

## Steps to build data pipelines

Begin by learning the basics of creating data pipelines in DataOS. This involves understanding the fundamental Resources required to construct a pipeline.

1. **Identify data sources:** Determine the specific input and output data sources for the pipeline.
2. **Select the right DataOS Resource:** Maps the pipeline requirements to the most appropriate DataOS Resource.
3. **Choose the right Stack:** Select the ideal Stack to handle the pipeline’s data processing needs.
4. **Create & apply manifest file:** Configure the pipeline using a YAML manifest file and activate the pipeline using the DataOS CLI..
5. **Check the progress of your Workflow:** Ensure the successful completion of Workflow.
6. **Verify ingested data:** On Workbench, query the data.


### **Step 1: Identify the data source**

Start by identifying the input (Data Source A) and output (Data Source B) data locations for the pipeline. Within DataOS, this involves understanding the characteristics of each data source:

- **Data source A:** An Azure BLOB storage containing raw purchase data in CSV format.
- **Data source B:** A Postgres database for storing processed cu data.

<aside class="callout">
🗣 Ensure you have read access to Data Source A and write access to target Data Source B.
</aside>


### **Step 2: Choose the right DataOS Resource**

DataOS offers three core resources for building pipelines in DataOS— Workflow, Service, and Worker — to determine which fits your use case.

| **Characteristic** | **Workflow** | **Service** | **Worker** |
| --- | --- | --- | --- |
| *Overview* | Orchestrates sequences of tasks that terminate upon completion. | A continuous process that serves API requests. | Executes specific tasks indefinitely. |
| *Execution Model* | Batch processing using DAGs. | API-driven execution. | Continuous task execution. |
| *Ideal Use Case* | Batch data processing pipelines and scheduled jobs. | Real-time data retrieval or user interaction. | Event-driven or real-time analytics. |

> For this scenario, select the Workflow resource (batch processing).

### **Step 3: Identify the right Stack**

Here are the available Stacks to handle various processing needs. 

| **Stack** | **Purpose** |
| --- | --- |
| **Scanner** | Extracting metadata from source system |
| **Flare** | Batch data processing. ETL. |
| **Bento** | Stream processing. |
| **Soda** | Data quality checks. |


> For the given scenario, you can choose the Flare Stack for its robust capabilities in batch data processing with SQL transformations. The Flare Stack enables you to efficiently read, process, and write data.


### **Step 4: Create and apply the manifest file**

Prepare your manifest file to configure the pipeline. 

🎯 **Your Actions: **

1. Specify the Workflow Resource, define the input and output data sources, and integrate the Flare Stack. 
2. Customize the SQL query (used for transformations) for your dataset. The provided query in the `steps` section already include transformations like casting string fields to numerical types.
> Carefully review the input & output properties specifying the dataset addresses, to ensure everything is correctly configured before proceeding— this helps avoid issues later in the workflow.


    ```yaml
    # Important: Replace 'abc' with your initials to personalize and distinguish the resource you’ve created.
    version: v1
    name: wf-customer-data-abc
    type: workflow
    workflow:
      dag:
        - name: dg-customer-data
          spec:
            stack: flare:7.0
            compute: runnable-default
            stackSpec:
              inputs:
                - name: customer_data
                  dataset: dataos://thirdparty:onboarding/customer.csv
                  format: csv
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
                  title: Purchase Dataset
                  options:
                    saveMode: overwrite

    ```

3. With the manifest file complete, use the DataOS CLI to deploy the pipeline. Create a dedicated workspace for all your resources. You can create a new workspace using the command. 
    
    ```bash
    dataos-ctl workspace create -n <workspacename>
    ```
    
    To learn more, refer to [Workspaces](https://dataos.info/interfaces/cli/workspace/details/#create).

4. Deploy the workflow in the personal workspace using the following command. This applies only to workspace-level resources. 
    
    ```bash

    dataos-ctl apply -f <filename with path> -w <workspace name>
    ```

5. Check the progress of your Workflow.

    ```bash
    dataos-ctl get -t workflow -w public
    ```
    You can also open the Operations app and ensure the successful completion of Workflow. 

    In case of error, you can refer to the logs to identify the root cause.


6. Verify ingested data.
   
    Go to the Workbench app and query data.

  

> By the end of this process, you have successfully created a batch data pipeline that automated the transfer of customer data from Azure blob storage to PostgreSQL. 

## Troubleshooting

Need help debugging issues like Depot creation failures or ingestion/transformation errors? 
Refer to the [Troubleshooting Guide](/learn/troubleshooting/). You can find information to diagnose and resolve problems.

## Hands on exercise

Ready to take on your next data pipeline challenge? Follow the same steps and start building your own workflows in DataOS to transfer product data for the example use case.

??? "Click here to see Workflow for ingesting Product data from Azure blob storage to PostgreSQL"
    ```yaml
    # Important: Replace 'abc' with your initials to personalize and distinguish the resource you’ve created.
    version: v1
    name: wf-product-data-abc
    type: workflow
    tags:
      - crm
    description: Ingesting product data in lakehouse
    workflow:
      # schedule:
      #   cron: '00 20 * * *'
      #  # endOn: '2023-12-12T22:00:00Z'
      #   concurrencyPolicy: Forbid
      dag:
        - name: dg-product-data
          spec:
            tags:
              - crm
            stack: flare:7.0
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
                  - name: product_data
                    dataset: dataos://thirdparty:onboarding/product.csv?acl=rw
                    format: csv
                    options:
                      inferSchema: true

                steps:
                  - sequence:
                      - name: final
                        sql: >
                          SELECT 
                            CAST(customer_id AS DOUBLE) as customer_id,
                            product_id, 
                            product_category, 
                            product_name, 
                            CAST(price AS DOUBLE) as price
                          FROM product_data
                        
                outputs:
                  - name: final
                    dataset: dataos://postgresabc:public/product_data?acl=rw  
                    # Replace abc with your initials
                    driver: org.postgresql.Driver
                    format: jdbc
                    title: Product Dataset
                    options:
                      saveMode: overwrite
    ```

## Scheduling Workflows

You are now equipped to handle batch data pipelines efficiently. As you move forward, you can explore additional features and capabilities in DataOS like scheduling. You can schedule pipelines to run at regular intervals using the schedule: property in the manifest. This helps keep data up to date.

<aside class="callout">
🗣 Only the Workflow resource supports scheduling, the Worker and Service Resource don’t have a defined end.

</aside>

For a detailed guide on setting up and managing pipeline schedules, refer to the link below.

[Topic: Scheduling pipelines](/learn/dp_foundations1_learn_track/build_pipeline/scheduling_workflows/)


## Next step

Now that your pipeline is running smoothly, it’s time to set quality checks using SLOs to ensure your data is accurate and trustworthy.

👉 Refer to this topic: [Define quality checks](/learn/dp_foundations1_learn_track/quality_check/)





